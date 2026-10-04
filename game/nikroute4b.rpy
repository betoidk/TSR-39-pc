label nikroute4b:
stop background fadeout 1.5
if SOLDN_Points==0:
    play sound ("sfx/sgun1.ogg")
else:
    play sound ("sfx/sgun2.ogg")
scene bg white with dis1
scene bg minequarryevening with dis
if SOLDN_Points==0:
    queue sound ("sfx/sgun2.ogg")
    scene bg white with dis1
    scene bg minequarryevening with dis
if SOLDN_Points==1:
    play music ("music/tension.ogg")
else:
    play music ("sfx/death.ogg")
"Suddenly, I hear a noise that I’ve never heard before."
"It’s coming from the direction of the crowd."
stop sound
"It’s a loud, popping sound, followed by a whizz."
"Then there’s a wet gurgle."
"It’s coming from behind me."
"Somebody got shot."
"There’s a wolf I haven’t seen before, dressed in miner’s clothing."
"He holds onto his neck as blood splatters from his paws."
play sound ("sfx/thud6.ogg") volume 0.6
"Then he goes down on the floor."
stop sound
"Through the blood I can see that he was holding a gun."
"I look in the direction that I thought I heard the sound from."
"A tiger’s tail disappears deeper into the crowd."

if SOLDN_Points ==0:

    unk "\"THEY KILLED HIM!\""
    m "\"Was it the guard?\""
    unk "\"Who else would it be!\""
    unk "\"It’s just like how they did it at Ludlow!\""
    unk "\"GODDAMN MURDERERS.\""

"One of the guards has a wild look in his eye."
"He lifts his gun."
show wil angry at center,sunsetlilac with dis3
"...That is, until Will grabs the barrel."
wi "\"STOP!\""
wi "\"SAGUARO COUNTY IS MY JURISDICTION.\""
"The man is struggling, twisting to get his gun out of the coyote's paw, but Will just brings him closer."
wi "\"You raise that gun into an audience again and I will shoot you myself, y'hear?!\""
"Guard" "\"You can't do that!\""
show wil with dis3
"Captain" "\"Shut the fuck up and listen to the Sheriff.\""
"Captain" "\"He should know how to handle his people, if he’s any good.\""
"Immediately, the man stops resisting."
"Will walks toward the fallen gunman."
show wil with dis3
"Then he crouches over the body, relaxing his wrist on his knee."
show wil surprised with dis
"He has an odd look on his face when he sees him-- almost something like a look of deja vu, {nw}"
show wil with dis
extend "but it quickly passes."
show wil eyes with dis
"His sharp, hard expression returns, and he nods."
show wil with dis
"He turns his head to the crowd."
show wil talking with dis
wi "\"Now I have a question for the workin' folks.\""
show wil with dis
"He has the whole crowd's attention, now."
show wil talking with dis
wi "\"What was this man's name?\""
show wil with dis1
show wil talking with dis
wi "\"If he has a family, they ought to know.\""
show wil with dis
"Will looks from one man to another."
"Nobody comes forward."
show wil eyes with dis
"Nobody says a thing."
show wil eyes talking with dis
wi "\"Let's try something else then.\""
show wil with dis1
show wil talking with dis
wi "\"Raise your arm if you've ever worked a shift with this man.\""
show wil with dis
"Still no answers."
"Confused murmurs run throughout the crowd."

if SOLDN_Points ==0:
    show wil eyes talking with dis
    wi "\"Now how about the other body.\""
    show wil with dis
    "I blink."
    "There’s another body?"
    "Did two people get shot?"
    "I can feel my heartbeat in my chest."
    "As I approach, I’m trying to see who’s on the floor, but the crowd is swarming the other body."
    "All I can see is a paw."
    show wil talking with dis
    wi "\"Who knew ‘em?\""
    show wil with dis
    if SOLDF_Points ==1:
        $ porterfirstchoice = "Felipe"
        "All I can make out is what looks like the brown fur of a hare."
        "But it couldn’t be...?"
        "The odds that it’s him are too low."
        "That’s what I keep telling myself."
        show nik surprised at sunsetlilac behind wil with dis3:
            yalign 1.0
            xpos -0.10
            xzoom-1
        "Nik just stares, quivering a little."
        #
    if SOLDD_Points ==1:
        $ porterfirstchoice = "Dimitri"
        "A large, black bear paw."
        "I feel my throat closing up."
        "It can’t be him."
        "There’s no way something like this could take him down."
        "Not after everything he’s been through."
        show nik sad at sunsetlilac behind wil with dis3:
            yalign 1.0
            xpos -0.10
            xzoom-1
        "I hear Nik snort."
        "He’s wiping a tear from his face, nodding, then turns away."
        #

    if SOLDP_Points ==1:
        $ porterfirstchoice = "Paul"
        "There’s a burly brown paw."
        "I shake my head, thinking surely it can’t be a wolverine paw."
        "But as I continue to stare at it, I know that I recognize who it belongs to."
        "He always had a knack for speaking his mind."
        "Riling up trouble."
        "But he didn’t deserve this."
        "I feel like he’d only have one word for somebody who uses a gun in the dark rather than their own fist."
        "Coward."
        "But my word is much different."
        "Monster."
        show nik sidelook at sunsetlilac behind wil with dis3:
            yalign 1.0
            xpos -0.10
            xzoom-1
        "Nik’s paw is balled into a fist."
        "He’s shaking with anger."
        #
    show wil eyes with dis
    ni "\"I knew him.\""
    "Goat" "\"So did I.\""
    show wil with dis
    "Mountain lion" "\"Aye.\""
    hide nik with dis3
    show wil talking with dis3
    wi "\"Looks to me like the bullet came from the direction of the wolf on the ground.\""
    show wil eyes with dis1
    show wil eyes talking with dis
    wi "\"I’ll bet the bullets in his gun match the victim’s.\""
    show wil eyes with dis1
    show wil eyes talking with dis
    wi "\"Looks like somebody was trying to stop them.\""
    show wil with dis
    m "\"So... it wasn’t the Guard?\""
    show wil talking with dis
    wi "\"Doesn’t look like it.\""
show wil with dis
"There’s an uncomfortable degree of silence that falls over a crowd this large."
"Both the miners and the Guards look confused and shaken rather than pissed."
"I shift uncomfortably."
m "\"William, are--\""
show wil talking
wi "\"HEY!\"" with vpunch
show wil with dis
"He yells so loud I stop in my tracks."
show wil talking with dis
wi "\"We have the situation under control, sir.\""
show wil with dis
stop music fadeout 5.5
"I don’t know what William did, but it seems to be working."
"I’ve seen him control a crowd before, but never to this degree."
"Is it over?"
if SOLDN_Points==0:
    "Was murdering [porterfirstchoice] all that Briggs wanted here?"
    "Or is there something even worse he's planning?"
else:
    "Did we stop what Briggs wanted to happen here?"
    "Or did we just slow it down a little?"
"I don’t really know."
"And I sure as hell don’t want to stick around, waiting for something else to happen."
"I look around me."
"Weapons are lowered."
"The tension in the air isn’t nearly as thick."
"Things feel oddly normal."
"Ordinary."
"It’s that funny kind of feeling like you’re in the middle of one big old clusterfuck, rather than being at the wrong place at the wrong time before somethin’ extremely awful happens."
show wil talking with dis
wi "\"The situation is under my control, civilian.\""
show wil with dis
"I’m still taken off guard by the shift of tone in his voice, but nobody’s paying us much attention."
"Miners are still crowding around the body."
"But up above me, in the cliffs, I see something slip in between a wall of rocks."
"An orange tail, with stripes."
show wil talking with dis
wi "\"Hey!\"" with vpunch
show wil with dis
"He barks at me again, shaking me out of my spell."
show wil talking with dis
wi "\"Don’t you have someplace else to be?\""
show wil with dis
"I get the feeling he’s trying to tell me something."
"Did he figure out something about Yao without telling us?"
"I just don’t know."
hide wil with dis3
"But when he turns away from me and people fill the space between us, I want to put my faith in him."
"People are already breaking up and dispersing, clearing the way for others to move out."
"If something was going to happen here today, I feel like it already would have."
show nik neutral at left,sunsetlilac with dis3:
    xzoom-1
m "\"Nik?\""
"I see the badger staring into William’s back."
ni @talking "\"...He didn’t have to yell at you.\""
m "\"I don’t think he meant it none.\""
if SOLDN_Points==0:
    show nik sad with dis3
else:
    show nik sidelook with dis3
ni "\"Regardless...\""
if SOLDN_Points==0:
    "I notice he's trying very hard to avoid looking at [porterfirstchoice]'s corpse."
show nik neutral with dis3
m "\"We need to talk about Yao, Nik.\""
m "\"I mean, really talk.\""
show nik eyes with dis
"He {nw}"
show nik neutral with dis
extend "blinks."
ni @talking "\"Why?\""
m "\"Not here...\""
show nik sidelook with dis3
"Nik jerks his head toward the direction of the open mine."
show nik neutral with dis3
"I squint at him like he’s nuts."
m "\"You can’t be serious.\""
show nik eyestalking with dis
ni "\"It’s the only quiet place there is out here, isn’t it?\""
show nik neutral with dis
"I feel the air from the entrance, blowing out again."
"Just a little bit."
"Like it’s sleeping."
"I shake my head."
m "\"Not there, neither...\""
show nik disappointed with dis3
"Nik crosses his arms."
ni "\"If we aren’t going after Yao, then we might as well leave.\""
"God damn it."
"I roll my neck, then my shoulders."
"Then I lower my voice to an audible whisper as best I can."
show nik neutral with dis3
m "\"If we’re going in again... I think I saw another entrance in the cliffs.\""
ni @talking "\"Another entrance?\""
"I jerk my head in the direction of the hills {nw}"
show nik sidelook with dis3
extend "in the quarry, toward the pair of boulders I saw the tail disappear into."
show nik neutral with dis3
m "\"It might be new.\""
m "\"It might not.\""
m "\"In any case I doubt it’s on Yao’s map.\""
m "\"And at this point it must be one of many.\""
show nik sidelook with dis3
ni "\"I do not see an opening there, but we can check.\""
$ renpy.music.set_volume(1.0, delay=0.0, channel='ambient')
play sound ("sfx/gravelwalk.ogg")
scene bg minesecretentrance with dis3
"It takes about a five minute walk up the incline to the two boulders."
"They hang quite some distance over the quarry below, and don’t really have any noticeable opening."
stop sound
"At least, not until I touch ‘em."
"I expected to feel rock beneath my paws, but it’s baggy."
"I follow it down to the bottom of my foot paws and see it disappear into the ground."
show nik neutral at right,sunsetlilac with dis3
m "\"Look here.\""
show nik surprised with dis3
ni "\"That is painted canvas cloth...\""
m "\"Odd place for a tarp don’t ya think?\""

scene bg minesecretentrancetunnel with dis3
play sound ("sfx/clothrustle.ogg")
$ renpy.music.set_volume(0.6, delay=0.5, channel='background')
play ambient ("sfx/softwind.ogg") fadein 1.0
"I pull on the sides of the cloth and poke my head through. A narrow passage runs to the left."
stop sound
"That slow, breathy rush of wind that brushes across my ears lets me know for sure that this is another entrance."
stop ambient fadeout 1.0
scene bg minesecretentrance
$ renpy.music.set_volume(1.0, delay=0.5, channel='background')
show nik sidelook at right,sunsetlilac
with dis3
ni "\"Do you think it is worth it?\""
show nik neutral with dis3
m "\"Think {i}what’s{/i} worth it?\""
ni @talking "\"Seeing where this goes?\""
m "\"The fuck you askin’ {i}me{/i} that for?\""
m "\"I didn’t even want to {i}be{/i} here.\""
show nik disappointed with dis3
"Nik puts his hands in his pockets."
ni "\"But you do want to talk.\""
ni "\"If we need the privacy...\""
"He sighs real loud."
show nik sidelook with dis3
ni "\"Then let us be private.\""
show nik neutral with dis3
m "\"Do you know what I’m going to talk to you about?\""
show nik disappointed with dis3
play sound ("sfx/rummage1.ogg")
"Nik rummages through his bag, takes out his hat, {nw}"
stop sound fadeout 1.0
show nik disappointed h with dis3
extend "and puts it on."
ni "\"...I think so.\""
show nik neutral with dis3
m "\"Alright then...\""

hide nik with dis3
play sound ("sfx/clothrustle.ogg")
"I pull back the cloth and see a wider gap in the rock than the cover would have us believe."
stop sound
"It’s almost hard to believe something like this was hiding in plain sight, but there’s a whole lot of tan crags around here that almost makes everything look the same."
"Then I walk once again into that god-forsaken cave, and I swear that this is the last time."

#chapter page goes here
play background ("sfx/whispers.ogg") fadeout 2.5 fadein 2.5
scene bg black with dissolve
scene bg minesecretentrancetunnel with dissolve
show nik neutral h at right,dark2 with dis3
m "\"I saw Yao in the crowd.\""
show nik eyes with dis
"Nik rests his eyes for a moment, wiping his brow."
show nik -eyes with dis
"When he looks at me again, he looks as if he’s not entirely confident."
show nik talking with dis
ni "\"He told us not to follow him.\""
show nik sidelook with dis3
ni "\"He did not want us to be here at the site at all.\""
m "\"...And you never once thought about why?\""
show nik disappointed with dis3
ni "\"I thought plenty about {i}why{/i}, Samuel.\""
ni "\"I think he knew that the violence would be inevitable.\""
m "\"No.\""
m "\"I meant why’d he have to be here for it?\""
show nik sidelook with dis3
ni "\"Maybe he has somebody else he’s trying to protect.\""
show nik surprised with dis3
m "\"He isn’t you, Nik.\""

"He looks taken aback when I say this."
show nik talking with dis
ni "\"I think everybody has somebody to protect.\""
show nik neutral with dis
m "\"Or something, you mean.\""
ni @talking "\"What do you think then?\""

if SNY_Points >0:
    m "\"Must be that he’s overestimatin’ himself.\""
    ni @talking "\"What do you mean?\""
    m "\"I mean I think whatever he’s doing, he thinks he can pull it off all by himself.\""
    m "\"Thought the whole point of us stickin’ together was to make sure we’d all make it out of this shithole.\""
    m "\"You’d think he’d feel that way on some level after everything we’ve been through.\""
    ni @talking "\"What are you saying?\""
    "I lick my lips because they feel dry."
    m "\"I’m saying whatever he wants, it feels like he wants it so bad he’s okay with the possibility of not catchin’ that train out.\""
    show nik disappointed with dis3
    ni "\"There is no way I believe that.\""
    ni "\"If anybody makes it out of these horrors I know it will be him.\""
    show nik neutral with dis3
    m "\"Believe what you want, but it’s how I feel.\""
    m "\"He has to know it’s possible.\""
    m "\"So why do that if he already has the gold?\""
    m "\"Y’see how that doesn’t add up?\""
    show nik sidelook with dis3
    m "\"He’s after somethin’, Nik.\""
    ni "\"Like what?\""
    m "\"Don’t know.\""
    show nik neutral with dis3
    m "\"But what are we supposed to do if he doesn’t want to leave without it?\""
    m "\"I want to see him catch the train.\""
    #

else:
    m "\"I think it’s always been suspicious how well he knows these mines.\""
    m "\"Sure, he’s fast.\""
    m "\"And he’s a good liar.\""
    m "\"But Briggs and his foremen aren’t stupid.\""
    show nik smile with dis
    ni "\"He’s a good thief.\""
    show nik neutral with dis
    m "\"No.\""
    m "\"They’d have to notice things were endin’ up missin’, or put into the wrong places.\""
    m "\"We {i}know{/i} the type of man Briggs is...\""
    m "\"No way in hell he’d trust a man who looks and sounds like Yao.\""
    m "\"He’s makin’ some kind of deal.\""
    "Nik doesn’t answer immediately."
    #sfx
    "The dripping water of the cave is all we have to keep us company for a while."
    show nik sidelook with dis3
    ni "\"I refuse to believe that.\""
    ni "\"Or if he is, it’s a trick.\""
    show nik neutral with dis3
    m "\"Probably is.\""
    m "\"But somebody might still be gettin’ hurt.\""
    m "\"What if he tipped off Briggs on our meetin’ place?\""
    ni @talking "\"There’s no reason for him to tell them our rendezvous.\""
    m "\"Unless...\""
    ni @talking "\"Unless?\""
    m "\"He wants something that he doesn’t have yet.\""
    show nik disappointed with dis3
    ni "\"You still haven’t told me what that could be, Sam.\""
    m "\"Vengeance never cross your mind?\""
    ni "\"Living well is vengeance enough.\""
    show nik neutral with dis3
    m "\"For you.\""
    m "\"Is that good enough for him?\""
    #

