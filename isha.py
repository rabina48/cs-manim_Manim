from manim import *

class QueueScene(Scene):
    def construct(self):
        # Create a queue with elements 1, 2, 3, 4, 5, and 6
        elements = [1, 2, 3, 4, 5, 6]
        queue = self.create_queue(elements)
        
        # Animate the enqueue and dequeue operations
        for element in elements:
            self.enqueue_element(queue, element)
            self.wait(1)
            self.dequeue_element(queue)
            self.wait(1)

    def create_queue(self, elements):
        element_spacing = 0.2
        queue = VGroup()

        for element in elements:
            element_rect = Rectangle(height=0.6, width=1, fill_opacity=0.7)
            element_text = Text(str(element)).next_to(element_rect, UP)
            element_group = VGroup(element_rect, element_text)
            if queue:
                element_group.next_to(queue[-1], RIGHT, buff=element_spacing)
            queue.add(element_group)

        queue.move_to(ORIGIN)
        self.add(queue)
        return queue

    def enqueue_element(self, queue, element):
        new_element = Rectangle(height=0.6, width=1, fill_opacity=0.7)
        new_text = Text(str(element)).next_to(new_element, UP)
        new_element_group = VGroup(new_element, new_text)
        new_element_group.next_to(queue[-1], RIGHT, buff=0.2)
        self.play(Create(new_element_group))
        queue.add(new_element_group)

    def dequeue_element(self, queue):
        dequeued_element = queue[0]
        self.play(FadeOut(dequeued_element))
        queue.remove(dequeued_element)
        for element in queue:
            self.play(element.animate.shift(LEFT))