from manim import *

class FirstScene(Scene):
    def construct(self):
        title = Text("This is the first slide").scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        title = Text("This is the second slide").scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
