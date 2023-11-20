from manim import *
from manim.opengl import *
from manim_slides import Slide
from manim.opengl import *
from manim_slides import Slide



class BFSToQueue(Slide):
    def construct(self):
        self.bfs_and_queue_visualization()

    def bfs_and_queue_visualization(self):
       
        title_bfs = Text("Breath First Search", font="Calibri", font_size=72, color=BLUE_D, weight=BOLD)
        text_line_1 = Text("- Rabina Shrestha", font_size=24, color=RED)
        text_line_1.to_corner(DR, buff=0.5)  # Position at bottom right corner

        # Create the second line of text in red color
        text_line_2 = Text("- Isha Narang", font_size=24, color=RED)
        text_line_2.next_to(text_line_1, UP, buff=0.5)  # Position above the first line

        self.add(title_bfs,text_line_1, text_line_2)
        self.next_slide()
        self.play(FadeOut(title_bfs,text_line_1,text_line_2))
        # Add the text to the scene
        
        
        # Center 'BFS' in the middle of the screen
        title_bfs.move_to(ORIGIN)

        # Animate the 'BFS' title
        self.play(Write(title_bfs))
        self.wait(2)

        # Move the title up
        title_bfs.generate_target()
        title_bfs.target.to_edge(UP)
        self.play(MoveToTarget(title_bfs))
        
        # Manually adjust the text for each bullet point
        bullet_point_1_text = (
            "BFS is an algorithm for traversal to explore nodes and \n "
            "edges of a graph."
        )
        bullet_point_2_text = (
            "It runs with a time complexity of O(V+E)."
        )
        bullet_point_3_text = (
            "It is particularly useful for finding the shortest path on \n "
            "an unweighted graph."
        )
        self.next_slide()
        # Bullet Point 1
        bullet_point_1 = Text(
            bullet_point_1_text,
            t2c={"BFS": WHITE, "algorithm for traversal": RED, "edges": RED, "graph": RED}
        ).scale(0.7)
        bullet_point_1.next_to(title_bfs.target, DOWN, buff=1)
        self.play(Write(bullet_point_1))
        self.wait(2)

        # Bullet Point 2
        bullet_point_2 = Text(
            bullet_point_2_text,
            t2c={"O(V+E)": RED}
        ).scale(0.7)
        bullet_point_2.next_to(bullet_point_1, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(bullet_point_2))
        self.wait(2)
        self.next_slide()
        # Bullet Point 3
        bullet_point_3 = Text(
            bullet_point_3_text,
            t2c={"shortest path on an unweighted graph": RED}
        ).scale(0.7)
        bullet_point_3.next_to(bullet_point_2, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(bullet_point_3))
        self.wait(2)

        # Fade out all elements
        self.play(FadeOut(title_bfs, bullet_point_1, bullet_point_2, bullet_point_3))
        self.next_slide()
        
        
        # title_bfs_trave = Text("BFS Traversal", font="Calibri", font_size=36, color=YELLOW_A)
        # title_bfs_trave.next_to(title_bfs_trave, LEFT*0.5, buff=0.5)
        # title_bfs_trave.shift(UP * 3.5)  # Adjust the 0.5 value to change how far up it shifts
        
            # Create the title text
        title_bfs_trave = Text("BFS Traversal", font="Calibri", font_size=36, color=BLUE_C, weight=BOLD)

        # Position the title in the top left corner with a slight offset
        title_bfs_trave.to_edge(UL, buff=0.5)  # 'UL' means upper left, 'buff' is the buffer space from the edge

        # Add the title to the scene
        self.add(title_bfs_trave)
        self.play(Write(title_bfs_trave))
        self.wait(2)
        self.next_slide()
        label_to_key = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F','7': 'G'}
        nodes = {
            "A": self.create_labeled_circle('1', GREEN, 0.4).move_to(UP*3),
            "B": self.create_labeled_circle('2', GREEN, 0.4).next_to(UP*2, LEFT*3),
            "C": self.create_labeled_circle('3', GREEN, 0.4).next_to(UP*2, RIGHT*3),
            "D": self.create_labeled_circle('4', GREEN, 0.4).next_to(UP*2 + LEFT*3, DOWN*5),
            "E": self.create_labeled_circle('5', GREEN, 0.4).next_to(UP*2 + RIGHT*1, DOWN*6),
            "F": self.create_labeled_circle('6', GREEN, 0.4).next_to(UP*2 + LEFT*4, DOWN*11),
            "G": self.create_labeled_circle('7', GREEN, 0.4).next_to(UP*2 + LEFT*2, DOWN*11),
            # "H": self.create_labeled_circle('8', GREEN, 0.4).next_to(UP*2 + RIGHT*2, DOWN*11)
           
        }
        
       
        edges = [
            Line(nodes["A"][0].get_center(), nodes["B"][0].get_center()),
            Line(nodes["A"][0].get_center(), nodes["C"][0].get_center()),
            Line(nodes["B"][0].get_center(), nodes["D"][0].get_center()),
            Line(nodes["B"][0].get_center(), nodes["E"][0].get_center()),
            Line(nodes["D"][0].get_center(), nodes["F"][0].get_center()),
            Line(nodes["D"][0].get_center(), nodes["G"][0].get_center()),
            # Line(nodes["E"][0].get_center(), nodes["H"][0].get_center())
        ]
        # Step 3: Display O(1) to the right of the first line, shifted 10 characters to the right
    
    
        for edge in edges:
            self.add(edge)
        self.play(*[FadeIn(node) for node in nodes.values()])
        self.next_slide()
        # Queue Animation
        title_queue = Text("Traversal", font="Calibri", font_size=28, color=BLUE_C, weight=BOLD)
        title_queue.shift(1*LEFT+3.4*DOWN) # 'DL' means down left
        self.add(title_queue)
        self.play(Write(title_queue))
        box_side_length = 0.7
        box_spacing = 0.1
        boxes = VGroup()
        values = VGroup()
        bfs_levels = {}
        current_level = 0
        level_text = Text("Level 0", font="Calibri", font_size=28, color=RED)
        level_text.to_corner(UR)  # Position at the upper right corner
        self.play(Write(level_text))
        self.wait(2)
        self.next_slide()
        bfs_levels = {}
        current_level = 1
        level_text = Text("Level 1", font="Calibri", font_size=28, color=RED)
        level_text.to_edge(RIGHT, buff=0.5)  # Position at the upper right corner
        level_text.shift(UP * self.camera.frame_height * 0.25 - level_text.get_height() / 2)
  # Shift to middle vertically
        self.next_slide()
        self.play(Write(level_text))
        
        self.wait(2)
        
        bfs_levels = {}
        current_level = 2
        level_text = Text("Level 2", font="Calibri", font_size=28, color=RED)
        level_text.shift(RIGHT * self.camera.frame_height * 0.75 - level_text.get_height() / 2)  # Shift 50% up from bottom
  # Position at the upper right corner
        self.play(Write(level_text))

        self.next_slide()
        bfs_levels = {}
        current_level = 2
        level_text = Text("Level 3", font="Calibri", font_size=28, color=RED)
        level_text.shift(DR  * self.camera.frame_height * 0.95 - level_text.get_height() / 2)  # Shift 50% up from bottom
  # Position at the upper right corner
        self.play(Write(level_text))
        self.wait(2)
        
        
        

        bfs_order = ["1", "2", "3", "4", "5", "6","7"]
        for i, label in enumerate(bfs_order):
            box = Square(side_length=box_side_length, fill_color="#FFFF00", fill_opacity=0.9, color=WHITE)
            box.next_to(boxes, RIGHT, buff=box_spacing).to_edge(DOWN, buff=0.1)
            boxes.add(box)
            self.add(box)
            value_text = Text(label, font_size=24, color=WHITE)
            value_text.move_to(box)
            values.add(value_text)
            self.add(value_text)

        self.next_slide()
        
        # arrow = Arrow(0.01*UP, boxes[0].get_bottom(), buff= 0, max_tip_length_to_length_ratio=0.3, color=WHITE)
            # arrow = Arrow(color=WHITE)
            #arrow = Arrow(1.4, 1, color=WHITE)
            #arrow.scale(0.5) 
            # arrow=Arrow(start=[-1.5,1,0],end=[-0.7,0,0],buff=0.05)
        arrow = Arrow(start=[-1.5, 1, 0], end=[-0.7, 0, 0], buff=0.05, stroke_width=1)

        arrow.move_to(LEFT*10)
            #arrow.move_to(UP*10)
            
        self.play(GrowArrow(arrow))
        self.next_slide()
    

        # # Traverse
        # bfs_edges = edges
        # for idx, label in enumerate(bfs_order):
        #     key = label_to_key[label]
        #     self.play(nodes[key][0].animate.set_fill(RED, opacity=1), run_time=1)
        #     if idx < len(bfs_edges):
        #         self.play(bfs_edges[idx].animate.set_color(RED), run_time=0.2)
        #     self.play(boxes[idx].animate.set_fill(ORANGE, opacity=0.75))
        #     self.play(arrow.animate.next_to(boxes[idx].get_top(), UP + LEFT*0.45, buff=0.1), run_time=0.75)
        #     self.play(boxes[idx].animate.set_fill(GRAY, opacity=0.9))  # Change color to gray after visit
        #     self.play(nodes[key][0].animate.set_fill(GRAY, opacity=1), run_time=0.75)
        #     self.wait(3)
        # Traverse
        # Traverse
        bfs_edges = edges
        for idx, label in enumerate(bfs_order):
            key = label_to_key[label]

            # Highlight the edge first
            if idx < len(bfs_edges):
                self.play(bfs_edges[idx].animate.set_color(WHITE), run_time=0.2)
            

            # Now highlight the node
            self.play(nodes[key][0].animate.set_fill(RED, opacity=1), run_time=0.5)

            # Continue with the rest of the steps
            self.play(boxes[idx].animate.set_fill(ORANGE, opacity=0.75))
            self.play(arrow.animate.next_to(boxes[idx].get_top(), UP + LEFT*0.45, buff=0.1), run_time=0.75)
            self.play(boxes[idx].animate.set_fill(GRAY, opacity=0.9))  # Change color to gray after visit
            self.play(nodes[key][0].animate.set_fill(GRAY, opacity=1), run_time=0.75)
            self.wait(3)
            self.next_slide()

        self.play(FadeOut(*self.mobjects))
        
        

        heading = Text("Pseudo Code", font="Calibri", weight=BOLD, color=BLUE).to_edge(UL)
        self.next_slide()
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
         
    
        # Create and style the text
        code_text = """
       <span fgcolor='yellow'> BFS (G, s)  </span>                 
            //Where G is the graph and s is the source node
            <span fgcolor='yellow'>let Q be queue.</span> 
           //Inserting s in queue until all its neighbour vertices are marked.
            <span fgcolor='yellow'>Q.enqueue( s ) </span> 

            <span fgcolor='yellow'>mark s as visited.</span> 
            <span fgcolor='yellow'>while ( Q is not empty)</span> 
               //Removing that vertex from queue, whose neighbour will be visited now
                <span fgcolor='yellow'>v  =  Q.dequeue( )</span> 

                //processing all the neighbours of v
                <span fgcolor='yellow'>for all neighbours w of v in Graph G</span> 
                   <span fgcolor='yellow'> if w is not visited</span> 
                        //Stores w in Q to further visit its neighbour
                       <span fgcolor='yellow'> Q.enqueue( w ) </span>             
                        <span fgcolor='yellow'>mark w as visited.</span> 
        """

        text_display = MarkupText(code_text, font="Monospace", line_spacing=0.5).scale(0.4)
        text_display.next_to(heading, DOWN, buff=0.5).align_to(heading, LEFT)

        # [Rest of your script for arrow animation and other elements]


        # Create a smaller arrowhead and position it in front of the first line
        arrow = Arrow(0.5*LEFT, 0.5*RIGHT, color=RED, tip_length=0.1, stroke_width=3, max_tip_length_to_length_ratio=0.75)
        heading = Text("Pseudo Code", color=BLUE).to_edge(UL)
    
