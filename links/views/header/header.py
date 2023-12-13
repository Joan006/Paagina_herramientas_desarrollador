import reflex as rx
from links.components.link_icon import link_icon
from links.styles.styles import Size as Size
from links.styles.colors import TextColor as TextColor
from links.styles.fonts import Font as Font 


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(name="Joan Martinez", size="xl"),
            rx.vstack(
                rx.heading(
                    "Joan Martinez",
                    size="lg",
                    font_family = Font.TITLE.value,
                    color = TextColor.HEADER.value,
                ),
                rx.text(
                    "@joanmtz",
                    margin_top="0px !important"
                ),
                rx.hstack(
                    link_icon("https://x.com/mouredev"),
                    link_icon("https://x.com/mouredev"),
                    link_icon("https://x.com/mouredev")
                ),
                align_items="start",
                color = TextColor.BODY.value
            ),
            spacing=Size.MEDIUM.value,
        ),
        rx.text(
            """
            Soy Joan Martinez , soy un estudiante de programacion , y esta pagina sera para tener 
            las herramientas que ocupo a lo largo de mi desarrollo.
            """,
            color = TextColor.BODY.value,
            font_size = Size.DEFAULT.value
        ),
        spacing=Size.BIG.value,
        align_items="start"
    )
