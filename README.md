# RetroArch Dynamic Wallpapers – RetroPlayer

This repository contains dynamic **RetroArch wallpapers** designed for the **RetroPlayer** theme.  
The `.xcf` files inside the `src/` directory are the original GIMP source files.  
The `.png` files inside the `dist/` directory are the exported versions used by RetroArch.

Only the exported `.png` files are required for use in RetroArch.

The 18 `Z Genre` wallpapers use generated collages based on selected titles from
the supplied genre playlists. The standalone backgrounds are in `backgrounds/`;
`backgrounds/generation-manifest.json` records the prompts and playlist motifs.
Platformer combines iconic level environments, and System depicts retro computing.
Each genre XCF uses the `Genre collage` layer; the original background is removed.
The PNGs in `dist/` include the visible titles, frames, and artwork.
Titles use light lettering with a shadow for contrast over the artwork.

`- Games List` and `- Multiplayer Games` also use collages based on their own
playlists, with the same layered XCF and complete PNG export workflow. Their
artwork is stored in a `Playlist collage` layer; all original backgrounds are removed.

The 19 system wallpapers use generated close-ups inspired by their hardware:
plastic grain, wood veneer, ventilation slots, buttons and other shell details.
Arcade and electronic handheld playlists combine materials typical of their devices;
DOS and Windows use period computer case details. These are artistic interpretations
of hardware surfaces. Existing logos, device illustrations and frames remain separate
layers above `System surface`. Original backgrounds are removed, and text contrast is
adapted to light or dark materials. The manifest records each system's playlist and prompt.
The top-right device cutouts are centered on translucent smoked-glass cards with
rounded edges, a soft shadow and a subtle light in a platform-specific accent color.
These elements remain editable in the `Device presentation` group, below `Device`.

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
