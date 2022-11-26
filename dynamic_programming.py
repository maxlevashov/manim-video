from manim import *


class MovingFrameBox(Scene):
    def construct(self):
        title = Text("Dynamic programming").shift(3 * UP)
        vertices = [1, 2, 3, 4, 5]
        edges = [(1, 2), (1, 3), (2, 4), (2, 5)]
        graphie = Graph(
            vertices,
            edges,
            layout={1: [0, 2, 0], 2: [-2, 1, 0],
                    3: [2, 1, 0], 4: [-4, 0, 0], 5: [0, 0, 0]},
            labels={1: "fib(5)", 2: "fib(4)", 3: "fib(3)", 4: "fib(3)", 5: "fib(2)"}
        )
        graphie.width = 4
        self.add(graphie, title)
        self.wait(1)
        new_edges = [(5, 6)];
        new_vertices = [6];
        
        graphie.add_vertices(
            *new_vertices,
            positions={6: [0, -1, 0]},
            labels={6: "fib(1)"}
        )
        self.add(graphie)
        self.wait(1)
        
        