from manim import *


class OpenbsdComDumb(ZoomedScene):

    bridge1 = [
        "Hello,",
        "Are there any experts out there?",
        "Please reply if you can help me.",
        "I just rm -rf'ed /home",
        "I don't know how",
        "But I need this feature now.",
        "My users are pained",
        "I need my server up again.",
        "Relax.",
        "The list needs a dmesg first.",
        "Just the basic facts",
        "Stop whining between your blurts.",
    ]

    bridge2 = [
        "OK",
        "Just a little firewall pin prick",
        "There'll be lots of aaaaaaaah!",
        "You're p0wn3d by a script kiddie dick.",
        "Can you upgrade?",
        "We do believe it's working, good.",
        "That'll keep you going for a while.",
        "Our patience is at null.",
    ]

    chorus1 = [
        "There is no wifi, you are pleading.",
        "Vendor firmware not on horizon.",
        "Packets only coming through in waves.",
        "Your lips move but broken audio", "mutes what you're saying.",
        "Fork-bomb child. Crappy C coder.",
        "Bad PF ruleset. Machines fall down, go boom.",
        "Now we've got that feeling once again.",
        "We can't explain, you would not understand.",
        "This is just how you are.",
        "Original poster, you ...", "have become comfortably dumb.",
    ]

    chorus2 = [
        "There is no wifi, you are pleading.",
        "Vendor firmware not on horizon.",
        "Packets only coming through in waves.",
        "Your lips move but broken audio", "mutes what you're saying.",
        "Fork-bomb child.",
        "I can no longer handle reading misc.",
        "I want to scrape out both my eyes.",
        "I tried to reply but your address bounced.",
        "I give you my middle finger now.",
        "My inner child is crushed.",
        "My dreams are gone.",
        "You ... have become comfortably dumb.",
    ]

    image = None

    count_bridge = 1

    def createText(self, text, color='#FFCC00', weight=BOLD):
        return Text(text, font="sans-serif", color=color, weight=weight, font_size=46)

    def construct(self):
        self.add_sound('./content/song60d.mp3')
        self.image = ImageMobject('./content/comdumb.jpg').shift(3 * DOWN)
        self.image.width = 7
        self.add(self.image)
        
        title = VGroup(
            self.createText("OpenBSD 6.0", GREY, NORMAL).shift(3.5 * UP),
            self.createText("Comfortably Dumb", GREY, NORMAL).shift(2.9 * UP),
            self.createText("(the misc song)", GREY, NORMAL).shift(2.3 * UP))
        title.shift(5.5 * LEFT)
        title.width = 2.5
        self.add(title)

        self.wait(5)
        self.remove(self.image)

        self.show_bridge(self.bridge1)

        self.show_chorus(self.chorus1)

        self.show_bridge(self.bridge2)

        self.show_chorus(self.chorus2)

    def show_chorus(self, chorus):
        text = VGroup(
            self.createText(chorus[0]).shift(2 * UP),
            self.createText(chorus[1]).shift(UP),
            self.createText(chorus[2]),
            self.createText(chorus[3]).shift(DOWN),
            self.createText(chorus[4]).shift(2 * DOWN),
        )
        self.add(text)
        self.wait(28)
        self.remove(text)

        text = VGroup(
            self.createText(chorus[5]).shift(2 * UP),
            self.createText(chorus[6]).shift(UP),
            self.createText(chorus[7]),
            self.createText(chorus[8]).shift(DOWN),
        )
        self.add(text)
        
        if self.count_bridge == 2:
            self.wait(27)
            self.remove(text)
            text = VGroup(
                self.createText(chorus[9]).shift(UP),
                self.createText(chorus[10]),
                self.createText(chorus[11]).shift(DOWN),
            )
            self.add(text)
            self.wait(15)
            self.remove(text)
        elif self.count_bridge == 3:
            print(self.count_bridge)
            self.wait(21)
            self.remove(text)
            text = VGroup(
                self.createText(chorus[9]).shift(2 * UP),
                self.createText(chorus[10]).shift(UP),
                self.createText(chorus[11]),
                self.createText(chorus[12]).shift(DOWN),
            )
            self.add(text)
            self.wait(20)
            self.remove(text)

        self.add(self.image)
        self.wait(28)
        self.remove(self.image)

        if self.count_bridge == 2:
            text = VGroup(
                self.createText(chorus[10]),
                self.createText(chorus[11]).shift(DOWN),
            )
            
            self.add(text)
            self.wait(14)
            self.remove(text)

    def show_bridge(self, bridge):
        text = VGroup(
            self.createText(bridge[0]).shift(2 * UP),
            self.createText(bridge[1]).shift(UP),
            self.createText(bridge[2]),
            self.createText(bridge[3]).shift(DOWN)
        )
        self.add(text)
        self.wait(16)
        self.remove(text)

        text = VGroup(
            self.createText(bridge[4]).shift(2 * UP),
            self.createText(bridge[5]).shift(UP),
            self.createText(bridge[6]),
            self.createText(bridge[7]).shift(DOWN)
        )
        self.add(text)
        self.wait(16)
        self.remove(text)
        
        if self.count_bridge == 1:
            text = VGroup(
                self.createText(bridge[8]).shift(2 * UP),
                self.createText(bridge[9]).shift(UP),
                self.createText(bridge[10]),
                self.createText(bridge[11]).shift(DOWN)
            )
            self.add(text)
            self.wait(15)
            self.remove(text)   

        self.count_bridge += 1        
 