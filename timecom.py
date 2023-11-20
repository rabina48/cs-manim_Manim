from manim import *

class PseudoCode(Scene):
    def construct(self):
        # Step 1: Display the heading "Time Complexity Analysis" in yellow at the top-left corner
        heading = Text("Time Complexity Analysis", color=YELLOW).to_edge(UL)
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
        text_display = Text(code_text, font="Monospace", t2c={"BFS": BLUE}, line_spacing=0.8).scale(0.4)
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

        # # Step 4: Display a text "Overall Time Complexity"
        # overall_text = Text("Overall Time Complexity: O(V + E)", color=YELLOW).scale(0.8).next_to(heading, DOWN, buff=1).move_to(ORIGIN)
        # self.play(FadeIn(*overall_text))
        # self.wait(2)
        # ... previous code ...

        # Step 4: Display a text "Overall Time Complexity" in the right corner with a red rectangular box
        overall_text = Text("Overall Time Complexity: O(V + E)", color=YELLOW).scale(0.8)
        overall_text.to_edge(DR, buff=0.5)  # Positioning the text in the bottom right corner

        # Creating a red rectangle background for the text
        background_rect = BackgroundRectangle(overall_text, color=RED, fill_opacity=1)

        # Manually adjusting the size of the rectangle
        background_rect.width = overall_text.width + 0.1
        background_rect.height = overall_text.height + 0.1

        # Aligning the rectangle with the text
        background_rect.move_to(overall_text)

        # Grouping the text and rectangle together
        overall_text_group = VGroup(background_rect, overall_text)

        # Animate the appearance of the text with the rectangle
        self.play(FadeIn(overall_text_group))
        self.wait(2)

# ... rest of your code ...
