# from manim import *
from manim_slides import Slide

# class BFSTitle(Slide):
    
#     def construct(self):
#         title = Text("Breadth-First Search (BFS)", color=BLUE).scale(1.5)
#         self.play(Write(title))
#         self.wait(2)
#         self.next_slide()
#         self.play(FadeOut(title))

#         definition = Paragraph(
#             "Breadth-First Search (BFS) is an algorithm for traversing",
#             "or searching tree or graph data structures."
#         ).scale(0.7)

#         # Create nodes with labels
#         nodes = {
#             "A": self.create_labeled_circle('4', GREY, 0.3).move_to(UP*3),
#             "B": self.create_labeled_circle('5', GREY, 0.3).next_to(UP*2, LEFT*3),
#             "C": self.create_labeled_circle('3', GREY, 0.3).next_to(UP*2, RIGHT*3),
#             "D": self.create_labeled_circle('2', GREY, 0.3).next_to(UP*2 + LEFT*3, DOWN*5),
#             "E": self.create_labeled_circle('1', GREY, 0.3).next_to(UP*2 + RIGHT*1, DOWN*6),
#             "F": self.create_labeled_circle('6', GREY, 0.3).next_to(UP*2 + LEFT*6, DOWN*6),
#         }

#         label_to_key = {
#             '4': 'A',
#             '5': 'B',
#             '3': 'C',
#             '2': 'D',
#             '1': 'E',
#             '6': 'F'
#         }

#         # Edges
#         edges = [
#             Line(nodes["A"][0].get_center(), nodes["B"][0].get_center()),
#             Line(nodes["A"][0].get_center(), nodes["C"][0].get_center()),
#             Line(nodes["B"][0].get_center(), nodes["D"][0].get_center()),
#             Line(nodes["B"][0].get_center(), nodes["E"][0].get_center()),
#             Line(nodes["D"][0].get_center(), nodes["F"][0].get_center())
#         ]

#         # Add to the scene
#         for edge in edges:
#             self.add(edge)
#         self.play(*[FadeIn(node) for node in nodes.values()])

#         # BFS animation
#         bfs_order = ["4", "5", "3", "2", "1", "6"]
#         bfs_edges = edges
#         for idx, label in enumerate(bfs_order):
#             # Convert label to key
#             key = label_to_key[label]

#             # Color the visited node RED while visiting
#             self.play(nodes[key][0].animate.set_fill(RED, opacity=1), run_time=1)

#             # If there's an edge to animate, color it but don't revert its color
#             if idx < len(bfs_edges):
#                 self.play(bfs_edges[idx].animate.set_color(RED), run_time=1)

#             # Color the visited node GREY after visiting
#             self.play(nodes[key][0].animate.set_fill(GREEN, opacity=1), run_time=1)

#             self.wait(2)
            
#         # Fade out the graph to prepare for next slide
#         self.play(FadeOut(VGroup(*nodes.values(), *edges)))

#         # Slide 3: Key Points about BFS
#         key_points_title = Text("Key Points about BFS", color=BLUE).scale(1.5).to_edge(UP).shift(DOWN*1.5)
#         self.play(Write(key_points_title))

#         point1 = Text("- BFS is optimal for shortest-path problems.", color=WHITE).scale(0.7).next_to(key_points_title, DOWN)
#         point2 = Text("- It uses a Queue data structure.", color=WHITE).scale(0.7).next_to(point1, DOWN)
#         point3 = Text("- Complexity: O(V + E) for an adjacency list.", color=WHITE).scale(0.7).next_to(point2, DOWN)

#         self.play(Write(point1), Write(point2), Write(point3))
#         self.wait(3)

#     def create_labeled_circle(self, label, color, radius):
#         circle = Circle(color=color, fill_color=color, fill_opacity=1, radius=radius)
#         text = Text(label).scale(0.5).move_to(circle.get_center())
#         return VGroup(circle, text)
    
# class Queue:
#     def __init__(self):
#         self.items = []

#     def is_empty(self):
#         return not self.items

#     def enqueue(self, item):
#         self.items.insert(0, item)

