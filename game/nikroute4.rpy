label nikroute4a:
#chapter page goes here
pause 1.5
"I feel Nik’s big paw grab onto my shoulder, shaking me."
scene bg minequarryevening
show nik shocked at center,sunsetlilac
with dis3
ni "\"We have to go.\""
hide nik with dis3
"I stare at Will just lying on the ground."
"The pool of blood around him stains the sand."
$ renpy.music.set_volume(0.1, delay=3.0, channel='ambient')
"I want to say {i}we can’t leave him{/i}."
"I want to say {i}but he’s still right there{/i}."
"But I stumble backward."
"The walls of the quarry feel taller and tighter."
"That all I can do for the rest of my life is run until I can’t run anymore."
play sound ("sfx/gunleft.ogg")
"The sounds of gunshots go off to my left."
"A row of people climbing out the side of the quarry tumbles to the ground, some silent, some twitching while they bleed."
stop sound
"The Guard surrounds the ground of the quarry from every side."
play sound ("sfx/multishot.ogg")
play sound2 ("sfx/ricochet.ogg")
"I hear the gunshots again, and pellets whiz through the air to the side of me and from behind me."
"Somebody trying to run gets their head popped like a balloon full of red jelly."
stop sound
stop sound2
"That old fear in me is back."
"The fear that I’m doomed."
"That the rest of my life is just me running."
"Running until I run out of energy."
show nik shocked at center,sunsetlilac with dis3
ni "\"Wake up Sam!\""
ni "\"We have to go into the mine!\""
show nik surprised with dis3
"I shake my head."
m "\"...Fuck that goddamn pit.\""
ni "\"It’s the only way we are getting out!\""
play sound ("sfx/chittering.ogg") volume 0.3
hide nik with dis3
"I hear the wind from the tunnel."
"Like it's opening its jaws for me."
"One last time."
stop sound
"I want to tell Nik that if we go in the cave, we’re not coming back out."
"But there’s nowhere left to go."

play background ("sfx/battle.ogg") fadein 5.0
"Shots fire again."
"This time from behind me, too."
stop sound
"Another wave of men in front of me fall."
"Why God, why is there nowhere left to go?"
"As much as I want to see, I don’t check to see if any of the guards in front of me fall."
"I have to run as fast as I can, past the first turn of the rocks where the bullets can’t hit me."
stop music fadeout 20.0
scene bg quarrybarricadeevening with dis3

"We see a wall of crates stacked up where we hadn’t seen them before."
"I recognize the snout of gun barrels poking through holes."
show nik surprised at right,sunsetlilac with dis3
m "\"Oh, God, we’re already dead.\""
ni "\"Those are our side, Sam!\""
"I don’t particularly think anybody is on our side right now."
"They don’t shoot, but I don’t want to give them a chance to change their minds."
hide nik with dis3
"We turn another corner of rocks before we hear another round of shooting."
play ambient ("sfx/malecrowd.ogg") fadein 6.5
"Then the angry buzz of voices drowns out everything else."

scene bg mineentranceevening with dis3
"In front of us, there’s a crowd of men shouting, flailing, bottlenecked at the entrance to the thin shaft leading into the bigger room."
"As we close the gap of the people in front of us, more bodies slam into us from behind, pushing us forward, shouting for us to go in."
show nik disappointed at right,sunsetlilac with dis3
m "\"They’re not moving fast enough, Nik.\""
ni "\"The gunmen at the front will buy us enough time.\""
show nik neutral with dis3
m "\"And then what?\""
show nik talking with dis
ni "\"Then we find Yao.\""
show nik -talking with dis1
show nik talking with dis
ni "\"He’ll have a plan.\""
show nik -talking with dis
m "\"You sound so fucking sure about that.\""
show nik talking with dis
ni "\"Because I am sure of it, Sam!\""
show nik -talking with dis
m "\"Will was sure about everything too, now {i}wasn’t he?{/i}\""
show nik sidelook with dis3
"Nik doesn’t respond."
m "\"I said, wasn’t he?\""
show nik surprised with dis1
hide nik
play sound ("sfx/thud6.ogg")
"Something barrels into me and it's hard to breathe." with vpunch
"Everything goes sideways for a moment."
stop sound
scene bg black with dis
"Then I see black."
scene bg mineentranceevening
show nik angry at right,sunsetlilac
with dis4
"But it’s just for a moment."
$ renpy.music.set_volume(1.0, delay=0.0, channel='music')
"Nik is pushing the crowd of men off of me, throwing punches as they elbow him, trying to push their way forward."
"So is this where we die?"
"No."
"The crowd is moving forward."
$ renpy.music.set_volume(0.3, delay=1.0, channel='background')
stop ambient fadeout 1.5
play background ("sfx/battlemine.ogg") fadeout 1.0 fadein 1.0
scene bg black with dissolve
scene bg mineforeman with dis3
play music ("sfx/whispers.ogg") fadein 3.0
"We’re free of the tight passage finally and we break into the open domed room."
"Apart from the fleeing protestors, the mines are completely empty today."
"There’s nobody pushing carts or huddling around the elevator."
"They must have been told to go home."
"As if they knew something was going to happen."
"Men run past us, shouting in various languages, stumbling over each other."
"There’s an overflow of bodies crawling over one another, like ants pouring out of a hole."
"One of them falls in front of the crowd, screaming until his voice suddenly goes silent."
"Most everybody has such a wild look in their eyes that they only seem to be looking forward, running as far away from the sounds of the shots as possible."
scene bg mineforemanshadow with dis3
"But out of the corner of my eye I see a lizard’s tail slip left, then disappear into the foreman’s post before the door slips shut."
show nik surprised at right,dark2 with dis3
"I pull Nik’s wrist toward that direction."

ni "\"Why there?!\""
$ renpy.music.set_volume(0.3, delay=3.0, channel='ambient')
m "\"Beckett’s in there.\""
show nik neutral with dis
"Nik’s brow furrows, his eyes narrow, and he nods."
scene bg mineforemandoor with dissolve
show nik neutral at right,dark2 with dis3
play sound ("sfx/mineladder.ogg")
"We climb up the wooden scaffold to the door."

"There’s a shadow there behind the scuffed door."
"I can’t see him entirely, but I know he’s looking straight at us through the tinted glass."
stop sound
"I open the mail slot with my claw and slip down to my knees."
show nik sidelook with dis3
m "\"Help us! Please!\""
play sound ("sfx/rummage1.ogg")

"I hear a ruckus coming from inside the room."
"Drawers are opening. Boxes are shuffled."
stop sound

m "\They’re killing everybody!\""
show nik surprised with dis3
play sound ("sfx/holster1.ogg")
"I try to look through the slat to get a better look-see at what he’s doing, and I’m met with cold metal to my forehead."

bk "\"You don’t back away from this door?\""
stop sound
bk "\"You’re joining ‘em.\""
"He pauses for a moment."
bk "\"Shit.\""
bk "\"You’re the two who were hovering around that damn tiger.\""
"Nik raises his voice to a yell."
ni "\"Why are you talking about a tiger?!\""
bk "\"Well he’s part of the reason the Guard is here, ain’t he?\""
bk "\"He was stashing dangerous weapons in the mine.\""
"The both of us tense up."
ni "\"...You caught him doing this?\""
bk "\"Not me specifically, but the leadership was notified.\""
bk "\"Pretty recently, in fact.\""
bk "\"Everybody knows about it now.\""

if SOLDB_Points==1:
    "But how could they have known?"
    "He was so careful."
    m "\"That has to be a mistake.\""
    bk "\"No mistake.\""
    bk "\"Ben was able to show us the evidence after being confronted.\""
    show nik sad with dis3
    "Nik’s ears splay back."
    ni "\"Confronted?\""
    bk "\"An anonymous tip tried to accuse him of something similar.\""
    bk "\"He had a good nose for rootin’ out the truth of things.\""
    bk "\"Though he’s missing now.\""
    bk "\"Probably dead, God rest his soul.\""
    "Even after he’s gone, that man’s causin’ us grief."
    m "\"God ain’t got nothin’ to do with him, I reckon.\""
    show nik surprised with dis3
    "He nudges me with the gun."
    bk "\"Whatever his crimes, it weren’t stashin’ weapons.\""
    bk "\"Can’t say the same about your friend.\""
    #

if SOLDY_Points==1:
    m "\"What’s that suppose to mean?\""
    bk "\"Means he got caught in the act.\""
    bk "\"Never would have thought to look if it weren’t for an anonymous tip we got at the office.\""
    bk "\"What doesn’t make sense is that he was always a good worker.\""
    bk "\"Strong. Resourceful. Compliant.\""
    bk "\"But after everything, I guess we just got to see his true colors.\""
    m "\"If he’s under arrest, then why’s the Guard runnin’ everybody down?\""
    bk "\"Who said he’s under arrest?\""
    bk "\"You think I’d be hiding here if I knew whether the violent insurrectionist down here was caught or not yet?\""
    bk "\"Shit, what kind of operation do you think I help manage down here?\""
    bk "\"We’re exporting minerals, not raising a militia!\""
    #


"I’ve got to ask him more."
"There’s a chance he might tell us more."
"Or at least let us hide."
"I have to say something."
"Anything!"

