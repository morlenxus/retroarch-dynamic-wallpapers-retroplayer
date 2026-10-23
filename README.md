# RetroArch Dynamic Wallpapers – RetroPlayer

This repository contains dynamic **RetroArch wallpapers** designed for the **RetroPlayer** theme.  
The `.xcf` files inside the `src/` directory are the original GIMP source files.  
The `.png` files inside the `dist/` directory are the exported versions used by RetroArch.

Only the exported `.png` files are required for use in RetroArch.

The `icons/` directory contains 23 matching playlist icons for the horizontal
RetroArch menu: All Games, Multiplayer, Netplay, and all 20 genres. Each PNG is
256 × 256 pixels with a transparent background and a centered illustrated motif.
Filenames match the playlist stems exactly, including the `- ` and `Z Genre `
prefixes. The icons depict playlist subjects and genre symbols, such as jumping
Superfrog, an arcade maze, a fighting turtle, and a retro computer. Local multiplayer uses two
controllers; Netplay adds a connected globe.
`icons/generation-manifest.json` records the generation prompts and motifs.
See the [complete icon overview](screenshots/Playlist%20Icons%20Overview.png).

These icons are separate from the dynamic wallpapers in `dist/`.

The 20 `Z Genre` wallpapers use generated collages based on selected titles from
the supplied genre playlists. The standalone backgrounds are in `backgrounds/`;
`backgrounds/generation-manifest.json` records the prompts and playlist motifs.
Platformer combines Mario with Yoshi, Sonic, Donkey Kong, Kirby, Mega Man,
Crash Bandicoot and Superfrog with iconic level environments from its playlist.
System depicts retro computing.
Each genre XCF uses the `Genre collage` layer; the original background is removed.
The PNGs in `dist/` include the visible titles, frames, and artwork.
Titles use light lettering with a shadow for contrast over the artwork.
All genre sources include an editable `Genre dimming` layer at 55% opacity
above the collage and below the titles and frames. This reduces background glare
so menu text and game covers stand out. The original collage PNGs in
`backgrounds/` retain their full brightness; exported wallpapers include the dimming.
The manifest records the strength as `genre_dimming_opacity`.
All genre headings use warm-white DejaVu Sans Mono Bold with black shadows.
Titles are centered in the same 384 × 66 px header area at (30, 23); long names
shrink to fit. The `GENRE` caption uses a common area at (30, 87). All genre
cover frames use the neutral Platformer frame template with identical positions
and colors. The shared settings are recorded under `genre_style` in the manifest.

Three collections replace the generic `Shooter` collection and split its 76
playlist entries into disjoint groups. Earlier versions are tracked in Git.

| Playlist | Entries | Scope |
|---|---:|---|
| `Z Genre Ego-Shooter` | 25 | Doom, Quake, Half-Life and other first-person shooters; includes the 6DoF Descent games. |
| `Z Genre Action-Shooter` | 32 | Turrican-style run-and-gun, top-down and vehicle action, plus explicitly marked lightgun and target shooters. |
| `Z Genre Shoot 'em Up` | 19 | Scrolling, fixed-screen and rail arcade shooters, plus explicitly marked adjacent space combat games. |

Ready-to-copy `.lpl` files are in `playlists/`.
The [Shooter group overview](screenshots/Shooter%20Groups%20Overview.png)
shows the three wallpapers and their icons side by side.
Ports, duplicate titles on different systems and DOOM WAD variants remain separate
entries. Original game paths, core settings and database associations are preserved.
The source playlist on the remote machine is not changed.

These are practical menu groups rather than strict genre definitions: lightgun
and Moorhuhn target games are included under Action-Shooter, while Wing Commander
and Starglider 2 are labeled as space combat simulations within the Shoot 'em Up
collection. Each collection has its own generated background, layered XCF source,
1920 × 1080 wallpaper export and 256 × 256 transparent icon. The Ego-Shooter icon
shows a first-person weapon and crosshair.
Active filename stems match across `playlists/`, `backgrounds/`, `src/`, `dist/`
and `icons/`: `Z Genre Ego-Shooter`, `Z Genre Action-Shooter` and
`Z Genre Shoot 'em Up`. `Ego-Shooter` uses the German genre name requested for
this collection.

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

`- Controller Settings` follows the clean hardware style: a dark graphite
controller surface with cropped buttons and an analog stick on the right, leaving
the left side quiet for the menu. Its editable `CONTROLLER` / `SETTINGS` heading
and neutral cover frames sit above the `System surface` layer. The ready-to-use
1920 × 1080 export is `dist/- Controller Settings.png`; the layered source is
`src/- Controller Settings.xcf`. The generation prompt is recorded in the background
manifest. Rebuild it in GIMP with `update('Controller Settings')`.

`History` depicts recently played games as a clean still life of unlabelled
cartridges, floppy disks in several formats and silver CDs, loosely overlapping
on the right. The media fade into a dark, quiet menu area on the left. Muted
materials, soft lighting and restrained color keep the image consistent with
the device wallpapers. Its editable `History` heading and shared cover frames
remain separate from the `Playlist collage` and 12% `Playlist dimming` layers.
The 1920 × 1080 wallpaper is `dist/History.png`, the layered source is
`src/History.xcf`, and the original artwork is `backgrounds/History.png`.
The background manifest records the built-in image generation prompt;
rebuild the source and export with `update('History')`.

`Netplay` is a clean wallpaper for the XMB Netplay menu tab: restrained teal-blue
network connections and nodes on the right fade into an empty charcoal menu area
on the left. The editable `Netplay` heading uses the shared typography. The
separate `Fading` overlay uses the Wii wallpaper's cool-blue vertical lines,
light cover frames and translucent horizontal band to match the network motif.
The manifest selects this overlay with an asset-specific `frame_template`.
This menu wallpaper is
`dist/Netplay.png`, with its source in `src/Netplay.xcf` and artwork in
`backgrounds/Netplay.png`. It is separate from the `- Netplay Games` playlist.
Rebuild with `update('Netplay')`; the background manifest records the prompt.
XMB supports this through its [dynamic wallpaper lookup by menu title](https://github.com/libretro/RetroArch/blob/master/menu/drivers/xmb.c),
and the [English Netplay tab title](https://github.com/libretro/RetroArch/blob/master/intl/msg_hash_us.h)
is `Netplay`. Enable dynamic wallpapers and use this project's `dist/` as the
wallpaper directory. With another menu language, the filename must match the
displayed tab title.

`Main Menu` is the wallpaper for the English XMB main menu, including its
`Quit RetroArch` entry. A recessed physical power button with restrained teal
lighting occupies the right side, leaving the left menu area calm and dark.
The editable `Main Menu` title and the cool-blue `Fading` group match Netplay;
lines, frames and overlays remain separate layers inside that group.
Use `dist/Main Menu.png` for RetroArch; `src/Main Menu.xcf` is the layered source
and `backgrounds/Main Menu.png` is the artwork. The prompt is recorded in the
background manifest. Rebuild with `update('Main Menu')`.

`Settings` adds a matching wallpaper for the English XMB Settings tab. Three
dark rotary adjustment dials with restrained teal accents and distinct pointer
directions occupy the right side;
the left side stays dark and quiet for the menu. The editable `Settings` title
and separate cool-blue `Fading` group match Main Menu and Netplay, preserving
individual line, frame and overlay layers. Use `dist/Settings.png` in RetroArch;
the layered source is `src/Settings.xcf` and the artwork is
`backgrounds/Settings.png`. The background manifest records the generation prompt.
Rebuild with `update('Settings')`.

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
