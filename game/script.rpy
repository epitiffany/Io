

# Script for .....

define f = Character("Alex", callback=callbackcontinue)
define g = Character("Bandit", callback=callbackcontinue)
define w = Character("Wizzie", callback=callbackcontinue)



# The game starts here.

label start:

    show dark
    show jack

    play sound "audio/begin.mp3"
    "It's Halloween night. The moon is shining bright."
    "You can sense the anticipation in the air, mixed in with a little fear."
    stop sound fadeout 3.0

    # Haunted House
    scene house
    play sound "audio/crowd.mp3" fadein 2.0 fadeout 3.0 loop
    "You stand in front of a line of people waiting to enter the haunted house."
    "You hear your friend starting to grow impatient."
    f "Are we going inside or what?"
    stop sound fadeout 2.0
    menu:
        "Yes":
            play sound "audio/click.mp3"
            scene door
            play sound "audio/open.mp3"
            "You gather up your strength and step inside the looming house."
            play sound "audio/click.mp3"
            jump darkness
        "Or what":
            f "Well too bad. I didn't wait this long just to turn around and go home."
            scene door
            play sound "audio/open.mp3"
            "You timidly make your way into the house, bracing yourself for what you're about to see."
            play sound "audio/click.mp3"
            jump darkness

    # Enter Bandit
    label darkness:
        scene dark
        show teen
        play sound "audio/boo.mp3"
        "You expect to be jump scared by a poorly costumed teenager, but wait...."
        play sound "audio/click.mp3"
        hide teen
        show confusion
        "Something feels off."
        play sound "audio/click.mp3"
        "You're surrounded by utter and complete darkness. The air seems to stand still."
        hide confusion
        play sound "audio/click.mp3"
        play sound "audio/wind.mp3" fadein 3.0 fadeout 15.0
        "After what seems like hours, you start to hear something."
        play sound "audio/click.mp3"
        stop sound fadeout 1.0
        show flash:
            alpha 1.0
            time 1.0
            alpha 0.0
        play sound "audio/flash.mp3"
        show ghost behind flash
        "Suddenly, you're blinded by a brief flash of bright light."
        play sound "audio/click.mp3"
        "An apparation has appeared in front of you."
        play sound "audio/click.mp3"
        hide ghost
        show ghello
        g "Hey there! Sorry if I scared you. That seems to be the only way I can enter into worlds."
        hide ghello
        show ghost
        menu:
            "Worlds?":
                play sound "audio/click.mp3"
                jump ghost_worlds
            "Who are you? Where is everything?":
                play sound "audio/click.mp3"
                jump ghost_intro

    label ghost_worlds:
        hide ghost
        show garms
        g "Yes worlds! There are billions of them, but for some reason the human eye can only see one."
        hide garms
        show ghost
        g "That's probably why you guys are always stuck in your houses these days huh? No places to explore."
        menu:
            "Who are you?":
                play sound "audio/click.mp3"
                jump ghost_intro


    # Pick Weapons

    label ghost_intro:
        g "I'm Bandit. I'll be your acting guide for where we're heading."
        g "We're almost there actually. You're gonna love it!"
        hide ghost
        show gshock
        g "I almost forgot! You need to pick a weapon quickly!"
        play sound "audio/appear.mp3"
        hide gshock
        call screen weapons

    label stick_picked:
        scene sparkle
        show stick
        play sound "audio/glitter.mp3" fadein 5.0 fadeout 3.0
        "You picked the stick!"
        play sound "audio/click.mp3"
        jump cyclops

    label staff_picked:

        scene sparkle
        show staff
        play sound "audio/glitter.mp3" fadein 5.0 fadeout 3.0
        "You picked the staff!"
        play sound "audio/click.mp3"
        jump imp

    label sword_picked:
        scene sparkle
        show sword
        play sound "audio/glitter.mp3" fadein 5.0 fadeout 3.0
        "You picked the sword!"
        play sound "audio/click.mp3"
        jump griffin

    # Enter Monsters

    label cyclops:
        scene volcano
        show cyclops with vpunch
        play sound "audio/growl.mp3"
        "A cyclops suddenly appears out of thin air!"
        play sound "audio/click.mp3"
        jump end

    label imp:
        scene dark
        show imp with vpunch
        "An imp suddenly lands in front of you!"
        play sound "audio/click.mp3"
        jump end

    label griffin:
        scene dark
        show griffin with vpunch
        "You find yourself face to face with an enormous griffin!"
        play sound "audio/click.mp3"
        jump end

    label end:
        "TBC....."

    # label wizzie:
    #     scene dark
    #     show wizzie
    #     w "Hi there, you seem lost. Maybe we could help each other out?"
    #     play sound "audio/click.mp3"
    #     menu:
    #         "What do you mean? How do I get home?":
    #             play sound "audio/click.mp3"
    #             w "Like I said, I'll help you out, if you help me."
    #             w "Look, you see how my wand is broken? Could you go and grab some materials so I can make a new one?"
    #             jump quest
    #
    # label quest:
    #     scene dark
    #     show wizzie
    #     menu:
    #         "Fine. What do you need?":
    #             w "Perfect! You're too kind. I need a harpy feather and some willow tree bark."
    #             "You ask the shady wizard where to find these items."
    #             w "Oh, those are easy to find. There's a griffin down that path right there who has what I need."
    #             w "He may take some convincing, though...."
    #             w "Well, off you go then. Good luck strange traveler! Hope to see you alive and soon."
    #             jump trail
    #         "I'll pass.":
    #             w "Well, fine. I was just trying to do you a favor."
    #             w "Just know, there will be consequences to denying me."
    #             jump death
    # label trail:
    #     "hello"
    #
    # label death:
    #     "hello"




    # This ends the game.

    return
