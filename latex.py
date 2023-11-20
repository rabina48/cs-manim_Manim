from manim import *

class MyScene(Scene):
    def construct(self):
        # LaTeX string for "for each v belongs to V"
        text = MathTex(r"\text{for each }", "v", r"\in V")

        # Add the LaTeX text to the scene
        self.play(Write(text))

        # Wait for a while before ending the scene
        self.wait(2)
