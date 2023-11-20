
from manim import *

class PseudoCode(Scene):
     def construct(self):
        # Create and style the heading
        heading = Text("Pseudo Code", color=BLUE).to_edge(UL)

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

        # Move arrow to the second line
        #self.play(arrow.animate.next_to(text_display[8], LEFT, buff=0.1))
        #self.wait(2)

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
        self.play(heading.animate.shift(DOWN), heading.animate.set_color(ORANGE))
        self.wait(2)

   