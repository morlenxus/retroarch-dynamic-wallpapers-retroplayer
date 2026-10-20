# RetroArch Dynamic Wallpapers – RetroPlayer

This repository contains dynamic **RetroArch wallpapers** designed for the **RetroPlayer** theme.  
The `.xcf` files inside the `src/` directory are the original GIMP source files.  
The `.png` files inside the `dist/` directory are the exported versions used by RetroArch.

Only the exported `.png` files are required for use in RetroArch.

The 18 `Z Genre` wallpapers use generated collages based on selected titles from
the supplied genre playlists. The standalone backgrounds are in `backgrounds/`;
`backgrounds/generation-manifest.json` records the prompts and playlist motifs.
Platformer combines Mario with Yoshi, Sonic, Donkey Kong, Kirby, Mega Man,
Crash Bandicoot and Superfrog with iconic level environments from its playlist.
System depicts retro computing.
Each genre XCF uses the `Genre collage` layer; the original background is removed.
The PNGs in `dist/` include the visible titles, frames, and artwork.
Titles use light lettering with a shadow for contrast over the artwork.
All 18 genre sources include an editable `Genre dimming` layer at 55% opacity
above the collage and below the titles and frames. This reduces background glare
so menu text and game covers stand out. The original collage PNGs in
`backgrounds/` retain their full brightness; exported wallpapers include the dimming.
The manifest records the strength as `genre_dimming_opacity`.
All genre headings use warm-white DejaVu Sans Mono Bold with black shadows.
Titles are centered in the same 384 × 66 px header area at (30, 23); long names
shrink to fit. The `GENRE` caption uses a common area at (30, 87). All genre
cover frames use the neutral Platformer frame template with identical positions
and colors. The shared settings are recorded under `genre_style` in the manifest.

`- Games List` and `- Multiplayer Games` also use collages based on their own
playlists, with the same layered XCF and complete PNG export workflow. Their
artwork is stored in a `Playlist collage` layer; all original backgrounds are removed.
Both collections use an editable `Playlist dimming` layer at 55% opacity and the
same warm-white font, black shadow, header alignment and cover-frame template as
the genre wallpapers. Their single-line headings remain `ALL GAMES` and
`MULTIPLAYER GAMES`, without a genre caption. The manifest records
`playlist_dimming_opacity`, `heading_title` and `heading_subtitle`.

`- Netplay Games` uses a generated illustration based on three user-supplied
living-room photographs. Two players in separate homes, each with a television
and controller, occupy spaces separated by a softly glowing vertical cyan line
from the top to the bottom of the image. The enlarged right TV balances the left; the globe and central solid
divider are removed. The rooms retain the
wall-mounted TV, black lowboard and LED lighting of one setup and the standing
TV with walnut storage cabinets of the other. Both screens show illustrated
classic Game Boy Tennis gameplay in olive-green monochrome from opposite
player viewpoints, with swapped player sprites, scores and ball positions,
conveying competition over the internet. The source playlist
contains 48 entries; this illustration emphasizes remote play rather than a character
collage. Its layered XCF and PNG export use the same header, frames and editable
55% dimming as the other collections. Cabinet cubbies contain illustrated retro
game packaging generated from the complete 48-title playlist; small cover text
and an exact one-to-one correspondence are not independently verified. The full
shelf title list and generation/edit prompts are recorded in the manifest.

The 21 system wallpapers use generated close-ups inspired by their hardware:
plastic grain, wood veneer, ventilation slots, buttons and other shell details.
Arcade and electronic handheld playlists combine materials typical of their devices;
DOS and Windows use period computer case details. These are artistic interpretations
of hardware surfaces. Existing logos and frames remain separate
layers above `System surface`. Original backgrounds are removed. Bright materials
are dimmed with an editable `Evening shading` layer while retaining their original hue;
already dark surfaces keep their existing lighting. All `Released` labels use warm-white
lettering with a dark shadow. The manifest records each system's playlist, prompt and
shading strength.
Separate top-right device illustrations and their presentation cards are removed.

Game Gear and Sega CD include original platform logo artwork on separate layers
alongside the existing SEGA wordmark. Vector artwork and attribution are stored in
[assets/logos](assets/logos/README.md). Their release labels use the first Japanese
hardware releases: [Game Gear (1990)](https://www.sega.jp/history/hard/gamegear/)
and [Mega-CD (1991)](https://www.sega.jp/history/hard/mega-cd/index.html).

---

## Installation

### Requirements

- A working installation of **RetroArch**
- Access to your RetroArch configuration directory (location depends on your OS)

Typical paths:

| Operating System | Path |
|------------------|------|
| **Windows** | %APPDATA%\RetroArch\assets\wallpapers\ |
| **Linux** | ~/.config/retroarch/assets/wallpapers/ |
| **macOS** | ~/Library/Application Support/RetroArch/assets/wallpapers/ |

---

### Installing the Wallpapers

1. **Navigate** to your RetroArch wallpapers directory.
2. **Create** the folder `retroplayer` if it doesn’t already exist.
3. **Download** the contents of the `dist/` directory from this repository  
   (either by cloning the repo or downloading the ZIP from GitHub).
4. **Extract or copy** all files from `dist/` into the `retroplayer` folder.

---

### Verifying in RetroArch

1. Launch **RetroArch**.  
2. Go to **Settings - User Interface - Menu - Background Image**.  
3. Choose one of the installed wallpapers from the **retroplayer** folder.

---

## Credits

- **Design & Creation:** [Brian 'morlenxus' Miculcy](https://brian.miculcy.com)
- **Inspired by:** Shakalakka Dynamic Wallpapers
- **License:** [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)

---

*Enjoy your new RetroPlayer dynamic wallpapers!*
