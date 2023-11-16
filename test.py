# from manim import *

# class BFSToQueue(Scene):
#     def construct(self):
#         self.bfs_and_queue_visualization()

#     def bfs_and_queue_visualization(self):
#         # BFS Visualization
#         title = Text("Breadth-First Search (BFS)", color=BLUE).scale(1.5)
#         self.play(Write(title))
#         self.wait(2)
#         self.play(FadeOut(title))

#         definition = Paragraph(
#             "Breadth-First Search (BFS) is an algorithm for traversing",
#             "or searching tree or graph data structures."
#         ).scale(0.7)
#         self.play(Write(definition))
#         self.wait(2)
#         self.play(FadeOut(definition))

#         label_to_key = {'4': 'A', '5': 'B', '3': 'C', '2': 'D', '1': 'E', '6': 'F'}
#         nodes = {
#             "A": self.create_labeled_circle('4', GREEN, 0.3).move_to(UP*3),
#             "B": self.create_labeled_circle('5', GREEN, 0.3).next_to(UP*2, LEFT*3),
#             "C": self.create_labeled_circle('3', GREEN, 0.3).next_to(UP*2, RIGHT*3),
#             "D": self.create_labeled_circle('2', GREEN, 0.3).next_to(UP*2 + LEFT*3, DOWN*5),
#             "E": self.create_labeled_circle('1', GREEN, 0.3).next_to(UP*2 + RIGHT*1, DOWN*6),
#             "F": self.create_labeled_circle('6', GREEN, 0.3).next_to(UP*2 + LEFT*6, DOWN*6),
#         }

#         edges = [
#             Line(nodes["A"][0].get_center(), nodes["B"][0].get_center()),
#             Line(nodes["A"][0].get_center(), nodes["C"][0].get_center()),
#             Line(nodes["B"][0].get_center(), nodes["D"][0].get_center()),
#             Line(nodes["B"][0].get_center(), nodes["E"][0].get_center()),
#             Line(nodes["D"][0].get_center(), nodes["F"][0].get_center())
#         ]

#         for edge in edges:
#             self.add(edge)
#         self.play(*[FadeIn(node) for node in nodes.values()])

#         # Queue Animation
#         box_side_length = 1
#         box_spacing = 0.2
#         boxes = VGroup()
#         values = VGroup()

#         bfs_order = ["4", "5", "3", "2", "1", "6"]
#         for i, label in enumerate(bfs_order):
#             box = Square(side_length=box_side_length, fill_color="#FFFF00", fill_opacity=0.9, color=WHITE)
#             box.next_to(boxes, RIGHT, buff=box_spacing).to_edge(DOWN, buff=0.1)
#             boxes.add(box)
#             self.add(box)
#             value_text = Text(label, font_size=24, color=WHITE)
#             value_text.move_to(box)
#             values.add(value_text)
#             self.add(value_text)

#         arrow = Arrow(UP, boxes[0].get_top(), buff=0.1, max_tip_length_to_length_ratio=0.1, color=WHITE)
#         self.play(GrowArrow(arrow))

#         # Traverse
#         bfs_edges = edges
#         for idx, label in enumerate(bfs_order):
#             key = label_to_key[label]
#             self.play(nodes[key][0].animate.set_fill(RED, opacity=1), run_time=1)
#             if idx < len(bfs_edges):
#                 self.play(bfs_edges[idx].animate.set_color(RED), run_time=1)
#             self.play(boxes[idx].animate.set_fill(ORANGE, opacity=0.9))
#             self.play(arrow.animate.next_to(boxes[idx].get_top(), UP, buff=0.1), run_time=0.5)
#             self.play(nodes[key][0].animate.set_fill(GREEN, opacity=1), run_time=1)
#             self.wait(1)

#     def create_labeled_circle(self, label, color, radius):
#         circle = Circle(color=color, fill_color=color, fill_opacity=1, radius=radius)
#         text = Text(label).scale(0.5).move_to(circle.get_center())
#         return VGroup(circle, text)


