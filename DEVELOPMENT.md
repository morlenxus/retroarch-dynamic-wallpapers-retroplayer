# Development Notes

Technical details for editing and rebuilding the wallpapers. Users only need
the files in `dist/` (see [README](README.md)).

## Files and naming

- `backgrounds/` – generated artwork at 1920 × 1080, without titles or frames.
- `src/` – layered GIMP 3 sources (`.xcf`); artwork, titles, shadows, logos,
  frames and lines are separate, editable layers.
- `dist/` – PNG exports used by RetroArch. Alternative playlist names
  (e.g. `Nintendo - Handheld - 1989 - Game Boy.png`) are symlinks to the main
  export and pick up changes automatically.
- `icons/` – 256 × 256 transparent playlist icons.
- Filename stems match across `backgrounds/`, `src/`, `dist/` and `icons/`,
  including the `- ` and `Z Genre ` prefixes.

## Manifests

- `backgrounds/generation-manifest.json` – image generation prompts and motifs
  per wallpaper, earlier collage prompts, playlist context, per-system shading
  strength and shared style settings (`menu_overlay_style`, `genre_style`,
  `genre_dimming_opacity`, `playlist_dimming_opacity`, asset-specific
  `frame_template`).
- `icons/generation-manifest.json` – icon generation prompts and motifs.

## Layer structure

- **Genres:** artwork in a `Genre still life` layer.
- **Collections** (`- Games List`, `- Multiplayer Games`, `- Netplay Games`):
  artwork in a `Playlist still life` layer.
- **Systems** and `- Controller Settings`: artwork in a `System surface` layer;
  bright materials are dimmed by an editable `Evening shading` layer. Logos and
  `Released` labels are separate layers above.
- **History:** `Playlist collage` with a 12 % `Playlist dimming` layer.
- **Icon strip / frames:** all in the `Fading` group – `Overlay Outside` (35 %),
  `Overlay Inside` (50 %), `Border X` and `Border Y` (85 %), plus cover frames
  and shadows. Line colors are a muted per-wallpaper accent (72 % HSL lightness,
  max. 25 % saturation). `Main Menu`, `Settings` and `Netplay` use the cool-blue
  overlay of the Wii wallpaper via `frame_template`.

## Typography

Titles use warm-white DejaVu Sans Mono Bold with a black shadow. Genre titles
sit centered in a 384 × 66 px area at (30, 23) and shrink to fit; the `GENRE`
caption uses a common area at (30, 87).

## Scripts (run in the GIMP 3 Python console)

```python
ns = runpy.run_path('scripts/update_genre_wallpapers.py')
ns['update']()               # rebuild all XCFs and PNG exports
ns['update']('History')      # rebuild a single asset by its manifest name
ns['update_overlays']()      # refresh only overlay layers and exports

runpy.run_path('scripts/audit_wallpaper_overlays.py')['audit']()
# checks line/frame geometry, colors, opacity and editability;
# report: backgrounds/overlay-audit.json
```

`scripts/png_optimizer.sh` recompresses all PNGs in `dist/` with ImageMagick.

## Shooter genres

The former `Shooter` collection is split into three disjoint playlists. These
are practical menu groups rather than strict genre definitions:

| Playlist | Scope |
|---|---|
| `Z Genre Ego-Shooter` | First-person shooters (Doom, Quake, Half-Life, …), incl. 6DoF Descent games. |
| `Z Genre Action-Shooter` | Run-and-gun, top-down and vehicle action, lightgun and target shooters. |
| `Z Genre Shoot 'em Up` | Scrolling, fixed-screen and rail shooters, plus space combat games. |

## Release years

Release years shown on the system wallpapers use the first (Japanese) hardware
release where applicable, e.g. [Game Gear (1990)](https://www.sega.jp/history/hard/gamegear/)
and [Mega-CD (1991)](https://www.sega.jp/history/hard/mega-cd/index.html).
