# from manim import *

# class TitleAnimation(Scene):
#     def construct(self):
#         # Create two separate Text objects
#         title_bfs = Text("BFS", font="Calibri", font_size=72, color=BLUE)
#         title_full = Text("(Breadth First Search)", font="Calibri", font_size=48, color=RED)

#         # Center 'BFS' and position '(Breadth First Search)' right below it
#         title_bfs.move_to(UP * 3)
#         title_full.next_to(title_bfs, DOWN, buff=0.5)

#         # Animate the titles
#         self.play(Write(title_bfs), Write(title_full))

#         # Hold the frame to view the title
#         self.wait(2)

from manim import *

class TitleAnimation(Scene):
    def construct(self):
        # # 'BFS' text in a different color
        # title_bfs = Text("BFS", font="Calibri", font_size=72, color=RED)

        # # '(Breadth First Search)' text in black color
        # title_full = Text("(Breadth First Search)", font="Calibri", font_size=48, color=BLACK)

        # # 'Prepared by' text at the bottom right
        # prepared_by = Text("Prepared by [Your Name]", font="Calibri", font_size=36, color=GRAY)
        # prepared_by.to_corner(DR, buff=0.5)  # Positioning at bottom right

        # # Center 'BFS' and position '(Breadth First Search)' right below it
        # title_bfs.move_to(UP * 3)
        # title_full.next_to(title_bfs, DOWN, buff=0.5)

        # # Animate the titles and 'Prepared by' text
        # self.play(Write(title_bfs), Write(title_full), Write(prepared_by))

        # # Hold the frame to view the title and 'Prepared by' text
        # self.wait(2)


# from manim import *
