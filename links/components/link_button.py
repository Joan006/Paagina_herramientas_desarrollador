import reflex as rx
import links.styles.styles as styles
from links.styles.styles import Size as Size

def link_button(title:str, body:str,url:str, image:str ) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src = image,
                    font_size =Size.LARGE.value,
                    heigth = Size.BIG.value,
                    margin = Size.SMALL.value
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing = Size.SMALL.value,
                    align_items="start",
                    margin = Size.ZERO.value,
                )
            )
        ),
        href=url,
        is_external=True,
        width="100%"
    )
