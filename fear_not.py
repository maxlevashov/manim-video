from manim import *



class FearNot(ZoomedScene):


    def createText(self, text, color='#CCCC00', weight=BOLD):
        return Tex(text, font="sans-serif", color=color, weight=weight)

    def construct(self):
        self.add_sound('./content/song42.mp3')
        image = ImageMobject('./content/marathon.jpg').shift(3 * DOWN).shift(5.5 * LEFT)
        self.add(image)

        
        
        text = self.createText("asdfasfd")
        text.rotate(PI/2, axis = RIGHT)
        self.add(text)
        self.wait(12)
        self.remove(text)