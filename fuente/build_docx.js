// Construye el cuadernillo Word a partir de out/book.json
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, ImageRun,
  AlignmentType, BorderStyle, WidthType, LevelFormat, PageBreak, Footer, PageNumber,
  VerticalAlign, HeightRule, PositionalTab, PositionalTabAlignment, PositionalTabRelativeTo, PositionalTabLeader,
} = require("docx");

const ROOT = __dirname;
const book = JSON.parse(fs.readFileSync(path.join(ROOT, "out", "book.json"), "utf8"));
const OUT = process.argv[2] || path.join(ROOT, "out", "English7_Refuerzo.docx");
const FONT = "Arial";
const CONTENT_W = 9936; // Letter 12240 - 2 * 1152

// ---------- texto enriquecido: **negrita**, *cursiva* (anidables) ----------
function runs(text, base = {}) {
  const out = [];
  let bold = false, italics = false, buf = "";
  const flush = () => { if (buf) out.push(new TextRun({ text: buf, bold: bold || base.bold, italics: italics || base.italics, size: base.size, font: FONT })); buf = ""; };
  for (let i = 0; i < text.length; i++) {
    if (text.startsWith("**", i)) { flush(); bold = !bold; i++; continue; }
    if (text[i] === "*") { flush(); italics = !italics; continue; }
    buf += text[i];
  }
  flush();
  return out;
}
const P = (text, opts = {}) => new Paragraph({ children: runs(text, opts.run || {}), spacing: { after: 100, ...(opts.spacing || {}) }, alignment: opts.align, indent: opts.indent, keepNext: opts.keepNext, border: opts.border, pageBreakBefore: opts.pbb });

const line = { style: BorderStyle.SINGLE, size: 6, color: "000000" };
const borders = { top: line, bottom: line, left: line, right: line };
const boxBorder = { top: line, bottom: line, left: line, right: line };
const cell = (children, width, extra = {}) => new TableCell({ borders, width: { size: width, type: WidthType.DXA }, margins: { top: 70, bottom: 70, left: 110, right: 110 }, children, ...extra });