# from manim import *

# class BFSToQueue(Scene):
#     def construct(self):
#         self.bfs_and_queue_visualization()

#     def bfs_and_queue_visualization(self):
#         # BFS Visualization
#         title = Text("Breadth-First Search (BFS)", color=BLUE).scale(1.5)
#         self.play(Write(title))
#         self.wait(2)
#         self.play(FadeOut(title))

#         definition = Paragraph(
#             "Breadth-First Search (BFS) is an algorithm for traversing",
#             "or searching tree or graph data structures."
#         ).scale(0.7)
#         self.play(Write(definition))
#         self.wait(2)
#         self.play(FadeOut(definition))

#         label_to_key = {'4': 'A', '5': 'B', '3': 'C', '2': 'D', '1': 'E', '6': 'F'}
#         nodes = {
#             "A": self.create_labeled_circle('4', GREEN, 0.3).move_to(UP*3),
#             "B": self.create_labeled_circle('5', GREEN, 0.3).next_to(UP*2, LEFT*3),
#             "C": self.create_labeled_circle('3', GREEN, 0.3).next_to(UP*2, RIGHT*3),
#             "D": self.create_labeled_circle('2', GREEN, 0.3).next_to(UP*2 + LEFT*3, DOWN*5),
#             "E": self.create_labeled_circle('1', GREEN, 0.3).next_to(UP*2 + RIGHT*1, DOWN*6),
#             "F": self.create_labeled_circle('6', GREEN, 0.3).next_to(UP*2 + LEFT*6, DOWN*6),
#         }

#         edges = [
#             Line(nodes["A"][0].get_center(), nodes["B"][0].get_center()),
#             Line(nodes["A"][0].get_center(), nodes["C"][0].get_center()),
#             Line(nodes["B"][0].get_center(), nodes["D"][0].get_center()),
#             Line(nodes["B"][0].get_center(), nodes["E"][0].get_center()),
#             Line(nodes["D"][0].get_center(), nodes["F"][0].get_center())
#         ]

#         for edge in edges:
#             self.add(edge)
#         self.play(*[FadeIn(node) for node in nodes.values()])

#         # Queue Animation
#         box_side_length = 1
#         box_spacing = 0.2
#         boxes = VGroup()
#         values = VGroup()

#         bfs_order = ["4", "5", "3", "2", "1", "6"]
#         for i, label in enumerate(bfs_order):
#             box = Square(side_length=box_side_length, fill_color="#FFFF00", fill_opacity=0.9, color=WHITE)
#             box.next_to(boxes, RIGHT, buff=box_spacing).to_edge(DOWN, buff=0.1)
#             boxes.add(box)
#             self.add(box)
#             value_text = Text(label, font_size=24, color=WHITE)
#             value_text.move_to(box)
#             values.add(value_text)
#             self.add(value_text)

#         arrow = Arrow(UP, boxes[0].get_top(), buff=0.1, max_tip_length_to_length_ratio=0.1, color=WHITE)
#         self.play(GrowArrow(arrow))

#         # Traverse
#         bfs_edges = edges
#         for idx, label in enumerate(bfs_order):
#             key = label_to_key[label]
#             self.play(nodes[key][0].animate.set_fill(RED, opacity=1), run_time=1)
#             if idx < len(bfs_edges):
#                 self.play(bfs_edges[idx].animate.set_color(RED), run_time=1)
#             self.play(boxes[idx].animate.set_fill(ORANGE, opacity=0.9))
#             self.play(arrow.animate.next_to(boxes[idx].get_top(), UP, buff=0.1), run_time=0.5)
#             self.play(boxes[idx].animate.set_fill(GRAY, opacity=0.9))  # Change color to gray after visit
#             self.play(nodes[key][0].animate.set_fill(GREEN, opacity=1), run_time=1)
#             self.wait(1)

