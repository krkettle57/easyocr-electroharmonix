import easyocr

from generator import TextImageGenerator

text = "HELLO, WORLD!"
font_filepath = "fonts/electroharmonix.ttf"
output_dir = "data"

output_image_filepath = f"{output_dir}/gen_{text}.png"

generator = TextImageGenerator(font_filepath)
generator.generate(text).save(output_image_filepath)


langs = [
    ["en"],
    ["ja"],
    ["en", "ja"],
]

for lang in langs:
    result = easyocr.Reader(lang, gpu=False).readtext(output_image_filepath)
    key = ",".join(lang)
    for detect in result:
        print(f"{key}: {detect[1]}")
