scene house
scene dark
scene door
scene sparkle
scene volcano
init:
    image jack:
        im.Scale("jack.png", 650, 720)
        ypos 675

    image house:
        im.Scale("house.png", 1280, 720)

    image door:
        im.Scale("doorway.png", 1280, 720)

    image teen:
        im.Scale("teen.png", 1280, 720)

    image confusion:
            im.Scale("confusion.png",1280, 720)

    image dark:
        im.Scale("darkness.png",1280, 720)

    image flash:
        im.Scale("flash.png", 1280, 720)

    image ghost:
        "ghost.png"
        zoom 0.5
        xalign 0.5
        yalign 0.2

    image ghello:
        "ghost_hello.png"
        zoom 0.5
        xalign 0.5
        yalign 0.2

    image gshock:
        "shocked_ghost.png"
        zoom 0.5
        xalign 0.5
        yalign 0.2

    image garms:
        "ghost_arms.png"
        zoom 0.5
        xalign 0.5
        yalign 0.2

    image stick:
        "stick.png"
        zoom 0.5
        ypos 550

    image staff:
        "staff.png"
        zoom 0.5
        ypos 550

    image sword:
        "sword.png"
        zoom 0.5
        ypos 525
        xpos 700

    image sparkle:
        im.Scale("sparkle.png", 1280, 720)

    image imp:
        "imp.png"
        zoom 0.5
        yalign 0.05

    image griffin:
        "griffin.png"
        zoom 0.7
        yalign 0
        xalign 0.6

    image cyclops:
        "cyclops1.png"
        zoom 0.7
        yalign 1

    image volcano:
        im.Scale("volcano1.jpg", 1280, 720)


    image wizzie:
        "wizzie.png"
        zoom 0.7
        ypos 565



init python:
    def callbackcontinue(ctc, **kwargs):
        if ctc == "end":
            renpy.music.play("audio/click.mp3",channel="sound")
