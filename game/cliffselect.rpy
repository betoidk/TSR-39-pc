label cliff_chapter_select:

show black with dissolve
#Point reset (keep an eye on this)
$ MT_Points = 0
$ HaveMap = False
$ FollowCM = False
$ SMC_Points = 0
$ tsyis = False

###############################
#CLIFFORD

#Chapter 1 label - can skip directly

if (chapter_value == 1):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    pause 1.0
    window show
    jump cliffroute

#Chapter 2 label
menu:
    "Did you object to Murdoch joining the trip?"

    "Yes.":
        $ MT_Points += 0
    "No.":
        $ MT_Points += 1

if (chapter_value == 2):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    pause 1.0
    jump cliffroute2

#Chapter 3 label

if MT_Points == 0:
    menu:
        "When Murdoch asked for an honest conversation after the attack in the woods, did you agree?"

        "Yes.":
            $ MT_Points += 1
        "No.":
            $ MT_Points += 0

menu:
    "Did you take the map?"

    "Yes.":
        $ HaveMap = True
    "No.":
        $ HaveMap = False

menu:
    "Did you follow Cliff and Murdoch into the abandoned cabin, or did you stay outside with Avery and Jeb?"

    "I followed inside.":
        $ FollowCM = True
    "I stayed outside.":
        $ FollowCM = False


menu:
    "Do you sleep with Murdoch at the hot springs?"

    "Yes.":
        $ SMC_Points += 1
    "No.":
        $ SMC_Points += 0


if (chapter_value == 3):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    pause 1.0
    jump cliffroute3

#End of last update label:

if SMC_Points == 1:
    menu:
        "As Cliff, did you choose to keep doing intimate things with Murdoch?"

        "Yes.":
            $ SMC_Points = 1
        "No.":
            $ SMC_Points = 0

menu:
    "As Cliff, what do bring up to Tsela and Yiska?"

    "You asked if a raiload system system would be helpful to the people in the settlement.":
        $ CorMor += 0
    "You said that there are plans to expand the Echo train station through the settlement.":
        $ CorMor += 1
        $ tsyis = True

menu:
    "As Cliff, what do you ask the Meseta woman running the trading post in the settlement?"

    "If she thinks there would be more business if more people passed through the area, bringing supplies.":
        $ CorMor += 0
    "Why there's only enough local business for one store?":
        $ CorMor += 1

if (chapter_value == 4):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    pause 1.0
    scene settlementstore with dissolve
    play music "music/generalstore.ogg" fadein 3.0
    window show
    jump aftercliffint2

if (chapter_value == 5):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    pause 1.0
    play background ("sfx/crickets.ogg") fadein 4.0
    scene bg black
    with dissolve
    window show
    jump cliffroute3a
