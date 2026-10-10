"""Genera public/index.html y public/sw.js a partir de app.html.
Uso: python3 tools/build.py (desde la raíz del repositorio)."""
import re,os,hashlib
s=open('app.html').read()
head=('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
 '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
 '<meta name="description" content="Asistente y casos prácticos de análisis de riesgos en Protección Civil (Módulo 1502, Canarias).">\n'
 '<meta name="theme-color" content="#1F3A68">\n'
 '<link rel="manifest" href="manifest.webmanifest">\n'
 '<link rel="icon" type="image/png" sizes="32x32" href="icons/favicon-32.png">\n'
 '<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">\n'
 '<meta name="apple-mobile-web-app-capable" content="yes">\n'
 '<meta name="apple-mobile-web-app-title" content="Análisis de Riesgos">\n')
title=re.search(r'<title>.*?</title>',s).group(0)
rest=s.replace(title,'',1)
e=rest.index('</style>')+8
sw_reg=('<script>if("serviceWorker" in navigator){addEventListener("load",()=>{'
 'navigator.serviceWorker.register("sw.js").catch(()=>{})})}</script>\n')
html=head+title+'\n'+rest[:e]+'\n</head>\n<body>\n'+rest[e:]+'\n'+sw_reg+'</body>\n</html>\n'
os.makedirs('public',exist_ok=True)
open('public/index.html','w').write(html)
CORE=["./","./index.html","./manifest.webmanifest","./img/logo-centro.jpg",
 "./vendor/jspdf.umd.min.js","./vendor/jspdf.plugin.autotable.min.js",
 "./icons/icon-192.png","./icons/icon-512.png","./icons/icon-maskable-512.png",
 "./icons/apple-touch-icon.png","./icons/favicon-32.png"]
h=hashlib.sha256()
for f in CORE[1:]:
    h.update(open('public/'+f[2:],'rb').read())
ver=h.hexdigest()[:10]
sw=open('tools/sw.template.js').read().replace("__VERSION__",ver).replace("__CORE__",repr(CORE).replace("'",'"'))
open('public/sw.js','w').write(sw)
print("build",ver)
