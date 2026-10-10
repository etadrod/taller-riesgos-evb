/* Service worker: guarda la app para usarla sin conexión. Generado por tools/build.py */
const CACHE="evb-5870dadbdf";
const CORE=["./", "./index.html", "./manifest.webmanifest", "./img/logo-centro.jpg", "./vendor/jspdf.umd.min.js", "./vendor/jspdf.plugin.autotable.min.js", "./icons/icon-192.png", "./icons/icon-512.png", "./icons/icon-maskable-512.png", "./icons/apple-touch-icon.png", "./icons/favicon-32.png"];
self.addEventListener("install",e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting()))});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k.startsWith("evb-")&&k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener("fetch",e=>{
  const req=e.request;if(req.method!=="GET")return;
  const url=new URL(req.url);
  if(req.mode==="navigate"){
    e.respondWith(fetch(req).then(r=>{const cp=r.clone();caches.open(CACHE).then(c=>c.put("./index.html",cp));return r}).catch(()=>caches.match("./index.html")));return}
  if(url.origin===location.origin){
    e.respondWith(caches.match(req).then(hit=>hit||fetch(req).then(r=>{if(r.ok){const cp=r.clone();caches.open(CACHE).then(c=>c.put(req,cp))}return r})));return}
  if(url.hostname==="fonts.googleapis.com"||url.hostname==="fonts.gstatic.com"){
    e.respondWith(caches.open(CACHE).then(c=>c.match(req).then(hit=>{const net=fetch(req).then(r=>{if(r.ok||r.type==="opaque")c.put(req,r.clone());return r}).catch(()=>hit);return hit||net})))}
});
