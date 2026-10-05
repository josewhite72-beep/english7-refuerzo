# -*- coding: utf-8 -*-
"""Contenido del Tema 1.1 — Where are you from?
Bloques que leen build_docx.js (cuadernillo), gen_audio.py (MP3) y build_site.py (página de audio).
Marcado en textos: **negrita**, *cursiva*.
"""
from common import test_blocks, answer_blocks
from tests_t11 import TESTS

THEME_ID = "1-1"
THEME_TITLE = "Where are you from?"
SCENARIO = "Scenario 1: Our New Classmates"

# ---------------------------------------------------------------- AUDIO ----
# Cada pista: id, título, instrucción (español), segmentos (voz, texto, pausa en s)
NAR, SOF, MAT, KEV = "af_heart", "af_bella", "am_michael", "am_fenrir"

VOCAB = [
    ("classmate", "KLAS-meit", "compañero/a de clase", "Mateo is my new classmate."),
    ("hometown", "JÓUM-taun", "pueblo o ciudad donde naciste", "My hometown is Penonomé."),
    ("be from / come from", "bi from / kam from", "ser de / venir de", "She comes from David, in Chiriquí."),
    ("countryside", "KÁN-tri-said", "el campo", "My grandparents live in the countryside."),
    ("city", "SÍ-ti", "ciudad", "Now I live in the city."),
    ("schedule", "SKÉ-yul", "horario", "My school schedule starts at seven."),
    ("subject", "SÁB-yekt", "asignatura, materia", "My favorite subject is English."),
    ("recess", "RÍ-ses", "recreo", "We play soccer at recess."),
    ("cafeteria", "ka-fe-TÍ-ria", "cafetería, comedor", "I eat a snack in the cafeteria."),
    ("library", "LÁI-bre-ri", "biblioteca", "We read books in the library."),
    ("uniform", "YÚ-ni-form", "uniforme", "I wear a blue and white uniform."),
    ("friendly", "FRÉND-li", "amigable", "My new classmates are friendly."),
]

READING = [
    "Hi! My name is Sofía Ríos. I am twelve years old, and I am from Penonomé, in Coclé. Now I live in Panama City with my family. This year, I go to a new school.",
    "My school day starts at seven o'clock. I wear a blue and white uniform. My favorite subject is English because I like songs and stories. At recess, I eat a snack in the cafeteria with my classmate Mateo.",
    "Mateo comes from David, in Chiriquí. He plays soccer every afternoon, and he watches cartoons on Saturdays. On Fridays, we read books in the library.",
    "I miss my hometown, but my new classmates are friendly. Where are you from?",
]

CHANT = [
    "Where are you from? Where are you from?",
    "I'm from Coclé. And where are you from?",
    "She walks to school at seven each day,",
    "He reads in the library, then he goes out to play.",
    "She watches the clock, and she catches the bus.",
    "New friends, new school. Come and learn with us!",
]

DIALOGUE_PRACTICE = [
    (MAT, "Hi! Are you new here?"),
    (SOF, "Yes, I am. I'm Sofía. Today is my first day."),
    (MAT, "Nice to meet you, Sofía. I'm Mateo. Where are you from?"),
    (SOF, "I'm from Penonomé, in Coclé. And you?"),
    (MAT, "I come from David, in Chiriquí. My family moved here last year."),
    (SOF, "Cool! What's your favorite subject?"),
    (MAT, "Math. And you?"),
    (SOF, "English. I love songs and stories."),
    (MAT, "Our English class is on Monday and Wednesday, after recess."),
    (SOF, "Great! Where is the cafeteria?"),
    (MAT, "It's next to the library. Come with me at recess!"),
]

TEST_MONOLOGUE = [
    "Hello, everyone! My name is Kevin Martínez. I'm thirteen years old.",
    "I'm from Bocas del Toro, an island town in the west of Panama. In Bocas, I walked to school next to the beach.",
    "Now I live in Santiago, in Veraguas, and I take the bus to school.",
    "My new schedule is different. Classes start at seven thirty, and we have recess at ten.",
    "My favorite subject is Science because I like animals and plants.",
    "After school, my sister and I play basketball. On weekends, my dad cooks fish, like in Bocas.",
    "I'm a little nervous, but my classmates are very friendly. Thank you!",
]