#     def create_labeled_circle(self, label, color, radius):
#         circle = Circle(color=color, fill_color=color, fill_opacity=1, radius=radius)
#         text = Text(label).scale(0.5).move_to(circle.get_center())
#         return VGroup(circle, text)

from manim import *

class BFSToQueue(Scene):
    def construct(self):
        self.bfs_and_queue_visualization()

    def bfs_and_queue_visualization(self):
        # BFS Visualization
        title = Text("Breadth-First Search (BFS)", color=BLUE).scale(1.5)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        definition = Paragraph(
            "Breadth-First Search (BFS) is an algorithm for traversing",
            "or searching tree or graph data structures."
        ).scale(0.7)
        self.play(Write(definition))
        self.wait(2)
        self.play(FadeOut(definition))

        label_to_key = {'4': 'A', '5': 'B', '3': 'C', '2': 'D', '1': 'E', '6': 'F'}
        nodes = {
            "A": self.create_labeled_circle('4', GREEN, 0.3).move_to(UP*3),
            "B": self.create_labeled_circle('5', GREEN, 0.3).next_to(UP*2, LEFT*3),
            "C": self.create_labeled_circle('3', GREEN, 0.3).next_to(UP*2, RIGHT*3),
            "D": self.create_labeled_circle('2', GREEN, 0.3).next_to(UP*2 + LEFT*3, DOWN*5),
            "E": self.create_labeled_circle('1', GREEN, 0.3).next_to(UP*2 + RIGHT*1, DOWN*6),
            "F": self.create_labeled_circle('6', GREEN, 0.3).next_to(UP*2 + LEFT*6, DOWN*6),
        }

        edges = [
            Line(nodes["A"][0].get_center(), nodes["B"][0].get_center()),
            Line(nodes["A"][0].get_center(), nodes["C"][0].get_center()),
            Line(nodes["B"][0].get_center(), nodes["D"][0].get_center()),
            Line(nodes["B"][0].get_center(), nodes["E"][0].get_center()),
            Line(nodes["D"][0].get_center(), nodes["F"][0].get_center())
        ]

        for edge in edges:
            self.add(edge)
        self.play(*[FadeIn(node) for node in nodes.values()])

        # Queue Animation
        box_side_length = 1
        box_spacing = 0.2
        boxes = VGroup()
        values = VGroup()

        bfs_order = ["4", "5", "3", "2", "1", "6"]
        for i, label in enumerate(bfs_order):
            box = Square(side_length=box_side_length, fill_color="#FFFF00", fill_opacity=0.9, color=WHITE)
            box.next_to(boxes, RIGHT, buff=box_spacing).to_edge(DOWN, buff=0.1)
            boxes.add(box)
            self.add(box)
            value_text = Text(label, font_size=24, color=WHITE)
            value_text.move_to(box)
            values.add(value_text)
            self.add(value_text)

        arrow = Arrow(UP, boxes[0].get_top(), buff= 0, max_tip_length_to_length_ratio=5, color=WHITE)
        self.play(GrowArrow(arrow))

        # Traverse
        bfs_edges = edges
        for idx, label in enumerate(bfs_order):
            key = label_to_key[label]
            self.play(nodes[key][0].animate.set_fill(RED, opacity=1), run_time=1)
            if idx < len(bfs_edges):
                self.play(bfs_edges[idx].animate.set_color(RED), run_time=1)
            self.play(boxes[idx].animate.set_fill(ORANGE, opacity=0.9))
            self.play(arrow.animate.next_to(boxes[idx].get_top(), UP, buff=0.1), run_time=0.5)
            self.play(boxes[idx].animate.set_fill(GRAY, opacity=0.9))  # Change color to gray after visit
            self.play(nodes[key][0].animate.set_fill(GREEN, opacity=1), run_time=1)
            self.wait(1)

    def create_labeled_circle(self, label, color, radius):
        circle = Circle(color=color, fill_color=color, fill_opacity=1, radius=radius)
        text = Text(label).scale(0.5).move_to(circle.get_center())
        return VGroup(circle, text)


