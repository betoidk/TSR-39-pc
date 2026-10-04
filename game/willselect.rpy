label will_chapter_select:

show black with dissolve

#Point reset (keep an eye on this)
$ SW_Points =0
$ DD_Points =0
$ quick_menu = True
$ quick_menu_will = False
$ willnote = False
$ unlocked_journal_pages = 0
$ STAGNIGHT_Points = 0
$ STAGDAY_Points = 0
$ CITYHALLNIGHT_Points = 0
$ CITYHALLDAY_Points = 0
$ PORINT_Points = 0
$ MININT_Points = 0
$ ETHINT_Points = 0
$ HARINT_Points = 0
$ CYNINT_Points = 0
$ DORINT_Points = 0
$ BG_Light = 0
$ willstag1interview = False
$ willstag2interview = False
$ willstag3interview = False
$ willstag1interview2 = False
$ willstag2interview2 = False
$ willchall1interview = False
$ willchall2interview = False
$ willchall3interview = False
$ willmanorportrait1 = False
$ willmanorkitchen1 = False
$ willmanorlivingroom1 = False
$ willjamesfile = False
$ willjamesfolder = False
$ willjamestrash = False
$ chnighttext = "I should go to city hall."
$ stagnighttext = "I wonder what folks at the stag might have to offer?"
$ cynthiatext = ".."
$ jamestext = "Hendricks is usually up to something. Worst thing is, it's probably not illegal."
$ portertext = "City Hall holds a lot of secrets."
$ changtext = "Could a CGCS employee placed a hit on Cliff, or was it somebody else?"
$ huxley1 = "I need to find Reed."
$ huxley2 = "Marcy may know what happened to the gun."
$ huxley3 = "So what was Reed up to if he didn't place a hit on Cliff?"
$ etheltext = "The workers at the hip are the best source of information in town."
$ harlantext = "The staff at the hip turned a saloon in the middle of nowhere into a world-famous attraction."
$ jamesimage = "todddumb"
$ huxley4 = "The body was in a ditch."
$ gumtext = "Tutti-frutti."
$ kanetext = "Do I feel like making a mistake? Maybe."
$ filmtext = "This looks like one of the film rolls Murdoch's used before."
$ jartext = "One of these flowers is definitely mugwart."
$ dolltext = "A doll in the basement."
$ marcydolltext = "..."
$ samtoddtext = "Slick, fellahs..."
$ shroudtext = "Her grandma's shroud was in the bed... I have a pretty good idea of what we'd find if we opened it."
$ murdochtext = "It's probably nothing."
$ portraittext = "I need to get a good look at the portrait of James the First..."
$ manortext = "Is there anything James is hiding?"
$ investigorder = "first"
$ KaneChoice = False
$ SWNChoice = False

#Chapter 1 label - can skip directly

if (chapter_value == 1):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    pause 1.0
    scene powderroom with dissolve
    jump williamroute

#Chapter 2 label - can skip directly

if (chapter_value == 2):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    pause 1.0
    play background "sfx/crickets.ogg" fadein 3.0
    jump williamroute2

#Chapter 3 label:

menu:
    "When William confides in you his feelings about his wife arriving in echo, what did you tell him?"

    "Nothing. You reminded him of his heartbeat.":
        $ SW_Points +=1
    "You said that his duty to his family was noble.":
        $ SW_Points +=0
    "You told him he made a hard choice.":
        $ SW_Points +=1
    "You told him it's okay to be a little bit selfish.":
        $ SW_Points +=1



menu:
    "Did you reveal yourself to Harlan after Dora talks to him about the box?"

    "Yes":
        $ DD_Points +=1

    "No":
        menu:
            "Where did you hide?"

            "I crouched and waited for him to leave.":
                $ DD_Points +=1
            "I slipped into the office quickly.":
                $ DD_Points +=0



menu:
    "When William wondered what was wrong with his judgement in the mines, you:"

    "Assured him he's done nothing wrong.":
        $ SW_Points +=0
    "Said that people sometimes hallucinate.":
        $ SW_Points +=1
    "Joked about witches influencing him.":
        $ SW_Points +=1
    "Talked about gasses in the mines.":
        $ SW_Points +=1

if (chapter_value == 3):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    pause 1.0
    jump williamroute3

#End of last update label:

menu:
    "As William, did you get Sam off in the bedroom?"

    "Yes.":
        $ SW_Points +=1
    "No.":
        $ SW_Points +=0


$ unlocked_journal_pages += 7

menu:
    "Where did you go investigate first in the day?"

    "City Hall.":
        $ unlocked_journal_pages += 6
        $ CITYHALLDAY_Points +=1
        $ STAGNIGHT_Points +=1
        $ MININT_Points +=1
        $ stagnighttext = "Harlan gets into fights with James? He usually keeps things professional."
        $ willstag1interview2 = True

    "The Stag.":
        $ unlocked_journal_pages += 6
        $ STAGDAY_Points +=1
        $ CITYHALLNIGHT_Points +=1
        $ PORINT_Points +=1
        $ chnighttext = "Apparently, at least one person who works at the hip is leaking information to James."


