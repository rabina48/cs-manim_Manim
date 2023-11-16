# import os
# from manim import *

# class OutlineParagraph(Scene):
#     def construct(self):
#         # Define the paragraph text, each line as an item in a list
#         paragraph_lines = [
#             "This is the first line of the paragraph.",
#             "This is the second line, which will be outlined after the first.",
#             "And this is the third line, following the second."
#         ]

#         # Initialize an empty list to hold text objects
#         text_objects = []

#         # Initialize an empty list to hold rectangle objects
#         box_objects = []

#         # Create Text objects for each line and corresponding Rectangles
#         for line in paragraph_lines:
#             text = Text(line, font_size=20, color=WHITE).scale(0.7)
#             box = Rectangle(width=text.get_width() + 0.2, height=text.get_height() + 0.2, stroke_color=RED, stroke_width=2, fill_color=BLACK, fill_opacity=1)
#             text_objects.append(text)
#             box_objects.append(box)

#         # Position the first line of text and its box
#         text_objects[0].to_edge(UP, buff=1)
#         box_objects[0].surround(text_objects[0])

#         # Add the first line of text and its box to the scene
#         self.play(Create(box_objects[0]), Write(text_objects[0]))
#         self.wait(1)

#         # Position and animate the rest of the lines
#         for i in range(1, len(text_objects)):
#             text_objects[i].next_to(text_objects[i-1], DOWN, buff=0.5)
#             box_objects[i].surround(text_objects[i])
#             self.play(Create(box_objects[i]), Write(text_objects[i]))
#             self.wait(1)

#         # Keep everything on screen for a few seconds
#         self.wait(3)

# # To execute the script, save it in a file named `outline_paragraph.py`, and run:
# # manim -pql outline_paragraph.py OutlineParagraph

# from manim import *

# class OutlineParagraph(Scene):
#     def construct(self):
#         # Define the paragraph text, each line as an item in a list
#         paragraph_lines = [
#             "1. Initialize Q to be an empty queue",
#             "2. Mark all nodes in G as unvisited except s",
#             "3. Enqueue s into Q and mark s as visited",
#             "4. While Q is not empty:",
#             "    a. Dequeue the front node v from Q",
#             "    b. For each neighbor w of v:",
#             "        i. If w is not visited:",
#             "            - Enqueue w into Q",
#             "            - Mark w as visited"
#         ]

#         # Initialize an empty VGroup (this will make it easier to position lines relative to each other)
#         text_group = VGroup()

#         # Create Text objects for each line and add them to the VGroup
#         for line in paragraph_lines:
#             text = Text(line, font_size=20, color=WHITE).scale(0.7)
#             text_group.add(text)

#         # Align all text objects in a column with equal spacing
#         text_group.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.5)

#         # Animation
#         for text in text_group:
#             box = SurroundingRectangle(text, color=RED, fill_color=BLACK, fill_opacity=1)
#             self.play(Create(box), Write(text))
#             self.wait(0.5)  # Pause to read each line
#             # Fade out the rectangle before proceeding to the next line
#             self.play(FadeOut(box))

#         # Keep everything on screen for a few seconds
#         self.wait(3)

# # To execute the script, save it in a file named `outline_paragraph.py`, and run:
# # manim -pql outline_paragraph.py OutlineParagraph


from manim import *

class OutlineParagraph(Scene):
    def construct(self):
        # Define the paragraph text, each line as an item in a list
        paragraph_lines = [
            "1. Initialize Q to be an empty queue",
            "2. Mark all nodes in G as unvisited except s",
            "3. Enqueue s into Q and mark s as visited",
            "4. While Q is not empty:",
            "    a. Dequeue the front node v from Q",
            "    b. For each neighbor w of v:",
            "        i. If w is not visited:",
            "            - Enqueue w into Q",
            "            - Mark w as visited"
        ]

        # Create Text objects for each line and add them to the scene
        text_objects = [Text(line, font_size=20, color=WHITE).scale(0.7) for line in paragraph_lines]
        for i, text in enumerate(text_objects):
            text.move_to(UP * 3 - i * 0.5 * UP)  # Adjust the vertical position manually

        # Animation
        for text in text_objects:
            box = SurroundingRectangle(text, color=RED, fill_color=BLACK, fill_opacity=1)
            self.play(Create(box), Write(text))
            self.wait(0.5)  # Pause to read each line
            # Fade out the rectangle before proceeding to the next line
            self.play(FadeOut(box))

        # Keep everything on screen for a few seconds
        self.wait(3)

# To execute the script, save it in a file named `outline_paragraph.py`, and run:
# manim -pql outline_paragraph.py OutlineParagraph
