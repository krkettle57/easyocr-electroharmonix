from pathlib import Path
from typing import List, Tuple

import easyocr

from generator import TextImageGenerator


def get_ocr_detects(langs: List[List[str]], filepath: str) -> List[Tuple[str, str]]:
    detects = []
    for lang in langs:
        result = easyocr.Reader(lang, gpu=False).readtext(filepath)
        key = ",".join(lang)
        for detect in result:
            detects.append((key, detect[1]))

    return detects


def get_font_name(font_filepath: str) -> str:
    return Path(font_filepath).stem


def main(text: str, font_filepath: str) -> Tuple[str, List[Tuple[str, str]]]:
    langs = [
        ["en"],
        ["ja"],
        ["en", "ja"],
    ]
    font_name = get_font_name(font_filepath)
    output_dir = "data"

    output_image_filepath = f"{output_dir}/gen_{font_name}_{text}.png"

    generator = TextImageGenerator(font_filepath)
    generator.generate(text).save(output_image_filepath)
    detects = get_ocr_detects(langs, output_image_filepath)

    return font_name, detects


if __name__ == "__main__":
    text = "HELLO, WORLD!"
    for font_filepath in Path("fonts").glob("*.ttf"):
        print(main(text, str(font_filepath)))