show nik surprised with dis
play sound ("sfx/benyell1.ogg") volume 0.35
ni "\"Quiet.\""
ni "\"Did you hear that?\""
m "\"Yeah.\""
hide nik with dis3
"We walk for a bit in the dark."
scene bg minesecretentrancedrop with dissolve
"But then I see light shine up from a hole in the floor."
"I beckon Nik over and we can see tracks below us."
"It’s suspiciously well-lit for a part of the mine when more than half the workers are absent for the day."
"So we wait, and we listen."
"We don’t hear voices."
"No pickaxes."
"Nothin’."
scene bg minetunnel with dissolve
play sound ("sfx/thud3.ogg")
"So I drop down the hole first." with vpunch
show nik angry h at right,dark2 with dis
play sound ("sfx/thud6.ogg")
"Nik lands a little louder." with vpunch
show nik neutral with dis3
"I recognize this area as one of the busier tunnels we've worked in before."
"We’re close enough to the central shaft."
"Odd how it feels like {i}nobody{/i} is here today."
"Even if it always feels like there’s somebody watchin’."
show nik surprised with dis
play sound ("sfx/benyell2.ogg") volume 0.6
pause 1.0
m "\"What is that?\""
show nik sidelook with dis3
ni "\"It is coming from a different direction.\""
"There’s something about that voice that feels wrong to me."
"Something that makes the fur on my back stand up."
show nik neutral with dis3
m "\"Let’s avoid it?\""
show nik talking with dis
ni "\"If we can.\""
show nik neutral with dis1
hide nik with dis3
"Normally I think somebody like Nik would want to go toward a sorrowful sound like that."
"But the fact that we felt too alone while we heard it changed the feel of the sound just a little bit."
"Made it sound less like a person."
scene bg minechasm
show nik neutral h at right,dark3
with dissolve
show nik talking with dis
ni "\"Look.\""
show nik -talking with dis1
show nik talking with dis
ni "\"The light at the main shaft is on.\""
show nik neutral with dis
m "\"So somebody used it?\""
show nik disappointed with dis3
ni "\"Unlikely.\""
ni "\"The shaft to level two and three is unused...\""
ni "\"The shaft to level four was always broken.\""
show nik surprised with dis3
play sound ("sfx/switch1.ogg")
"I press a big green button and hear something whirr."
stop sound
ni "\"Sam, what are you doing!?\""
m "\"Seein’ if it’s still broken.\""
play ambient ("sfx/elevatorengineloop.ogg") fadein 10.0
"The machine rattles to life again."
"I shake my head."
m "\"Don’t much sound like it’s broken now, does it?\""
"The machine whirrs softly as we hear something in the deep clicking and scraping against the sides of metal."
show nik sidelook with dis3
m "\"Y’think Yao could have fixed this elevator?\""
"The clicking gets louder."
ni "\"Mechanics are his speciality.\""
ni "\"If anybody can--\""
stop ambient fadeout 0.5
play sound ("sfx/elevatorlock.ogg")
"The sound of something heavy locks into place with a hollow boom." with hpunch
show nik sad with dis3
m "\"I’d bet all my gold you gave me as well as those first two double eagles I lost that Yao’s used this thing to be down there right now.\""
stop sound
ni "\"But why?\""

m "\"Are you willing to find out?\""
show nik sidelook with dis3
"I hear him exhale."

ni "\"So what happens if he {i}isn’t{/i} down there?\""
show nik neutral with dis3
m "\"Well {i}somebody{/i} is.\""

m "\"It’s suspicious timing all the same, ain’t it?\""

m "\"Big fight up top causes a commotion and gets rid of the dissenters in the mine all at the same time, yeah?\""

m "\"But the people who ain’t on strike aren’t here neither.\""
m "\"Where’s the bootlickers?\""
show nik sad with dis3
"Nik begins to look uncomfortable."
m "\"They have their own pockets to fill don’t they?\""
m "\"Seems to me like somebody told them not to be here if they ain’t.\""
m "\"So why is that, especially if this elevator is workin’ now?\""
#scene adjust
show nik neutral h at right,dark3 with dis3
play sound ("sfx/elevatoropenmine2.ogg")
"The metal lattice of the door creaks as Nik pulls it open."
show nik disappointed with dis3
"He puts one foot through the door, shifting his weight."
stop sound
play sound ("sfx/stresstest.ogg")
"The platform sinks a little as he steps down, {nw}"
show nik neutral with dis3
extend"but it bounces back up."
stop sound
show nik talking with dis
ni "\"It’s fine.\""
show nik smile with dis
"He reaches a paw out to me."
play sound ("sfx/stresstest.ogg")
"I take it as I step forward and feel the platform beneath me sink, {nw}"

stop sound fadeout 0.2
extend"which makes my chest tighten, before it bounces back up."
show nik neutral with dis
play sound ("sfx/switch2.ogg")
"Once the platform stops rocking I press the button to go down."
stop sound
play ambient ("sfx/elevatorengineloop.ogg") fadein 1.0
scene bg mineelevator
show nik neutral h at center,dark3
with dissolve

"Shadows of bars are cast across our faces as we descend."
m "\"Would be pretty stupid if this is how we get caught after everything else we’ve done.\""

show nik eyestalking with dis
ni "\"Then do not get caught.\""
show nik neutral with dis
stop ambient fadeout 1.0
"As Nik says this, the platform comes to a stop."
play sound ("sfx/elevatoropenmine.ogg")
scene bg cavebridge
show yao teeth h at center,fullblack
show deepmine:
    alpha 0.6
with dis3
"He peels back the doors, slowly, and there’s just enough of a glow from the light to see that somebody’s waiting for us at the bottom."
stop sound
"There’s just enough light to see he’s holding a weapon."
ni "\"...Shit.\""
yaunk "\"I told you not to come here.\""
m "\"...Yao?\""
"The figure lowers its weapon and {nw}"
hide yao with dis3
extend "recedes into the darkness."
play sound ("sfx/stonescrape.ogg")
"I hear the scrape of stone against stone and a small click."
show yao angry crossed h at center,dark2 behind deepmine with dis3
stop sound
"Then he steps fully into the light."
ya "\"Arriving at the quarry was bad enough.\""
ya "\"Coming here is lunacy.\""
show nik surprised h at dark2 behind deepmine with dis3:
    xpos 0.65
    yalign 1.0
ni "\"What are you doing here Yao?\""
ya "\"When it happens you will know.\""
"The tiger doesn’t hesitate with his response."
m "\"When what happens?\""
play sound ("sfx/benyell1.ogg")
"We hear something."
"It’s that noise again."
stop sound
"But it’s clearer this time."
"A low, strained moaning."
"It almost sounds pitiful."

ni "\"What’s that?\""
show yao teeth with dis
ya "\"Have you learned nothing from last time?\""
show yao angry with dis
ya "\"Do not seek out the voices.\""
show nik disappointed -h with dis3
"Nik takes off his hat, pulls a box of matches from his pocket, {nw}"
#sfx
show nik disappointed h with dis3
hide deepmine
with dis3
extend "and lights the flame."
show nik angry with dis3
ni "\"I am not scared of anything I can punch.\""
play sound ("sfx/minewalk.ogg")
hide nik with dis3
"He starts walking in the direction of the sound."
m "\"Nik!\""
stop sound
"I look between him and Yao."

m "\"What, you ain’t gonna try and stop him?\""
show yao neutral crossed with dis
ya "\"I will pretend I saw neither of you here.\""
"I chuff."
m "\"Oh really?\""
show yao sidelook -crossed with dis3
"He bends down to grab what looks like a thin wire on the ground."
"He tugs on it like he’s testing something, pulls it all the way back to the corner of the room."
show yao sidelook at left with dis3
"He keeps doing this with various strands."
hide yao with dis3
"I don’t really have time to figure out what he’s doing or wait for his response, so I go after Nik before I lose sight of him."
scene bg black with dissolve
scene bg lakebenapproach
show nik sidelook h at left,night:
    xzoom-1
with dis3
play background ("sfx/spring.ogg") fadeout 2.5 fadein 3.5
"As we follow the sound, Yao disappears from view, and we hear running water."
m "\"Nik, he was doing something back there.\""
ni "\"And he was also ignoring the sounds.\""
m "\"Y’think he has something to do with that?\""
ni "\"I don’t think anything yet.\""
show nik disappointed with dis3
ni "\"But there’s no reason not to look.\""
scene bg cavelakeben with dissolve
show nik neutral h at left,night:
    xzoom-1
with dis3
"The sound of the water gets louder."
ni @talking "\"Hear anything?\""
"His beam of light scans the surface of the water, but we only see pebbles, flecks of mica, and thick deposits of mud."
"We see a blind crab scuttle beneath a flap of something in the murk."

play sound ("sfx/benyell2.ogg")
"Then we hear the moaning again."
m "\"There!\""
stop sound
show nik surprised with dis
ni "\"Somebody’s crawling out of the mud.\""
"Or something."
m "\"Keep your light still.\""
"It’s sliding through the sludge."
"The dirt is caked on and its fur is matted."
play music ("music/contemplation.ogg") fadein 2.5
benunk "\"Help...\""
benunk "\"Help me...\""
"I whirl to Nik."
m "\"That’s Ben’s voice.\""
"We look again at whatever has come out of the mud."
"We mostly can only see his eyes beneath the grime."
"His overalls are filthy."
"His left arm and foot are bent in the wrong way beneath the revealed bits of skin."
m "\"Is he alive?\""
show nik sidelook with dis3
ben "\"F-fuck you!\""
m "\"Yeah, he’s alive.\""
"But only barely, it looks like."
show nik neutral with dis3
ben "\"Y-you gotta help me.\""
m "\"...Excuse me?\""
ben "\"Y-you’re the ones who did this.\""
m "\"We didn’t make you fuckin’ fall.\""
ben "\"Get me to the surface...\""
ben "\"Everybody’s gonna know...\""
ben "\"What y’all did...\""
show nik sidelook with dis3
ni "\"Hm.\""
ni "\"Let us go.\""
m "\"Agreed.\""
#sfx
ben "\"Wait a minute.\""
show nik neutral h at left,night with dis3:
    xzoom 1
"We start to walk away."
show nik eyes with dis
ben "\"I said WAIT a minute! Y-you can’t just leave me to die...\""
"I keep on walkin’."
show nik disappointed with dis3
"Nik stops for some reason though."
ni "\"You tried to kill us earlier.\""
show nik neutral h at left,night with dis3:
    xzoom-1
ben "\"N-now hold on now, that was just talk...\""
"I crook my entire neck so hard I almost feel like my head is about to fall off."
m "\"Just talk?!\""
ben "\"You boys were tryin’ to keep all the gold for yourselves!\""
ben "\"After all, I was right, wasn’t I!?\""
ben "\"Y’all filled your pockets with a one-way ticket to the good life and you were just gonna mosey on out of town, weren’t ya?\""
ben "\"How was that fair for the rest of us?!\""
show nik disappointed with dis3
"Nik shines his beam over Ben’s face and takes a good look at him."
ni "\"Since when have you cared about the rest of anybody?\""
ben "\"I know what it’s like to work like hell for nothin’, waitin’ for somethin’!\""
ben "\"But the boss, he works hard too!\""
m "\"Oh fuck {i}off{/i}.\""
ben "\"I know things are hard, but how exactly is it fair to steal from ‘em?!\""
ben "\"You commies pretend to care about everybody, but at the end of the day, you just take what you want and give it to your friends, yeah?\""
ben "\"Where exactly is the fairness in all that?\""
ben "\"You gonna kill me because that sits wrong to me?\""
m "\"It ain’t killin’ ya if you went ahead did it to yourself.\""
ben "\"Bullshit on that! It’s the same fuckin’ thing as murder if you leave me like this!\""
show nik neutral with dis3
m "\"I pick murder, then.\""
ben "\"You dirty motherfucker!\""
"He starts makin’ a sound."
"An ugly sound."
"I blink because I don’t really get what he’s doing at first."
"Then I realize the son of a bitch is crying."
m "\"Let’s stop wastin’ our time here and go.\""
if SNY_Points==0:
    show nik sidelook with dis3
    "Nik inhales."
    show nik disappointed with dis3
    "Then exhales."
    ni "\"He likely will die if we leave him here, Sam.\""
    m "\"So it all works out.\""
    m "\"We ready to go now?\""
    show nik eyes with dis3
    "Nik slowly shakes his head and turns {nw}"
    show nik neutral with dis
    extend "to Ben."
    ni @talking "\"I’ll help you out of the mine if you promise me one condition.\""
    ben "\"Oh! Anything!\""
    show nik neutral h at center,transparent with dissolve
    ni @talking "\"You forget what you saw with the gold, with us, and with the creature, and you never tell a living soul.\""
    ben "\"Not a {i}single{/i} soul?\""
    play sound ("sfx/thud5.ogg")
    show nik angry
    "Nik grabs the filthy man’s overalls and shakes him." with hpunch
    ni "\"Nobody! Or we {i}will{/i} find you!\""
    stop sound
    "There’s a snarl in Nik’s voice that lets the both of us know he isn’t lying."
    ben "\"A-alright! Alright! I p-romise! Won’t tell a soul!\""
    show nik neutral at halfleft with dis3:
        xzoom 1
    "I rush up to Nik and turn him my way, lowering my voice."
    m "\"Oh come on now Nik, he’s gonna try and fuck us up if we help him.\""
    show nik disappointed with dis3
    ni "\"He’s no threat to us, even if he tried.\""
    ni "\"Just look at him.\""
    show nik neutral with dis3
    m "\"It’s better for the both of us if you just put him out of his misery.\""
    "Or if you won’t, let me."
    show nik angry with dis3
    ni "\"I am saving him Sam!\"" with hpunch
    "I recoil just a bit from how loud he yells at me."
    show nik sidelook with dis3
    ni "\"This is my decision.\""
    "He’s heaving."
    m "\"Shit.\""
    m "\"You’re serious.\""
    show nik disappointed with dis3
    "He pauses to breathe a little slower, then coughs."
    show nik sad with dis3
    "Then he grimaces."
    ni "\"I took one life.\""
    ni "\"I will save another as penance.\""
    show nik neutral at halfright with dis3:
        xzoom-1
    "He turns around, walks up to Ben, and {nw}"
    play sound ("sfx/clothrustle.ogg")
    show nik disappointed
    show ben at night:
        xpos 0.70
        yalign 1.0
    show benmud at night:
        xpos 0.70
        yalign 1.0
    with dis3
    extend "kneels down to drag him."
    stop sound
    ni "\"I can drag you, but you can help me by crawling forward on your good leg.\""
    show ben eyes talking
    show nik neutral
    with dis3
    ben "\"Oh thank you. Oh God bless you!\""
    show ben eyes with dis1
    scene bg lakebenapproach with dis3
    "I try not to scream from the stupidity of this."
    "We came here for Yao."
    "We got somebody worse."
    show nik sidelook h at right,night
    show ben at night:
        xpos 0.70
        yalign 1.0
    show benmud at night:
        xpos 0.70
        yalign 1.0
    with dis3
    #
else:
    show nik sidelook with dis3
    "Nik starts scratching his head, looking from time to time at the sorry state of the golden retriever on the floor."
    "He inhales."
    show nik disappointed with dis3
    "Then exhales."
    ni "\"Try not to stand.\""
    ni "\"Something might be broken.\""
    "I almost can’t believe my eyes."
    m "\"Nik, just leave him here.\""
    ben "\"Leave me?!\""
    m "\"He’s a murderer.\""
    show nik sidelook at left,night with dis3:
        xzoom 1
    "Nik gives me a sideways look."
    "He looks like he’s about to say something to me, but then he doesn’t."
    show nik eyestalking with dis3
    ni "\"Most men become terrible things when they think nobody in the world will help them.\""
    show nik neutral with dis
    m "\"That’s an awfully big presumption, don’t you think?\""
    show nik disappointed with dis3
    ni "\"He’s light enough to drag.\""
    show nik sidelook at halfright,night with dis3:
        xzoom-1
    ni "\"You do not have to help.\""
    play sound ("sfx/clothrustle.ogg")
    show nik disappointed at halfright,transparent
    show ben at night:
        xpos 0.70
        yalign 1.0
    show benmud at night:
        xpos 0.70
        yalign 1.0
    with dis3
    ni "\"I will do this on my own.\""
    stop sound
    scene bg lakebenapproach with dis3
    "You can’t keep living like this Nik."
    "That faith in people is wasted, just as faith in a false interpretation of God."
    show nik sidelook h at right,night
    show ben eyes at night:
        xpos 0.70
        yalign 1.0
    show benmud at night:
        xpos 0.70
        yalign 1.0
    with dis3
    "Ben just looks back at me with that sickly smile."
    "He’ll take his chance sometime soon."
    show ben with dis
    "But I’ll be ready."
    #
