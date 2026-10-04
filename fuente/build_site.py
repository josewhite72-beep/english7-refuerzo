# -*- coding: utf-8 -*-
"""Genera la página estática de audios (site/) para GitHub + Vercel. Sin build."""
import json, os, re, shutil, html

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")
book = json.load(open(os.path.join(ROOT, "out", "book.json"), encoding="utf-8"))

def md(t):  # **negrita** y *cursiva* -> HTML
    t = html.escape(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    return re.sub(r"\*(.+?)\*", r"<i>\1</i>", t)

CSS = """
:root{--bg:#fbfaf7;--ink:#1d1d1f;--muted:#5b5b60;--line:#d9d6cf;--card:#fff;--accent:#1f5f8b;--accent-ink:#fff}
@media (prefers-color-scheme:dark){:root{--bg:#141416;--ink:#f2f1ee;--muted:#a9a8a3;--line:#33333a;--card:#1d1d21;--accent:#7fb6dc;--accent-ink:#0d1b24}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
main{max-width:560px;margin:0 auto;padding:20px 16px 48px}
.kicker{font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin:0}
h1{font-size:26px;line-height:1.2;margin:4px 0 6px}h2{font-size:18px;margin:28px 0 8px}
.instr{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px;margin:14px 0}
.play{display:flex;align-items:center;justify-content:center;gap:10px;width:100%;min-height:64px;border:0;border-radius:14px;background:var(--accent);color:var(--accent-ink);font-size:20px;font-weight:700;cursor:pointer}
.row{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:10px}
.btn{min-height:52px;border:1px solid var(--line);border-radius:12px;background:var(--card);color:var(--ink);font-size:16px;font-weight:600;cursor:pointer}
.btn[aria-pressed=true]{border-color:var(--accent);box-shadow:inset 0 0 0 2px var(--accent)}
.bar{height:8px;background:var(--line);border-radius:4px;margin:14px 0 4px;overflow:hidden}.bar i{display:block;height:100%;width:0;background:var(--accent)}
.time{font-size:14px;color:var(--muted);text-align:right;font-variant-numeric:tabular-nums}
details{margin-top:22px;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px}
summary{cursor:pointer;font-weight:600}details p{margin:8px 0}
ul.tracks{list-style:none;padding:0;margin:0}ul.tracks a{display:flex;gap:12px;align-items:baseline;padding:12px 4px;border-bottom:1px solid var(--line);color:var(--ink);text-decoration:none}
ul.tracks b{color:var(--accent);min-width:64px}
.foot{margin-top:36px;font-size:13px;color:var(--muted)}a{color:var(--accent)}
"""

PLAYER_JS = """
const a=document.getElementById('a'),play=document.getElementById('play'),bar=document.querySelector('.bar i'),tm=document.getElementById('tm');
const src={normal:a.dataset.normal,slow:a.dataset.slow};let mode='normal';
const fmt=s=>isFinite(s)?Math.floor(s/60)+':'+String(Math.floor(s%60)).padStart(2,'0'):'0:00';
function setLabel(){play.textContent=a.paused?'▶  Reproducir':'❚❚  Pausa'}
play.onclick=()=>{a.paused?a.play():a.pause()};a.onplay=a.onpause=a.onended=setLabel;
a.onloadedmetadata=a.ontimeupdate=()=>{bar.style.width=(a.currentTime/a.duration*100||0)+'%';tm.textContent=fmt(a.currentTime)+' / '+fmt(a.duration)};
document.getElementById('restart').onclick=()=>{a.currentTime=0;a.play()};
document.querySelectorAll('[data-speed]').forEach(b=>b.onclick=()=>{if(b.dataset.speed===mode)return;mode=b.dataset.speed;
 document.querySelectorAll('[data-speed]').forEach(x=>x.setAttribute('aria-pressed',x===b));const was=!a.paused;a.src=src[mode];a.load();if(was)a.play()});
if('serviceWorker' in navigator)navigator.serviceWorker.register('/sw.js');
"""

SW_JS = """// Guarda lo que el estudiante ya abrió para poder escucharlo sin internet
const C='audios-v1';
self.addEventListener('install',e=>self.skipWaiting());
self.addEventListener('activate',e=>e.waitUntil(self.clients.claim()));
self.addEventListener('fetch',e=>{if(e.request.method!=='GET')return;
 e.respondWith(caches.open(C).then(async c=>{try{const r=await fetch(e.request);if(r.ok&&r.status===200)c.put(e.request,r.clone());return r}
 catch(err){const m=await c.match(e.request,{ignoreSearch:true});if(m)return m;throw err}}))});
"""

def page(title, body, depth):
    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title>
<link rel="stylesheet" href="/style.css"><link rel="manifest" href="/manifest.json"><meta name="theme-color" content="#1f5f8b"></head>
<body><main>{body}<p class="foot">English 7 · Libro de refuerzo · I Trimestre — <a href="/">Todos los audios</a></p></main></body></html>"""

def main():
    if os.path.exists(SITE): shutil.rmtree(SITE)
    os.makedirs(SITE)
    open(os.path.join(SITE, "style.css"), "w").write(CSS)
    open(os.path.join(SITE, "player.js"), "w").write(PLAYER_JS)
    open(os.path.join(SITE, "sw.js"), "w").write(SW_JS)
    json.dump({"name": "English 7 · Audios", "short_name": "English 7", "start_url": "/", "display": "standalone",
               "background_color": "#fbfaf7", "theme_color": "#1f5f8b", "lang": "es"},
              open(os.path.join(SITE, "manifest.json"), "w"))
    shutil.copytree(os.path.join(ROOT, "audio"), os.path.join(SITE, "audio"))
    json.dump({"cleanUrls": True, "headers": [{"source": "/audio/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=604800"}]}]},
              open(os.path.join(SITE, "vercel.json"), "w"), indent=2)
    open(os.path.join(SITE, "README.md"), "w").write("# English 7 · Audios del libro de refuerzo\n\nPágina estática (sin build). Cada QR del libro apunta a /<tema>/<pista>, por ejemplo /1-1/04.\nNo cambies los nombres de archivos ni de carpetas: están impresos en los QR.\n")
    themes = {}
    for key, tr in book["tracks"].items():
        theme, n = key.split("/")
        themes.setdefault(theme, {"title": tr["theme_title"], "scenario": tr["scenario"], "tracks": []})["tracks"].append((n, tr))
        label = f"Audio {theme.replace('-', '.')}-{n}"
        body = f"""<p class="kicker">{html.escape(tr['scenario'])} · Theme {theme.split('-')[1]}</p>
<h1>{label}<br>{html.escape(tr['title'])}</h1>
<div class="instr">{md(tr['instr'])}</div>
<audio id="a" preload="metadata" src="/audio/{theme}/{n}.mp3" data-normal="/audio/{theme}/{n}.mp3" data-slow="/audio/{theme}/{n}-slow.mp3"></audio>
<button class="play" id="play">▶  Reproducir</button>
<div class="bar"><i></i></div><div class="time" id="tm">0:00</div>
<div class="row"><button class="btn" data-speed="normal" aria-pressed="true">Velocidad normal</button><button class="btn" data-speed="slow" aria-pressed="false">Velocidad lenta</button></div>
<div class="row"><button class="btn" id="restart" style="grid-column:1/-1">↺  Escuchar desde el inicio</button></div>
<details><summary>Ver el texto del audio</summary><p><i>Ábrelo solo después de responder.</i></p>{''.join(f'<p>{md(l)}</p>' for l in tr['transcript'])}</details>
<script src="/player.js"></script>"""
        d = os.path.join(SITE, theme); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, f"{n}.html"), "w", encoding="utf-8").write(page(f"{label} · {tr['title']}", body, 2))
    idx = ['<p class="kicker">English 7 · Libro de refuerzo · I Trimestre</p><h1>Audios del libro</h1>',
           '<p>Escanea el código QR de tu libro o elige el audio aquí.</p>']
    for theme, th in sorted(themes.items()):
        idx.append(f"<h2>{html.escape(th['scenario'])}<br>Theme {theme.split('-')[1]}: {html.escape(th['title'])}</h2><ul class='tracks'>")
        for n, tr in th["tracks"]:
            idx.append(f"<li><a href='/{theme}/{n}'><b>{theme.replace('-', '.')}-{n}</b><span>{html.escape(tr['title'])}</span></a></li>")
        idx.append("</ul>")
    idx.append("<script>if('serviceWorker' in navigator)navigator.serviceWorker.register('/sw.js')</script>")
    open(os.path.join(SITE, "index.html"), "w", encoding="utf-8").write(page("English 7 · Audios", "".join(idx), 0))
    print("site ok:", sum(len(t["tracks"]) for t in themes.values()), "pistas")

main()
