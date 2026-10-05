# -*- coding: utf-8 -*-
"""Tema 2.1 — The Habitat of Wildlife"""
from common import *
from common import test_blocks, answer_blocks
from tests_t21 import TESTS

THEME_ID = "2-1"
THEME_TITLE = "The Habitat of Wildlife"
SCENARIO = "Scenario 2: Panama's Wildlife"
CAR, GUI, REP = "am_michael", "af_sarah", "af_heart"
SPEAKERS = {CAR: "Carlos", GUI: "Guía"}

VOCAB = [
    ("habitat", "JÁ-bi-tat", "hábitat, hogar natural", "The rainforest is the habitat of the jaguar."),
    ("wildlife", "UÁILD-laif", "vida silvestre", "Panama has a lot of wildlife."),
    ("rainforest", "RÉIN-fo-rest", "bosque lluvioso", "Many monkeys live in the rainforest."),
    ("species", "SPÍ-shiz", "especie(s)", "There are many species of birds in Panama."),
    ("biodiversity", "bai-o-dai-VÉR-si-ti", "biodiversidad", "Darién has great biodiversity."),
    ("endangered", "en-DÉIN-yerd", "en peligro de extinción", "The golden frog is endangered."),
    ("protect", "pro-TÉKT", "proteger", "We must protect the forests."),
    ("predator", "PRÉ-da-tor", "depredador", "The harpy eagle is a predator."),
    ("prey", "PREI", "presa", "Sloths are prey for the harpy eagle."),
    ("survive", "ser-VÁIV", "sobrevivir", "Animals need water to survive."),
    ("nest", "NEST", "nido; hacer un nido", "Sea turtles make nests on the beach."),
    ("camouflage", "KÁ-mo-flash", "camuflaje", "The sloth's green fur is good camouflage."),
]

READING = [
    "Panama is a small country, but it has a lot of wildlife. There are more than nine hundred species of birds here! Animals live in many different habitats: rainforests, mountains, rivers, beaches, and the ocean.",
    "The rainforest in Darién is one of the richest habitats in the country. Jaguars, monkeys, sloths, and harpy eagles live there. The harpy eagle is Panama's national bird. It is one of the strongest eagles in the world, and it hunts monkeys and sloths in the tall trees.",
    "The golden frog lives in the mountains near El Valle de Antón. It is smaller than your hand, and it is very endangered.",
    "On some beaches, like Isla Cañas, sea turtles come out of the ocean at night and make their nests in the sand.",
    "Many of these animals are in danger because people cut down trees and pollute rivers. We must protect their habitats.",
]
READING_BOOK = [p.replace("nine hundred", "900") for p in READING]

CHANT_SPOKEN = [
    "Rainforest, rainforest, green and wide,",
    "Jaguars and monkeys live inside.",
    "Wildlife here and wildlife there,",
    "Birdsongs floating in the air.",
    "The harpy eagle, strong and great.",
    "Protect their home. Don't wait!",
]
CHANT_BOOK = [
    "Rain-for-est, rain-for-est, green and wide,",
    "Jag-uars and mon-keys live in-side.",
    "Wild-life here and wild-life there,",
    "Bird-songs float-ing in the air.",
    "The har-py ea-gle, strong and great.",
    "Pro-tect their home. Don't wait!",
]

DIALOGUE = [
    (GUI, "Welcome to the Metropolitan Natural Park! This park is a habitat for many animals."),
    (CAR, "Are there monkeys here?"),
    (GUI, "Yes, there are. You can see them in the morning."),
    (CAR, "What is that animal in the tree?"),
    (GUI, "That's a sloth. Sloths are the slowest mammals in the forest. They eat leaves."),
    (CAR, "Is it dangerous?"),
    (GUI, "No, it isn't. But it has long claws. Look, there is a toucan, too!"),
    (CAR, "Wow! The toucan is more colorful than the sloth."),
    (GUI, "Yes! Remember: don't feed the animals, and don't touch them. We must protect their habitat."),
]

