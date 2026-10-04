// Guarda lo que el estudiante ya abrió para poder escucharlo sin internet
const C='audios-v1';
self.addEventListener('install',e=>self.skipWaiting());
self.addEventListener('activate',e=>e.waitUntil(self.clients.claim()));
self.addEventListener('fetch',e=>{if(e.request.method!=='GET')return;
 e.respondWith(caches.open(C).then(async c=>{try{const r=await fetch(e.request);if(r.ok&&r.status===200)c.put(e.request,r.clone());return r}
 catch(err){const m=await c.match(e.request,{ignoreSearch:true});if(m)return m;throw err}}))});
