default stickHov = "Unhovered"
default staffHov = "Unhovered"
default swordHov = "Unhovered"
screen weapons():


    text "Select a weapon" size 50 xalign 0.5 color "#ffffff"


    imagebutton idle im.Scale("staff.png", 500, 500) action Jump("staff_picked") hovered SetVariable("staffHov", "Hovered") unhovered SetVariable("staffHov", "Unhovered") ypos 0.15 focus_mask True
    imagebutton idle im.Scale("stick.png", 500, 500) action Jump("stick_picked") hovered SetVariable("stickHov", "Hovered") unhovered SetVariable("stickHov", "Unhovered") ypos 0.2 focus_mask True xpos 350
    imagebutton idle im.Scale("sword.png", 500, 500) action Jump("sword_picked") hovered SetVariable("swordHov", "Hovered") unhovered SetVariable("swordHov", "Unhovered") ypos 0.1 focus_mask True xpos 800


    showif stickHov == "Hovered":
        text "Stick" size 50 ypos 0.8 xpos 0.45 color "#ffffff"

    showif staffHov == "Hovered":
        text "Staff" size 50 ypos 0.8 xpos 0.10 color "#ffffff"

    showif swordHov == "Hovered":
        text "Sword" size 50 ypos 0.8 xpos 0.70 color "#ffffff"
