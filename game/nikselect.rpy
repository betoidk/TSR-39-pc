label nik_chapter_select:


#Point reset (keep an eye on this)
$ SNY_Points =0
$ SOLDN_Points = 0
$ SOLDY_Points = 0
$ SOLDB_Points = 0
$ SOLDF_Points = 0
$ SOLDP_Points = 0
$ SOLDD_Points = 0
$ BKWALLET_Points =0
$ SN_Points =0
$ PD_Points =0
$ porterfirstchoice = " "
$ nikproposal = False

show black with dissolve

if (chapter_value == 1):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    pause 1.0
    window show
    scene powderroom with dissolve
    jump nikroute

if (chapter_value == 2):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    pause 1.0
    window show
    play background "sfx/whispers.ogg"
    jump nikroute2

menu:
    "Did you find Yao helpful, or suspicious?"

    "Helpful.":
        $ SNY_Points +=1
    "Suspicious.":
        $ SNY_Points +=0

menu:
    "Whose name did you give to Porter?"

    "Nik.":
        $ SOLDN_Points +=1
        $ porterfirstchoice = "Nik"
    "Yao.":
        $ SOLDY_Points +=1
        $ porterfirstchoice = "Yao"
    "Ben.":
        $ SOLDB_Points +=1
        $ porterfirstchoice = "Ben"
    "Felipe.":
        $ SOLDF_Points +=1
        $ porterfirstchoice = "Felipe"
    "Paul.":
        $ SOLDP_Points +=1
        $ porterfirstchoice = "Paul"
    "Dimitri.":
        $ SOLDD_Points +=1
        $ porterfirstchoice = "Dimitri"


menu:
    "What's the locker combination?"

    "8 turning right.":
        menu:
            "8 turning right.":
                menu:
                    "3 turning left.":
                        $ BKWALLET_Points +=0
                    "4 Turning left.":
                        $ BKWALLET_Points +=0
                    "5 Turning left.":
                        $ BKWALLET_Points +=0
            "15 turning right.":
                menu:
                    "3 turning left.":
                        $ BKWALLET_Points +=0
                    "4 Turning left.":
                        $ BKWALLET_Points +=0
                    "5 Turning left.":
                        $ BKWALLET_Points +=0
            "16 turning right.":
                menu:
                    "3 turning left.":
                        $ BKWALLET_Points +=0
                    "4 Turning left.":
                        $ BKWALLET_Points +=0
                    "5 Turning left.":
                        $ BKWALLET_Points +=0

    "8 turning left.":
        menu:
            "8 turning right.":
                menu:
                    "3 turning left.":
                        $ BKWALLET_Points +=0
                    "4 Turning left.":
                        $ BKWALLET_Points +=0
                    "5 Turning left.":
                        $ BKWALLET_Points +=0
            "15 turning right.":
                menu:
                    "3 turning left.":
                        $ BKWALLET_Points +=0
                    "4 Turning left.":
                        $ BKWALLET_Points +=0
                    "5 Turning left.":
                        $ BKWALLET_Points +=0
            "16 turning right.":
                menu:
                    "3 turning left.":
                        $ BKWALLET_Points +=1
                    "4 Turning left.":
                        $ BKWALLET_Points +=0
                    "5 Turning left.":
                        $ BKWALLET_Points +=0

    "9 turning left.":
        menu:
            "8 turning right.":
                menu:
                    "3 turning left.":
                        $ BKWALLET_Points +=0
                    "4 Turning left.":
                        $ BKWALLET_Points +=0
                    "5 Turning left.":
                        $ BKWALLET_Points +=0
            "15 turning right.":
                menu:
                    "3 turning left.":
                        $ BKWALLET_Points +=0
                    "4 Turning left.":
                        $ BKWALLET_Points +=0
                    "5 Turning left.":
                        $ BKWALLET_Points +=0
            "16 turning right.":
                menu:
                    "3 turning left.":
                        $ BKWALLET_Points +=0
                    "4 Turning left.":
                        $ BKWALLET_Points +=0
                    "5 Turning left.":
                        $ BKWALLET_Points +=0

$ print("Checking Nik values")
$ print(chapter_value)

