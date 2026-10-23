# RetroArch Dynamic Wallpapers – RetroPlayer

Dynamic **RetroArch wallpapers** for the **XMB** menu in the **RetroPlayer** style:
calm, dark 1920 × 1080 images with a quiet menu area on the left and a motif on the
right. RetroArch switches the wallpaper automatically depending on the selected
playlist or menu tab.

The set includes:

- **21 systems** – close-ups of the original hardware with logo and release year,
  from Atari 2600 and Commodore 64 to Dreamcast, PlayStation and Wii.
  [Overview](screenshots/Systems%20Overview.jpg)
- **20 genres** – tactile still lifes for genre playlists (`Z Genre …`), e.g. Puzzle,
  Racing, Role-Playing Game, Ego-Shooter or Shoot 'em Up.
  [Overview](screenshots/Genres%20Overview.jpg)
- **Collections** – `- Games List`, `- Multiplayer Games`, `- Netplay Games` and
  `- Controller Settings`. [Overview](screenshots/Collections%20Overview.jpg)
- **Menu tabs** – `Main Menu`, `Settings`, `History` and `Netplay` (English menu titles).
- **24 playlist icons** (256 × 256, transparent) for All Games, Multiplayer,
  Netplay, Controller Settings
  and all genres in `icons/`. [Overview](screenshots/Playlist%20Icons%20Overview.png)

| Directory | Content |
|---|---|
| `dist/` | Ready-to-use wallpapers – the only files RetroArch needs |
| `icons/` | Matching playlist icons |
| `src/` | Layered GIMP source files (`.xcf`) |
| `backgrounds/` | Artwork without titles and frames |
| `scripts/` | Build and helper scripts, see [DEVELOPMENT.md](DEVELOPMENT.md) |

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

1. Copy all files from `dist/` into a folder of your choice, e.g. the
   `wallpapers` directory listed above.
2. In RetroArch, set **Settings → Directory → Dynamic Backgrounds** to that folder.
3. Enable **Settings → User Interface → Appearance → Dynamic Background**.
4. Optional: copy the `icons/` files into the playlist icon folder of your XMB theme.

The filenames must match your playlist names or menu titles exactly. Some
files in `dist/` are symlinks for alternative playlist names (e.g.
`Atari - 1977 - 2600.png`). If your system or ZIP download does not preserve
symlinks, copy and rename the target files instead. With a menu language other
than English, rename the menu tab wallpapers to the displayed titles.

---

## Credits

- **Design & Creation & Ideas:** [Brian 'morlenxus' Miculcy](https://brian.miculcy.com)
- **AI:** ChatGPT Images 2.5
- **Inspired by:** Shakalakka Dynamic Wallpapers
- **License:** [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)

---

*Enjoy your new RetroPlayer dynamic wallpapers!*