$ huxley1 = "According to Reed, Huxley's gun was pawned. Sales records indicate Huxley repurchased it."
$ huxley3 = "Huxley was an alcoholic who needed more money for his drinking habit. I wonder where he was getting the cash?"
$ huxley2 = "Marcy may know what happened to the gun."
$ changtext = "{s}Could a CGCS employee placed a hit on Cliff, or was it somebody else?{/s} Seems like the CGCS employees loyal to the company don't even get along. Some favor James. Some favor Briggs."
$ jamestext = "Made James bleed. Was funny."
$ jamesimage = "wn8"
$ willchall1interview = True
$ willchall2interview = True
$ willstag1interview = True
$ willstag2interview2 = True
$ willstag3interview = True
$ unlocked_journal_pages += 2
$ cynthiatext = "Maybe Cynthia does too."



menu:
    "Who did you interview at the Hip?"

    "Dora.":
        $ DORINT_Points +=1

    "Harlan.":
        if  MININT_Points > 0:
            $ HARINT_Points += 1
            $ harlantext = "Harlan has a grudge against James and has regular access to most of Dora's information."

    "Ethel.":
        if  PORINT_Points > 0:
            $ ETHINT_Points +=1
            $ etheltext = "Ethel reacted to a hollow threat of exposure. She's probably the one leaking information to James."

    "Cynthia.":
        $ CYNINT_Points +=1

$ unlocked_journal_pages += 4
$ current_journal_page = 18

if (chapter_value == 4):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    pause 1.0
    window show
    jump updatemarcy

$ unlocked_journal_pages += 4
$ willmanorportrait1 = True
$ willmanorkitchen1 = True
$ willmanorlivingroom1 = True
$ willjamesfile = True
$ willjamesfolder = True
$ willjamestrash = True
$ portraittext = "The Hendricks house has hollow walls that the owners claim not to understand, entirely. The painting at the top of the stairs in the foyer has hinges."
$ manortext = "There is a vanity full of hand mirrors near the basement of the Hendricks mansion. The amount and variety of them is more than excessive."
$ unlocked_journal_pages += 4
$ current_journal_page = 26

if (chapter_value == 5):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    pause 1.0
    $ quick_menu = False
    $ quick_menu_will = True
    $ willnote = True
    window show
    scene bg hipwashroom
    show cyn serious a at centerleft
    show cli at right
    with dissolve
    jump williamroute3c

$ unlocked_journal_pages += 2
$ hledgertext = "Names. Addresses. Companions. I could probably track down half the city with all of this information."
$ hlettertext = "The mafia uses these pictures as intimidating messeages. Nobody wants to wake up to these in their mail. I imagine Chang Fulin didn't, whoever he is."
if ETHINT_Points ==1:
    $ unlocked_journal_pages += 1
    $ ethelclifftext = "We could hear him down the hallway. But at least I know now that Harlan asked for the wine delivery."

menu:
    "As William, when Sam asked why would you take a risk with Kane, what did you reply?"

    "He reminds me of you.":
        $ SW_Points +=0

    "It's about doing something more than sayin' it.":
        $ SW_Points +=1

    "He's not that risky.":
        $ SW_Points +=0

    "He reminds me of something still wild in me.":
        $ SW_Points +=1

if SW_Points>=3:
    menu:
        "As William, when Sam asked asked if you would loosen up and let Kane call the shots, what was your reply?"

        "Fat chance if you think I'd lift my tail.":
            $ KaneChoice = False

        "I'll be calling all the shots if anything happens.":
            $ KaneChoice = False

        "Maybe.":
            $ SW_Points +=1
            $ KaneChoice = True

        "If you can allow for things to go where they need to, then so can I.":
            $ SW_Points +=1
            $ KaneChoice = True

    menu:
        "As William, did you decide to make a mistake with Kane?"

        "Yes." if KaneChoice == True:
            $ KaneChoice = True

        "No.":
            $ KaneChoice = False
            if SW_Points>=4:
                menu:
                    "As William, did you decide to tell Nikolai the truth about how you feel?"

                    "Yes." if SW_Points >= 5:
                        $ SWNChoice=True

                    "No.":
                        $ SWNChoice=False

$ marcydolltext = "It used to belong to Marcy's sister."
$ current_journal_page = 21

if (chapter_value == 6):
    stop music fadeout 3.0
    stop music2 fadeout 3.0
    stop background fadeout 3.0
    stop sound
    pause 1.0
    window show
    if KaneChoice == True:
        scene bg hipwashroom
        show cyn seriouscrossed a at centerleft
        show wil nw at right
        with dissolve
    else:
        scene bg hipwashroom
        show cyn seriouscrossed a at centerleft
        show wil at right
        with dissolve
    jump williamroute3d
