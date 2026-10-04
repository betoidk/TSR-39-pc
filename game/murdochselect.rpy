label murdoch_chapter_select:

show black with dissolve
$ hollyconversation = True
$ jimconversation = True
$ reubinconversation = True
$ neilconversation = True
$ ralphconversation =True
$ melissaconversation = True
$ murdochconversation = True
$ cynthiaconversation = True
$ blitheconversation = True
$ auditoriumvisit = 2
$ basementvisit = 2
$ classroomvisit = 2
$ officevisit = 2
$ libraryvisit = 2
$ ralauditoriumvisit = True
$ ralbasementvisit = True
$ ralclassroomvisit = True
$ ralofficevisit = True
$ rallibraryvisit = True
$ jimauditoriumvisit = True
$ jimbasementvisit = True
$ jimclassroomvisit = True
$ jimofficevisit = True
$ jimlibraryvisit = True
$ melauditoriumvisit = True
$ melbasementvisit = True
$ melclassroomvisit = True
$ melofficevisit = True
$ mellibraryvisit = True
$ bliauditoriumvisit = True
$ blibasementvisit = True
$ bliclassroomvisit = True
$ bliofficevisit = True
$ blilibraryvisit = True
$ dahprogress = 0
$ dahliaanswer = 0
$ dahliaanswer1 = -1
$ dahliaanswer2 = -1
$ finalpuzzle = ""
$ attemptcount = 0
$ medicineprogress = 0
$ missingreagent = ""

if (chapter_value == 1):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    pause 1.0
    jump Murdochroute

if (chapter_value == 2):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    pause 1.0
    jump murdochroute2

if (chapter_value == 3):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    pause 1.0
    jump murdochroute3

if (chapter_value == 4):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    pause 1.0
    scene bg echochurchinterior with dissolve
    window show
    play sound ("sfx/schooldoor.ogg")
    jump murdochroute3c

menu:
    "After escaping the fire and reaching the school, did you manage to reach the observatory?" #Not gonna try to simulate the entire schools exploration, so just

    "Yes.":
        $ dahprogress = 4
        $ murdochchoices = "When Dahlia asked for the count of celestial bodies, what was your answer?"
        $ dahliaanswer = renpy.input([murdochchoices], allow="0123456789", length=7)
        if dahliaanswer == "41" or dahliaanswer == "37":
            stop music2 fadeout 3.0
            stop background fadeout 3.0
            stop sound
            pause 1.0
            window show
            play music ("music/abyss.ogg") fadeout 3.0 fadein 3.5
            scene bg observatory at dark3
            show dah at center, night
            show expression AlphaMask("nightshadedah", At("dah frown", center)) as mask:
                alpha 0.6
            with slow_dissolve
            jump dahliasuccess
        else:
            stop music fadeout 3.0
            stop music2 fadeout 3.0
            stop background fadeout 3.0
            stop sound
            window show
            play background ("sfx/crickets.ogg") fadein 3.0
            jump dahliafailure


    "No.":

        stop music fadeout 3.0
        stop music2 fadeout 3.0
        stop background fadeout 3.0
        stop sound
        window show
        play background ("sfx/crickets.ogg") fadein 3.0
        pause 1.0
        jump dahliafailure


    "Repeat school exploration.":

        stop music fadeout 3.0
        stop music2 fadeout 3.0
        stop background fadeout 3.0
        stop sound
        window show
        play background ("sfx/crickets.ogg") fadein 3.0
        pause 1.0
        jump murdochroute4



if (chapter_value == 5):

    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    window show
    play background ("sfx/crickets.ogg") fadein 3.0
    pause 1.0
    jump murdochroute4
