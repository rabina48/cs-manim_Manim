# from manim import *

# class RectangleAtRightBottom(Scene):
#     def construct(self):
#         # # Create the first rectangle
#         # rect1 = Rectangle(height=1, width=2, color=BLUE)

#         # # Position it at the middle bottom
#         # rect1.to_edge(DOWN, buff=0.1)

#         # # Create the second rectangle
#         # rect2 = Rectangle(height=1, width=2, color=RED)

#         # # Position it next to the first rectangle
#         # rect2.next_to(rect1, RIGHT, buff=0.2)
#         # rect2.align_to(rect1, DOWN)

#         # # Add the rectangles to the scene with a fade-in effect
#         # self.play(FadeIn(rect1))
#         # self.wait(1)
#         # self.play(FadeIn(rect2))
#         # self.wait(1)
        
#           # Create the first rectangle
#         rect1 = Rectangle(height=1, width=2, color=BLUE)

#         # Position it at the middle bottom
#         rect1.to_edge(DOWN, buff=0.1)

#         # Create the second rectangle
#         rect2 = Rectangle(height=1, width=2, color=RED)

#         # Position it next to the first rectangle
#         rect2.next_to(rect1, RIGHT, buff=0.2)
#         rect2.align_to(rect1, DOWN)

#         # Create text for the rectangles
#         text1 = Text("1").scale(0.5).move_to(rect1.get_center())
#         text2 = Text("2").scale(0.5).move_to(rect2.get_center())

#         # Create arrows pointing to the rectangles
#         arrow1 = Arrow(UP, rect1.get_top(), buff=1, color=YELLOW)
#         arrow2 = Arrow(UP, rect2.get_top(), buff=1, color=YELLOW)

#         # Add the rectangles, text, and arrows to the scene with effects
#         self.play(FadeIn(rect1))
#         self.play(Write(text1))
#         self.play(GrowArrow(arrow1))
#         self.wait(1)

#         self.play(FadeIn(rect2))
#         self.play(Write(text2))
#         self.play(GrowArrow(arrow2))
#         self.wait(1)


from manim import *

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.insert(0, item)

    def size(self):
        return len(self.items)

class QueueAnimation(Scene):
    def construct(self):
        queue = Queue()
        box_side_length = 1
        box_spacing = 0.2
        boxes = VGroup()
        values = VGroup()

        for i in range(5):
            box = Square(side_length=box_side_length, fill_color="#FFFF00", fill_opacity=0.9, color=WHITE)
            box.next_to(boxes, RIGHT, buff=box_spacing)
            boxes.add(box)
            self.play(Create(box))
            value_text = Text(str(i), font_size=24, color=WHITE)
            value_text.move_to(box)
            values.add(value_text)
            self.play(Write(value_text))
            queue.enqueue(i)

        # Initialize arrow pointing to the first box
        arrow = Arrow(UP, boxes[0].get_top(), buff=0.1, max_tip_length_to_length_ratio=0.5, color=WHITE)
        self.play(GrowArrow(arrow))

        # Visit each box, change the color to orange, and move the arrow to the next box
        for i in range(4):  # Loop only until the fourth box to prevent the "list index out of range" error
            visited_box = boxes[i]
            self.play(visited_box.animate.set_fill(ORANGE, opacity=0.9))
            self.wait(1)
            visited_box.set_fill(GRAY, opacity=0.9)  # Change to gray after the visit
            # Move the arrow to the next box
            self.play(arrow.animate.put_start_and_end_on(arrow.get_start() + RIGHT*(box_side_length + box_spacing), boxes[i+1].get_top()))

if __name__ == "__main__":
    os.system("manim -pql queue_animation.py QueueAnimation")