#comp
if BKWALLET_Points==2 and PD_Points==0:
    "I lick my lips, and I start to talk real slow-like."
    m "\"...what did you see the last time we talked?\""
    bk "\"...what?\""
    m "\"In the office.\""
    show nik disappointed with dis3
    ni "\"Sam, he isn’t going to—\""
    show nik surprised
    play sound ("sfx/knock.ogg")
    "I bang on the door with my fist." with vpunch
    stop sound
    m "\"If you ain’t gonna help us, at least let me know.\""
    m "\"I just need to know what you saw!\""
    "The barrel of the gun pulls out of the slat."
    bk "\"Five minutes.\""
    bk "\"Deal’s off the moment you give me any trouble.\""
    play sound ("sfx/keyopen.ogg")
    "We hear the lock shift as the door opens."
    stop sound
    $ renpy.music.set_volume(0.0, delay=1.0, channel='background')
    scene bg mineforemanoffice
    show bec grumpy squint at halfright,staglight
    with dis3
    "He’s still aiming the gun at us."
    show bec angry talking with dis
    bk "\"You shout to get anybody’s attention, I shoot you.\""
    show bec grumpy squint with dis
    "It’s a very steady aim."
    show bec angry talking with dis
    bk "\"You come at me suddenly, I shoot you.\""
    show bec angry with dis1
    show bec angry talking with dis
    bk "\"Hands up and close the door behind you.\""
    show bec angry
    #adjust
    play sound ("sfx/doorcreakopen.ogg")
    show nik sidelook at staglight:
        xpos -0.1
        xzoom-1
        yalign 1.0
    with dis3
    "We walk through and Nikolai gets the door..."
    stop sound
    show bec angry talking with dis
    bk "\"I want y’all to understand one thing.\""
    show bec angry with dis1
    show bec angry talking with dis3
    show nik neutral with dis3
    bk "\"The albino did me a favor, so I’ll do him one in turn.\""
    show bec angry with dis1
    show bec angry talking with dis
    bk "\"After that, we’re even.\""
    show bec angry with dis1
    show bec angry talking with dis
    bk "\"We’re nothing to one another.\""
    show bec angry with dis1
    show bec angry talking with dis
    bk "\"Y’hear?\""
    show bec angry with dis
    "I nod slowly."
    "Surely."
    show nik disappointed with dis3
    "Nikolai shakes his head."
    ni "\"What exactly {i}did{/i} Sam do for you?\""
    show nik neutral with dis3
    show bec angry talking with dis3
    bk "\"Brought me back my wallet.\""
    show bec angry with dis1
    show bec angry talking with dis
    bk "\"Made me think about my cousin.\""
    show bec angry with dis1
    show bec angry talking with dis
    bk "\"Though sometimes I wish he didn’t.\""
    show bec angry with dis
    "Nik is staring at the gun, but I see the direction of his gaze flick to the corners of the room."
    ni @ talking "\"Why do you wish he didn’t?\""
    "The lizard shakes his head."
    show bec angry talking with dis
    bk "\"I really.\""
    show bec angry with dis1
    show bec angry talking with dis
    bk "\"Wish.\""
    show bec angry with dis1
    show bec angry talking with dis
    bk "\"He didn’t.\""
    show bec grumpy squint with dis
    play sound ("sfx/gunload.ogg")
    "He aims the gun at Nik."
    show bec angry talking with dis
    bk "\"You’re looming too close.\""
    stop sound
    show bec angry with dis1
    show bec angry talking with dis
    bk "\"Big man.\""
    show bec angry with dis
    show bec grumpy squint with dis
    show nik sidelook with dis3
    "Nik’s hands curl up into a ball."
    show nik sidelook at staglight with dis3:
        xpos-0.15
        yalign 1.0
    "He backs up."
    m "\"Just... tell me what you saw.\""
    "Beckett still stares at Nik, as if trying to decide to shoot or not."
    show bec with dis3
    show nik neutral with dis3
    "Then he rolls his head on his neck, relaxing his muscles."
    show bec with dis1
    show bec talking with dis
    bk "\"It was less than a second, but I know what I saw.\""
    show bec with dis
    "He shakes his head, aim still steady."
    show bec talking with dis
    bk "\"Ain’t you, or the bosses, or any ordained men of God gonna deny me what I saw.\""
    show bec angry with dis
    m "\"What was it, then?\""
    "He changes his aim to me."
    m "\"Please.\""
    m "\"I just really want to know.\""
    show bec angry talking with dis
    bk "\"Only one reason I can think of where a man will stare down the barrel of a gun just to hear an answer.\""
    show bec with dis1
    show bec talking with dis
    bk "\"You’ve been seeing things too, ain'tcha?\""
    show bec with dis1
    show bec talking with dis
    bk "\"The kinds of things you see that make it so you don’t care if you die now or later.\""
    show bec with dis1
    show bec talking with dis
    bk "\"Things that show you there’s something else.\""
    show bec with dis1
    show bec talking with dis
    bk "\"Yeah?\""
    show bec angry with dis
    "I nod my head, too scared to slow my heart, too scared to think about much of anything else than what he’s talkin’ about."
    m "\"We just saw our best friend die.\""
    m "\"I gotta know if he’s somewhere else or not.\""
    m "\"’Cause it’s my fault he was there at all.\""
    "Beckett flicks his forked tongue past his lips."
    show bec angry talking with dis
    bk "\"That’s too bad.\""
    show bec angry with dis
    "I can’t tell if he’s sorry or not."
    "Either he doesn’t care, or he’s numb to hearing about this sort of thing."
    "He flicks it again before letting that hang in the air."
    show bec talking with dis
    bk "\"People tell you all the time what ghosts look like.\""
    show bec with dis1
    show bec talking with dis
    bk "\"They say {i}see-through people with their burial shrouds still over their heads{/i}.\""
    show bec with dis1
    show bec talking with dis
    bk "\"Or {i}phantoms that slip into the corner of your house{/i}.\""
    show bec with dis1
    show bec talking with dis
    bk "\"Sometimes they’ll talk about the chains of hell, like in that Dickens Christmas story.\""
    show bec angry with dis1
    show bec angry talking with dis
    bk "\"But not a damn one has ever told me...\""
    show bec with dis1
    show bec talking with dis
    bk "\"Tall.\""
    show bec angry with dis1
    show bec angry talking with dis
    bk "\"Blue.\""
    show bec angry with dis1
    show bec angry talking with dis
    bk "\"Disgusting.\""
    show bec angry with dis1
    show bec angry talking with dis
    bk "\"With the most intense hatred in its sticky red eyes that pierced through the dark.\""
    show bec angry with dis1
    show bec angry talking with dis
    bk "\"Hating me with all its being, just because I was what it was not.\""
    show bec angry with dis1
    show bec angry talking with dis
    bk "\"Alive.\""
    show bec angry with dis
    "His hands shake for just a moment."
    "Then he takes a deep breath and steadies them again."
    show bec angry talking with dis
    bk "\"When I screamed I thought I saw the ghost of my cousin wearing your face Mr. Ayers.\""
    show bec angry with dis1
    show bec angry talking with dis
    bk "\"But if that was him, if it was ever him, and not just somethin’ trying to scare me, then it ain’t him anymore.\""
    show bec angry with dis1
    show bec angry talking with dis
    bk "\"A part of me was hoping it would show itself again.\""
    show bec angry with dis1
    show bec angry talking with dis
    bk "\"Just so I could ask it somethin’.\""
    show bec angry with dis1
    show bec angry talking with dis
    bk "\"Just so I could make {i}completely{/i} sure.\""
    show bec with dis
    "He looks at me, as if he’s waiting."
    show bec with dis1
    show bec talking with dis
    bk "\"But looks like that’s not happening.\""
    show bec with dis1
    show bec talking with dis
    bk "\"Should have showed itself by now if it were really here.\""
    show bec grumpy sideeye with dis
    "He looks to the window."
    show bec angry sideeye talking with dis
    bk "\"But then again, there was a mirror in the office though wasn’t the–-\""
    show bec surprised talking
    #check
    show nik angry at halfleft,transparent
    play sound ("sfx/punch1.ogg")
    "Nik’s paw makes contact with Beckett’s face." with hpunch
    hide bec
    play sound ("sfx/thud3.ogg")
    "He drops to the ground, slumping into the chair." with vpunch
    show nik eyes with dis3
    m "\"What are you doing?!\""
    show nik disappointed with dis3
    "Nik takes the gun and puts it behind his back."
    ni "\"We need this more than he does.\""
    #sfx?
    show nik neutral with dis3
    "I put my hand to his face and bat it, trying to slap him awake."
    m "\"Is he dead?!\""
    show nik sidelook with dis3
    ni "\"No.\""
    $ renpy.music.set_volume(0.5, delay=2.0, channel='background')
    scene bg mineforemanshadow with dissolve
    show nik eyes at left,dark2 with dis3:
        xzoom-1
    "He drags me from the shack before I can see if he’s breathing or not."
    #sfx
    "We hear more bullets inside of the mines."
    show nik neutral with dis
    m "\"Why don’t we stay here and hide?\""
    show nik sidelook with dis3
    ni "\"Because if we do, they will find us.\""
    ni "\"And then they will execute us.\""
    m "\"...At least give me some more time to make sure he’s breathing.\""
    show nik disappointed with dis3
    "He keeps dragging me forward."
    ni "\"As long as I draw breath, Sam, I will not let you die, too.\""
    hide nik with dis3
    "I know he’s smart to leave him."
    "For knocking him cold."
    "And for stealing the gun."
    "It sounded like he didn’t know a damn thing anyway."
    "And as soon as the Guard finds him, they’ll help him."
    "We’re the ones they’re hunting."
    "If you could even call it a hunt."
    "To them it’s probably more like culling the livestock."
    "Just because some of us bleated too loud."
    "Now they’re comin’ for all of us."
    "We ain’t nothin’ more than meat to them."
    #

