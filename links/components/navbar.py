import reflex as rx
from links.styles.styles import Size as Size
from links.styles.colors import Colors as Colors
import links.styles.styles as styles

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.span("Jan", color =Colors.PRIMARY.value),
            rx.span("dv", color= Colors.SECONDARY.value),
            style =styles.title_style_navbar
        ),
        position ="sticky",
        bg = Colors.CONTENT.value,
        padding_x = Size.BIG.value,
        padding_y = Size.DEFAULT.value,
        z_index = "999",
        top="0"
    )   