stop background fadeout 5.0
"Nik doesn’t have much trouble dragging him along."
"For a man who’s been through what he has, I’d expect to see death in his eyes, or some kind of distance."
"Instead I can feel his eyes on me."
"And when I look at him, he doesn’t even pretend not to look at me."
"He has a smile in those eyes."
"They’re sparking, like he knows that he beat me in some kind of sick little game, and there’s something about it that absolutely disgusts me."
"I know we’d be better off if we just killed him."
"Nik would probably forgive me in time if I did it right now."
"But I don’t have time, and I need Nik on my side until we’re clear of this place."
show nik disappointed
show ben eyes
with dis3
"We stop for a break, and Nik gives Ben some water first, then some whiskey to drink from his flask, which I consider a terrible waste."
show ben with dis
"But we’re all sitting together now, terribly uncomfortable, and terribly awkward, but sharing this fucked up moment all the same."
"So I figure I might as well say what I feel."
show nik neutral with dis3
m "\"So what the hell is the problem with you?\""
"The golden retriever drops his gleeful little stare and slips into something that looks more like confusion."
show ben talking with dis
ben "\"The hell’s that supposed to mean?\""
show ben with dis
m "\"I mean I said what I said.\""
m "\"No point in hidin’ you tried to kill me three times, is there?\""
show ben talking with dis
ben "\"You talk like you’re innocent?\""
show ben with dis
"I blink like I’ve just been hit in the head with a frying pan."
m "\"Yeah?\""
m "\"Cos I am?\""
show ben annoyed with dis
ben "\"You blew years of good will I built up with the boss...\""
"The man sputters as he speaks."
show ben angry with dis
ben "\"And I mean {i}YEARS{/i}... in just one day?\""
show ben annoyed with dis
m "\"How you figure?\""
ben "\"I weren’t tryin’ to kill you.\""
ben "\"At least not at first.\""
m "\"Well thanks for that!\""
show ben angry with dis
ben "\"You were just supposed to get injured.\""
show ben annoyed
show nik sidelook
with dis3
ni "\"...\""
ben "\"Show the other men you were an occupational hazard, ya know?\""
show nik neutral with dis3
ben "\"You had that Hendricks stink all over you.\""
ben "\"It was supposed to make {i}him{/i} look bad.\""
ben "\"Instead you just made me look a fool twice over.\""
ben "\"Because you couldn’t take any heat for a job you didn’t even give a damn about.\""
m "\"You tried to crush my goddamn paw!\""
ben "\"It would have healed.\""
m "\"You don’t know that!\""
show ben talking with dis
ben "\"I doubt some a pretty boy like you has to make use of both hands on a given day anyhow.\""
show ben with dis
m "\"You’d be surprised.\""
"He looks confused again."
ben "\"...Huh?\""
show nik disappointed with dis3
ni "\"The point is...\""
"Nik’s voice is a little high because he’s obviously trying to change the subject."
show nik talking with dis3
ni "\"You’re sorry for what you did?\""
show nik neutral with dis
show ben talking with dis
ben "\"Well shit.\""
show ben with dis1
show ben talking with dis
ben "\"I don’t fuckin’ know...\""
show ben with dis1
show ben talking with dis
ben "\"I’m more sorry I failed than for tryin’, but yeah.\""
show ben with dis1
show ben talking with dis
ben "\"It got out of hand, yeah.\""
show ben annoyed with dis
ben "\"I don’t usually let things bother me this much, but I don’t think I’ve ever been that mad before.\""
ben "\"It’s the dizzying kind of anger. Almost makes you laugh.\""
show ben with dis1
show ben talking with dis
ben "\"Now Nate’s dead and my arm and leg are fuckin’ ruined.\""
show ben annoyed with dis
m "\"It’ll heal.\""
"He spits on me."
show ben angry with dis
ben "\"{i}Fuck{/i} you!\""
show ben annoyed with dis
"You can’t afford me."
show nik disappointed with dis3
"Nik leans in very close to him."
ni "\"You’re about to go through a time in your life where you can only rely on the help of others to make it through each day.\""
show nik talking with dis3
show ben with dis3
ni "\"Do you really think it is smart to start it talking that way to the only people willing to help you live?\""
show nik -talking with dis
show ben talking with dis
"He opens his mouth, {nw}"
show ben with dis
extend "but then closes it."
show ben eyes talking with dis
ben "\"No.\""
show ben with dis
show nik eyes with dis
"Nik nods."
show nik -eyes talking with dis
ni "\"Every new day might be hell for you.\""
#adjust
show nik -talking with dis1
show nik talking with dis
ni "\"But the sun will rise, you will be there to greet it, and you will be able to say, \"thank you for the light\".\""
show nik -talking with dis1
show nik talking with dis
ni "\"Most people do not even get that.\""
show nik -talking with dis

"He doesn’t say anything more."
show ben eyes with dis
"I stand with Nik, and he begins dragging the man by the back of his overalls again."
hide nik
hide ben
hide benmud
with dis3
stop music fadeout 2.5
"I don’t feel his stare much on me anymore."

"In fact, if I didn’t know any better, I’d say he was close to passing out."

"The pain must be really hard on his body."
scene bg black with dissolve
play background ("sfx/whispers.ogg") fadein 3.5
scene bg cavebridge
show yao h at fullblack:
    yalign 1.0
    xpos -0.10
    xzoom-1
with dis3
"In time we make our way back to the elevator. We see Yao’s silhouette in the dim light."
show nik h at right,dark2
show ben eyes at dark2:
    xpos 0.70
    yalign 1.0
show benmud at dark2:
    xpos 0.70
    yalign 1.0
with dissolve
show nik talking with dis
ni "\"We found--\""
show nik surprised
play sound ("sfx/pipe.ogg")
"Nik’s greeting is interrupted with the sound of a noisy crowbar dropping to the floor, its echoes reverberating loudly in the cave." with vpunch
brunk "\"Now what in the hell is going on over there?!\""
stop sound
"I swear I feel my heart drop into my stomach."
m "\"{i}That’s{/i}--\""
show deepmine:
    alpha 0.6
with dis
"Nik quickly snuffs the flame on his hat."
show nik shocked with dis3:
    yalign 1.0
    xpos 0.96
ni "\"Hide!\""

hide nik
hide yao
hide ben
hide benmud
scene bg cavebridgehide
show deepmine:
    alpha 0.6
with dis3

"Nik drags Ben over behind an outcrop of big rocks and I crouch down with him."

"I hear him whimper and make some little moans, so I try to shush him up."

"As my eyes adjust to the darkness, I can see three new men coming from the direction of the rope bridge that crosses the giant cavern below us."
"The man in the hat I’m certain is Briggs."

"The two others flanking his sides I’m not too sure about."

"At least, until they come a little bit closer."
#Elihere
m "\"Ain’t those James Hendricks’ bodyguards?\""

"I regret saying this the moment it leaves my mouth, because not only does it make Ben’s eyes open wide, but that sparkle is back in his eye."

m "\"Oh don’t you dare.\""

ben "\"HELP! SOMEBODY HELP ME--\"" with vpunch
#sfx
"I try to muzzle his mouth, but he bites me."

"But it doesn’t much matter now, because the wolf and the badger are running straight for us."

"Shit. Shit. {i}SHIT.{/i}"

"They point their guns at our heads."
$ renpy.music.set_volume(0.35, delay=5.5, channel='background')
play sound ("sfx/match.ogg")
show bri at left,fullblack with dis3:
    xzoom-1
"I can hear a match light."
play music ("music/bedhorror.ogg") fadein 2.5
show bri at left,dark2:
    xzoom-1
hide deepmine
with dis2
"Then I see Briggs’s face, which looks unbothered. Almost bored."
stop sound
show bri talking with dis
br "\"Come out now, or I tell ‘em to shoot in three seconds.\""
show bri with dis1
show bri talking with dis
br "\"One...\""
show bri with dis
"We don’t hesitate for a moment."
scene bg black with dissolve
scene bg cavebridge
show yao h at dark2:
    yalign 1.0
    xpos -0.17
    xzoom-1
show bri at left,dark2:
    xzoom-1
show eli suspenders s angry serious behind bri at halfleft,dark2:
    xzoom-1
with dissolve
show nik surprised h behind bri at right,dark2:
    xpos 1.20
    yalign 1.0
show ben at dark2:
    xpos 0.55
    yalign 1.0
show benmud at dark2:
    xpos 0.55
    yalign 1.0
with dis3

show bri talking with dis3
br "\"Good, I’m glad you know I don’t like to play.\""
show bri with dis
"He squints, {nw}"
show bri smile with dis
extend "and then his muzzle curls into a smile."
show bri smile talking with dis
#check
br "\"King?\""
show bri smile with dis
"Then his smile curdles."
show bri smile talking with dis
br "\"And Ayers.\""
show bri smile with dis
"He looks me up and down, ear-tip to boot."
show bri talking with dis
br "\"The hell are you doing here?\""
show bri with dis
m "\"We were lookin’ for our friend.\""
show bri talking with dis
br "\"Which friend?\""
show bri with dis
show yao angry h with dis
"Yao’s eyes flash."
show yao -angry h with dis
"I nod at Nik."

m "\"I was looking for Mr. King, sir.\""
show ben annoyed with dis
ben "\"That’s not what they were up to!\""

"Ben shouts out the words in a breathy kind of struggle, almost as if trying to hold back the manic, overwhelming glee he must be feeling at the turn of events."
show ben with dis
show bri talking with dis
br "\"Didn’t ask ya, Ben.\""
show bri with dis
"He gives the dog a quick glance without turning his head."
show bri talking with dis
br "\"I’m asking Mr. Ayers here.\""
show bri with dis1
show bri talking with dis
br "\"Mr. King is already here with you.\""
show bri with dis
m "\"Well, that’s because I found him, sir.\""
show bri smile with dis
"Briggs smiles a handsome smile."


"Then he turns to his left gunman and nods."
show bri smile talking with dis
show eli -serious -angry with dis
br "\"Right hand, middle of the palm.\""
play sound ("sfx/wgun.ogg")
show bri smile
with dis1
show white with dis1
show nik shocked at dark2:
    xpos 1.16
    yalign 1.0
hide white with dis
"I feel the sting before I hear the boom."
stop sound
"And then my ears are ringing."
"There’s a small hole in my hand."
"Gore rushes out of me as I shake."
show nik angry
show eli angry serious

with dis3
"Nik snarls in rage as both of the gunmen point their barrels at his temple."
"Yao does not look at us, remaining expressionless."
show bri talking with dis
br "\"Get cute with me again and they’ll blow your balls off next.\""
show bri
#adjust
show nik sidelook h at right,dark2:
    xpos 1.20
    yalign 1.0
with dis3
"Briggs clasps his hand and jerks his head over to the retriever."
show bri talking with dis
show eli -angry -serious with dis
br "\"So how come he could do that.\""
show bri with dis
"He nods at the badger on his left."
show bri talking with dis
br "\"In two seconds.\""
show bri angry with dis1
show bri angry talking with dis
br "\"But it takes you {i}two weeks{/i} and you can’t even manage it?\""
show bri angry with dis
show ben talking with dis
ben "\"I... I know I messed up, and you’re right!\""
show ben with dis1
show ben talking with dis
ben "\"I’m sorry.\""
show ben with dis1
show ben talking with dis
ben "\"But I’ll do you one better!\""
show ben annoyed with dis
ben "\"I know what they’re here for!!\""
show ben angry with dis
show bri with dis
ben "\"He’s not on your side!\""
show ben annoyed with dis
"He’s pointing at the tiger."
ben "\"Go on then and fix his hand! He’ll pass out from the blood loss if you stand by!\""
show yao talking with dis
ya "\"I follow orders from boss because he smart and he rich.\""
show yao -talking crossed with dis3
"Yao crosses his arms and looks at Ben."
ya @talking "\"You do not look rich, so I no take order.\""
show ben angry with dis
ben "\"You lying, fucking chink!\""
show ben annoyed with dis
play sound ("sfx/clothrip.ogg") volume 0.6
show nik sad with dis3
"Nik makes his way to me, slowly, tearing the sleeve off his shirt, watching the guns pointed at him as walks."
stop sound
"He makes contact with me, touching me, holding the shirt to my palm."
"As he wraps me up, I can feel him vibrating with anger."
show bri eyes with dis
"Briggs makes an inquisitive little hum."
show bri talking with dis
br "\"Well now, this is a doozy.\""
show bri with dis1
show bri talking with dis
show ben with dis
br "\"I have a mediocre Columbian who tells me one of my men is not on my side.\""
show bri with dis1
show bri talking with dis
br "\"Then I have my excellent engineer, who fought tooth and claw to be here. He crossed a whole damn ocean, in fact.\""
show bri eyes with dis1
show bri eyes talking with dis
br "\"Of course, he’s still a chink, through no fault of his own. That means he will sell me out to the highest price one day.\""
show bri with dis

"Briggs pulls a gun from his breast pocket."
show bri talking with dis
br "\"You want one last chance to fix this Ben?\""
show bri with dis
show ben talking with dis
ben "\"Yes sir.\""
show ben with dis
"Ben gulps as he looks into the barrel pointed at his head."
show ben talking with dis
ben "\"I want to make this right, sir.\""
show ben with dis
"Briggs stares at him and nods, dipping his nose down twice."
show bri talking with dis
br "\"Now then, this is your last chance. You hear me right?\""
show bri with dis
show ben talking with dis
ben "\"Yes sir. I do hear you.\""
show ben with dis
show bri eyes talking with dis
br "\"This will be an act of trust.\""
show bri with dis
show ben talking with dis
ben "\"...Yes sir.\""
show ben with dis
show bri smile talking with dis
br "\"Very good.\""
show bri smile with dis
"He twirls the gun playfully in his hand."
show bri smile talking with dis
br "\"Let me tell you a little secret about my gun.\""
show bri smile with dis1
show bri smile talking with dis
br "\"You see, it has room in the barrel for six bullets, but I only put in one.\""
show bri smile with dis
show ben talking with dis
ben "\"...Why just one?\""
show ben with dis
show bri smile talking with dis
br "\"Well that’s very good, Ben. I thought you’d ask...\""
show bri with dis
"He crouches down to his knees to meet Ben face-to-face."
show bri talking with dis
br "\"I think about it like this. Bullets are expensive, yeah?\""
show bri with dis
show ben talking with dis
ben "\"...yeah.\""
show ben with dis
show bri talking with dis
br "\"If I find myself in a sticky situation... well, I’ve already lost if my own boys are down.\""
show bri with dis1
show bri talking with dis
br "\"Sure I’d be able to take somebody down with a single bullet. But pistols ain’t that quick. And it just takes one more person in a gun fight to get their opportunity.\""
show bri eyes smile with dis
"He shakes his head and chuckles."
show bri talking with dis
br "\"No, that one bullet is for me.\""
show bri with dis
show ben talking with dis
ben "\"...why?\""
show ben with dis
show bri talking with dis
br "\"Because nobody hates losing more than a man after his revenge.\""
show bri with dis
"Briggs gives Yao a look."
show bri talking with dis
br "\"Now for the next secret.\""
show bri with dis1
show bri talking with dis
br "\"I’m no sharpshooter.\""
show bri with dis1
show bri talking with dis
br "\"Doesn’t mean I haven’t hunted in my time, but that’s not the same as being a professional mankiller.\""
show bri with dis1
show bri talking with dis
br "\"I like to be careful with my gun...\""
show bri with dis
show ben talking with dis
ben "\"Careful how?\""
show ben with dis
show bri talking with dis
br "\"I wouldn’t want the damn thing going off on my person if I go about hiding it in my breast pocket.\""
show bri with dis1
show bri talking with dis
br "\"That would be a very stupid, very messy end.\""
show bri with dis1
show bri talking with dis
br "\"Don’t you agree?\""
show bri with dis
show ben talking with dis
ben "\"Yes sir. Very stupid.\""
show ben with dis
show bri talking with dis
br "\"So the second secret about this gun that I carry is that the first barrel is empty.\""
show bri with dis
"He turns the gun around in his paw and holds it up to Ben."
show bri talking with dis
br "\"This here will be an act of trust.\""
show bri with dis1
show bri talking with dis
br "\"If you shoot the chink, I’ll promote you to foreman.\""
show bri with dis3
show yao sidelook with dis3
"Ben looks at the gun in his hand that Briggs hasn’t let go of yet, then at the tiger, whose expression is impossible to read with his cap hiding his eyes."
show ben talking with dis
ben "\"Really?\""
show ben eyes with dis
show bri talking with dis
br "\"Yes. Really.\""
show bri with dis
"He still hasn’t let go of the gun."
show bri talking with dis
br "\"But first, ah, you gotta do something for me.\""
show ben with dis3
show bri with dis3
show yao -sidelook with dis3
"The smile on Ben’s face slowly fades."
show ben talking with dis
ben "\"Yeah?\""
show ben with dis
show bri talking with dis
br "\"Yeah.\""
show bri with dis1
show bri talking with dis3
show nik surprised with dis3
br "\"Put the gun in your mouth.\""
show bri with dis
show ben talking with dis
ben "\"...What?\""
show ben with dis
show bri talking with dis
br "\"I said.\""
show bri with dis1
show bri talking with dis
br "\"Put the gun.\""
show bri with dis1
show bri talking with dis
br "\"Inside your mouth.\""
show bri with dis1
show bri talking with dis
br "\"And fire the empty chamber.\""
show bri smile with dis

"He pats the other dog on the shoulder and stands."
show bri with dis
"Ben stares at the gun."
show ben talking with dis
ben "\"B-but...\""
show ben with dis1
show ben talking with dis
ben "\"Won’t it still hurt...?\""
show ben with dis
show bri talking with dis
br "\"Probably.\""
show bri with dis1
show bri talking with dis
br "\"But you’ll live.\""
show bri with dis
"Ben stares at the gun some more."

"His hand moves towards the barrel."
show bri talking with dis
br "\"Ah ah ah.\""
show bri with dis
"Ben’s hand freezes."
show bri talking with dis
br "\"Remember. This is an exercise in trust.\""
show bri with dis1
show bri talking with dis
br "\"If you open the barrel, I’ll have these gentlemen shoot you where you sit.\""
show bri smile with dis1
show bri smile talking with dis
br "\"So!\""
show bri with dis1
show bri talking with dis
br "\"Will you walk the path of better men, or will you miss your final chance, Ben?\""
show bri with dis1
show bri talking with dis
br "\"That’s the question I’m asking you tonight.\""
show bri with dis

"He’s trembling."

"Yao is perfectly still."

"He looks perfectly calm for a man who was just given the permission to be murdered."

"I don’t envy Ben’s position."

"But Briggs is right."
"If there is a bullet in that gun, he doesn’t have a chance."

"But Ben holds up the gun and points it at himself."
show eli serious with dis
m "\"Don’t do it.\""

"Ben pauses."
show eli talking with dis
badeli "\"Should I shut him up?\""
show eli -talking with dis
show bri talking with dis
br "\"Let him speak.\""
show bri with dis1
show bri talking
show eli -serious
with dis
br "\"It’s a free country.\""
show bri with dis1
show ben talking with dis3
"Ben's eyes narrow and he opens his mouth."
show ben annoyed with dis
m "\"You put that gun in your mouth and you’ll die, idiot.\""

ben "\"Who the fuck you callin’ an idiot?\""

m "\"You!\""
m "\"You idiot!\""
ni "\"If you pull that trigger you’ll die!\""
show ben angry with dis
ben "\"Y’all don’t know that!\""
show ben annoyed with dis
m "\"Of course we do.\""

m "\"He’s toying with you.\""


ben "\"Y’all just want to save your associate.\""

m "\"Nik wants to save you, you stupid asshole.\""

m "\"I don’t care what you do.\""

ben "\"Good then, because I’m gonna do it.\""
show ben talking with dis2
"He opens his mouth wide and slides his mouth over the gun."
ben "\"Boss!\""
ben "\"I’m trusting you!\""
play sound ("sfx/wgun.ogg")
play sound2 ("sfx/thud3.ogg")
show white with dis1
show nik shocked at dark2:
    xpos 1.16
    yalign 1.0
