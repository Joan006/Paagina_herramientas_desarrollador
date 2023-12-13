import reflex as rx
import datetime
from links.styles.styles import Size as Size
from links.styles.colors import TextColor as TextColor



def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="ipn.png",
            height = Size.VERY_BIG.value   
        ),
        rx.link(
            f"(a) 2014-{datetime.date.today().year} Joan Martinez Olivares.",
            href="https://mouredev.com",
            is_external=True,
            font_size = Size.MEDIUM.value,
        ),
        rx.text(
            "PAGINA DE HERRAMIENTAS DE DESARROLLADOR.",
            font_size= Size.MEDIUM.value,
        ),
        margin_bottom = Size.BIG.value,
        padding = Size.BIG.value,
        color = TextColor.FOOTER.value
    )