SPEAK_MODELS = [
    "I'm from Penonomé, in Coclé.",
    "Where are you from?",
    "My favorite subject is English because I like songs.",
    "She walks to school.",
    "He plays soccer at recess.",
    "She watches videos in English.",
]

SPEAK_TEST_Q = [
    "Question one. What's your name?",
    "Question two. Where are you from?",
    "Question three. What's your favorite subject? Why?",
    "Question four. What do you do at recess?",
    "Question five. Think of your best friend. Where does your best friend come from?",
]

def _vocab_segments():
    segs = []
    for w, _, _, ex in VOCAB:
        word = w.replace(" / ", ", ")
        segs += [(NAR, word, 1.2), (NAR, ex, 1.6)]
    return segs

TRACKS = [
    {"n": "01", "title": "Vocabulario clave",
     "instr": "Escucha cada palabra y su ejemplo. Repite en voz alta durante la pausa.",
     "segments": _vocab_segments()},
    {"n": "02", "title": "Lectura: Meet Sofía",
     "instr": "Escucha el texto mientras lo sigues con el dedo en tu libro.",
     "segments": [(SOF, p, 1.0) for p in READING]},
    {"n": "03", "title": "Chant: Where Are You From?",
     "instr": "Escucha el chant y repítelo. Fíjate en el sonido final de walks, reads y watches.",
     "segments": [(NAR, l, 0.5) for l in CHANT]},
    {"n": "04", "title": "Listening — Práctica: First Day",
     "instr": "Escucha el diálogo dos veces. La primera vez, solo escucha. La segunda vez, responde.",
     "segments": [(v, t, 0.6) for v, t in DIALOGUE_PRACTICE]},
    {"n": "05", "title": "Listening — Mini-test: Kevin",
     "instr": "Mini-test. Escucha dos veces como máximo y responde en tu libro.",
     "segments": [(KEV, t, 0.7) for t in TEST_MONOLOGUE]},
    {"n": "06", "title": "Speaking — Oraciones modelo",
     "instr": "Escucha cada oración y repítela en la pausa. Después grábate y compara.",
     "segments": [(NAR, s, 3.0) for s in SPEAK_MODELS]},
    {"n": "07", "title": "Speaking — Mini-test (examen oral)",
     "instr": "Activa la grabadora de tu celular. Responde cada pregunta en voz alta durante la pausa.",
     "segments": [(NAR, "Speaking test. Answer each question with a complete sentence.", 2.0)]
                 + [(NAR, q, 9.0) for q in SPEAK_TEST_Q]},
]

# ----------------------------------------------------------- CUADERNILLO ----
def audio(n):
    t = next(t for t in TRACKS if t["n"] == n)
    return {"t": "audio", "id": f"{THEME_ID}/{n}", "label": f"Audio {THEME_ID.replace('-', '.')}-{n}", "title": t["title"]}

def score(text):
    return {"t": "score", "text": text}

TIP = lambda *lines: {"t": "box", "title": "Consejo para la prueba", "lines": list(lines)}
NOTE = lambda title, *lines: {"t": "box", "title": title, "lines": list(lines)}
P = lambda text, **k: dict({"t": "p", "text": text}, **k)
H1 = lambda text: {"t": "h1", "text": text}
H2 = lambda text: {"t": "h2", "text": text}
H3 = lambda text: {"t": "h3", "text": text}
ITEMS = lambda *items: {"t": "items", "items": list(items)}
OPTS = lambda *opts: {"t": "opts", "items": list(opts)}
LINES = lambda n=1: {"t": "lines", "n": n}
BULLETS = lambda *items: {"t": "bullets", "items": list(items)}
TABLE = lambda widths, header, rows: {"t": "table", "widths": widths, "header": header, "rows": rows}
PB = {"t": "pb"}

