from dataclasses import dataclass
from typing import Tuple, Union

from PIL import Image, ImageDraw, ImageFont

Color = Union[float, Tuple[float, ...], str]


@dataclass
class TextImageGenerator:
    font_filepath: str = "fonts/ipaexg.ttf"
    fontsize: int = 48
    px_ratio: float = 0.1
    py_ratio: float = 0.1

    def generate(
        self,
        text: str,
        color: Color = (0, 0, 0),
        bg_color: Color = (255, 255, 255),
    ) -> Image:
        font = self._get_font()
        canvas_size, text_tl = self._get_canvas_size(text, font)
        img = self._get_canvas(bg_color, canvas_size)
        draw = ImageDraw.Draw(img)
        draw.text(text_tl, text, fill=color, font=font)

        return img

    def _get_canvas_size(self, text: str, font: ImageFont.FreeTypeFont) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        text_width, text_height = ImageDraw.Draw(Image.new("RGB", (200, 200))).textsize(text, font)
        width = int(text_width * (1 + 2 * self.px_ratio))
        height = int(text_height * (1 + 2 * self.py_ratio))

        text_top_left_x = int(width * self.px_ratio / (1 + 2 * self.px_ratio))
        text_top_left_y = int(height * self.py_ratio / (1 + 2 * self.py_ratio))
        return (width, height), (text_top_left_x, text_top_left_y)

    def _get_canvas(self, bg_color: Color, canvas_size: Tuple[int, int]) -> Image:
        return Image.new("RGB", canvas_size, bg_color)

    def _get_font(self) -> ImageFont.FreeTypeFont:
        return ImageFont.truetype(self.font_filepath, self.fontsize)
