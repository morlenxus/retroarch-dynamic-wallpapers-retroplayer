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


def integrate_device(image, asset):
    """Place the existing device on an editable glass card in the header."""
    device = next(l for l in image.get_layers() if l.get_name() == "Device")
    for layer in list(image.get_layers()):
        if layer.get_name() == "Device presentation":
            image.remove_layer(layer)

    # Some source cutouts have oversized canvases and stray pixels outside the
    # header. Measure the actual device alpha inside its intended header area.
    image.select_item(Gimp.ChannelOps.REPLACE, device)
    image.select_rectangle(Gimp.ChannelOps.INTERSECT, 1500, 40, 420, 190)
    Gimp.Selection.sharpen(image)
    _, nonempty, x1, y1, x2, y2 = Gimp.Selection.bounds(image)
    Gimp.Selection.none(image)
    if not nonempty:
        raise RuntimeError(f"No device cutout in header: {asset['genre']}")
    _, old_x, old_y = device.get_offsets()
    width, height = x2 - x1, y2 - y1
    device.resize(width + 16, height + 16, old_x - x1 + 8, old_y - y1 + 8)
    device.set_offsets(round(1700 - width / 2) - 8, round(130 - height / 2) - 8)

    group = Gimp.GroupLayer.new(image, "Device presentation")
    image.insert_layer(group, None, image.get_item_position(device) + 1)
    Gimp.context_push()
    try:
        def shape(name, color, opacity, x, y, w, h, radius=20, feather=0, ellipse=False):
            layer = Gimp.Layer.new(image, name, 440, 240, Gimp.ImageType.RGBA_IMAGE,
                                   opacity, Gimp.LayerMode.NORMAL)
            image.insert_layer(layer, group, 0)
            layer.set_offsets(1480, 20)
            if ellipse:
                image.select_ellipse(Gimp.ChannelOps.REPLACE, x, y, w, h)
            else:
                image.select_round_rectangle(Gimp.ChannelOps.REPLACE, x, y, w, h, radius, radius)
            if feather:
                Gimp.Selection.feather(image, feather)
            Gimp.context_set_foreground(Gegl.Color.new(color))
            layer.edit_fill(Gimp.FillType.FOREGROUND)
            Gimp.Selection.none(image)
            layer.set_visible(True)

        shape("Soft shadow", "black", 40, 1510, 48, 380, 184, feather=10)
        shape("Glass rim", "#dceaf4", 40, 1510, 38, 380, 184)
        shape("Smoked glass", "#101923", 86, 1512, 40, 376, 180, radius=18)
        accent = asset.get("device_accent", "#7db7ce")
        shape("Ground light", accent, 26, 1580, 184, 240, 15, feather=9, ellipse=True)
        shape("Accent line", accent, 65, 1645, 210, 110, 2, radius=1)
    finally:
        Gimp.Selection.none(image)
        Gimp.context_pop()
    group.set_visible(True)


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
        image = Gimp.file_load(
            Gimp.RunMode.NONINTERACTIVE, Gio.File.new_for_path(str(xcf_path))
        )
        image.undo_disable()
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

        if asset.get("device_presentation"):
            integrate_device(image, asset)

        if not Gimp.file_save(
            Gimp.RunMode.NONINTERACTIVE, image, Gio.File.new_for_path(str(xcf_path))
        ):
            raise RuntimeError(f"XCF save failed: {xcf_path}")
        export_png(image, ROOT / asset["export"])
        image.delete()
        print(f"Updated: {asset['genre']}", flush=True)
