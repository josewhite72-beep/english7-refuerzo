# -*- coding: utf-8 -*-
"""Mini-tests del Tema 2.1 (fuente única para el libro y la versión en línea)."""
from common import *

TESTS = {
 "listening": {"skill": "listening", "total": 6,
  "tip": ["Cuando el audio da **varios números** (fechas, cantidades, días), anótalos al margen mientras escuchas. Después decide cuál responde cada pregunta."],
  "review": "El Consejo de Listening (anotar números) y el audio 04 en velocidad lenta",
  "parts": [{"intro": "Escucha un reporte de noticias sobre las tortugas marinas de Isla Cañas. Puedes escuchar **dos veces como máximo**.",
             "audio": "05", "qs": [
    {"t": "mc", "q": "Where is Isla Cañas?", "opts": ["in Bocas del Toro", "in Los Santos", "in Darién"], "a": 1, "exp": "*Isla Cañas, a small island in Los Santos.*"},
    {"t": "mc", "q": "When do the turtles come out of the ocean?", "opts": ["in the morning", "at noon", "at night"], "a": 2, "exp": "*They come out of the ocean at night.*"},
    {"t": "mc", "q": "How many eggs does each turtle lay?", "opts": ["about 15", "about 50", "about 100"], "a": 2,
     "exp": "*Each turtle lays about one hundred eggs.* El 50 es el número de **días** que tardan en salir las tortuguitas: era una trampa."},
    {"t": "mc", "q": "After about fifty days, the baby turtles...", "opts": ["walk to the ocean.", "stay in the nest.", "fly away."], "a": 0},
    {"t": "tf", "q": "Crabs and birds eat baby turtles.", "a": True, "exp": "*Many animals eat the baby turtles: birds, crabs, and dogs.*"},
    {"t": "tf", "q": "You can use lights on the beach at night.", "a": False, "exp": "*Don't use lights on the beach at night. Lights confuse the turtles.*"},
  ]}]},

 "reading": {"skill": "reading", "total": 6,
  "tip": ["Si una pregunta dice **Why…?**, busca en el texto **because** o **so**. Si dice **How heavy / How long…?**, busca un número con su unidad (kg, m)."],
  "review": "La tabla *Animals of Panama* y el Consejo de Reading",
  "parts": [{"intro": "Lee el texto sobre los manatíes y responde.",
             "reading": {"title": "Gentle Giants: The Manatees", "paras": [
                "Manatees are big, gentle animals. They live in warm rivers and lagoons. In Panama, there are manatees in Bocas del Toro, in the San San River.",
                "An adult manatee can be three meters long, and it can weigh more than 400 kilograms. Manatees are herbivores: they eat water plants for many hours every day. They swim slowly and come up to breathe air every few minutes.",
                "Manatees have no natural predators, but they are in danger. Boats hit them, and people pollute the rivers. Scientists in Bocas protect the manatees and teach people about them."]},
             "qs": [
    {"t": "mc", "q": "Where are there manatees in Panama?", "opts": ["in Darién", "in Bocas del Toro", "in Los Santos"], "a": 1, "exp": "*In the San San River.*"},
    {"t": "short", "q": "How heavy can an adult manatee be? ______________________",
     "accept": [["~400", "~four hundred"]], "show": "**More than 400 kilograms.**"},
    {"t": "short", "q": "What do manatees eat? ______________________",
     "accept": [["~plant"]], "show": "**Water plants.**", "exp": "(*They are herbivores*: solo comen plantas.)"},
    {"t": "tf", "q": "Manatees swim fast.", "a": False, "exp": "*They swim slowly.*"},
    {"t": "tf", "q": "Manatees have a lot of natural predators.", "a": False,
     "exp": "*Manatees have **no** natural predators.* Ojo con la palabra **no**: cambia todo el significado."},
    {"t": "short", "q": "Why are manatees in danger? ______________________________________",
     "accept": [["~boat", "~pollut"]], "show": "**Because boats hit them and people pollute the rivers.**", "exp": "(Con una de las dos razones vale el punto.)"},
  ]}]},

 "writing": {"skill": "writing", "total": 10,
  "tip": ["Revisa **there is / there are** mirando la palabra que sigue: ¿es una cosa o varias? Y en comparativos, nunca juntes **more** con **-er**."],
  "review": "Gramática A (there is / there are) y B (comparativos)",
  "parts": [
   {"intro": "**Parte A. Cada oración tiene un error. Escríbela correctamente.** (1 punto cada una)", "qs": [
    {"t": "fix", "q": "There is many species in Panama.", "accept": ["there are many species in panama"], "show": "There **are** many species in Panama.", "exp": "*many species* = varias cosas"},
    {"t": "fix", "q": "The jaguar is more big than the ocelot.", "accept": ["the jaguar is bigger than the ocelot"], "show": "The jaguar is **bigger** than the ocelot.", "exp": "*big* es corta: no lleva *more*"},
    {"t": "fix", "q": "The sloth is the most slow animal.", "accept": ["the sloth is the slowest animal"], "show": "The sloth is **the slowest** animal.", "exp": "*slow* es corta → *the slowest*"},
    {"t": "fix", "q": "The harpy eagle is stronger that the hawk.", "accept": ["the harpy eagle is stronger than the hawk"], "show": "The harpy eagle is stronger **than** the hawk.", "exp": "para comparar se usa *than*, no *that*"},
    {"t": "fix", "q": "There are a golden frog in El Valle.", "accept": ["there is a golden frog in el valle", "theres a golden frog in el valle"], "show": "There **is** a golden frog in El Valle.", "exp": "*a golden frog* = una sola"},
   ]},
   {"intro": "**Parte B.** Escribe una **tarjeta informativa** de 4 a 5 oraciones sobre un animal de Panamá (puedes usar la tabla). (5 puntos)",
    "open": {"lines": 5, "min_sent": 4, "max_sent": 5, "check_intro": "**Revisa tu tarjeta.** Marca un punto por cada casilla:", "checklist": [
      {"text": "Dije el nombre del animal y su hábitat.", "auto": r"\blives? in\b|\bhabitat\b"},
      {"text": "Usé **there is** o **there are**.", "auto": r"\bthere (is|are)\b|\bthere'?s\b"},
      {"text": "Escribí un comparativo (*bigger than, more colorful than…*).", "auto": r"\b\w+er than\b|\bmore \w+ than\b"},
      {"text": "Escribí un superlativo o dije si está **endangered**.", "auto": r"\bthe \w+est\b|\bthe most\b|\bendangered\b|\bin danger\b"},
      {"text": "Cada oración empieza con mayúscula y termina con punto.", "auto": "caps"}],
     "sample": "The harpy eagle lives in the rainforest. There are harpy eagles in Darién. It is heavier than the howler monkey. It is one of the strongest eagles in the world. It is endangered, so we must protect it."}},
  ]},

 "speaking": {"skill": "speaking", "total": 8,
  "tip": ["Para dar tu opinión, empieza con **In my opinion,...** o **I think...** y explica con **because**."],
  "review": "El audio 06 y la mini-exposición sobre un animal",
  "parts": [{"intro": "Activa la grabadora de tu celular y luego reproduce el audio. Responde cada pregunta en voz alta **durante la pausa**.",
             "audio": "07",
             "open": {"record": True, "check_intro": "Después, escucha tu grabación y marca un punto por cada casilla:", "checklist": [
               {"text": "Pregunta 1 con oración completa"}, {"text": "Pregunta 2: usé **there are**"}, {"text": "Pregunta 3: usé un comparativo"},
               {"text": "Pregunta 4: usé un superlativo y **because**"}, {"text": "Pregunta 5 con oración completa"},
               {"text": "Usé al menos 3 palabras del vocabulario"}, {"text": "Hablé sin leer"}, {"text": "No usé español"}]}}]},

 "mediation": {"skill": "mediation", "total": 8,
  "tip": ["Para dar instrucciones, empieza con el verbo: **Walk…, Be…, Take…, Don't…**  Una idea por oración."],
  "review": "Cómo dar instrucciones que empiezan con un verbo",
  "parts": [
   {"intro": "**Parte A.** Tu clase va a un parque. Un compañero nuevo no entiende español. Escribe las instrucciones de la guía en **3 oraciones cortas en inglés** y haz un dibujo junto a cada una.",
    "note": ["Instrucciones de la guía", "Caminen siempre por el sendero. No hagan ruido para no asustar a los animales. Lleven su basura de regreso a casa."],
    "open": {"lines": 3, "min_sent": 3, "max_sent": 3, "checklist": [
      {"text": "Instrucción 1 correcta (sendero = *trail*)", "auto": r"\btrail\b|\bpath\b"},
      {"text": "Instrucción 2 correcta (ruido = *noise*; también puedes usar *Be quiet*)", "auto": r"\bnoise\b|\bquiet\b"},
      {"text": "Instrucción 3 correcta (basura = *trash*)", "auto": r"\btrash\b|\bgarbage\b|\brubbish\b"},
      {"text": "Cada instrucción empieza con un verbo"},
      {"text": "Hice un dibujo para cada instrucción"}],
     "sample": "Walk on the trail. Don't make noise. (o Be quiet.) Take your trash home."}},
   {"intro": "**Parte B.** Simplifica este aviso en **1 o 2 oraciones** para un compañero.",
    "note": ["Aviso", "*Due to the nesting season, access to the beach after 6:00 p.m. is restricted to authorized personnel only.*"],
    "open": {"lines": 2, "min_sent": 1, "max_sent": 2, "checklist": [
      {"text": "Dije **cuándo** (*after 6 p.m.*).", "auto": r"\b6\b|\bsix\b"},
      {"text": "Dije **qué no se puede hacer** (ir a la playa).", "auto": r"\bbeach\b"},
      {"text": "Dije **por qué** (las tortugas hacen nidos).", "auto": r"\bnest|\bturtle"}],
     "sample": "After 6 p.m., you can't go to the beach. The turtles are making nests."}},
  ]},
}
