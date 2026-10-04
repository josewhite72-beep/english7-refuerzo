# -*- coding: utf-8 -*-
"""Repaso de 6° (al inicio) — lo que los temas de 7° dan por sabido."""
from common import *

BLOCKS = [
    H1("Repaso de 6°: lo que necesitas saber"),
    P("Los temas de 7° usan cosas que viste en 6°. Si algo de esta página no lo recuerdas, **repásalo antes de empezar**: te ahorrará muchos errores."),
    H2("1. El verbo to be (ser / estar) en presente"),
    TABLE([3300, 3300, 3200], ["Afirmativa", "Negativa", "Pregunta"], [
        ["I **am** (I'm) twelve.", "I'**m not** tired.", "**Am** I late?"],
        ["You / We / They **are** (you're…)", "They **aren't** here.", "**Are** you ready?"],
        ["He / She / It **is** (he's…)", "She **isn't** sick.", "**Is** it big?"],
    ]),
    H2("2. Pronombres y posesivos"),
    P("Los vas a usar mucho, sobre todo para **hablar de otra persona** (Mediation)."),
    TABLE([1950, 1950, 1950, 1950, 2000], ["Sujeto", "Posesivo", "Sujeto", "Posesivo", "Ejemplo"], [
        ["I", "**my**", "we", "**our**", "*This is **my** school.*"],
        ["you", "**your**", "they", "**their**", "*They love **their** teacher.*"],
        ["he", "**his**", "she", "**her**", "*She lost **her** pen.*"],
        ["it", "**its**", "", "", "*The bird is in **its** nest.*"],
    ]),
    H2("3. Palabras para preguntar"),
    TABLE([2000, 2500, 5300], ["Palabra", "Significa", "Ejemplo"], [
        ["**What**", "¿Qué? / ¿Cuál?", "What is your name?"],
        ["**Where**", "¿Dónde?", "Where are you from?"],
        ["**When**", "¿Cuándo?", "When is your English class?"],
        ["**Who**", "¿Quién?", "Who is your teacher?"],
        ["**Why**", "¿Por qué? (se responde con *because*)", "Why do you like English? — Because…"],
        ["**How** / **How many** / **How old**", "¿Cómo? / ¿Cuántos? / ¿Qué edad?", "How many students are there?"],
    ]),
    H2("4. Números y horas"),
    P("**Números que se confunden:** thir**teen** (13) / **thir**ty (30) · four**teen** (14) / **for**ty (40) · fif**teen** (15) / **fif**ty (50). En *-teen* el acento va al final; en *-ty*, al inicio."),
    P("**La hora:** *seven o'clock* (7:00) · *seven fifteen* (7:15) · *seven thirty* (7:30) · *at noon* (12:00 del día) · *at midnight* (12:00 de la noche)."),
    P("**Días:** Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday  ·  **Meses:** January, February, March, April, May, June, July, August, September, October, November, December"),
    H2("5. Mini-chequeo"),
    P("Responde rápido. Si fallas más de 2, vuelve a leer esta página."),
    ITEMS("1. She ______ (be) from Colón.", "2. We ______ (be) in seventh grade.", "3. This is Mateo and ______ (his / her) sister.",
          "4. ______ is your birthday? — In May.", "5. Escribe el número: forty = ______", "6. ______ you twelve? — Yes, I am."),
    P("*Respuestas: 1. is · 2. are · 3. his (Mateo es él) · 4. When · 5. 40 · 6. Are*"),
    PB,
]
