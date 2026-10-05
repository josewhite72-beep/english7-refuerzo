# Fuente del libro "English 7 · Libro de refuerzo · I Trimestre"

Esta carpeta contiene todo lo necesario para **regenerar el libro en Word, los audios y los códigos QR**.
Vercel no la publica (ver `.vercelignore` en la raíz del repositorio).

## Qué hay aquí

| Archivo | Qué hace |
|---|---|
| `content/front.py` | Portada y "Cómo usar este libro". Aquí está la dirección impresa en los QR (`SITE`). |
| `content/repaso.py` | Repaso de 6° (inicio del libro). |
| `content/t11.py`, `t12.py`, `t21.py`, `t22.py` | Cada tema: vocabulario, lectura, gramática, prácticas, mini-tests, respuestas y los textos de los audios (`TRACKS`). |
| `content/referencia.py` | Gramática de consulta rápida (final del libro). |
| `content/common.py` | Funciones compartidas para escribir los temas. |
| `build_assets.py` | Genera los MP3 (voz Kokoro, normal y lenta), los QR y `out/book.json`. Incluye la lista `NAMES` con la pronunciación en español de nombres y lugares. |
| `build_docx.js` | Arma el Word a partir de `out/book.json`. |
| `content/tests_t11.py` … `tests_t22.py` | Los 20 mini-tests como datos: preguntas, respuestas, variantes aceptadas, explicaciones y listas de cotejo. **El libro y la versión en línea salen de aquí**: si corriges un mini-test, se corrige en los dos. |
| `web/tests.js`, `web/tests.css` | La versión en línea de los mini-tests (`tests.html`): se corrigen solos, guardan el progreso en el dispositivo y graban la voz en Speaking. |
| `build_site.py` | Arma la página en `site/`: audios, mini-tests en línea, enlaces de los QR `/test/…` y el zip para usar sin internet (`descargar/english7-refuerzo.zip`). |

## Cómo corregir algo

- **Un texto o una pregunta del libro:** edita el tema en `content/`, y vuelve a correr `build_assets.py` (con `NO_AUDIO=1` si no cambiaste audios) y `build_docx.js`.
- **Un audio:** edita el texto en `TRACKS` del tema, borra ese MP3 (normal y `-slow`) y corre `build_assets.py`: solo se regeneran los que faltan.
- **La pronunciación de un nombre:** agrégalo a `NAMES` en `build_assets.py` (en IPA) y regenera los audios donde aparece.

**No cambies los números de pista, los nombres de los mini-tests (`listening`, `reading`…) ni la dirección `SITE`:** están impresos en los QR.

## Cómo regenerar (requiere computadora o una sesión de Claude)

```bash
pip install kokoro-onnx soundfile numpy "qrcode[pil]"   # y tener ffmpeg y node con el paquete docx
mkdir tts-model
curl -L -o tts-model/kokoro.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.int8.onnx
curl -L -o tts-model/voices.bin  https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin

cp -r ../audio ./audio          # reutiliza los audios ya publicados
python3 build_assets.py         # audios que falten + QR + out/book.json
node build_docx.js              # out/English7_Refuerzo.docx
python3 build_site.py           # site/
cp -r site/. ../                # publica: copia la página a la raíz del repo
```

Las carpetas `audio/`, `qr/`, `out/`, `site/` y `tts-model/` se generan y no se guardan aquí.