NEWS = [
    "Good morning! This is Wildlife News. Today we are on Isla Cañas, a small island in Los Santos.",
    "Every year, from July to November, thousands of sea turtles come to this beach.",
    "They come out of the ocean at night and make their nests in the sand. Each turtle lays about one hundred eggs.",
    "After about fifty days, the baby turtles come out and walk to the ocean.",
    "Many animals eat the baby turtles: birds, crabs, and dogs. Only a few turtles survive.",
    "That's why the people of Isla Cañas protect the nests.",
    "Remember: if you visit, don't use lights on the beach at night. Lights confuse the turtles.",
]

SPEAK_MODELS = [
    "The rainforest is the habitat of the jaguar.",
    "There are many species of birds in Panama.",
    "The harpy eagle is stronger than the hawk.",
    "The jaguar is the biggest cat in the Americas.",
    "The golden frog is endangered.",
    "We must protect the rainforest.",
]

SPEAK_TEST_Q = [
    "Question one. What is your favorite animal? Where does it live?",
    "Question two. Name two animals that live in the rainforest. Use: there are.",
    "Question three. Compare two animals. Use bigger, smaller, or faster.",
    "Question four. In your opinion, which animal is the strongest? Why?",
    "Question five. How can we protect wildlife?",
]

TRACKS = [
    {"n": "01", "title": "Vocabulario clave", "instr": "Escucha cada palabra y su ejemplo. Repite en voz alta durante la pausa.",
     "segments": vocab_segments(VOCAB)},
    {"n": "02", "title": "Lectura: Panama, A Home for Wildlife", "instr": "Escucha el texto mientras lo sigues con el dedo en tu libro.",
     "segments": [(REP, p, 1.0) for p in READING]},
    {"n": "03", "title": "Chant: Rainforest", "instr": "Escucha y repite. Aplaude una vez por cada sílaba: rain-for-est, wild-life.",
     "segments": [(NAR, l, 0.5) for l in CHANT_SPOKEN]},
    {"n": "04", "title": "Listening — Práctica: A Visit to the Park", "instr": "Escucha el diálogo dos veces. La primera vez, solo escucha. La segunda vez, responde.",
     "segments": [(v, t, 0.6) for v, t in DIALOGUE]},
    {"n": "05", "title": "Listening — Mini-test: Wildlife News", "instr": "Mini-test. Escucha dos veces como máximo y responde en tu libro.",
     "segments": [(GUI, t, 0.7) for t in NEWS]},
    {"n": "06", "title": "Speaking — Oraciones modelo", "instr": "Escucha cada oración y repítela en la pausa. Después grábate y compara.",
     "segments": [(NAR, s, 3.0) for s in SPEAK_MODELS]},
    {"n": "07", "title": "Speaking — Mini-test (examen oral)", "instr": "Activa la grabadora de tu celular. Responde cada pregunta en voz alta durante la pausa.",
     "segments": [(NAR, "Speaking test. Answer each question with complete sentences.", 2.0)] + [(NAR, q, 11.0) for q in SPEAK_TEST_Q]},
]
audio = audio_factory(THEME_ID, TRACKS)

CHART = TABLE([1800, 1900, 2000, 1500, 1300, 1300], ["Animal", "Habitat", "Food", "Active", "Weight", "In danger?"], [
    ["jaguar", "rainforest", "deer, peccaries, turtles", "mostly at night", "about 90 kg", "yes"],
    ["harpy eagle", "tall rainforest trees", "monkeys, sloths", "during the day", "about 7 kg", "yes"],
    ["howler monkey", "rainforest", "leaves, fruit", "during the day", "about 6 kg", "no"],
    ["three-toed sloth", "rainforest", "leaves", "day and night", "about 4 kg", "no"],
    ["golden frog", "mountain streams", "small insects", "during the day", "less than 20 g", "yes"],
    ["sea turtle", "ocean and beaches", "jellyfish, crabs", "nests at night", "about 40 kg", "yes"],
])

