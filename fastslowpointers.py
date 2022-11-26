from manim import *


class MovingFrameBox(Scene):
    def construct(self):
        title = Text("Fast & Slow Pointers - Linked List Cycle.").shift(3 * UP)

        vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        edges = [(1, 2), (2, 3), (3, 4), (4, 5),
                 (5, 6), (6, 7), (7, 8), (8, 3)]
        graphie = Graph(
            vertices,
            edges,
            layout={1: [-3, 0, 0],2: [-2, 0, 0],
                    3: [-1, 0, 0],4: [0, 0, 0],
                    5: [1, 0, 0], 6: [1, -1, 0],
                    7: [0, -1, 0], 8: [-1, -1, 0]},
            labels=True,
        )

        trackerSlow = ComplexValueTracker(-3 + 0.5j)
        dotSlow = Dot(color='GREEN').add_updater(
            lambda x: x.move_to(trackerSlow.points)
        )
        trackerFast = ComplexValueTracker(-3 + 0.5j)
        dotFast = Dot(color='RED').add_updater(
            lambda x: x.move_to(trackerFast.points)
        )

        self.add(graphie, title, dotSlow, dotFast)
        self.wait(1)
        self.play(trackerSlow.animate.set_value(-2 + 0.5j))
        self.play(trackerFast.animate.set_value(-1 + 0.5j))
        self.wait(1)
        self.play(trackerSlow.animate.set_value(-1 + 0.5j))
        self.play(trackerFast.animate.set_value(1 + 0.5j))
        self.wait(1)
        self.play(trackerSlow.animate.set_value(0 + 0.5j))
        self.play(trackerFast.animate.set_value(0 - 0.5j))
        self.wait(1)
        self.play(trackerSlow.animate.set_value(1 + 0.5j))
        self.play(trackerFast.animate.set_value(-1 + 0.5j))
        self.wait(1)
        self.play(trackerSlow.animate.set_value(1 - 0.5j))
        self.play(trackerFast.animate.set_value(1 + 0.5j))
        self.wait(1)
        self.play(trackerSlow.animate.set_value(0 - 0.5j))
        self.play(trackerFast.animate.set_value(0 - 0.5j))
        self.play(graphie[7].animate.set_color(YELLOW))
        self.wait(1)