else:
    m "\"Please!\""
    m "\"If we can just hide—\""
    bk "\"You think they won’t look here?\""
    "He turns his head and sees Nik."
    bk "\"Oh hell no.\""
    bk "\"They’re {i}especially{/i} looking for him.\""
    play sound ("sfx/gunload.ogg")
    "We hear the gun load."
    bk "\"I’m sorry but I can’t help you.\""
    stop sound
    bk "\"Ain’t gonna hurt you neither, unless you make me.\""
    bk "\"’Cause if I do, it’ll be your own damn fault.\""
    bk "\"You have the count of ten or I will shoot.\""
    m "\"It’s not our fault!\""
    bk "\"One...\""
    m "\"Nik ain’t have anything to do with whatever started the gunfire!\""
    bk "\"Two...\""
    m "\"Please!\""
    bk "\"THREE!\""
    show nik angry with dis3
    play sound ("sfx/creak1.ogg")
    "Nikolai picks me up."
    stop sound
    "He grunts, lifting me with his arms while I struggle, squirming my way out of his grasp."
    scene bg black with dis3
    "I don’t hear Beckett’s voice anymore."
    scene bg mineforemanshadow with dis3
    show nik disappointed at right,dark2 with dis3
    "We’re off of the scaffold and Nikolai is breathing heavily."
    show nik sidelook with dis3
    "I twist my arms out of the lock he has on me and try to go back to the cabin."
    show nik surprised with dis3
    "But he grabs me again."
    m "\"Let me just try and reason with him one more time!\""
    ni "\"You did try.\""
    show nik disappointed with dis3
    ni "\"There is no more time!\""
    hide nik with dis3
    $ renpy.music.set_volume(0.5, delay=5.0, channel='background')
    "Bitterly, I turn away from the shack, walking in stride with Nik as he takes me deeper into the twists and turns of the dark tunnels."
    "I want to argue, but the gunshots get louder."
    "I think I can hear them tearing the boxes stationed near the front to shreds as wet groans cry into the air."
    "We don’t talk for a while after that."
    #

scene bg minetunnel with dis3
$ renpy.music.set_volume(0.5, delay=5.0, channel='background')
"Nikolai picks up his pace, and so do I to keep up with his stride."
show nik sidelook at right,dark2 with dis3
"The longer we walk, the closer the gunshots sound."
m "\"They wouldn’t fire this far inside of the cave would they?\""
"Nik doesn’t look at me."
"He’s walking at a pace where he’s panting for breath now."
ni "\"Don’t know.\""
m "\"They could cause a cave-in!\""
show nik disappointed with dis3
ni "\"They do not care, Sam.\""
stop background fadeout 4.5
scene bg minenook with dissolve
show nik disappointed at right,dark2 with dis3
m "\"But that would trap them too, wouldn’t it?\""
show nik sidelook with dis3
ni "\"Something tells me Briggs wouldn’t care if that happened to them, either.\""
play music ("music/contemplation.ogg") fadeout 1.5 fadein 2.0
show nik surprised with dis3
"???" "\"Who’s there?\""
"We stop in our tracks."
"A man’s voice calls out."
"???" "\"Identify yourself. Now!\""
"I’m trying to figure out where the voice is coming from."
"Behind us there’s just a long curve of tunnel."
show nik neutral with dis3
"In front of us there’s a junction of the tunnel going four ways."
"I open my mouth to answer that we’re just lost, but Nikolai holds his paw over my mouth."
"He points his claw at the silhouette of a gun tip, dangling in front of the passageway, obscuring the rest of its owner."
"???" "\"I know which direction you spoke from.\""
"My heart starts banging in my chest."
"They caught us."
"We’re caught."
"???" "\"You should come out.\""
"???" "\"There’s four of us here.\""
show nik eyes with dis
"I look at Nik, asking with my expression if we should answer, but he shakes his head."
show nik neutral with dis
"???" "\"Shooting me won’t save you.\""
"???" "\"Drop your weapons and face us!\""
show nik sidelook with dis3
"We don’t move."
"We don’t breathe."
"We don’t say a goddamn thing."
"???" "\"That’s the only course of action to take if you wish to leave these mines alive, civilian.\""
"I don’t believe them."
"Nik doesn’t believe them either."
show nik eyestalking with dis3
ni "\"It sounds like there’s only one of you.\""
if BKWALLET_Points==2 and PD_Points==0:
    show nik neutral with dis
    play sound ("sfx/holster2.ogg")
    "He raises the gun without hesitation."
    stop sound
    "I’ve never seen Nik use a gun before."
    "It’s probably because he’s never had to, for as long as I’ve known him."
    "But it’s clear to me that he knows how to hold it."
else:
    show nik angry with dis3
    "Nikolai crouches and places his paw on a rock."
    "I've never seen him sit so still."
"???" "\"Sounds like you want to make a wager.\""
"???" "\"I’ll take it.\""
show nik surprised with dis3

play sound ("sfx/minerun2.ogg")
"Several officers turn into the tunnel."
stop music fadeout 2.0
play sound2 ("sfx/doubleshot mine.ogg")
scene bg black with dis
"Then I hear a series of shots."
stop sound
stop sound2
"We guessed wrong."
"I begin to wonder when I’ll feel the bullets tear holes through my body."
"Whether it will hurt, or sting, or catch me in a spot where I feel nothing at all."
"But the pain doesn’t come."
"I still hear Nikolai breathing."
scene bg minenook
show nik surprised at right,dark2
with dis3
"Two bodies are lying on the floor."
show nik eyes with dis
"Just two."
show nik neutral with dis
"The sharp smells of iron and smoke mix with the rancid smell of guts, making my eyes water."
play music ("music/mines.ogg") fadein 2.0
paunk "\"They were bluffin’.\""
"I know that voice."
show nik happy with dis3
"Nikolai starts laughing."
"Then so do I."
show nik -happy smile with dis3
"Hearing Paul’s voice tends to mean that some sort of fight is about to break out."
"For the first time, I’m grateful for somebody who isn’t afraid to get his hands dirty."
$ renpy.music.set_volume(0.6, delay=5.0, channel='music')
"{i}William is dead.{/i}"
"{i}You’re still trapped in the mines.{/i}"
"I can’t think about that now."
"If I think about it, I’ll give up."
"Giving up means death."
$ renpy.music.set_volume(1.0, delay=5.0, channel='music')
"I have to keep going."
show pau at halfleft,dark2 with dissolve:
    xzoom-1
show pau talking with dis
pa "\"Y’all alright?\""
show pau with dis
m "\"As much as we can be, but...\""
show nik eyestalking with dis
ni "\"Yeah.\""
show nik disappointed with dis3
"Nik is panting harder now, his breath sounding more like grunts with each passing breath."
show nik neutral with dis3
feunk "\"We need to go.\""
feunk "\"I don’t know if Yao will wait for us if we’re not at the rendezvous soon.\""
"I hear Felipe’s voice too."
"Finding them makes me feel safer."
"The more of us who find one another, the better our chances."
"I tell myself that this has to be the truth."
no3 "\"Because a gun runs out of bullets when there are too many bodies.\""
show pau angry talking with dis
pa "\"Yao wouldn’t abandon us after all this.\""
show pau with dis1
show pau talking with dis
pa "\"Let’s move.\""
show pau with dis1
scene bg black with dissolve
scene bg minemaze with dis3
play music ("sfx/whispers.ogg") fadeout 3.0 fadein 3.5
"I try to ignore the voice I just heard."
"The voices had stopped."
"But this one didn’t sound as much like me."
"How this sounded was hard to describe."
"Like the sound you’d think a pumpkin would make after it rotted in the sun."
"A withered, sickly sound."
"I tell myself that I know everything down here is dangerous."
"But that doesn’t necessarily mean it can kill you."
"So I decide to ignore it."
"Just for now."
scene bg cavebeam1 with dis3
"We walk along passageway after passageway, feeling the walls."
"I loosen up with a stretch and a silent sigh now that the sounds of the guns are a distant way away now."
"Nobody speaks as we keep a steady gait between stretches of darkness broken occasionally by the beams of light breaking through the ceiling."
show fel mask at left,dark2:
    xzoom-1
show pau at centerleft,dark2:
    xzoom-1
