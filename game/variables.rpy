#characters
init python:
    def define_bilingual_char(name, color):
        return (
            Character(name, color=color, condition='lang == "english"'),
            Character(u"{}".format(name), color=color, condition='lang == "svenska"')
        )

    en, sv = Character(None, condition='lang == "english"'), Character(None, condition='lang == "svenska"')

    en_c, sv_c = define_bilingual_char("Cass", "#642929")
    en_a, sv_a = define_bilingual_char("Alvin", "#0d37a0")
    en_t, sv_t = define_bilingual_char("Tyler", "#0da037")
    en_b, sv_b = define_bilingual_char("Bella", "#da19ec")
    en_s, sv_s = define_bilingual_char("Starr", "#b429ff")
    en_bb, sv_bb = define_bilingual_char("Bear Blaine", "#1e6b2a")
    en_bs, sv_bs = define_bilingual_char("Burt Salem", "#ff0b0b")

#affections
default affection_dad = 0
default affection_bella = 0
default affection_bear = 0

default phone_bella = 0

default subtle_letter = True

image bg courtyard = "images/courtyard.jpg"
image bg hallway = "images/hallway.jpg"
image bg cass_bedroom = "images/cass_bedroom.jpg"
image bg classroom = "images/classroom.jpg"
image bg ice_rink = "images/ice_rink.jpg"

image bella happy = "images/bella happy.png"
image bella neutral = "images/bella neutral.png"
image bella thinking = "images/bella thinking.png"
image bella serius = "images/bella serius.png"
image bella scarred = "images/bella scarred.png"
image bella tied upp = "images/bella tied_upp.png"

image alvin happy = "images/alvin happy.png"
image alvin neutral = "images/alvin neutral.png"

image tyler happy = "images/tyler happy.png"
image tyler neutral = "images/tyler neutral.png"
image tyler angry = "images/tyler angry.png"
image tyler furius = "images/tyler furius.png"
image tyler thinking = "images/tyler thinking.png"

