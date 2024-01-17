"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from os import link
from rxconfig import config
import reflex as rx
from links.components.navbar import navbar
from links.views.header.header import header
from links.views.links.links import links
from links.components.footer import footer
import links.styles.styles as styles
from links.styles.styles import Size as Size
from links.views.acording.acording import acordingPython, acording_front


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                acording_front(),
                acordingPython(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding = Size.BIG.value
            ),
        ),
        footer(),
        background_color = "#0C151D",
    )


# Add state and page to the app.
app = rx.App(style=styles.BASE_STYLE)
app.add_page(index, title="Janv || Herramientas de Desarrollador")
