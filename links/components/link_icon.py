import reflex as rx 
from links.styles.styles import Size as Size

def link_icon(image:str, url: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=Size.DEFAULT.value,
            border_radius = "8px"
        ),
        href=url,
        is_external=True
    )
