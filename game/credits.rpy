#
# If you want to change the appearnce of the end credits to match a certain route
# Define "Credits" as that route number, and then add to the folder "credits" a folder with the same number
# In that folder name the images 1-5.webp
#

init python:

    style.cred2 = Style(style.button_text)
    style.cred2.clear()
    style.cred2.background = None
    style.cred2_text.color = "#F2C34E"
    style.cred2_text.size = 40
    style.cred2_text.xalign = 0.5
    style.cred2_text.yalign = 0.5
    style.cred2_text.font = "font/DMSerifDisplay-Regular.ttf"

    style.credits = Style(style.button_text)
    style.credits.clear()
    style.credits.background = None
    style.credits_text.color = "#FFF"
    style.credits_text.size = 30
    style.credits_text.xalign = 0.5
    style.credits_text.yalign = 0.5


transform LogoFade():
    alpha 0
    linear 5 alpha 1
    pause (2)
    linear 100 ypos -6800

transform ImageFade(Time):
    alpha 0
    pause (Time)
    linear 5 alpha 1
    pause (7)
    linear 3 alpha 0

transform ImageEnd(Time):
    alpha 0
    pause (Time)
    linear 3 alpha 1
    pause (35)
    linear 3 alpha 0

transform ImageEnd2(Time):
    alpha 0
    pause (Time)
    linear 3 alpha 1
    pause (27)
    linear 3 alpha 0

transform CreditsBorders():
    alpha 0
    linear 5 alpha 1
    pause (100)
    linear 5 alpha 0

screen credits():

    style_prefix "credits"

    hbox at ImageFade(15):
        xfill True
        image "images/credits/[Credits]/1.webp"

    hbox at ImageFade(30):
        xfill True
        image "images/credits/[Credits]/2.webp"

    hbox at ImageFade(45):
        xfill True
        image "images/credits/[Credits]/3.webp"

    hbox at ImageFade(60):
        xfill True
        image "images/credits/[Credits]/4.webp"

    hbox at ImageFade(75):
        xfill True
        image "images/credits/[Credits]/5.webp"

    hbox at ImageEnd(90):
        xfill True
        image "images/credits/Ralph.webp"

    hbox at ImageFade(0):
        xfill True
        xpos 460
        ypos 50
        image "images/credits/Logo.webp"

    hbox at CreditsBorders():
        xfill True
        image "images/credits/Border.webp"

    vbox at ImageFade(15):
        xpos 100
        xsize 850
        spacing 15
        yalign 0.5
        text "Project Lead" style "cred2_text"
        text "@GeorgeSquares"
        text ""
        text "Consultation" style "cred2_text"
        text "Howly"
        text ""
        text "Writing By" style "cred2_text"
        text "@GeorgeSquares"
        text "@reddtheshibe"

    vbox at ImageFade(30):
        xpos 1000
        xsize 850
        spacing 15
        yalign 0.5
        text "Story Editors" style "cred2_text"
        text "@cafealopex"
        text "@Kardamon"
        text "@ShtarFish"
        text "@GeorgeSquares"
        text "@reddtheshibe"
        text "@scruffie"
        text "@linsang"
        text "@spectacledlion"
        text ""
        text "Original Music" style "cred2_text"
        text "Ian Martyn"
        text "Anonymous"
        text "Darby Cupit"
        text ""
        text "Stock Music" style "cred2_text"
        text "Audioblocks"
    vbox at ImageFade(45):
        xpos 100
        xsize 850
        spacing 15
        yalign 0.5
        text "Coding" style "cred2_text"
        text "@CyFyKitty"
        text "@Kardamon"
        text "@GeorgeSquares"
        text "@reddtheshibe"
        text "@horrorbuns"
        text "Eden"
        text "Translation" style "cred2_text"
        text "@betoidk0"
        text ""
        text "UI & Graphic Design" style "cred2_text"
        text "Dylan Wunsch @compymono"
        text ""
        text "Art Direction" style "cred2_text"
        text "@ShtarFish"
        text "@Kardamon"
        text "@9KLIPSE"

    vbox at ImageFade(60):
        xpos 1000
        xsize 850
        spacing 30
        yalign 0.5
        text "Character Design & Sprite Artwork" style "cred2_text"
        text "@rlerofevrything"
        text "@Vulpro_Fox"
        text "@Werewhiskey"
        text "@tropicalsleet"
        text "@Iam0range3"
        text "@ShtarFish"
        text "@9KLIPSE"
        text "Eden"
        text "@staufdraws"
        text "@BigHufferPuffer"

    vbox at ImageFade(75):
        xpos 100
        xsize 750
        spacing 10
        yalign 0.5
        text "Background Artwork" style "cred2_text"
        text "@Kardamon"
        text "@9KLIPSE"
        text "@TELBATdraws"
        text "@badstranj"
        text ""
        text "Additional Artwork" style "cred2_text"
        text "@OtterboxedArts"
        text "@horrorbuns"
        text "@Soffbagel"
        text "@Yesntpan"
        text "@notoxen"

    vbox at ImageFade(90):
        xpos 1000
        xsize 850
        spacing 9
        yalign 0.5
        text "CG Artworks" style "cred2_text"
        text "@TELBATdraws"
        text "@ShtarFish"
        text "@SoloSoloSolomon"
        text "@Horrorbuns"
        text "@badstranj"
        text "@anino_x"
        text ""
        text "Special Thanks & Merch" style "cred2_text"
        text "@Soffbagel"
        text "@SeagullLarus"
        text "@seachordArt"
        text "@FruitzJam"
        text "Grufflol"
        text "@otterboxedarts"
        text "@venkpng"
        text "Recremen"
        text "@itreyu"
        text "Wesi"
        text "@badstranj"

    vbox at ImageEnd2(105):
        xpos 1000
        xsize 850
        spacing 15
        yalign 0.5
        text "Thank you for playing!"

    button:
        xsize 1920
        ysize 1080
        action [Stop("sound"), Return()]

    #timer sends to main menu a few seconds after the music finishes
    timer 142.0 action [Stop("sound"), Return()]
