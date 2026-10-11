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

## Normativa de carga de fuego

La pestaña «Carga de Fuego Ponderada» sigue el Anexo I del Reglamento de seguridad contra incendios en los establecimientos industriales aprobado por el Real Decreto 164/2025 (tablas 1.1.1 y 1.3.1 a 1.3.5) y resume las exigencias de los anexos II y III (tablas 2.1.1, 2.1.2, 3.3.1 a 3.5.1 y apartados de detección, rociadores y control de humos).
