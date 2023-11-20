from manim import *

class YourScene(Scene):
    def construct(self):
        # Your existing code
        # ...


       
        text_line_1 = Text("- Rabina Shrestha", font_size=24, color=RED)
        text_line_1.to_corner(DR, buff=0.5)  # Position at bottom right corner

        # Create the second line of text in red color
        text_line_2 = Text("- Isha Narang", font_size=24, color=RED)
        text_line_2.next_to(text_line_1, UP, buff=0.5)  # Position above the first line

        # Add the text to the scene
        self.add(text_line_1, text_line_2)

        # ... rest of your scene ...
