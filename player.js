
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
