# -*- coding: utf-8 -*-
"""Genera la página estática de audios (site/) para GitHub + Vercel. Sin build."""
import json, os, re, shutil, html, zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")
book = json.load(open(os.path.join(ROOT, "out", "book.json"), encoding="utf-8"))

def md(t):  # **negrita** y *cursiva* -> HTML
    t = html.escape(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    return re.sub(r"\*(.+?)\*", r"<i>\1</i>", t)

THEMES = {
 "papel":   dict(bg="#FAF7F0",ink="#2B2B2B",muted="#5E5A52",line="#DDD6C8",card="#FFFDF8",accent="#2F6690",accent_ink="#FFFFFF",good="#2E7D32",warn="#9A5B00",bad="#B3261E",hl="#FFF0B3"),
 "sepia":   dict(bg="#F4ECD8",ink="#3B2F2F",muted="#6B5B4E",line="#D9CBAE",card="#FAF4E6",accent="#8A4B2A",accent_ink="#FFFFFF",good="#2F6B2F",warn="#8A5A00",bad="#A62B1F",hl="#EFD993"),
 "oscuro":  dict(bg="#1E2127",ink="#E6E1D6",muted="#A3A7AE",line="#3A3F4A",card="#262A32",accent="#7FB6DC",accent_ink="#0D1B24",good="#7CC985",warn="#E0A85A",bad="#EF8A8A",hl="#4A3F12"),
 "pizarra": dict(bg="#23302B",ink="#EDEBE3",muted="#B3BDB6",line="#3E4F48",card="#2B3A34",accent="#F2C14E",accent_ink="#23302B",good="#8FD694",warn="#F0A35E",bad="#F28B82",hl="#5A4A16"),
}
def _vars(t): return ";".join(f"--{k.replace('_','-')}:{v}" for k, v in THEMES[t].items())
THEME_CSS = (f":root{{{_vars('papel')}}}\n@media (prefers-color-scheme:dark){{:root:not([data-theme]){{{_vars('oscuro')}}}}}\n"
             + "\n".join(f"[data-theme={t}]{{{_vars(t)}}}" for t in THEMES))

THEME_JS = """// Selector de colores: se guarda en este dispositivo
(function(){
var K='e7-theme',D=document.documentElement,TC={auto:null,papel:'#FAF7F0',sepia:'#F4ECD8',oscuro:'#1E2127',pizarra:'#23302B'};
var O=[['auto','Automático','Claro u oscuro, según tu celular'],['papel','Papel','Claro, como el libro'],['sepia','Sepia','Claro y cálido, para leer mucho rato'],['oscuro','Oscuro suave','Para estudiar de noche'],['pizarra','Pizarra','Verde pizarra con tiza amarilla']];
function get(){try{return localStorage.getItem(K)||'auto'}catch(e){return 'auto'}}
function apply(t){if(t==='auto')D.removeAttribute('data-theme');else D.setAttribute('data-theme',t);
 var m=document.querySelector('meta[name=theme-color]');if(m)m.content=TC[t]||(matchMedia('(prefers-color-scheme:dark)').matches?'#1E2127':'#FAF7F0')}
apply(get());
var main=document.querySelector('main');if(!main)return;
var bar=document.createElement('div');bar.className='topbar';
var btn=document.createElement('button');btn.className='tbtn';btn.type='button';btn.textContent='🎨 Colores';btn.setAttribute('aria-expanded','false');
var pan=document.createElement('div');pan.className='tpanel';pan.hidden=true;pan.innerHTML='<p>Elige los colores de la página:</p>';
O.forEach(function(o){var b=document.createElement('button');b.type='button';b.className='topt';b.dataset.t=o[0];
 b.innerHTML=(o[0]==='auto'?'<span class="sw half">Aa</span>':'<span class="sw" data-theme="'+o[0]+'">Aa<i></i></span>')+'<span>'+o[1]+'<small>'+o[2]+'</small></span>';
 b.onclick=function(){try{localStorage.setItem(K,o[0])}catch(e){}apply(o[0]);mark()};pan.appendChild(b)});
function mark(){var t=get();pan.querySelectorAll('.topt').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.t===t)})}
function show(v){pan.hidden=!v;btn.setAttribute('aria-expanded',v)}
btn.onclick=function(e){e.stopPropagation();mark();show(pan.hidden)};
pan.onclick=function(e){e.stopPropagation()};
document.addEventListener('click',function(){show(false)});
document.addEventListener('keydown',function(e){if(e.key==='Escape')show(false)});
bar.appendChild(btn);bar.appendChild(pan);main.insertBefore(bar,main.firstChild);
})();
"""

CSS = """
""" + THEME_CSS + """
*{box-sizing:border-box}html{color-scheme:light}html[data-theme=oscuro],html[data-theme=pizarra]{color-scheme:dark}
@media (prefers-color-scheme:dark){html:not([data-theme]){color-scheme:dark}}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
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
.topbar{display:flex;justify-content:flex-end;margin:-8px 0 8px;position:relative}
.tbtn{min-height:40px;padding:0 14px;border:1px solid var(--line);border-radius:20px;background:var(--card);color:var(--ink);font:inherit;font-size:15px;font-weight:600;cursor:pointer}
.tpanel{position:absolute;right:0;top:46px;z-index:20;width:min(320px,calc(100vw - 32px));background:var(--card);color:var(--ink);border:1px solid var(--line);border-radius:14px;padding:12px;box-shadow:0 8px 24px rgba(0,0,0,.25)}
.tpanel[hidden]{display:none}.tpanel p{margin:0 0 8px;font-size:14px;color:var(--muted)}
.topt{display:flex;align-items:center;gap:12px;width:100%;min-height:52px;margin:0 0 6px;padding:6px 10px;border:1px solid var(--line);border-radius:12px;background:transparent;color:var(--ink);font:inherit;font-size:16px;text-align:left;cursor:pointer}
.topt[aria-pressed=true]{border-color:var(--accent);box-shadow:inset 0 0 0 2px var(--accent)}
.sw{flex:none;display:inline-flex;align-items:center;justify-content:center;width:44px;height:36px;border-radius:8px;border:1px solid var(--line);background:var(--bg);color:var(--ink);font-weight:700;font-size:15px}
.sw i{display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--accent);margin-left:4px}
.sw.half{background:linear-gradient(135deg,#FAF7F0 50%,#1E2127 50%);color:transparent}
.topt small{display:block;font-size:13px;color:var(--muted)}
.cta{display:block;margin:18px 0 6px;padding:14px 16px;border-radius:14px;background:var(--accent);color:var(--accent-ink);text-decoration:none;font-weight:700}.cta span{display:block;font-weight:400;font-size:14px;opacity:.9}
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
if('serviceWorker' in navigator&&location.protocol.startsWith('http'))navigator.serviceWorker.register('../sw.js');
"""

SW_JS = """// Guarda lo que el estudiante ya abrió para poder escucharlo sin internet
const C='audios-v1';
self.addEventListener('install',e=>self.skipWaiting());
self.addEventListener('activate',e=>e.waitUntil(self.clients.claim()));
self.addEventListener('fetch',e=>{if(e.request.method!=='GET')return;
 e.respondWith(caches.open(C).then(async c=>{try{const r=await fetch(e.request);if(r.ok&&r.status===200)c.put(e.request,r.clone());return r}
 catch(err){const m=await c.match(e.request,{ignoreSearch:true});if(m)return m;throw err}}))});
"""

def page(title, body, depth, extra_css="", main_cls="", foot=True):
    up = "../" * depth
    css = f'<link rel="stylesheet" href="{up}style.css">' + (f'<link rel="stylesheet" href="{up}{extra_css}">' if extra_css else "")
    ft = f'<p class="foot">English 7 · Libro de refuerzo · I Trimestre — <a href="{up}index.html">Audios</a> · <a href="{up}tests.html">Mini-tests en línea</a></p>' if foot else ""
    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title>
{css}<link rel="manifest" href="{up}manifest.json"><meta name="theme-color" content="#FAF7F0">
<script>try{{var t=localStorage.getItem('e7-theme');if(t&&t!=='auto')document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script></head>
<body><main class="{main_cls}">{body}{ft}</main><script src="{up}theme.js"></script></body></html>"""

def main():
    if os.path.exists(SITE): shutil.rmtree(SITE)
    os.makedirs(SITE)
    open(os.path.join(SITE, "style.css"), "w").write(CSS)
    open(os.path.join(SITE, "player.js"), "w").write(PLAYER_JS)
    open(os.path.join(SITE, "theme.js"), "w", encoding="utf-8").write(THEME_JS)
    open(os.path.join(SITE, "sw.js"), "w").write(SW_JS)
    json.dump({"name": "English 7 · Audios", "short_name": "English 7", "start_url": "/", "display": "standalone",
               "background_color": "#FAF7F0", "theme_color": "#FAF7F0", "lang": "es"},
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
<audio id="a" preload="metadata" src="../audio/{theme}/{n}.mp3" data-normal="../audio/{theme}/{n}.mp3" data-slow="../audio/{theme}/{n}-slow.mp3"></audio>
<button class="play" id="play">▶  Reproducir</button>
<div class="bar"><i></i></div><div class="time" id="tm">0:00</div>
<div class="row"><button class="btn" data-speed="normal" aria-pressed="true">Velocidad normal</button><button class="btn" data-speed="slow" aria-pressed="false">Velocidad lenta</button></div>
<div class="row"><button class="btn" id="restart" style="grid-column:1/-1">↺  Escuchar desde el inicio</button></div>
<details><summary>Ver el texto del audio</summary><p><i>Ábrelo solo después de responder.</i></p>{''.join(f'<p>{md(l)}</p>' for l in tr['transcript'])}</details>
<script src="../player.js"></script>"""
        d = os.path.join(SITE, theme); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, f"{n}.html"), "w", encoding="utf-8").write(page(f"{label} · {tr['title']}", body, 1))
    idx = ['<p class="kicker">English 7 · Libro de refuerzo · I Trimestre</p><h1>Audios del libro</h1>',
           '<p>Escanea el código QR de tu libro o elige el audio aquí.</p>',
           '<a class="cta" href="tests.html">Mini-tests en línea<span>Los 20 mini-tests del libro: se corrigen solos y te explican cada respuesta.</span></a>']
    for theme, th in sorted(themes.items()):
        idx.append(f"<h2>{html.escape(th['scenario'])}<br>Theme {theme.split('-')[1]}: {html.escape(th['title'])}</h2><ul class='tracks'>")
        for n, tr in th["tracks"]:
            idx.append(f"<li><a href='{theme}/{n}.html'><b>{theme.replace('-', '.')}-{n}</b><span>{html.escape(tr['title'])}</span></a></li>")
        idx.append("</ul>")
    idx.append("<script>if('serviceWorker' in navigator&&location.protocol.startsWith('http'))navigator.serviceWorker.register('sw.js')</script>")
    open(os.path.join(SITE, "index.html"), "w", encoding="utf-8").write(page("English 7 · Audios", "".join(idx), 0))
    build_tests()
    build_zip()
    print("site ok:", sum(len(t["tracks"]) for t in themes.values()), "pistas,", sum(len(t["tests"]) for t in book["tests"].values()), "mini-tests")

def build_tests():
    web = os.path.join(ROOT, "web")
    shutil.copy(os.path.join(web, "tests.js"), SITE)
    shutil.copy(os.path.join(web, "tests.css"), SITE)
    with open(os.path.join(SITE, "tests-data.js"), "w", encoding="utf-8") as f:
        f.write("window.TESTS = " + json.dumps(book["tests"], ensure_ascii=False) + ";\n")
    body = '<div id="app"><p>Cargando…</p></div><noscript>Activa JavaScript para usar los mini-tests.</noscript><script src="tests-data.js"></script><script src="tests.js"></script>'
    open(os.path.join(SITE, "tests.html"), "w", encoding="utf-8").write(page("Mini-tests en línea · English 7", body, 0, "tests.css", "wide"))
    for theme, th in book["tests"].items():
        d = os.path.join(SITE, "test", theme); os.makedirs(d, exist_ok=True)
        for sk in th["tests"]:
            url = f"../../tests.html#{theme}/{sk}"
            open(os.path.join(d, f"{sk}.html"), "w", encoding="utf-8").write(
                f'<!doctype html><html lang="es"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0;url={url}">'
                f'<title>Mini-test</title><script>location.replace("{url}")</script></head><body><a href="{url}">Abrir el mini-test</a></body></html>')

def build_zip():
    d = os.path.join(SITE, "descargar"); os.makedirs(d, exist_ok=True)
    leeme = ("ENGLISH 7 · LIBRO DE REFUERZO · I TRIMESTRE\r\n\r\n"
             "1. Descomprime esta carpeta (clic derecho > Extraer todo).\r\n"
             "2. Abre el archivo index.html (audios) o tests.html (mini-tests).\r\n"
             "3. Funciona sin internet. Tu progreso se guarda en este navegador.\r\n")
    with zipfile.ZipFile(os.path.join(d, "english7-refuerzo.zip"), "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("english7-refuerzo/LEEME.txt", leeme)
        for base, _, files in os.walk(SITE):
            rel = os.path.relpath(base, SITE)
            if rel.split(os.sep)[0] in ("descargar", "test"): continue
            for fn in files:
                if fn in ("vercel.json", "README.md", "sw.js", "manifest.json"): continue
                z.write(os.path.join(base, fn), os.path.join("english7-refuerzo", rel, fn) if rel != "." else os.path.join("english7-refuerzo", fn))

main()
