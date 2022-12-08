from catppuccin import Flavour

from .utils import replacetext
from .var import (def_accent_dark, def_accent_light, def_color_map, src_dir,
                  theme_name, work_dir)


def recolor_accent(color, file: str, accent: str = "blue"):
    """
    Recolors the accent color in a file.
    color:
        The color scheme to recolor to. Like mocha, frappe, latte, etc.
    file:
        The file to modify
    accent:
        The accent color to replace. Defaults to Blue
    """
    print(f"Recoloring accent for {file}...")
    # Recolor as per accent for light. Hard code it as latte
    for key, value in Flavour.latte().__dict__.items():
        if key == accent:
            replacetext(
                file, def_accent_light[def_color_map[accent]], value.hex)

    # Recolor as per base for dark theme.
    for key, value in color.__dict__.items():
        if key == accent:
            replacetext(
                file, def_accent_dark[def_color_map[accent]], value.hex)


def recolor(color, accent: str):
    """
    Recolor the theme. currently hard code it frappe
    """
    print("Recoloring to suit catppuccin theme")
    replacetext(f"{work_dir}/install.sh", "Colloid", theme_name)

    print("MOD: Gtkrc.sh")
    # Recolor as per accent for dark
    recolor_accent(color, f"{work_dir}/gtkrc.sh", accent)

    replacetext(f"{work_dir}/gtkrc.sh", "background_light='#FFFFFF'",
                f"background_light='#{Flavour.latte().base.hex}'")  # use latte_base for background_light
    replacetext(f"{work_dir}/gtkrc.sh", "background_dark='#0F0F0F'",
                f"background_dark='#{color.base.hex}'")
    replacetext(f"{work_dir}/gtkrc.sh", "background_darker='#121212'",
                f"background_darker='#{color.mantle.hex}'")
    replacetext(f"{work_dir}/gtkrc.sh",
                "background_alt='#212121'", f"background_alt='#{color.crust.hex}'")
    replacetext(f"{work_dir}/gtkrc.sh", "titlebar_light='#F2F2F2'",
                f"titlebar_light='#{Flavour.latte().crust.hex}'")  # use latte_crust for titlebar_light
    replacetext(f"{work_dir}/gtkrc.sh", "titlebar_dark='#030303'",
                f"titlebar_dark='#{color.crust.hex}'")
    replacetext(f"{work_dir}/gtkrc.sh", "background_dark='#2C2C2C'",
                f"background_dark='#{color.base.hex}'")
    replacetext(f"{work_dir}/gtkrc.sh", "background_darker='#3C3C3C'",
                f"background_darker='#{color.mantle.hex}'")
    replacetext(f"{work_dir}/gtkrc.sh",
                "background_alt='#464646'", f"background_alt='#{color.crust.hex}'")
    replacetext(f"{work_dir}/gtkrc.sh",
                "titlebar_light='#F2F2F2'", f"titlebar_light='#{Flavour.latte().crust.hex}'")
    replacetext(f"{work_dir}/gtkrc.sh",
                "titlebar_dark='#242424'", f"titlebar_dark='#{color.crust.hex}'")

    print("Mod SASS Color_Palette_default")
    recolor_accent(
        color, f"{src_dir}/sass/_color-palette-default.scss", accent)

    # Greys
    if color == Flavour.latte():  # Hardcode till someone smarter than me comes along
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-050: #FAFAFA", f"grey-050: #{color.crust.hex}")
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-100: #F2F2F2", f"grey-100: #{color.mantle.hex}")
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-150: #EEEEEE", f"grey-150: #{color.base.hex}")
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-200: #DDDDDD", f"grey-200: #{color.surface0.hex}")  # Surface 0 Late
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-250: #CCCCCC", f"grey-250: #{color.surface1.hex}")  # D = Surface 1 Late
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-650: #3C3C3C", f"grey-650: #{Flavour.mocha().surface0.hex}")  # H $surface $tooltip
        replacetext(f"{src_dir}/sass/_color-palette-default.scss", "grey-700: #2C2C2C",
                    f"grey-700: #{Flavour.mocha().base.hex}")  # G $background; $base; titlebar-backdrop; $popover
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-750: #242424", f"grey-750: #{Flavour.mocha().crust.hex}")  # F $base-alt
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-800: #212121", f"grey-800: #{Flavour.mocha().crust.hex}")  # E $panel-solid;p
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-850: #121212", f"grey-850: #{Flavour.mocha().surface1.hex}")  # H Darknes
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-900: #0F0F0F", f"grey-900: #{Flavour.mocha().base.hex}")  # G Darknes
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-950: #030303", f"grey-950: #{Flavour.mocha().crust.hex}")  # F Darknes
    else:
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-050: #FAFAFA", f"grey-050: #{color.overlay2.hex}")
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-100: #F2F2F2", f"grey-100: #{color.overlay1.hex}")
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-150: #EEEEEE", f"grey-150: #{color.overlay0.hex}")
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-200: #DDDDDD", f"grey-200: #{color.surface2.hex}")  # Surface 0 Late
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-250: #CCCCCC", f"grey-250: #{color.surface1.hex}")  # D = Surface 1 Late
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-650: #3C3C3C", f"grey-650: #{color.surface0.hex}")  # H $surface $tooltip
        replacetext(f"{src_dir}/sass/_color-palette-default.scss", "grey-700: #2C2C2C",
                    f"grey-700: #{color.base.hex}")  # G $background; $base; titlebar-backdrop; $popover
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-750: #242424", f"grey-750: #{color.crust.hex}")  # F $base-alt
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-800: #212121", f"grey-800: #{color.crust.hex}")  # E $panel-solid;p
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-850: #121212", f"grey-850: #{color.surface1.hex}")  # H Darknes
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-900: #0F0F0F", f"grey-900: #{color.base.hex}")  # G Darknes
        replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                    "grey-950: #030303", f"grey-950: #{color.crust.hex}")  # F Darknes

    # Buttons
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "button-close: #fd5f51", f"button-close: #{color.red.hex}")
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "button-max: #38c76a", f"button-max: #{color.green.hex}")
    replacetext(f"{src_dir}/sass/_color-palette-default.scss",
                "button-min: #fdbe04", f"button-min: #{color.yellow.hex}")

    print("Mod Accent Cinnamon")
    recolor_accent(color, f"{src_dir}/assets/cinnamon/make-assets.sh", accent)

    print("Mod Accent Gnome shell")
    recolor_accent(
        color, f"{src_dir}/assets/gnome-shell/make-assets.sh", accent)

    print("Mod Accent GTK")
    recolor_accent(color, f"{src_dir}/assets/gtk/make-assets.sh", accent)

    print("Mod Accent GTK 2.0")
    recolor_accent(color, f"{src_dir}/assets/gtk-2.0/make-assets.sh", accent)