# Font-Tools

A colllection of simple font tools.

**Please download release to use, or you need to download dependecies binaries by your self while cloning the repo**

## 1. Font-Subset

The tool to extract a subset of a full font, to refering it in a web page.

### Pre Configuration

Open `font-subset.json` and edit for your font, and we recommend that copy your font to fonts folder. For example:

```json
{
  "source_font_path": "./fonts/Helvetica.ttf",
  "project_save_path": "./fonts/Helvetica-subset.sfd",
  "target_font_path": "./fonts/Helvetica-subset.woff",
  "subset": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
}
```

You can set several options in a json array.

### Usage

#### Win

For win, run in command line:

```
.\font-subset-win.bat
```

#### Mac

For mac

```
./font-subset-mac.sh
```