#DOne
    
        # Create and style the text
        code_text = """
        BFS (G, s)
            //Where G is the graph and s is the source node
            let Q be queue.
            //Inserting s in queue until all its neighbour vertices are marked.
            Q.enqueue( s )

            mark s as visited.
            while ( Q is not empty)
                //Removing that vertex from queue, whose neighbour will be visited now
                v  =  Q.dequeue( )

                //processing all the neighbours of v
                for all neighbours w of v in Graph G
                    if w is not visited
                        //Stores w in Q to further visit its neighbour
                        Q.enqueue( w )
                        mark w as visited.
        """

        text_display = Text(code_text, font="Monospace", t2c={"//": RED, 
                                                              "BFS": BLUE, 
                                                              "G":RED,
                                                              "Q":RED,
                                                              "enqueue": BLUE,
                                                              "dequeue": BLUE,
                                                              "mark": YELLOW,
                                                              "visited":GREEN_A
                                            
                                                              
                                                              }, line_spacing=0.5).scale(0.4)
        text_display.next_to(heading, DOWN, buff=0.5).align_to(heading, LEFT)

        # Create a smaller arrowhead and position it in front of the first line
        # arrow = Arrow(LEFT, RIGHT, color=WHITE, tip_length=0.1, stroke_width=0.5, max_tip_length_to_length_ratio=0.25)
        # arrow.next_to(text_display[1], LEFT, buff=0.2)
        arrow = Arrow(0.5*LEFT, 0.5*RIGHT, color=GREEN, tip_length=0.1, stroke_width=3, max_tip_length_to_length_ratio=0.75)
        arrow.next_to(text_display[1], LEFT, buff=0.2)

        # Display the heading, text, and arrow
        self.play(Create(heading), Create(text_display), Create(arrow))
        self.wait(3)

        # Move arrow to the third line
        self.play(arrow.animate.next_to(text_display[45], LEFT, buff=0.1))
        self.wait(2)

        # Move arrow to the fourth line
        #self.play(arrow.animate.next_to(text_display[57], LEFT, buff=0.1))
        #self.wait(2)

        # Move arrow to the fifth line
        self.play(arrow.animate.next_to(text_display[114], LEFT,   buff=0.1))
        self.wait(2)

        # Move arrow to the sixth line
        self.play(arrow.animate.next_to(text_display[126], LEFT,  buff=0.1))
        self.wait(2)

        # Move arrow to the seventh line
        self.play(arrow.animate.next_to(text_display[141], LEFT,  buff=0.1))
        self.wait(2)

        # Move arrow to the eight line
        self.play(arrow.animate.next_to(text_display[219], LEFT,  buff=0.1))
        self.wait(2)

        # Move arrow to the ninth line
        self.play(arrow.animate.next_to(text_display[263], LEFT,  buff=0.1))
        self.wait(2)

        # Move arrow to the tenth line
        self.play(arrow.animate.next_to(text_display[291], LEFT,  buff=0.1))
        self.wait(2)

        # Move arrow to the eleventh line
        self.play(arrow.animate.next_to(text_display[344], LEFT,  buff=0.1))
        self.wait(2)

        # Move arrow to the twelveth line
        self.play(arrow.animate.next_to(text_display[356], LEFT,  buff=0.1))
        self.wait(2)

        # Fade out the arrow
        self.play(FadeOut(arrow))

        # Example animation: Move the heading and change its color after 3 seconds
        self.wait(2)
        #  # Create the first rectangular box
        # box1 = Rectangle(width=box_width, height=box_height, fill_opacity=0, color=WHITE)
        # box1.to_edge(RIGHT)  # Position the box at the middle right of the scene

        # # Create the second rectangular box
        # box2 = Rectangle(width=box_width, height=box_height, fill_opacity=0, color=WHITE)
        # box2.next_to(box1, DOWN, buff=1.5)  # Position the box 1.5 units below the first box


        # # Add the boxes to the scene
        # self.add(box1, box2)

        # # Add the numbers '1', '2', and '3' to the left side of box2
        # text1 = Text("1", font_size=24, color=YELLOW)
        # text2 = Text("2", font_size=24, color=YELLOW)
        # text3 = Text("3", font_size=24, color=YELLOW)
        # text4 = Text("4", font_size=24, color=YELLOW)
        # text5 = Text("5", font_size=24, color=YELLOW)
        # text6 = Text("6", font_size=24, color=YELLOW)
        # text7 = Text("7", font_size=24, color=YELLOW)

        # text1.move_to(box2.get_left() + 0.3 * RIGHT)  # Adjust the buffer as needed
        
        # text2.next_to(text1, RIGHT, buff=0.1)
        # text3.next_to(text2, RIGHT, buff=0.1)

        # self.add(text1)
        # self.wait(2)
        # self.add( text2)
        # self.wait(2)
        # self.add( text3)
        # self.wait(2)

        # # Move '1' from box2 to box1
        # text1.move_to(box1.get_left() + 0.3 * RIGHT)  # Adjust the buffer as needed

        # # Shift the places of '2' and '3' slightly to the left of box1
        # text2.move_to(box2.get_left() + 0.3 * RIGHT)
        # text3.next_to(text2, RIGHT, buff=0.1)
        # self.wait(2)

        # text2.next_to(text1, RIGHT, buff=0.1)
        # #self.wait(2)
        # text3.move_to(box2.get_left() + 0.3 * RIGHT)
        # self.wait(2)
        # text4.next_to(text3)
        # text5.next_to(text4)
        # self.add(text4)
        # self.add(text5)
        # self.wait(2)
        # text3.next_to(text2)
        # text4.move_to(box2.get_left() + 0.3 * RIGHT)
        # text5.next_to(text4)
        # text4.next_to(text3)
        # self.wait(2)
        # text5.move_to(box2.get_left() + 0.3 * RIGHT)
        # self.add(text6)
        # self.add(text7)
        # text6.next_to(text5)
        # text7.next_to(text6)
        # self.wait(2)
        # text5.next_to(text4)
        # self.wait(2)
        # text6.move_to(box2.get_left() + 0.3 * RIGHT)
        # text7.next_to(text6)
        # self.wait(2)
        # text6.next_to(text5)
        # self.wait(2)
        # text7.move_to(box2.get_left() + 0.3 * RIGHT)
        # self.wait(2)
        # text7.next_to(text6)
        

        # # Wait for a few seconds at the end of the animation
        # self.wait(3)
        self.play(FadeOut(*self.mobjects))
        
        self.next_slide()
         # Step 1: Display the heading "Time Complexity Analysis" in yellow at the top-left corner
        
        heading = Text("Time Complexity Analysis", color=BLUE).to_edge(UL)
        self.play(Create(heading))
        self.wait(1)
        

        # Step 2: Display the entire pseudocode with increased line spacing and aligned to the left
        code_text = """
        BFS (G, s)
            let Q be queue.
            Q.enqueue( s )

            mark s as visited.
            while ( Q is not empty)
                v  =  Q.dequeue( )

                for all neighbours w of v in Graph G
                    if w is not visited
                        Q.enqueue( w )
                        mark w as visited.
        """
        text_display = Text(code_text, font="Monospace", t2c={"BFS": BLUE,
                                                              "Q": RED,
                                                              "while":YELLOW,
                                                              "Graph":GREEN,
                                                              "enqueue":RED,
                                                              "dequeue":RED
                                                              }, line_spacing=0.8).scale(0.4)
        text_display.next_to(heading, DOWN, buff=0.5).align_to(heading, LEFT)
        self.play(Create(text_display))
        self.wait(1)

        # Step 3: Display O(1) to the right of the first line, shifted 10 characters to the right
        time_complexity_label = Text("O(1)", color=RED).scale(0.4)
        time_complexity_label.next_to(text_display[10], RIGHT, buff=0.2).shift(2 * RIGHT)
        self.play(FadeIn(time_complexity_label))
        self.wait(2)

        time_complexity_label = Text("O(1)", color=RED).scale(0.4)
        time_complexity_label.next_to(text_display[22], RIGHT, buff=0.2).shift(2 * RIGHT)
        self.play(FadeIn(time_complexity_label))
        self.wait(2)

        time_complexity_label = Text("O(1)", color=RED).scale(0.4)
        time_complexity_label.next_to(text_display[32], RIGHT, buff=0.2).shift(3 * RIGHT)
        self.play(FadeIn(time_complexity_label))
        self.wait(2)

        time_complexity_label = Text("O(V)", color=RED).scale(0.4)
        time_complexity_label.next_to(text_display[52], RIGHT, buff=0.2).shift(3 * RIGHT)
        self.play(FadeIn(time_complexity_label))
        self.wait(2)

        time_complexity_label = Text("O(1)", color=RED).scale(0.4)
        time_complexity_label.next_to(text_display[69], RIGHT, buff=0.2).shift(2 * RIGHT)
        self.play(FadeIn(time_complexity_label))
        self.wait(2)  

        time_complexity_label = Text("O(E)", color=RED).scale(0.4)
        time_complexity_label.next_to(text_display[99], RIGHT, buff=0.2).shift(2 * RIGHT)
        self.play(FadeIn(time_complexity_label))
        self.wait(2) 

        time_complexity_label = Text("O(1)", color=RED).scale(0.4)
        time_complexity_label.next_to(text_display[112], RIGHT, buff=0.2).shift(2 * RIGHT)
        self.play(FadeIn(time_complexity_label))
        self.wait(2)              

        time_complexity_label = Text("O(1)", color=RED).scale(0.4)
        time_complexity_label.next_to(text_display[129], RIGHT, buff=0.3).shift(2 * RIGHT)
        self.play(FadeIn(time_complexity_label))
        self.wait(2) 

        time_complexity_label = Text("O(1)", color=RED).scale(0.4)
        time_complexity_label.next_to(text_display[139], RIGHT, buff=0.3).shift(2 * RIGHT)
        self.play(FadeIn(time_complexity_label))
        self.wait(2)      

        self.play(FadeOut(*self.mobjects))

        self.wait(1)

        # Step 4: Display a text "Overall Time Complexity"
        overall_text = Text("Overall Time Complexity: O(V + E)", color=BLUE_C).scale(0.8).next_to(heading, DOWN, buff=1).move_to(ORIGIN)
        self.play(FadeIn(*overall_text))
        self.play(FadeOut(*self.mobjects))
        
        self.wait(2)
    
    def create_labeled_circle(self, label, color, radius):
        circle = Circle(color=color, fill_color=color, fill_opacity=1, radius=radius)
        text = Text(label).scale(0.5).move_to(circle.get_center())
        return VGroup(circle, text)
    
        self.play(FadeOut(*self.mobjects))
        
        
    
    
        
    
    


