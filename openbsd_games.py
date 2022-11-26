from manim import *


class OpenbsdGames(ZoomedScene):

    text_list1 = [
        "You wanna know the truth?",
        "Intel's",
        "controlling you",
        "And Microsoft is too",
        "is too",
        "But this",
        "is nothing new",
        "With A.C.P.I.",
        "This endless mess so corporate",
        "Tangles and angles",
        "angles",
        "In what could be", "straight forward",
    ]

    text_list2 = [
        "Now on the motherboard",
        "Where all",
        "my life is stored",
        "Playing with garbage there",
        "there",
        "With rules",
        "so unfair",
        "Ruled by A.C.P.I.",
        "Whose heart is so corrupted",
        "Forcing us all to play",
        "play",
        "Our progress",
        "interrupted",
    ]

    text_list3 = [
        "Yes I'm a user",
        "And I'm not", "the only one",
        "I'm not a loser", "loser",
        "With help", "from Puffy Tron",
        "And we will find it",
        "The pin in all this heartache",
        "Map our devices", "devices",
        "And we know", "what it'll take",
    ]

    text_coda_list = [
        "On and on",
        "Can we all", "be wrong?",
        "All and all", "all",
        "We", "are one",
        "Clean the dream",
        "Gone wrong",
        "We are Tron", "Tron",
        "On and on", "and on",
    ]

    bridge_count = 1;

    def createText(self, text, color=YELLOW):
        return Text(text, font="sans-serif", color=color)

    def construct(self):
        self.add_sound('song45.mp3')
        image = ImageMobject('pufftron.jpg').shift(3 * DOWN).shift(5.5 * LEFT)
        #image.width = 20
        self.add(image)
        
        title = VGroup(
            self.createText("OpenBSD 4.5", YELLOW).shift(3.5 * UP),
            self.createText("Games", YELLOW).shift(2.9 * UP))
        title.shift(5.5 * LEFT)
        title.width = 1.8
        self.add(title)

        self.wait(6)
        
        self.chorus([])

        self.bridge(self.text_list1)

        self.prechorus([])

        self.chorus([])

        self.bridge(self.text_list2)

        self.prechorus([])

        self.chorus([])

        self.bridge(self.text_list3)

        self.prechorus([])

        self.bridge(self.text_coda_list)

        self.wait(24)

        self.chorus([])

    def bridge(self, text_list): 
        text = self.createText(text_list[0])
        self.play(DrawBorderThenFill(text))
        self.wait()
        self.remove(text)

        text1 = self.createText(text_list[1]).shift(UP).shift(2 * LEFT)

        text2 = self.createText(text_list[2]).shift(DOWN).shift(2 * RIGHT)
        self.play(Write(text1))
        self.play(Write(text2))
        self.wait(1.5)
        self.remove(text1)
        self.remove(text2)

        text = self.createText(text_list[3])
        text1 = self.createText(text_list[4], GREY).shift(3 * DOWN)

        self.play(AddTextLetterByLetter(text))
        self.add(text1)
        self.wait(1)
        if self.bridge_count == 4:
            self.wait(0.5)
        self.remove(text)
        self.remove(text1)

        text = self.createText(text_list[5]).shift(UP).shift(2 * LEFT)
        text.shift(UP)
        self.play(Create(text))
        text1 = self.createText(text_list[6]).shift(DOWN).shift(2 * RIGHT)
        text1.shift(DOWN)
        self.play(Create(text1))
        self.play(Uncreate(text))
        
        if self.bridge_count == 3:
            self.wait(0.5)
        if self.bridge_count == 4:
            self.wait(2)
        self.remove(text1)

        text = self.createText(text_list[7])
        self.play(GrowFromCenter(text))
        self.wait()
        self.play(ShrinkToCenter(text))

        text = self.createText(text_list[8])
        self.play(FadeIn(text))
        
        if self.bridge_count != 4:
            self.wait()
        if self.bridge_count < 4:
            self.play(FadeOut(text))
        if self.bridge_count == 4:
            self.remove(text)    
        
        text = self.createText(text_list[9])
        text1 = self.createText(text_list[10], GREY).shift(3 * DOWN)
        self.play(SpiralIn(text))
        self.add(text1)
        
        if self.bridge_count != 4:
            self.wait(2)
        self.play(FadeOut(text))
        self.remove(text1)
        
        tex_in = self.createText(text_list[11]).scale(2)
        tex_out = self.createText(text_list[12]).scale(2)
        self.play(FadeIn(tex_in, shift=DOWN, scale=0.66))
        self.play(ReplacementTransform(tex_in, tex_out))
        self.play(FadeOut(tex_out, shift=DOWN * 2, scale=1.5))

        self.bridge_count += 1

    def chorus(self, text_list):
        text = self.createText("I love to hate my PC").shift(1.5 * UP).shift(LEFT)
        self.play(Wiggle(text))
        self.wait(2)
        self.remove(text)

        text = self.createText("But now it's not so easy").shift(2 * DOWN).shift(RIGHT)
        self.play(ApplyWave(text))
        self.wait(1.4)
        self.remove(text)

        text = self.createText("Just wanna get this job done").shift(1.5 * UP).shift(RIGHT)
        self.play(Wiggle(text))
        self.wait(1.3)
        self.remove(text)

        text = self.createText("But these A.M.L. games are dumb").shift(1.5 * UP).shift(LEFT)
        self.play(ApplyWave(
            text, direction=RIGHT,
            time_width=0.5,
            amplitude=0.3))
        if self.bridge_count != 2:
            self.wait(1)
        
        self.remove(text)

    def prechorus(self, text_list):
        text1 = self.createText("Lost connections")
        self.play(Create(text1))
        text2 = self.createText("Lost my mind").shift(DOWN)

        if self.bridge_count > 3:
            text_string = "Oh Ooh Woah end of line"
        else:
            text_string = "It's such a waste of time"

        text3 = self.createText(text_string).shift(2 * DOWN)
        self.play(Create(text2))
        self.wait(0.5)
        self.play(Create(text3))

        self.wait(4)
        print(self.bridge_count)
        self.remove(text1)
        self.remove(text2)
        self.remove(text3)



        
        