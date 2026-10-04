# -*- coding: utf-8 -*-
"""Exporta el contenido a JSON, genera los MP3 (normal y lento) y los QR estáticos."""
import json, os, subprocess, sys, importlib
import numpy as np, soundfile as sf, qrcode

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "content"))
front = importlib.import_module("front")
MODULES = [importlib.import_module(m) for m in sys.argv[1:] or ["repaso", "t11", "t12", "t21", "t22", "referencia"]]
SITE = front.SITE
SPEAKERS = {"af_bella": "Sofía", "am_michael": "Mateo", "am_fenrir": "Kevin"}
TTS_DIR = os.environ.get("TTS_DIR", os.path.join(ROOT, "tts-model"))

def make_qr(theme_id, n):
    path = os.path.join(ROOT, "qr", f"{theme_id}-{n}.png")
    img = qrcode.make(f"https://{SITE}/{theme_id}/{n}", box_size=10, border=2,
                      error_correction=qrcode.constants.ERROR_CORRECT_M)
    img.save(path)
    return path

# Pronunciación de nombres en español (IPA aproximado, como lo diría un hablante en Panamá)
NAMES = {
    "Martínez": "mɑːɹtˈiːnɛs", "David": "dɑːvˈiːd", "Sofía": "soʊfˈiːə", "Ríos": "ɹˈiːoʊs",
    "Penonomé": "pˌɛnoʊnoʊmˈeɪ", "Chiriquí": "tʃˌiːɹiːkˈiː", "Coclé": "koʊklˈeɪ", "Veraguas": "vɛɹˈɑːɡwɑːs",
    "Colón": "koʊlˈoʊn", "Lucía": "luːsˈiːə", "Darién": "dɑːɹjˈɛn", "Mateo": "mɑːtˈeɪoʊ", "Pérez": "pˈɛɹɛs",
    "Bocas": "bˈoʊkɑːs", "Castillo": "kɑːstˈiːjoʊ", "Tablas": "tˈɑːblɑːs", "Antón": "ɑːntˈoʊn", "Tomás": "toʊmˈɑːs", "Chitré": "tʃiːtɹˈeɪ", "Cañas": "kˈɑːnjɑːs", "Gamboa": "ɡɑːmbˈoʊɑː", "Javier": "hɑːvjˈɛɹ", "Elena": "ɛlˈeɪnɑː", "Luis": "luːˈiːs", "San San": "sˈɑːn sˈɑːn", "Sofía Ríos": "soʊfˈiːə ɹˈiːoʊs", "Valle de Antón": "vˈɑːjeɪ deɪ ɑːntˈoʊn", "Las Tablas": "lɑːs tˈɑːblɑːs", "Isla Cañas": "ˈiːslɑː kˈɑːnjɑːs", "Los Santos": "loʊs sˈɑːntoʊs", "Chorrera": "tʃoʊɹˈɛɹɑː", "Emberá": "ɛmbɛɹˈɑː", "Aguadulce": "ˌɑːɡwɑːdˈuːlseɪ",
}
_NAME_PH = {}
def speak(kokoro, text, voice, speed):
    ph = kokoro.tokenizer.phonemize(text, "en-us")
    for name, ipa in sorted(NAMES.items(), key=lambda kv: -len(kv[0])):
        if name in text:
            orig = _NAME_PH.setdefault(name, kokoro.tokenizer.phonemize(name, "en-us"))
            ph = ph.replace(orig, ipa)
    return kokoro.create(ph, voice=voice, speed=speed, is_phonemes=True)

def gen_audio(kokoro, theme_id, track):
    out_dir = os.path.join(ROOT, "audio", theme_id); os.makedirs(out_dir, exist_ok=True)
    for suffix, speed, pause_k in (("", 1.0, 1.0), ("-slow", 0.8, 1.3)):
        mp3 = os.path.join(out_dir, f"{track['n']}{suffix}.mp3")
        if os.path.exists(mp3) and not os.environ.get("FORCE"):
            continue
        parts, sr = [np.zeros(int(24000 * 0.4), dtype=np.float32)], 24000
        prev_voice = None
        for voice, text, pause in track["segments"]:
            a, sr = speak(kokoro, text, voice, speed)
            parts += [a.astype(np.float32), np.zeros(int(sr * pause * pause_k), dtype=np.float32)]
        wav = mp3[:-4] + ".wav"
        sf.write(wav, np.concatenate(parts), sr)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-ac", "1", "-b:a", "48k", mp3], check=True)
        os.remove(wav)

def transcript(track, speakers):
    lines, multi = [], len({v for v, _, _ in track["segments"]}) > 1
    for voice, text, _ in track["segments"]:
        who = speakers.get(voice)
        lines.append(f"**{who}:** {text}" if multi and who else text)
    return lines

def main():
    kokoro = None
    if not os.environ.get("NO_AUDIO"):
        from kokoro_onnx import Kokoro
        kokoro = Kokoro(os.path.join(TTS_DIR, "kokoro.onnx"), os.path.join(TTS_DIR, "voices.bin"))
    book = {"site": SITE, "blocks": list(front.BLOCKS), "tracks": {}}
    for th in MODULES:
        spk = getattr(th, "SPEAKERS", SPEAKERS)
        for tr in getattr(th, "TRACKS", []):
            key = f"{th.THEME_ID}/{tr['n']}"
            make_qr(th.THEME_ID, tr["n"])
            if kokoro: gen_audio(kokoro, th.THEME_ID, tr)
            book["tracks"][key] = {"title": tr["title"], "instr": tr["instr"], "theme": th.THEME_ID,
                                   "theme_title": th.THEME_TITLE, "scenario": th.SCENARIO,
                                   "transcript": transcript(tr, spk)}
        for b in th.BLOCKS:
            if b.get("t") == "transcripts":
                b = {"t": "transcripts", "items": [
                    {"label": f"Audio {th.THEME_ID.replace('-', '.')}-{tr['n']} · {tr['title']}",
                     "lines": transcript(tr, spk)} for tr in th.TRACKS]}
            if (b.get("t") == "theme_cover" or b.get("text") == "Gramática de consulta rápida") and book["blocks"] and book["blocks"][-1].get("t") != "pb":
                book["blocks"].append({"t": "pb"})
            book["blocks"].append(b)
    with open(os.path.join(ROOT, "out", "book.json"), "w", encoding="utf-8") as f:
        json.dump(book, f, ensure_ascii=False, indent=1)
    print("ok", len(book["blocks"]), "blocks,", len(book["tracks"]), "tracks")

main()
