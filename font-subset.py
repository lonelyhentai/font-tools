import fontforge
from sys import argv
from typing import Iterable
from os import path
import json

DEFAULT_CONFIG_PATH = './font-subset.json'

def open_font(font_path) -> fontforge.font:
  return fontforge.open(font_path)

def subset_of_font(source_font: fontforge.font, subset: Iterable[str]) -> fontforge.font:
  # selecting the subset from source font
  for c in subset:
    fc = 'u%04x' % ord(c)
    source_font.selection.select(("more", None), fc)
  source_font.selection.invert()
  for i in source_font.selection.byGlyphs:
    source_font.removeGlyph(i)
  return source_font

def save_font(source_font: fontforge.font, save_path: str):
  source_font.save(save_path)
  
def generate_font(source_font: fontforge.font, generate_path: str):
  source_font.generate(generate_path)

def main():
  if len(argv) < 2:
    config_path = DEFAULT_CONFIG_PATH
  else:
    command_line_config_path = argv[1]
    if not path.exists(command_line_config_path):
      config_path = DEFAULT_CONFIG_PATH
    else:
      config_path = command_line_config_path
  with open(config_path, 'r', encoding='utf-8') as config_file:
    config_content = config_file.read()
  print(f"loading config from {path.abspath(config_path)}...")
  config = json.loads(config_content)
  print(f"config loaded!")
  for c in config:
    source_font_path = c['source_font_path']
    project_save_path = c['project_save_path']
    target_font_path = c['target_font_path']
    subset = c['subset']
    print(f'loading source font from "{path.abspath(source_font_path)}"...')
    source_font = open_font(source_font_path)
    print(f'selecting subset...')
    target_font = subset_of_font(source_font, subset)
    print(f'saving project file to "{path.abspath(project_save_path)}"...')
    save_font(target_font, project_save_path)
    print(f'generating target font file to "{path.abspath(target_font_path)}"...')
    generate_font(target_font, target_font_path)
  print("succeed!")

if __name__ == '__main__':
  main()