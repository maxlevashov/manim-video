from manim import *


class MovingFrameBox(Scene):
    def construct(self):
        title = Text("Sliding window - maximum average subarray.").shift(2 * UP)
        text = MathTex(
            "1", "12", "-5", "-6", "50", "3", arg_separator=','
        ).shift(2 * DOWN)
        group1 = VGroup(text[0], text[1], text[2], text[3])
        group2 = VGroup(text[1], text[2], text[3], text[4])
        group3 = VGroup(text[2], text[3], text[4], text[5])
        problem = MathTex("Input: [1, 12, -5, -6, 50, 3], k = 4, Output: 12.75").shift(UP)
        sumTemp = MathTex(
            "(1 + 12 +(-5) +(-6)) = 2",
            "2 - 1 + 50 = 51",
            "51 - 12 + 3 = 42",
            "51 / 4 = 12.75"
        ).shift(DOWN)
        maxValue = MathTex("max = 0", "max  = 2", "max  = 51")
        text.width = 3
        self.play(Write(title))
        self.play(Write(problem))
        self.play(Write(text))
        self.play(Write(maxValue[0].shift(2 * RIGHT)))

        framebox1 = SurroundingRectangle(group1, buff=.1)
        framebox2 = SurroundingRectangle(group2, buff=.1)
        framebox3 = SurroundingRectangle(group3, buff=.1)
        self.play(
            Create(framebox1)
        )
        self.wait(2)

        self.play(Write(sumTemp[0].shift(3 * RIGHT)))
        self.play(FadeOut(maxValue[0]))
        self.play(Write(maxValue[1]))

        self.wait(2)
        self.play(
            ReplacementTransform(framebox1, framebox2)
        )
        self.wait(2)
        self.play(FadeOut(sumTemp[0]))

        self.play(Write(sumTemp[1]))
        self.wait(2)
        self.play(FadeOut(maxValue[1]))
        self.play(Write(maxValue[2].shift(2 * LEFT)))
        self.wait(2)
        self.play(
            ReplacementTransform(framebox2, framebox3)
        )
        self.wait(2)
        self.play(FadeOut(sumTemp[1]))
        self.play(Write(sumTemp[2].shift(3 * LEFT)))
        self.wait(2)
        self.play(FadeOut(maxValue[2]))
        self.play(Write(maxValue[2]))
        self.wait(2)
        self.play(FadeOut(sumTemp[2]))
        self.play(Write(sumTemp[3].shift(6 * LEFT)))
        self.wait(4)
