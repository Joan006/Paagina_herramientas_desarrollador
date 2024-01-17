import reflex as rx 
from enum import Enum
from .colors import Colors as Colors 
from .colors import TextColor as TextColor
from .fonts import Fonts as Fonts
# constants
MAX_WIDTH = "600px"

# sizes 

class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em" 
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"


# styles

BASE_STYLE = {
    "font-family": Fonts.DEFAULT.value,
    "background_color":"#0C151D",
    rx.Button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Colors.CONTENT.value,
        "_hover": {
            "background_color": Colors.SECONDARY.value
        }
    },
    rx.Link: {
        "text_decoration": "none",
        "_hover": {}
    }
}
    
title_style_navbar = dict (
    font_family = Fonts.LOGO.value,
    font_size = Size.LARGE.value        
)

title_style = dict (
    width="100%",
    padding_top =Size.DEFAULT.value,
    color = TextColor.HEADER.value
)

button_title_style = dict(
    font_size = Size.DEFAULT.value,
    color = TextColor.HEADER.value

)

button_body_style = dict (
    font_size = Size.MEDIUM.value,
    color = TextColor.BODY.value,
)