if (chapter_value == 3):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    pause 1.0
    window show
    scene echodesertnight
    play background "sfx/crickets.ogg" fadein 3.0
    show nik eyes h at left,nightgreen
    show yao neutral h at right,nightgreen
    with dissolve
    jump nikroute3

menu:
    "Did you accept Nik's proposal?"

    "Yes.":
        $ SN_Points +=1
        $ nikproposal = True
    "I needed to think on it.":
        $ SN_Points +=0


menu:
    "Did you say you'd like to wear James Hendrick's armor?"

    "Yes.":
        $ SN_Points +=0
    "No.":
        $ SN_Points +=1

if (chapter_value == 4):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    jump nikroute3a


if BKWALLET_Points == 1:
    $ BKWALLET_Points += 1

if BKWALLET_Points == 2:
    menu:
        "During a conversation with Beckett at night, did you:"

        "Ask him about the time he screamed at you.":
            $ PD_Points +=1
        "Let it lie.":
            $ PD_Points +=0

menu:
    "During second meeting with Porter, did you change your previous answer?"

    "Yes.":
        menu:
            "Who did you name instead of [porterfirstchoice]?"

            "Nik." if SOLDN_Points == 0:
                $ SOLDN_Points +=1
                $ SOLDY_Points =0
                $ SOLDB_Points =0
                $ SOLDF_Points =0
                $ SOLDP_Points =0
                $ SOLDD_Points =0

            "Yao." if SOLDY_Points == 0:
                $ SOLDN_Points =0
                $ SOLDY_Points +=1
                $ SOLDB_Points =0
                $ SOLDF_Points =0
                $ SOLDP_Points =0
                $ SOLDD_Points =0

            "Ben." if SOLDB_Points == 0:
                $ SOLDN_Points =0
                $ SOLDY_Points =0
                $ SOLDB_Points +=1
                $ SOLDF_Points =0
                $ SOLDP_Points =0
                $ SOLDD_Points =0

            "Felipe." if SOLDF_Points == 0:
                $ SOLDN_Points =0
                $ SOLDY_Points =0
                $ SOLDB_Points =0
                $ SOLDF_Points +=1
                $ SOLDP_Points =0
                $ SOLDD_Points =0
                $ porterfirstchoice = "Felipe"

            "Paul." if SOLDP_Points == 0:
                $ SOLDN_Points =0
                $ SOLDY_Points =0
                $ SOLDB_Points =0
                $ SOLDF_Points =0
                $ SOLDP_Points +=1
                $ SOLDD_Points =0
                $ porterfirstchoice = "Paul"

            "Dimitri." if SOLDD_Points == 0:
                $ SOLDN_Points =0
                $ SOLDY_Points =0
                $ SOLDB_Points =0
                $ SOLDF_Points =0
                $ SOLDP_Points =0
                $ SOLDD_Points +=1
                $ porterfirstchoice = "Dimitri"


    "No.":
        pause 0.05

menu:
    "How did you feel about Yao before going to extract the gold?"

    "I was glad I pushed my doubts about him back.":
        $ SNY_Points +=1
    "I felt he still can’t be trusted.":
        $ SNY_Points =0

if SNY_Points==0 and nikproposal==False:
    menu:
        "Did you accept Nik's proposal the second time he asked, after the cave-in in the mines?"

        "Yes.":
            $ nikproposal = True
        "No.":
            $ nikproposal = False

if (chapter_value == 5):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    scene bg black with dissolve
    window show
    if SNY_Points >0:
        play music ("music/quiet.ogg") fadein 2.5
        scene echobackalley
        show wil talking
        with dis3
        jump nikroute3d1
    else:
        play music ("music/contemplation.ogg") fadein 2.5
        scene echobackalley
        show wil shocked
        with dis3
        jump nikroute3d2

if (chapter_value == 6):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    $ renpy.music.set_volume(0.8, delay=1.0, channel='music')
    $ renpy.music.set_volume(0.5, delay=1.0, channel='ambient')
    $ renpy.music.set_volume(0.5, delay=1.0, channel='background')
    if SOLDY_Points ==1 or SOLDB_Points==1:
        play music ("sfx/death.ogg") fadeout 3.0 fadein 2.0
        scene bg black with dissolve
        window show
        jump nikroute4a
    else:
        scene bg minequarryevening with dissolve
        window show
        pause 1.0
        jump nikroute4b
