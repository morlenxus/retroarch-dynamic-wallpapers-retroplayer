"""Run inside GIMP 3's python-fu-eval batch interpreter.

Use runpy.run_path(...)["update"]() to rebuild all generated playlist sources and exports.
An optional playlist argument (stored as "genre" in the manifest) rebuilds only that asset. Requires the generated
backgrounds and generation-manifest.json; does not call an image service.
"""

import json
import re
from pathlib import Path

from gi.repository import Gegl, Gimp, Gio


ROOT = Path(__file__).resolve().parents[1]


def remove_device(image):
    """Remove the device cutout and its presentation card from hardware sources."""
    for layer in list(image.get_layers()):
        if layer.get_name() in ("Device", "Device presentation"):
            image.remove_layer(layer)


def style_hardware(image, asset):
    """Apply editable evening lighting and consistent, truly dark text shadows."""
    remove_device(image)
    for layer in list(image.get_layers()):
        if layer.get_name() in ("Evening shading", "Released - shadow"):
            image.remove_layer(layer)

    opacity = asset.get("evening_opacity", 0)
    if opacity:
        surface = next(l for l in image.get_layers() if l.get_name() == "System surface")
        shading = Gimp.Layer.new(image, "Evening shading", image.get_width(),
                                 image.get_height(), Gimp.ImageType.RGBA_IMAGE,
                                 opacity, Gimp.LayerMode.NORMAL)
        image.insert_layer(shading, None, image.get_item_position(surface))
        shading.set_blend_space(Gimp.LayerColorSpace.RGB_PERCEPTUAL)
        shading.set_composite_space(Gimp.LayerColorSpace.RGB_PERCEPTUAL)
        Gimp.context_push()
        try:
            Gimp.Selection.none(image)
            Gimp.context_set_foreground(Gegl.Color.new("black"))
            shading.edit_fill(Gimp.FillType.FOREGROUND)
        finally:
            Gimp.context_pop()
        shading.set_visible(True)

    title = next(l for l in image.get_layers() if l.get_name() == "Released")
    markup = title.get_markup()
    if markup:
        # Inline foreground colors override TextLayer.set_color(), including on
        # copied shadows. Keep sizing/formatting but remove those color overrides.
        title.set_markup(re.sub(r'\s(?:foreground|color)="[^"]*"', "", markup))
    title.set_color(Gegl.Color.new(asset.get("text_color", "#f4f2ed")))
    title.set_visible(True)
    shadow = title.copy()
    image.insert_layer(shadow, None, image.get_item_position(title) + 1)
    shadow.set_color(Gegl.Color.new(asset.get("shadow_color", "black")))
    shadow.set_name("Released - shadow")
    shadow.set_opacity(asset.get("shadow_opacity", 90))
    _, x, y = title.get_offsets()
    shadow.set_offsets(x + 2, y + 2)
    shadow.set_visible(True)


def export_png(image, path):
    # Export a composite of every visible layer, independent of layer selection.
    composite = image.duplicate()
    composite.merge_visible_layers(Gimp.MergeType.CLIP_TO_IMAGE)
    procedure = Gimp.get_pdb().lookup_procedure("file-png-export")
    config = procedure.create_config()
    config.set_property("run-mode", Gimp.RunMode.NONINTERACTIVE)
    config.set_property("image", composite)
    config.set_property("file", Gio.File.new_for_path(str(path)))
    config.set_property("compression", 9)
    for key in ("include-exif", "include-iptc", "include-xmp", "include-thumbnail"):
        config.set_property(key, False)
    result = procedure.run(config)
    composite.delete()
    if result.index(0) != Gimp.PDBStatusType.SUCCESS:
        raise RuntimeError(f"PNG export failed: {path}: {result.index(0)}")


def apply_platform_logo(image, asset):
    """Import the original platform artwork as a separate image layer."""
    for layer in list(image.get_layers()):
        if layer.get_name() in (
            "Platform title", "Platform title - shadow", "Platform accent",
            "Platform logo",
        ):
            image.remove_layer(layer)
    logo = Gimp.file_load_layer(
        Gimp.RunMode.NONINTERACTIVE, image,
        Gio.File.new_for_path(str(ROOT / asset["platform_logo"])),
    )
    logo.set_name("Platform logo")
    image.insert_layer(logo, None, 0)
    width = asset.get("platform_logo_width", 384)
    height = round(width * logo.get_height() / logo.get_width())
    Gimp.context_push()
    try:
        Gimp.context_set_interpolation(Gimp.InterpolationType.NOHALO)
        logo.scale(width, height, False)
    finally:
        Gimp.context_pop()
    logo.set_offsets(*asset.get("platform_logo_position", [30, 89]))
    logo.set_visible(True)