show nik sidelook at right,dark2
with dis3
"Not until Nik breaks the silence."
ni "\"Have you seen any others?\""
"I can barely make out Paul and Felipe exchanging glances silently. Then the wolverine clears his throat."
show pau talking with dis
pa "\"More than a few.\""
show pau eyes with dis1
show pau eyes talking with dis
pa "\"Speaking optimistically, I think they only took out about a third of us with the guns.\""
show pau
show nik sad
with dis3
"Nik doesn’t answer right away."
"His voice is gruff when he does."
ni "\"That is hundreds of people.\""
"Our boots crunch into the sand as we march forward."
show pau angry talking with dis
pa "\"Which means we’ll have a national case on our hands if hundreds more get out and take it to the court.\""
show pau angry with dis
"His voice raises, and his temper creeps in."
show pau angry talking with dis
pa "\"They can’t do this to this many people!\""
show pau angry with dis1
show pau angry talking with dis
pa "\"They want a clean nose!\""
show pau angry with dis1
show pau angry talking with dis3
show fel mask angry with dis3
show nik neutral with dis3
pa "\"Especially when it comes to the lives and deaths of red-blooded Columbians!\""
show pau angry with dis
"I can make out Nik and Felipe getting tense when he says that."
show pau angry talking with dis
pa "\"Believe me when I say we’re on the right side of history here.\""
show pau angry with dis
"I decide to speak up."
"My words sputter out."
show pau with dis
show fel mask with dis
m "\"Especially if there’s somebody like Dimitri to speak up about it.\""
"I’m aware they sound too high."
"Too desperate."
m "\"He can certainly motivate a crowd.\""
"Paul and Felipe don’t respond."
play sound ("sfx/minewalk.ogg")
"The sounds of our boots crunching fill the silence again."
show nik eyestalking with dis
ni "\"Did he make it?\""
show nik neutral with dis
stop sound
"When Nik is blunt he’s hard to ignore."
show pau talking with dis
show fel mask eyes with dis
pa "\"He said his leg would slow us down.\""
show pau with dis1
show pau talking with dis
show fel mask with dis
pa "\"So he volunteered to fire at the door.\""
show pau with dis1
show pau talking with dis3
show nik sidelook with dis3
pa "\"We haven’t seen him yet.\""
show pau with dis
"I like that Paul says yet, because he’s not saying what all of us dread."
"He speaks like we are going to see him again."
"But the despair washes up in me, just as fresh."
"I want to ask {i}why didn’t you stop him{/i}? Or {i}why didn’t you carry him with you{/i}?"
no3 "\"He would make for an excellent shield.\""
"But he answers before I can ask."
show pau eyes talking with dis
pa "\"He punched me so hard in the face that I bled.\""
show pau with dis1
#adjust
scene bg cavebeam1 with dis3
"At this point I can’t tell if I am crying or not."
"Lately I’ve cried so much that I can’t help but be numb to it."
"I’m grateful that I ain’t feelin’ anything yet."
"‘Cause if I felt anything at all, it would be too much."
"And then I would have to stop."
"And none of us can afford to stop."
"Nik and I know that there is something wrong within these mines."
"But as terrified as I am with whatever waits for me down here..."
if SNY_Points >0:
    "The thing that took my trust."
else:
    "The thing that took my eye."
"That took my joy."
"That put me on this path of misery and hate..."
"It seems to work within a set of rules and habits that I don't quite understand."
"With certainty, I can understand the finality of a gunshot, now."
"So if there is something worse that waits for me after death, the worst thing that can happen to me now is getting shot."
"But the ease of mind that comes with seeing familiar faces after something horrible is starting to slip away."
"We’re all still in danger."
show fel mask at left,dark2:
    xzoom-1
show pau at centerleft,dark2:
    xzoom-1
show nik neutral at right,dark2
with dis3
"I speak up again."
show pau surprised with dis
m "\"Did Yao tell you to go this way in person?\""
show pau eyes with dis
"The wolverine{nw}"
show pau with dis
extend " blinks, as if I had just asked him if he personally knew Babe the Blue Ox."
show pau talking with dis
pa "\"I’m not gonna be cute with any answers. But yes.\""
show pau angry with dis
m "\"You’re sure?\""
m "\"In person?\""
show fel mask angry with dis
"The group all looks at me now the way Paul did the first time."
"They seem irritated with the repetition of my question."
"Nik adds weight to my question."
ni @talking "\"He told you where the rendezvous would be then?\""
show pau with dis
"Paul clears his throat."
show pau talking with dis
pa "\"To answer your question...\""
show pau with dis1
show pau talking with dis
pa "\"Using his communication network, he passed me a letter with his seal.\""
show pau with dis1
show pau talking with dis
pa "\"The only way the message could be compromised is if he were compromised himself.\""
show pau with dis

if SNY_Points >0:
    m "\"He showed us where he hid his weapons before.\""
    "In that place. Below. Which led to the Hendricks’ manor."
    show nik talking with dis
    ni "\"That doesn’t mean it was the only location.\""
    show nik eyes -talking with dis1
    show nik talking with dis
    ni "\"Or even a permanent one.\""
    show nik disappointed with dis3
    ni "\"I understand that he made backups with his plans.\""
    #

else:
    show nik sidelook with dis3
    m "\"Would he really need to keep his weapons just in one place?\""
    #
show pau angry talking with dis
pa "\"If you want to think that way, then you’re just admitting that you think we’re much worse off than we’re tellin’ ya.\""
show pau angry with dis
"There’s a low growl in his voice now."
show pau angry talking with dis
pa "\"I like to think that’s quitter talk.\""
show pau angry with dis1
show pau angry talking with dis
pa "\"And quittin’ in these circumstances just means laying your head down to die, don’t it?\""
show pau angry with dis3
show nik neutral with dis3
"The uneasy feeling in my body just keeps building."
m "\"But why {i}this way{/i}?\""
m "\"These weren’t the exits we had taken before.\""
show nik sidelook with dis3
ni "\"You’re still not convinced?\""
m "\"I just think I recognize where we’re going is all.\""
m "\"Nik wrote on his map that there were vapors close by.\""
show nik talking with dis3
ni "\"Yao had many secrets.\""
show nik -talking with dis1
show nik talking with dis
ni "\"It would not be out of character to put down misleading information if his plans were to fall in the wrong hands.\""
show nik -talking with dis
if SNY_Points ==0:
    m "\"Ain’t that just an excuse?\""
    show nik disappointed with dis3
    ni "\"We have to put faith in his results, Sam.\""
    #
else:
    "I drop the subject."
    "There’s no point in talking about it if we’re all going this way anyhow."
    #

scene bg mineoverhang with dis3
"As we pass through another beam of light, I notice something I hadn’t before."
#adjust
show nik neutral blood at halfright,dark3 with dis3
"There are specks of blood on Nik’s shirt."
"He’s been coughing."
"Coughing hard."
"I lean in to whisper into his ear."
m "\"You’re bleeding?\""
show nik sidelook with dis3
"He hushes me, looking forward."
show nik neutral with dis3
"Paul and Felipe haven’t noticed yet."
show nik eyestalking with dis
ni "\"They don’t need to know.\""
show nik neutral with dis
m "\"But it’s all over your chest.\""
show nik sidelook with dis3
ni "\"We can say it’s somebody else’s blood.\""
show nik disappointed with dis3
ni "\"I am just overexerting myself a bit.\""
"That doesn’t look like a bit."
show nik talking with dis3
ni "\"Hey.\""
show nik neutral with dis
"He takes a very sharp and serious tone with me."
show nik talking with dis
ni "\"No fretting.\""
show nik neutral with dis1
show nik talking with dis
ni "\"Worry about cave monsters and bullets.\""
show nik sidelook with dis3
ni "\"Not what I cough up on a napkin.\""
show nik neutral with dis3
m "\"Your shirt ain’t a napkin.\""
show nik talking with dis
ni "\"I am fine, Samuel.\""
show nik neutral with dis
"He seems to believe so."
"But I don’t think he’s right."
"We had people at the Hip cough blood from time to time and Dora always took it seriously."
hide nik with dis3
play ambient ("sfx/malecrowd.ogg") fadein 10.5
"The longer we walk, the more voices we hear ahead."
"The only thing that keeps me from panicking is that I hear more than just Albion being spoken."
scene bg cavecrate1 with dis3
"We come out to a domed cavern with better natural lighting."
"Paul was right."
"There are more miners here than I thought there would be — hundreds who have escaped the Guard."
"All gathered in this place."
"Rays of light pierce through the rocks in the sky far above."
"Craggy sandstone stacked in wedges makes them look possible to climb."
"The idea of an exit existing here somewhere begins to feel more likely."
"But if it’s here, I still can’t identify it."
"And I don’t see Yao either."
"But what everybody does see is a tall crate in the middle of the room with a white sheet over it."
show pau at left,dark2:
    xzoom-1
show nik neutral blood at right,dark2
with dis3
"Nik tilts his head a bit."
ni "\"Are those supposed to be the weapons?\""
show pau talking with dis
pa "\"This is where he said they would be.\""
show pau with dis1
show pau talking with dis
pa "\"We followed his marks on the wall.\""
show pau with dis
m "\"But... a big crate?\""
m "\"Just sitting out there in the open?\""
show nik disappointed with dis3
"Nik shakes his head."
ni "\"No.\""
ni "\"This feels too conspicuous for Yao.\""
show pau angry with dis
"Paul frowns."
"Either he doesn’t agree, or he doesn’t want to admit that he thinks somethin’ isn’t right."
hide pau
hide nik
with dis3
"People crowd around the box."
"Some mention that they have waited long enough."
"Some ask for the appearance of Feng Yaolin."
show fel mask at left,dark2:
    xzoom-1
with dis3
play sound ("sfx/oneknock.ogg")
"But it’s Felipe who kneels by the crate and knocks on it."
stop sound
show pau at right,dark2 with dis3
"He turns his head and gives the wolverine a skeptical look."
show fel mask angry with dis
fe "\"Yao’s not here, man.\""
show pau talking with dis
pa "\"I ain’t blind Felipe.\""
show pau with dis
fe "\"He didn’t think to leave us tools?\""
fe "\"It’s nailed shut.\""
hide pau
hide fel
with dis3
"Voices talk over one another as people in the room shuffle about, touching the crate, trying to push on it to tip it over or look under the sheet."
"It takes a while for Paul to get everybody to quiet down."
"When none of the Albion speakers manage to bring forward a pick, he asks Felipe to ask the Sonoran speakers if they have one on hand."
"Eventually, somebody manages to supply one, and they start picking at the outside walls of the crate."
$ renpy.music.set_volume(0.35, delay=3.0, channel='ambient')
play sound ("sfx/bonebreak.ogg")
scene bg cavecrate2 with dis3
"After cracking the wood open, the buzz of the crowd only grows angrier."
"From the angle I can see, it doesn’t look like there are any guns or ammunition inside."
stop sound
"More people shout to take all of the wood off."
"Paul shoves his torso inside instead, looking around. He lets out a shout from within."
show pau angry at right,dark2
show fel mask surprised at left,dark2:
    xzoom-1