hide ben
hide benmud
hide white
with dis
"Just like before, I see the flash of the shot and the splatter before I hear it."
stop sound
stop sound2
show nik surprised with dis3
"Briggs plucks a handkerchief from his pocket, kneels, wipes his boots, then throws it on Ben’s still spasming body."
show bri talking with dis
br "\"His last chance there was to shoot me.\""
show bri smile with dis
"He stands back up and clasps his paws together."
show bri smile talking
show eli smile
with dis
br "\"Didn’t say that it was a good chance because my associates here would have got him first, but still a chance.\""
show bri with dis
show eli angry serious with dis
m "\"What do you--\""
show bri talking with dis
br "\"You speak when I ask you to speak.\""
show bri with dis1
show bri talking with dis
br "\"Understood?\""
show bri with dis
"I still feel my blood dripping to the ground when I nod."
show bri talking with dis
show eli -serious -angry with dis
br "\"Good.\""
show bri with dis1
show bri talking with dis3
show yao -crossed with dis3
br "\"Check them for weapons.\""
show bri with dis
"Wolf" "\"The chink too?\""
show bri eyes talking with dis
br "\"Of course the chink too. Don’t be stupid.\""

show bri with dis1
show bri talking with dis
br "\"Raise your hands or I’ll put a hole through the white faggot’s head, no questions asked.\""
show bri with dis3
show nik sidelook with dis3
show yao sidelook with dis3
"Yao and Nik don’t hesitate."

"I lift mine as well. A few specks of my own blood hit my forehead."
play sound ("sfx/gunload.ogg")
show eli serious at centerright,transparent with dis3
"The wolf aims his guns at us while the badger pats us down, one by one."
show yao -sidelook with dis3
show eli eyes talking with dis
badeli "\"They’re clear.\""
show eli -eyes -talking with dis
stop sound

show bri at centerleft,transparent with dissolve
show bri smile talking with dis
br "\"I have to say Mr. King, Mr. Yaolin, I respect ambition more than any other quality in a man.\""

show bri with dis1
show bri talking with dis
br "\"Of course, we’ll probably end up killing each other one day, but that certainly doesn’t have to be this day.\""
show bri with dis1
show bri talking with dis
br "\"You saw nothing. I saw nothing. And the three of you leave me today with fat pockets.\""
show bri smile with dis1
show bri smile talking with dis
br "\"How’s that for a sweet deal?\""
show bri with dis

ni "\"...\""

ya "\"...\""
show bri smile with dis
m "\"...sounds good.\""

"If true."
show bri smile talking with dis
br "\"Then we strike an accord.\""
show bri smile with dis1
show bri smile talking with dis
br "\"...I have just one last condition.\""
show bri smile with dis
"Oh, here it comes."
show bri talking with dis
br "\"See these wires on the ground?\""
show bri with dis
"I look down."

"There’s dozens of strands going this way and that way."

"At least ten go behind me into the tunnel."

"Three go over the bridge."
show bri talking with dis
br "\"If you want any money, all you have to do is light one of the fuses...\""
show bri with dis1
show bri talking with dis
br "\"I don’t care which fuse or where you do it from.\""
show bri eyes with dis1
show bri eyes talking with dis
br "\"I don’t even care if just one of the three of you does it.\""
show bri with dis1
show bri talking with dis
br "\"Hell, I’ll even turn around if you’re concerned with me seeing who does it...\""
show bri with dis1
show bri talking with dis
br "\"Nobody ever has to know who struck the match.\""
show bri eyes with dis1
show bri eyes talking with dis
br "\"Nobody aside from yourselves. And the gentlemen with the guns who will watch you.\""
show bri smile with dis1
show bri smile talking with dis
br "\"Consider it!\""
show bri smile with dis
m "\"What does lighting a fuse do?\""
show bri smile talking with dis
br "\"It just starts a little fire.\""
show bri smile with dis1
show bri smile talking with dis
br "\"Somewhere.\""
show bri smile with dis1
show bri smile talking with dis
br "\"Someplace.\""
show bri smile with dis1
show bri smile talking with dis
br "\"And those little fires light someplace else too.\""
show bri with dis3
show nik talking with dis3
ni "\"Why do you think we would consider doing such a thing?\""
show nik neutral with dis
"Briggs shakes his head and whistles."
show bri talking with dis
br "\"I have two reasons in mind.\""
show bri with dis1
show bri talking with dis
br "\"The first is, as workers in this fine mine, I believe you’re all intimately familiar with how much of a blight the Hendricks family is on this town.\""
show bri with dis1
show bri talking with dis
br "\"The current patriarch has no sense of how to run a mine, or a business in general.\""
show bri with dis1
show bri talking with dis
br "\"He consumes half of our hard-earned labor on all manner of toys and finery rather than what’s needed to expand our facilities, or to attract necessary new talent.\""
show bri with dis1
show bri talking with dis
br "\"Fortunately for us, the current Hendricks family’s lack of knowledge on the elaborate underground tunnels that James the First started and James the Second continued leaves them sitting ducks.\""
show bri with dis1
show bri talking with dis
br "\"So we’re gonna burn the rot straight out of the town.\""
show bri with dis
show nik talking with dis
ni "\"So you’re killing them?\""
show nik neutral with dis
show bri talking with dis
br "\"I’m sending them packing at the very least.\""
show bri eyes with dis1
show bri eyes talking with dis
br "\"If they happen to perish in the conflagration, well, that’s just a bonus.\""
show bri with dis


show nik talking with dis
ni "\"...Why {i}us{/i}?\""
show nik neutral with dis
show bri smile talking with dis
br "\"Because you are extremely lucky sons of bitches for one.\""
show bri smile with dis
play sound ("sfx/thud8.ogg")
"He kicks over Ben’s still-twitching corpse."
show bri smile with dis1
show bri smile talking with dis
br "\"You have a patsy.\""
show bri smile with dis1
show bri smile talking with dis
br "\"That means your oriental friend over there leading you down here doesn’t mean you have to die after all!\""
show bri smile with dis
"Judging by Nik’s face, he doesn’t believe it at all."


if SNY_Points >0:
    "But there’s something else going on."
    "If Yao is the one playing Briggs right now, he’s the most dangerous man in the room."
    "And I don’t know how to feel about that just yet."
    #

else:
    "But I fuckin’ knew it."
    "Everybody worships the same God at the end of the day, and that God is money."
    #

show bri smile talking with dis
br "\"Now that means if you don’t give me any trouble, the three of you can leave richer than you ever have been in your filthy lives.\""
show bri with dis1
show bri talking with dis
br "\"Of course I could just shoot you all in the head and light the fuses myself.\""
show bri eyes with dis1
show bri eyes talking with dis
br "\"That works just as well, but this is much neater, and much safer.\""
show bri eyes with dis1
hide bri
hide eli
with dis3
"He turns around."
br "\"I’ll give you a couple of minutes. I trust you have matches.\""

$ renpy.music.set_volume(1.0, delay=3.5, channel='background')
stop music fadeout 2.5
"The three of us stand in place, legs stiff and stuck, like they’re made of cast iron."

"I lean in close to Nik, lowering my voice to a whisper."
show nik surprised with dis
m "\"...Should we do it?\""
"His ears wiggle."
show nik sad with dis3
ni "\"Sam, why would you say that?\""

m "\"’Cause he said we could light any of the wires.\""

m "\"The one across the bridge just goes to the mansion.\""

ni "\"I know where it goes.\""

m "\"Yeah but they’re {i}rich{/i} Nik.\""

ni "\"I don’t care.\""

ni "\"Seizing and redistributing their resources is one thing...\""
show nik surprised with dis3
ni "\"But arson?\""

ni "\"There are servants in the house.\""
show nik sidelook with dis
ni "\"A wife. A child.\""
show nik sad with dis3
"He looks at the floor."

"Ben’s body has finally stopped twitching."

ni "\"No more death, Sam.\""

ni "\"...Not on my part.\""

m "\"He might kill us if we walk away without lighting anything.\""

ni "\"He might kill us even if we don’t.\""

m "\"Fair point.\""

"If Ben’s death could teach me one meaningful thing, it’s that Briggs himself doesn’t want us to play this game."

"He wants to see if we can find an out."

"We need an out, or else we lose."

"The harder my heart pounds, the hazier I feel."
play sound ("sfx/clothrustle.ogg")
show yao sidelook crossed with dis3
"I hear Yao rustling through his pockets."
stop sound
ya "\"I will light the wire in the corner.\""

ya "\"I have no more reason to hide my actions.\""

if SNY_Points >0:
    hide yao with dis3
    "Wait."
    "I remember that corner now."
    "I remember what’s there."
    #

else:
    show yao -sidelook -crossed with dis3
    m "\"So that’s how it is, huh?\""
    "The tiger pauses for a moment."
    hide yao with dis3
    "But he doesn’t answer me."
    m "\"Un-fucking believable.\""
    #

m "\"Nik.\""
"I can hear myself breathing as hard as I can."
ni "\"What?\""
show nik neutral with dis3
m "\"Give me a match.\""
show nik talking with dis3
ni "\"No.\""
show nik neutral with dis
m "\"Just trust me on this okay?\""
show nik eyes with dis
"He slips out the box of matches in his pocket and places them in my good hand."
show nik neutral with dis1
hide nik with dis3

"I fumble with the box a bit, {nw}"
show eli suspenders s serious hip at centerleft,dark2 with dis3:
    xzoom-1
extend "noticing the wolf and the badger still staring at me as I get a little bit closer to the wires that go toward the Hendricks manor."
#sfx
"My hands shake as I take out a match from the cardboard package and strike it against the side."
play sound ("sfx/match.ogg")
"It takes me a few times to get the motion right until I see light and feel heat against my face."
stop sound
"I swagger forward to the right cord on the ground."

"I get down on one knee."

"And I look at both of the bodyguards above me."

m "\"Alright then.\""

show eli surprised with dis
m "\"Watch.\""
show white with dis1
hide eli
hide white
with dis3
play sound ("sfx/ignite.ogg")
"The match lights the fuse of the line even quicker than a wick of dynamite."
stop sound
"I know it’s going to whizz across that bridge like an evil ghost, gliding over a swamp, damning the ones it chases and bringing long-deserved ruin to the children of long-gone benefactors of countless misdeeds."
"At least, that’s how I picture it in my mind."

"Because I don’t have the time to watch."
$ renpy.music.set_volume(0.35, delay=3.5, channel='background')
"I figure they’re going to turn their heads for less than half a second."

play music ("music/tension.ogg")
play sound ("sfx/thud2.ogg")
"And that’s all the time I have to use my left leg to launch myself off the ground and into the chest of one of the gunmen." with hpunch
play sound ("sfx/thud5.ogg")
"I hear the wind leave his lungs as I topple him over, bleeding on him."
stop sound
"I only have seconds before the other shoots me."
play sound ("sfx/ygun3.ogg")
show white with dis1
hide white with dis
"But I hear the shot."
stop sound
"Though by some miracle, I’m not in pain."

"I don’t have time to look, but Nik is beside me."
play sound ("sfx/thud6.ogg")
"He helps me wrestle the gun from the wolf, and we beat him in the head."
stop sound
"He goes limp. Blood trickles from his nose."
show yao angry h at left,dark2 with dis3:
    xzoom-1
"Yao is standing over the other man with a smoking pistol in his hand."

"The badger is bleeding from his hand, just like I am."

"I put together that Yao is the one who shot him."
show yao teeth with dis
ya "\"Everything I have done...\""
play sound ("sfx/ygun1.ogg")
show white with dis1
hide white with dis
"A shot."

ya "\"Led to this moment...\""
play sound ("sfx/ygun2.ogg")
show white with dis1
hide white with dis
"Another shot."


ya "\"Every laugh I have endured...\""
play sound ("sfx/ygun3.ogg")
show white with dis1
hide white with dis
"Then another."
ya "\"Has been for one. Single. Scream.\""
stop sound
show yao angry
show eli suspenders s fury angry at halfright,dark2
with dis3
"But the badger is up again, {nw}"
play sound ("sfx/thud.ogg")
hide yao
hide eli
extend "tackling Yao to the floor." with hpunch
play sound ("sfx/ygun1.ogg")
show white with dis1
hide white with dis
"Yao falls, and there’s another shot."
#sfx?
"I hear something wet, then a howl of pain."
"Something long, thin, hairy, and bloody lies on the floor."
"If I didn’t know better, I’d say it looked like Brigg’s tail."
"Nik rushes on over to help Yao, but he doesn’t need the help by the time Nik gets there."
"Yao’s claws are out, leaving deep gashes in the badger’s arms as he fights for control of the rifle, until he can wrestle it out of his arms."
play sound ("sfx/thud2.ogg")
"As Yao starts beating the other gunman with the back of his rifle, we hear the sizzling sound of wire again."
m "\"Nik, the fuse!\""
play sound ("sfx/minerun.ogg")
"Nik races for it across the rope bridge, pulling a pair of shears from his pocket and cutting it."
"I exhale loudly as my spark goes out, knowing my part in any of this won’t lead to needless harm."
stop sound
play sound2 ("sfx/elevatorengineloop.ogg")

"Then we hear the elevator {nw}"
stop sound2 fadeout 10.0
extend"operating."

play sound ("sfx/ygun3.ogg")
show white with dis1
hide white with dis
show yao angry h at left,dark2 with dis3:
    xzoom-1
"Yao shoots at the bottom of it as it ascends."
stop sound
show yao teeth with dis
"Then he curses."
show yao angry with dis3
show nik angry h at right,dark2 with dis3
$ renpy.music.set_volume(1.0, delay=3.5, channel='background')
stop music fadeout 2.5
m "\"Yeah, you better run!\""
m "\"We stopped the fire, asshole!\""
"A pained voice howls back at me."
show nik surprised with dis3
br "\"We started the mansion fire an hour ago, dumbass!\""
m "\"...huh?\""

"He laughs an awful laugh. It doesn’t sound like it should belong to him."
stop background fadeout 3.0
play sound ("sfx/jamesexplosionmine.ogg")
"Then I hear an explosion come from the other side of that bridge." with vpunch

"For just a moment, my heart stops."
stop sound
"Nik is looking at the floor, as if panicked to realize something."
show yao shocked with dis
ni "\"...He lit the other wires too!\""
play ambient ("sfx/caveinloop.ogg") volume 0.6 fadein 2.5
#shake
show bg cavebridge at my_shake2:
    zoom 1.003
show nik shocked at my_shake2
show yao shocked at my_shake2,transparent
with dis3
play sound ("sfx/mine explosion.ogg")
"We hear more explosions."

"Behind us."
play sound ("sfx/mine explosion 2.ogg")
"In front of us."

scene bg cavebridge
show nik shocked h at right,dark2
show yao shocked h at left,dark2:
    xzoom-1
with dis3
"All around us!"
play music ("music/runfool.ogg")
show nik angry with dis3
ni "\"{i}Podpalacz!{/i}\""
stop sound
"His voice shouts up at the elevator."
show yao sidelook with dis3
"But he’s so far away I doubt he can hear what Nik is saying."

show nik surprised with dis3
m "\"How the hell are we gonna get out without the elevator?\""
show yao angry with dis
ya "\"I placed a rope ladder behind the shaft while I fixed the elevator.\""



ni "\"Won’t he shoot us if we climb?\""

ya "\"He left his pistol and he’s bleeding.\""

ya "\"I think he intends to live rather than die taking us out.\""
play sound ("sfx/holster1.ogg")
"He picks up the gun on the floor and puts it in his holster."
hide yao with dis3
"Then he walks up to the shaft and tugs on something in the dark that I can barely see."
stop sound

ya "\"We can climb it if we hurry!\""

"Yao goes up first."
scene bg mineelevatorascent with dis3
"I move so quickly I almost get my face hit by his tail, but he’s just as fast of a climber."

"Nik follows."

"I expect the rope to sway with our combined weight, but it’s bolted to the face of the rock."

"...Yao planned ahead for this."

"We make our way to the middle of the rope without incident."
play sound ("sfx/ignite2.ogg")
"Until I hear another explosion down below." with vpunch

"The bridge to the Hendricks manor is on fire."
stop sound
"Flames swallow the sides of it, singing the connections as the abyss swallows it greedily."

"I’m so distracted by the sight I almost don’t hear Nik and Yao both yelling at me."

ni "\"Body against the wall!\""

ya "\"NOW!\""

scene bg black with dis
"The elevator rushes down on us from above."
play sound ("sfx/elevatorfall1.ogg")
"I feel the wind of it as it passes me by, faster than it should be going, as it smashes against the floor."
scene bg mineelevatorascent with dis3
ya "\"DO NOT STOP MOVING!\""
play sound ("sfx/jamesexplosionmine.ogg") volume 0.4
"I hear more explosions." with vpunch

"But all we can do now is climb."

"And climb."

"And climb."
stop ambient fadeout 4.0
scene bg minenook
show yao sidelook h at center,dark2:
    xzoom-1
with dis3
"Once I’m finally at the top, Yao pulls me up by my wrists to get me out of the way faster, so he can get Nik up next."
show nik disappointed h at dark2 with dis3:
    yalign 1.0
    xpos 0.62
m "\"I’m surprised he didn’t cut the rope ladder.\""
show yao teeth crossed with dis3
show nik surprised with dis3
"For the first time, I hear the tiger growl, leaning over a puddle of gore and holding up the fray of the ladder."
ya "\"He did.\""
show yao angry crossed with dis
ya "\"I bolted it into the rock in eight different places, so it would not fall.\""
show yao angry -crossed with dis3
"He pinches the blood on the floor between his claws."

ya "\"If we follow the blood we will find a way out.\""
show nik sad with dis3
ni "\"Don’t follow him...\""
ya "\"Why?\""
show nik surprised with dis3
ni "\"It’s too dangerous!\""
ni "\"There are other ways out of the mine, and we need to warn people who might be inside that there’s a fire below!\""
"Yao looks like he’s about to bolt off in the direction of the blood, {nw}"
show yao teeth with dis
extend "when he hears somebody running down the tunnel."
hide yao with dis3
"The tiger hides around a corner, pulling the gun from his pocket."
scene bg mautunnel2
show nik surprised h at dark2:
    yalign 1.0
    xpos 0.62
