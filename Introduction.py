
# MANIM Introduction

from manim import *

class SquareAnimation(Scene):
    def construct(self):
        square = Square(side_length = 5, stroke_color = RED, fill_color = BLUE, fill_opacity = 0.75)
        print(square)
        self.play(Create(square), run_time = 5)
        self.wait()