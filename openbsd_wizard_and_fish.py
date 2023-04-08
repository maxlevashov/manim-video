from manim import *


class OpenbsdWizardAndFish(ZoomedScene):

    bridge1 = [
        "Once there was a Wizard so old and wise",
        "that he asked Mother Night for a new enterprise",
        "falling asleep his wish was heard",
        "and by Merlin's beard",
        "what a strange world he entered",
    ]

    bridge2 = [
        "In this world existed only zeros and ones",
        "never had a Wizard seen such duality, not once",
        "He approached one of the zeros and said",
        "Who are you?",
        "I'm a zero",
        "yes, I see, but what do you do?",
        "The zero said",
        "I am the beginning and the end",
    ]

    bridge3 = [
        "Never had our Wizard met such a strange friend",
        "He did not understand at all what he saw",
        "and walking on this time met another strange fella",
        "he approached the one and said:",
        "Who are you?",
        "I'm One",
        "Yes, I see, but what do you do?",
        "The one said: I am everything in between",
    ]

    bridge4 = [
        "The Wizard could not believe what his eyes had just seen",
        "He sat down on a stone feeling tired and alone",
        "missing his friends in the binary unknown",
        "silent and sad he played with his beard",
        "suddenly, a little fish appeared!",
    ]

    bridge5 = [
        "The Wizard said: you are not a zero or a one?",
        "No, I'm a fish, come swim with me, come",
        "They swam together and dived",
        "deep into the ocean",
        "until they found the place",
        "where it once all began",
    ]

    bridge6 = [
        "The little fish took a small rake and starting raking the sand",
        "and the Wizard was amazed by the waves of this new friend",
        "he said",
        "Little fish, who are you?",
        "I'm a gardener, don't you see?",
        "Well, yes, but what do you do?",
        "The little fish - without stopping - calmly made clear",
        "My task is important, this is what I do here,",
        "the sand contains crucial information",
        "which I need to order",
        "before the rising of the sun.",
    ]

    bridge7 = [
        "Suddenly, from far, a big whale appeared",
        "The Wizard, frightend, quickly hid behind his beard",
        "The whale opened his mouth",
        "but instead of swallowing our friend",
        "released from his tongue",
        "piles and piles of new sand.",
        "The Wizard, startled, opened his mouth",
        "but the fish said",
        "No no no, no questions allowed,",
        "we do not need to know where he comes from or goes",
        "for a little mystery is what gives us purpose.",
    ]

    bridge8 = [
        "Finally something the Wizard could understand",
        "he had found the mystery underneath the beginning", "and the end",
        "he had dived way below everything in between",
        "and saw the biggest whale he had ever seen",
    ]

    bridge9 = [
        "He said My dear fish, what you do, I can see,",
        "is raking the maritime soil of mystery",
        "from now on, I will protect you, your sand, and your shells,",
        "coming back every year to update my spells.",
    ]

    bridge10 = [
        "They said their goodbyes",
        "and the Wizard returned",
        "to his nice and warm bed,",
        "with all his lessons learned",
        "He was happy that he now understood this strange place",
        "and could protect his new friends for the rest of his days",
    ]


    def createText(self, text, color='#CCCC00', weight=NORMAL):
        return Text(text, font="sans-serif", color=color, weight=weight, font_size=38)

    def construct(self):
        self.add_sound('./content/song73.ogg')
        
        title = VGroup(
            self.createText("OpenBSD 7.3", GREY, BOLD),
            self.createText("The Wizard and the Fish", GREY, BOLD).shift(2 * UP))
        
        self.add(title)

        self.wait(9)
        self.remove(title)

        self.show_bridge1(self.bridge1, 23)

        self.show_bridge1(self.bridge2, 28)

        self.show_bridge1(self.bridge3, 34)

        self.show_bridge1(self.bridge4, 23)

        self.show_bridge1(self.bridge5, 19)

        self.show_bridge2(self.bridge6, 21, 18)

        self.show_bridge2(self.bridge7, 21, 18)

        self.show_bridge1(self.bridge8, 19)

        self.show_bridge1(self.bridge9, 20)

        self.show_bridge1(self.bridge10, 19)

    def show_bridge1(self, bridge, wait):
        result = []
        for index, element in enumerate(bridge):
            result.append(self.createText(element))

        text = VGroup(*result).arrange(direction=DOWN)
        
        self.add(text)
        self.wait(wait)
        self.remove(text)

    def show_bridge2(self, bridge, wait1, wait2):
        text = VGroup(
            self.createText(bridge[0]).shift(2 * UP),
            self.createText(bridge[1]).shift(UP),
            self.createText(bridge[2]),
            self.createText(bridge[3]).shift(DOWN),
            self.createText(bridge[4]).shift(2 * DOWN),
            self.createText(bridge[5]).shift(3 * DOWN)
        )
        self.add(text)
        self.wait(wait1)
        self.remove(text)   
        
        text = VGroup(
            self.createText(bridge[6]).shift(2 * UP),
            self.createText(bridge[7]).shift(UP),
            self.createText(bridge[8]),
            self.createText(bridge[9]).shift(DOWN),
            self.createText(bridge[10]).shift(2 * DOWN)
        )
        self.add(text)
        self.wait(wait2)
        self.remove(text)  

       
 