with dissolve
show mel eyes at left,dark2:
    xzoom-1
show bli shocked at dark2:
    yalign 1.0
    xpos 0.1
    xzoom-1
with dis3
ni "\"...little girls?!\""
show nik shocked with dis3
ni "\"You shouldn’t be down here!\""
show bli angry with dis
blunk "\"Shit, who says we wanted to be?\""
show nik surprised with dis3
blunk "\"Can’t you see my friend is barely conscious?\""
m "\"What’s your names?\""
show bli a squints grit at dark2 with dis3:
    yalign 1.0
    xpos -0.035
blunk "\"Who the hell is askin’?\""
blunk "\"That sure as shit doesn’t matter right now! We need to get OUT!\""

if SNY_Points ==0:
    play sound ("sfx/minerun.ogg")
    "Yao bolts past us, breaking into a run, following the direction of the blood."
    m "\"Goddamnit!\""
    stop sound
    blunk "\"And who the hell was that?\""
    m "\"The reason why we were here, is who!\""
    ni "\"He’s a companion. We’re all also trying to get out!\""
    m "\"We should go after him.\""
    show nik sad with dis3
    ni "\"He’ll get out on his own.\""
    show nik surprised with dis3
    ni "\"We should help them get out.\""
    #

else:
    play sound ("sfx/minewalk.ogg")
    show yao h at centerright,dark2 behind nik with dissolve
    ya @talking "\"I know who you are.\""
    show bli a squints with dis
    "The cat sizes him up."
    stop sound
    show bli a squints grit with dis
    blunk "\"Sure as hell don’t know who you are, but ok!\""
    show yao talking crossed with dis3
    ya "\"I have seen you before, marking the tunnels.\""
    show yao -talking with dis1
    show yao talking with dis
    ya "\"You know extra ways out.\""
    show yao -talking with dis
    #

show bli angry at dark2 with dis3:
    yalign 1.0
    xpos 0.1
    xzoom-1
blunk "\"...Why are y’all talkin’ like this is urgent?\""
ni "\"Because there’s a fire down below!\""
show bli shocked with dis
"The cat’s eyes widen."

blunk "\"From which direction?\""
ni "\"The Hendricks manor!\""
blunk "\"Shit, so that’s why he ran away!\""
show bli angry with dis
blunk "\"Oh God damn it, that means we can’t make it to the lake.\""

if SNY_Points ==0:

    m "\"How do you know where we should go?\""
    "She ignores me completely."
    #

show bli squints talking with dis
blunk "\"I do know a way that goes out by the railroad.\""
show bli squints with dis1
show bli squints talking with dis
blunk "\"There’s a maniac on the loose down here.\""
show bli angry with dis
blunk "\"Help watch our backs.\""
show bli eyes with dis
"She nods at the woolly-furred rabbit hanging onto her arm."
show bli angry with dis
blunk "\"And I’ll get you there.\""
blunk "\"We got a deal?\""
show nik disappointed with dis3
ni "\"So long as we stop and warn any of the workers on our way out.\""
show bli a squints at dark2 with dis3:
    yalign 1.0
    xpos -0.035
blunk "\"Shit!\""
show nik neutral with dis3
blunk "\"We ain’t got time for all that!\""

if SNY_Points ==0:
    show nik disappointed at center,transparent behind bli with dis3
    show bli angry at dark2 with dis3:
        yalign 1.0
        xpos 0.1
        xzoom-1
    "Nik walks over to the rabbit girl."
    ni "\"Put her on my back.\""
    play sound ("sfx/clothrustle.ogg")
    show bli eyes
    hide mel
    with dis3
    "The black cat hoists the rabbit onto Nik’s back."
    stop sound
    show bli angry with dis3
    show nik sidelook with dis3
    "He holds her legs and whispers to her."
    #

else:
    show deepmine with dis3:
        alpha 0.4
    m "\"Arguin’ about... {nw}"
    show nik surprised with dis3
    show yao eyebrows with dis3
    show bli shocked at dark2 with dis3:
        yalign 1.0
        xpos 0.1
        xzoom-1
    hide deepmine with dis3
    extend"all this...\""
    m "\"Ain’t really... {nw}"
    show deepmine with dis3:
        alpha 0.7
    extend "savin’ any... time...\""
    "There’s a weird rush inside my head."
    hide deepmine with dis2
    "The scar on the back of my head hurts again for some reason."
    ni "\"Are you alright Sam?\""
    m "\"Yeah I just...\""
    $ renpy.music.set_volume(0.2, delay=0.5, channel='music')
    show yao shocked with dis
    show black with dis
    "The world goes sideways."
    "I try to stand up with it but feel like I’m falling."
    show yao sad with dis3
    "I expect the sudden hard, painful, gritty slam that comes after you make a fool of yourself."
    "But it never comes."
    hide black with dis2
    "I feel damp fur and strong muscle grip me and then put me over an arm."
    $ renpy.music.set_volume(1.0, delay=10.0, channel='music')
    show yao sidelook with dis3
    ya "\"You lost a lot of blood.\""
    ya "\"You do not need yet another injury.\""
    m "\"What’s... that supposed to mean?\""
    play sound ("sfx/clothrustle.ogg")
    show nik sidelook with dis3
    "Nik slides in next to me."
    stop sound
    #

#check
ni "\"{cps=15}{i}Oh hop, hop, you lush herb,\nthere will be no wedding without you.{/i}\""
show bli squints with dis3
"The cat gives him a funny look."
show bli with dis
"But I can tell from the look on Nik’s face that he’s remembering something."
"Probably something he’s never told me about."
"Something I don’t need to know, that’s just for him."
"He picks up his pace and the girl speeds up with him to match him."
show bli angry with dis
blunk "\"This way!\""
scene bg mautunnel1 at dark2 with dis3
"I see a bit of paint on the rock wall as she leads us down a passageway I hadn’t seen before."

"It doesn’t exactly look finished, and there isn’t any mine railing on the floor."
play sound ("sfx/mine explosion.ogg") volume 0.2
"We feel another explosion." with vpunch


if SNY_Points ==0:
    "I hear multiple screams as I feel the tunnels shake and lose my footing."
    "The girl on Nik’s back chokes out a sob."
    stop sound

else:
    play sound ("sfx/thud.ogg")
    "I stumble again and lose my footing, nearly pulling the two of them down with me." with hpunch
    stop sound
    "But they stand resolute, in spite of my weight, and in spite of the smothering scent of our sweat, our blood, of smoke and fire."
    #

ni "\"{cps=15}{i}Oh hop, you poor thing\nMay God help you, oh poor hop.{/i}\""

if SNY_Points ==0:
    "The rabbit clings harder to the badger’s back."
    #
"Beams of light shine through the cave walls as we climb."
scene bg mausoleumexit with dis3
"Then we come to the end of the tunnel."
m "\"It’s a dead end!\""
scene bg mausoleumexitopen
show bli squints at right,dark2
with dis3
play sound "sfx/scrape2.ogg"
"The cat walks over and knocks a piece of plywood to the side, gesturing to it and looking at me like I’m slow."
stop sound
if SNY_Points ==0:
    show nik disappointed h at left,dark2 with dis3:
        xzoom-1
    "Nikolai hunches to let the rabbit {nw}"
    show mel fear at center,dark2 with dis3
    extend "off of his back."
    show nik eyestalking with dis3
    ni "\"See now? You are perfectly safe.\""
    show nik neutral with dis1
    hide mel
    hide nik
    #
hide bli
with dis3

"The girls go first."
"I see the cat hop strategically to the side for some reason as she goes through the passage and it doesn’t take me long to see why."
stop music fadeout 3.5
scene bg mausoleum2 with dis3
if SNY_Points>0:
    "I almost stumble again against something squishy on the floor."
else:
    "I almost stumble against something squishy on the floor."

m "\"The hell?\""
show bli shocked at left,dark2 with dis3:
    xzoom-1
blunk "\"Yeah, that’s a whole man.\""

"I blink and look down."

"It’s a familiar looking fox with tawny fur."

"Though I’m not sure if I can place where he’s from."

if SNY_Points >0:

    "I think I saw him serving drinks at the Stag."

    m "\"Ain’t this the barkeep over at that place y’all took me to?\""
    show yao sidelook crossed h at right,dark2 with dis3
    ya "\"I have seen him there, yes.\""
    show yao talking with dis3
    ya "\"He has helped some people into the town who would otherwise not be able to find themselves here.\""
    show yao -talking with dis1
    show yao talking with dis
    ya "\"It makes sense that he would know a connection from the train to the tunnels.\""
    show yao -talking with dis
    #
m "\"He dead?\""
if SNY_Points >0:
    show nik disappointed h at halfright,dark2 behind yao with dis3
else:
    show nik disappointed h at right,dark2 with dis3
ni "\"Will be soon if we leave him here in the way of the smoke.\""
show bli sideeye with dis
blunk "\"That guy gets beat up all the time.\""
blunk "\"I’ve seen him passed out in all sorts of places.\""
show bli with dis
"I’m not gonna bother askin’ any number of the many questions in my head, so I opt to leave it be."
show nik sidelook h with dis3
ni "\"I’ll drag him outside.\""
hide bli with dis3
hide nik with dis3
if SNY_Points >0:
    hide yao with dis3
$ renpy.music.set_volume(0.2, delay=0.0, channel='background')
"I drag myself out, still just as dizzy as before, expecting to have to shield my eyes from the sun."
scene bg cemetary2fire with dis3
#music
play background ("sfx/burning.ogg") fadein 4.5
"But instead, the sky is red as can be."
"Smoke is in the air, and I can see flames in the distance, coming all the way from the hilltop."
scene bg trainstationfire with dis3
play music ("sfx/reverb.ogg") fadein 4.5
"I can see a crowd amassing at the train station, likely clamoring for tickets in a frantic buzz."

m "\"Holy shit.\""
"My eyes are watering and my nostrils feel like they’re irritated."

"I cover my mouth and nose with my shirt because there’s so much smoke in the air already."
show wil sideeyes at center,bonfire with dis3
"But I’m also glad to see a familiar face."
show wil surprised with dis3
m "\"William!\""
wi "\"Sam!\""
m "\"The hell happened to your tooth?\""
wi "\"The hell happened to your hand?\""
m "\"...Long story.\""
show wil sideeyes with dis3
wi "\"Same for me.\""
wi "\"The Hendricks manor caught aflame right after the National Guard calmed down.\""
show wil with dis3
m "\"...Did everybody make it out?\""
show wil talking with dis
wi "\"We’re not sure yet.\""
show wil with dis1
show wil talking with dis
wi "\"James Hendricks is still missing.\""
show wil frustrated with dis3
wi "\"The Guard’s still hauling buckets up and down from Lake Emma to put it out.\""
wi "\"Doubt they’ll save downtown though.\""
"I feel myself seize up."
show wil with dis3
m "\"Downtown’s on fire too?!\""
show wil eyes talking with dis
wi "\"Just about everywhere in Echo is.\""
show wil with dis1
show wil talking with dis
wi "\"Seems like it started because of a connected underground fire.\""
show wil sideeyes with dis3
wi "\"...At least for most of the places, as far as we can tell.\""
show wil with dis
"Shit."
play sound ("sfx/foreststep.ogg")
show nik sad h at bonfire with dis3:
    yalign 1.0
    xpos 0.6
"We couldn’t stop it."
stop sound
show nik with dis3
show wil with dis3
m "\"Nik...\""
m "\"Will...\""
show wil surprised with dis3
show nik surprised with dis3
m "\"I gotta go back into town.\""
ni "\"But the fire’s worse there!\""
m "\"I need to check on the Madam.\""
wi "\"What?\""
m "\"She was good to me.\""
m "\"She looked after me.\""
show wil with dis
m "\"I could have run away a thousands times, and I would have, but I can’t leave her like this!\""
show nik disappointed with dis3
ni "\"She’s got people, Sam.\""
m "\"I’m her people!\""
show nik angry
ni "\"SO ARE WE, DAMN YOU!\"" with vpunch
#sfx
m "\"I’ll be back, okay?\""
hide nik
hide wil
with dis3
m "\"I’ll be back!\""
$ renpy.music.set_volume(0.35, delay=2.5, channel='background')
scene bg desertfire with dis3
"Everything everywhere looks bathed in red light from the smoke and the firelight."
"If I didn’t know better, I’d say it feels like the end of the world."
"In a way, it is the end of the world for most of the people who live here."
"Most folks walking on the road past me have bags, or suitcases, and they’re moving in the opposite direction."
$ renpy.music.set_volume(0.7, delay=2.5, channel='background')
scene bg echobackalleyfire with dis3
"From here I can see town hall is torched."
"The upper scale menswear store had its glass kicked in."
"I’m surprised that the last printing press in town looks like the only thing I can recognize that hasn’t caught fire yet."
"That and Red’s General store."
"The Hip, however..."
scene bg saloonfire with dis3
"It wasn’t so lucky."
"I arrive just in time to see one of the artisan glass windows shatter from the pressure of the heat."
"Men and women surround the place and townsfolk and guardsmen bring bucket after bucket of lake water."
"There are a few brothel girls I don’t recognize, standing around, crying their eyes out."
show dor cig profile serious at bonfire with dis3:
    yalign 1.0
    xpos 0.55
"I see Dora’s tall silhouette against the front of the flames, just a suitcase at her side, still smoking."

m "\"You’re safe!\""
show dor cig worried with dis
"She turns her head."

md "\"Sam?\""

md "\"I didn’t think I’d be seeing you again.\""

m "\"You probably wouldn’t have if things didn’t get so bad.\""
show dor cig profile squint with dis3
md "\"I guess that makes you a bad luck man.\""
show dor cig profile thinking with dis
"She smirks."
show dor cig profile squint with dis3
md "\"I hate to say it, but a part of me felt like we were always going to go down in flames.\""
show dor cig talking with dis3
md "\"I just didn't expect the whole damn town to go with us.\""
show dor cig with dis1
show dor cig talking with dis
md "\"I have my contingency plans Sam, but this is pretty goddamn bad.\""
show dor cig with dis
play sound ("sfx/impact1.ogg") volume 0.5
"The sign on the front of the Hip falls to the ground with a loud crash." with vpunch
show dor cig talking with dis3
md "\"Until then, we’ll find some way to hold the girls over.\""
stop sound
show dor cig with dis1
show dor cig talking with dis
md "\"We always do.\""
show dor cig worried with dis
md "\"But as stubborn as I am, even I have to admit that everything must come to a close one day.\""
show dor cig profile talking with dis3
md "\"It’s a bit ironic that the day that Harlan wanted most is the day he goes missing.\""
show dor cig profile with dis
m "\"Missing...?\""
show dor cig profile talking with dis
md "\"His office was cleaned out before the fire.\""
show dor cig profile with dis1
show dor cig profile talking with dis
md "\"He took off, as far as I know.\""
show dor cig profile with dis1
show dor cig profile talking with dis
md "\"It’s not exactly like him, but he hasn’t exactly been like himself for a very long time.\""
show dor cig profile thinking with dis
md "\"You know, I was going to leave Miss Tsosie the business, but a donation of matchsticks is hardly a gift.\""
show dor cig profile talking with dis
md "\"You haven’t seen her, have you?\""
show dor cig profile with dis
m "\"I told her to take a trip to Payton.\""
show dor cig profile talking with dis
md "\"Sounds like you had a feeling.\""
show dor cig profile with dis
m "\"Would you have left a few days ago if I told you I did?\""
show dor cig eyes with dis3
"She takes a drag on her cigarette."
"Then she blows."
show dor cig eyes talking with dis
md "\"Probably not.\""
show dor cig profile talking with dis3
md "\"But it would have been appreciated nonetheless.\""
show dor cig profile with dis
"I feel somebody walk up behind us."
play sound ("sfx/camera windup.ogg")
"He holds something up, which I realize a little too late is a camera."
play sound ("sfx/tumble.ogg")
"But I run out of the focus before he can take the shot."
play sound ("sfx/camera release.ogg")
show mur snapshot at left,bonfire with dis3:
    xzoom-1
m "\"The fuck are you doing?!\""
stop sound
show mur concerned d with dis3
mu "\"Just documenting the current damage of the Hip.\""
show mur fear d with dis
m "\"Don’t take any fucking pictures of me without my permission!\""
m "\"Especially not in front of property damage!\""
m "\"Y’hear?!\""
show mur concerned d with dis3
mu "\"Loud and clear, but it’s usually just to get figures for scale.\""
mu "\"This wasn’t meant to be for anything incriminating.\""
show mur sideeye with dis
mu "\"If it makes you feel better, you probably blurred the image.\""
hide mur with dis3
m "\"Whatever.\""
show dor cig with dis3
m "\"If everybody’s fine then I’m done here.\""
show dor cig talking with dis
md "\"If you’re headed to the station, could you carry an old woman’s bags?\""
show dor cig with dis1
show dor cig talking with dis
md "\"Just once more, for old time’s sake.\""
show dor cig with dis
m "\"...Sure.\""
show dor cig profile thinking with dis3
md "\"Very good.\""
md "\"You can have what’s in the front pocket.\""
show dor cig profile talking with dis
md "\"So long as you don’t open it until you get there.\""
show dor cig profile with dis
m "\"...Why?\""
show dor cig profile talking with dis
md "\"Because I’m not the sentimental type when it comes to goodbyes.\""
show dor cig profile thinking with dis
md "\"I’ll come find you in time. If I'm able.\""
hide dor with dis3
"I push the luggage cart, which is predictably heavy in spite of its wheels."
"I probably shouldn’t have taken Harlan for granted, considerin’ how willing he was to wheel her stuff around."
"But it does feel weird to know this will be the last errand I run for the Madam."
stop music fadeout 3.5
$ renpy.music.set_volume(0.2, delay=2.5, channel='background')
scene bg black with dissolve
scene bg trainstationfire with dis3
"Back at the station, the crowd has nearly doubled."
#sfx
"Thankfully, I hear chugging in the distance."