#     def size(self):
#         return len(self.items)

#     def construct(self):
#         queue = Queue()
#         box_side_length = 1
#         box_spacing = 0.2
#         boxes = VGroup()
#         values = VGroup()

#         for i in range(5):
#             box = Square(side_length=box_side_length, fill_color="#FFFF00", fill_opacity=0.9, color=WHITE)
#             box.next_to(boxes, RIGHT, buff=box_spacing)
#             boxes.add(box)
#             self.play(Create(box))
#             value_text = Text(str(i), font_size=24, color=WHITE)
#             value_text.move_to(box)
#             values.add(value_text)
#             self.play(Write(value_text))
#             queue.enqueue(i)

#         # Initialize arrow pointing to the first box
#         arrow = Arrow(UP, boxes[0].get_top(), buff=0.1, max_tip_length_to_length_ratio=0.5, color=WHITE)
#         self.play(GrowArrow(arrow))

#         # Visit each box, change the color to orange, and move the arrow to the next box
#         for i in range(4):  # Loop only until the fourth box to prevent the "list index out of range" error
#             visited_box = boxes[i]
#             self.play(visited_box.animate.set_fill(ORANGE, opacity=0.9))
#             self.wait(1)
#             visited_box.set_fill(GRAY, opacity=0.9)  # Change to gray after the visit
#             # Move the arrow to the next box
#             self.play(arrow.animate.put_start_and_end_on(arrow.get_start() + RIGHT*(box_side_length + box_spacing), boxes[i+1].get_top()))

# if __name__ == "__main__":
#     os.system("manim -pql queue_animation.py QueueAnimation")


from manim import *

class BFSToQueue(Scene):
    
    def construct(self):
        # BFS Visualization
        self.bfs_visualization()
        # Queue Animation
        self.queue_animation()

    def bfs_visualization(self):
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

        bfs_order = ["4", "5", "3", "2", "1", "6"]
        bfs_edges = edges
        for idx, label in enumerate(bfs_order):
            key = label_to_key[label]
            self.play(nodes[key][0].animate.set_fill(RED, opacity=1), run_time=1)
            if idx < len(bfs_edges):
                self.play(bfs_edges[idx].animate.set_color(RED), run_time=1)
            self.play(nodes[key][0].animate.set_fill(GREY, opacity=1), run_time=1)
            self.wait(2)

        # self.play(FadeOut(VGroup(*nodes.values(), *edges)))

    def queue_animation(self):
        box_side_length = 1
        box_spacing = 0.2
        boxes = VGroup()
        values = VGroup()

        for i in range(5):
            box = Square(side_length=box_side_length, fill_color="#FFFF00", fill_opacity=0.9, color=WHITE)
            box.next_to(boxes, RIGHT, buff=box_spacing)
            boxes.add(box)
            box.to_edge(DOWN, buff=0.1)
            self.play(Create(box))
            value_text = Text(str(i), font_size=24, color=WHITE)
            value_text.move_to(box)
            values.add(value_text)
            self.play(Write(value_text))

        arrow = Arrow(UP, boxes[0].get_top(), buff=0.1, max_tip_length_to_length_ratio=0.5, color=WHITE)
        self.play(GrowArrow(arrow))

        for i in range(4):  
            visited_box = boxes[i]
            self.play(visited_box.animate.set_fill(ORANGE, opacity=0.9))
            self.wait(1)
            visited_box.set_fill(GRAY, opacity=0.9)  
            # self.play(arrow.animate.put_start_and_end_on(arrow.get_start() + RIGHT*(box_side_length + box_spacing), boxes[i+1].get_top()))
            self.play(arrow.animate.put_start_and_end_on(arrow.get_start() + RIGHT*(box_side_length + box_spacing), boxes[i+1].get_top()).scale(0.8))


    def create_labeled_circle(self, label, color, radius):
        circle = Circle(color=color, fill_color=color, fill_opacity=1, radius=radius)
        text = Text(label).scale(0.5).move_to(circle.get_center())
        return VGroup(circle, text)