with dis3
"He comes out, eyes red from irritation, holding what looks like something limp and rubbery."
fe "\"The hell’s that man?\""
pa "\"These are Yao’s mining gloves.\""
play sound ("sfx/clothrustle.ogg")
"He puts his hand inside, and then pulls out a letter."
play sound ("sfx/paper1.ogg")
"I see a Huaxian character stamped into the red wax of the seal before the wolverine breaks it."
stop sound
"Paul pulls out the letter inside, unfolding it as people let out sounds of surprise or confusion."
"Most of them probably can’t even read the letter considering it’s in Albion."
"Me and Nik look over his shoulder to see what it says."
$ renpy.music.set_volume(0.1, delay=2.0, channel='ambient')
play music ("music/bedhorror.ogg")
show yaonotegetout at dark2 with dissolve
pause
hide yaonotegetout
show fel mask angry
with dis3
fe "\"Oh, fuck this!\""
"We hear the hare curse behind our necks."
"We all turn to Felipe, who has thrown up his arms."
fe "\"No weapons?!\""
"The wolverine stares at the paper some more, as if that will change what the writing says."
show pau angry talking with dis
pa "\"’fraid not.\""
show pau angry with dis
"The hare lets out strings of Sonoran that I don’t understand."
"It makes some of the other Sonorans cover their mouths, or let out calls of despair."
fe "\"He pushes us this far and doesn’t even give us anything to protect ourselves with?\""
show pau eyes with dis
"Paul shakes his head."
show pau angry talking with dis
pa "\"We don’t know what happened!\""
show pau angry with dis1
show pau angry talking with dis
pa "\"I doubt he wanted things to be like this!\""
show pau angry with dis1
show pau angry talking with dis
pa "\"Something must have happened.\""
show pau surprised with dis
show fel mask eyes with dis
"The hare is tugging his ears so hard it looks like he's about to pull them out."

fe "\"Doesn’t matter.\""
show fel mask angry with dis
show pau angry with dis
fe "\"I don’t care.\""
fe "\"There’s no excuse for putting us in this position.\""
show pau angry talking with dis
pa "\"Shit happens Felipe!\""
show pau angry with dis
fe "\"Shit is right!\""
fe "\"He just expects us all to push through the mines and walk out into the desert?\""
fe "\"Just walk on, out there, out in the open?\""
fe "\"No food?\""
fe "\"No water?\""
fe "\"No idea or direction for what’s next?!\""
"He lets out another string of Sonoran, harsher, quieter, more like hissing."
fe "\"No way.\""
show fel mask eyes with dis
show pau surprised with dis
fe "\"I’m out.\""
show fel mask with dis
show pau eyes with dis
"Paul just{nw}"
show pau surprised with dis
extend " stares and blinks."
show fel mask angry with dis
show pau angry talking with dis
pa "\"The fuck you mean, {i}you’re out{/i}?\""
show pau angry with dis
"The hare shakes his head."
fe "\"I said what I said!\""
show fel mask eyes at left,dark2 with dis3:
    xzoom 1
"The hare starts pushing his way through the crowd."
show fel mask surprised with dis3
show pau angry at centerleft with dis3
play sound ("sfx/thud8.ogg")
"Paul grabs him by hooking him around the elbow."
show fel mask angry at left,dark2 with dis3:
    xzoom-1
show pau angry talking with dis3
stop sound
pa "\"You think if you just put up your hands they won’t shoot and they’ll let you go back to mining?!\""
show pau angry with dis
fe "\"I dunno man!\""
fe "\"Maybe?!\""
fe "\"You think it was worth it, losing all of our friends? All of our jobs?\""
fe "\"Our lives?\""
fe "\"How was any of this worth it?\""
"I worry that if Paul pulls any tighter on the hare’s arm that he’ll tear it off at the socket."
show pau angry talking with dis
pa "\"How is the Guard’s overreaction {i}our{/i} fault?\""
show pau angry with dis1
show pau angry talking with dis
pa "\"Do you really think things would have gone better if we hadn’t done anything at all?\""
show pau angry with dis
fe "\"I really don’t know!\""
play sound ("sfx/thud6.ogg")
show pau surprised at center
"Felipe yanks his arm away from the wolverine and pushes him away." with hpunch
show pau angry with dis
fe "\"Kind of hard to imagine anything worse than this?\""
stop sound
show pau angry talking with dis
pa "\"It was pretty damn easy to imagine considering they’ve done it before!\""
show pau angry with dis1
show pau angry talking with dis
pa "\"They’re monsters, Felipe!\""
show pau angry with dis1
show pau angry talking with dis
pa "\"They were never gonna stop!\""
show pau angry with dis1
show pau angry talking with dis
pa "\"They don’t know how to stop!\""
show pau angry with dis1
show pau angry talking with dis
pa "\"We had to show them the consequences!\""
show pau angry with dis
"The hare holds up both of his paws in front of the wolverine to cut him off from speaking."
show fel mask eyes with dis
fe "\"Look.\""
show fel mask angry with dis
fe "\"I know you don’t have a family.\""
play sound ("sfx/clothrustle.ogg")
show fel angry with dissolve
show fel angry talking with dis
fe "\"But I do.\""
stop sound
show fel angry with dis1
show fel angry talking with dis
fe "\"They will die without me, and I am not going to let that happen.\""
show fel angry with dis1
show fel angry talking with dis
fe "\"So fuck your ideals.\""
show fel angry with dis1
show fel angry talking with dis
fe "\"And fuck your imaginary weapons.\""
show fel angry with dis1
show fel angry talking with dis
fe "\"My family relies on {i}tangible{/i} things.\""
show fel angry with dis1
show fel angry talking with dis
fe "\"So like I said before...\""
show fel angry with dis1
show fel angry talking with dis
fe "\"I’m out!\""
show fel angry with dis1
hide fel with dis3
"The hare pushes past the wolverine and starts loping down the tunnel."
show pau angry talking with dis
pa "\"You’re a coward! You hear me?!\""
show pau angry with dis1
show pau angry talking with dis
pa "\"A damn fool if you do this!\""
show pau angry with dis3
show nik disappointed blood at right,dark2 behind pau with dis3
ni "\"Just let him go, Paul.\""
hide pau
show nik sidelook
with dis3
"The wolverine ignores Nik and follows the direction that Felipe run off in."
"Paul shouts again, cursing him, damning him, saying he’ll skin him if he ever sees him again."
"Confusion breaks out again once the hare disappears completely into the dark."
"Again, people call out Yao’s name, and for the weapons."
m "\"Nik...\""
show nik eyestalking with dis3
ni "\"What, Sam?\""
show nik neutral with dis
"He sounds agitated."
"I don’t know if it’s because of what Yao really left in the crate, or what just happened with Felipe."
m "\"...Sorry.\""
show nik sidelook with dis3
ni "\"Nothing to be sorry for.\""
ni "\"We can only control what we choose to do.\""
show nik disappointed with dis3
ni "\"Others will do what they want.\""
show nik sidelook with dis3
ni "\"And right now I’m looking for that red paint.\""
ni "\"Even if that’s all he gave us, that’s still something.\""
if SNY_Points >0:
    m "\"He told us not to come.\""
    show nik smile with dis3
    "Nik smiles."
    ni "\"And we did anyway.\""
    ni "\"You’re only proving my point, Samuel.\""
    #
else:
    "You and I both know that ain’t shit, Nik."
    "I told you not to trust him Nik, but you wouldn’t listen."
    #
show nik neutral with dis3
m "\"But why would he leave his gloves?\""
if SNY_Points >0:
    "I think about the pit at the bottom the mines."
ni @talking "\"Perhaps he wanted to hide the letter.\""
m "\"Somebody would find it.\""
hide nik with dis3
"I look at the pair of gloves dropped on the floor, bending down to pick them up."
"Maybe he left some other message with them."
"There’s nothing scratched onto the outside of them."
"I feel around them."
"Nothing inside."
"They’re just leather gloves, as thick as they are ordinary."
"But I recognize his smell."
"These are definitely his."
stop music fadeout 5.0
stop ambient fadeout 7.0
"I try to bring up how useless they are before a loud noise makes me shut my mouth."
play sound ("sfx/doubleshot mine.ogg") volume 0.65
"We hear gunshots down the tunnel."
stop sound
"Gunshots that are extremely close."
"Everybody goes quiet."
"I don’t want to think if those shots were for Felipe or not."
"Somebody shoves the crate, making it rock."
"For a moment I see there’s darkness beneath the corner."
"Nik sees it too."
show nik angry blood at right,dark2 with dis3
play sound ("sfx/creak4.ogg")
"We hold the ends and shove it together."
stop sound
"It budges, but we can’t muster the strength to tip it over alone."
ni "\"Give us a hand!\""
show pau angry at left,dark2 with dis3:
    xzoom-1