ni "\"Sam!\""

"Nik sees me before I see him."
show nik disappointed at bonfire with dis3:
    xzoom-1
    xpos -0.10
    yalign 1.0
ni "\"I got our tickets.\""
show nik talking with dis3
ni "\"We’re on our way out at the first arrival.\""
show nik smile with dis
ni "\"First class, too.\""
show nik neutral with dis
wi "\"Since when can you afford first class?\""
show wil at right,bonfire with dis3
m "\"Holy shit, William.\""

m "\"I didn’t even see you this time.\""
show wil eyes smile with dis
wi "\"Good to know I’m not rusty.\""
show wil with dis
m "\"It’s good I ran into you again anyhow.\""

m "\"...I gotta whisper somethin’.\""

"He tilts his ear my way."
show wil talking with dis
wi "\"Go ahead.\""
show wil with dis
m "\"I know the guy who did it Will.\""
m "\"Me and Nik both saw.\""
m "\"It was Briggs.\""
m "\"The other co-owner of the mine.\""
show wil frustrated with dis3
"Will chuffs."
show nik eyes with dis
wi "\"Well of course he did.\""
show nik neutral with dis3
show wil with dis3
m "\"...You knew?\""
show wil talking with dis
wi "\"Not that he was an arsonist, no.\""
show wil with dis1
show wil talking with dis
wi "\"Though, not like it matters much right now, when the first priority is putting out the fires.\""
show wil with dis
m "\"Can’t you arrest him now?\""
show wil eyes talking with dis
wi "\"It’s not like there’s anywhere we can jail him without a manhunt and hogtying him with rope.\""
show wil with dis1
show wil talking with dis
wi "\"Your suspect is involved in a whole lot of other situations that are time and case sensitive.\""
show wil sideeyes with dis3
wi "\"I wouldn’t tell anybody about it unless you have a considerable number of witnesses.\""
show wil frustrated with dis3
wi "\"Ain’t shit I can do about it until this reaches a federal court.\""
show wil with dis3
m "\"The hell is that supposed to mean?\""
m "\"You’re the sheriff!\""
m "\"So go on an’ sheriff!\""
show wil sideeyes with dis3
wi "\"Not much left to sheriff, Sam.\""

wi "\"Especially if both halves of the most important economic force are missing, and the place’s economy just burst into flames.\""

wi "\"This place is doomed.\""
show wil with dis3
m "\"But you’re still the law!\""

m "\"You’re still wearing your badge and everything!\""
show wil eyes with dis
play sound ("sfx/holster2.ogg") volume 0.6
"He plucks the badge off of his front pocket and tosses it to me."
show wil talking with dis
wi "\"Catch.\""
show wil with dis
play sound ("sfx/thud8.ogg")
"I snatch it as quick as I can out of the air to make sure it doesn’t drop."
stop sound
m "\"Why are you givin’ me this!?\""
show wil talking with dis3
show nik sidelook with dis3
wi "\"’Cause I resigned about an hour ago.\""
show wil with dis1
show wil talking with dis
wi "\"’I’m leaving what information I know for Mrs. Hendricks.\""
show wil with dis
m "\"What!?\""
show wil eyes talking with dis
wi "\"Keep it to remember me by.\""
show wil with dis1
show wil talking with dis
wi "\"Or just throw it away. It’s worthless copper.\""
show wil with dis
m "\"What the hell!?\""
show wil frustrated with dis3
wi "\"Don’t be so dramatic.\""
show wil talking with dis3
wi "\"You want to see me again?\""
show wil with dis1
show wil talking with dis
wi "\"Come find me in Payton, because this town isn’t my problem anymore.\""
show wil with dis1
show wil talking with dis
wi "\"Tickets are flying fast. I suggest you guard that slip of paper like it’s treasure for the time being.\""
show wil sideeyes with dis3
wi "\"I’m gonna go help some putting the fires out before I see y’all elsewhere.\""
show wil talking with dis3
wi "\"It’s like I said before, boys.\""
show wil eyes with dis1
show wil eyes talking with dis
wi "\"Survive.\""
show wil with dis1
show wil talking with dis
wi "\"Til’ next we meet.\""
show wil with dis1
hide wil with dis3
"He vanishes into the crowd."
#sfx
play background ("sfx/malecrowd.ogg") fadein 3.5
scene bg trainplatformfire with dissolve
show nik disappointed at bonfire with dis3:
    xzoom-1
    xpos -0.10
    yalign 1.0

"The chugging of the train gets louder."
#sfx
"It pulls in for a stop as crowds swarm it, restlessly."

if SOLDD_Points ==0:
    show nik smile
    show dim smile at bonfire behind nik:
        xpos 0.23
        yalign 1.0
    with dissolve
    show dim smile talking with dis
    di "\"Fancy seeing you again, my friends.\""
    show dim smile with dis3
    show nik happy with dis3
    ni "\"Dimitri!\""
    show dim smile talking with dis
    di "\"Nikolai!\""
    show dim eyes smile with dis3
    show nik eyessmile with dis3
    "The two clap each other on the back."
    "I’m surprised he takes me in for a warm embrace as well."
    "He has a warm, boozy smell to him."
    show dim smile talking with dis
    show nik smile with dis
    di "\"All aboard the Payton express, eh?\""
    show dim smile with dis
    ni "\"Aye.\""
    show nik talking with dis
    show dim with dis
    ni "\"I hear it’s not as developed as Echo.\""
    show nik sad with dis3
    ni "\"Or, ah, as developed as it used to be.\""
    show dim angry talking with dis
    di "\"True, but at least it isn’t hell.\""
    show dim with dis1
    show dim talking with dis
    di "\"I hear they need work.\""
    show nik neutral with dis3
    show dim with dis3
    m "\"Won’t there be problems with the huge influx of people?\""
    show dim talking with dis
    di "\"Not if they’re receptive to the right push in urban planning.\""
    show dim with dis1
    show dim talking with dis
    di "\"I could lend them my expertise in the matter if they’re receptive.\""
    show dim smile with dis3

if SOLDF_Points ==0:
    if SOLDD_Points ==0:
        show fel mask at bonfire with dis3:
            xpos 0.52
            yalign 1.0
    else:
        show fel mask at center,bonfire with dis3
    show nik smile with dis3
    fe "\"Oiy.\""
    show nik happy with dis3
    ni "\"Felipe!\""
    ni "\"You’re alright as well.\""
    show nik smile with dis3
    show fel eyes mask with dis3
    fe "\"Funny to see everybody all at the same time when it’s not late at night.\""
    show nik neutral with dis
    fe "\"All it took was the whole town lighting on fire.\""
    show nik talking with dis
    if SOLDD_Points ==0:
        show dim with dis
    ni "\"Is your family alright?\""
    show nik neutral with dis
    show fel mask angry with dis
    fe "\"Not really, but they’re going to have to be if they don’t want to choke to death.\""
    fe "\"I used to think not even the fire of the devil would get my mother to leave Echo, and that turned out to be true.\""
    show fel mask eyes with dis
    fe "\"But my cousins aren’t staying with her.\""
    show fel mask with dis
    fe "\"I need to find work, and that work is in Payton now.\""



if SOLDP_Points ==0:
    show nik smile with dis3
    if SOLDD_Points ==0 and SOLDF_Points ==0:
        show pau talking at bonfire with dis3:
            xpos 0.7
            yalign 1.0
        show dim smile with dis3
    else:
        show pau talking at right,bonfire with dis3
    pa "\"Well look who kept their fur unsinged.\""
    show pau with dis1
    show pau talking with dis
    pa "\"I thought y’all were charcoal when I saw you sneak on through that cave.\""
    if SOLDF_Points ==0:
        show pau angry with dis
        show fel mask eyes with dis
        fe "\"In fairness they are probably surprised to see you alive too.\""
        show fel mask with dis
        show pau angry talking with dis
        pa "\"In fairness you can lick my sweaty balls.\""
        show pau eyes smile with dis1
        show pau eyes smile talking with dis
        pa "\"I’m the daredevil in these parts.\""
        show pau eyes smile with dis1
        show pau eyes smile talking with dis
        pa "\"These boys just must be shittin’ out four leaf clovers every time they eat their greens with how much luck they got.\""
        show pau eyes smile with dis1
        show pau eyes smile talking with dis
    else:
        show pau with dis
        m "\"No offense, but I’m surprised to see you alive as well.\""
        show pau talking with dis
    pa "\"The reaper ain’t fast enough to catch me yet.\""
    show pau surprised with dis1
    show pau surprised talking with dis
    pa "\"Say uh...\""
    show pau surprised with dis1
    show pau surprised talking with dis
    pa "\"If we’re all goin’ in the same direction and the same place, y’all wouldn’t mind if we shacked up for a bit, right?\""
    show pau with dis1
    show pau talking with dis
    pa "\"I figure money is tight between the lot of us.\""
    show pau eyes smile with dis
    show nik eyessmile with dis
    ni "\"I don’t see why not.\""
    show nik smile with dis
    ni "\"It’s what we were doing before anyway.\""

if SOLDD_Points ==0:
    show dim talking with dis
    di "\"Manpower is more important than money in times of crisis anyway.\""
    show dim smile with dis1
    show dim smile talking with dis
    if SOLDP_Points==0:
        show pau with dis
    di "\"You could all learn a thing or two about living off the land.\""
    show dim smile with dis

if SOLDF_Points ==0:
    show fel eyes mask with dis
    fe "\"In the future it depends on where my mother and my cousins end up settling...\""
    show fel mask with dis
    fe "\"But for now I won’t be able to commute from Echo to Payton every night, so I need a place too.\""


ni "\"Any objections Sam?\""
m "\"Sounds like more or less of the same as we’ve been doing.\""
m "\"But let’s play it by ear?\""

if SNY_Points >0:
    scene bg trainplatformfire with dis3
    "I see another figure in the crowd try and keep his head low."
    show yao sidelook crossed h at center,bonfire with dis3
    "But I’d recognize his cap anywhere."
    play sound ("sfx/thud.ogg")
    hide yao with vpunch
    "But before I can get to him, the hard, cold muscle of another person’s body bumps into me."
    show bec surprised at center,bonfire with dis3
    stop sound
    m "\"Ungh.\""

else:
    scene bg trainplatformfire with dissolve
    play sound ("sfx/thud.ogg")
    m "\"Ungh.\"" with vpunch
    show bec surprised at center,bonfire with dis3
    "The hard, cold muscle of another person’s body bumps into me."
    stop sound
show bec angry talking with dis
bk "\"You again?!\""
show bec grumpy squint with dis
"He looks more frustrated than panicked."
"Or maybe just exhausted."
show bec sideeye angry talking with dis
bk "\"How is it that every time something goes wrong I manage to run into you?\""
show bec grumpy squint with dis
m "\"When aren’t things going wrong here?\""
show bec angry talking with dis
bk "\"We were doin’ pretty damn good the last decade, all things considered.\""
show bec grumpy squint with dis
"I take a look at the bags at his feet."
m "\"You leavin’ for Payton?\""
show bec angry eyes talking with dis
bk "\"Are you slow?\""
show bec grumpy squint with dis1
show bec angry talking with dis
bk "\"I’ll be back in town when the fire’s dead.\""
show bec grumpy squint with dis1
show bec sideeye angry talking with dis
bk "\"Who do you think will be held responsible for cleaning up this mess?\""
show bec grumpy squint with dis
"I wince a little at the thought."
m "\"You think you can?\""
"He grunts."
show bec angry talking with dis
bk "\"You think there’s anybody else?\""
show bec grumpy eyes with dis1
show bec angry eyes talking with dis
bk "\"Ain’t shit I can do anyway ’till that’s the case. And it’s not like I want to fall asleep and wake up with black lung.\""
show bec sideeye with dis
"He looks away briefly as a family of otters passes through, pushing their way against us."

if BKWALLET_Points ==0:
    show bec sideeye angry talking with dis
    bk "\"Now unless you want to make ME your problem, just stay out of my way.\""
    show bec sideeye with dis
    m "\"Hey!\""
    show bec grumpy eyes with dis
    m "\"You were the one who ran into {i}me{/i}!\""
    show bec angry eyes talking with dis
    bk "\"Now you know how it feels!\""
    show bec grumpy squint with dis
    "He bends his legs, picks up his luggage, {nw}"
    hide bec with dis3
    extend "and turns from me without looking back."
    "I feel a bit irritable now, but it’s not like I can tell him what really happened."
    "Either way, I’m not going to make him my problem."
    if SNY_Points>0:
        "I still need to find Yao."

else:
    m "\"Is that really the reason you’re staying?\""
    show bec surprised with dis
    "His head snaps to me very quickly."
    "It makes me a little more confident about my guess."
    show bec eyes talking with dis
    bk "\"A paycheck is a paycheck, buddy.\""
    show bec with dis
    "I lean to look past him to the right."
    "Then to the left."
    show bec grumpy squint with dis
    m "\"I don’t see your brother at the station.\""
    show bec angry eyes talking with dis
    bk "\"Now why the hell would you?\""
    show bec sideeye with dis1
    show bec sideeye angry talking with dis
    bk "\"Snakes crawl on their bellies.\""
    show bec angry with dis
    m "\"Did he know about this?\""
    m "\"That all of this was gonna happen?\""
    show bec grumpy eyes with dis
    "He grunts again."
    show bec eyes talking with dis
    bk "\"Can’t say for sure.\""
    show bec sideeye with dis1
    show bec sideeye angry talking with dis
    bk "\"But if he’s alive?\""
    show bec sideeye with dis1
    show bec sideeye angry talking with dis
    bk "\"He’ll show up eventually.\""
    show bec sideeye with dis1
    show bec sideeye angry talking with dis
    bk "\"And then I’ll find out.\""
    show bec with dis
    "Now he nods slowly."
    "A cluster of tumbleweeds pass us by in the distance."
    "The fire casts long shadows of the stuck, tightly overlapping branches."
    show bec talking with dis
    bk "\"Welp.\""
    show bec eyes with dis1
    show bec eyes talking with dis
    bk "\"I got a feeling we won’t be seeing one another again.\""
    show bec with dis1
    show bec talking with dis
    bk "\"So let’s make ourselves scarce.\""
    show bec with dis1
    show bec talking with dis
    bk "\"Make sure to take care of yourself Mr. Ayers.\""
    show bec sideeye with dis1
    show bec sideeye angry talking with dis
    bk "\"Family sure as hell won’t.\""
    show bec sideeye with dis
    "He bends his legs, picks up his luggage, {nw}"
    hide bec with dis3
    extend "and turns from me without looking back."
    "I still can’t decide if I like him or not."
    "But it’s hard not to wish him luck after everything he’s gone though."
    "And everything he has coming."
    if SNY_Points>0:
        "But I don’t have time to think about that for long."
        "I still need to find Yao."





if SNY_Points ==0:
    "There’s only one last person who doesn’t show up at the station."
    "That damn tiger."
    "I still don’t get why we found him down there with Briggs."
    "Nik tells me later that he believes Yao did what he had to to get close enough to Briggs to get his one shot in."
    "But I can’t be so sure about that."
    "Briggs might have lost his tail, but it’s hard for me to believe Yao missed."
    "There must have been a deal he made somewhere that we aren’t privy to."
    "Won’t ever be privy to."

else:
    "I push past a few more crowds of people, searching, feeling like if I don't find him soon, I won't find him at all."
    show yao sidelook crossed h at center,bonfire with dis3
    "But then I see a striped arm."
    show yao angry -crossed h with dis3
    "I grab for his sleeve with my good hand and he whirls around."
    show yao teeth
    play sound ("sfx/thud6.ogg")
    "He presses me against the wall of the station, {nw}" with hpunch
    show yao -teeth with dis
    extend "only relaxing when he realizes it’s me."
    stop sound
    m "\"...Hi.\""
    show yao angry crossed with dis3
    ya "\"That... was just another one of your not so good ideas.\""
    show yao talking with dis
    ya "\"You are lucky that I have become familiar with your touch.\""
    show yao -talking with dis
    m "\"I’d make the easy joke if I were in the mood for joking.\""
    show yao sidelook with dis3
    ya "\"...Clearly you have something you wanted to say.\""
    ya "\"You should say it before I go.\""
    m "\"Well that’s sort of it.\""
    m "\"Why do you have to go?\""
    m "\"Ain’t everything over?\""
    ya "\"Briggs is still alive and at large.\""
    show yao -sidelook with dis3
    m "\"William said he’s going to take care of him.\""
    show yao eyebrows with dis
    ya "\"...the cop?\""
    m "\"I guess he technically ain’t anymore.\""
    show yao sidelook with dis3
    ya "\"I see.\""
    m "\"So, that means you don’t need to worry too much, I don’t think?\""
    ya "\"If they look for us, better they do not find us all in one place.\""
    m "\"But nobody knows about...\""
    m "\"You know. What we took.\""
    ya "\"It is still smarter to separate.\""


    menu yaofuturechoice1:
        "Being able to see you has nothing to do with what’s smart or not.":
            show yao eyebrows with dis3
            m "\"We’ve been through too much to go our separate ways...\""
            m "\"I don’t want you to go.\""
            ya "\"Why?\""
            menu yaofuturechoice2:
                "Because I want you in my life.":
                    show yao surprised with dis3
                    m "\"And I think Nik would want you too.\""
                    m "\"It’s hard to imagine what the day would be without you anymore.\""
                    show yao sad -crossed with dis3
                    $ SNY_Points = 4
                "Because you’re my friend.":
                    show yao talking with dis
                    ya "\"True friendships do not end.\""
                    show yao -talking with dis1
                    show yao talking with dis
                    ya "\"Even if they are oceans apart.\""
                    $ SNY_Points = 3
        "I guess you’re right.":
            $ SNY_Points = 3



    if SNY_Points ==3:
        show yao smile with dis3
        "He puts his paws on my shoulders."
        ya "\"You are my friend, Samuel Ayers.\""
        show yao eyessmile with dis
        ya "\"And I am not usually one to befriend idiots.\""
        show yao smile with dis

    if SNY_Points ==4:
        "He leans in close to me."
        "Closer than he’s ever been."
        show yao sidelook with dis3
        ya "\"I already love somebody, Samuel Ayers.\""
        show yao surprised with dis3
        m "\"Ain’t there always room for more?\""
        show yao -surprised with dis
        "His chest presses against mine."
        "I can hear his breath get ragged, and I feel him stiffen."
        "The smell of his arousal comes off of him."
        "Then he pulls away, quickly."

    m "\"Come with us to Payton.\""
    show yao smirk with dis
    ya "\"I will in time.\""
    show yao neutral with dis
    m "\"I mean today.\""
    show yao sidelook crossed with dis3
    m "\"Now.\""
    play sound ("sfx/nondistant train.ogg")
    "The whistle of the train blows as the doors open."
    stop sound
    ni "\"Sam, that’s us!\""
    ya "\"There is still somebody I need to find.\""
    show yao talking with dis3
    ya "\"If we do not see one another again, it is not your fault.\""
    show yao -talking with dis1
    show yao talking with dis
    ya "\"Goodbye, Samuel Ayers.\""
    show yao -talking -crossed with dis3
    ni "\"Sam, they’re loading up the luggage! We have to get on board!\""
    hide yao with dis3
    "Yao leaves, not giving me much more of a chance to stand around and hesitate."
