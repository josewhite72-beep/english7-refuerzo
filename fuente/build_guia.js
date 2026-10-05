const fs = require("fs");
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, AlignmentType, BorderStyle, WidthType,
  LevelFormat, Footer, PageNumber } = require("docx");
const FONT = "Arial", W = 9936;
function runs(text, base = {}) {
  const out = []; let b = false, i = false, buf = "";
  const flush = () => { if (buf) out.push(new TextRun({ text: buf, bold: b || base.bold, italics: i || base.italics, size: base.size, font: FONT })); buf = ""; };
  for (let k = 0; k < text.length; k++) {
    if (text.startsWith("**", k)) { flush(); b = !b; k++; continue; }
    if (text[k] === "*") { flush(); i = !i; continue; }
    buf += text[k];
  } flush(); return out;
}
const P = (t, o = {}) => new Paragraph({ children: runs(t, o.run || {}), spacing: { after: 120, ...(o.sp || {}) }, alignment: o.align, keepNext: o.keepNext });
const H1 = t => new Paragraph({ children: runs(t, { bold: true, size: 30 }), spacing: { before: 280, after: 140 }, keepNext: true,
  border: { bottom: { style: BorderStyle.SINGLE, size: 10, color: "000000", space: 4 } } });
const H2 = t => new Paragraph({ children: runs(t, { bold: true, size: 25 }), spacing: { before: 220, after: 100 }, keepNext: true });
const B = t => new Paragraph({ numbering: { reference: "bul", level: 0 }, children: runs(t), spacing: { after: 70 } });
const N = (t, ref = "num") => new Paragraph({ numbering: { reference: ref, level: 0 }, children: runs(t), spacing: { after: 70 } });
const line = { style: BorderStyle.SINGLE, size: 6, color: "000000" };
const borders = { top: line, bottom: line, left: line, right: line };
const cell = (t, w, bold) => new TableCell({ borders, width: { size: w, type: WidthType.DXA }, margins: { top: 70, bottom: 70, left: 110, right: 110 },
  children: [P(t, { run: { bold }, sp: { after: 0 } })] });
const table = (widths, head, rows) => [new Table({ width: { size: widths.reduce((a, c) => a + c, 0), type: WidthType.DXA }, columnWidths: widths,
  rows: [new TableRow({ tableHeader: true, children: head.map((h, i) => cell(h, widths[i], true)) }),
    ...rows.map(r => new TableRow({ cantSplit: true, children: r.map((c, i) => cell(c, widths[i])) }))] }), P("", { sp: { after: 60 } })];
const SITE = "english7-refuerzo.vercel.app";

