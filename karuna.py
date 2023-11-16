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

        # arrow = Arrow(0.01*UP, boxes[0].get_bottom(), buff= 0, max_tip_length_to_length_ratio=0.3, color=WHITE)
            arrow = Arrow(color=WHITE)
            arrow.scale(0.5) 
            arrow.move_to(LEFT*10)
            


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
            self.play(nodes[key][0].animate.set_fill(GRAY, opacity=1), run_time=1)
            self.wait(1)
            
            self.wait(2)
       
        # Clear the screen by removing all elements
        
        # self.play(FadeOut(mobjects=self.mobjects))
        self.play(FadeOut(*self.mobjects))
        
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


    def create_labeled_circle(self, label, color, radius):
        circle = Circle(color=color, fill_color=color, fill_opacity=1, radius=radius)
        text = Text(label).scale(0.5).move_to(circle.get_center())
        return VGroup(circle, text)
    
        
    
    