def initialize_hardware_header(image, asset):
    """Retain the template's SEGA wordmark and set the new release year."""
    keep = set(asset["template_brand_layers"])
    for layer in list(image.get_layers()):
        if layer.get_name().startswith("Logo") and layer.get_name() not in keep:
            image.remove_layer(layer)
    released = next(l for l in image.get_layers() if l.get_name() == "Released")
    markup = released.get_markup()
    text = f"Released: {asset['release_year']}"
    if markup:
        released.set_markup(re.sub(r"Released: [^<]+", text, markup))
    else:
        released.set_text(text)


def update(genre=None):
    manifest = json.loads((ROOT / "backgrounds/generation-manifest.json").read_text())
    for asset in manifest["assets"]:
        if genre is not None and asset["genre"] != genre:
            continue
        background_path = ROOT / asset["background"]
        background = Gimp.file_load(
            Gimp.RunMode.NONINTERACTIVE, Gio.File.new_for_path(str(background_path))
        )
        if (background.get_width(), background.get_height()) != (1920, 1080):
            Gimp.context_set_interpolation(Gimp.InterpolationType.NOHALO)
            background.scale(1920, 1080)
            export_png(background, background_path)
        background.delete()

        xcf_path = ROOT / asset["xcf"]
        is_new = not xcf_path.exists()
        source_path = ROOT / asset["template_xcf"] if is_new else xcf_path
        image = Gimp.file_load(
            Gimp.RunMode.NONINTERACTIVE, Gio.File.new_for_path(str(source_path))
        )
        image.undo_disable()
        if is_new:
            initialize_hardware_header(image, asset)
        if asset.get("platform_logo"):
            apply_platform_logo(image, asset)
        original_layers = list(image.get_layers())
        for layer in original_layers:
            if layer.get_name() in (
                "Genre collage", "Playlist collage", "System surface",
                "Background", "Background (old)"
            ):
                image.remove_layer(layer)
        collage = Gimp.file_load_layer(
            Gimp.RunMode.NONINTERACTIVE, image,
            Gio.File.new_for_path(str(background_path)),
        )
        collage.set_name(asset.get("collage_layer", "Genre collage"))
        image.insert_layer(collage, None, len(image.get_layers()))
        collage.set_visible(True)
        for layer in image.get_layers():
            if layer.get_name() == "Fading" or isinstance(layer, Gimp.TextLayer):
                layer.set_visible(True)

        if asset.get("logo_shadow_color"):
            Gimp.context_push()
            try:
                Gimp.context_set_foreground(Gegl.Color.new(asset["logo_shadow_color"]))
                for logo in list(image.get_layers()):
                    if not logo.get_name().startswith("Logo") or logo.get_name().endswith(" - contrast"):
                        continue
                    name = logo.get_name() + " - contrast"
                    if any(l.get_name() == name for l in image.get_layers()):
                        continue
                    shadow = logo.copy()
                    shadow.set_name(name)
                    image.insert_layer(shadow, None, image.get_item_position(logo) + 1)
                    shadow.set_lock_alpha(True)
                    shadow.edit_fill(Gimp.FillType.FOREGROUND)
                    shadow.set_lock_alpha(False)
                    _, x, y = logo.get_offsets()
                    shadow.set_offsets(x + 3, y + 3)
                    shadow.set_visible(True)
            finally:
                Gimp.context_pop()

        for title in (l for l in original_layers if isinstance(l, Gimp.TextLayer)):
            if title.get_name().endswith(" - shadow"):
                continue
            shadow_name = title.get_name() + " - shadow"
            if not any(l.get_name() == shadow_name for l in image.get_layers()):
                shadow = title.copy()
                shadow.set_name(shadow_name)
                image.insert_layer(shadow, None, image.get_item_position(title) + 1)
                _, x, y = title.get_offsets()
                shadow.set_offsets(x + 2, y + 2)
                shadow.set_color(Gegl.Color.new(asset.get("shadow_color", "black")))
                shadow.set_visible(True)
            if asset.get("text_color") and title.get_markup():
                title.set_markup(re.sub(r'\s(?:foreground|color)="[^"]*"', "", title.get_markup()))
            title.set_color(Gegl.Color.new(asset.get("text_color", "white")))

        if asset.get("design") == "hardware-surface":
            style_hardware(image, asset)

        if not Gimp.file_save(
            Gimp.RunMode.NONINTERACTIVE, image, Gio.File.new_for_path(str(xcf_path))
        ):
            raise RuntimeError(f"XCF save failed: {xcf_path}")
        export_png(image, ROOT / asset["export"])
        image.delete()
        print(f"Updated: {asset['genre']}", flush=True)
