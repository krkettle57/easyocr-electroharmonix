from generator import TextImageGenerator

text = "HELLO, WORLD!"
font_filepath = "fonts/electroharmonix.ttf"
output_dir = "data"

generator = TextImageGenerator(font_filepath)
generator.generate(text).save(f"{output_dir}/image.png")
