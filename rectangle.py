from manim import *

class BFSVisualization(Scene):
    def construct(self):
        # BFS Title Setup
        title_bfs = Text("Breath First Search", font="Calibri", font_size=72, color=GREEN_B, weight=BOLD)

        # Center 'BFS' in the middle of the screen
        title_bfs.move_to(ORIGIN)

        # Animate the 'BFS' title
        self.play(Write(title_bfs))
        self.wait(2)

        # Move the title up
        title_bfs.generate_target()
        title_bfs.target.to_edge(UP)
        self.play(MoveToTarget(title_bfs))

        # Bullet Point 1
        bullet_point_1 = Text(" BFS is an algorithm for traversal to explore "
                              "nodes and edges of a graph.",
                              t2c={"BFS": YELLOW}).scale(0.7)
        bullet_point_1.next_to(title_bfs.target, DOWN, buff=1)
        self.play(Write(bullet_point_1))
        self.wait(2)  # Wait for the audience to read

        # Bullet Point 2
        bullet_point_2 = Text(" It runs with a time complexity of O(V+E).", t2c={"O(V+E)": RED}).scale(0.7)
        bullet_point_2.next_to(bullet_point_1, DOWN, buff=0.5)
        self.play(Write(bullet_point_2))
        self.wait(2)  # Wait for the audience to read

        # Bullet Point 3
        bullet_point_3 = Text(" It is particularly useful for finding the\n" 
                              "shortest path on an unweighted graph.", 
                              t2c={"shortest path on an unweighted graph": BLUE_B}).scale(0.7)
        bullet_point_3.next_to(bullet_point_2, DOWN, buff=0.5)
        self.play(Write(bullet_point_3))
        self.wait(2)  # Wait for the audience to read

        # Fade out all elements
        self.play(FadeOut(title_bfs, bullet_point_1, bullet_point_2, bullet_point_3))

        # Continue with the rest of your BFS visualization