window hide
play sound ("sfx/chuggachugga.ogg")
stop background fadeout 4.5
pause 3.0
scene bg black with slower_dissolve
stop sound fadeout 3.5
play music ("music/Court_and_Page.ogg")
scene bg ontracksfire with slower_dissolve
window show
"I always wanted to leave this God forsaken place."
"But now that I have the opportunity... or more or less no choice, the moment where all of the people in my life were coming together to build something that worked..."
"It all tears itself apart again."
stop sound
"And we’re all left as nomads."
"Travelers without a home."
"Fuck you, Echo."
"Fuck you for hurting me."
"Fuck you for hurting Nikolai."
"Fuck you for hurting William."
if SNY_Points>0:
    "Fuck you for hurting Yao."
"Fuck you for hurting all of the people you force together before you tear them apart."
"And fuck you for the promise of better days and a better life."
"Now that you’re nothing, may nobody stumble upon you on some God forsaken path."
"May nobody slip through you on their way to bigger, better places."
scene bg black
pause 1.0

"And may nobody remember your name."
stop music fadeout 5.5
pause 5.0
$ renpy.music.set_volume(1.0, delay=2.5, channel='background')
#[EPILOGUE]
window hide
scene bg oyl with slow_dissolve
scene bg black with slow_dissolve
window show
scene bg niksamhouse with dissolve
ni "\"...hm.\""
play music ("music/mieux.ogg") fadein 3.5
show nik disappointed at stagday with dis3:
    yalign 1.0
    xpos -0.15
    xzoom-1
m "\"...what’s wrong?\""
show nik sidelook with dis3
ni "\"If the bench is forward it is not facing the sun.\""
m "\"So... that’s a good thing?\""
ni "\"But it is looking into the street.\""
show wil frustrated at stagday with dis3:
    yalign 1.0
    xpos 0.60
wi "\"You want to pick a direction before we turn the damn bench again?\""
wi "\"We’re sweatin’ our asses off over here.\""
show wil with dis3
ni "\"It is also hard work to maximize comfort.\""
if SOLDD_Points ==0:
    show dim smile talking behind nik at center,stagday with dis3
    show nik neutral with dis3
    di "\"Thank you for selecting the {i}wooden{/i} wind chime.\""
    show dim smile with dis3
    show nik talking with dis3
    ni "\"We all remember the stories.\""
    show nik eyes with dis1
    show nik eyestalking with dis
    ni "\"Even if you never bothered to elaborate.\""
    show nik neutral with dis
    show dim eyes smile talking with dis
    di "\"I would if I could, my friend.\""
    show dim smile with dis1
    show dim smile talking with dis
    di "\"Perhaps it was something in the frequency of their sound that bothered me, but, their presence alone was enough.\""
    show dim smile with dis3
if SOLDP_Points ==0:
    show nik neutral with dis3
    show pau eyes smile talking at halfleft,stagday behind nik with dis3:
        xzoom-1
    pa "\"So long as he’s lettin’ us board for free, all hail the king of comfort.\""
    show nik talking with dis
    show pau surprised with dis
    ni "\"Who says this is for free?\""
    show nik smile with dis
    show pau eyes smile with dis
    ni "\"I will need more furniture.\""
    show pau eyes smile talking with dis
    pa "\"Provide the materials and tools and I’ll provide the handiwork.\""
    show pau with dis
    ni "\"If you start on the bunks it will be a lot more comfortable than the floor.\""
    show pau talking with dis
    pa "\"Ain’t nothin’ wrong with the floor.\""
    show pau with dis1
    show pau talking with dis
    pa "\"Straight timber is the best for your back.\""
    show pau angry with dis
    m "\"I am not sharing my bed again.\""
    show pau angry talking with dis
    pa "\"Good thing too. You take up twice your body size, anyhow!\""
    show pau with dis3

if SOLDF_Points ==0:
    show fel eyes talking at halfright,stagday behind wil with dis3
    fe "\"It’s nicer than the barracks were.\""
    show fel with dis1
    show fel talking with dis
    fe "\"Not that this is saying much.\""
    show fel with dis
    ni "\"I am trying not to be cheap.\""
    show fel smile talking with dis
    fe "\"Be as cheap as you want.\""
    show fel smile with dis1
    show fel smile talking with dis
    fe "\"You and your...\""
    show fel with dis
    "He’s about to say something and then stops himself."
    show fel talking with dis
    show wil surprised with dis
    fe "\"...rich amigo are the ones who made this possible.\""
    show fel with dis
    wi "\"...He thinks Sam’s rich?\""
    "I sweat a little."
    show wil with dis
    m "\"Well, you know.\""
    m "\"The Hip was highly visited, William.\""
    m "\"I used to be a star.\""
    show wil smile with dis
    wi "\"So it was stardust that flaked off your face when you washed.\""
    m "\"You mean my pension.\""

scene bg niksamhouse with dis3
play sound ("sfx/thud.ogg")
"Will scoots the bench a little too hard forward." with vpunch
stop sound
"The pain in my paw lights up again like fire."
show nik surprised at left,stagday with dis3:
    xzoom-1
show wil surprised at right,stagday with dis3
m "\"FUCK!\""
wi "\"Ah shit, it’s your paw again ain’t it?\""
show nik neutral with dis
show wil with dis
m "\"It’s fine.\""
show wil talking with dis
wi "\"This good, Nik?\""
show wil with dis3
show nik sidelook with dis3
"He tilts his head and scrutinizes the bench."
show nik eyestalking with dis3
ni "\"Yes, I think it works.\""
show nik neutral with dis
show wil talking with dis
wi "\"Good, because me and Sam are taking 20.\""
stop music fadeout 2.5
show wil with dis1
show wil talking with dis
wi "\"Let’s get you something for the pain, okay?\""
show wil with dis
m "\"...\""
"I want to say I’m fine, but he’s being pushy."
m "\"Be right back everybody.\""
scene bg niksamhouseinside with dis3
#sfx
"I hear a click as William turns on the gas stove."
show wil sideeyes at center,stagday with dis3
play music ("music/quiet.ogg") fadein 2.5
m "\"...So what did you really want to say?\""
"I hear him fill the teapot with water, then he places it on the surface."
play sound ("sfx/match.ogg")
"A match strikes and the flame lights up."
stop sound
wi "\"Just so you know, Briggs returned to the mining operation.\""
wi "\"He’s practically seized total control.\""
m "\"...They never found Mr. Hendricks?\""
"William shakes his head."
show wil talking with dis3
wi "\"No, but his missus is giving him hell.\""
show wil with dis1
show wil talking with dis
wi "\"And thanks to the evidence we’ve compiled, she’s trying to pin the fire on ‘im, too.\""
show wil with dis
m "\"Can we testify against him?\""
show wil talking with dis
wi "\"To who?\""
show wil with dis
m "\"...weren’t you takin’ this to the state?\""
show wil talking with dis
wi "\"Yeah but it’s gotta work its way up to a federal level.\""
show wil with dis1
show wil talking with dis
wi "\"He’s already trying to place the blame on y’all, you know?\""
show wil with dis
"I flinch."
m "\"With what fuckin’ evidence?\""
show wil sideeyes with dis3
wi "\"Don’t need much evidence if you get enough people mad and you can hand over a few dead foreigners and a homosexual prostitute.\""
show wil eyes talking with dis3
wi "\"But his evidence is weak and the counterevidence against him is stacking up.\""
show wil with dis
m "\"... you really think people would take our side against his in federal court?\""
show wil sideeyes with dis3
wi "\"Not really, no.\""
show wil talking with dis3
wi "\"But the widow Hendricks?\""
show wil smile with dis
wi "\"She’s as sweet as her ice cream, ain’t she?\""
show wil talking with dis
wi "\"Probably not a dishonest bone in her body as far as the legal system is concerned.\""
show wil with dis1
show wil talking with dis
wi "\"The fact that her family was wealthy too doesn’t hurt.\""
show wil with dis
m "\"So things are going to be fine?\""
show wil talking with dis
wi "\"Should be, so long as you keep your head down and never go back to Echo.\""
show wil with dis
m "\"Hrm.\""
show wil talking with dis
wi "\"Why hrm?\""
show wil with dis1
show wil talking with dis
wi "\"Knowing how you thought of the place, I thought you’d be sighing with relief.\""
show wil surprised with dis
m "\"I was just hoping I’d hear from Cynthia is all.\""
"He looks at me with some consternation."
wi "\"You mean you haven’t?\""

"I hold my finger up {nw}"
#sfx
hide wil with dis3
extend "and walk to the cabinet."
play sound ("sfx/paper1.ogg")
"I pull out a drawer and remove the top, leaving an envelope underneath."
#sfx
show wil surprised at center,stagday with dis3
stop sound
"Then I walk back to the table and plop the letter on the surface."
wi "\"That’s Dora’s seal.\""
show wil with dis
m "\"Go ahead and open it.\""
"The coyote flips the top open quickly and smoothes it out on the table."
"He pulls two things from the inside of the envelope."
"One is a picture of the old staff at the Hip last year."
"The other is a browned, formal-looking piece of paper."
show wil talking with dis
wi "\"So Dora gave you the deed, huh?\""
show wil with dis
m "\"She gave {i}Cynthia{/i} the deed.\""

m "\"You think I’d still have it if I had seen her?\""
show wil talking with dis
wi "\"Need me to track her down?\""
show wil with dis
m "\"That would be helpful.\""

m "\"Though sometimes I wonder if she might not want to be found.\""
show wil eyes talking with dis
wi "\"Doesn’t hurt to try.\""
show wil with dis
m "\"...There’s another reservation on Echo’s edge.\""
m "\"I hear some of the girls from the Hip were staying there until things get fixed up.\""
"Not that I think things will ever get fixed up."
"I hear the fire in the mine is still going."
show wil talking with dis
wi "\"You think she’s there?\""
show wil with dis
m "\"I think she could be.\""
m "\"Ain’t ever going back to check though.\""
m "\"And I don’t want you going back there neither.\""
show wil talking with dis
wi "\"I go there from time to time, but I don’t exactly plan on stayin’.\""
show wil sideeyes with dis3
wi "\"’Specially not at night.\""
m "\"I don’t even like entertaining the idea that she’d go back.\""
wi "\"Then maybe she didn’t.\""
wi "\"But if she’s there, I’ll find her.\""
show wil talking with dis3
wi "\"Ok?\""
show wil with dis
"I pull the envelope back off of the table."
m "\"Ok.\""
show wil talking with dis
wi "\"Knowin’ her, she’s doin’ just fine somewhere.\""
show wil with dis
m "\"Regardless, I’d like to be sure.\""
show wil smile with dis
wi "\"Well, that’s something I can be good for.\""
show wil talking with dis
wi "\"I’ll get you an answer some day.\""
show wil with dis
m "\"You promise?\""
show wil talking with dis
wi "\"Yeah, I promise Sam.\""
show wil eyes with dis
"He presses his forehead to mine and musses the fur on the back of my head."
stop music fadeout 3.5
show wil eyes smile with dis
wi "\"Let’s worry about Lord Król’s plans for now, huh?\""
show wil smile with dis
"I smile at that."

"I remember {i}król{/i} means {i}king{/i} in Nik's language."

"{i}Lord King{/i} is silly enough to fit."
scene bg niksamhouse with dis3

"Outside I expect Nik to be the first thing I see in front of the steps."
show yao crossed h at center,stagday with dis3
show wil surprised at stagday with dis3:
    yalign 1.0
    xpos 0.55
"But instead it’s a tiger."
show yao talking with dis
ya "\"...Adler.\""
show yao -talking with dis
show wil talking with dis
wi "\"No need to be cold with me Yao, I ain’t police no more.\""
show wil with dis

if SNY_Points ==0:
    show yao talking with dis
    ya "\"Once a cop, always a cop.\""
    show yao angry with dis3
    show wil frustrated with dis3
    wi "\"If that’s the case, send me some of your tax dollars, ‘cause I sure as hell ain’t getting paid by the state.\""
    show wil with dis3

if SNY_Points >0:
    show yao eyebrows with dis
    ya "\"So you have other reasons to be alone with Sam?\""
    show wil talking with dis
    wi "\"Private ones yeah.\""
    show wil with dis
    show yao talking with dis
    ya "\"Not too private I hope.\""
    if SNY_Points ==4:
        show yao angry with dis
        ya "\"Or else I will have him wear a ring to remind you he is mine.\""
    if SNY_Points ==3:
        show yao angry with dis
        ya "\"Nik does not like to share everything.\""

"They stare at one another in silence."
show yao eyessmile -crossed with dis3
show wil smile with dis3
play music ("music/busymorning.ogg") volume 0.7
"Then they both look at me and start to crack up."
show yao smile with dis3
show nik talking at stagday behind yao with dis3:
    yalign 1.0
    xpos -0.05
    xzoom-1
ni "\"What is going on?\""
show nik neutral with dis
m "\"They’re besmirching my good character.\""

wi "\"Now come on, Sam.\""

wi "\"Everybody knows you’re as loose as a rubber band.\""
show nik disappointed with dis3
ni "\"Bullying Sam will not be tolerated.\""

ni "\"Unless he does not clean his dishes.\""
show nik smile with dis3
m "\"Thank you Nik.\""

ya "\"And he remembers not to use the nice silver when we are eating for casual occasions.\""

m "\"I will assuredly not, Yao.\""

if SOLDP_Points ==0:
    hide wil with dis3
    show cha talking at right,stagday with dis3
    ch "\"As if you ever saved the appropriate silver for appropriate times, Yaolin.\""
    show cha with dis3
    show yao sidelook crossed with dis3
    ya "\"Ah.\""
    ya "\"But we did not used to have nice silver.\""
    show cha eyes talking with dis
    ch "\"Just because you have money now doesn't mean you have class.\""
    show cha with dis3
    show yao eyebrows with dis3
    ya "\"The wisest conclusion to come to is that we have no need for class in this country.\""
    show cha smirk with dis
    ch "\"That is what people lacking finesse say, yes.\""
    show cha with dis

show nik talking with dis
ni "\"How’s the search for work going?\""
show yao talking with dis
show nik neutral with dis
if SOLDP_Points ==1:
    show wil with dis
ya "\"I have found something already.\""

if SOLDP_Points ==0:
    show yao -talking with dis
    show cha eyes talking with dis
    ch "\"Good.\""
    show cha with dis1
    show cha talking with dis
    ch "\"I could not stand you if you were idle.\""
    show yao smirk with dis
    show cha surprised with dis
    ya "\"You can rile me later when we are alone.\""
    "The sable’s ears redden."
    show cha pipe eyes with dis3
    ch "\"Tch.\""
    show cha pipe with dis
else:
    show yao -talking with dis1

show yao talking with dis
ya "\"They are building an electric plant.\""
show yao smile with dis
ya "\"I have already secured a position.\""
show yao neutral with dis
m "\"Sounds dangerous.\""
show yao talking with dis
if SOLDP_Points ==0:
    show cha pipe sidelook with dis
ya "\"No more dangerous than your old job?\""
show yao neutral with dis1
show yao talking with dis
ya "\"Hearts are heavy things.\""
show yao neutral with dis
m "\"Men have heavier things than hearts when they’re blessed, and it keeps things a whole lot more simple.\""
scene bg nikcg10
if SOLDD_Points==0:
    show nikcg10dim
if SOLDF_Points==0:
    show nikcg10fel
if SOLDP_Points==0:
    show nikcg10chpa
if nikproposal==True or SNY_Points==4:
    show nikcg10rsam
    if SNY_Points==0:
        show nikcg10e1
else:
    show nikcg10nrsam
    if SNY_Points==0:
        show nikcg10e2
if SNY_Points ==4:
    show nikcg10ryao
else:
    show nikcg10nryao

with dis4
"I say that a little too loudly and I think that everybody must be looking at me."

"But they ain’t."

"It’s easy to forget yourself when you're surrounded by the people you’ve been through hell with together."

"But it’s just ordinary for us."

"And the fact that any of us are still here makes me stop worrying."

"If only for a little while."
window hide
pause 5.0
stop music fadeout 5.0
scene bg black with slower_dissolve
window show
if SOLDN_Points==1 and SNY_Points ==4:

    "{i}(Meowdy, folks.){/i}"
    "{i}(If you got here, you unlocked a secret scene!){/i}"
    "{i}(When consulting with project supporters, we decided it would be fairly big and asset heavy, so it could use some time to cook.){/i}"
    "{i}(However, it’s not something crucial for the ending of Nikolai’s main route.){/i}"
    "{i}(Keep on clicking to see the next scene.){/i}"
    pause 3.0

