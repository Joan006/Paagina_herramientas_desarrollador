import reflex as rx
from links.components.link_button import link_button
from links.components.title import title
from links.styles.styles import Size as Size

# importamos acordeon


def links() -> rx.Component:
    return rx.vstack(
        title("Paginas de Consulta en General"),
        link_button(
            "Developer Mozilla",
            "Consulta sobre lenguajes",
            "https://developer.mozilla.org/es/",
            "icons/code-solid.svg"
        ),
        link_button(
            "w3schools",
            "Consulta sobre lengujaes",
            "https://www.w3schools.com/",
            "icons/code-solid.svg"
        ),
        link_button(
            "devdocs", 
            "Consulta sobre lenguajes", 
            "https://devdocs.io/",
            "icons/code-solid.svg"
        ),
        title("Practica Programacion"),
        link_button(
            "freecodecamp",
            "Aprende desde cero a programar",
            "https://www.freecodecamp.org/learn/",
            "icons/code-solid.svg"
        ),
        link_button(
            "Excercism",
            "Realiza ejercicios del lenguaje que quieras",
            "https://exercism.org/dashboard",
            "icons/code-solid.svg"
        ),
        link_button(
            "IDE online",
            "Ejecuta codigo python online",
            "https://www.online-python.com/",
            "icons/code-solid.svg"
        ),
        width="100%",
        spacing=Size.MEDIUM.value,
        align_items="center"
    )
