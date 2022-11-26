from manim import *


class MovingFrameBox(Scene):
    def construct(self):
        title = Text("Two pointers - two sum.").shift(2 * UP)
        text = MathTex(
            "2", "4", "7", " 15", "22", arg_separator=','
        ).shift(2 * DOWN)
        sum = MathTex("Sum = 22").shift(UP)
        sumTemp = MathTex(
            "2 + 22 = 24",
            "4 + 22 = 26",
            "4 + 15 = 19",
            "7 + 15 = 22"
        )
        text.width = 3
        self.play(Write(title))
        self.play(Write(sum))
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[0], buff=.1)
        framebox2 = SurroundingRectangle(text[1], buff=.1)
        framebox3 = SurroundingRectangle(text[2], buff=.1)
        framebox4 = SurroundingRectangle(text[3], buff=.1)
        framebox5 = SurroundingRectangle(text[4], buff=.1)
        self.play(
            Create(framebox1)
        )
        self.play(
            Create(framebox5),
        )
        self.play(Write(sumTemp[0]))
        self.wait(2)
        self.play(sumTemp[0].animate.set_fill(RED))
        self.wait(2)
        self.play(FadeOut(sumTemp[0]))

        self.play(
            ReplacementTransform(framebox1, framebox2)
        )
        self.play(Write(sumTemp[1]))
        self.wait(2)
        self.play(sumTemp[1].animate.set_fill(RED))
        self.wait(2)
        self.play(FadeOut(sumTemp[1]))

        self.play(
            ReplacementTransform(framebox5, framebox4)
        )
        self.play(Write(sumTemp[2]))
        self.wait(2)
        self.play(sumTemp[2].animate.set_fill(RED))
        self.wait(2)
        self.play(FadeOut(sumTemp[2]))
        self.play(
            ReplacementTransform(framebox2, framebox3)
        )
        self.play(Write(sumTemp[3]))
        self.wait(2)
        self.play(sumTemp[3].animate.set_fill(GREEN))
        self.wait(2)

        self.play(text[2].animate.shift(UP))
        self.play(text[3].animate.shift(UP))
        self.wait(2)