const children = [
  P("English 7 · Libro de refuerzo · I Trimestre", { align: AlignmentType.CENTER, run: { bold: true, size: 40 }, sp: { after: 60 } }),
  P("Descripción e instrucciones de uso", { align: AlignmentType.CENTER, run: { size: 28 }, sp: { after: 60 } }),
  P("José White · PanaMentorLabs", { align: AlignmentType.CENTER, run: { italics: true, size: 22 }, sp: { after: 240 } }),

  H1("1. ¿Qué es English 7 Refuerzo?"),
  P("Es un **libro de apoyo para estudiar inglés en casa**, pensado para estudiantes que pasan de 6° a 7° grado. Sigue los temas del **I Trimestre de 7°** del programa de inglés de MEDUCA, para que el estudiante pueda repasar por su cuenta cuando vea esos temas en su nueva escuela y sienta que necesita ayuda."),
  P("Está diseñado para **estudiar sin un adulto al lado**: todas las instrucciones están en español sencillo, cada actividad trae un ejemplo resuelto y las respuestas explican el porqué de cada error."),
  P("El material tiene tres partes que se complementan:"),
  ...table([2600, 7200], ["Parte", "Qué es"], [
    ["**Libro impreso** (Word, 85 páginas)", "La base de todo. Se imprime y funciona aunque el estudiante no tenga celular ni internet."],
    ["**Página de audios**", `Los 28 audios del libro, en velocidad normal y lenta. Se abren con los códigos QR impresos. Dirección: **${SITE}**`],
    ["**Mini-tests en línea**", `Los 20 mini-tests del libro en versión interactiva: se corrigen solos y explican cada respuesta. Dirección: **${SITE}/tests.html**`],
  ]),

  H1("2. Qué contiene el libro"),
  ...table([3400, 6400], ["Sección", "Contenido"], [
    ["Repaso de 6°", "Verbo *to be*, pronombres y posesivos, palabras para preguntar, números y horas, con un mini-chequeo."],
    ["Scenario 1: Our New Classmates", "Theme 1: *Where are you from?* · Theme 2: *What Was Your Previous School Like?*"],
    ["Scenario 2: Panama's Wildlife", "Theme 1: *The Habitat of Wildlife* · Theme 2: *The Daily Habits of Animals*"],
    ["Gramática de consulta rápida", "Resumen de toda la gramática del trimestre, 20 verbos irregulares y las palabras que más se confunden en las pruebas."],
  ]),
  H2("Cada tema tiene las mismas partes"),
  B("**¿Te sientes perdido? Empieza aquí:** lo esencial del tema en una sola página."),
  B("**Vocabulario** con pronunciación aproximada, **lectura**, **chant** y **gramática** explicada en español."),
  B("**Las cinco destrezas** (Listening, Reading, Writing, Speaking y Mediation): una práctica y un **mini-test** de cada una, con un consejo para la prueba y su puntaje."),
  B("**¿Cómo me fue?:** tabla para anotar los puntajes, con lo que conviene repasar según el resultado."),
  B("**Respuestas** con la explicación de cada error, y las **transcripciones** de todos los audios."),

  H1("3. Instrucciones para el estudiante"),
  H2("Cómo usar el libro"),
  N("Cuando tu profesor empiece un tema en clase, **búscalo en el libro por su nombre** (Scenario y Theme)."),
  N("Si no entendiste algo en clase, lee primero la página **¿Te sientes perdido? Empieza aquí**."),
  N("Estudia en sesiones cortas: **20 minutos** al día rinden más que 3 horas un solo día."),
  N("Haz la práctica de cada destreza y luego su **mini-test**, sin mirar las respuestas."),
  N("Corrige con las **Respuestas** al final del tema **solo después de terminar**, y lee la explicación de lo que fallaste."),
  N("Anota tus puntajes en **¿Cómo me fue?** y repasa lo que te indique la tabla."),
  H2("Cómo escuchar los audios"),
  N("Donde veas un código QR con la palabra **AUDIO**, ábrelo con la cámara de tu celular. Si no puedes escanearlo, escribe la dirección que aparece al lado.", "num4"),
  N("Toca **Reproducir**. Si va muy rápido, elige **Velocidad lenta**.", "num4"),
  N("El texto del audio está oculto: ábrelo **solo después de responder**.", "num4"),
  N("Si no tienes internet, al final de cada tema están las **transcripciones** para leerlas en voz alta.", "num4"),
  H2("Cómo hacer los mini-tests en línea", "num2"),
  new Paragraph({ numbering: { reference: "num2", level: 0 }, children: runs("Escanea el QR **HAZ ESTE MINI-TEST TAMBIÉN EN LÍNEA** que está al final de cada mini-test, o entra a **" + SITE + "/tests.html** y elige el tema y la destreza."), spacing: { after: 70 } }),
  N("Responde todas las preguntas. Lo que escribes se guarda solo en tu celular o laptop.", "num2"),
  N("Toca **Revisar mis respuestas**: verás qué acertaste, la respuesta correcta y la explicación de cada pregunta.", "num2"),
  N("En **Writing** y **Mediation**, escribe en el cuadro: la página cuenta tus oraciones y te da pistas (\"parece que sí\"). Tú marcas las casillas de la lista con honestidad.", "num2"),
  N("En **Speaking**, escucha las preguntas, toca **Grabar mi respuesta** y luego escúchate. La primera vez, el navegador pedirá permiso para usar el micrófono.", "num2"),
  N("Si tu puntaje fue bajo, la página te dice **qué repasar en el libro**. Luego toca **Intentar de nuevo**.", "num2"),
  H2("Cómo usarlo sin internet (laptop)"),
  N("Con internet, entra una vez a **" + SITE + "/tests.html** y toca **Descargar (zip)** (unos 11 MB).", "num3"),
  N("Busca el archivo descargado, haz clic derecho y elige **Extraer todo**.", "num3"),
  N("Abre la carpeta y haz doble clic en **index.html** (audios) o **tests.html** (mini-tests). Todo funciona sin conexión.", "num3"),

  H1("4. Para la familia"),
  P("No es necesario que un adulto acompañe al estudiante, pero si alguien puede ayudar, esto suma mucho:"),
  B("Pregúntenle qué tema está viendo en clase y ayúdenlo a encontrarlo en el libro."),
  B("Revisen juntos la tabla **¿Cómo me fue?** al terminar un tema."),
  B("Cuando se equivoque, no digan \"no\": pídanle que lea la explicación en las Respuestas y vuelva a intentarlo."),
  B("Celebren cada mini-test terminado, aunque el puntaje no sea perfecto."),

  H1("5. Preguntas frecuentes"),
  ...table([3700, 6100], ["Pregunta", "Respuesta"], [
    ["¿Necesito internet para usar el libro?", "No. El libro impreso funciona solo. Internet sirve para los audios y los mini-tests en línea, y estos también se pueden descargar para usar sin conexión."],
    ["¿Se pierde mi progreso?", "Los puntajes y respuestas se guardan en el navegador del dispositivo que usas. Si cambias de celular o borras los datos del navegador, se pierden."],
    ["¿Alguien ve mis respuestas?", "No. No hay cuentas ni registro, y nada se envía a ningún lugar. Las grabaciones de Speaking se quedan en tu dispositivo."],
    ["¿Los mini-tests en línea son iguales a los del libro?", "Sí. Son exactamente las mismas preguntas; en línea se corrigen solos y explican cada respuesta."],
    ["¿Esto es material oficial de MEDUCA?", "No. Es un material de apoyo de PanaMentorLabs que sigue los temas del programa de inglés de MEDUCA."],
  ]),
];

const num = ref => ({ reference: ref, levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 300 } } } }] });
const doc = new Document({
  creator: "José White · PanaMentorLabs", title: "English 7 Refuerzo — Descripción e instrucciones",
  styles: { default: { document: { run: { font: FONT, size: 22 } } } },
  numbering: { config: [{ reference: "bul", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 270 } } } }] },
    num("num"), num("num2"), num("num3"), num("num4")] },
  sections: [{ properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1080, bottom: 1080, left: 1152, right: 1152 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [
      new TextRun({ text: "English 7 Refuerzo · Descripción e instrucciones — ", size: 16, font: FONT }), new TextRun({ children: [PageNumber.CURRENT], size: 16, font: FONT })] })] }) },
    children }],
});
Packer.toBuffer(doc).then(b => { fs.writeFileSync(process.argv[2], b); console.log("ok"); });
