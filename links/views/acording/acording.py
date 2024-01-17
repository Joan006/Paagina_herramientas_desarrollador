from os import link
import reflex as rx
from links.components.title import title
from links.components.link_button import link_button
from links.styles.styles import Size as Size
from links.styles.colors import TextColor as TextColor


def acordingPython() -> rx.Component:
    return rx.accordion(
        rx.accordion_item(
            rx.accordion_button(
                title(
                    "Librerias Python",
                ),
                rx.accordion_icon(
                    color=TextColor.HEADER.value, font_size=Size.LARGE.value
                ),
                text_align="justify",
            ),
            rx.accordion_panel(
                rx.vstack(
                    link_button(
                        "Numpy",
                        """Variedad de funciones
                    matematicas.""",
                        "https://numpy.org/doc/stable/",
                        "icons/terminal-solid.svg",
                    ),
                    link_button(
                        "Pandas",
                        "Manipular, analizar y visualizar datos",
                        "https://numpy.org/doc/stable/",
                        "icons/terminal-solid.svg",
                    ),
                    link_button(
                        "Matplotlip",
                        "Visualizacíon de datos",
                        "https://matplotlib.org/stable/index.html",
                        "icons/terminal-solid.svg",
                    ),
                    link_button(
                    "Scikit-learn",
                    "Aprendisaje automatico",
                    "https://scikit-learn.org/stable/user_guide.html",
                    "icons/terminal-solid.svg",
                ),
                link_button(
                    "Django",
                    "Manejar backend con python",
                    "https://docs.djangoproject.com/en/4.2/",
                    "icons/terminal-solid.svg",
                ),
                margin=Size.MEDIUM.value,
            ),
        ),
        border_bottom_width="inherit !important",
        border_top_width="inherit !important",
        margin_top=Size.MEDIUM.value,
    ),
    allow_toggle=True,
    width="100%",
    align_items="center",
    border_bottom_width="none",
        margin_top=Size.MEDIUM.value,
    )


def acording_front() -> rx.Component:
    return rx.accordion(
        rx.accordion_item(
            rx.accordion_button(
                title("Herramientas Frontend"),
                rx.accordion_icon(
                    color=TextColor.HEADER.value, font_size=Size.LARGE.value
                ),
                text_align="justify",
            ),
            rx.accordion_panel(
                rx.vstack(
                    link_button(
                        "Google fonts",
                        "Amplia gama de fuentas",
                        "https://fonts.google.com/",
                        "icons/mug-saucer-solid.svg",
                    ),
                    link_button(
                        "FontAwesome",
                        "Iconos para tu web",
                        "https://fontawesome.com/",
                        "icons/mug-saucer-solid.svg",
                    ),
                    link_button(
                        "Icons8",
                        "Iconos para tu web",
                        "https://iconos8.es/",
                        "icons/mug-saucer-solid"
                    ),
                    link_button(
                        "Gradiente de colores",
                        "Podras elegir el gradiente",
                        "https://mycolor.space/gradient3?ori=circle&hex=%23FBA70C&hex2=%236FD909&hex3=%23FB430C&submit=submit",
                        "icons/mug-saucer-solid.svg",
                    ),
                    link_button(
                        "RGBA Color Picker",
                        "Elegir color rgba",
                        "https://rgbacolorpicker.com/#google_vignette",
                        "icons/mug-saucer-solid"
                    ),
                    link_button(
                        "Plantillas para html",
                        "Plantillas para tu pagina",
                        "https://html5up.net/",
                        "icons/mug-saucer-solid.svg",
                    ),
                    link_button(
                        "Css reference",
                        "Ideas y componentes",
                        "https://cssreference.io/",
                        "icons/mug-saucer-solid.svg",
                    ),
                    link_button(
                        "ui Verse",
                        "Componentes UI",
                        "https://uiverse.io/",
                        "icons/mug-saucer-solid"
                    ),
                    link_button(
                        "TW Elements",
                        "Componentes Tailwind",
                        "https://tw-elements.com/",
                        "icons/mug-saucer-solid"
                    ),
                    margin=Size.MEDIUM.value,
                ),
            ),
            border_bottom_width="inherit !important",
            border_top_width="inherit !important",
            margin_top=Size.MEDIUM.value,
        ),
        allow_toggle=True,
        width="100%",
        align_items="center",
        border_bottom_width="none",
    )