// ---------- bloques ----------
const BINDS = new Set(["audio","reading","table","box","poem","opts","lines","items","bullets","score"]);
function render(b, next) {
  const bindNext = !!next && BINDS.has(next.t);
  switch (b.t) {
    case "book_cover": {
      const out = [new Paragraph({ spacing: { before: 2200 }, children: [] }),
        P(b.title, { align: AlignmentType.CENTER, run: { bold: true, size: 72 } }),
        P(b.subtitle, { align: AlignmentType.CENTER, run: { size: 32 } }),
        P(b.desc, { align: AlignmentType.CENTER, run: { italics: true, size: 24 }, spacing: { after: 900 } }),
        P("Contenido", { align: AlignmentType.CENTER, run: { bold: true, size: 24 } })];
      b.contents.forEach(c => out.push(P(c.trim(), { align: AlignmentType.CENTER, run: { bold: !c.startsWith(" "), size: 22 }, spacing: { after: 40 } })));
      out.push(new Paragraph({ spacing: { before: 1600 }, alignment: AlignmentType.CENTER, children: runs(b.author, { size: 20 }) }));
      out.push(new Paragraph({ children: [new PageBreak()] }));
      return out;
    }
    case "theme_cover": {
      const inner = [
        P(b.scenario, { align: AlignmentType.CENTER, run: { size: 24 } }),
        P(b.theme, { align: AlignmentType.CENTER, run: { bold: true, size: 40 } }),
        P(b.es, { align: AlignmentType.CENTER, run: { italics: true, size: 24 }, spacing: { after: 200 } }),
        P("En este tema vas a aprender a:", { run: { bold: true } }),
        ...b.goals.map(g => new Paragraph({ numbering: { reference: "bul", level: 0 }, children: runs(g), spacing: { after: 60 } })),
      ];
      return [new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [CONTENT_W],
        rows: [new TableRow({ children: [cell(inner, CONTENT_W, { margins: { top: 200, bottom: 200, left: 300, right: 300 } })] })] }),
        new Paragraph({ spacing: { after: 200 }, children: [] })];
    }
    case "h1": return [new Paragraph({ children: runs(b.text, { bold: true, size: 32 }), spacing: { before: 120, after: 160 }, keepNext: true, pageBreakBefore: b.pbb,
      border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: "000000", space: 4 } } })];
    case "h2": return [new Paragraph({ children: runs(b.text, { bold: true, size: 26 }), spacing: { before: 240, after: 100 }, keepNext: true, pageBreakBefore: b.pbb })];
    case "h3": return [new Paragraph({ children: runs(b.text, { bold: true, size: 23 }), spacing: { before: 180, after: 80 }, keepNext: true })];
    case "p": return [P(b.text, { align: b.align === "center" ? AlignmentType.CENTER : undefined, keepNext: bindNext })];
    case "items": return b.items.map((t, i) => P(t, { indent: { left: 360, hanging: 360 }, spacing: { after: 80 },
      keepNext: i === b.items.length - 1 && !!next && ["opts", "lines"].includes(next.t) }));
    case "opts": return b.items.map((t, i) => P(t, { indent: { left: 900 }, spacing: { after: i === b.items.length - 1 ? 140 : 20 }, keepNext: i < b.items.length - 1 }));
    case "bullets": return b.items.map(t => new Paragraph({ numbering: { reference: "bul", level: 0 }, children: runs(t), spacing: { after: 60 } }));
    case "lines": return Array.from({ length: b.n }, () => new Paragraph({ spacing: { before: 260, after: 0 },
      children: [new TextRun({ font: FONT, text: "_".repeat(80) })] }))
      .concat([new Paragraph({ spacing: { after: 120 }, children: [] })]);
    case "score": return [P(b.text, { align: AlignmentType.RIGHT, run: { bold: true, size: 24 }, spacing: { before: 160, after: 160 } })];
    case "pb": return [new Paragraph({ children: [new PageBreak()] })];
    case "box": {
      const ps = [P(b.title, { run: { bold: true }, spacing: { after: 60 } }), ...b.lines.map(l => P(l, { spacing: { after: 40 } }))];
      return [new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [CONTENT_W],
        rows: [new TableRow({ cantSplit: true, children: [cell(ps, CONTENT_W, { margins: { top: 100, bottom: 100, left: 180, right: 180 } })] })] }),
        new Paragraph({ spacing: { after: 120 }, children: [] })];
    }
    case "reading": {
      const ps = [P(b.title, { align: AlignmentType.CENTER, run: { bold: true, size: 26 }, spacing: { after: 120 } }),
        ...b.paras.map(t => P(t, { run: { size: 24 }, spacing: { after: 140, line: 320 } }))];
      return [new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [CONTENT_W],
        rows: [new TableRow({ cantSplit: true, children: [cell(ps, CONTENT_W, { margins: { top: 200, bottom: 120, left: 300, right: 300 } })] })] }),
        new Paragraph({ spacing: { after: 160 }, children: [] })];
    }
    case "poem": return b.lines.map((l, i) => P(l, { align: AlignmentType.CENTER, run: { italics: true, size: 24 }, spacing: { after: i === b.lines.length - 1 ? 160 : 20 } }));
    case "audio": {
      const [theme, n] = b.id.split("/");
      const png = fs.readFileSync(path.join(ROOT, "qr", `${theme}-${n}.png`));
      const qrW = 1500, txtW = CONTENT_W - qrW;
      const qrCell = cell([new Paragraph({ alignment: AlignmentType.CENTER, children: [new ImageRun({ type: "png", data: png, transformation: { width: 84, height: 84 } })] })], qrW, { verticalAlign: VerticalAlign.CENTER });
      const txtCell = cell([
        P(`AUDIO ${theme.replace("-", ".")}-${n}`, { run: { bold: true, size: 24 }, spacing: { after: 40 } }),
        P(b.title, { spacing: { after: 40 } }),
        P(`Escanea el código o escribe: **${book.site}/${theme}/${n}**`, { run: { size: 19 }, spacing: { after: 0 } }),
      ], txtW, { verticalAlign: VerticalAlign.CENTER });
      return [new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [qrW, txtW],
        rows: [new TableRow({ cantSplit: true, children: [qrCell, txtCell] })] }), new Paragraph({ spacing: { after: 140 }, children: [] })];
    }
    case "online": {
      const [theme, skill] = b.id.split("/");
      const png = fs.readFileSync(path.join(ROOT, "qr", `test-${theme}-${skill}.png`));
      const qrW = 1300, txtW = CONTENT_W - qrW;
      const qrCell = cell([new Paragraph({ alignment: AlignmentType.CENTER, children: [new ImageRun({ type: "png", data: png, transformation: { width: 70, height: 70 } })] })], qrW, { verticalAlign: VerticalAlign.CENTER });
      const txtCell = cell([
        P("HAZ ESTE MINI-TEST TAMBIÉN EN LÍNEA", { run: { bold: true, size: 21 }, spacing: { after: 30 } }),
        P("En línea se corrige solo y te explica cada respuesta.", { run: { size: 19 }, spacing: { after: 30 } }),
        P(`Escanea el código o escribe: **${book.site}/test/${theme}/${skill}**`, { run: { size: 19 }, spacing: { after: 0 } }),
      ], txtW, { verticalAlign: VerticalAlign.CENTER });
      return [new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [qrW, txtW],
        rows: [new TableRow({ cantSplit: true, children: [qrCell, txtCell] })] })];
    }
    case "table": {
      const total = b.widths.reduce((a, c) => a + c, 0);
      const head = new TableRow({ tableHeader: true, cantSplit: true, children: b.header.map((h, i) => cell([P(h, { run: { bold: true }, spacing: { after: 0 } })], b.widths[i])) });
      const rows = b.rows.map(r => new TableRow({ cantSplit: true, children: r.map((c, i) => cell([P(c, { spacing: { after: 0 } })], b.widths[i])) }));
      return [new Table({ width: { size: total, type: WidthType.DXA }, columnWidths: b.widths, rows: [head, ...rows] }), new Paragraph({ spacing: { after: 140 }, children: [] })];
    }
    case "transcripts": return b.items.flatMap(it => [
      P(it.label, { run: { bold: true }, spacing: { before: 160, after: 60 }, keepNext: true }),
      ...it.lines.map(l => P(l, { indent: { left: 360 }, spacing: { after: 30 } })),
    ]);
    default: throw new Error("Bloque desconocido: " + b.t);
  }
}

// Un salto de página antes de un título se convierte en "pageBreakBefore" (evita páginas en blanco)
const blocks = [];
for (let i = 0; i < book.blocks.length; i++) {
  const b = book.blocks[i], nx = book.blocks[i + 1];
  if (b.t === "pb" && nx && ["h1", "h2"].includes(nx.t)) { book.blocks[i + 1] = { ...nx, pbb: true }; continue; }
  blocks.push(b);
}
const children = blocks.flatMap((b, i) => render(b, blocks[i + 1]));
const doc = new Document({
  creator: "José White · PanaMentorLabs",
  title: "English 7 — Libro de refuerzo I Trimestre",
  styles: { default: { document: { run: { font: FONT, size: 22 } } } },
  numbering: { config: [{ reference: "bul", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 270 } } } }] }] },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1080, bottom: 1080, left: 1152, right: 1152 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [
      new TextRun({ text: "English 7 · Libro de refuerzo · I Trimestre  —  ", size: 16, font: FONT }),
      new TextRun({ children: [PageNumber.CURRENT], size: 16, font: FONT })] })] }) },
    children,
  }],
});
Packer.toBuffer(doc).then(buf => { fs.writeFileSync(OUT, buf); console.log("written", OUT); });
