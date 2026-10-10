# Taller de Análisis de Riesgos

App web para el alumnado del Módulo 1502 *Evaluación de riesgos y medidas preventivas* (CFGS Coordinación de Emergencias y Protección Civil, Canarias).

- Asistente de análisis en 6 pasos (índice P × D y matriz 5×5).
- Casos prácticos autocorregibles.
- Referencia rápida de escalas, fenómenos y planes canarios.

Sitio estático: `public/index.html`. `app.html` es la fuente; `public/vendor` contiene jsPDF y jsPDF-AutoTable (licencia MIT) para generar el informe en PDF.

## Instalación como aplicación

La web es una aplicación instalable (PWA): `public/manifest.webmanifest`, iconos en `public/icons/` y `public/sw.js` para el uso sin conexión. Se instala desde Chrome, Edge o Safari (Mac: Archivo → Añadir al Dock) sin permisos de administrador.

## Generar la versión publicada

Tras editar `app.html`, ejecutar `python3 tools/build.py`. Genera `public/index.html` y `public/sw.js` (con una versión nueva de caché para que los equipos instalados se actualicen).