#-fast forward in time 1950s-

scene bg black with dissolve
niunk "\"Sam...\""
m "\"...\""

niunk "\"Sam.\""
play background ("music/cicadas.ogg") volume 0.5 fadein 5.0
scene bg niksambedroom with dissolve
"The window’s open."

"I feel warm air sift through my fur as the sunlight peeks through the doilied curtains."
show oldnik smile at center with dis3
ni "\"Get up, Sam.\""
show oldnik with dis
m "\"I’m sorry.\""
show oldnik surprised with dis
m "\"My head hurts just a bit.\""

ni "\"...Ah.\""
show oldnik sidelook with dis3
ni "\"It is another one of those days?\""

m "\"Maybe.\""

m "\"Could be that I just slept funny.\""
show oldnik disappointed with dis3
ni "\"We used to be able to sleep on hard wooden slats.\""

m "\"Might be better for our backs now.\""
show oldnik smile with dis3
ni "\"I brought you breakfast.\""

ni "\"Rose hip tea.\""
ni "\"And there’s these croissants from the new place downtown where the butter melts in your mouth.\""
show oldnik sidelook with dis3
ni "\"...though there’s plenty of sausages if you don’t want something too buttery.\""
m "\"...some aspirin sounds delicious.\""
show oldnik smile with dis3
ni "\"Of course!\""
ni "\"I’ll bring that right away.\""
hide oldnik with dis3
"He stumbles backwards and out of the room."
"It kills me how much energy he has in the morning, even at his age."
"Can’t be helped, I suppose."
"I roll my neck and slip out of bed."
"Thankfully it’s not too hot to slip into my robes."
#sfx
show oldnik smile at center with dis3
"I hear Nik re-entering the room with a glass and another plate as he twirls around the radiator and slips them onto the tray in my bed."
ni "\"Your medicine.\""
"I smile at him as he puts them into my paw."
m "\"...Thanks. It should kick in fast.\""
ni "\"...No rush.\""
m "\"You seem happy.\""
show oldnik eyes smile with dis
ni "\"I am often happy when I’m with you, Sam.\""
show oldnik smile with dis
m "\"...No, I mean.\""
m "\"Something’s different.\""
m "\"You’re in {i}too good{/i} of a mood.\""
"He drops a roll of paper into my lap."
ni "\"Read the headline.\""
m "\"You know I don’t read the paper.\""
show oldnik eyes smile with dis
ni "\"You should this time.\""
show oldnik smile with dis
"I sigh and squint at the paper."
m "\"...{i}Echo Mine Owner Guilty of Gross Negligence{/i}.\""
m "\"{i}CSCG shutting down for good{/i}.\""
m "\"Huh...\""
m "\"That old bag of shit was still alive?\""
show oldnik disappointed with dis3
ni "\"If you can call it that.\""
ni "\"Looks like things didn’t go his way after the fires.\""
show oldnik with dis3
m "\"...William never could pin the fires on him, could he?\""
show oldnik talking with dis
ni "\"No, but he did a good enough job at making his life hard.\""
show oldnik with dis
m "\"Says here {i}Miranda Cosgrove, Cordelia Hendricks, and William Adler credited as key witnesses{/i}.\""
m "\"Better late than never, I s’pose.\""
"My eyes narrow down on Hendricks."
m "\"...Did they really never find James?\""
show oldnik sidelook with dis3
ni "\"They may have, but I never followed it closely.\""
ni "\"You think we would have heard about him if they did?\""
m "\"I’d at least expect to get pictures of his chest sent to me in the mail.\""
show oldnik happy with dis3
"Nik starts laughing."
show oldnik disappointed with dis3
"Then he laughs a bit too hard."
m "\"...You alright?\""
"His laugh turns into a full-on wheeze, and he nods, water in his eyes."
"He sputters for a while and it takes him some time to recover."
"I rub his back, waiting, listening to the windchimes just outside the window."
if SOLDD_Points==0:
    "I never found out why Dimitri didn’t like the sounds they made, but we got one only after he passed."
m "\"...Tell ya what.\""
m "\"You eat most of my breakfast for me and I’ll draw us a bath.\""
m "\"You could use a soak in the hot water.\""
ni "\"A-at least eat the sausages.\""
m "\"It’s fine.\""
show oldnik sad with dis3
ni "\"Samuel...\""
show oldnik with dis3
"I pluck one off the plate with my bare paws and rip into it, chewing as I go."
show oldnik talking with dis
ni "\"Brought you silverware...\""
play music ("music/niktheme.ogg")
show oldnik with dis1
hide nik with dis3
stop background fadeout 3.0
play music ("music/niktheme.ogg")
scene bg niksamhouseinside1950s with dis3
play sound ("sfx/softknock.ogg")
"Once I’m out by the front door I hear a quiet knock."
"I open the door and look down."
stop sound
"There’s a package."
"If it’s what I suspect it is, it’s the perfect timing."
scene bg niksambathroom with dis3
play sound ("sfx/bathtub.ogg")
"When I get back inside, I feel a silly sense of pride as I turn the knob and wait for the water to heat up."
"It’s a hell of a lot easier to draw a bath these days than it used to be."
"But there’s something tender about it that makes me giddy."
stop sound fadeout 1.5
"I wait for the water to get too hot for my paws."
"Then I add a bit of liquid soap and a bit of anise oil so the room smells like licorice."
play sound ("sfx/paperrip.ogg")
"As the tub fills I rip open the box with my claws."
"Jackpot."
stop sound
show oldnik sidelook n at right with dis3
ni "\"Is it ready?\""
m "\"No.\""
m "\"Though I can see that you are, considering you’re already naked.\""
show oldnik disappointed n with dis3
ni "\"We used to get naked for it all the time without having to wait for the perfect temperature.\""
show oldnik n with dis3
m "\"Maybe you did.\""
m "\"I had to prepare the perfect temperature for clients plenty back when I had to rely on a stove.\""

m "\"It was exciting to always meet somebody new.\""
m "\"Figure out what made them like to move.\""
show oldnik sidelook n with dis3
ni "\"Sounds like you miss it.\""
m "\"Some parts of it, sure.\""
m "\"I don’t miss pretending that spending time with you was work, though.\""
show oldnik n with dis3
m "\"Take a look at this.\""
play sound ("sfx/splash5.ogg")
show oldnik surprised n with dis
"I throw the toy duck into the water."
show oldnik shocked n with dis3
ni "\"Don’t break anything!\""
stop sound
show oldnik surprised n with dis3
m "\"Calm down and look.\""
m "\"It floats.\""
ni "\"Is it wood?\""
ni "\"You threw it pretty hard.\""
m "\"It’s made of rubber.\""
ni "\"Oh.\""
show oldnik shocked n with dis3
ni "\"Oh!\""
#sfx
ni "\"It is smooth and squishy.\""
ni "\"How is this possible?\""
show oldnik smile n with dis3
m "\"New production methods I ‘spose.\""
m "\"Thought you’d like it.\""
show oldnik happy n with dis3
play sound ("sfx/splash4.ogg")
ni "\"It moves fast when I push it!\""
"I think about saying something at that moment but he’s too invested in shoving the thing around in the water."
play sound ("sfx/splash2.ogg")
"He slaps it repeatedly, submerging it, laughing at it each time it resurfaces."
m "\"Say, Nik?\""
stop sound
show oldnik eyes smile n with dis3
ni "\"Mhm?\""
m "\"Why do you really like ducks as much as you do?\""
show oldnik n with dis3
"He rolls his eyes."
show oldnik talking n with dis
ni "\"There is no particular reason.\""
show oldnik sidelook n with dis3
ni "\"But the day of my sister’s wedding, there were ducks.\""
ni "\"The days after the violence in my country, on the river, there were ducks.\""
ni "\"When I came to this country, in the harbor, in the lakes...\""
ni "\"There were ducks.\""
ni "\"Usually close by the duck honks, you would often hear people laughing.\""
ni "\"You would hear popcorn machines popping.\""
ni "\"Or some calliope music sounding off.\""
ni "\"Where there were ducks there were always people.\""
ni "\"And when there’s the sound of people, there is always the reminder that another morning is soon to come.\""
m "\"Profound.\""
show oldnik disappointed n with dis3
ni "\"Like I said, there’s no particular reason.\""
ni "\"Associations with associations, nothing more.\""
show oldnik n with dis3
m "\"The water’s fine.\""
show oldnik smile n with dis
m "\"Let’s get in.\""
#sfx
scene bg nikcghappyending with slow_dissolve

ni "\"I’m grateful we could afford a tub to contain us both.\""
m "\"I’m grateful there exists a tub to contain us both.\""
ni "\"It won’t be so impressive if you keep on skipping breakfast.\""
m "\"Mmhm.\""
ni "\"...\""
m "\"What?\""
ni "\"Are you happy with me, Sam?\""
m "\"Now there’s a loaded question.\""
ni "\"I just meant...\""
ni "\"If you could have done things differently, would you have?\""
m "\"Hell if I know.\""
m "\"That sounds like a problem for some other me.\""
ni "\"...And you don’t see things anymore, do you?\""
m "\"Not for a long while, no.\""
ni "\"That is good.\""
m "\"I don’t know what it means, frankly.\""
m "\"I still wonder of course.\""
ni "\"Wonder what?\""
m "\"About what’s out there, past being alive.\""
m "\"But then sometimes I just figure it ain’t my fuckin’ business.\""
m "\"If I never know, I never know.\""
m "\"If I ever do, then I will.\""
m "\"Sorry to get philosophical.\""
ni "\"Has Yao’s boyfriend been teaching you words?\""
m "\"{i}Philosophical{/i} ain’t that fancy.\""
ni "\"I find {i}you{/i} very fancy.\""
m "\"Heh...\""
m "\"Hey Nik?\""
ni "\"Yes Sam?\""
m "\"Nadal cię kocham.\""
ni "\"...I love you too.\""
$ renpy.music.set_volume(1.0, delay=2.0, channel='background')
$ renpy.music.set_volume(1.0, delay=2.0, channel='music2')
stop music fadeout 4.0
scene bg black with slower_dissolve
window hide
pause 2.0
$ Credits = 1
$ quick_menu = False

play sound "music/PeppersRag.ogg" fadein 5.0
call screen credits

if SNY_Points==4 and SOLDP_Points==0:

    stop music fadeout 4.0
    pause 1.0
    window show
    play background ("music/windbirds.ogg") volume 0.4 fadein 4.0
    "There is an old cemetery in a prosperous town where wealthy families come to rest."
    "The wind slips through the leaves of the lone willow tree here, and its music lets those who hear it know that there is clean water nearby, often with honking ducks and playing children."
    scene nikcg11000 with dis4
    "Two men meet each other here, exiles in their own country and this one, who get by on the vast amount of their accumulated wealth as one by one they lose their community to the unrelenting march of time."

    ya "\"I’m glad to see you decided to come see him.\""
    ch "\"I came for you.\""
    scene nikcg11010 with dis3
    ch "\"You’re the one who loved him.\""
    ya "\"Nik wanted him buried next to him.\""
    scene nikcg11000 with dis3
    ya "\"There was some resistance.\""
    scene nikcg11100 with dis3
    ya "\"Luckily, Nik planned ahead and already documented the purchases ahead of time.\""
    scene nikcg11110 with dis3
    ch "\"What did him in?\""
    ya "\"Nik, or Sam?\""
    scene nikcg11111 with dis3
    ch "\"I’ve time to hear both.\""
    ch "\"We’re at a cemetery.\""
    scene nikcg11011 with dis3

    ya "\"Nik was the lung disease.\""
    ya "\"Sam followed soon after with a stroke.\""
    scene nikcg11000 with dis3
    ch "\"Not surprising.\""
    ch "\"He seemed to have head problems.\""
    ch "\"Saw things.\""
    scene nikcg11010 with dis3
    ch "\"Of course you could always see the scar on the back of his head when he was wet.\""
    scene nikcg11110 with dis3
    ya "\"You could feel it too.\""
    scene nikcg11010 with dis3
    ch "\"Your hand was placed on top of his head plenty.\""
    ya "\"If you’re jealous I can put mine on your head when we go home.\""
    scene nikcg11000 with dis3
    ch "\"I am not jealous of a ghost.\""
    ya "\"Maybe you should be.\""
    scene nikcg11100 with dis3
    ya "\"He was very good.\""
    play sound ("sfx/thud.ogg")
    scene bg black with vpunch
    "The is a loud thud in the cemetery."
    stop sound
    ya "\"OW!\""
    scene nikcg11011 with dis3
    ya "\"You should not hit me.\""
    ch "\"And you should not make me hit you.\""
    scene nikcg11111 with dis3
    ya "\"Do not abuse an old man.\""
    scene nikcg11011 with dis3
    ch "\"I am old too.\""
    ch "\"I will abuse you as much as I like.\""
    scene nikcg11000 with dis3
    ch "\"Anyway...\""
    ch "\"If you kick the bucket first, is this where you want me to dump your ashes?\""
    ya "\"I don’t care where you dump my ashes...\""
    scene nikcg11100 with dis3
    ya "\"Just do not smoke them.\""
    play sound ("sfx/thud.ogg")
    scene bg black
    ya "\"OW!\"" with vpunch
    stop sound
    scene nikcg11011 with dis3
    ch "\"You were the one who made me quit smoking.\""
    scene nikcg11111 with dis3
    ya "\"You’re welcome.\""
    scene nikcg11000 with dis3
    ch "\"It was hell.\""
    ya "\"But because you quit, you are still here with me, in heaven.\""
    scene nikcg11010 with dis3
    ch "\"I am pretty sure it is still hell.\""
    play sound ("sfx/thud5.ogg")
    scene bg black
    ch "\"OW!\"" with vpunch
    stop sound
    scene nikcg11110 with dis3
    ya "\"It was my turn to punch.\""
    scene nikcg11010 with dis3
    ch "\"Are you ready to go now?\""
    ya "\"Just one last thing.\""
    scene bg black with dis3
    "The tiger places two coins on the headstones."

    "One on the headstone labeled Nikolai Król."

    if nikproposal == True:
        "One on the headstone labeled Samuel Król."
    else:
        "One on the headstone labeled Samuel Ayers."
    scene nikcg11011 with dis3
    ch "\"Are those double eagles? Like the ones from Sam’s stories?\""
    scene nikcg11111 with dis3
    ya "\"Those are {i}the{/i} double eagles.\""
    scene nikcg11011 with dis3
    ch "\"You liar.\""
    ya "\"Not lying.\""
    scene nikcg11111 with dis3
    ya "\"The girl in the mines still had hers.\""
    ya "\"She was saving it to give it back to Sam, but she never found him.\""
    scene nikcg11011 with dis3
    ch "\"Then how’d you find the other?\""
    ya "\"I found the ruins of Red’s Trading Post the night it burned down.\""
    ya "\"There was only one double eagle in the register, and she told me that’s where she spent it.\""
    ch "\"Once a thief, always a thief.\""
    ya "\"I left a nugget worth twice as much.\""
    scene nikcg11000 with dis3
    ch "\"I was joking.\""
    scene nikcg11010 with dis3
    ch "\"Obviously the insurance paid for the Byrnes’ losses, not that they needed it.\""
    ya "\"I hear they definitely did.\""
    ya "\"That family didn’t do so well after the fire.\""
    scene nikcg11110 with dis3
    ya "\"They stayed in Echo.\""
    scene nikcg11000 with dis3
    ch "\"Not much of Echo left in Echo I hear, but so long as it was their choice.\""

    "Yao stares at both of the stones, nodding."

    "Wind plays through the lone willow tree again."

    ya "\"I miss them.\""
    scene nikcg11010 with dis3
    ch "\"Just be glad we got old enough to miss them.\""

    ch "\"Is there one last thing you might want to say before we leave them?\""

    "The old tiger clears his throat."
    scene nikcg11000 with dis3
    ya "\"Nikolai Król.\""

    ya "\"We came to this land as immigrants and strangers.\""

    ya "\"Somehow, we all survived together much longer than we should have in these United States of Columbia, which have tried to kill us at every given opportunity.\""

    ya "\"Sam, I have no idea where the hell you came from, but I also loved you all the same.\""

    ya "\"There is no method of political change we can make to turn an evil empire good.\""
    scene nikcg11100 with dis3
    ya "\"But we can still live good lives within one, together, on the fringes.\""
    scene nikcg11011 with dis3
    ch "\"Is that all?\""

    ya "\"Yes, that is all.\""
    scene nikcg11000 with dis3
    ch "\"By all accounts, based on what we did, we should have died.\""
    ch "\"I know it sounds strange, but...\""
    scene nikcg11011 with dis3
    ch "\"Sometimes it feels like we did...\""
    scene nikcg11111 with dis3
    ya "\"You never told me that before.\""
    scene nikcg11000 with dis3
    ch "\"I know.\""
    ya "\"All I can say is that it is a strange feeling.\""
    ya "\"But at the end of the day, that is all that it is.\""
    ya "\"Besides, if you want to die, I doubt you will have to wait much longer.\""
    scene nikcg11010 with dis3
    ch "\"Nonsense.\""
    ch "\"I’m as healthy as I ever was.\""
    scene nikcg11110 with dis3
    ya "\"So you are dying tomorrow?\""
    play sound ("sfx/thud.ogg")
    scene bg black
    ya "\"OW!\"" with vpunch
    stop sound
    scene nikcg11000 with dis3
    ch "\"Let’s go home now.\""
    ya "\"It will be strange without him.\""
    ya "\"But okay...\""
    scene bg black with dis3

    "The old sable and the old tiger leave the cemetery together."
    "The coins do not last in their resting spot for long."
    stop background fadeout 10.0
    "Nobody is entirely sure what happened to them, as nobody in their right mind would try to use them to purchase anything in the year 1974."
    "But it is quite likely that another teenager stole them."
    scene black with slow_dissolve
    window hide
    scene bg theend with slow_dissolve
    pause
    scene black with slow_dissolve

return
