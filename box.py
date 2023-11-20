from manim import *

class YourScene(Scene):
    def construct(self):
        # Initialize an empty group for the boxes
         # Dimensions and spacing for the boxes
        box_width = 3
        box_height = 0.5
        box_spacing = 0.5

        # # Create the first empty rectangular box
        # box1 = Rectangle(width=box_width, height=box_height, fill_opacity=0, color=WHITE)
        # box1.next_to(UP)

        # box1.to_edge(DR)

        # # Create the second rectangular box
        # box2 = Rectangle(width=box_width, height=box_height, fill_opacity=0, color=WHITE)
        # box2.next_to(box1, DR, buff=box_spacing)
         # Create the first rectangular box
        box1 = Rectangle(width=box_width, height=box_height, fill_opacity=0, color=WHITE)
        box1.to_edge(DR, buff = 0.4)  # Position the box at the middle right of the scene

        # Create the second rectangular box
        box2 = Rectangle(width=box_width, height=box_height, fill_opacity=0, color=WHITE)
        box2.next_to(box1, UP*2, buff=0.4)  # Position the box 1.5 units below the first box



        title_queue = Text("Traversal", font="Calibri", font_size=28, color=BLUE_C, weight=BOLD)
        title_queue.shift(1*LEFT+3.4*DOWN) # 'DL' means down left
        self.add(title_queue)
        self.play(Write(title_queue))
        
        
        # Add the boxes to the scene
        self.add(box1, box2)

        # Add the numbers '1', '2', and '3' to the left side of box2
        text1 = Text("1", font_size=24, color=YELLOW)
        text2 = Text("2", font_size=24, color=YELLOW)
        text3 = Text("3", font_size=24, color=YELLOW)
        text4 = Text("4", font_size=24, color=YELLOW)
        text5 = Text("5", font_size=24, color=YELLOW)
        text6 = Text("6", font_size=24, color=YELLOW)
        text7 = Text("7", font_size=24, color=YELLOW)

        text1.move_to(box2.get_left() + 0.3 * RIGHT)  # Adjust the buffer as needed
        
        text2.next_to(text1, RIGHT, buff=0.1)
        text3.next_to(text2, RIGHT, buff=0.1)

        self.add(text1)
        self.wait(2)
        self.add( text2)
        self.wait(2)
        self.add( text3)
        self.wait(2)

        # Move '1' from box2 to box1
        text1.move_to(box1.get_left() + 0.3 * RIGHT)  # Adjust the buffer as needed

        # Shift the places of '2' and '3' slightly to the left of box1
        text2.move_to(box2.get_left() + 0.3 * RIGHT)
        text3.next_to(text2, RIGHT, buff=0.1)
        self.wait(2)

        text2.next_to(text1, RIGHT, buff=0.1)
        #self.wait(2)
        text3.move_to(box2.get_left() + 0.3 * RIGHT)
        self.wait(2)
        text4.next_to(text3)
        text5.next_to(text4)
        self.add(text4)
        self.add(text5)
        self.wait(2)
        text3.next_to(text2)
        text4.move_to(box2.get_left() + 0.3 * RIGHT)
        text5.next_to(text4)
        text4.next_to(text3)
        self.wait(2)
        text5.move_to(box2.get_left() + 0.3 * RIGHT)
        self.add(text6)
        self.add(text7)
        text6.next_to(text5)
        text7.next_to(text6)
        self.wait(2)
        text5.next_to(text4)
        self.wait(2)
        text6.move_to(box2.get_left() + 0.3 * RIGHT)
        text7.next_to(text6)
        self.wait(2)
        text6.next_to(text5)
        self.wait(2)
        text7.move_to(box2.get_left() + 0.3 * RIGHT)
        self.wait(2)
        text7.next_to(text6)
        

        # Wait for a few seconds at the end of the animation
        self.wait(3)
        self.play(box1.animate.to_corner(DR), box2.animate.to_corner(DR))
        # boxes = VGroup()
        # box_side_length = 0.5  # Adjust the size of the boxes
        # box_spacing = 0.1      # Adjust the spacing between boxes

        # # Number of boxes
        # num_boxes = 7

        # # Create the boxes in a loop
        # for _ in range(num_boxes):
        #     # Create a box filled with yellow color
        #     box = Square(side_length=box_side_length, color=WHITE, fill_color=YELLOW, fill_opacity=1)

        #     # Position the first box or position subsequent boxes
        #     if boxes.submobjects:
        #         box.next_to(boxes, RIGHT, buff=box_spacing)
        #     else:
        #         box.to_edge(DOWN, buff=0.1)  # Position the first box

        #     boxes.add(box)  # Add the new box to the group
        #     self.add(box)

        
