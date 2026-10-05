/* Mini-tests en línea — English 7 · Libro de refuerzo
   Datos: window.TESTS (tests-data.js), generado desde fuente/content/tests_*.py
   Funciona en línea (Vercel) y sin internet (carpeta descargada, file://). */
(function () {
  "use strict";
  const DATA = window.TESTS || {};
  const SK = ["listening", "reading", "writing", "speaking", "mediation"];
  const SKN = { listening: "Listening", reading: "Reading", writing: "Writing", speaking: "Speaking", mediation: "Mediation" };
  const SKES = { listening: "Escuchar", reading: "Leer", writing: "Escribir", speaking: "Hablar", mediation: "Ayudar a otros a entender" };
  const app = document.getElementById("app");
  const store = {
    get(k, d) { try { const v = localStorage.getItem("e7:" + k); return v ? JSON.parse(v) : d; } catch (e) { return d; } },
    set(k, v) { try { localStorage.setItem("e7:" + k, JSON.stringify(v)); } catch (e) {} },
    del(k) { try { localStorage.removeItem("e7:" + k); } catch (e) {} },
  };

  // ---------- utilidades ----------
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  function md(s) {
    return esc(s).replace(/\*\*(.+?)\*\*/g, "<b>$1</b>").replace(/\*(.+?)\*/g, "<i>$1</i>");
  }
  const norm = s => String(s).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "")
    .replace(/[’`´]/g, "'").replace(/'/g, "").replace(/[^a-z0-9 ]+/g, " ").replace(/\s+/g, " ").trim();
  function accepts(answer, list) {
    const a = norm(answer);
    if (!a) return false;
    return list.some(x => x.startsWith("~") ? x.slice(1).split(" ").every(k => a.includes(norm(k))) : a === norm(x));
  }
  const LET = "abcdef";
  const el = (tag, cls, html) => { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; };
  const themeLabel = id => id.replace("-", ".");

  // ---------- índice ----------
  function renderIndex() {
    document.title = "Mini-tests en línea · English 7";
    app.innerHTML = "";
    app.append(el("p", "kicker", "English 7 · Libro de refuerzo · I Trimestre"));
    app.append(el("h1", null, "Mini-tests en línea"));
    app.append(el("p", "lead", "Los mismos mini-tests del libro, pero <b>se corrigen solos</b> y te explican cada respuesta. Tu progreso se guarda en este dispositivo."));
    Object.keys(DATA).sort().forEach(tid => {
      const th = DATA[tid];
      const sec = el("section", "theme");
      sec.append(el("h2", null, `<span class="tnum">Tema ${themeLabel(tid)}</span> ${esc(th.title)}`));
      sec.append(el("p", "scen", esc(th.scenario)));
      const grid = el("div", "cards");
      SK.forEach(sk => {
        const t = th.tests[sk]; if (!t) return;
        const best = store.get(`best:${tid}/${sk}`, null);
        const a = el("a", "card");
        a.href = `#${tid}/${sk}`;
        a.innerHTML = `<span class="sk">${SKN[sk]}</span><span class="skes">${SKES[sk]}</span>` +
          (best != null ? `<span class="best ${best / t.total >= 0.8 ? "ok" : best / t.total >= 0.5 ? "mid" : "low"}">Mejor: ${best} / ${t.total}</span>` : `<span class="best none">Sin intentar</span>`);
        grid.append(a);
      });
      sec.append(grid);
      app.append(sec);
    });
    const off = el("section", "offline");
    off.innerHTML = `<h2>Usar sin internet</h2><p>Descarga una vez la carpeta con los audios y los mini-tests. Descomprímela y abre el archivo <b>index.html</b>: funciona sin conexión en una laptop.</p><p><a class="btn" href="descargar/english7-refuerzo.zip" download>Descargar (zip)</a> <a class="btn ghost" href="index.html">Ver los audios</a></p>`;
    app.append(off);
    window.scrollTo(0, 0);
  }

  // ---------- reproductor ----------
  function player(theme, n) {
    const box = el("div", "player");
    const a = new Audio(); a.preload = "metadata";
    const srcs = { normal: `audio/${theme}/${n}.mp3`, slow: `audio/${theme}/${n}-slow.mp3` };
    let mode = "normal", plays = 0; a.src = srcs.normal;
    box.innerHTML = `<div class="prow"><button class="play" type="button">▶ Reproducir</button><div class="pinfo"><div class="bar"><i></i></div><span class="tm">0:00</span></div></div>
      <div class="prow2"><label><input type="checkbox" class="slow"> Velocidad lenta</label><span class="plays"></span></div>`;
    const btn = box.querySelector(".play"), bar = box.querySelector(".bar i"), tm = box.querySelector(".tm"), pl = box.querySelector(".plays");
    const fmt = s => isFinite(s) ? Math.floor(s / 60) + ":" + String(Math.floor(s % 60)).padStart(2, "0") : "0:00";
    const lab = () => btn.textContent = a.paused ? "▶ Reproducir" : "❚❚ Pausa";
    btn.onclick = () => a.paused ? a.play() : a.pause();
    a.onplay = () => { if (a.currentTime < 0.5) { plays++; pl.textContent = `Escuchado ${plays} ${plays === 1 ? "vez" : "veces"}`; } lab(); };
    a.onpause = a.onended = lab;
    a.ontimeupdate = a.onloadedmetadata = () => { bar.style.width = (a.currentTime / a.duration * 100 || 0) + "%"; tm.textContent = fmt(a.currentTime) + " / " + fmt(a.duration); };
    box.querySelector(".slow").onchange = e => { mode = e.target.checked ? "slow" : "normal"; const was = !a.paused; a.src = srcs[mode]; a.load(); if (was) a.play(); };
    box.querySelector(".bar").onclick = e => { if (isFinite(a.duration)) { const r = e.currentTarget.getBoundingClientRect(); a.currentTime = (e.clientX - r.left) / r.width * a.duration; } };
    return box;
  }

  // ---------- grabadora ----------
  function recorder() {
    const box = el("div", "rec");
    if (!(navigator.mediaDevices && window.MediaRecorder)) {
      box.innerHTML = `<p class="muted">Este navegador no permite grabar. Usa la grabadora de tu celular o laptop.</p>`;
      return box;
    }
    box.innerHTML = `<button type="button" class="recbtn">● Grabar mi respuesta</button><span class="recst"></span><div class="takes"></div>`;
    const b = box.querySelector(".recbtn"), st = box.querySelector(".recst"), takes = box.querySelector(".takes");
    let mr = null, chunks = [], t0 = 0, timer = null;
    b.onclick = async () => {
      if (mr && mr.state === "recording") { mr.stop(); return; }
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mr = new MediaRecorder(stream); chunks = [];
        mr.ondataavailable = e => chunks.push(e.data);
        mr.onstop = () => {
          stream.getTracks().forEach(t => t.stop()); clearInterval(timer);
          const url = URL.createObjectURL(new Blob(chunks, { type: mr.mimeType }));
          const row = el("div", "take", `<span>Grabación ${takes.children.length + 1}</span>`);
          const au = document.createElement("audio"); au.controls = true; au.src = url; row.append(au);
          takes.prepend(row); b.textContent = "● Grabar otra vez"; b.classList.remove("on"); st.textContent = "";
        };
        mr.start(); t0 = Date.now(); b.textContent = "■ Detener"; b.classList.add("on");
        timer = setInterval(() => st.textContent = "Grabando… " + Math.floor((Date.now() - t0) / 1000) + " s", 250);
      } catch (e) { st.textContent = "No se pudo usar el micrófono. Revisa el permiso del navegador."; }
    };
    return box;
  }

  // ---------- ayudas para textos abiertos ----------
  function sentences(text) { return text.split(/(?<=[.!?])\s+|\n+/).map(s => s.trim()).filter(s => /[a-z]/i.test(s)); }
  function capsOk(text) { const ss = sentences(text); return ss.length > 0 && ss.every(s => /^[^a-z]*[A-Z0-9¡¿"*(]/.test(s) && /[.!?)"*]$/.test(s)); }
  function autoHint(rule, text) {
    if (!rule || !text.trim()) return null;
    if (rule === "caps") return capsOk(text);
    try { return new RegExp(rule, "is").test(text.toLowerCase()) || new RegExp(rule, "ism").test(text.toLowerCase()); } catch (e) { return null; }
  }

  // ---------- un mini-test ----------
  function renderTest(tid, sk) {
    const th = DATA[tid], t = th && th.tests[sk];
    if (!t) { renderIndex(); return; }
    document.title = `${SKN[sk]} · Tema ${themeLabel(tid)} · English 7`;
    const key = `ans:${tid}/${sk}`, saved = store.get(key, {});
    const save = () => store.set(key, saved);
    app.innerHTML = "";
    const top = el("div", "crumbs", `<a href="#">← Todos los mini-tests</a>`);
    app.append(top);
    app.append(el("p", "kicker", `${esc(th.scenario)} · Tema ${themeLabel(tid)}: ${esc(th.title)}`));
    app.append(el("h1", null, `Mini-test de ${SKN[sk]}${sk === "speaking" ? " (examen oral)" : ""}`));
    const tip = el("div", "tip"); tip.innerHTML = `<b>Consejo para la prueba</b>` + t.tip.map(x => `<p>${md(x)}</p>`).join(""); app.append(tip);

    const graders = []; // funciones que devuelven puntos
    let qn = 0;
    t.parts.forEach((part, pi) => {
      const sec = el("section", "part" + (part.reading ? " has-reading" : ""));
      const left = el("div", "pleft"), right = el("div", "pright");
      if (part.intro) left.append(el("p", "intro", md(part.intro)));
      if (part.audio) left.append(player(tid, part.audio));
      if (part.reading) {
        const r = el("div", "reading"); r.innerHTML = `<h3>${esc(part.reading.title)}</h3>` + part.reading.paras.map(p => `<p>${md(p)}</p>`).join("");
        left.append(r);
      }
      if (part.note) { const n = el("div", "note"); n.innerHTML = `<b>${esc(part.note[0])}</b>` + part.note.slice(1).map(x => `<p>${md(x)}</p>`).join(""); left.append(n); }
      (part.qs || []).forEach(q => {
        qn++; const id = `q${qn}`;
        const box = el("div", "q"); box.dataset.id = id;
        const fb = el("div", "fb");
        if (q.t === "mc" || q.t === "tf") {
          const opts = q.t === "mc" ? q.opts.map((o, i) => [i, `${LET[i]}) ${o}`]) : [[true, "True"], [false, "False"]];
          box.append(el("p", "qt", `<span class="n">${qn}.</span> ${md(q.q)}`));
          const row = el("div", "opts" + (q.t === "tf" ? " tf" : ""));
          opts.forEach(([val, label]) => {
            const b = el("button", "opt", esc(label)); b.type = "button";
            if (saved[id] === val) b.classList.add("sel");
            b.onclick = () => { if (box.classList.contains("done")) return; saved[id] = val; save(); row.querySelectorAll(".opt").forEach(x => x.classList.toggle("sel", x === b)); };
            b.dataset.val = String(val); row.append(b);
          });
          box.append(row);
          graders.push(() => {
            const ok = saved[id] === q.a;
            row.querySelectorAll(".opt").forEach(x => { if (x.dataset.val === String(q.a)) x.classList.add("right"); else if (x.classList.contains("sel")) x.classList.add("wrong"); });
            return ok;
          });
        } else if (q.t === "short") {
          const parts = q.q.split(/_{3,}/); const p = el("p", "qt");
          p.innerHTML = `<span class="n">${qn}.</span> `;
          const inputs = [];
          parts.forEach((txt, i) => {
            p.append(Object.assign(document.createElement("span"), { innerHTML: md(txt) }));
            if (i < parts.length - 1) {
              const inp = el("input", "blank"); inp.type = "text"; inp.autocomplete = "off"; inp.spellcheck = false;
              inp.value = (saved[id] || [])[i] || ""; inp.setAttribute("aria-label", "Respuesta " + qn);
              inp.oninput = () => { const v = saved[id] || []; v[i] = inp.value; saved[id] = v; save(); };
              inputs.push(inp); p.append(inp);
            }
          });
          box.append(p);
          graders.push(() => { const ok = inputs.every((inp, i) => accepts(inp.value, q.accept[i] || q.accept[0])); inputs.forEach(x => x.classList.add(ok ? "right" : "wrong")); return ok; });
        } else if (q.t === "fix") {
          box.append(el("p", "qt", `<span class="n">${qn}.</span> <span class="wrongs">${md(q.q)}</span>`));
          const inp = el("input", "fixin"); inp.type = "text"; inp.placeholder = "Escribe la oración corregida"; inp.autocomplete = "off"; inp.spellcheck = false;
          inp.value = saved[id] || ""; inp.oninput = () => { saved[id] = inp.value; save(); };
          box.append(inp);
          graders.push(() => { const ok = accepts(inp.value, q.accept); inp.classList.add(ok ? "right" : "wrong"); return ok; });
        }
        box.append(fb);
        const g = graders.pop();
        graders.push(() => {
          const v = saved[id], blank = v == null || v === "" || (Array.isArray(v) && !v.some(x => x && String(x).trim()));
          const ok = g();
          box.classList.add("done", ok ? "is-right" : "is-wrong");
          const ans = q.t === "mc" ? `${LET[q.a]}) ${q.opts[q.a]}` : q.t === "tf" ? (q.a ? "True" : "False") : q.show.replace(/\*\*/g, "");
          fb.innerHTML = (ok ? `<b class="ok">✓ ¡Correcto!</b>` : `<b class="no">${blank ? "Sin responder." : "✗"} Respuesta correcta:</b> ${md(q.t === "fix" || q.t === "short" ? q.show : ans)}`) +
            (q.exp ? `<p>${md(q.exp)}</p>` : "");
          box.querySelectorAll("input").forEach(x => x.readOnly = true);
          return ok ? 1 : 0;
        });
        right.append(box);
      });
      const op = part.open;
      if (op) {
        const ob = el("div", "open");
        if (op.record) ob.append(recorder());
        let ta = null;
        if (op.lines) {
          ta = el("textarea", "wr"); ta.rows = Math.max(4, op.lines + 1); ta.placeholder = "Escribe aquí tu respuesta en inglés…";
          ta.value = saved[`o${pi}`] || ""; ta.spellcheck = false;
          const cnt = el("div", "cnt");
          const upd = () => {
            const n = sentences(ta.value).length;
            cnt.textContent = `${n} ${n === 1 ? "oración" : "oraciones"}` + (op.min_sent ? ` · se piden ${op.min_sent === op.max_sent ? op.min_sent : op.min_sent + " a " + op.max_sent}` : "");
            cnt.className = "cnt" + (op.min_sent && n >= op.min_sent && n <= op.max_sent ? " good" : "");
            ob.querySelectorAll(".chk").forEach(c => {
              const h = autoHint(c.dataset.auto, ta.value), hint = c.querySelector(".hint");
              hint.textContent = h == null ? "" : h ? "parece que sí" : "no lo encuentro"; hint.className = "hint " + (h == null ? "" : h ? "yes" : "nope");
            });
          };
          ta.oninput = () => { saved[`o${pi}`] = ta.value; save(); upd(); };
          ob.append(ta, cnt); setTimeout(upd, 0);
        }
        ob.append(el("p", "chkintro", md(op.check_intro || "Marca un punto por cada casilla:")));
        const list = el("div", "checks");
        op.checklist.forEach((c, ci) => {
          const lab = el("label", "chk"); lab.dataset.auto = c.auto || "";
          const cb = el("input"); cb.type = "checkbox"; cb.checked = !!(saved[`c${pi}`] || [])[ci];
          cb.onchange = () => { const v = saved[`c${pi}`] || []; v[ci] = cb.checked; saved[`c${pi}`] = v; save(); };
          lab.append(cb, el("span", "ct", md(c.text)), el("span", "hint"));
          list.append(lab);
        });
        ob.append(list);
        if (op.sample) {
          const d = el("details", "sample"); d.innerHTML = `<summary>Ver un ejemplo de respuesta (solo después de escribir la tuya)</summary><p><i>${esc(op.sample)}</i></p>`;
          ob.append(d);
        }
        right.append(ob);
        graders.push(() => { list.querySelectorAll("input").forEach(x => x.disabled = true); if (ta) ta.readOnly = true; return [...list.querySelectorAll("input")].filter(x => x.checked).length; });
      }
      sec.append(left, right);
      app.append(sec);
    });

    const actions = el("div", "actions");
    const check = el("button", "btn big", "Revisar mis respuestas"); check.type = "button";
    const result = el("div", "result");
    actions.append(check);
    app.append(result, actions);
    check.onclick = () => {
      const unanswered = qn - Object.keys(saved).filter(k => /^q\d+$/.test(k) && (Array.isArray(saved[k]) ? saved[k].some(Boolean) : saved[k] !== "" && saved[k] != null)).length;
      if (unanswered > 0 && !confirm(`Te faltan ${unanswered} pregunta(s) por responder. ¿Revisar de todos modos?`)) return;
      const pts = graders.reduce((s, g) => s + g(), 0);
      const pct = pts / t.total;
      const best = store.get(`best:${tid}/${sk}`, null);
      if (best == null || pts > best) store.set(`best:${tid}/${sk}`, pts);
      store.set(`last:${tid}/${sk}`, { pts, at: Date.now() });
      const msg = pct >= 0.8 ? "¡Estás listo para la prueba!" : pct >= 0.5 ? "Vas bien. Lee las explicaciones de lo que fallaste y vuelve a intentarlo." : "Necesitas repasar un poco antes de la prueba.";
      result.className = "result show " + (pct >= 0.8 ? "ok" : pct >= 0.5 ? "mid" : "low");
      result.innerHTML = `<div class="score">${pts} / ${t.total}</div><p class="msg">${msg}</p>` +
        (pct < 0.8 ? `<p><b>Qué repasar en tu libro (Tema ${themeLabel(tid)}):</b> ${md(t.review)}</p>` : "") +
        `<p class="small">Las respuestas abiertas cuentan según las casillas que marcaste. Sé honesto contigo mismo.</p>`;
      actions.innerHTML = "";
      const again = el("button", "btn", "Intentar de nuevo"); again.type = "button";
      again.onclick = () => { store.del(key); renderTest(tid, sk); window.scrollTo(0, 0); };
      const back = el("a", "btn ghost", "Todos los mini-tests"); back.href = "#";
      actions.append(again, back);
      result.scrollIntoView({ behavior: "smooth", block: "center" });
    };
    window.scrollTo(0, 0);
  }

  function route() {
    const h = decodeURIComponent(location.hash.replace(/^#\/?/, ""));
    const m = h.match(/^(\d-\d)\/(\w+)$/);
    if (m) renderTest(m[1], m[2]); else renderIndex();
  }
  window.addEventListener("hashchange", route);
  route();
  if ("serviceWorker" in navigator && location.protocol.startsWith("http")) navigator.serviceWorker.register("sw.js");
})();