"Paul doesn’t wait to ask anything as he puts his body weight into the box too."
"His eyes are angry and bleary, probably because of what likely just happened down the tunnel."
"But he puts everything that he has into the push."
#adjust
play sound ("sfx/thud7.ogg")
scene bg cavecrate3
"It topples over, and beneath it we can see a shallow drop." with vpunch
"There’s dark red paint splattered on the floor."
show pau angry at left,dark2 with dis3:
    xzoom-1
"The wolverine gestures with his arms and shouts."
show pau angry talking with dis
pa "\"Down! Quick!\""
show pau angry with dis1
scene bg cavepassage with dis3
play music ("sfx/whispers.ogg") fadein 4.0
"Nik and I and several other miners drop down."
"As we descend, we can see that there’s a series of additional drops that lead into the lower level of the next floor if we slide through the gaps and keep dropping."
"Dozens of people follow us through, spilling through the cracks."
"I see one man twist his leg, but he covers his mouth to smother the noise of his pain."
"Another man slips, hitting his forehead, going unconscious."
"Some people try to carry him, but others argue about it."
"We don’t stop to see whether they bring him or not."
scene bg caveelevator with dis3
"It doesn’t take long to get to the widest room of the mine with the long vertical shaft."
"Like Yao promised, a caged platform is there which wasn’t there before."
if SNY_Points >0:
    "I recognize it as the disassembled piece which was left at the bottom of the mine on the way to the Hendricks’ manor."
    #
else:
    "There’s something about it that doesn’t fit in with the rest of the nature of the mining equipment."
    "It feels too old and too nice to have any meaning for being here."
    #
"Nik tells us the elevator looks sturdy enough to fit about ten people at a time."
"Paul volunteers to operate the winch above."
"The way it whines and squeals sends chills through my bones as I watch the first group of ten go down."

"It’s not any easier when it’s my turn to descend."
"I wonder for a moment if it’s noisy enough to get us caught."
"If there are guardsmen watching us, they ain’t speakin’, and they definitely ain’t shooting."
scene bg cavebridge with dis3
"Nik operates the winch from the bottom, and I feel a little better once the three of us are down here together with the rest of the men."
"But the long rope bridge swaying from one side of a chasm to another is waiting for us, and the acid in my stomach wells up in my throat."
if SNY_Points >0:
    "The voice has long left me, but I remember how it goaded me across that bridge."
    "Wanting me to go down."
    "Wanting me to go deeper."
    "But across from me, I also see the false rock."
    "I remember that Yao had stored a gun."
    "I test the rock to see if it’s still there..."
    play sound ("sfx/stonescrape2.ogg")
    "And it is."
    "A reminder of a promise, despite everything, somewhat fulfilled."
    stop sound
    "I whisper."
    show nik neutral blood at right,dark2 with dis3
    m "\"Nik.\""
    show nik surprised with dis
    "He turns to me, feeling the gun at his side."
    show nik neutral with dis
    "I try to slip it to him, to make him hide it."
    show nik disappointed with dis3
    "But he shakes his head, then slips it in my pocket."
    ni "\"You will need that more than me.\""
    show nik angry with dis3
    "He bares his fangs and shows me fisticuffs, lightening my heart, making me forget for just one moment where we are again, and what’s happened to us."
    show nik neutral with dis3
    show pau angry at left,dark2 with dis3:
        xzoom-1
    m "\"Paul.\""
    show pau angry talking with dis
    pa "\"What now, Ayers?\""
    show pau angry with dis
    "The wolverine still sounds emotional."
    "Whether it’s because of what Felipe did, or what likely happened to him, we can’t say."
    show pau angry with dis
    m "\"When we get to the bottom of the mine there’s a path we have to follow.\""
    show pau with dis
    m "\"Tell as many people as you can that they have to follow the markings on the ground, and go nowhere else.\""
    show pau eyes talking with dis
    pa "\"Sure thing sweetheart.\""
    show pau with dis
    show nik surprised with dis
    "Nik gives me a wary look."
    show nik neutral with dis
    m "\"We’ve been this way before Paul.\""
    m "\"You have to do this.\""
    ni @talking "\"Yao was the one who told us to do it the first time.\""
    "He nods slowly."
    "It’s not an understanding nod."
    show pau talking with dis
    pa "\"So how come it wasn't in the letter then?\""
    show pau with dis
    "That’s a fair question."
    "{i}How come it wasn’t on the letter{/i}?"
    "Nik and I weren’t guaranteed to be here to tell anybody."
    "That omission feels reckless for a fella like Yao."
    "A fella who’d factor in every detail."
    "Maybe he was rushed."
    "Either way, we can’t tell if Paul’s choosing to listen to us or not."
    "But I can only hope everybody who would choose to listen heard us."
    #
else:
    show pau angry at left,dark2 with dissolve:
        xzoom-1

show pau angry talking with dis
pa "\"Let’s go, folks, let’s GO!\""
show pau angry with dis
"The ropes beneath us squeak and whine as we’re shepherded across the bridge."
"Considerin’ the circumstances, I’m impressed that too many people aren’t crossing over at the same time."
"But considerin’ we can’t even see the bottom of where we’d fall, it might be because everybody knows they don’t really want to cross this bridge."
"Even though they know now that they have to."
scene bg cavebridge2 with dis3
"In some ways it’s a miracle we can manage to get this many people across this old bridge without it failing."
"It’s so damn dependable for a bridge this old."
"Especially for something made of rope."
"But for some reason, that also feels wrong to me."
"Because it shouldn’t be for something so ordinary."
"But it is."
"It's as if this bridge isn’t meant to fail."
"Every person is meant to make it."
"And every person does make it to the descent of stone steps on the other side."
if SNY_Points >0:
    "They’re just as old and out of place as I remember them. That same feeling that the elevator gave me."
scene bg cavespiral with dis3
"Our long walk down begins."
"And I don’t know how long we walk."
"We go deeper."
show deepmine with dis4
"It gets darker."
"Hearing the shambling of so many footsteps stops making me feel so comfortable now."
"There are many of us, but we couldn’t see one another’s faces."
"As we go deeper, I don’t hear as many footsteps."
"And it frightens me."
"I try to stare into the dark, to try and see if anything has happened, as if to make out whether or not there are fewer of us."
"I can still see many men walking, even if their faces are hard to make out."
"But some of them are crawling on their hands."
show nik sidelook blood at right,dark3 behind deepmine with dis3
ni "\"You see them doing it too?\""
"I don’t answer for a while."
"Then I whisper."
m "\"Yeah.\""
"I wait a while before I speak up again."
no3 "\"Don’t let them hear you.\""
"The fur on the back of my neck sticks up after I hear that voice, the voice that couldn’t possibly belong to a person."
m "\"Why’re they crawling?\""
show nik disappointed with dis3
ni "\"Must be tired.\""
ni "\"It is like your feet know when you shouldn’t be walking.\""
show nik talking with dis3
ni "\"But your hands know there is always more work to be done.\""
show nik eyes -talking with dis1
show nik eyestalking with dis
ni "\"Busy hands are living hands.\""
show nik neutral with dis
"I nod, even though he’s talking kind of funny."
m "\"Please don’t start crawling Nik.\""
ni @talking "\"I would not if you asked me to.\""
"I reach out to hold his hand in the dark."
"But whether the dark is at fault, or the level of the steps, it’s impossible to find."
$ renpy.music.set_volume(0.8, delay=4.0, channel='music')
play music ("sfx/crystalhum.ogg") fadeout 3.0 fadein 3.0
scene bg black with dissolve
scene bg crystal entrance2 with dis3
"At last, we reach the bottom of the steps."
"I don’t feel better being here."
"But it’s much easier to see."
"And I don’t hear any guns down here."
"Just a buzzing sound."
"A sound like the earth is talking."
"Talking from one of the oldest pits of time."
"A time before time even began for people."
"It’s impossible to ignore the massive pile of stacked gloves beside me."
play sound ("sfx/thud8.ogg")
show pau at center,nightgreen with dis3
"Without saying anything, Paul takes Yao’s gloves and tosses them onto the pile."
stop sound
"Nobody feels the need to ask him why."
"So I do."
m "\"Why did you do that?\""
"There’s an inexplicable dread inside me again."
show pau talking with dis
pa "\"Dunno.\""
show pau with dis1
show pau talking with dis
pa "\"I wasn’t really thinkin’ about it.\""
show pau with dis
m "\"But still.\""
m "\"You did it.\""
show pau angry with dis
"He looks at me like I’m crazy."
"But I’m not the person who has a hard time explaining why I do things whenever somebody asks."
"It’s crazy that he doesn’t know why."
show pau angry talking with dis
pa "\"It’s not like he’s going to need those anymore, is he?\""
show pau with dis1
show pau talking with dis
pa "\"I’ll buy him new ones.\""
show pau angry with dis1
show pau angry talking with dis
pa "\"That is, if I ever see the sunuvabitch again.\""
show pau angry with dis1
hide pau with dis3
"I notice that the pile gets bigger as more workers get to the bottom."
"And Paul didn’t just put Yao’s in the pile."
"His are gone too."
"I don’t know why, or what it means, but I don’t think it’s a good idea."
"I keep mine on in case I’ll need to climb anything sharp."

"{i}The pile has already been there after all{/i}."

