from manim import *


class OpenbsdPlanetUsers(ZoomedScene):

    bridge1 = [
        "Welcome to the future",
        "One very rich man",
        "runs the Earth with",
        "one multinational",
        "owns your stuff",
        "and owns your birth",
        "Everyone is armless",
        "Personal robots",
        "Do it all for you",
        "Sitting on your slug head",
        "One channel TV",
        "never gonna bore you",
    ]

    bridge2 = [
        "Everyone is happy",
        "No more government",
        "No more media",
        "Only the Company",
        "Entertains you",
        "while it feeds you",
        "Soylent Green pap",
        "Eating your friends while",
        "shopping, buying",
        "Stupid applications",
        "Obsolete before you try them",
    ]

    bridge3 = [
        "Way back in my time",
        "Open source kept",
        "everyone choosing",
        "People knew the insides",
        "Of devices they were using",
        "Hackers had a doorway",
        "Now it's locked and",
        "dumbed down so much",
        "One button coma",
        "Stop the future truly outta touch",
    ]

    coda = [
        "Take me back",
        "Take me back",
        "Please",
        "Take me back",
    ]

    chorus = [
        "Does it sound like a paradise",
        "or a way to die",
        "while alive and a loser",
        "I'm a man from the open past",
        "And I'll never last",
        "on the Planet of the Users",
    ]

    count_bridge = 1

    def createText(self, text, color='#CCCC00'):
        return Text(text, font="sans-serif", color=color)

    def construct(self):
        self.add_sound('./content/song46.mp3')
        image = ImageMobject('./content/planetusers.jpg').shift(3 * DOWN).shift(5.5 * LEFT)
        self.add(image)
        
        title = VGroup(
            self.createText("OpenBSD 4.6", GREY).shift(3.5 * UP),
            self.createText("Planet of the Users", GREY).shift(2.9 * UP))
        title.shift(5.5 * LEFT)
        title.width = 2.5
        self.add(title)

        self.show_bridge(self.bridge1)

        self.show_chorus()

        self.show_bridge(self.bridge2)

        self.show_chorus()

        text = VGroup(
            self.createText(self.coda[0]).shift(2 * UP),
            self.createText(self.coda[1]).shift(UP),
            self.createText(self.coda[2]),
            self.createText(self.coda[3]).shift(DOWN)
        )
        self.add(text)
        self.wait(19.5)
        self.remove(text)

        self.show_bridge(self.bridge3)

        self.show_chorus()

    def show_chorus(self):
        text = VGroup(
            self.createText(self.chorus[0]).shift(2 * UP),
            self.createText(self.chorus[1]).shift(UP),
            self.createText(self.chorus[2]),
            self.createText(self.chorus[3]).shift(DOWN),
            self.createText(self.chorus[4]).shift(2 * DOWN),
            self.createText(self.chorus[5]).shift(3 * DOWN),
        )
        self.add(text)
        self.wait(16)
        self.remove(text)

    def show_bridge(self, bridge):
        text = VGroup(
            self.createText(bridge[0]).shift(2 * UP),
            self.createText(bridge[1]).shift(UP),
            self.createText(bridge[2]),
            self.createText(bridge[3]).shift(DOWN)
        )
        self.add(text)
        if self.count_bridge == 2:
            self.wait(9)
        else: 
            self.wait(8)
        self.remove(text)

        text = VGroup(
            self.createText(bridge[4]).shift(2 * UP),
            self.createText(bridge[5]).shift(UP),
            self.createText(bridge[6]),
            self.createText(bridge[7]).shift(DOWN)
        )
        self.add(text)
        if self.count_bridge == 3:
            self.wait(9.5)
        else: 
            self.wait(9)
        self.remove(text)

        if (len(bridge) == 12):
            text = VGroup(
                self.createText(bridge[8]).shift(2 * UP),
                self.createText(bridge[9]).shift(UP),
                self.createText(bridge[10]),
                self.createText(bridge[11]).shift(DOWN)
            )
        elif (len(bridge) == 11):   
            text = VGroup(
                self.createText(bridge[8]).shift(UP),
                self.createText(bridge[9]),
                self.createText(bridge[10]).shift(DOWN),
            )     
        elif (len(bridge) == 10):   
            text = VGroup(
                self.createText(bridge[8]).shift(UP),
                self.createText(bridge[9]),
            ) 
        self.add(text)
        if self.count_bridge == 3:
            self.wait(6)
        else: 
            self.wait(8)
        self.remove(text)
        self.count_bridge += 1        









        
        