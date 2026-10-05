// Selector de colores: se guarda en este dispositivo
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
