# from manim import *

# class BFSTitle(Scene):
#     def construct(self):
#         title = Text("Breadth-First Search (BFS) ", color=BLUE).scale(1.5)
#         self.play(Write(title))
#         self.wait(2)
#         self.next_slide()

from manim import *

class BFSTitle(Scene):
    def construct(self):
        title = Text("Breadth-First Search (BFS)", color=BLUE).scale(1.5)
        self.play(Write(title))
        self.wait(2)
        
        self.play(FadeOut(title))  # Animate the removal of the title
        
        definition = Paragraph(
    "Breadth-First Search (BFS) is an algorithm for traversing",
    "or searching tree or graph data structures."
).scale(0.7)

        self.play(Write(definition))
        self.wait(2)
        
        self.play(FadeOut(definition)) 
        
    #    # A simple visualization of BFS
    #     # root = Dot(color=BLUE)
        
    #     root = Circle(color=BLUE, radius=0.3)
    #     root_label = Text("Root").next_to(root, UP)

    #     level_1 = [
    #         Circle(color=GREEN).next_to(root, LEFT*1 + DOWN*1),
    #         Circle(color=GREEN).next_to(root, RIGHT*1 + DOWN*1)
    #     ]
    #     level_1_labels = [
    #         Text("L1-A").next_to(level_1[0], DOWN),
    #         Text("L1-B").next_to(level_1[1], DOWN)
    #     ]

    #     level_2 = [
    #         Circle(color=ORANGE).next_to(level_1[0], LEFT + DOWN*1),
    #         Circle(color=ORANGE).next_to(level_1[0], RIGHT + DOWN*1),
    #         Circle(color=ORANGE).next_to(level_1[1], LEFT + DOWN*1),
    #         Circle(color=ORANGE).next_to(level_1[1], RIGHT + DOWN*1),
    #     ]

    #     tree_group = VGroup(root, root_label, *level_1, *level_1_labels, *level_2).center()
    #     self.play(FadeIn(tree_group))

    #     for l, label in zip(level_1, level_1_labels):
    #         self.play(GrowFromCenter(l), Write(label), Create(Line(root.get_center(), l.get_center())))
    #         self.wait(0.5)

    #     for l in level_2:
    #         parent = level_1[0] if l.get_center()[0] < root.get_center()[0] else level_1[1]
    #         self.play(GrowFromCenter(l), Create(Line(parent.get_center(), l.get_center())))
    #         self.wait(0.5)

    #     self.wait(2)
    
     # Create nodes with labels
        nodes = {
            "A": self.create_labeled_circle('A', WHITE, 0.3).move_to(UP*3),
            "B": self.create_labeled_circle('B', WHITE, 0.3).next_to(UP*2, LEFT*3),
            "C": self.create_labeled_circle('C', WHITE, 0.3).next_to(UP*2, RIGHT*3),
            "D": self.create_labeled_circle('D', WHITE, 0.3).next_to(UP*2 + LEFT*3, DOWN*5),
            "E": self.create_labeled_circle('E', WHITE, 0.3).next_to(UP*2 + RIGHT*1, DOWN*6),
            "F": self.create_labeled_circle('F', WHITE, 0.3).next_to(UP*2 + LEFT*6, DOWN*6),
        }

        # Edges
        edges = [
            Line(nodes["A"][0].get_center(), nodes["B"][0].get_center()),
            Line(nodes["A"][0].get_center(), nodes["C"][0].get_center()),
            Line(nodes["B"][0].get_center(), nodes["D"][0].get_center()),
            Line(nodes["B"][0].get_center(), nodes["E"][0].get_center()),
            Line(nodes["D"][0].get_center(), nodes["F"][0].get_center())
        ]

        # Add to the scene
        for edge in edges:
            self.add(edge)
        self.play(*[FadeIn(node) for node in nodes.values()])

        # BFS animation
        bfs_order = ["A", "B", "C", "D", "E", "F"]
        bfs_edges = edges
        for idx, label in enumerate(bfs_order):
            # self.play(
            #     nodes[label][0].animate.set_color(GREEN),
            #     rate_func=linear, run_time=1
            # )
            # if idx < len(bfs_edges):
            #     self.play(
            #           nodes[label][0].animate.set_fill(GREEN, opacity=1),
            #         rate_func=there_and_back, run_time=1
            #     )
            
            # Color the visited node
            self.play(nodes[label][0].animate.set_fill(GREEN, opacity=1), run_time=1)
            
            # If there's an edge to animate, color it but don't revert its color
            if idx < len(bfs_edges):
                self.play(bfs_edges[idx].animate.set_color(RED), run_time=1)

        self.wait(2)

      

    def create_labeled_circle(self, label, color, radius):
        circle = Circle(color=color, fill_color=color, fill_opacity=0, radius=radius)
        text = Text(label).scale(0.5).move_to(circle.get_center())
        return VGroup(circle, text)
    
    
    
    


