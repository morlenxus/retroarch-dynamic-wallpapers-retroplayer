"""Read-only GIMP 3 audit: runpy.run_path(...)["audit"]()."""

import colorsys
import hashlib
import json
from pathlib import Path

from gi.repository import Gegl, Gimp, Gio

ROOT = Path(__file__).resolve().parents[1]


def audit():
    manifest = json.loads((ROOT / "backgrounds/generation-manifest.json").read_text())
    assets = {ROOT / a["xcf"]: a for a in manifest["assets"]}
    sources = set(ROOT.rglob("*.xcf"))
    if sources != set(assets):
        raise RuntimeError("XCF files and manifest assets do not match")
    report = []
    geometry = {
        "Border X": (1920, 80, 0, 233),
        "Border Y": (1920, 1080, 0, 0),
        "Box, Shadow Big": (208, 163, 432, 191),
        "Box, Shadow Small": (156, 144, 458, 391),
    }
    for path in sorted(sources):
        asset = assets[path]
        image = Gimp.file_load(Gimp.RunMode.NONINTERACTIVE, Gio.File.new_for_path(str(path)))
        try:
            assert (image.get_width(), image.get_height()) == (1920, 1080), path
            group = next(l for l in image.get_layers() if l.get_name() == "Fading")
            assert group.get_visible() and abs(group.get_opacity() - 100) < 0.001, path
            layers = {l.get_name(): l for l in group.get_children()}
            assert len(layers) == 7, path
            for name, style in manifest["menu_overlay_style"].items():
                layer = layers[name]
                assert layer.get_visible() == style["visible"], (path, name)
                assert abs(layer.get_opacity() - style["opacity"]) < 0.001, (path, name)
            borders = {}
            for name, expected_geometry in geometry.items():
                layer = layers[name]
                actual = (layer.get_width(), layer.get_height(), *layer.get_offsets()[1:])
                assert actual == expected_geometry, (path, name, actual)
                assert layer.get_visible(), (path, name)
                assert not layer.get_lock_content() and not layer.get_lock_position(), (path, name)
                rect = Gegl.Rectangle.new(0, 0, layer.get_width(), layer.get_height())
                data = layer.get_buffer().get(rect, 1.0, "R'G'B'A u8", Gegl.AbyssPolicy.NONE)
                assert any(data[3::4]), (path, name)
                if name not in ("Border X", "Border Y"):
                    continue
                expected_rgb = tuple(int(asset["menu_line_color"][i:i+2], 16) for i in (1, 3, 5))
                opaque = [tuple(data[i:i+3]) for i in range(0, len(data), 4) if data[i+3] == 255]
                assert opaque, (path, name)
                assert all(max(abs(a-b) for a, b in zip(rgb, expected_rgb)) <= 2 for rgb in opaque), (path, name)
                borders[name] = {
                    "opacity": round(layer.get_opacity(), 2),
                    "color": asset["menu_line_color"],
                    "geometry": actual,
                    "alpha_sha256": hashlib.sha256(data[3::4]).hexdigest(),
                    "visible": True,
                    "editable": True,
                }
            h, lightness, saturation = colorsys.rgb_to_hls(*(v/255 for v in expected_rgb))
            assert abs(lightness - manifest["menu_line_style"]["lightness_hsl"]) < 0.005, path
            assert saturation <= manifest["menu_line_style"]["maximum_saturation_hsl"] + 0.01, path
            export = ROOT / asset["export"]
            assert export.is_file(), export
            report.append({"xcf": str(path.relative_to(ROOT)), "export": asset["export"], "lines": borders, "frames": "visible, editable, shared geometry", "status": "OK"})
            print("Verified overlays: " + path.name, flush=True)
        finally:
            image.delete()
    output = {"checked_files": len(report), "line_style": manifest["menu_line_style"], "files": report}
    (ROOT / "backgrounds/overlay-audit.json").write_text(json.dumps(output, indent=2) + "\n")
    print(f"PASS: {len(report)} XCF files, both line axes and both cover frames.", flush=True)
