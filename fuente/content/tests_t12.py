# -*- coding: utf-8 -*-
"""Mini-tests del Tema 1.2 (fuente única para el libro y la versión en línea)."""
from common import *

TESTS = {
 "listening": {"skill": "listening", "total": 6,
  "tip": ["Escucha bien los números que se parecen: four**teen** (14) y **for**ty (40). En *-teen* el acento va al final; en *-ty*, al inicio.",
          "Fíjate si la pregunta habla del pasado (**was, did, used to**) o del presente (**is, does, now**)."],
  "review": "El Consejo de Listening (números *-teen* y *-ty*) y el audio 04 en velocidad lenta",
  "parts": [{"intro": "Escucha a Elena hablar de su escuela anterior y de su escuela nueva. Puedes escuchar **dos veces como máximo**.",
             "audio": "05", "qs": [
    {"t": "mc", "q": "Where is Elena from?", "opts": ["Penonomé", "Antón", "Colón"], "a": 1,
     "exp": "*I'm from Antón, in Coclé.* Penonomé es donde estudia **ahora**."},
    {"t": "mc", "q": "How many students were there in her old school?", "opts": ["14", "40", "500"], "a": 1,
     "exp": "Elena dice *forty* (40), con el acento al inicio: FOR-ty. *Fourteen* (14) lleva el acento al final."},
    {"t": "mc", "q": "What did the students do every Friday?", "opts": ["They cleaned the garden.", "They played music.", "They ate in the cafeteria."], "a": 0,
     "exp": "*Every Friday, we cleaned the school garden together.*"},
    {"t": "mc", "q": "Her new school is ______ than her old school.", "opts": ["smaller and quieter", "bigger and noisier", "older"], "a": 1,
     "exp": "*It is much bigger and noisier.*"},
    {"t": "tf", "q": "Classes at her new school finish at 12:00.", "a": False,
     "exp": "Terminan a la una y media (*one thirty*). Las doce (*twelve*) era la hora de salida en su escuela **anterior**."},
    {"t": "tf", "q": "Elena used to play the guitar at home.", "a": True, "exp": "*I used to play the guitar alone at home.*"},
  ]}]},

 "reading": {"skill": "reading", "total": 6,
  "tip": ["Las preguntas con **Why?** se responden con **because**. Busca en el texto la palabra *so* o *because*: ahí suele estar la razón."],
  "review": "La lectura de Luis y cómo responder preguntas con *Why? — Because...*",
  "parts": [{"intro": "Lee lo que cuenta el abuelo Tomás sobre su escuela y responde.",
             "reading": {"title": "Grandpa's School", "paras": [
                "When I was a boy, my school was a wooden house with only one classroom. There were thirty students of different ages and only one teacher, Miss Carmen.",
                "We didn't have notebooks, so we wrote on small blackboards. We walked two kilometers to school every day, in rain or sun! At recess, we played marbles and ate mangoes from the trees.",
                "Today, schools are bigger and more modern, and students use computers. But I think my old school was the happiest place in the world."]},
             "qs": [
    {"t": "mc", "q": "Grandpa's school had ______.", "opts": ["one classroom", "two classrooms", "thirty classrooms"], "a": 0,
     "exp": "*Thirty* es el número de estudiantes, no de salones."},
    {"t": "short", "q": "Who was the teacher? ______________________",
     "accept": [["miss carmen", "carmen", "the teacher was miss carmen"]], "show": "**Miss Carmen.**"},
    {"t": "short", "q": "Why did they write on small blackboards? ______________________________________",
     "accept": [["~notebook"]], "show": "**Because they didn't have notebooks.**",
     "exp": "En el texto: *We didn't have notebooks, **so** we wrote on small blackboards.* La palabra *so* (por eso) marca la razón."},
    {"t": "tf", "q": "The students walked to school.", "a": True, "exp": "*We walked two kilometers to school every day.*"},
    {"t": "tf", "q": "At recess, they used computers.", "a": False,
     "exp": "Jugaban canicas (*marbles*) y comían mangos. Las computadoras son de las escuelas de **hoy**."},
    {"t": "mc", "q": "What does Grandpa think about his old school?", "opts": ["It was the biggest school.", "It was the happiest place in the world.", "It was very modern."], "a": 1},
  ]}]},

 "writing": {"skill": "writing", "total": 10,
  "tip": ["Antes de entregar, busca en tu texto los verbos en pasado. ¿Tienen **-ed** o son irregulares? ¿Después de *didn't* quitaste la -ed?"],
  "review": "Gramática A (was/were), B (pasado y *didn't*) y E (comparativos)",
  "parts": [
   {"intro": "**Parte A. Cada oración tiene un error. Escríbela correctamente.** (1 punto cada una)", "qs": [
    {"t": "fix", "q": "My old school were small.", "accept": ["my old school was small"], "show": "My old school **was** small.", "exp": "*school* es singular → *was*"},
    {"t": "fix", "q": "I used to walked to school.", "accept": ["i used to walk to school"], "show": "I used to **walk** to school.", "exp": "después de *used to*, verbo base"},
    {"t": "fix", "q": "My new school is more big than my old school.", "accept": ["my new school is bigger than my old school"], "show": "My new school is **bigger** than my old school.", "exp": "*big* es corta: no se usa *more*"},
    {"t": "fix", "q": "We didn't had a garden.", "accept": ["we didnt have a garden", "we did not have a garden"], "show": "We didn't **have** a garden.", "exp": "después de *didn't*, verbo base"},
    {"t": "fix", "q": "The cafeteria is the noisyest place.", "accept": ["the cafeteria is the noisiest place"], "show": "The cafeteria is the **noisiest** place.", "exp": "*noisy*: la y cambia a i → noisiest"},
   ]},
   {"intro": "**Parte B.** Imagina que ya estás en tu escuela nueva. Escribe un correo de **4 a 6 oraciones** a un amigo de tu escuela anterior. (5 puntos)",
    "open": {"lines": 6, "min_sent": 4, "max_sent": 6, "check_intro": "**Revisa tu correo.** Marca un punto por cada casilla:", "checklist": [
      {"text": "Tiene saludo y despedida (*Hi, Ana! … Your friend, …*).", "auto": r"^\s*(hi|hello|dear|hey)\b"},
      {"text": "Describí mi escuela anterior con **was / were**.", "auto": r"\b(was|were)\b"},
      {"text": "Comparé las dos escuelas (*bigger than, more modern than…*).", "auto": r"\b\w+er than\b|\bmore \w+ than\b|\bthe \w+est\b|\bthe most\b"},
      {"text": "Usé **used to** o un verbo en pasado.", "auto": r"\bused to\b|\b\w+ed\b|\b(went|had|ate|made|met|saw|took|came)\b"},
      {"text": "Escribí un plan con **will**.", "auto": r"\bwill\b|'ll\b"}],
     "sample": "Hi, Ana! I'm in my new school now. My old school was small and quiet, but this school is bigger and more modern. I used to walk to school, but now I take the bus. Next week, I will join the music club. Your friend, Luis."}},
  ]},

 "speaking": {"skill": "speaking", "total": 8,
  "tip": ["Si te preguntan en pasado, responde en pasado: *What **was** it like? — It **was**...*  ·  *How **did** you go? — I **walked**.*"],
  "review": "Gramática C (pronunciación de -ed) y el audio 06",
  "parts": [{"intro": "Activa la grabadora de tu celular y luego reproduce el audio. Responde cada pregunta en voz alta **durante la pausa**.",
             "audio": "07",
             "open": {"record": True, "check_intro": "Después, escucha tu grabación y marca un punto por cada casilla:", "checklist": [
               {"text": "Pregunta 1 con oración completa"}, {"text": "Pregunta 2 con oración completa"}, {"text": "Pregunta 3 con oración completa"},
               {"text": "Pregunta 4 con oración completa"}, {"text": "Pregunta 5 con oración completa"}, {"text": "Usé **was / were** correctamente"},
               {"text": "Usé un comparativo (*bigger, smaller, more modern…*)"}, {"text": "Pronuncié la -ed sin agregar sílabas de más"}]}}]},

 "mediation": {"skill": "mediation", "total": 8,
  "tip": ["Al resumir lo que dijo alguien, revisa los pronombres: **I → he/she**, **my → his/her**, **we → they**."],
  "review": "Cómo cambiar *I → he / she* al resumir",
  "parts": [
   {"intro": "**Parte A.** Diego, un compañero nuevo, se presentó en clase. Escribe un resumen de **2 o 3 oraciones** para tu profesor.",
    "note": ["Presentación de Diego", "*Hi! I'm Diego. My previous school was in Aguadulce. It was smaller than this school, but it had a swimming pool! I used to swim every Wednesday. I want to join the swimming team here.*"],
    "open": {"lines": 3, "min_sent": 2, "max_sent": 3, "checklist": [
      {"text": "Dije dónde estaba su escuela anterior.", "auto": r"\baguadulce\b"},
      {"text": "Incluí una comparación (*smaller than…*).", "auto": r"\b\w+er than\b|\bmore \w+ than\b"},
      {"text": "Dije lo que él solía hacer (*used to swim*).", "auto": r"\bused to swim\b|\bswam\b"},
      {"text": "Cambié a tercera persona (*he, his*).", "auto": r"\b(he|his|diego'?s)\b"},
      {"text": "Usé oraciones cortas y claras."}],
     "sample": "Diego's previous school was in Aguadulce. It was smaller than this school, but it had a swimming pool. He used to swim every Wednesday, and he wants to join the swimming team."}},
   {"intro": "**Parte B.** Simplifica este aviso en **1 o 2 oraciones** para un compañero nuevo.",
    "note": ["Aviso", "*Due to the rain, the outdoor sports activities scheduled for this afternoon have been moved to the gym, and students should bring their sports shoes.*"],
    "open": {"lines": 2, "min_sent": 1, "max_sent": 2, "checklist": [
      {"text": "Dije **dónde** es ahora la actividad (*in the gym*).", "auto": r"\bgym\b"},
      {"text": "Dije **cuándo** (*this afternoon*).", "auto": r"\bafternoon\b|\btoday\b"},
      {"text": "Dije **qué traer** (*sports shoes*).", "auto": r"\bshoes\b"}],
     "sample": "It's raining. This afternoon, sports are in the gym. Bring your sports shoes."}},
  ]},
}