"It feels very grim to me, like agreeing to have your bones thrown into a tomb, or an ossuary."
"Mixed in and inseparable from all the others."
"Where not even your bones can point out much about who you were anymore."
"I don’t want to look to see if Nik has put his gloves on the pile too."
"Some people make casual talk about the walk being hell and that they don’t want to carry any more unnecessary weight."

if SNY_Points >0:
    scene bg crystal corridor2 with dis3
    "But I can’t pay much more attention to them."
    "I need to find the path."
    "The path that will lead me and Nikolai out of here."
    "But then I stop."
    "Nothing in this tunnel glows like the way it did the first time."
    "What was bright and lustrous looks wet, like glistening mud, or fouled water that shines in uneven flecks when disturbed."
    "I can’t see a path anymore."
    "There’s no distinct pattern to light the way."
    "Just faintly glowing lights that mix together, and crossroads into what look like arched doorways."
    #
else:
    scene bg crystal corridor2
$ renpy.music.set_volume(1.0, delay=0.0, channel='ambient')
show pau at left,nightgreen:
    xzoom-1
show nik neutral blood at right,nightgreen
with dissolve
show pau talking with dis
pa "\"This is the bottom of the mine, ain’t it?\""
show pau with dis3
show nik sidelook with dis3
ni "\"Must be.\""
show pau talking with dis
pa "\"Well, what the hell?\""
show pau with dis1
show pau talking with dis
pa "\"Never thought we’d see it, with all the warnings and the stories.\""
show pau with dis
"He sounds almost proud to be here."
show pau talking with dis
pa "\"This was supposed to be undeveloped cave, but that ain’t true at all.\""
show pau with dis1
show pau talking with dis
pa "\"What do you think of it?\""
show pau with dis
"I pity him."
show nik disappointed with dis3
ni "\"I think I never want to see it again, Paul.\""
ni "\"This, or any level.\""
show nik neutral with dis3
show pau angry with dis3
"Paul spits on the ground."
show pau angry talking with dis
pa "\"Just leaving a piece of me behind.\""
show pau with dis1
hide pau
hide nik
with dis3
"Some people mill about, looking at the lights."
"Some people chat a little easier."
"But they shouldn’t."
"Because there isn’t time for this."
"We have to get out."
"Whatever sense of urgency we had is gone."
"Some people choose a spot to rest."
"We have to get out!"
"I must have said that out loud because of the pat on the back somebody gives me."

play sound ("sfx/jamesexplosionmine.ogg")
play background ("sfx/caveinloop.ogg") fadein 2.5
show bg crystal corridor2 at my_shake2:
    zoom 1.003
"But all voices stop when we hear the explosion." with vpunch
"It doesn’t sound like a cave in, or a dynamite stick going off."
"It sounds like a hundred dynamite sticks tied together and then launched into the sun."
"There’s a terrible quaking around us all."
"Some people think it’s an earthquake."
stop background fadeout 4.0
scene bg crystal corridor2 with dis3
"Some people think it’s an air strike."
show pau surprised at left,nightgreen:
    xzoom-1
show nik surprised blood at right,nightgreen
with dis
m "\"What just happened?\""
show nik sad with dis3
ni "\"It sounded like an explosion above.\""
show pau surprised talking with dis
pa "\"That’s what I thought it was too.\""
show pau angry with dis
"A cougar spooked by the explosion is shouting."
show nik sidelook with dis3
"Even in his own language I could pick out what he was shouting about. The dark, the lack of weapons."
show pau angry talking with dis
pa "\"Stop screaming.\""
show pau angry with dis
"His patience has run out."
show pau angry talking with dis
pa "\"I said stop {i}fucking{/i} screaming, and {i}stay calm{/i}.\""
show pau angry with dis
"Paul’s patience has run out, too."
show pau angry talking with dis
pa "\"All we {i}have{/i} to do is keep going straight until we run into the right way.\""
show pau angry with dis
"The man keeps yelling."
"So does Paul."
"It couldn’t be clearer that neither could understand one another, but Paul keeps talking, waving his arms."
show pau angry talking with dis
pa "\"It’s obvious this was carved out to be a path!\""
show pau angry with dis
"The wolverine holds out his arms, gesturing forward."
"Some of the men start following him while others argue with one another, perhaps over in which direction to go."
"Paul decides to go straight, still shouting at the man."
show nik surprised with dis3
stop music fadeout 3.0
"But Nik looks like he realizes something."
ni "\"Wait.\""
"The wolverine’s shouts drown out the badger’s."
show nik shocked with dis3
"Nik raises his voice, trying to get Paul and the cougar’s attention still."
$ renpy.music.set_volume(1.0, delay=0.1, channel='music')
ni "\"WAIT!\""
show white with dis1
show black with dis1
play sound ("sfx/ignite2.ogg")
play music ("music/refraction.ogg") fadein 4.5
play background ("sfx/burninglong.ogg") fadein 2.5
scene bg crystal corridor3 with dis4
"But it’s too late."
"A sudden pillar of flame rushes past the cougar, burning his body."
"He screams, and we can all can smell his fat boil in the heat."
stop sound
"When he turns, his eyes have melted out of his sockets."
"Sloughs of flesh fall from his body as he crumples into a heap of wet flesh."
"It happens so fast that we can’t even help."
"Paul bends over, eyes wild, laughing, crying, then throwing up."
"Whatever sense of confidence he was trying to broadcast is long gone."
"For a moment, it looks like he can’t pretend anymore that we’re going to be saved."

if SNY_Points ==0:
    "Perhaps he was wrong to think that he ever should."
    "Or could."
    "I beg Nikolai to see."
    "Beg him to realize this is what will happen to him too, if he tries to save everyone."
    #
else:
    "Nobody deserves what had happened to that other puma."
    "Nobody deserved to see it, either."
    #
"The entire cavern fills with warm, bright light, making the crystals around us shine hotly."
"Smoke starts to fill the room slowly now."

show nik shocked blood at center,cavefire with dis3
m "\"Nik, the gasses!\""
ni "\"Paul!\""
"The wolverine isn’t responding."
hide nik with dis3
"Nik goes over to grab him but he doesn’t budge."
"He stubbornly refuses to move."
"It’s as if he doesn’t seem aware of who he is or where he is anymore."
"I try to shake Nik, who in turn shakes Paul."
"The smoke from the fire covers him with a fog, making him cough and hack."
"Nik starts to cough too."
show nik sad blood at center,cavefire with dis3
ni "\"Damn it Paul, don’t you leave me too!\""
"He takes the man’s arm."
"I realize that if I don’t help him the smoke is going to catch up with Nik."
hide nik with dis3
"So we drag Paul out of the smoke together."
"The wolverine is still laughing."
"He’s sobbing and drooling over himself in between coughs."
"We hear people in front of us cry out as the heat waves of another combustion surge past us."
"Some people’s clothes are alight."
"Some fur is singed."
"The temperature of the room as a whole rises."
"People start to scream as more rock catches aflame."
"The smoke level is past some people’s heads and I’m surrounded by coughing."
"Choking."
"People crawl over one another, trying to climb rocks, or one another."
"But some people start to stick together as they burn."
"Nik takes my hand and charges me through the cave."
"Some people see us and cry out, following us, yelling words we don’t understand."
show nik surprised blood at center,cavefire with dis3
m "\"Nik, you’re following the flames!\""
ni "\"Yes!\""
m "\"We’ll die!\""
show nik angry with dis3
ni "\"No, we die if we stay!\""
$ renpy.music.set_volume(0.2, delay=1.5, channel='background')
scene bg crystalgate1 with dis3
"Somehow, we come to a staircase on the other side of the room."
"But there’s an iron gate behind it."
"And it’s closed."
show nik surprised blood at right,nightgreen with dis3
"Nikolai stops in his tracks."
"I wonder if he feels defeated again, if only for a moment."
"But I realize that he’s hesitating."
"The men who followed us run ahead of him, going for the grate."
show nik shocked with dis3
ni "\"Do NOT!\""
"But again, he’s ignored."
hide nik
$ renpy.music.set_volume(0.5, delay=1.5, channel='background')
play sound ("sfx/sizzle.ogg")
"People scream as their paws fry around the grate of the opening, sticking to the hot metal."
stop sound
"Their hands wind together, fusing to the iron, flesh melting off the digits of their paws, all grasping at the other side, hunting for some latch, or some lever that will lift the hot bars and let them climb."
"And then a terrible feeling comes over me."
"A feeling like I’ve been here before."
"Worse than ever before."
"The first wave of fire had to come from somewhere."
"And then something worse happens."
show white with dis1
scene bg black with dis1
play sound ("sfx/ignite2.ogg")
"A new vortex of flame from the mouth of the staircase swirls out, igniting the people stuck to the metal."
scene bg crystalgate2 with dis4
"By the time it passes them by, their flesh is so disfigured that their faces and bodies have grafted together into a terrible mass of eyes and gaping mouths."
stop sound
"Whatever the nature of this chamber was, it feels as if it's shifting."
"Blue shadows give way to scarlet miasmas."
"Flames color the stone ceiling a deep, vast, red, almost as if it were the sky itself, on fire."
"If what was here was sleeping, it now feels fully awake, and it sips in the screams, sucks up the melting organs."
"It’s the worst thing I’ve ever seen in my life."

