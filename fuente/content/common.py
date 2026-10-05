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

# ---------------------------------------------------------------- MINI-TESTS ----
# Una sola fuente: el libro (bloques) y la versión en línea (tests.js) salen de estos datos.
# Tipos de pregunta: mc (opciones, a = índice), tf (a = True/False), short (huecos ___ con
# accept = lista por hueco), fix (oración con error, accept = correcciones válidas).
# accept: texto exacto (se normaliza) o "~palabra palabra" = deben aparecer todas.
SKILL_TITLES = {"listening": "Mini-test de Listening", "reading": "Mini-test de Reading", "writing": "Mini-test de Writing",
                "speaking": "Mini-test de Speaking (examen oral)", "mediation": "Mini-test de Mediation"}
LETTERS = "abcdef"

def _q_block(n, q):
    t = q["t"]
    if t == "mc":
        return [ITEMS(f"{n}. {q['q']}"), OPTS(*[f"{LETTERS[i]}) {o}" for i, o in enumerate(q["opts"])])]
    if t == "tf":
        return [ITEMS(f"{n}. {q['q']}    True / False")]
    if t == "fix":
        return [ITEMS(f"{n}. {q['q']}  →  ______________________________")]
    return [ITEMS(f"{n}. {q['q']}")]

def test_blocks(test, audio=None, online=None):
    out = [PB, H2(SKILL_TITLES[test["skill"]]), TIP(*test["tip"])]
    n = 0
    for part in test["parts"]:
        if part.get("intro"): out.append(P(part["intro"]))
        if part.get("audio"): out.append(audio(part["audio"]))
        if part.get("reading"): out.append(READ(part["reading"]["title"], part["reading"]["paras"]))
        if part.get("note"): out.append(NOTE(part["note"][0], *part["note"][1:]))
        for q in part.get("qs", []):
            n += 1
            out += _q_block(n, q)
        op = part.get("open")
        if op:
            if op.get("lines"): out.append(LINES(op["lines"]))
            out.append(P(op.get("check_intro", "Marca un punto por cada casilla:")))
            out.append(checklist(*[c["text"] for c in op["checklist"]]))
    out.append(SCORE(f"Puntaje: ______ / {test['total']}"))
    if online: out.append(online)
    return out

def _strip_dot(s): return s[:-1] if s.endswith(".") else s

def answer_blocks(test):
    sk = test["skill"]
    if sk == "speaking": return []
    lines, n = [], 0
    for part in test["parts"]:
        for q in part.get("qs", []):
            n += 1
            t, exp = q["t"], q.get("exp", "")
            if t == "mc": head = f"**{LETTERS[q['a']]}) {_strip_dot(q['opts'][q['a']])}.**"
            elif t == "tf": head = f"**{'True' if q['a'] else 'False'}.**"
            else: head = q["show"]
            if t == "fix": lines.append(f"{n}. {head}" + (f" ({exp})" if exp else ""))
            else: lines.append(f"{n}. {head}" + (f" {exp}" if exp else ""))
    out = []
    if sk == "writing":
        out += [H3("Writing — Mini-test, Parte A"), ITEMS(*lines)]
        sample = [p["open"]["sample"] for p in test["parts"] if p.get("open")][0]
        out.append(P(f"**Parte B, ejemplo de respuesta:** *{sample}*"))
    elif sk == "mediation":
        samples = [p["open"]["sample"] for p in test["parts"] if p.get("open")]
        out += [H3("Mediation — Mini-test (ejemplos de respuesta)"), ITEMS(*[f"Parte {'AB'[i]}: *{s}*" for i, s in enumerate(samples)])]
    else:
        out += [H3(f"{sk.capitalize()} — Mini-test"), ITEMS(*lines)]
    return out
