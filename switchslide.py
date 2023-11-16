from manim import *

class BFSTitle(Scene):
    def construct(self):
        # First slide/page
        title = Text("Breadth-First Search (BFS)", color=BLUE).scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
        
        # Second slide/page
        secondary_title = Text("Another Important Topic", color=RED).scale(1.5)
        self.play(Write(secondary_title))
        self.wait(2)
        self.play(FadeOut(secondary_title))