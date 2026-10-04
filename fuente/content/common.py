# -*- coding: utf-8 -*-
"""Helpers compartidos para escribir los temas."""
NAR = "af_heart"

def P(text, **k): return dict({"t": "p", "text": text}, **k)
def H1(text): return {"t": "h1", "text": text}
def H2(text): return {"t": "h2", "text": text}
def H3(text): return {"t": "h3", "text": text}
def ITEMS(*items): return {"t": "items", "items": list(items)}
def OPTS(*opts): return {"t": "opts", "items": list(opts)}
def LINES(n=1): return {"t": "lines", "n": n}
def BULLETS(*items): return {"t": "bullets", "items": list(items)}
def TABLE(widths, header, rows): return {"t": "table", "widths": widths, "header": header, "rows": rows}
def TIP(*lines): return {"t": "box", "title": "Consejo para la prueba", "lines": list(lines)}
def NOTE(title, *lines): return {"t": "box", "title": title, "lines": list(lines)}
def READ(title, paras): return {"t": "reading", "title": title, "paras": list(paras)}
def POEM(lines): return {"t": "poem", "lines": list(lines)}
def SCORE(text): return {"t": "score", "text": text}
PB = {"t": "pb"}

def audio_factory(theme_id, tracks):
    def audio(n):
        t = next(t for t in tracks if t["n"] == n)
        return {"t": "audio", "id": f"{theme_id}/{n}", "title": t["title"]}
    return audio

def vocab_segments(vocab, voice=NAR):
    segs = []
    for w, _, _, ex in vocab:
        segs += [(voice, w.replace(" / ", ", "), 1.2), (voice, ex, 1.6)]
    return segs

def checklist(*items): return BULLETS(*[f"☐ {i}" for i in items])
