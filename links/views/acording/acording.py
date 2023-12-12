from os import link
import reflex as rx
from links.components.title import title
from links.components.link_button import link_button
from links.styles.styles import Size as Size


def acordingPython() -> rx.Component:
    return rx.accordion(
        rx.accordion_item(
            rx.accordion_button(
                title("Librerias Python"),
                rx.accordion_icon(),
            ),
            rx.accordion_panel(
                rx.vstack(
                    link_button(
                        "Numpy",
                        """Tabaja con arreglos, matrices y una gran variedad de funciones
                    matematicas.""",
                        "https://numpy.org/doc/stable/",
                    ),
                    link_button(
                        "Pandas",
                        "utilizada para manipular, analizar y visualizar datos de manera eficiene",
                        "https://numpy.org/doc/stable/",
                    ),
                    link_button(
                        "Matplotlip",
                        "Visualizacíon de datos",
                        "https://matplotlib.org/stable/index.html",
                    ),
                    link_button(
                        "Scikit-learn",
                        "Aprendisaje automatico",
                        "https://scikit-learn.org/stable/user_guide.html",
                    ),
                    link_button(
                        "Django",
                        "Nos permite manejar el backend con python",
                        "https://docs.djangoproject.com/en/4.2/",
                    ),
                    margin=Size.MEDIUM.value,
                ),
            ),
            border_top_width="inherit !important",
        ),
        allow_toggle=True,
        width="100%",
        align_items="center",
        border_bottom_width="none",
    )


def acording_front() -> rx.Component:
    return rx.accordion(
        rx.accordion_item(
            rx.accordion_button(
                title("Herramientas Frontend"),
                rx.accordion_icon(),
            ),
            rx.accordion_panel(
                rx.vstack(
                    link_button(
                        "Google fonts",
                        "Amplia gama de fuentas",
                        "https://fonts.google.com/",
                    ),
                    link_button(
                        "Gradiente de colores",
                        "Podras elegir el gradiente y copiar el codigo",
                        "https://mycolor.space/gradient3?ori=circle&hex=%23FBA70C&hex2=%236FD909&hex3=%23FB430C&submit=submit",
                    ),
                    link_button(
                        "Plantillas para html",
                        "variedad de plantillas para tu pagina",
                        "https://html5up.net/",
                    ),
                    link_button(
                        "Css reference",
                        "Ideas y componentes con css puro",
                        "https://cssreference.io/",
                    ),
                    margin=Size.MEDIUM.value,
                ),
            ),
            border_top_width="inherit !important",
        ),
        allow_toggle=True,
        width="100%",
        align_items="center",
    )