show nik surprised blood at center,cavefire with dis3
ni "\"DON’T LOOK!\""
scene bg black with dis3
"Nik takes me by the arms and pulls me up around his neck."
scene bg gateclimb1 with dis3
"Somehow, we’re climbing now."
"The fire hasn’t gotten to him yet."
"He’s still whole."
"Still mine."
m "\"Hey, Nik?\""
"He doesn’t answer."
m "\"Did you know that you were the best friend that somebody like me could have had?\""
ni "\"Stop speaking.\""
m "\"But I want to say what I need to before the smoke catches up.\""
ni "\"We can talk after we get you out of here.\""
m "\"But I’m not getting out of here, am I, Nik?\""
"He ignores me as he reaches his hands up."
#sfx
"Clawing away the rocks with his sharp claws."
"I can see now where we are."
"We’re several feet above the iron gate."
"There’s a weak point in the stone wall."
"Nik is holding onto it with the pick we used to open Yao’s crate."
m "\"I wasted too much time chasing a dream, Nik.\""
#adjust
"We can see a some loose stone."
m "\"I wanted respect.\""
play sound ("sfx/rocktumble.ogg")
scene bg gateclimb2 with dis3
"He beats away the loose stone with his paws, and it falls loose from the damp earth, revealing iron bars that block another way into the stairs."
stop sound
m "\"I wanted money.\""
"The smoke has already risen thick at our feet."
"The last we hear of Paul is below us at the gate."
"He’s trying to help open it with the others who have been disfigured."
"But the smoke gets so thick we can’t see them anymore."
ni "\"If we break through we can open it from the other side.\""
"I don’t know if he’s listening anymore."
"But I still need him to hear this."
"I need him to hear this before the end of him, and me, and every trace we have of one another."
m "\"I wanted to live the end of my life out in light and glamor.\""
m "\"And I wasted it when I could have spent that time with you.\""
"He starts beating the iron blocking our way with his fist."
"Beating it until his paws bleed."
"The smoke is at our shoulders now."
m "\"I love you, Nikolai Król.\""
ni "\"I SAID.\""
play sound ("sfx/thud.ogg")
scene bg gateclimb3
"The badger crouches, and jumps, bashing his skull into the iron." with vpunch
stop sound
m "\"STOP!\""
"He leaves a massive dent in the bar."
play sound ("sfx/thud6.ogg")
scene bg gateclimb4
ni "\"I’M GETTING YOU!\"" with vpunch
"The second leaves the bar curves and his forehead bloody."
play sound ("sfx/thud2.ogg")
scene bg black
ni "\"OUT!\"" with vpunch
play sound ("sfx/rocktumble2.ogg")
stop music fadeout 1.0
pause 2.0
"I can’t stop him."
stop sound
"It pops off with the third hit."
scene bg pastgate with dis3
"He grabs me by the waist and pushes me up, onto the stone staircase, hacking, coughing, and then slumps."
"The smoke isn’t as bad at this level yet."
"Nik got me out, away from the others, just like he promised."
"But he isn’t moving."
"He isn’t even breathing."
show white with dis1
hide white with dis
"Above me, I see another terrible flash of white."
"A pillar of fire is coming for me, and for Nik."
"I’m grateful that at least Nik won’t feel it."
"I reach through the grating of the stairs and hold onto his paws."
"Just to squeeze them one last time."
scene bg black with dis3
"Then I close my eyes and wait."
stop background fadeout 4.0
"But something’s wrong."
"I look around me."
play ambient ("sfx/thrumming.ogg") fadein 5.0
"I’m in the dark."
"The air is cool, and wet, and I hear that gentle thrumming."
"It’s that terrible, hollow earth sound."
"But right now, for some reason, it puts me at ease."
"It’s my only reminder that, right now, somehow, my blood still runs through me."
"I look about me as I let my eyes adjust."
scene bg cavelight with dis4
"But I see nobody in this place."
"And nothing but an endless expanse with rays of light that bounce, almost gracefully, off of materials I ain't ever seen the likeness of before, them being more liquid than rock, both solid and wet and formless and smooth."
"But a voice speaks, and anything capable of glimmering in the room gives light, like molten gold running through liquid marble."
no3a "\"Life is not constant.\""
"A voice reaches out to me."
no3a "\"Death is not constant.\""
"A happy voice."
no3a "\"You, yourself, are not constant.\""
"A content voice."
"A voice I have heard before."
"But something has changed about it since the last time I heard it."
"It no longer sounds crackled, or dry."
"It sounds rich, and playful."
"Almost comforting."
no3a "\"Be not afraid.\""
no3a "\"For this time, in solitude, you are saved.\""
"I wait in silence, almost eager, for my next message."
"Because I am so happy that we are still here."
"That time continues for us, like a clock not yet broken."
"Though I do not know who us is."
"All I can feel is that my dread wanes."
no3a "\"Now remember.\""
"And the voice comes back to me, pouring down my ear, like some secret music composed for the architecture of my body, alone, thrumming through the chambers of my heart, and plucking at the string of every nerve."
no3a "\"There is only one constant in all of creation.\""
"The warmth."
"The light."
"The safety."
"It is overwhelming to me."
no3a "\"And that is a meal.\""
stop ambient fadeout 3.0
scene bg black with dis3
"The light in the chamber goes out."
"As soon as they had come, those lovely, bubbly, calming thoughts leave me."
"The sense of peace is gone."
"The sense of awe rushes from my veins as though every last one of them has been sliced open."
$ renpy.music.set_volume(0.4, delay=1.0, channel='background')
play music ("sfx/reverb.ogg") fadein 4.0
"I wake up beneath the quivering carapace of that monster spider."
"I think surely that if the flames haven’t killed me, this will be it."
"But it does not kill me."
"It drags me by the wrist, up those winding stairs, away from the burned body of Nikolai Król, whose arms I leave outreached."
"It takes me through parts of the earth inaccessible to those who can’t climb walls."
"Scuttling."
"Slithering."
play background ("sfx/burninglong.ogg") fadein 5.0
scene bg desertfire with dis4
"Pushing me out of a hole in the ground in the middle of the desert."
"It is rejecting me."
"But only me."
"As if I were scraps."
"As if to diminish Nik’s sacrifice."
"As if to say that he wasn’t why I had gotten out after all."
"But that doesn’t matter to me."
"It was he who got me out of that hell."
"Because he promised me that he would."
scene bg mansionfire with dis4
"And it’s because of him that I can see, in the distance, that the Hendricks’ manor burns, shinin’ like the world’s brightest torch."
"The explosion we heard below had been a house fire."
"Nik put together that this was what had set the mine ablaze."
"Because Yao hadn’t been lying about the gasses."
"Yao’s map was trustworthy."
"And Nik had trusted him."
"Was that why wasn’t I enough for him?"
"He wanted to save us all."
"Instead, he lost us."
"He should have been more selfish."
"{i}I{/i} should have been more selfish."
"For a moment, I really want to believe in their dream."
"But why die for a better world if none of us could make it there?"
scene bg desertfire with dis4
"I sit on the metal grating, struggling to move out of the smoke, when everything I've lost catches up to me."
"How could I have been so stupid to try and run away when the person I really wanted was here the whole time?"
"I think about William, who protected us until the very end, until a single bullet twisted him into something lifeless and empty. "
"I think about Nik, my best friend, the greatest love I’ve ever known, dead with his associates, miles beneath the ground, only because he gave more and more of himself until there was nothing left."
"And how the people who made him happy are all dead."
"At the very least, I think about how that house, and this mine, and this city will be consumed with them in this inferno."
"But was it worth this?"
"Their suffering?"
"Their unraveling?"
"Their undoing?"
"I don’t know."
"I look again at the metal grating I sit on top of."
"There, I see the hands of more men."
"Men who had died in different parts of the mine, who had tried to get out."
"Who were sticking their hands through the bars, searching for a latch or a weak spot in the dirt, just like the men lost at the bottom, who had all suffocated from the smoke."
"And I start sobbing."
"Again, I don’t know."
"But there’s one thing I know for sure, beneath the red sky, as my lungs fill with toxic smoke."
$ renpy.music.set_volume(0.1, delay=0.0, channel='music2')
scene bg black with dis4
"It feels like it’s my turn to die too."
"But it doesn’t come to me."
"Oh God, why doesn’t it come to me?"
play music2 ("sfx/hysteria.ogg") fadein 15.0
$ renpy.music.set_volume(0.8, delay=5.0, channel='background')
scene bg echobackalleyfire with dis4
"As I hobble toward the Hip, I find that the Hendricks’ manor isn’t the only thing caught up in this inferno."
"The town hall and most of downtown has been caught in the flames too."
scene bg saloonfire with dis3
"The girls and the Madam are nowhere to be found."
"Nor the mayor."
"Nor James or his wife."
stop background fadeout 5.0
scene bg black with dis3
"But I remain."
"Much longer after the fire goes out."
scene bg echored with dis4
"Much longer after the people here rebuild a town that is a shadow of the young city it once was."
"And I try to forget them all."
"Because now there’s nobody to love."
"Nobody to hate."
"Nobody to talk to or think about at all."
"Just an empty place, where empty things happen."
"Where the people who know what happened pretend that they don’t."
"And they survive as lesser versions of themselves."
"Every day, I just experience the one constant of creation."
"That there is a meal."
stop music fadeout 1.5
stop music2 fadeout 1.5
scene bg black
pause 2.0
"Amen."

$ renpy.music.set_volume(1.0, delay=2.0, channel='background')
$ renpy.music.set_volume(1.0, delay=2.0, channel='music2')

scene black with slow_dissolve
window hide
scene credits with slow_dissolve
pause
scene credits2 with slow_dissolve
pause
scene black with slow_dissolve
