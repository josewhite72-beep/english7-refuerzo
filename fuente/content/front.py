# -*- coding: utf-8 -*-
"""Portada e introducción del cuadernillo."""
SITE = "english7-refuerzo.vercel.app"

BLOCKS = [
    {"t": "book_cover",
     "title": "English 7",
     "subtitle": "Libro de refuerzo · I Trimestre",
     "desc": "Para estudiar en casa, a tu ritmo, cuando sientas que lo necesitas.",
     "contents": ["Repaso de 6°", "Scenario 1: Our New Classmates", "   Theme 1: Where are you from?", "   Theme 2: What Was Your Previous School Like?",
                  "Scenario 2: Panama's Wildlife", "   Theme 1: The Habitat of Wildlife", "   Theme 2: The Daily Habits of Animals", "Gramática de consulta rápida"],
     "author": "José White · PanaMentorLabs"},
    {"t": "h1", "text": "Cómo usar este libro"},
    {"t": "p", "text": "Este libro sigue los temas del **I Trimestre de 7° grado** del programa de inglés de MEDUCA. Cuando tu profesor empiece un tema en clase, búscalo aquí por su nombre (Scenario y Theme)."},
    {"t": "p", "text": "Antes del primer tema hay un **Repaso de 6°**, y al final del libro, una **Gramática de consulta rápida** para la noche antes de una prueba."},
    {"t": "h3", "text": "Cada tema tiene estas partes"},
    {"t": "bullets", "items": [
        "**¿Te sientes perdido? Empieza aquí:** lo esencial del tema en una página.",
        "**Vocabulario, Lectura y Gramática:** lo que necesitas saber, explicado en español.",
        "**Listening, Reading, Writing, Speaking y Mediation:** una práctica y un **mini-test** de cada destreza, como los de una prueba.",
        "**¿Cómo me fue?:** anota tus puntajes y descubre qué repasar.",
        "**Respuestas:** al final de cada tema, con la explicación de cada error. Corrige **solo después de terminar**."]},
    {"t": "h3", "text": "Los audios"},
    {"t": "p", "text": "Donde veas un código QR, hay un audio. Ábrelo con la cámara de tu celular o escribe la dirección que aparece al lado. Puedes escucharlo las veces que quieras y también **en velocidad lenta**."},
    {"t": "p", "text": f"Todos los audios están en: **{SITE}**"},
    {"t": "p", "text": "Si no tienes internet, al final de cada tema están las **transcripciones** (el texto de cada audio)."},
    {"t": "h3", "text": "Consejos para estudiar solo"},
    {"t": "bullets", "items": [
        "Estudia en sesiones cortas: **20 minutos** cada día rinden más que 3 horas un solo día.",
        "Escribe tus respuestas en tu cuaderno si quieres usar el libro otra vez.",
        "Para Speaking, usa la **grabadora de tu celular**: escucharte es la mejor forma de mejorar.",
        "Equivocarse es parte de aprender. Lo importante es leer la explicación y volver a intentarlo."]},
    {"t": "pb"},
]
