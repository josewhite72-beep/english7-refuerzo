# -*- coding: utf-8 -*-
"""Gramática de consulta rápida (al final del libro)."""
from common import *

IRREG = [("be", "was / were", "ser, estar"), ("go", "went", "ir"), ("have", "had", "tener"), ("eat", "ate", "comer"),
         ("make", "made", "hacer"), ("meet", "met", "conocer"), ("see", "saw", "ver"), ("take", "took", "tomar"),
         ("come", "came", "venir"), ("get", "got", "obtener"), ("give", "gave", "dar"), ("know", "knew", "saber"),
         ("say", "said", "decir"), ("write", "wrote", "escribir"), ("read", "read (\"red\")", "leer"), ("swim", "swam", "nadar"),
         ("run", "ran", "correr"), ("sleep", "slept", "dormir"), ("fly", "flew", "volar"), ("lay", "laid", "poner (huevos)")]

BLOCKS = [
    H1("Gramática de consulta rápida"),
    P("Usa estas páginas la noche antes de una prueba. Al lado de cada tema está **dónde se explica con más detalle**."),

    H2("Presente simple — hábitos y rutinas (Temas 1.1 y 2.2)"),
    TABLE([3300, 3300, 3200], ["Afirmativa", "Negativa", "Pregunta"], [
        ["I / you / we / they **play**", "I **don't** play", "**Do** you play?"],
        ["he / she / it **plays**", "she **doesn't** play", "**Does** she play?"],
    ]),
    P("-s: walk**s** · -es: watch**es**, go**es** · -ies: stud**ies**  ·  Después de *does / doesn't*, el verbo **sin -s**."),
    P("**Frecuencia:** always · usually · often · sometimes · never → **antes del verbo** (*I always walk*) y **después de be** (*She is always late*)."),

    H2("Pasado: was / were y verbos en -ed (Tema 1.2)"),
    P("I / he / she / it **was** · you / we / they **were** · **wasn't / weren't**"),
    P("Regulares: walk**ed**, live**d**, stud**ied**, sto**pped**  ·  Negativa: **didn't** + verbo base  ·  Pregunta: **Did** you + verbo base?"),
    H3("20 verbos irregulares que más se usan"),
    TABLE([1650, 1650, 1650, 1650, 1650, 1650], ["Verbo", "Pasado", "Español", "Verbo", "Pasado", "Español"],
          [[IRREG[i][0], f"**{IRREG[i][1]}**", IRREG[i][2], IRREG[i + 10][0], f"**{IRREG[i + 10][1]}**", IRREG[i + 10][2]] for i in range(10)]),

    H2("Used to — lo que hacías antes (Tema 1.2)"),
    P("*I **used to** walk to school.* · *I **didn't use to** like Math.* · ***Did** you **use to** play?*"),

    H2("Will — futuro (Tema 1.2)"),
    P("*I **will** join the club.* · *We **won't** be late.* · ***Will** you come? — Yes, I **will**. / No, I **won't**.*"),

    H2("There is / There are (Tema 2.1)"),
    P("**There is** + una cosa · **There are** + varias cosas · **Is there…? / Are there…?** · **There isn't / There aren't**"),

    H2("Comparativos y superlativos (Temas 1.2 y 2.1)"),
    TABLE([2500, 2400, 2400, 2500], ["Regla", "Ejemplo", "Comparativo", "Superlativo"], [
        ["Corta", "small", "smaller **than**", "**the** smallest"],
        ["Se dobla la consonante", "big", "bigger than", "the biggest"],
        ["Termina en -y", "noisy", "noisier than", "the noisiest"],
        ["Larga", "modern", "**more** modern than", "**the most** modern"],
        ["Irregular", "good / bad", "better / worse than", "the best / the worst"],
    ]),

    H2("Instrucciones (Tema 2.2)"),
    P("Empiezan con el verbo: ***Choose** a card. **Don't** say the name.*  ·  Orden: **First, Then, Next, Finally**."),

    H2("Pronunciación de terminaciones (Temas 1.1 y 1.2)"),
    TABLE([3300, 3300, 3200], ["-s / -es", "-ed", "Recuerda"], [
        ["/s/ walks, eats", "/t/ walked, helped", "La sílaba extra solo aparece en:"],
        ["/z/ plays, reads", "/d/ played, lived", "-s → después de s, sh, ch, x (watch**es**)"],
        ["/ɪz/ watches, uses", "/ɪd/ planted, wanted", "-ed → después de t o d (plant**ed**)"],
    ]),

    H2("Palabras que se confunden en las pruebas"),
    TABLE([3300, 6500], ["Confusión", "Cómo recordarlo"], [
        ["**than** / **that**", "Para comparar siempre es **than**: *bigger than*."],
        ["**do** / **does**", "**Does** solo con he, she, it. Después, verbo sin -s."],
        ["**there is** / **there are**", "Mira la palabra que sigue: ¿una cosa (is) o varias (are)?"],
        ["**-teen** / **-ty**", "thir**TEEN** (13) acento al final; **THIR**ty (30) acento al inicio."],
        ["**be from** / **live in**", "*I'm from Coclé* = nací allí. *I live in Colón* = vivo allí ahora."],
    ]),
]
