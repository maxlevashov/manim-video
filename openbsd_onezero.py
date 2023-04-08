from manim import *


class OpenbsdOneZero(ZoomedScene):

    bridge1 = [
        "The starting line is nervous",
        "we burst upon the course",
        "Electric is our passion",
        "An open hearted force",
        "The water's full of dangers",
        "That interrupt the flow",
        "And soon the spirit splinters",
        "as temptation takes its toll",
    ]

    bridge2 = [
        "The window is a wall by now",
        "A sieve of sickened holes",
        "The water chicken stealing maps",
        "Mistaking us for foes",
        "The sun a son of Icarus",
        "Flies too close to itself",
        "Forbidden fruit is blinded",
        "by the toys upon the shelf",
    ]

    bridge3 = [
        "Slow and steady wins they say",
        "but this is not a race",
        "It's not about who takes a prize",
        "for first or second place",
        "Imaginary rings of brass",
        "Were traded for real goals",
        "The vision and the mission lost",
        "For those with corporate souls",
    ]

    coda1 = [
        "One Zero Zero Zero Zero One",
    ]

    coda2 = [
        "One Zero One Zero One Zero One",
    ]

    chorus = [
        "Give and get back some",
        "Sharing it all",
        "Path we know best",
        "we're having a ball",
        "Opulent mission",
        "Lost in our passion",
        "You can still choose",
        "If you don't swim to win",
        "you'll never lose",
        "Give and get zeros",
        "Give and get ones",
        "Given to you but",
        "Not you to us",
    ]

    count_bridge = 1

    def createText(self, text, color='#CCCC00', weight=BOLD):
        return Text(text, font="sans-serif", color=color, weight=weight)

    def construct(self):
        self.add_sound('./content/song42.mp3')
        image = ImageMobject('./content/marathon.jpg').shift(3 * DOWN).shift(5.5 * LEFT)
        self.add(image)
        
        title = VGroup(
            self.createText("OpenBSD 4.2", GREY, NORMAL).shift(3.5 * UP),
            self.createText("100001 1010101", GREY, NORMAL).shift(2.9 * UP))
        title.shift(5.5 * LEFT)
        title.width = 2.5
        self.add(title)

        self.wait(30)

        self.show_bridge(self.bridge1)

        self.show_chorus()

        text = self.createText(self.coda1[0])
        self.add(text)
        self.wait(12)
        self.remove(text)

        self.show_bridge(self.bridge2)

        self.show_chorus()

        self.wait(34)
        text = self.createText(self.coda2[0])
        self.add(text)
        self.wait(11)
        self.remove(text)

        self.show_bridge(self.bridge3)

        self.show_chorus(True)

    def show_chorus(self, last=False):
        text = VGroup(
            self.createText(self.chorus[0]).shift(2 * UP),
            self.createText(self.chorus[1]).shift(UP),
            self.createText(self.chorus[2]),
            self.createText(self.chorus[3]).shift(DOWN),
        )
        self.add(text)
        self.wait(7)
        self.remove(text)

        if last:
            text = VGroup(
                self.createText(self.chorus[9]).shift(2 * UP),
                self.createText(self.chorus[10]).shift(UP),
                self.createText(self.chorus[11]),
                self.createText(self.chorus[12]).shift(DOWN),
            )
            self.add(text)
            self.wait(6.5)
            self.remove(text)

        text = VGroup(
            self.createText(self.chorus[4]).shift(2 * UP),
            self.createText(self.chorus[5]).shift(UP),
            self.createText(self.chorus[6]),
            self.createText(self.chorus[7]).shift(DOWN),
            self.createText(self.chorus[8]).shift(2 * DOWN),

        )
        self.add(text)
        self.wait(10)
        self.remove(text)

    def show_bridge(self, bridge):
        text = VGroup(
            self.createText(bridge[0]).shift(2 * UP),
            self.createText(bridge[1]).shift(UP),
            self.createText(bridge[2]),
            self.createText(bridge[3]).shift(DOWN)
        )
        self.add(text)
        self.wait(14)
        self.remove(text)

        text = VGroup(
            self.createText(bridge[4]).shift(2 * UP),
            self.createText(bridge[5]).shift(UP),
            self.createText(bridge[6]),
            self.createText(bridge[7]).shift(DOWN)
        )
        self.add(text)
        self.wait(12)
        self.remove(text)
        self.remove(text)
        self.count_bridge += 1        
 