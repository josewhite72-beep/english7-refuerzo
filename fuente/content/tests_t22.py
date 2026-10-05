# -*- coding: utf-8 -*-
"""Mini-tests del Tema 2.2 (fuente única para el libro y la versión en línea)."""
from common import *

TESTS = {
 "listening": {"skill": "listening", "total": 6,
  "tip": ["Cuando el audio cuenta una historia en orden, fíjate en las palabras **First, Then, At noon, In the afternoon**: te dicen en qué parte del día pasó cada cosa."],
  "review": "El Consejo de Listening (First, Then, At noon) y el audio 04 en velocidad lenta",
  "parts": [{"intro": "Escucha a Javier contar el paseo de su clase a Gamboa. Puedes escuchar **dos veces como máximo**.",
             "audio": "05", "qs": [
    {"t": "mc", "q": "When did the class go to the rainforest?", "opts": ["last Saturday", "last Sunday", "last Friday"], "a": 0},
    {"t": "mc", "q": "What did they hear first?", "opts": ["toucans", "howler monkeys", "hawks"], "a": 1,
     "exp": "*First, we heard the howler monkeys.* La palabra **First** te da la respuesta."},
    {"t": "short", "q": "Why were most animals resting at noon? ______________________________",
     "accept": [["~hot"]], "show": "**Because it was very hot.**"},
    {"t": "mc", "q": "How long did the sloth stay still?", "opts": ["one minute", "one hour", "one day"], "a": 1, "exp": "*It didn't move for one hour!*"},
    {"t": "tf", "q": "The hawks migrate every October.", "a": True, "exp": "*They migrate from North America to South America every October.*"},
    {"t": "tf", "q": "The students saw the bats.", "a": False, "exp": "*We went home at five, **before** the bats came out.* Se fueron antes de que salieran."},
  ]}]},

 "reading": {"skill": "reading", "total": 6,
  "tip": ["Las preguntas de selección múltiple a veces tienen **dos opciones que aparecen en el texto**. Lee la oración completa para ver cuál responde exactamente la pregunta."],
  "review": "El horario *Animal Schedules* y el Consejo de Reading",
  "parts": [{"intro": "Lee el texto sobre las hormigas arrieras y responde.",
             "reading": {"title": "The Busy Leafcutter Ants", "paras": [
                "Leafcutter ants are some of the busiest animals in Panama's forests. You can see them on long trails, carrying pieces of green leaves. Each piece is bigger than the ant!",
                "But the ants don't eat the leaves. They take them to their nest under the ground. There, they use the leaves to grow a special fungus, and they eat the fungus.",
                "Some ants cut leaves, some carry them, and some clean the nest. Big ants protect the trail from predators. Leafcutter ants often work at night, but they sometimes work during the day too. A big nest can have millions of ants!"]},
             "qs": [
    {"t": "mc", "q": "Where is the ants' nest?", "opts": ["in the trees", "under the ground", "near the river"], "a": 1, "exp": "*Their nest under the ground.*"},
    {"t": "short", "q": "Do the ants eat the leaves? ______________________________",
     "accept": [["no", "no they dont", "no they do not", "~no fungus"]], "show": "**No, they don't.**", "exp": "They eat a fungus (un hongo)."},
    {"t": "short", "q": "What do the big ants do? ______________________________",
     "accept": [["~protect"]], "show": "**They protect the trail from predators.**"},
    {"t": "tf", "q": "Each piece of leaf is smaller than the ant.", "a": False, "exp": "*Each piece is **bigger** than the ant.*"},
    {"t": "tf", "q": "Leafcutter ants never work during the day.", "a": False,
     "exp": "*They **sometimes** work during the day too.* **Never** sería 0 %, y el texto dice *sometimes*."},
    {"t": "mc", "q": "How many ants can live in a big nest?", "opts": ["hundreds", "thousands", "millions"], "a": 2},
  ]}]},

 "writing": {"skill": "writing", "total": 10,
  "tip": ["En instrucciones, revisa que cada paso **empiece con un verbo** y que uses **First, Then, Finally** para ordenarlos."],
  "review": "Gramática A (frecuencia), C (preguntas con *does*) y D (instrucciones)",
  "parts": [
   {"intro": "**Parte A. Cada oración tiene un error. Escríbela correctamente.** (1 punto cada una)", "qs": [
    {"t": "fix", "q": "The owl hunt at night.", "accept": ["the owl hunts at night"], "show": "The owl **hunts** at night.", "exp": "*the owl* = it → -s"},
    {"t": "fix", "q": "Bats sleeps during the day.", "accept": ["bats sleep during the day"], "show": "Bats **sleep** during the day.", "exp": "*bats* = they → sin -s"},
    {"t": "fix", "q": "Sloths move always slowly.", "accept": ["sloths always move slowly"], "show": "Sloths **always move** slowly.", "exp": "la palabra de frecuencia va antes del verbo"},
    {"t": "fix", "q": "Does the toucan eats fruit?", "accept": ["does the toucan eat fruit"], "show": "Does the toucan **eat** fruit?", "exp": "después de *does*, verbo sin -s"},
    {"t": "fix", "q": "Not touch the animals!", "accept": ["dont touch the animals", "do not touch the animals"], "show": "**Don't touch** the animals!", "exp": "la negación en instrucciones es *Don't*"},
   ]},
   {"intro": "**Parte B.** Escribe las instrucciones del juego **Guess the Animal** en **4 o 5 pasos**. (5 puntos)",
    "open": {"lines": 5, "min_sent": 4, "max_sent": 5, "check_intro": "**Revisa tus instrucciones.** Marca un punto por cada casilla:", "checklist": [
      {"text": "Cada paso empieza con un verbo (*Choose, Describe, Guess…*).", "auto": r"\b(choose|describe|guess|take|say|read|change|write|pick)\b"},
      {"text": "Usé **First**, **Then** y **Finally**.", "auto": r"(?=.*\bfirst\b)(?=.*\bthen\b)(?=.*\bfinally\b)"},
      {"text": "Incluí una regla con **Don't**.", "auto": r"\bdon'?t\b|\bdo not\b"},
      {"text": "Expliqué cómo se gana o cuántas oportunidades hay.", "auto": r"\bchances?\b|\bwin|\bpoints?\b|\btries\b"},
      {"text": "Cada oración empieza con mayúscula y termina con punto.", "auto": "caps"}],
     "sample": "First, choose an animal card. Don't show it to your partner. Then, describe the animal's habits. Your partner has three chances to guess. Finally, change roles."}},
  ]},

 "speaking": {"skill": "speaking", "total": 8,
  "tip": ["Para explicar las reglas de un juego, ordénalas: **First…, Then…, Finally…** Así quien te escucha (o te evalúa) te sigue fácilmente."],
  "review": "El audio 06 y el juego con tus 3 animales",
  "parts": [{"intro": "Activa la grabadora de tu celular y luego reproduce el audio. Responde cada pregunta en voz alta **durante la pausa**.",
             "audio": "07",
             "open": {"record": True, "check_intro": "Después, escucha tu grabación y marca un punto por cada casilla:", "checklist": [
               {"text": "Pregunta 1: describí al menos 2 hábitos"}, {"text": "Pregunta 2: dije **nocturnal** o **diurnal** y por qué"},
               {"text": "Pregunta 3: usé **always**"}, {"text": "Pregunta 4: usé **First**, **Then** y **Don't**"}, {"text": "Pregunta 5 con oración completa"},
               {"text": "Pronuncié la -s con *it / he / she*"}, {"text": "Hablé sin leer"}, {"text": "No usé español"}]}}]},

 "mediation": {"skill": "mediation", "total": 8,
  "tip": ["Divide las instrucciones largas en **pasos numerados**. Cada paso, una sola acción."],
  "review": "Cómo dividir una instrucción larga en pasos",
  "parts": [
   {"intro": "**Parte A.** Convierte esta instrucción larga en **3 pasos cortos y numerados**, y haz un dibujo pequeño para cada paso.",
    "note": ["Instrucción", "*For today's activity, each student will select one animal card from the box, then write three sentences describing the animal's daily habits without mentioning its name, and finally read the description aloud so that classmates can guess the animal.*"],
    "open": {"lines": 3, "min_sent": 3, "max_sent": 5, "checklist": [
      {"text": "Paso 1 correcto (tomar una tarjeta)", "auto": r"\bcard\b"},
      {"text": "Paso 2 correcto (escribir 3 oraciones sobre sus hábitos)", "auto": r"\bwrite\b.*\b(3|three)\b|\bhabits\b"},
      {"text": "Incluí la regla: no escribir el nombre (*Don't…*)", "auto": r"\bdon'?t\b.*\bname\b|\bdo not\b.*\bname\b"},
      {"text": "Paso 3 correcto (leer en voz alta; los demás adivinan)", "auto": r"\bread\b|\bguess"},
      {"text": "Hice un dibujo para cada paso"}],
     "sample": "1. Take an animal card. 2. Write 3 sentences about its habits. Don't write its name. 3. Read your sentences. Your classmates guess."}},
   {"intro": "**Parte B.** Un visitante que solo habla inglés llega a tu salón. Traduce este cartel en **inglés simple**.",
    "note": ["Cartel", "Levanta la mano para hablar y no corras en el salón."],
    "open": {"lines": 2, "min_sent": 1, "max_sent": 2, "checklist": [
      {"text": "Escribí *Raise your hand*.", "auto": r"\braise your hand\b|\bput your hand up\b"},
      {"text": "Escribí *to talk / to speak*.", "auto": r"\bto (talk|speak)\b"},
      {"text": "Escribí *Don't run in the classroom*.", "auto": r"\bdon'?t run\b|\bdo not run\b|\bno running\b"}],
     "sample": "Raise your hand to talk. Don't run in the classroom."}},
  ]},
}
