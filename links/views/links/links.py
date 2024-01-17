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
            "icons/laptop-code-solid.svg"
        ),
        link_button(
            "Excercism",
            "Realiza ejercicios del lenguaje que quieras",
            "https://exercism.org/dashboard",
            "icons/laptop-code-solid.svg"
        ),
        link_button(
            "IDE online",
            "Ejecuta codigo python online",
            "https://www.online-python.com/",
            "icons/laptop-code-solid.svg"
        ),
        title("Mecanografia"),
        link_button(
            "Keybr",
            "Practica mecanografia",
            "https://www.keybr.com/",
            "icons/keyboard-regular.svg"
        ),
        link_button(
            "Agilefingers",
            "Practica Mecanografia",
            "https://agilefingers.com/es/textos/texto-ejemplo",
            "icons/keyboard-regular.svg"
        ),
        width="100%",
        spacing=Size.MEDIUM.value,
        align_items="center",
        style = {
            "background_color":"#0C151D"
        },
    )   