BLOCKS = [
    {"t": "theme_cover", "scenario": SCENARIO, "theme": "Theme 1: " + THEME_TITLE,
     "es": "¿De dónde eres?",
     "goals": ["Decir de dónde eres y preguntar a otros: *Where are you from? — I'm from...*",
               "Hablar de tu escuela y tu rutina con el presente simple: *She **walks** to school.*",
               "Pronunciar bien la **-s** final: walk**s** /s/, play**s** /z/, watch**es** /ɪz/."]},

    # ---------------------------------------------------- EMPIEZA AQUÍ ----
    H1("¿Te sientes perdido? Empieza aquí"),
    P("Si en clase no entendiste el tema, lee esta página primero. Aquí está **lo esencial** en una sola hoja."),
    H3("1. Las 10 palabras que más vas a escuchar"),
    TABLE([2200, 2700, 2200, 2700], ["Inglés", "Español", "Inglés", "Español"], [
        ["classmate", "compañero/a de clase", "subject", "asignatura"],
        ["hometown", "pueblo natal", "recess", "recreo"],
        ["be from", "ser de", "cafeteria", "comedor"],
        ["countryside", "el campo", "library", "biblioteca"],
        ["schedule", "horario", "friendly", "amigable"],
    ]),
    H3("2. La pregunta del tema y cómo responderla"),
    TABLE([4900, 4900], ["Pregunta", "Respuesta"], [
        ["Where **are you** from?", "**I'm** from Coclé."],
        ["Where **is she** from?", "**She's** from Chiriquí."],
        ["Where **does he** come from?", "He **comes** from Colón."],
    ]),
    H3("3. La regla que más se pregunta en las pruebas"),
    P("Con **he, she, it** (él, ella, eso) el verbo lleva **-s** o **-es**:"),
    P("I walk → she walk**s**   ·   I play → he play**s**   ·   I watch → she watch**es**   ·   I study → he stud**ies**", align="center"),
    H3("4. Una presentación modelo"),
    P("*Hi! My name is Ana. I'm from Penonomé. My favorite subject is English. At recess, I play with my classmates.*"),
    P("Escucha estas palabras en el **Audio 1.1-01** (página de Vocabulario)."),
    PB,

    # ---------------------------------------------------- VOCABULARIO ----
    H1("1. Vocabulario"),
    P("Escucha el audio, señala cada palabra y repítela en voz alta. La columna **Se pronuncia** te da una ayuda aproximada; el audio es la pronunciación correcta."),
    audio("01"),
    TABLE([2100, 1700, 2300, 3700], ["Inglés", "Se pronuncia", "Español", "Ejemplo"],
          [[f"**{w}**", p, s, f"*{ex}*"] for w, p, s, ex in VOCAB]),
    NOTE("Palabras que ayudan a preguntar (Wh- questions)",
         "**Who?** ¿Quién?  ·  **What?** ¿Qué?  ·  **Where?** ¿Dónde?  ·  **When?** ¿Cuándo?  ·  **Why?** ¿Por qué?  ·  **How?** ¿Cómo?"),

    PB,
    # ---------------------------------------------------- LECTURA ----
    H1("2. Lectura: Meet Sofía"),
    P("Lee el texto dos veces. La primera vez, en silencio. La segunda, en voz alta o junto con el audio."),
    audio("02"),
    {"t": "reading", "title": "Meet Sofía", "paras": READING},
    H2("Chant: Where Are You From?"),
    P("Escucha y repite. Marca el ritmo con palmadas. Fíjate en el sonido de la **-s** final (lo explicamos en la Gramática C)."),
    audio("03"),
    {"t": "poem", "lines": CHANT},
    P("En el chant: walk**s** /s/ · read**s** /z/ · go**es** /z/ · watch**es** /ɪz/ · catch**es** /ɪz/"),
    PB,

    # ---------------------------------------------------- GRAMÁTICA ----
    H1("3. Gramática del tema"),
    H2("A. Where are you from?"),
    TABLE([3300, 3300, 3200], ["Con be (ser/estar)", "Con come from", "En español"], [
        ["I'**m** from Coclé.", "I **come** from Coclé.", "Soy de Coclé."],
        ["You'**re** from Colón.", "You **come** from Colón.", "Eres de Colón."],
        ["He'**s** / She'**s** from David.", "He / She **comes** from David.", "Él / Ella es de David."],
        ["We'**re** / They'**re** from Panama.", "We / They **come** from Panama.", "Somos / Son de Panamá."],
    ]),
    P("Preguntas: **Where are you from?**  ·  **Where is he from?**  ·  **Where does she come from?**"),
    H2("B. Presente simple: rutinas y hábitos"),
    P("Usamos el presente simple para lo que hacemos **siempre o normalmente**: horarios, rutinas, gustos."),
    TABLE([3300, 3300, 3200], ["Afirmativa", "Negativa", "Pregunta"], [
        ["I / You / We / They **play**.", "I **don't** play.", "**Do** you play?"],
        ["He / She / It **plays**.", "She **doesn't** play.", "**Does** she play?"],
    ]),
    P("**Cómo se agrega la -s:**"),
    BULLETS("La mayoría de los verbos: **+ s** → walk**s**, play**s**, read**s**, start**s**.",
            "Verbos que terminan en -s, -sh, -ch, -x, -o: **+ es** → watch**es**, wash**es**, fix**es**, go**es**, do**es**.",
            "Consonante + y: **y → ies** → study → stud**ies**, fly → fl**ies**. (Pero vocal + y: play → play**s**.)"),
    NOTE("Error común",
         "Después de **doesn't** o **does**, el verbo va **sin -s**:",
         "✗ She doesn't play**s**.  ✓ She doesn't **play**.     ✗ Does he come**s**?  ✓ Does he **come**?"),
    H2("C. Pronunciación de la -s final"),
    TABLE([2200, 4100, 3500], ["Sonido", "Cuándo", "Ejemplos"], [
        ["/s/", "después de p, t, k, f", "walks, starts, eats, *participates*"],
        ["/z/", "después de vocal o b, d, g, l, m, n, r, v", "plays, reads, comes, lives"],
        ["/ɪz/ (una sílaba más)", "después de s, sh, ch, x, z, ge", "watches, washes, uses, fixes"],
    ]),
    PB,

    # ---------------------------------------------------- LISTENING ----
    H1("4. Listening (Escuchar)"),
    H2("Práctica: First Day"),
    P("Escucha el diálogo entre Sofía y Mateo. **Primera vez:** solo escucha. **Segunda vez:** responde. Si lo necesitas, usa la velocidad lenta."),
    audio("04"),
    P("**Ejemplo:** Today is Sofía's ______ day.  →  **first**"),
    ITEMS("1. Where is Sofía from?"),
    OPTS("a) David", "b) Penonomé", "c) Colón"),
    ITEMS("2. Mateo comes from ______________, in Chiriquí."),
    ITEMS("3. Mateo's favorite subject is:"),
    OPTS("a) English", "b) Science", "c) Math"),
    ITEMS("4. Their English class is on:"),
    OPTS("a) Monday and Wednesday", "b) Tuesday and Thursday", "c) Friday"),
    ITEMS("5. The cafeteria is next to the ______________."),
    *test_blocks(TESTS["listening"], audio),
    PB,

    # ---------------------------------------------------- READING ----
    H1("5. Reading (Leer)"),
    H2("Práctica (texto: Meet Sofía)"),
    P("**A. True or False.** Escribe T o F. Si es falso, corrige la oración."),
    P("**Ejemplo:** Sofía is twelve years old. → **T**"),
    ITEMS("1. Sofía is from Panama City. ______", "2. Her school day starts at seven o'clock. ______",
          "3. Mateo plays soccer every afternoon. ______", "4. They read books in the cafeteria on Fridays. ______"),
    P("**B. Une cada pregunta con su respuesta.** Escribe la letra."),
    TABLE([5600, 4200], ["Pregunta", "Respuesta"], [
        ["1. Where is Mateo from?  ___", "a) English"],
        ["2. What is Sofía's favorite subject?  ___", "b) In the cafeteria"],
        ["3. Where does Sofía eat a snack?  ___", "c) Blue and white"],
        ["4. What color is her uniform?  ___", "d) From David, in Chiriquí"],
    ]),
    P("**C. Cazador de terminaciones.** Busca en el texto 4 verbos que terminen en -s o -es y escribe su forma base."),
    P("**Ejemplo:** starts → **start**"),
    ITEMS("1. __________ → __________", "2. __________ → __________", "3. __________ → __________", "4. __________ → __________"),
    *test_blocks(TESTS["reading"], audio),
    PB,

    # ---------------------------------------------------- WRITING ----
    H1("6. Writing (Escribir)"),
    H2("Práctica"),
    P("**A. Completa con la forma correcta del verbo.**"),
    P("**Ejemplo:** Sofía ______ (live) in Panama City. → **lives**"),
    ITEMS("1. Mateo ______________ (come) from David.",
          "2. Sofía ______________ (watch) videos in English.",
          "3. My classmates ______________ (play) at recess.",
          "4. She ______________ (study) Math on Tuesdays.",
          "5. ______________ (do) he wear a uniform?"),
    P("**B. Ordena las palabras para formar oraciones.**"),
    P("**Ejemplo:** from / I'm / Coclé → **I'm from Coclé.**"),
    ITEMS("1. from / is / Where / she / ?  →  ______________________________",
          "2. school / at / starts / seven / My  →  ______________________________",
          "3. like / doesn't / He / Science  →  ______________________________"),
    P("**C. Escribe sobre ti.** Completa el modelo en tu cuaderno."),
    P("*My name is ________. I'm from ________. My favorite subject is ________ because ________. At recess, I ________.*"),
    *test_blocks(TESTS["writing"], audio),
    PB,

    # ---------------------------------------------------- SPEAKING ----
    H1("7. Speaking (Hablar)"),
    H2("Práctica: escucha, repite y grábate"),
    P("**Paso 1.** Escucha cada oración y repítela en la pausa."),
    P("**Paso 2.** Graba en tu celular las mismas oraciones."),
    P("**Paso 3.** Escucha tu grabación y compárala con el audio. ¿Se oye la -s final?"),
    audio("06"),
    ITEMS(*[f"{i+1}. {s}" for i, s in enumerate(SPEAK_MODELS)]),
    P("**Prepara tu presentación.** Escribe 5 oraciones sobre ti usando el modelo de la página \"Empieza aquí\". Practícala hasta decirla **sin leer**."),
    *test_blocks(TESTS["speaking"], audio),
    PB,

    # ---------------------------------------------------- MEDIATION ----
    H1("8. Mediation (Ayudar a otros a entender)"),
    P("Mediar es **ayudar a otra persona a entender un mensaje**: lo haces más corto y simple, o lo pasas de un idioma a otro."),
    H2("Práctica"),
    P("**A. Simplifica.** Un compañero nuevo no entiende este aviso. Escríbelo en **2 oraciones cortas**."),
    NOTE("Aviso", "*Attention, students: because the cafeteria is closed for cleaning on Wednesday, all students must eat their snacks in the library during recess on that day.*"),
    P("**Ejemplo de inicio:** *On Wednesday, the cafeteria is closed.* ...completa la segunda oración:"),
    LINES(1),
    P("**B. Del español al inglés.** Tu compañero nuevo solo habla inglés y ve este letrero. Explícaselo en una oración simple."),
    NOTE("Letrero", "Uso obligatorio del uniforme de lunes a viernes."),
    LINES(1),
    P("**C. Reglas para un estudiante nuevo.** Escribe 3 reglas de tu salón en inglés simple."),
    P("**Ejemplo:** *We raise our hand to talk.*   ·   *We don't eat in the classroom.*"),
    LINES(3),
    *test_blocks(TESTS["mediation"], audio),
    PB,

    # ---------------------------------------------------- CIERRE ----
    H1("¿Cómo me fue en el Tema 1.1?"),
    P("Anota tus puntajes. Te dicen qué repasar antes de una prueba."),
    TABLE([2600, 1600, 5600], ["Mini-test", "Puntaje", "Si tuviste menos de la mitad, repasa..."], [
        ["Listening", "___ / 6", "Vocabulario (audio 01) y la práctica con el audio 04 en velocidad lenta"],
        ["Reading", "___ / 6", "La lectura *Meet Sofía* y el Consejo para la prueba de Reading"],
        ["Writing", "___ / 10", "Gramática B: la -s con he/she y el error común con doesn't"],
        ["Speaking", "___ / 8", "Audio 06: escucha, repite y grábate otra vez"],
        ["Mediation", "___ / 8", "El Consejo de Mediation: quién, qué y cuándo"],
    ]),
    TABLE([6400, 1100, 1100, 1200], ["Puedo...", "Sí", "Casi", "Todavía no"], [
        ["decir de dónde soy y preguntar a otros (*Where are you from?*)", "☐", "☐", "☐"],
        ["usar el presente simple con -s para he/she", "☐", "☐", "☐"],
        ["pronunciar la -s final: /s/, /z/, /ɪz/", "☐", "☐", "☐"],
        ["entender a un compañero que se presenta", "☐", "☐", "☐"],
        ["simplificar un aviso para un compañero nuevo", "☐", "☐", "☐"],
    ]),
    PB,

    # ---------------------------------------------------- RESPUESTAS ----
    H1("Respuestas del Tema 1.1"),
    P("Corrige **solo después de terminar**. Si te equivocaste, lee la explicación: ahí está lo que necesitas aprender."),
    H3("Listening — Práctica"),
    ITEMS("1. **b) Penonomé.** Sofía dice: *I'm from Penonomé, in Coclé.*",
          "2. **David.** Mateo dice: *I come from David, in Chiriquí.*",
          "3. **c) Math.**",
          "4. **a) Monday and Wednesday.** Mateo dice: *on Monday and Wednesday, after recess.*",
          "5. **library.** *It's next to the library.*"),
    *answer_blocks(TESTS["listening"]),
    H3("Reading — Práctica"),
    ITEMS("A1. **F.** Sofía is from **Penonomé**. Ahora *vive* en Panama City, pero no es *de* allí.",
          "A2. **T.**   A3. **T.**",
          "A4. **F.** They read books in the **library** on Fridays.",
          "B. 1-d · 2-a · 3-b · 4-c",
          "C. Puedes encontrar: starts → start · comes → come · plays → play · watches → watch. Fíjate: *watches* lleva **-es** porque *watch* termina en -ch."),
    *answer_blocks(TESTS["reading"]),
    H3("Writing — Práctica"),
    ITEMS("A1. **comes** (he → -s)   A2. **watches** (watch termina en -ch → -es)",
          "A3. **play** (classmates = they, sin -s)   A4. **studies** (consonante + y → -ies)   A5. **Does** (pregunta con he)",
          "B1. **Where is she from?**   B2. **My school starts at seven.**   B3. **He doesn't like Science.**",
          "C. Respuesta libre. Ejemplo: *My name is Luis. I'm from Aguadulce. My favorite subject is Science because I like animals. At recess, I play soccer.*"),
    *answer_blocks(TESTS["writing"]),
    H3("Mediation — ejemplos de respuesta"),
    ITEMS("Práctica A: *On Wednesday, the cafeteria is closed. We eat our snack in the library.*",
          "Práctica B: *We wear the uniform from Monday to Friday.*"),
    *answer_blocks(TESTS["mediation"]),
    PB,

    # ---------------------------------------------------- TRANSCRIPCIONES ----
    H1("Transcripciones de los audios del Tema 1.1"),
    P("Si no puedes escuchar un audio, pide a alguien que lo lea o léelo tú en voz alta. Úsalas también para revisar lo que no entendiste."),
    {"t": "transcripts"},
]
