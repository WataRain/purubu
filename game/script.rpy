# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character(kind=nvl)
define pl = Character(
    name=None, kind=nvl, what_prefix="Lowy: \"", what_suffix="\"")

# The game starts here.

label start:
    define menu = nvl_menu
    
    play music playfultanuki fadein 1.0

    show real laptop lowy at truecenter:
        zoom 2.8

    "One fine morning..."

    pl """
    I am Lowest from the PuruBu! I am the cutest of the cute! I am a first-year
    student at De La Sarru University. To be more specific, I'm in the College
    of Computer Science.
    """

    menu:
        "1. You are very cute!":
            pl "You sure know how to flatter somebody, eh?
            Now what did you say your name was, again?"
        "2. Studies.":
            pl """
            ...'Studies'? My studies are going well, thank you for asking!
            Now what did you say your name was, again?
            """

    label do_name:
        $ name = renpy.input("Name", length=16)
        if name == "":
            pl "...Hello? Still a bit sleepy? What's your name?"
            jump do_name

    define you = Character(
        name=None, kind=nvl, what_prefix="[name]: \"", what_suffix="\"")
    
    stop music

    you "I'm [name]#*$(#*@)($*#9413912=4-2+3)342="

    nvl clear
    nvl hide

    show real laptop lowy with pixellate:
        ease 0.5 zoom 1.0
    
    pause 0.5

    """
    Oh come on, a Segmentation Fault?! Do those things even happen in Python?!
    Argh, guess I'll just pack up and get going to school, then...
    """

    nvl clear

    play music ojouslamentation fadein 1.0
    scene bg road day with Dissolve(time=1.0)

    """
    Now this is more like it! The skies are blue, the rocks are gray, the roads
    are... also gray... Sigh... Have I gotten this bored of life already?
    """

    """
    It's been two weeks since I entered the prestigious De Lulu Sayo University,
    and I, Lowi, haven't been doing anything interesting.
    """

    """
    I got accepted into the course I wanted -- Computer Science -- and
    I've been a total academic weapon, but the scenes I've seen of the so-called
    "university life" on anime haven't happened to me at all...
    """

    """
    Ideally, I'd be having parties, but I can't ever talk better than a
    fifth-grader for the life of me; drinks, though I would sooner drink ten 
    liters of ice tea than a drop of wine; and, above all...
    """
    
    """
    Someone to get together with, but only a person that looks like Misaki
    Tobisawa from the hit game Aokana: Four Rhythms Across the Blue, and dresses
    like her, talks like her and eats like her would do!
    """

    """
    ...You know, maybe there is a reason why none of these have happened to me.
    """
    
    nvl clear

    """
    I mean, I've just been spending all this time doing nothing but attend
    classes, go home, lurk in Reddit and Discord, and program that stupid little
    VN as a way to project the reality I really want for myself.
    """

    """
    Who cares about some stupid VN made by some random person like me
    anyway? I know I haven't shown it to anyone but myself, but I doubt it'd be
    a blockbuster if I showed it to anyone but myself.
    """

    return