BLOCKS = [
    {"t": "theme_cover", "scenario": SCENARIO, "theme": "Theme 1: " + THEME_TITLE, "es": "El hábitat de la vida silvestre",
     "goals": ["Nombrar animales de Panamá y su hábitat: *The jaguar lives in the rainforest.*",
               "Describir lugares con **there is / there are**: *There **are** many species of birds.*",
               "Comparar animales: *stronger than, the biggest, more colorful than.*",
               "Leer una **tabla** con información y dividir palabras en **sílabas**: rain-for-est."]},

    H1("¿Te sientes perdido? Empieza aquí"),
    P("Si en clase no entendiste el tema, lee esta página primero. Aquí está **lo esencial** en una sola hoja."),
    H3("1. Las 10 palabras que más vas a escuchar"),
    TABLE([2200, 2700, 2200, 2700], ["Inglés", "Español", "Inglés", "Español"], [
        ["habitat", "hábitat", "endangered", "en peligro de extinción"],
        ["wildlife", "vida silvestre", "protect", "proteger"],
        ["rainforest", "bosque lluvioso", "predator", "depredador"],
        ["species", "especie", "prey", "presa"],
        ["survive", "sobrevivir", "nest", "nido"],
    ]),
    H3("2. Las preguntas del tema y cómo responderlas"),
    TABLE([4900, 4900], ["Pregunta", "Respuesta"], [
        ["Where **does** the jaguar **live**?", "It **lives** in the rainforest."],
        ["**Are there** monkeys in the park?", "Yes, **there are**. / No, **there aren't**."],
        ["Which animal is **bigger**, the jaguar or the frog?", "The jaguar is **bigger than** the frog."],
        ["What is **the strongest** bird in Panama?", "The harpy eagle is **the strongest**."],
    ]),
    H3("3. La regla que más se pregunta en las pruebas"),
    P("**There is** + una cosa (*There **is** a sloth in the tree*). **There are** + varias cosas (*There **are** many birds*)."),
    P("Para comparar, recuerda: **-er than** / **more ... than** · **the -est** / **the most ...**  (lo viste en el Tema 1.2)."),
    H3("4. Una descripción modelo"),
    P("*The harpy eagle lives in the rainforest. There are harpy eagles in Darién. It is stronger than the hawk. It is endangered, so we must protect it.*"),
    P("Escucha estas palabras en el **Audio 2.1-01** (página de Vocabulario)."),
    PB,

    H1("1. Vocabulario"),
    P("Escucha el audio, señala cada palabra y repítela en voz alta. La columna **Se pronuncia** es una ayuda aproximada; el audio es la pronunciación correcta."),
    audio("01"),
    TABLE([2100, 1900, 2200, 3600], ["Inglés", "Se pronuncia", "Español", "Ejemplo"],
          [[f"**{w}**", p, s, f"*{ex}*"] for w, p, s, ex in VOCAB]),
    NOTE("Animales del tema", "**jaguar** jaguar · **harpy eagle** águila harpía · **sloth** perezoso · **howler monkey** mono aullador · **toucan** tucán · **golden frog** rana dorada · **sea turtle** tortuga marina · **deer** venado · **hawk** gavilán"),
    PB,

    H1("2. Lectura: Panama, A Home for Wildlife"),
    P("Lee el texto dos veces. La primera vez, en silencio. La segunda, en voz alta o junto con el audio."),
    audio("02"),
    READ("Panama, A Home for Wildlife", READING_BOOK),
    H2("Chant: Rainforest"),
    P("Escucha y repite. **Aplaude una vez por cada sílaba** (lo explicamos en la Gramática C)."),
    audio("03"),
    POEM(CHANT_BOOK),
    PB,

    H1("3. Gramática del tema"),
    H2("A. There is / There are"),
    P("Sirven para decir **qué hay** en un lugar."),
    TABLE([3300, 3300, 3200], ["Afirmativa", "Negativa", "Pregunta"], [
        ["**There is** a sloth in the tree.", "**There isn't** a jaguar here.", "**Is there** a river?"],
        ["**There are** many species.", "**There aren't** any monkeys.", "**Are there** turtles?"],
    ]),
    P("Con **many** (muchos), **some** (algunos) y **a lot of** (muchos) se usa **there are**: *There are **a lot of** birds.*"),
    NOTE("Error común", "En español decimos *\"hay\"* para todo, pero en inglés cambia:",
         "✗ There **is** many birds.  ✓ There **are** many birds.     ✗ There **are** a frog.  ✓ There **is** a frog."),
    H2("B. Comparar animales"),
    P("Las reglas son las mismas del Tema 1.2. Aquí van con animales:"),
    TABLE([2500, 2400, 2400, 2500], ["Regla", "Palabra", "Comparativo", "Superlativo"], [
        ["Corta: + er / + est", "strong", "strong**er** than", "the strong**est**"],
        ["Vocal + consonante: se dobla", "big", "bi**gger** than", "the bi**ggest**"],
        ["Termina en -y: ier / iest", "heavy", "heav**ier** than", "the heav**iest**"],
        ["Larga: more / most", "colorful", "**more** colorful than", "**the most** colorful"],
        ["Irregular", "good / bad", "**better** / **worse** than", "the **best** / the **worst**"],
    ]),
    H2("C. Sílabas y palabras compuestas"),
    P("Una **sílaba** es cada golpe de voz. Aplaude mientras dices la palabra: **an-i-mal** (3), **jag-uar** (2), **hab-i-tat** (3), **en-dan-gered** (3)."),
    P("Una **palabra compuesta** está hecha de **dos palabras** que ya conoces:"),
    TABLE([3300, 3300, 3200], ["Palabra compuesta", "Se forma con", "Sílabas"], [
        ["wildlife", "wild + life", "wild-life (2)"],
        ["rainforest", "rain + forest", "rain-for-est (3)"],
        ["birdsong", "bird + song", "bird-song (2)"],
        ["sunlight", "sun + light", "sun-light (2)"],
    ]),
    P("**Ojo:** *jaguar*, *habitat* y *forest* tienen varias sílabas, pero **no** son compuestas: no se pueden partir en dos palabras con significado."),
    PB,

    H1("4. Listening (Escuchar)"),
    H2("Práctica: A Visit to the Park"),
    P("Carlos visita el Parque Natural Metropolitano con una guía. **Primera vez:** solo escucha. **Segunda vez:** responde."),
    audio("04"),
    P("**Ejemplo:** The park is a habitat for many ______.  →  **animals**"),
    ITEMS("1. When can you see the monkeys?"), OPTS("a) at night", "b) in the morning", "c) in the afternoon"),
    ITEMS("2. What do sloths eat? ______________"),
    ITEMS("3. Sloths are the ______________ mammals in the forest."),
    ITEMS("4. Which animal is more colorful?"), OPTS("a) the sloth", "b) the toucan", "c) the monkey"),
    ITEMS("5. Park rules: don't ______________ the animals, and don't ______________ them."),
    *test_blocks(TESTS["listening"], audio),
    PB,

    H1("5. Reading (Leer)"),
    H2("Práctica: el texto y una tabla"),
    P("**A. True or False** (texto: *Panama, A Home for Wildlife*). Escribe T o F. Si es falso, corrige la oración."),
    P("**Ejemplo:** The harpy eagle is Panama's national bird. → **T**"),
    ITEMS("1. Panama has more than 900 species of birds. ______", "2. The golden frog lives near the beach. ______",
          "3. The harpy eagle hunts monkeys and sloths. ______", "4. Sea turtles make their nests in the morning. ______"),
    P("**B. Lee la tabla y responde.** Las tablas aparecen mucho en las pruebas: primero lee los **títulos de las columnas**."),
    P("**Animals of Panama** (datos aproximados de animales adultos)", ),
    CHART,
    ITEMS("1. Which animal is the heaviest? ______________",
          "2. What does the harpy eagle eat? ______________",
          "3. Is the howler monkey in danger? ______________",
          "4. Is the sea turtle heavier than the harpy eagle? ______________",
          "5. Name two animals that are active during the day. ______________"),
    P("**C. Sílabas.** Divide cada palabra en sílabas y escribe cuántas tiene. Marca con ✓ las que son **compuestas**."),
    P("**Ejemplo:** rainforest → **rain-for-est (3) ✓**"),
    ITEMS("1. animal → ______________", "2. wildlife → ______________", "3. jaguar → ______________", "4. sunlight → ______________"),
    *test_blocks(TESTS["reading"], audio),
    PB,

    H1("6. Writing (Escribir)"),
    H2("Práctica"),
    P("**A. Completa con there is o there are.**"),
    P("**Ejemplo:** ______ a sloth in the tree. → **There is**"),
    ITEMS("1. ______________ many species of frogs in Panama.", "2. ______________ a big river near the forest.",
          "3. ______________ any jaguars in the city? (pregunta)", "4. ______________ a lot of turtles on the beach."),
    P("**B. Escribe el comparativo o el superlativo.**"),
    ITEMS("1. The jaguar is ______________ (heavy) than the sloth.", "2. The harpy eagle is ______________ (strong) eagle in Panama.",
          "3. The toucan is ______________ (colorful) than the sloth.", "4. The golden frog is ______________ (small) than the sea turtle.",
          "5. The sloth is ______________ (slow) animal in the park."),
    P("**C. Escribe sobre un animal de la tabla.** Completa el modelo en tu cuaderno."),
    P("*The ________ lives in the ________. It eats ________. It is ________ than the ________. It is / isn't endangered.*"),
    *test_blocks(TESTS["writing"], audio),
    PB,

    H1("7. Speaking (Hablar)"),
    H2("Práctica: escucha, repite y grábate"),
    P("**Paso 1.** Escucha cada oración y repítela en la pausa."),
    P("**Paso 2.** Grábate diciendo las mismas oraciones."),
    P("**Paso 3.** Compara tu grabación con el audio. ¿Dijiste *species* con \"sh\" (SPÍ-shiz)? ¿*Habitat* con \"j\" suave (JÁ-bi-tat)?"),
    audio("06"),
    ITEMS(*[f"{i+1}. {s}" for i, s in enumerate(SPEAK_MODELS)]),
    P("**Prepara una mini-exposición.** Elige un animal de Panamá y prepara 5 oraciones: dónde vive, qué come, con qué otro animal lo comparas y por qué hay que protegerlo."),
    *test_blocks(TESTS["speaking"], audio),
    PB,

    H1("8. Mediation (Ayudar a otros a entender)"),
    P("En este tema vas a practicar **dar instrucciones claras con ayuda de dibujos o gestos**, como hace un guía en un parque."),
    H2("Práctica"),
    P("**A. Reglas con dibujos.** Escribe 3 reglas para visitar un parque, en inglés simple, y haz un dibujo pequeño junto a cada una."),
    P("**Ejemplo:** *Don't feed the animals.* + dibujo de una mano con comida y una X."),
    LINES(3),
    P("**B. Simplifica.** Un compañero no entiende este letrero. Escríbelo en **2 oraciones cortas**."),
    NOTE("Letrero", "*Visitors are kindly requested to refrain from feeding the wildlife, as human food may cause serious health problems to the animals.*"),
    LINES(2),
    P("**C. Del español al inglés.** Explica este letrero a un turista que solo habla inglés."),
    NOTE("Letrero", "Prohibido sacar plantas del parque."),
    LINES(1),
    *test_blocks(TESTS["mediation"], audio),
    PB,

    H1("¿Cómo me fue en el Tema 2.1?"),
    P("Anota tus puntajes. Te dicen qué repasar antes de una prueba."),
    TABLE([2600, 1600, 5600], ["Mini-test", "Puntaje", "Si tuviste menos de la mitad, repasa..."], [
        ["Listening", "___ / 6", "El Consejo de Listening (anotar números) y el audio 04 en velocidad lenta"],
        ["Reading", "___ / 6", "La tabla *Animals of Panama* y el Consejo de Reading"],
        ["Writing", "___ / 10", "Gramática A (there is / there are) y B (comparativos)"],
        ["Speaking", "___ / 8", "El audio 06 y la mini-exposición sobre un animal"],
        ["Mediation", "___ / 8", "Cómo dar instrucciones que empiezan con un verbo"],
    ]),
    TABLE([6400, 1100, 1100, 1200], ["Puedo...", "Sí", "Casi", "Todavía no"], [
        ["nombrar animales de Panamá y su hábitat", "☐", "☐", "☐"],
        ["usar *there is / there are* correctamente", "☐", "☐", "☐"],
        ["comparar animales (*heavier than, the strongest*)", "☐", "☐", "☐"],
        ["leer una tabla y encontrar información", "☐", "☐", "☐"],
        ["dividir palabras en sílabas y reconocer palabras compuestas", "☐", "☐", "☐"],
    ]),
    PB,

    H1("Respuestas del Tema 2.1"),
    P("Corrige **solo después de terminar**. Si te equivocaste, lee la explicación: ahí está lo que necesitas aprender."),
    H3("Listening — Práctica"),
    ITEMS("1. **b) in the morning.** *You can see them in the morning.*",
          "2. **leaves.** *They eat leaves.*",
          "3. **slowest.** *Sloths are the slowest mammals in the forest.*",
          "4. **b) the toucan.** *The toucan is more colorful than the sloth.*",
          "5. **feed** and **touch.** *Don't feed the animals, and don't touch them.*"),
    *answer_blocks(TESTS["listening"]),
    H3("Reading — Práctica"),
    ITEMS("A1. **T.**   A2. **F.** It lives **in the mountains** near El Valle de Antón.   A3. **T.**   A4. **F.** They make their nests **at night**.",
          "B1. **the jaguar** (about 90 kg).   B2. **monkeys and sloths.**   B3. **No, it isn't.**   B4. **Yes, it is** (40 kg es más que 7 kg).",
          "B5. Dos de estos: **harpy eagle, howler monkey, golden frog** (también el sloth, que está activo de día y de noche).",
          "C1. **an-i-mal (3)**   C2. **wild-life (2) ✓**   C3. **jag-uar (2)**   C4. **sun-light (2) ✓**. Solo *wildlife* y *sunlight* son compuestas."),
    *answer_blocks(TESTS["reading"]),
    H3("Writing — Práctica"),
    ITEMS("A1. **There are** (many species = varias)   A2. **There is** (a big river = una)   A3. **Are there**   A4. **There are**",
          "B1. **heavier** (y → ier)   B2. **the strongest**   B3. **more colorful** (palabra larga)   B4. **smaller**   B5. **the slowest**",
          "C. Respuesta libre. Ejemplo: *The howler monkey lives in the rainforest. It eats leaves and fruit. It is heavier than the sloth. It isn't endangered.*"),
    *answer_blocks(TESTS["writing"]),
    H3("Mediation — ejemplos de respuesta"),
    ITEMS("Práctica A: *Don't feed the animals.* · *Don't touch the animals.* · *Be quiet.* · *Don't throw trash.*",
          "Práctica B: *Don't feed the animals. Our food makes them sick.*",
          "Práctica C: *Don't take plants from the park.*"),
    *answer_blocks(TESTS["mediation"]),
    PB,

    H1("Transcripciones de los audios del Tema 2.1"),
    P("Si no puedes escuchar un audio, pide a alguien que lo lea o léelo tú en voz alta. Úsalas también para revisar lo que no entendiste."),
    {"t": "transcripts"},
]
