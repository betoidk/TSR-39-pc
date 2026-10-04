label cliffroute3:
stop music fadeout 5.0
stop background fadeout 5.0
scene black with slow_dissolve
$ renpy.music.set_volume(1.0, delay=1.5, channel='background')
window hide
scene clich3 with slow_dissolve
pause
scene black with slow_dissolve
scene atelier with slow_dissolve
play music "music/reminiscence.ogg" fadein 2.0
window show
unk "\"Lovely work, Cornelis. You're really getting the hang of this, aren't you?\""
"I feel my body grow warm as the old stoat sitting next to me leans in close to the canvas to inspect my work."
"I draw my eyes to the old wooden floorboards to avoid his gaze."
"He smells of paint and smoke, as does this whole atelier. Whereas others might find it an offensive odor, it puts me at ease."
"It reminds me that I am in the presence of an artist."
"A friend."
"A kindred spirit."
cor "\"I'm still nowhere near close to matching you, grandfather.\""
unk "\"Pish posh! Your compositions and use of color are already outstanding. And you're, what, fifteen?\""
cor "\"Fourteen and a half, sir. I turn fifteen this September.\""
"I don't blame him for losing track sometimes. Not with all that's happened."
"Even so, his memory is getting worse. I'm quite certain he thinks Marie is still six at times."
unk "\"Fourteen and a half! My, how time flies.\""
unk "\"I remember when you couldn't even pronounce the word easel, and look at you now!\""
unk "\"You'll be making royal portraits by the time you're twenty, mark my words.\""
"My face grows warmer still."
cor "\"Not if father has anything to say about the matter.\""
unk "\"Did he get cross with you again?\""
cor "\"He doesn't like it when I spend time with you.\""
cor "\"He calls it a waste of a bright mind.\""
unk "\"And you?\""
cor "\"I disagree.\""
unk "\"Is that all? Usually you speak more freely.\""
unk "\"I'm well aware the man loathes me, lad. No need to hold back for my sake.\""
cor "\"It's just that art speaks to me in ways his business lectures don't.\""
cor "\"It takes me to places I've only ever dreamt of, yet he intends to contain me in an office for the rest of my life as though I am some sort of beast to be caged and trained.\""
cor "\"It bores me to tears.\""
unk "\"Perhaps he's merely trying to keep you safe.\""
cor "\"He’s only become worse since Mother–\""
"I stop, and for the shortest of moments, so does my heart."
"It aches."
"It's the first time I've spoken about her in a year, and yet the wound still feels fresh."
cor "\"...since Mother passed.\""
"His face falls at the mention of her."
unk "\"Her passing changed us all.\""
unk "\"I don't blame your father for wanting to keep you close. But you have a serious aptitude for the canvas, Cornelis.\""
unk "\"It would be a waste of a bright mind not to hone it further yet.\""
cor "\"Th–thank you, sir.\""
"I look past him, at his canvas."
"While I've been busy painting portraits, it looks like he's busied himself with a painting of a structure unlike anything I've seen."
cor "\"What did you end up painting? It looks rather elaborate for an afternoon sketch.\""
unk "\"Ah, it's nothing.\""
"He gives me that look, that grin."
"It means he has something to hide, and he desperately wants me to find out."
"And find out I shall."
cor "\"I'd very much like to know.\""
unk "\"Ah, very well. Are you familiar with the Meseta tribe?\""
cor "\"I can't say that I am, sir.\""
unk "\"I wasn't expecting you to be. There's an entire ocean between us, after all.\""
cor "\"So how did you hear about them, sir?\""
unk "\"I recently happened upon a most curious book.\""
unk "\"I bought it for you, of course, but I was rather fascinated, myself. Why, I finished it in a single night.\""
"He points at his canvas. The paint is still wet."
unk "\"This is what is called a hogan. It's a Meseta dwelling.\""
"It looks nothing like the houses lining the canals here."
"What's more, it seems to be located in a rocky, sandy landscape, even more unlike the Batavia I know."
"Is this what they call a desert?"
cor "\"It's got a rather unique shape.\""
cor "\"Why is that?\""
unk "\"The round shape is symbolic of the sun.\""
"He gestures to the doorway he's just painted on."
unk "\"The door faces east, so that when the people living in the hogan wake up every morning...\""
cor "\"They'll see the sunrise!\""
unk "\"Exactly!\""
cor "\"I've always wondered what it's like outside Batavia.\""
"I'd very much like to hear more."
unk "\"You'll see for yourself one day, Cornelis, when you're old enough.\""
unk "\"And with it, all the beauty the world has to offer.\""
cor "\"May I... read the book?\""
unk "\"Piqued your interest, have I?\""
"It's difficult not to. Father only lets me read business ledgers."
unk "\"It's right there, on my desk. Have at it. The paint has yet to dry, anyway.\""
cor "\"Thank you very much, sir!\""
scene black with slow_dissolve
stop music fadeout 3.0
unk "\"Do please stop calling me sir, young man. I'm your grandfather, not the King of Batavia.\""
scene averytent with slow_dissolve
play background "sfx/desertmorning.ogg" fadein 3.0
"An unpleasant warmth is the first thing I feel when I wake."
"The second, a warm, sweaty body draped over mine."
"My vision's blurred without my glasses, but the white fur is unmistakable."
"He’s sleeping soundly, long tail flicking against my leg much like it did the first night we spent together."
"Much as I'd like to let him stay, his weight and the heat radiating from him are coming close to suffocating me."
"After all the setbacks I have – we have – suffered, I'd rather not have my life ended by one of my bedfellows rolling over on top of me."
cl "\"Samuel?\""
"Thirst stings the back of my throat as I speak. It would seem last night's merriment took quite a lot out of me."
"I give him a little tap on the head."
"It gets little reaction from him."
"His tail flicks against my leg again."
"It tickles, and I can't keep myself from twitching."
play music "music/popgoestheweasel.ogg"
cl "\"S–Samuel!\""
"I struggle to get out from under him, but his weight has reduced me to writhing rather awkwardly."
"Quite unbecoming, but it does cause him to stir and finally open his eyes."
"Without my glasses, I can only see the color, that brilliant red, and immediately all is forgiven."
"He makes a sound, somewhere between a grunt and a purr, and yawns."
stop music fadeout 3.0
show sam neutral -talking n at center,avtent with dissolve
m @talking "\"Mornin', Professor.\""
play music "music/busymorning.ogg"
cl "\"Um, you are–\""
"He looks down, no doubt realizing he's crushing me."
m flustered @ talking "\"Oh, 'm sorry.\""
cl "\"Oh heavens, no! It's quite alright.\""
"Putting on airs has become as comfortable as slipping into a shirt."
"My voice manages to goes up in pitch when I’m around him."
cl "\"Did you sleep well?\""
m neutral @ talking"\"Yeah.\""
show sam smile with dis
"Not one for morning conversation. I'm used to it by now."
"Father always told me I could talk for two."
m neutral @ talking "\"Uh, did you?\""
cl "\"Like a rock, as you say over here.\""
hide sam with dissolve
"He gets up, on his knees, and I savor the breath I've been holding in these past long minutes."
"He seems to regard my predicament with a degree of amusement."
"And while I usually cannot tell whether his affection for me is genuine, or just part of his profession, this smile in particular seems true enough to me."
"I don't quite know what time it is at the moment."
"It still looks rather dark out."
"I haven't heard anyone call for me yet."
"For all I know, we still have hours before we need to leave."
"And it still wouldn't be enough."
"His fingers dance down my chest."
"My heart thumps underneath them, a bit more frantically than I would like."
"He looks anything but restless."
"It's the first time I've seen him without a furrowed brow, without bags under his eyes."
"I sit up, and he leans forward, meeting me halfway."
"The kiss we share is long, and yet all too brief for my liking."
"I don't know what he's feeling right now, but it's the only way I can convey what I truly feel, what even I lack the vernacular to express."
"How I wish it did not have to be this way."
"How I wish I could spirit him away in the dead of night, to some far-off foreign country where no one knows our names."
"Where we can shed the hand of cards society has dealt us and start fresh."
"Where both of us can stop pretending to be people we are most certainly not."
"But once all of this is over, I might never meet this man again."
"When I pull away from him, the world feels a lot colder."
"I take solace in his paw cupping my cheek, and clasp it tightly."
cl "\"Thank you.\""
show sam smile n at center,avtent with dis3
m "\"Whatcha makin' a sad face for?\""
cl "\"Oh.\""
"I put on my brightest smile once more."
cl "\"Absolutely nothing to be worried about. Just... anxious to get to work.\""
show sam talking n with dis
m "\"There ever a time when you're not thinking about this work?\""
show sam neutral -talking n with dis
"He's as frank about the subject as ever."
cl "\"Well, there was last night.\""
show sam smile n with dis
m "\"Yeah.\""
cl "\"I've not had the time for revelry since my days at university.\""
show sam surprised talking n with dis
m "\"Revel... revelry?\""
show sam neutral -talking n with dis
cl "\"Parties.\""
show sam talking n with dis
m "\"Right.\""
show sam eyes -talking n with dis
"He repeats the word to himself once more, to memorize it, by the looks of it."
show sam -eyes talking n with dis
m "\"Didn't picture you to be the partying type.\""
show sam smile n with dis
m "\"What are university parties even like?\""
cl "\"What do you think they're like?\""
show sam talking n with dis
m "\"Bunch of smart folks in a room talkin' about how smart they are.\""
show sam neutral -talking n with dis
cl "\"Not too far from the truth, I must admit.\""
cl "\"Usually there's wine involved.\""
show sam annoyed with dis
"He makes a face."
show sam talking with dis
m "\"I'll take whiskey and beer over wine.\""
show sam -talking with dis1
hide sam with dis
mu "\"Hey, you folks alive in there?\""
"We scramble away from each other, struggling to put our clothes back on in such a cramped space."
"Quite amusing, considering the ease with which we slipped out of them only a few hours ago."
"It would seem Samuel recovered his change of clothes from what was left of our supplies yesterday."
"Shame. I'm going to miss the overalls Avery put him in. He looked cute as a button in them."
cl "\"J-just a minute!\""
"My regular clothes are all the way at the bottom of my pack, sitting neatly folded underneath my bag of taffies as if I'd never disturbed them."
"I'd forgotten all about them."
"So much has happened since I last opened this thing."
"I can't seriously be nostalgic for something that only happened a few days prior, and yet here I am, getting sentimental over a bag of candy, of all things!"
"I take it out and hold out the bag to Sam, who's got one leg in his trousers already."
m "\"Oh, thanks.\""
cl "\"You're very welcome.\""
"Once I make sure we're both at the very least presentable, I open the flap to the tent."
scene camp
show mur at center, forestdark
show expression AlphaMask("foliage", At("mur", center)) as mask:
    alpha 0.35
with slow_dissolve
play music "music/murdochtheme.ogg" fadein 3.0
"Mr. Byrnes' bright red fur and brighter smile is the first thing that greets me."
"I force my brightest smile in turn."
cl "\"Yoohoo, Murdoch!\""
show mur talking
show expression AlphaMask("foliage", At("mur talking", center)) as mask:
    alpha 0.35
with dis3
mu "\"You sure took a while. Almost had me worried you wouldn't come out at all.\""
show mur smile
show expression AlphaMask("foliage", At("mur smile", center)) as mask:
    alpha 0.35
with dis
cl "\"Oh, did we leave you all waiting?\""
show mur talking
show expression AlphaMask("foliage", At("mur talking", center)) as mask:
    alpha 0.35
with dis
mu "\"Just me. Avery and Jebediah are still sleeping too.\""
show mur mischief
show expression AlphaMask("foliage", At("mur mischief", center)) as mask:
    alpha 0.35
with dis
mu "\"You and Sam weren't the only ones going off together last night.\""
if SMC_Points == 1:
    show mur talking
    show expression AlphaMask("foliage", At("mur talking", center)) as mask:
        alpha 0.35
    with dis3
    mu "\"I was feeling awful lonely, you know. And after we had such a lovely evening at the springs the other night.\""
    show mur smile
    show expression AlphaMask("foliage", At("mur smile", center)) as mask:
        alpha 0.35
    with dis
    m "\"This tent's already barely fitting both of us.\""
    show mur mischief
    show expression AlphaMask("foliage", At("mur mischief", center)) as mask:
        alpha 0.35
    with dis
    mu "\"You know as well as I do I have no problem slipping into tight spaces, Sam.\""
    mu "\"Isn't that right, Cliff?\""
    "I feel my face grow warm despite myself."
    cl "\"I, erm...\""
    show mur concerned d
    show expression AlphaMask("foliage", At("mur concerned d", center)) as mask:
        alpha 0.35
    with dis3
    mu "\"You did enjoy it, right?\""
    cl "\"Well of course I did.\""
    mu "\"But what I'm saying is that it wasn't just another roll in the hay, right?\""
    mu "\"It was thrilling!\""
    mu "\"And damn right special.\""
    cl "\"No, no, I think so too.\""
    mu "\"You'd like to keep doing things like that, right?\""
    cl "\"Well, of course I would.\""
    cl "\"At least whenever the circumstances allow.\""
    show mur fear d
    show expression AlphaMask("foliage", At("mur concerned d", center)) as mask:
        alpha 0.35
    with dis
    mu "\"Well, what's that supposed to mean?\""
    menu murdochtent:

        "That as strange as life can be, I'd like you in mine as much as possible.":
            $ SMC_Points = 1
            cl "\"I said that you were special to me and I meant it.\""
            cl "\"The both of you.\""
            show mur smile
            show expression AlphaMask("foliage", At("mur smile", center)) as mask:
                alpha 0.35
            with dis3
            "He perks up."
            show mur talking
            show expression AlphaMask("foliage", At("mur talking", center)) as mask:
                alpha 0.35
            with dis
            mu "\"The spring should still be free if you want to go again.\""
            show mur
            show expression AlphaMask("foliage", At("mur", center)) as mask:
                alpha 0.35
            with dis3
            "I click my tongue at him."
            cl "\"You're incorrigible.\""
            show mur mischief
            show expression AlphaMask("foliage", At("mur mischief", center)) as mask:
                alpha 0.35
            with dis3
            mu "\"You didn't seem to mind last night.\""
            "It's true. I feel a shiver crawl up my back just recalling last night's events."
            "The manner in which they both looked down at me."
            "Their taste on my tongue."
            "I stop myself before my thoughts get too explicit."
            hide mur
            hide mask
            with dissolve
            "I look behind me to gauge Sam's reaction."
            "He gives me the smallest of nods."
            if HaveMap == True:
                "There's a smile on his face once more, as if it never left in the first place."
            show mur mischief at center,forestdark
            show expression AlphaMask("foliage", At("mur mischief", center)) as mask:
                alpha 0.35
            with dis3
            cl "\"We do still have some space left in our tent, cramped as it is.\""
            cl "\"Want to come in for a little while?\""
            mu "\"I'd be right happy to.\""
            scene black with slow_dissolve
            stop music fadeout 3.0
            jump aftertent



        "That this was a fun diversion. But the future holds many hoops.":
            $ SMC_Points = 0
            cl "\"I had a fantastic go in the springs with you, but... I'd rather we stay on professional terms. At least for now.\""
            cl "\"There's still a lot of work to be done, and I don't want to complicate matters.\""
            show mur sad
            show expression AlphaMask("foliage", At("mur sad", center)) as mask:
                alpha 0.35
            with dis3
            "His ears flick back."
            "For a moment, his expression shifts, and I see an intense emotion I've not seen before."
            "Disappointment, perhaps."
            "Or something closer to an expression that feels like..."
            "Nothing at all?"
            "Disquieting."
            mu "\"Very well, sir.\""
            mu "\"The photographs of your trip will be developed post-haste.\""
            cl "\"I'm sorry.\""
            show mur mischief
            show expression AlphaMask("foliage", At("mur mischief", center)) as mask:
                alpha 0.35
            with dis3
            "He quickly puts on that same cheeky grin again."
            "Maybe he's fine after all?"
            mu "\"I'm not. Been a while since I had a night like that!\""
            mu "\"I'll get to waking up the others. Shouldn't be long.\""
            show mur smile
            show expression AlphaMask("foliage", At("mur smile", center)) as mask:
                alpha 0.35
            with dis3
            cl "\"Thank you, Mr. Byrnes.\""
            scene black with slow_dissolve
            stop music fadeout 3.0
            jump aftertent

else:
    show mur eyes talking
    show expression AlphaMask("foliage", At("mur eyes talking", center)) as mask:
        alpha 0.35
    with dis3
    mu "\"I had to listen to that old coyote ramble on for hours.\""
    show mur talking
    show expression AlphaMask("foliage", At("mur talking", center)) as mask:
        alpha 0.35
    with dis3
    mu "\"I thought he was never going to head to bed.\""
    show mur smile
    show expression AlphaMask("foliage", At("mur smile", center)) as mask:
        alpha 0.35
    with dis
    "He does smell like alcohol and tobacco."
    "Not the most appealing of scents."
    cl "\"We're so sorry. We were just—\""
    show mur mischief
    show expression AlphaMask("foliage", At("mur mischief", center)) as mask:
        alpha 0.35
    with dis
    mu "\"Preoccupied. I know.\""
    show mur talking
    show expression AlphaMask("foliage", At("mur talking", center)) as mask:
        alpha 0.35
    with dis
    mu "\"I'm not going to pry this time. I promise.\""
    show mur sideeye
    show expression AlphaMask("foliage", At("mur sideeye", center)) as mask:
        alpha 0.35
    with dis3
    mu "\"And Cliff?\""
    "His voice is lower now."
    cl "\"Yes?\""
    show mur concerned d
    show expression AlphaMask("foliage", At("mur concerned d", center)) as mask:
        alpha 0.35
    with dis
    mu "\"Be careful with Sam, alright?\""
    mu "\"If my hunch is right, he's been through a lot.\""
    "The man doesn't even know half the story."
    cl "\"I'll be careful, don't you worry.\""
    mu "\"Good.\""
    show mur talking
    show expression AlphaMask("foliage", At("mur talking", center)) as mask:
        alpha 0.35
    with dis3
    mu "\"I'll go wake up the others then.\""
    show mur smile
    show expression AlphaMask("foliage", At("mur talking", center)) as mask:
        alpha 0.35
    with dis3
    "His voice is back to its usual jovial tone."
    "The man's a far better actor than I could ever hope to be."
    scene black with slow_dissolve
    stop music fadeout 3.0
    jump aftertent
label aftertent:
scene desertmorning with slow_dissolve
play music "music/nonsense.ogg" fadein 10.0
$ renpy.music.set_volume(0.35, delay=1.5, channel='background')
play background "sfx/desertmorning.ogg" fadein 5.0
"After we bid goodbye to everyone we met last night, we once again set off, hopefully for the last time."
"It's amusing, in a way."
"My studies have taken me to places far more seasoned explorers were afraid to tread, yet none of my journeys have been quite as perilous or as fraught with terror as this one."
"I wonder what my superiors will say about what happened to me if I present it all with naked honesty."
"I wonder what they'd think of Echo, that bustling jewel in the sand, and of its inhabitants."
"I doubt most of the things that transpired will even make it into my report once all of this is done."
"A monster coming for us in the night? A man murdered in a mine? A mysterious cabin out in the woods?"
"Last but not least, a rat getting whisked away with no one knowing where he went?"
"They'd probably reject it outright."
"And then there's Samuel and Murdoch."
"Well, that part of my story will certainly remain private for now."
"I'll have to settle for treasuring these last few days I can spend with them."
"Perhaps, by the time I'm old and decrepit, it might make for a nice chapter in my autobiography."
"As the sun slowly ascends the sky, I once again feel the scorching desert heat bearing down on me."
"We've scarcely left the camp and my shirt is already clinging to my fur."
"After I just bathed this morning, too."
"That's one thing I'm not going to miss about this place."
show sam neutral -talking at center,sunset with dissolve
show sam talking with dis
m "\"How much ground are we covering today?\""
show sam neutral -talking with dissolve
"I'm quite jealous of the composure Sam carries in public in the wake of terror."
"Whether it's all a front or not, he makes it look easy."
"I wish that Clifford Tibbits — that {i}I{/i} could be that confident."
show sam talking with dissolve
m "\"Cliff?\""
show sam neutral -talking with dissolve
cl "\"Oh!\""
"Caught myself daydreaming again."
"I clear my throat. My muzzle's dry again."
cl "\"We should be there in a... little while, I'd say.\""
show jeb happy at right,sunset with dis3
jeb "\"Not too long now. Y’all still got legs to stand on?\""
show mur mischief at left,sunset with dis3
mu "\"Someone's perky today. Don't you worry, we’ve built up some muscle.\""
show sam surprised with dis
cl "\"We should be getting plenty of time to recuperate in the coming week.\""
"I mostly can't wait to put on my regular clothes again."
show sam shocked with dis3
m "\"A week?!\""
cl "\"Studying takes time, Samuel. A week isn't even that long!\""
cl "\"There are studies which take months, if not years.\""
show sam sad with dis3
show mur eyes talking with dis3
mu "\"So it's a vacation of sorts.\""
"He shrugs nonchalantly."
cl "\"Not for you, it isn't.\""
cl "\"I'll still need someone to take pictures for my thesis, you know.\""
show mur concerned d with dis
mu "\"Too bad. I was looking forward to seeing what sights this town has to offer.\""
show mur mischief with dis3
mu "\"Maybe do some natuurfotografie.\""
hide mur
hide sam
hide jeb
with dissolve
"...He’s butchering it on purpose, isn’t he?"
"Still, it's good enough to get a chuckle out of me."
show ave thinking sad at center,sunset with dissolve
stop music fadeout 6.0
av "\"It's not a happy place, I'll have you know.\""
"That comment seems aimed solely at me. I've little choice but to take it in stride."
m "\"Are there a lot of folks living in the settlement?\""
show ave talking with dis3
av "\"It's not a tenth of the size of Echo, I'd reckon.\""
show ave thinking with dis3
av "\"Folks are only allowed to leave for trade.\""
m "\"At all?\""
show ave serious talking with dis3
av "\"Yeah.\""
show ave serious
show tse at right,sunset
with dissolve
show tse talking with dis
ts "\"And only with permission from the military or an agent.\""
show tse with dis
m "\"Why?\""
show tse angry talking with dis
ts "\"So they can control us. Keep an eye on us.\""
show tse angry with dis
"He scoffs."
show tse angry talking with dis
ts "\"Can't go where we please, can't do as we please.\""
show tse angry with dis
"It pains me to hear that."
"I'm well aware of the way my contemporaries discuss the Meseta, as well as other tribes like them, but still... it's quite disheartening."
"I strive to improve relations between us, so we can understand one another."
"The last thing I want is to dismantle our relationship further."
cl "\"Has anyone ever raised a fuss about it?\""
show ave thinking sad with dis3
av "\"Believe me, plenty people have.\""
av "\"But we don't make the rules.\""
show tse angry talking with dis
ts "\"Their military is all too happy to bend their own to take what they want from us.\""
show tse angry with dis
cl "\"I'm sure with the correct reasoning...\""
show ave thinking eyes with dis3
"I trail off as their eyes bore into me."
"How do you go about changing a situation like this?"
"The desert isn't a good place to ponder matters like these, either way. I'm starting to get parched."
hide ave
hide tse
with dissolve
stop music fadeout 2.0
stop background fadeout 2.0
scene deserttrail with slow_dissolve
play background "music/windbirds.ogg" fadein 10.0
"By the time the sun's looming high in the sky, we reach a large town gate not unlike Echo's."
"There are two canines posted at the entrance, but their garb doesn't resemble what I know of Meseta clothing."
"And they look armed to the teeth."
"Jebediah walks on ahead to talk to them."
"One of them turns his head to give us a once-over."
"Even after focusing his attention on Jebediah once more, his eyes stay glued to Avery and our fisherman friends."
"It's a look of utmost disdain I've not seen the likes of since the gentlemen at Saguaro's Hip brought me outside."
"He finally tips his head back, shouting something I can't quite make out."
play sound "sfx/rustygate.ogg"
"Jebediah beckons us near, and the sturdy metal gates open with a shriek that might very well be loud enough to wake up the entire settlement."
scene reservation with slow_dissolve
stop sound
play music "music/mellowpiano.ogg" fadein 2.0
"Or... no one, it seems."
"The streets are mostly empty."
"It’s as densely packed as a charming little town could be, but there are no people to fill that denseness. No joy to fill the silence."
"No laughing children, no sound of young men hawking newspapers, no ladies discussing gossip on the square."
"What is there just feels hollow, eerie, as if abandoned in a hurry."
"None of the unique architecture I've read about is present, and neither are the colorful fabrics I saw at Manaba's home - in fact, there's nary a speck of color to be found at all."
"Not just the gate resembles Echo, but the entire town; from its wooden buildings to the position of the lone church sitting on the other end of the long street we're in."
"All of the woodwork painted entirely white... it's quite striking."
"A stark contrast to the rather drab architecture around it."
show sam neutral -talking at center
show mur concerned d at right
with dissolve
show sam talking with dis
m "\"Odd to call this place a settlement when I don’t see nobody.\""
show sam neutral -talking with dis
cl "\"They're most likely still asleep.\""
show mur fear d with dis
mu "\"But it's... what, noon?\""
show sam talking with dis
m "\"Afternoon nap, maybe?\""
show sam neutral -talking with dis
show mur concerned d with dis
mu "\"Can't see a thing through the windows.\""
mu "\"If anyone's home, they're pretty well-hidden.\""
cl "\"Strange.\""
hide mur
hide sam
with dissolve
"We head down what I assume to be Main Street. Whereas Echo was lived-in and dirty, the settlement is immaculately clean, almost frighteningly so."
"Even the smell isn't as bad."
"Quite pleasant, actually. Must be the desert blooms I see potted around here and there."
stop music fadeout 2.0
stop background fadeout 2.0
play sound "sfx/bells.ogg"
show sam shocked at center with dissolve
m "\"Christ!\""
"We all look up at quite possibly the loudest church bells I've ever heard in my life."
"They leave a ringing in my ear long after they're done sounding."
play background "music/windbirds.ogg" fadein 10.0
scene residential church with slow_dissolve
show mur concerned d at right with dissolve
mu "\"Looks like there might be a service going on.\""
mu "\"Maybe that's where the welcome party's hiding.\""
show sam neutral -talking with dissolve
show sam talking with dis
m "\"Didn’t think that many Meseta followed Jesus.\""
show sam neutral -talking with dis1
hide sam
hide mur
with dis3
"I notice Avery's expression shifting from curiosity to pain."
"After a few moments, as if they were waiting for us, the doors open."
stop sound
"An imposing heron stands in the doorway, paying us little mind."
"His feathers are as pristine as the fresh paint on the building itself."
"Despite the rather cutting winds, his coal colored cassock doesn't show a hint of sand, wear, or tear."
"It's as though this man only just came off of one of Mr. Ford’s assembly lines, moments ago, smelling like fresh paint."
show ave angry at center with dissolve
"Avery's watching him alongside me. His eyes narrow. His lips purse. He grumbles only one word."
show ave angry talking with dis
av "\"Caldwell.\""
show ave angry with dis1
hide ave with dissolve
"So this is my contact."
"I'd expected him to be more like the people I met in Echo, rowdy and unwashed, but this man looks like he came from another world entirely."
"When we do finally catch his attention, it's as though he's peering right through our beings, looking out into the distance as people stream out of the church and onto the streets."
"But it doesn’t take him long to regard the wind, to brush off his shoulder, and to billow back into the church past the crowd still spilling out."
"Their footfalls are the only sound I hear, rhythmic, loud, as if they're marching in formation. It's quite the sight to see, though I don't know whether to be impressed or unsettled."
"Even so, none of them look particularly happy."
"Those who notice us quickly avert their eyes and disperse, leaving the streets just as empty as they were moments ago."
"All without making a sound."
show sam neutral -talking at center with dissolve
show sam talking with dis
m "\"That was a grim procession.\""
show sam neutral -talking with dis1
show ave thinking at right with dis3
av "\"They aren't too keen on folks from outside. Usually means trouble.\""
show mur concerned d at left with dis3
mu "\"We do kind of stick out here.\""
"Like a sore thumb!"
"Still, that was quite the unusual treatment, even for outsiders."
"I'd hoped we'd finally be out of the metaphorical woods, but it seems trouble is yet brewing."
"I only hope it doesn't get in the way of my work."
cl "\"I hope it's not going to be a problem when we start looking for a place to stay.\""
show sam talking with dis
m "\"I'm surprised you didn't plan that far ahead.\""
show sam neutral -talking with dis
show mur talking with dis3
mu "\"I don't suppose we could stay with one of our travel companions?\""
show mur with dis3
show ave talking with dis3
av "\"They've already got enough mouths to feed as is. No problem though. There's an inn pretty close by.\""
show ave with dis
cl "\"There is? Splendid!\""
cl "\"Sam and Murdoch, would you be so kind as to rent a room or two for our party?\""
cl "\"Please inform the proprietor that money is of no issue.\""
show mur concerned d with dis
mu "\"What are you going to do in the meantime?\""
cl "\"I have business to attend to.\""
hide mur
hide sam
with dissolve
show ave talking with dis
av "\"So do we. Right, Jeb?\""
show ave with dis1
show jeb happy at left with dis3:
    xzoom-1
jeb "\"Right. I need to barter for a new pair of donkeys if we're hoping to make it back to Echo this year.\""
"The man finally has some spring in his step, and I'm beginning to think Avery played a large part in improving his mood."
"At least based on what I smell on him."
show ave talking with dis
av "\"We can meet up before sundown, if you'd like.\""
show ave with dis
cl "\"Of course!\""
show tse angry with dissolve
show tse angry talking with dis
ts "\"No, thanks. We're off to pack our catches, and then we'll have to see Shilah's folks to tell them...\""
show tse with dis
"He pauses. His expression softens considerably, albeit for a moment."
"A rare occurrence."
show tse talking with dis
ts "\"...what happened.\""
show tse with dis
cl "\"Is it okay if I come ask you some questions later?\""
cl "\"It won't take long. I promise.\""
show tse eyes talking with dis
ts "\"Fine, I guess.\""
show tse with dis
cl "\"Splendid!\""
hide tse
hide jeb
hide ave
with dissolve
"The group splits up just as we arranged, and at last, I breathe out a sigh."
"It's my first time alone in days, but it doesn't feel particularly freeing."
"It only feels more stifling."
"Especially with that heron still standing in the doorway of the church building, as if he was waiting for everyone else to leave."
"He walks over to me in long strides, making no sound, his expression unchanging."
"It's like this man is walking on air."
stop background fadeout 3.0
play music "music/foreman.ogg" fadein 3.0
show cal arm at center with dissolve
show cal arm talking with dis3
ca "\"I suppose you were the one they sent from Echo?\""
show cal arm with dis3
"His voice is higher in pitch than even mine, breathy, like the murmurs of a ghost."
"Pale as this man's feathers are, he might easily pass for one."
cl "\"You're Mr. Caldwell, I presume?\""
"He keeps his hands on his back when I offer him mine to shake."
show cal smug arm talking with dis3
ca "\"Reverend Caldwell. And you are...\""
show cal smug arm with dis
"He sizes me up. Not since meeting the proprietress of Saguaro's Hip have I felt so small, so insignificant."
show cal talking arm with dis
ca "\"Cornelis van Houwelinck?\""
show cal arm with dis3
cl "\"Correct.\""
"It feels strange to hear my own name after so long."
"My actual name."
"I can feel my posture shift, my voice lowering, as if I'm getting scolded by my father again."
"He cants his head."
show cal arm talking with dis3
ca "\"Well, Mr. van Houwelinck. You're late.\""
show cal arm with dis3
cl "\"Ah yes, my apologies. We've had quite the eventful journey. Why, I'm surprised we were only delayed by two days!\""
show cal angry arm talking with dis3
ca "\"Two days? I was informed of your departure from Echo two weeks ago.\""
show cal angry arm with dis
cl "\"That can't be possible. We left earlier this week.\""
"Didn’t we?"
"I can't help but doubt my recollection of events."
"I know we left only a few days ago."
"I personally selected the day."
"Am I going insane?"
"The man regards my slack jawed stare by shaking his head."
show cal eyes with dis3
ca "\"I care not for the how and why. The fact remains that you're late.\""
show cal talking with dis
ca "\"I'm not an idle man, Mr. van Houwelinck. Were it not for the good this partnership would do for the community, I would have torn up the papers and sent you on your way back outright.\""
show cal with dis
cl "\"I'm terribly sorry.\""
show cal smug with dis
"He pays my apology little mind as he looks behind me, as if testing the temperature of the wind."
cl "\"I must say, I'm quite surprised to see a man of the cloth in a Meseta settlement.\""
show cal smug talking with dis
ca "\"And what, pray tell, is so strange about it?\""
show cal smug with dis1
show cal smug talking with dis
ca "\"Do you not think the people of this fine community deserve salvation?\""
show cal smug with dis
cl "\"I wasn't saying that.\""
show cal angry talking with dis
ca "\"One ought to think before speaking his mind. We are all worthy of God's love. Even the Meseta.\""
show cal angry with dis
"There is a stern degree of what sounds like earnesty there."
show cal eyes talking with dis
ca "\"And it would seem that today He has brought us a great blessing indeed.\""
show cal with dis1
show cal talking with dis
ca "\"You did bring the contract, did you not?\""
show cal with dis
cl "\"I have it in my pack, yes.\""
show cal smug talking with dis
ca "\"Good.\""
show cal smug with dis
cl "\"Could you tell me more? I must confess, I have an incomplete picture of what this venture entails.\""
"Even my contacts could only tell me so much."
"It would seem my benefactor is at least doing the bare minimum of covering his tracks."
show cal talking with dis
ca "\"You're writing a thesis on the Meseta, are you not?\""
show cal with dis
cl "\"I am.\""
show cal eyes talking with dis
ca "\"...And the subject?\""
show cal eyes with dis
"He says that like he knows the answer."
"I repeat it for him anyway."
cl "\"Crossing cultural boundaries through labor to create a unified working force.\""
"I say it slowly so I don't trip over my words, just the way I rehearsed."
show cal smug arm talking with dis3
ca "\"And there we are.\""
show cal smug arm with dis
"He smiles, almost sweetly."
show cal talking with dis3
ca "\"What if I told you the answers to all of your burning questions were right here, under our feet?\""
show cal with dis
cl "\"Are you referring to the settlement?\""
show cal eyes talking with dis
ca "\"Not the settlement. The land.\""
show cal eyes with dis
cl "\"What makes the land so special?\""
show cal arm talking with dis3
ca "\"You must be well aware of the ever-increasing need for railroads, Mr. van Houwelinck?\""
show cal smug arm with dis1
show cal smug arm talking with dis
ca "\"They've become the very veins which pump the lifeblood of our country, transporting people and goods worth more than you or I could ever imagine.\""
show cal smug with dissolve
show cal smug talking with dis
ca "\"And yet we see very little of it. Do you know why that is?\""
show cal smug with dis
"It's as though Father's quizzing me again."
cl "\"The trains don't reach here.\""
show cal talking with dis
ca "\"Correct.\""
show cal with dis
cl "\"You're... planning to expand the railroad through Meseta land?\""
cl "\"Wouldn't that displace all of these people?\""
show cal eyes talking with dis
ca "\"Not at all.\""
show cal with dis1
show cal talking with dis
ca "\"The whole intention of this project is to have them pioneer the construction.\""
show cal with dis
"Goodness gracious."
cl "\"Forgive me for this skepticism, but do you really think that’s prudent?\""
cl "\"I can't see the Meseta agreeing to such an arrangement.\""
show cal smug arm talking with dis3
ca "\"Well, I have to disagree with you there.\""
show cal eyes with dissolve
show cal eyes talking with dis
ca "\"A long term direction and a daily routine are very desirable things.\""
show cal with dis1
show cal talking with dis
ca "\"Fair pay for steady work and access to modern amenities will only help the people living here.\""
show cal with dis
cl "\"Some of these rivers and mountain ranges are considered sacred.\""
show cal eyes talking with dis
ca "\"To the older generation, perhaps, but I can attest to the truth that the youth think otherwise.\""
show cal with dis1
show cal talking with dis
ca "\"I'm a patient shepherd, Mr. van Houwelinck, and I know that most of my flock does not wish to wallow in superstition for a moment longer.\""
show cal with dis1
show cal talking with dis
ca "\"I mean no disrespect, considering such things are your...\""
show cal smug with dis
"His eyes narrow, as if he’s searching for the right word."
show cal smug talking with dis
ca "\"...expertise.\""
show cal smug with dis
"I feel myself blinking."
"...The nerve of this creature!"
"It's taking a considerable amount of energy to hold my tongue at the moment."
"So that's what I've been tromping to hell and back for all these weeks."
"A bloody railroad?"
"He looks at me with a healthy portion of skepticism."
"I take another breath and smile."
show cal talking with dis
ca "\"In return for your assistance, of course, I'll see to it that your studies aren't interrupted and you can roam the area freely.\""
show cal with dis
cl "\"Anywhere I please?\""
"He arches a brow."
show cal eyes talking with dis
ca "\"There are restrictions.\""
show cal eyes with dis1
show cal eyes talking with dis
ca "\"For one, I cannot allow you near the boarding school building without my strict supervision.\""
show cal with dis1
show cal talking with dis
ca "\"After all, we wouldn't want to upset...\""
show cal smug arm with dis3
"He looks me up and down. Slowly."
show cal smug arm talking with dis
ca "\"...the children.\""
show cal smug arm with dis
"Oh really?"
"I think I would be correct in assuming the wellbeing of the children in this man's care is the last thing on his mind."
show cal talking with dis3
ca "\"And please, do not disturb the military men stationed here. They only have the settlement's best interests at heart.\""
show cal with dis
"Does one truly need an armory's worth of weapons to protect a small town's interests?"
"Echo's got little more than Sheriff Adler, and from what my contacts could tell me, it's usually enough."
cl "\"That won't be a problem.\""
show cal eyes talking with dis
ca "\"Also, I trust Mr. Hendricks told you that this deal is strictly under the table, at the very least?\""
show cal with dis1
show cal talking with dis
ca "\"Neither your friends nor the Meseta are to know.\""
show cal with dis
cl "\"Of course.\""
"I wasn't even to so much as look at the contract's contents, according to Mr. Hendricks."
"He was very insistent."
show cal talking with dis
ca "\"Deliver the papers to me at the church after sundown. Until then, you may do as you'd like.\""
show cal with dis
cl "\"Thank you! I'll do just that.\""
show cal arm talking with dis3
ca "\"Oh, and Mr. van Houwelinck?\""
show cal arm with dis3
cl "\"Y–yes?\""
show cal smug arm talking with dis3
ca "\"Do heed my warnings. I'd hate to see you or your friends end up in places you shouldn't be.\""
show cal smug arm with dis
cl "\"Yes, sir. Thank you, sir.\""
hide cal with dis3
"With a curt bow of his head, he walks, no, glides back to the church, leaving me all alone in the town square, and more confused than I'd like."
stop music fadeout 5.0
play background "music/windbirds.ogg" fadein 5.0
"Really, now..."
"Are you kidding me?!"
"Does he really think he can get me to do entirely what he wants after acting so rude?!"
"It's obvious this man has something to hide, and even more obvious he's rather poor at doing so..."
"But what could it be?"
"Perhaps I should investigate. I'm sure the townspeople can give me at least something to work with."
"But then again, I should be working on my thesis as well."
"If trouble happens to find me when I’m doing the work, then he can only blame himself!"
"I should still have some time before Sam or Murdoch comes looking for me."
"I'm probably best off looking for some familiar faces first."
"Tsela and Yiska will do."
"Right..."
"I think this is the building I saw the both of them walk into."
play sound "sfx/knock.ogg"
"I knock on the front door, and I wait."
"Curiously, much more of a western log cabin that I had expected."
"I see some hogan structures closer to the treeline, but they don’t look as well-maintained as the one Gad and Manaba live in."
play sound "sfx/dooropen.ogg"
"The door opens."
show tse surprised at right with dissolve
"When the kit fox sees me he looks behind me, as if expecting somebody else."
show tse talking with dis
ts "\"Does Avery bring more information about the attack?\""
show tse with dis
cl "\"Not quite.\""
show tse talking with dis
ts "\"Unfortunate.\""
show tse with dis1
show tse talking with dis
ts "\"Tell me when he wants to discuss the attack with me.\""
show tse surprised with dis
"He’s about to close the door again when I put my foot forward."
cl "\"By kismet, it just so happens that I want to talk to just you and Yiska alone.\""
show tse angry with dis
"He tilts his head and narrows his eyes."
show tse angry talking with dis
ts "\"Why?\""
show tse angry with dis
cl "\"Because I want to know more about the people who live here... and used to live here.\""
show tse with dis
cl "\"And I have some information that could be relevant still to your futures.\""
cl "\"An open line of communication is all that I’m asking for.\""
"When he opens the door a little more I stumble forward."
show tse talking with dis
ts "\"Fine.\""
show tse with dis1
stop background fadeout 3.0
scene yistsecabin with slow_dissolve
play music "music/hogan.ogg" fadein 3.0
"The cabin is far cozier on the inside than it looks.\""
"Framed pictures of pressed leaves line the wall. Woven serapes line the walls and chairs by the hearth."
"The bear ignores me while he loads what looks like wrapped fish into an icebox."
show tse with dis3
cl "\"This settlement seems a bit different from what I had pictured for a large Meseta community.\""
cl "\"Have the two of you lived here all of your lives?\""
show tse talking with dis
ts "\"This was father’s first home, but now it is mine.\""
show tse with dis
cl "\"And what about Yiska?\""
show yis surprised at right with dissolve
"The large bear gives me a curious look and wanders my way."
show yis surprised talking with dis
ys "\"Family?\""
show yis surprised with dis1
show yis surprised talking with dis
ys "\"All of mine have been here for 35 years.\""
show yis surprised with dis
cl "\"I see.\""
cl "\"That’s barely a generation.\""
cl "\"What confuses me, though, is that from what I have gathered from trustworthy sources, the Meseta have had a strong tradition of maintaining a nomadic lifestyle.\""
show tse talking with dis
ts "\"The laws of this country make that impossible for most.\""
show tse with dis1
show tse talking with dis
ts "\"You are from Europa, yes?\""
show tse with dis
cl "\"That’s right.\""
show tse angry talking with dis
ts "\"The truth is that it would have been best for everybody if your ancestors stayed there.\""
show tse angry with dis
"My cheeks feel a little bit flushed."
show tse with dis
cl "\"I want to believe that a world where everybody understands one another better leads to compromise, and respect.\""
show tse talking with dis
ts "\"Understanding one another also exposes vulnerabilities, yes?\""
show tse angry with dis1
show tse angry talking with dis
ts "\"Exploitable vulnerabilities.\""
show tse angry with dis
cl "\"I would suppose that could be a reasonable position to take.\""
show tse angry talking with dis
ts "\"The collective information that my people give freely tends to be used by your people against them.\""
show tse angry with dis
"The large bear shifts his weight."
show yis talking with dis
ys "\"Tsela is right.\""
show yis with dis1
show yis talking with dis
ys "\"I know that I am strong, and I do not fear to be understood, but I am just one person.\""
show yis with dis1
show yis talking with dis
ys "\"I can talk to you about myself, but I will not talk to you about my people.\""
show yis with dis
show tse talking with dis
ts "\"But now that we have talked so much already, you said that you had information to share?\""
show tse with dis
cl "\"That’s right.\""
"I feel like they have a right to know what’s coming."
"But Tsela does have a point."
"If I tell them too much, that places a considerable amount of scrutiny on myself and all of my endeavors."
"I wonder if there’s some sort of compromise we can come to where everybody could win here."

menu cliffint1:
    "Do you think a train transportation network would be helpful for the people in this settlement?":
        show tse angry talking with dis
        ts "\"No.\""
        show tse angry with dis
        cl "\"No?\""
        show yis eyes with dis
        "Yiska hums thoughtfully."
        show yis talking with dis
        ys "\"I think I disagree with Tsela in this case.\""
        show yis smile with dis
        ys "\"That could make our lives a lot easier.\""
        show tse talking with dis
        ts "\"It won’t.\""
        show tse angry with dis1
        show tse angry talking with dis
        ts "\"It is foolish to think any gift from these people does not have a terrible cost.\""
        show tse angry with dis
        show yis talking with dis
        ys "\"If it means we could see our families or sell our game to more people, then I want it.\""
        show yis with dis
        "Tsela sucks on his teeth and shakes his head."
        show tse angry talking with dis
        ts "\"More people who couldn't care whether we live or die. I say no.\""
        show tse angry with dis
        show yis angry talking with dis
        ys "\"We haven't been doing as well as we could.\""
        show yis angry with dis
        show tse angry talking with dis
        ts "\"And we'll be doing even worse if we let them trample over us.\""
        show tse angry with dis
        "He narrows his eyes at me."
        show yis talking surprised with dis
        ys "\"Tsela...\""
        show yis surprised with dis
        cl "\"I-I'll take my leave. I'm sorry to have bothered you.\""
        "I make my way toward the door, probably only having worsened the situation. Yiska follows me."
        show yis talking with dis
        ys "\"Forgive my friend. He's been rather emotional these past few days.\""
        show yis with dis
        show tse angry talking with dis
        ts "\"You're talking about me like I'm not here.\""
        show tse with dis
        cl "\"I-it's quite alright. We've had a long few days.\""
        show yis talking with dis
        ys "\"I would be happy to answer questions later, if you are curious.\""
        show yis with dis
        cl "\"Truly? Thank you.\""
        show yis smile with dis
        "The bear smiles."
        show yis talking with dis
        ys "\"Only one thing I want to ask from you.\""
        show yis with dis
        cl "\"Which would be?\""
        show yis talking with dis
        ys "\"Do not listen to the man in the church.\""
        show yis with dis
        "Before I can ask what the meaning is behind his words, he shuts the door, and I'm left outside."
        "Very strange."
        jump aftercliffint1

    "There are plans to expand the Echo train station through the settlement.":
        $ CorMor += 1
        $ tsyis = True
        "Both of the men look at one another, then to me."
        show tse talking with dis
        ts "\"That must never happen.\""
        show tse with dis1
        show tse talking with dis
        ts "\"A connection from there to here must not be established.\""
        show tse angry with dis1
        show tse angry talking with dis
        "Tsela hisses something that I cannot understand."
        show tse angry with dis
        "I can tell that it was something in the Meseta language, but not vernacular that I am familiar with."
        show yis angry with dis
        "Yiska’s brow furrows and he looks a little sickened."
        "I can’t guarantee that James would cancel a contract like this if they did happen to dig up something scandalous on the Reverend, of course."
        "But I’m not exactly lying to them."
        cl "\"Things certainly don’t seem very ordinary to me around here.\""
        cl "\"If the Reverend isn’t conducting himself in a way that is befitting civilized society, then I do not wish to reward him.\""
        cl "\"So let’s help one another.\""
        "I hold out a paw."
        show tse surprised with dis
        "The kit fox looks at it like it’s a dead thing I dragged out of the road."
        show tse angry with dis
        show yis smile with dis
        "But the bear takes it and shakes it firmly."
        show yis eyes talking with dis
        ys "\"I’ll put some leads together for you tonight.\""
        show yis eyes with dis
        cl "\"Good on you, man! Good on you.\""
        "What a pity it would be for that puffed up poultry for there to be some reason his railroad project can’t get off the ground."
        "James might be disappointed if this venture doesn’t turn out well, but I’m sure he has backup plans for other routes just in case."
        "And if that goes poorly too, then Father will just have to cope with that."
        jump aftercliffint1

label aftercliffint1:
play background "music/windbirds.ogg" fadein 5.0
scene black with slow_dissolve
stop music fadeout 3.0
"I check my watch."
"I should still have time to look into some matters."
"I walked for ages to get here. I need new contacts."
scene reservation with slow_dissolve
"Surely there has to be a general store or a trading post."
"Those are always a good place to start when you don’t know anybody."
play sound "sfx/applebite.ogg"
"I stop walking when I hear a crunching noise behind me."
show jeb at center with dissolve
"It’s Jebediah."
"He’s holding a bright, shiny apple with a recent bite mark in the flesh."
show jeb talking with dis
jeb "\"You seem like you’ve been busy.\""
show jeb with dis
cl "\"Yes, well, what else is new?\""
cl "\"I can hardly complain.\""
cl "\"This is an extraordinary opportunity for me, after all.\""
show jeb doubt talking with dis
jeb "\"I meant with the skirt.\""
show jeb doubt with dis
"He jerks his head toward the church."
"What an odd thing to say."
"He’s not usually one to speak, or ask questions for that matter."
show jeb with dis
cl "\"The clergy has closer connections to the people here than the magistrate.\""
cl "\"Reverend Caldwell is speaking on my behalf to the town’s officials to let us stay here for a while.\""
cl "\"For my studies.\""
show jeb shocked with dis
"He blinks."
show jeb shocked talking with dis
jeb "\"Clergy aren’t supposed to have much direct say in the law.\""
show jeb shocked with dis1
show jeb shocked talking with dis
jeb "\"Their own church forbids it.\""
show jeb shocked with dis
"He’s not wrong."
cl "\"I suspect this is more of a gentle request than a demand.\""
show jeb talking with dis
jeb "\"Gentle, huh?\""
show jeb with dis
"I don’t really want to linger on this subject for very much longer."
cl "\"That apple looks delicious!\""
cl "\"Where could I buy one myself?\""
show jeb doubt with dis
"He lifts his eyebrows, but he says nothing."
show jeb talking with dis
jeb "\"Trading post is the wooden cabin with the red tin roof.\""
show jeb with dis
cl "\"Splendid. I’ll be back in a jiffy.\""
"I can feel his eyes resting on the back of my neck as I walk away."
"I can’t blame him for being suspicious of this place."
"But surely he knows that he can trust me."
"I am his employer after all."
stop background fadeout 3.0
scene settlementstore with slow_dissolve
play music "music/generalstore.ogg" fadein 3.0
play sound "sfx/entrancebell.ogg"
"A small bell rings when I walk through a wooden door."
"It’s a modest little trading post, but there’s something of everything: canned food, oil lamps, fishing poles, hardware tools."
"An old looking gray squirrel is manning the cash register while what looks to be her daughter helps her stock the shelves."
stop sound
cl "\"Good afternoon, my dear!\""
"She looks at me with a facial expression that is impossible to read... not angry, nor cheerful. Nor bored, not bothered."
"Withdrawn, perhaps?"
cl "\"My friend tells me that you sell delicious apples here?\""
"She points to a crate full of them by the door."
cl "\"Oh, good!\""
cl "\"Well, I’d like to pay for a dozen, then.\""
"She tells me the price, and then says nothing else."
cl "\"Not a bad price at all!\""
cl "\"My friends and I are in a bit of a pickle, and we need a lot of supplies and provisions to make up for what we lost on the road.\""
cl "\"Where else could we go in town for supplies?\""
"Squirrel" "\"This is the only store.\""
cl "\"I don’t mind going out of my way.\""
cl "\"I’ve traveled about two weeks on foot already just to get here.\""
"Two weeks... there's a noticeable waver in my voice when I say those words."
"...I can still hardly believe it's been that long."
"Unless the reverend was playing some sort of twisted joke on me."
"Was it the forest? It couldn't have been..."
"Squirrel" "\"This is the only store.\""
cl "\"No markets? No craft exchanges?\""
"She just repeats the same line."
"She isn’t impatient with me. She isn’t angry."
"It feels like I’m interacting with a recording."
"None of this makes sense to me at all."
"Surely one store like this wouldn’t be able to serve an entire community."
"Nothing about it speaks to the presence of a Meseta community save a paltry section selling pottery and some woven fabrics."
cl "\"If there are no other ways to buy goods, then surely there are other ways this community helps one another?\""
cl "\"Even if there’s not much I can purchase, I’d still love to know more about how the people here cooperate.\""
"She shrugs."
"Squirrel" "\"What can’t be bought is made or grown or traded.\""
"Squirrel" "\"Rations are distributed weekly by the township.\""
"Squirrel" "\"What is sold here is for those visiting, or passing through.\""
"Squirrel" "\"People with money.\""
cl "\"I suppose that makes me wonder.\""
"Squirrel" "\"Wonder what?\""
menu cliffint2:

    "If more people with money came through the area, wouldn’t there be more supplies, and thus... more business?":
        cl "\"It sounds like the way to attract more people to this town would be helpful for the community.\""
        "Squirrel" "\"More money means less reliance on provisions, and that would be welcome.\""
        cl "\"A railway system would make that easier.\""
        "I see a glint in the older woman’s eye."
        "Squirrel" "\"You think that the railroads will come here?\""
        cl "\"I can’t really say for sure.\""
        "Squirrel" "\"Well, I hope you are on to something.\""
        "Squirrel" "\"Seeing something like that would give me hope.\""
        "Squirrel" "\"There’s family I want my daughter to meet.\""
        cl "\"Hope is free, thankfully.\""
        cl "\"It sounds like there aren’t enough opportunities to make money here.\""
        "Squirrel" "\"There aren’t.\""
        cl "\"But why not?\""
        cl "\"Surely there’s arable land here.\""
        cl "\"This town is close to a major waterway.\""
        "Squirrel" "\"Some people outside will not buy from you unless you are a citizen.\""
        "Squirrel" "\"Leaving is difficult, but returning is more difficult.\""
        cl "\"I see...\""
        cl "\"You mentioned trade... Is there a robust bartering system in place?\""
        "Squirrel" "\"Not much of one.\""
        "Squirrel" "\"Most Meseta traditions are not desirable to the commonwealth. \""
        "Squirrel" "\"The path to citizenship, and to purchasing land, requires embracing traditions which are.\""
        cl "\"I see.\""
        "Squirrel" "\"Will you buy something else?\""
        "I feel a little paralyzed, to be frank."
        cl "\"...I’ll take a waterskin.\""
        jump aftercliffint2

    "Why is there only enough local business for one store?":
        $ CorMor += 1
        "Squirrel" "\"Most Meseta traditions are not desirable to the commonwealth. \""
        "Squirrel" "\"The path to citizenship, and to purchasing land, requires embracing traditions which are.\""
        cl "\"I see.\""
        "Squirrel" "\"Will you buy something else?\""
        "I feel a little paralyzed."
        cl "\"...I’ll take a waterskin.\""
        jump aftercliffint2

label aftercliffint2:
cl "\"Oh, I want to ask something else.\""
"She looks up from the cash box and stares."
cl "\"Now I don’t mean to come across as superstitious, but on my journey here, my companions and I ran into some bewildering hazards.\""
cl "\"Is there anything in the area you’d advise newcomers to steer clear of?\""
"Squirrel" "\"Visitors come and visitors leave.\""
"Squirrel" "\"There is no danger here that applies to them.\""
"Squirrel" "\"But there are some things to know while you are here.\""
cl "\"Things like what?\""
"Squirrel" "\"The well in the town center is not dry, but nobody drinks from it.\""
cl "\"Why?\""
"She shrugs."
"Squirrel" "\"Everybody gets sick. We draw from the river instead.\""
"Squirrel" "\"Another thing is that the lights in the school are always on after dark.\""
"Squirrel" "\"Nobody goes to see why.\""
"Most curious. Could this have something to do with the reverend's stipulations?"
"Squirrel" "\"Last is that curfew is 8 pm.\""
"Squirrel" "\"Anything bad that has happened to anybody in this town has happened after curfew.\""
"That would be after sundown... just about the time the reverend asked me to bring him the documents."
"Young squirrel" "\"There’s also the trail.\""
"I flinch."
"I had forgotten the daughter was there."
cl "\"What trail?\""
"Squirrel" "\"It is a fairy story. Do not pay it mind.\""
cl "\"But fairy stories interest me quite a bit.\""
"I remember the ones Grandfather used to tell me."
"I'd give anything to read that big old book with the tales from the Brothers Grimm again."
"Young squirrel" "\"You should know that she does pay it mind.\""
"She shakes her head, shushing her."
"Squirrel" "\"It’s just a game that I still play.\""
cl "\"Might I hear the rules?\""
"She purses her lips and crosses her chubby arms."
"Squirrel" "\"There is a trail leading west out of the settlement.\""
"Squirrel" "\"When I was a little, some cousins and I would walk on this trail and feel very unnerved.\""
"Squirrel" "\"We’d face each other, walking backwards, and call out one another’s names, and then...\""
"Squirrel" "\"Well, sometimes we’d swear we could hear one another behind us when we were looking forward, coming from the woods.\""
"Squirrel" "\"I thought I had experienced it once, but it never happened again.\""
"Young squirrel" "\"You said you buried your shoes.\""
"Young squirrel" "\"Because you didn’t want to risk bringing one pebble back.\""
"Squirrel" "\"Something had upset me that night.\""
"Squirrel" "\"But like I said... whatever happened never happened again.\""
"West, they said?"
"That makes me wonder..."
cl "\"Well, thank you for the talk and your time.\""
cl "\"It’s about time for me to scoot along!\""
scene black with slow_dissolve
"She hands me my purchases and I have to put some of the apples into my pack."
"I leave with more questions than I entered with."
stop music fadeout 5.0
play background "music/windbirds.ogg" fadein 5.0
scene reservation with slow_dissolve
play music "music/samueltheme.ogg" fadein 10.0
"And yet, along with a conspicuously large number of apples, I picked up a curious sense of determination as well."
"Unraveling the mysteries of this quaint little town shall no doubt be my largest task yet."
"I look at my watch once more."
"I ought to go and see if Sam and Murdoch succeeded in getting us a room."
"I think I'd do well to get some rest."
"After that, I don't know."
"At the very least, I would do well to find Avery soon."
"He might know more about Caldwell than anyone here is willing to tell me."
"And perhaps he can shed some light on the rumors I just heard."
"If anything, he might be willing to take one of these apples off my hands."
"I don't know how to feel about this settlement quite yet."
"I can't help but ponder what the rest of the week will offer..."


stop background fadeout 5.0
play music ("music/quiet.ogg") fadeout 5.0 fadein 4.0
scene bg black with slow_dissolve
scene bg innlobby with slow_dissolve
"The outside of the inn looks more like a tenement house than a professional setup suited for comfort."
"And the inside of the inn isn’t much to look at either."
"There’s a lobby with a desk and keys flanked on both sides."
"Not so much a place for reception."
"The goose eying us warily doesn’t look Meseta."
show mur smile at right,house1 with dissolve
show mur talking with dis
mu "\"Good afternoon, ma’am.\""
show mur smile with dis
"Goose" "\"Good afternoon.\""
"Goose" "\"Do you need a room for the night?\""
show mur talking with dis
mu "\"Our company will be staying for a week, if that isn’t a problem.\""
show mur smile with dis
"Goose" "\"It shouldn’t be.\""
"Goose" "\"A week for one bedroom will cost you twenty-one dollars.\""
show mur talking with dis
mu "\"Would it be alright if we have access to our rooms a little early?\""
show mur smile with dis
show mur talking with dis
mu "\"We’ve run into several hardships on the road and would love an opportunity to calm ourselves and get our bearings.\""
show mur smile with dis
"The goose shakes her beak."
"Goose" "\"Rooms can’t be rented without an upfront payment.\""
show mur eyes with dissolve
"Murdoch nods with understanding, as if he can recognize that tone of voice a mile away."
show mur talking with dissolve
mu "\"Right then.\""
show mur smile with dis
"He turns to me."
show mur talking with dis
mu "\"It seems like we may have to cough up the cash ourselves or wait for our benefactor to clear this up himself.\""
show mur smile with dis
"I gawk at him."
show mur fear d with dis
m "\"You think I have that much money?!\""
show mur concerned d with dis
mu "\"Well you do work at...\""
"His voice trails off as the goose stares at us."
show mur sideeye with dis
mu "\"...one of the finer establishments in Echo, do you not?\""
m "\"Not that fine.\""
show mur concerned d with dis
"He looks at me with skepticism at first, but then it turns into a gentle alarm."
show mur talking with dissolve
mu "\"Thankfully our patron should be coming along shortly.\""
show mur smile with dis
m "\"...Ain’t there a difference, typically, between what’s short to us, and short to Professor Tibbits?\""
show mur concerned d with dissolve
"Murdoch looks to be processing that."
show mur sideeye with dis
mu "\"Oh God, we could be waiting for hours.\""
show mur concerned d with dis
m "\"That’s what I’m sayin’.\""
"The goose clears her throat."
"Goose" "\"Could you tell me your patron’s name?\""
"Goose" "\"I do have a booking here.\""
show mur eyes with dis
"Me and the red fox both let out sighs of relief."
show mur with dis
mu "\"Oh good.\""
show mur talking with dissolve
mu "\"Is there a Mr. Clifford Tibbits down on the page?\""
show mur smile with dis
"The Goose flips through her booklet with her bony talons."
show mur concerned d with dissolve
"Goose" "\"I’m afraid there isn’t.\""
"Damn it."
m "\"Wait, wait.\""
m "\"Maybe he put it down as Jebediah Coles?\""
show mur talking with dis
mu "\"There’s a good idea.\""
show mur smile with dis
"The fox leans into the counter, places his paw on his hips, and gives the goose his best smile."
show mur talking with dis
mu "\"How about it?\""
show mur smile with dis
"Goose" "\"Well there’s a name I recognize.\""
show mur concerned d with dis
"Goose" "\"But no, he isn’t booked either.\""
"Murdoch’s smile and his eyelids drop immediately."
"He turns to me."
show mur eyes talking with dis
mu "\"We’re running out of options here.\""
"I mutter under my breath."
m "\"Might as well make something up.\""
show mur with dis
"Something about me saying that makes Murdoch’s eyes snap open."
show mur talking with dissolve
mu "\"How about a Mr. Cornelis van Houwelinck?\""
show mur smile with dis
"That name sounds familiar."
"Wasn’t he that painter Cliff mentioned?"
"We probably shouldn’t be wasting this lady’s time."
"But the goose’s eyes flick up from her book."
"Goose" "\"How’s that spelled?\""
"Murdoch takes a piece of paper out of his pocket."
"It looks slightly ripped and stained with dew."
show mur talking with dis
mu "\"Like this.\""
show mur smile with dis
"The goose leans forward, looking."
"Goose" "\"That’s him.\""
"Goose" "\"I don’t much like giving out keys before a down payment, but this is your lucky day.\""
"She unhooks a set of keys off the wall and sets them in the fox’s paw as he puts the paper away in his vest jacket."
show mur eyes with dis
"Goose" "\"Second floor, first door on the right.\""
"I don’t want to say anything now, but I get the feeling I need to know what the hell just happened."
hide mur with dissolve
"I keep my mouth shut for now and follow the fox up the narrow set of stairs to our room, his big tail almost hitting me in the face as we ascend."
scene bg innroom with fade
play sound "sfx/dooropen.ogg"
"Once we’re inside I forget myself for a moment."
"This room is much bigger than I thought it would be considering the conditions of the inn."
stop sound
"It’s bigger than my room at the Hip."
"It ain’t exactly lavish, but I get the feeling it’s nice for a place such as this."
show mur sideeye at right,inn with dissolve
mu "\"Only two beds, huh?\""
show mur eyes with dis
mu "\"Seems like one of us might have to share with Jeb.\""
show mur concerned d with dis
m "\"I know you’re not gonna pretend like what just happened didn’t happen.\""
m "\"Who’s Corn van Hoolick?\""
show mur with dis
mu "\"It’s Mr. Tibbits’s real name.\""
show mur sideeye with dis
mu "\"Or, at least the one he must go by in Europa.\""
show mur talking with dis
mu "\"Here.\""
show mur smile with dis
"He takes a piece of paper out of his pocket and shows it to me."
"I squint my eyes, looking over the letters."
"I guess I butchered it a little."
m "\"So why’s he using a fake name?\""
show mur sideeye d with dis
mu "\"It might not have been his choice.\""
mu "\"My grandparents had to change their names when they immigrated, though they didn’t have to change them by very much.\""
"I think for a second and remember Nik mentioning something similar."
"Nicholas was his official name, though he still preferred Nikolai."
"But he asked us to keep calling him Nik to play it safe, because nobody would be able to tell the difference between that and Nick."
m "\"How did you get that?\""
show mur concerned d with dissolve
mu "\"It was just lying around at the site where we got attacked.\""
show mur sideeye with dis
mu "\"I held onto it because I figured it was important identification papers, but it slipped my mind until you brought up fake names.\""
m "\"Anyway...\""
show mur concerned d with dis
mu "\"What?\""
m "\"Either you or the professor are gonna have to share your bed with Jeb.\""
mu "\"And why’s that?\""
m "\"Because we’re both huge, and you’re both small.\""
show mur angry with dissolve
mu "\"I am not small, Sam.\""
mu "\"I’m just as tall as most other men.\""
m "\"Compared to me and Jeb you’re small.\""
show mur sideeye with dissolve
mu "\"So are most people.\""
m "\"That’s beside the point.\""
m "\"That flimsy little bed couldn’t handle the both of us.\""
show mur talking with dissolve
mu "\"Well what about the doctor?\""
show mur smile with dis
m "\"What about the doctor?\""
show mur talking with dis
mu "\"Where exactly is he staying?\""
show mur sideeye d with dis
mu "\"He and Jeb seem close.\""
show mur talking with dis
mu "\"Maybe he’ll offer him a place to stay?\""
show mur sideeye d with dis
m "\"Sounds like you just want a bed to yourself.\""
show mur eyes talking with dissolve
mu "\"I just have some bad memories where I used to have to share a bedroom.\""
show mur concerned d with dis
mu "\"We had tiny bunk beds we had to share.\""
show mur sideeye with dis
mu "\"I’d wake up against the wall because I couldn’t breathe.\""
show mur concerned d with dis
m "\"Why didn’t you just sleep on the floor?\""
show mur sideeye with dis
mu "\"Because I don’t want to wake up with cramps.\""
mu "\"Bad start to a heavy work day.\""
show mur concerned d with dis
play sound "sfx/softknock.ogg"
"I’m about to say that he wouldn’t get as many cramps if he put some muscle on his back when I hear a knock on the door."
play sound "sfx/dooropen.ogg"
hide mur with dissolve
"He goes to open it and we see Cliff walk in through the door."
stop sound
show mur at right,inn
show cli adv happy at center,inn
with dissolve
cl "\"There you are, men.\""
show cli adv talking with dis
cl "\"I trust setting up the room wasn’t too much trouble?\""
show cli adv with dis
show mur concerned d with dis
m "\"Truth be told—\""
show mur sideeye with dis
mu "\"They almost didn’t let us in.\""
show mur talking with dissolve
mu "\"Did you pay?\""
show mur smile with dis
show cli adv eyes talking with dis
cl "\"I just paid off the room, so no need to trouble yourself with those worries.\""
show cli adv with dis
show cli adv talking with dis
cl "\"Now that we’re here, let’s just let go of our travel worries and strategize how we’re going to spend our time here and how we’re going to make our way back.\""
show cli adv with dis
"A week, huh?"
"That should be enough time to prep and plan a way out of here."
"If I walked, I could probably make it on my own to Camp Rosa."
"But I can’t remember if they have a train station or not."
show cli adv eyes talking with dis
cl "\"I have interviews with the Meseta in the morning from nine to noon, so we should wash and eat breakfast before eight.\""
show cli adv eyes with dis
show mur talking with dis
mu "\"Do you mind if I set up the closet for development?\""
show mur smile with dis
show cli adv talking with dis
cl "\"You’re one step ahead of me, Murdoch.\""
show cli adv with dis
show cli adv eyes talking with dis
cl "\"Just please make sure to keep your chemicals sealed up tight before and after you use them.\""
show cli adv doubt with dis
cl "\"I only have one week to speak with the people here, and I wouldn’t want to embarrass myself with the limited time that I have.\""
show cli adv with dis
m "\"You don’t need much more from me anymore, right?\""
show cli adv talking with dis
cl "\"Thankfully no since we’ve arrived.\""
show cli adv eyes down with dis
cl "\"Though admittedly I would feel a lot better if you made the return trip with us as well.\""
show cli adv with dis
m "\"Cliff.\""
show cli adv sad with dissolve
show mur sideeye d with dis
cl "\"I already know your circumstances.\""
cl "\"I’m merely just voicing my concern after what we went through to get here.\""
show cli adv doubt with dissolve
cl "\"It’s not exactly safe to go wondering about all alone after we found out what’s out there, is it?\""
show cli adv with dis
m "\"Okay.\""
m "\"It’s not safe much anywhere.\""
"Especially not for me."
show mur concerned d with dis
mu "\"I think he’s saying that at least there’s nothing here that will physically harm you.\""
"Unless a couple of bounty hunters from Echo stroll in if Will decided to give them my name."
"He must be putting the pieces together any day by now."
"And he knows where we went."
show cli adv eyes down with dis
cl "\"I don’t think it’s smart for anybody to travel alone after what happened.\""
show cli adv with dis
m "\"Then I’ll find somebody to travel with.\""
m "\"It’s not really either of your concern.\""
show cli adv doubt with dis
cl "\"But it is of our concern.\""
show cli adv eyes down with dis
cl "\"Just because you’re going your own way doesn’t mean we’ll stop being friends.\""
show mur talking with dis
mu "\"I feel the same way.\""
show mur sideeye d with dis
mu "\"I’ve been through more in the last few days with this group than I ever have before in my life.\""
show cli adv with dis
show mur smile with dis
jeb "\"Y’all gettin’ sentimental without me?\""
show jeb at left,inn behind cli with dissolve
"We turn to see the horse crouching to stand in the small doorway as he makes his way inside."
show jeb talking with dis
jeb "\"This a sewing circle or what?\""
show jeb with dis
show cli adv talking with dis
cl "\"Just trying to keep our plans for the week ship-shape.\""
show jeb shocked
show mur concerned d
with dis
show cli eyes down with dis
m "\"I won’t be going back to Echo with the rest of you.\""
"The mood is heavy again despite the weasel’s attempt at redirection."
show jeb shocked talking with dis
jeb "\"That so?\""
show jeb sad with dis
show jeb sad talking with dis
jeb "\"We’ll be worse off without you.\""
show jeb sad with dis
"That’s surprising to hear."
show jeb with dis
m "\"I don’t feel like I did much aside from gettin’ injured.\""
show jeb talking with dis
jeb "\"You helped me dig.\""
show jeb with dis
show jeb talking with dis
jeb "\"And you didn’t panic when most people could have.\""
show jeb sad with dis
show jeb sad talking with dis
jeb "\"Maybe even should have.\""
show jeb with dis
show jeb talking with dis
jeb "\"Stable men are hard to find.\""
show jeb with dis
"My smile is a bit strained."
m "\"You’re overselling my contributions.\""
show jeb talking with dis
jeb "\"Not really.\""
show jeb with dis
show jeb talking with dis
jeb "\"Just a fact of the prairie.\""
show jeb sad with dis
show jeb sad talking with dis
jeb "\"You’re all fine if at least one of you is.\""
show jeb with dis
show jeb talking with dis
jeb "\"And you’re a decent example for staying steady.\""
show jeb sad with dis
show jeb sad talking with dis
jeb "\"Better than I was, anyway, even if it wasn’t my fault.\""
stop music fadeout 3.5
show jeb with dis
show cli adv doubt with dis
cl "\"Well, Jeb is right about one thing.\""
show jeb doubt with dis
show cli adv talking with dis
cl "\"We’re only better off with you around, Sam.\""
show cli adv doubt with dis
show jeb angry talking with dis
play music "music/contemplation.ogg" fadein 3.0
jeb "\"Now wait just a minute.\""
show jeb doubt with dis
show jeb angry talking with dis
jeb "\"What do you mean right about one thing?\""
show jeb doubt with dis
show jeb angry talking with dis
jeb "\"I was right about a lot of things.\""
show jeb angry with dis
jeb "\"My animals are dead and my wagon got hacked up and I still got you where you needed to be.\""
show jeb doubt with dis
show cli adv angry with dissolve
cl "\"We ran into problems before the attack.\""
show jeb shocked with dis
show cli adv doubt with dissolve
cl "\"I’m late for my arrangements because of all the extra time spent in the woods.\""
m "\"Extra time?\""
"...What is he talking about?"
"It’s only been a few days."
show jeb doubt with dis
show cli adv sad with dissolve
cl "\"Oh, forget it.\""
cl "\"We’re lucky we weren’t turned away at the gate is all.\""
show cli adv doubt with dissolve
cl "\"I tell you what, Jebediah.\""
show cli adv with dis
show cli adv talking with dis
cl "\"Why don’t I just pay you for half of the trip, and you can just focus on resting up here?\""
show cli adv with dis
show cli adv eyes talking with dis
cl "\"I’ll pay for a new cart and new animals, but I’ll look into finding a different guide.\""
show cli adv with dis
show cli adv talking with dis
cl "\"What do you think of that?\""
show cli adv doubt with dis
show jeb angry talking with dis
jeb "\"I think it’s stupid as hell considering I’ve got to go back that way anyhow.\""
show jeb doubt with dis
show jeb angry talking with dis
jeb "\"You’ll be hard-pressed to find somebody else short notice.\""
show jeb doubt with dis
show mur sad with dissolve
mu "\"I also don’t think that’s such a good idea.\""
mu "\"My family will want me back in town as soon as possible.\""
show cli adv angry with dissolve
cl "\"Well I don’t want to pay top dollar just to get lost again.\""
show cli adv doubt with dissolve
show jeb angry with dis
jeb "\"I said that wasn’t my fault.\""
show jeb doubt with dis
show mur concerned d with dissolve
mu "\"It wasn’t.\""
show mur sideeye with dis
mu "\"We had multiple different experienced trackers experience problems and inconsistencies.\""
show mur concerned d with dis
show cli adv angry with dissolve
cl "\"Then here’s what I think.\""
cl "\"The naked truth must be that something on that path, or in that forest, has altered our perception of space and time.\""
show cli adv doubt with dissolve
cl "\"I know there are various types of hallucinogenic gasses that cause people to lose track of such things, and we must have fallen victim without realizing.\""
show mur sideeye with dis
show cli adv eyes down with dis
cl "\"That, or we all have a shared disease, though I must admit that I do not feel off or feverish.\""
show cli adv doubt with dis
cl "\"Drugging isn’t outside of the possibility either.\""
show mur concerned d with dis
show jeb angry talking with dis
jeb "\"Here’s something simpler, Mr. Tibbits.\""
show jeb doubt with dis
show jeb angry talking with dis
jeb "\"You are in an unfamiliar community in the middle of the woods, full of people who either cannot help you or cannot understand you.\""
show jeb doubt with dis
show jeb angry talking with dis
jeb "\"You are paying me to take you from point A to point B, and not much else.\""
show jeb doubt with dis
show jeb angry talking with dis
jeb "\"You owe me half, and I’ll want that amount in full tonight.\""
show jeb doubt with dis
show cli adv angry with dissolve
cl "\"Fine.\""
hide cli with dissolve
play sound ("sfx/clothrustle.ogg") #placeholder?
"The weasel mutters under his breath, putting his bag on one of the beds and scrambling through its contents."
stop sound
show cli adv doubt at center,inn with dissolve
"He pulls out the pre-written check and hands it over to the horse."
cl "\"I hope you use this responsibly.\""
show jeb angry talking with dis
jeb "\"It’s mine.\""
show jeb doubt with dis
show jeb angry talking with dis
jeb "\"I’ll use it how I damn well please.\""
show jeb doubt with dis
show jeb angry talking with dis
jeb "\"Come find me in a week if you plan to make good on the prior arrangement.\""
show jeb angry with dis
jeb "\"But this time I want you to pay up front.\""
hide jeb with dissolve
play sound ("sfx/doorshut.ogg")
hide jeb with vpunch
"He ducks down and out of the room, slamming the door behind him."
stop sound
"We can hear him trot down the stairs in a hurry."
show cli adv angry with dissolve
cl "\"And he didn’t even bother to tell us where to find him!\""
show cli adv doubt with dissolve
m "\"I’m sure you’ll see him around.\""
m "\"Hard to stay hidden in a place like this.\""
"I don’t like how right I am right now."
show cli adv sad
show mur sideeye
with dissolve
cl "\"I had thought if I laid out my reasoning he would come to understand my concerns!\""
cl "\"It isn’t as simple as going from point B to point A if there are dangerous miasmas flitting about the woods!\""
cl "\"And then there’s that beast to consider!\""
cl "\"If that patch of woods is its territory, does it make any sense to go traipsing around to provoke it again?\""
cl "\"Flinging ourselves to jaws both literal and proverbial is what that is if he intends to take the same path backwards.\""
show mur eyes talking with dis
mu "\"Cliff.\""
show cli adv doubt
show mur sideeye
with vpunch
cl "\"What?!\""
show mur sad with dissolve
mu "\"You don’t have to diagram what you’re thinking.\""
mu "\"I understand where you’re coming from.\""
cl "\"That’s good!\""
show mur sideeye with dissolve
mu "\"But you aren’t breathing enough.\""
mu "\"And Jeb is already gone.\""
show cli adv angry with dissolve
"He holds his hands to his temples."
cl "\"I know he’s gone.\""
cl "\"I just thought if I didn’t explain, you both wouldn’t get it, and you’d both think I wasn’t acting in a rational capacity.\""
show mur concerned d with dis
"I look at Murdoch to see his reaction to this."
"He’s looking at me too."
show mur eyes talking with dis
mu "\"I don’t think Jeb thought your thought process was questionable.\""
show mur concerned d with dis
mu "\"But...\""
show mur sad with dissolve
m "\"It’s more like you care an awful lot about how people react to the same information that you get.\""
mu "\"You’re making decisions based on how they feel.\""
show cli adv eyes down with dissolve
cl "\"Well isn’t that what I’m supposed to be doing?\""
show cli adv doubt with dissolve
cl "\"What kind of message does it send when a guide isn’t concerned about the safety of his passage?\""
m "\"He’s probably frustrated that you hired him for his expertise but doubt it whenever anything goes wrong.\""
show cli adv angry with dissolve
cl "\"But so many things have gone wrong.\""
cl "\"Do you really think that none of them are his fault?\""
show mur concerned d with dissolve
cl "\"That the drinking was appropriate when we were that close to death’s door?\""
show mur eyes talking with dis
mu "\"I think it’s fine to be mad about that.\""
show mur concerned d with dis
m "\"But he’s mixing up two different things.\""
show mur sideeye with dis
mu "\"Yeah.\""
show cli adv doubt with dissolve
cl "\"What?\""
show mur concerned d with dis
mu "\"I remember the times Jeb got drunk.\""
mu "\"They only happened after we got lost or attacked, not before.\""
show mur eyes talking with dis
mu "\"If your ideas about intoxicating gas are true, then we were already subjected to an altered experience before he started drinking.\""
show mur concerned d with dis
"The stoat’s lip trembles."
show cli adv eyes down with dissolve
cl "\"I see...\""
"He takes off his glasses to wipe them off, and then places them back with trembling hands."
show cli adv sad with dissolve
cl "\"You’re both right, of course.\""
cl "\"I haven’t been acting as a gentleman should.\""
cl "\"I shouldn’t expect others to react how I preconceive they should react.\""
cl "\"That’s not fair to anybody, is it?\""
show mur eyes talking with dis
mu "\"Part of that is just management experience.\""
show mur concerned d with dis
show cli adv eyes down with dissolve
cl "\"Well, yes, but that’s no excuse.\""
cl "\"This is my first expedition, and I should be trying harder to be on my best behavior.\""
cl "\"I don’t know what I’m doing, and this is the last impression the both of you will have of me if this really is our last week together.\""
show mur eyes with dis
mu "\"I’m not going anywhere.\""
"I don’t have much I can add."
"I don’t think anybody can change who they are in just a week."
"Unless it’s something really bad."
show mur concerned d with dis
m "\"Hey, Professor?\""
show cli adv with dis
cl "\"What, Samuel?\""
m "\"I’m going to remember you for who you are, not for who you want to be.\""
show cli adv eyes down with dissolve
show mur sideeye with dis
cl "\"Well then that’s just utterly humiliating, then, isn’t it?\""
show cli adv with dissolve
m "\"I don’t think it is.\""
m "\"But it’s strange when I’m talkin’ to somebody who’s living in tomorrow, not today.\""
show cli adv sad with dissolve
cl "\"It’s cruel to even bring up tomorrow!\""
cl "\"I can’t be in this kind of mood when I wake up.\""
show mur concerned d with dis
"Me and Murdoch look at one another again, and then back to Cliff."
stop music fadeout 4.5
show cli adv eyes down with dissolve
cl "\"I just need some time to think.\""
hide cli with dissolve
play sound ("sfx/doorshut.ogg")
"He walks out of the room, not exactly slamming the door, but not closing it gently neither."
show mur sideeye with dis
mu "\"...I don’t think he gets it.\""
m "\"Well, at least something good came out of this.\""
show mur concerned d with dis
mu "\"What’s that?\""
show mur sideeye with dis
m "\"You’re definitely going to get one of the beds to yourself.\""
play music ("music/quiet.ogg") fadein 3.0
"He clicks his tongue, ignoring my comment as he shuffles through his pack, pulling out a dark curtain and jars of liquid in a can."
show mur eyes with dis
mu "\"Maybe he’ll cheer up once I develop some of these photos.\""
show mur talking with dis
mu "\"I think it can help somebody see a visual representation of where they’ve started and where they’ve come.\""
show mur smile with dis
m "\"Where they’ve come?\""
show mur sideeye d with dis
m "\"Are you doing that in one of your nudie pictures?\""
show mur angry with dissolve
"He gives me a look."
mu "\"You know that’s not what I meant.\""
show mur sideeye with dissolve
mu "\"...that’s a bitch to time correctly, anyhow.\""
m "\"Right then.\""
m "\"I’ll leave you to your secrets.\""
show mur concerned d with dis
"He stops shuffling through his pack and looks in my direction."
mu "\"And where exactly are you going?\""
m "\"Doing like y’all said.\""
m "\"If I’m going in a different direction, then I need to find folks who might go with me.\""
m "\"Safety in numbers.\""
show mur sideeye with dis
mu "\"That’s a good idea for general traveling purposes.\""
"The fox narrows his eyes."
show mur fear d with dis
mu "\"But truth be told, I don’t think numbers will help anyone who runs across that thing.\""
m "\"So what will help?\""
show mur concerned d with dis
"He taps his chin."
show mur sad with dissolve
mu "\"I don’t know.\""
mu "\"I guess the pessimistic answer is two or more groups traveling at the same starting point in different directions, isn’t it?\""
m "\"Jesus.\""
show mur sideeye with dissolve
mu "\"Always another thing to try if you run out of options, but I don’t put much stock in it myself.\""
mu "\"But maybe we’ll stumble upon something.\""
show mur concerned d with dis
mu "\"That is usually how we get the answers to most things, isn’t it?\""
m "\"Just make sure you stumble first. And make sure to tell me what you learn before you bleed out.\""
show mur sideeye with dis
"He looks away and gives me a short military salute as he busies himself with his chemicals, and I slink out the doorway."


stop music fadeout 5.0
play background "music/windbirds.ogg" fadein 5.0
scene reservation with fade
"I ask directions to the few people wandering outside, but I'm only met with avoidant glances, head shakes, and quick words in a language I don’t understand."
"A raccoon points me in one direction, where I run into a trading post."
"The woman running it isn’t much help, stating that the inn is the only place travelers coming and going tend to be during their time here."
play background "sfx/crickets.ogg" fadeout 3.5 fadein 3.5
scene bg black with slow_dissolve
scene reservation
show deepmine
with slow_dissolve
"I make my way around the boundaries of the reservation at least twice."
"It’s getting dark by now."
"Men with guns leer at me from wooden outposts about six feet into the air."
"I’m strange to them, no doubt, but they don’t pay me much mind for long."
"While the south side is gated in an arc of wooden posts, the north is completely unguarded."
"It doesn’t take me long to see why."
scene bg black with dissolve
"The reservation is built upon a precipice, and its deep canyon is too steep to climb with ease, considerin’ the rapids running below it."
"There’s an unguarded post with a flimsy wooden gate to the west, posted before a thick tree line."
"I walk past the post, unsure if it’s still a part of the settlement’s boundaries or not."
"The woods here is thick with pine trees, and the sounds of the rapids are louder."
$ renpy.music.set_volume(0.0, delay=0.0, channel='music2')
"I should go back."
scene bg settlementwoods with slow_dissolve
$ renpy.music.set_volume(0.5, delay=8.5, channel='background')
play music "sfx/drum.ogg" fadein 5.0
play music2 "sfx/drumtsela.ogg" fadein 5.0
"But I stop when I hear drums."
"They’re steady, monotone beats."
"I see movement between the trees and see a procession of mostly adult Meseta, walking in a row with a man at the front shaking a rattle."
"But there’s also two others I recognize."
show yis eyes at left,nightbrown with dissolve
"There’s Yiska, that bear from the trip, hitting a drum."
show cli serious at right,nightbrown with dissolve
"And then there’s Cliff."
"He’s walking behind them, silent and focused, stepping to the sound of the instrument, as the man in front of them all chants, beating the top of the drum."
hide yis
hide cli
with dissolve
"It looks like they’re doing something informal, but they’re carrying bags of stuff, and the chanting and the rattling seem to imply otherwise."
$ renpy.music.set_volume(1.0, delay=0.7, channel='music2')
"I jump when I hear another drum."
scene bg well
show tse eyes at center,nightbrown
with dissolve
"This beat is coming from behind me."
"I see Tsela standing at a well, looking down to hit the drum with the palm of his hands."
show tse with dis
$ renpy.music.set_volume(0.0, delay=0.7, channel='music2')
"He looks up and stops playing when he notices me looking back."
m "\"What’s going on?\""
show tse angry with dis
$ renpy.music.set_volume(1.0, delay=0.7, channel='music2')
"His eyes narrow and he goes back to beating the drum."
show tse angry talking with dis
ts "\"A disagreement is playing out.\""
show tse eyes with dis
show tse eyes talking with dis
ts "\"Nothing to concern yourself with.\""
show tse eyes with dis
"He lets out a string of chants, then starts to play his drum again."
"Another group of men passes by, some carrying pillows."
"Another, a paper lamp with wooden siding that has leaves whittled out of it."
m "\"Where are they taking all of that stuff?\""
show tse eyes talking with dis
ts "\"They’re burying Shilah’s things.\""
show tse angry with dis
$ renpy.music.set_volume(0.0, delay=0.7, channel='music2')
m "\"Who?\""
show tse angry talking with dis
ts "\"He was our other companion.\""
show tse angry with dis
show tse angry talking with dis
ts "\"On the hunting trip.\""
show tse angry with dis
"I think back and remember that they had mentioned traveling with another person."
m "\"Is this a funeral?\""
show tse eyes talking with dis
ts "\"Not in your Christian sense, no.\""
show tse with dis
show tse talking with dis
ts "\"We bury the lost, but we don’t hold funerals.\""
show tse with dis
show tse talking with dis
ts "\"Shilah’s body is something we could not recover.\""
show tse with dis
m "\"...Couldn’t his family reuse his things?\""
m "\"I don’t see the point in burying them.\""
show tse talking with dis
ts "\"If they aren’t with the dead, then he might come looking for them.\""
show tse with dis
m "\"You mean like a ghost?\""
show tse talking with dis
ts "\"I mean exactly a ghost.\""
show tse with dis
m "\"I just ain’t ever heard of a ghost coming back to get his things.\""
m "\"People pass down the things they use all the time.\""
m "\"Never really saw one come back for their coat racks and griddles.\""
show tse angry talking with dis
ts "\"Perhaps this is because your culture surrounds you with tortured spirits so often you have lost the ability to notice them, or how they make you ill.\""
show tse angry with dis
"I chuff."
m "\"Ill in what sense?\""
show tse talking with dis
ts "\"In spirit and body.\""
show tse with dis
show tse talking with dis
ts "\"Your people have a bad relationship with the air and soil.\""
show tse with dis
m "\"I stopped going to church because people kept guilting me there, too.\""
show tse angry talking with dis
ts "\"Do not compare my people to your fantasies of the world molded in your image.\""
show tse angry with dis
m "\"Didn’t mean offense.\""
m "\"I’m just struggling to think of what makes somebody like you much different from the preacher who’d always tell me to pray more and do better in the eyes of the Lord.\""
show tse angry talking with dis
ts "\"The difference is that your people bend the world into your own image.\""
show tse angry with dis
m "\"I’d appreciate if you stopped saying {i}‘your people’{/i}.\""
m "\"I don’t exactly claim any of this.\""
show tse with dis
"A shadow of doubt crosses the kit fox’s face."
show tse talking with dis
ts "\"Then what exactly do you claim?\""
show tse with dis
show tse talking with dis
ts "\"What are your roots?\""
show tse with dis
"I stop and think for a bit."
m "\"I guess I don’t know.\""
show tse surprised with dis
ts "\"What do you mean you don’t know?\""
show tse with dis
m "\"My parents didn’t know where we come from.\""
m "\"If my grandparents knew they never told.\""
m "\"We followed the law and the religion of our township, but that place and my family are practically dead to me.\""
show tse talking with dis
ts "\"Yet you still claim Christendom without its congregations?\""
show tse with dis
m "\"I guess.\""
show tse talking with dis
ts "\"So you choose to bear the weight of a movement without knowing its impact on others?\""
show tse with dis
show tse talking with dis
ts "\"You stumble in the dark, then.\""
show tse eyes with dis
show tse eyes talking with dis
ts "\"Hardly surprising.\""
show tse angry with dis
m "\"I still don’t see what makes your faith so much better or different than mine.\""
show tse angry talking with dis
ts "\"That’s apparent.\""
show tse angry talking with dis
ts "\"Our faith emphasizes the importance of noticing everybody’s role in the balance of everything.\""
show tse angry with dis
show tse angry talking with dis
ts "\"Not establishing dominion.\""
show tse with dis
show tse talking with dis
ts "\"It’s the difference between speaking and listening.\""
show tse with dis
show tse talking with dis
ts "\"Or like seeing the way a river flows, and taking the fish that you need from the current instead of building a dam to control where the fish must swim.\""
show tse angry with dis
m "\"What’s wrong with building a dam?\""
"He twitches."
show tse angry talking with dis
ts "\"There’s nothing wrong with building a dam.\""
show tse angry with dis
show tse angry talking with dis
ts "\"It was just an analogy.\""
show tse angry with dis
m "\"Okay.\""
m "\"This is stressing me out.\""
"His lip curls down."
m "\"You got a lighter?\""
show tse with dis
"He relaxes his face and looks away from me while he pulls something silver from his pocket."
show tse eyes talking with dis
ts "\"...sure.\""
show tse with dis
"I take out one of the cigarettes I’ve been holding onto from my pocket and lean my head towards him."
play sound "sfx/lighteron.ogg"
"He flips it open deftly and retreats it almost immediately after the first spark and the first catch of burnt paper."
stop sound
m "\"Thanks.\""
play sound "sfx/lighteroff.ogg"
"He doesn’t answer, but he puts the lighter away."
stop sound
"I inhale the smoke, hold it, and then let it all out."
m "\"Anyway, you were saying something about an argument.\""
m "\"What’s it about?\""
"I gesture in the direction of the marching procession."
show tse angry with dis
m "\"I thought this kind of stuff wasn’t allowed here, anyway.\""
show tse angry talking with dis
ts "\"The clergy doesn’t care as much about what the older generation does.\""
show tse angry with dis
show tse angry talking with dis
ts "\"They know that we’ll be more cooperative if they let us practice, and they’re letting time and dogma do the rest of the work.\""
show tse angry with dis
m "\"You seem a lot angrier than your friend.\""
"The bear in the distance hops as he beats his drum."
show tse angry talking with dis
ts "\"Yiska is not troubled by present, or by the future.\""
show tse with dis
show tse talking with dis
ts "\"He lives happily that way.\""
show tse with dis
show tse talking with dis
ts "\"He is a very harmonious person.\""
show tse with dis
show tse talking with dis
ts "\"This is why he leads the first night of this blessingway.\""
show tse with dis
m "\"What’s that?\""
show tse talking with dis
ts "\"Mostly what it sounds like.\""
show tse angry with dis
show tse angry talking with dis
ts "\"But he would do better, at times, to recognize that we are surrounded by enemies and bad spirits.\""
show tse angry with dis
show tse angry talking with dis
ts "\"Like the spirit we encountered in the woods who spilled blood.\""
show tse angry with dis
show tse angry talking with dis
ts "\"And the priest.\""
show tse angry with dis
show tse angry talking with dis
ts "\"And you and the other strangers.\""
show tse angry with dis
m "\"I’m sorry I exist.\""
show tse talking with dis
ts "\"Me too.\""
show tse angry with dis
show tse eyes talking with dis
ts "\"But at least it is not your fault.\""
show tse with dis
"I rub my temple."
show tse talking with dis
ts "\"The enemyway is a different sort of practice.\""
show tse with dis
show tse talking with dis
ts "\"It keeps the dead away.\""
show tse with dis
show tse talking with dis
ts "\"The unnatural things that plague us.\""
show tse angry with dis
m "\"And does it work?\""
show tse angry talking with dis
ts "\"Of course it works.\""
show tse angry with dis
m "\"Uh huh.\""
"Why is everybody always so confident about these sorts of things?"
"Wouldn’t everybody be doing these things if they worked?"
"Then again... I’ve never needed this degree of spiritual protection before I came to Echo."
"Maybe just faith in something is enough to make a difference."
"Or maybe I just keep running into prideful individuals."
show tse surprised with dis
m "\"Show me then.\""
show tse angry with dis
"He glares at me a bit, then puts the drum beneath his arm."
show tse angry talking with dis
ts "\"Not possible.\""
show tse with dis
show tse talking with dis
ts "\"But I can show you parts.\""
show tse with dis
"He jerks his head in a direction into the woods."
hide tse with dissolve
$ renpy.music.set_volume(0.6, delay=3.0, channel='music')
play background ("sfx/bonfire.ogg") fadeout 3.0 fadein 5.0
$ renpy.music.set_volume(1.0, delay=6.0, channel='background')
scene bg bonfire with fade
show tse at right,bonfire with dissolve
"I follow him a little deeper until we come across a glade with another bonfire."
show tse talking with dis
ts "\"Most of what I can show will not bear the same meaning or sentiment to an outsider, so you won’t get much out of this.\""
show tse eyes with dis
$ renpy.music.set_volume(1.0, delay=0.7, channel='music2')
"He starts beating his drum with one hand, then the other, in a steady beat."
show tse eyes talking with dis
ts "\"When warriors return to their families, there’s always the risk of bringing back ghosts with them.\""
show tse eyes with dis
stop music2 fadeout 0.7
"Then he stops again."
show tse talking with dis
ts "\"The first reason why this isn’t possible is that the ceremony doesn’t take place in one location or one night.\""
show tse with dis
show tse talking with dis
ts "\"It can take place for nine nights, alongside many other rituals.\""
show tse with dis
show tse talking with dis
ts "\"We paint the sand with dry pigment, we sing, we pray...\""
show tse with dis
show tse talking with dis
ts "\"And many bear the responsibility of moving the rattle we make from one site to another.\""
show tse angry with dis
m "\"That sounds time consuming.\""
show tse angry talking with dis
ts "\"Our community loses much more than time when we start to neglect this ritual.\""
show tse with dis
show tse talking with dis
ts "\"Shilah was a warrior.\""
show tse with dis
show tse talking with dis
ts "\"So are we.\""
show tse with dis
"He’s really unloading this all on me."
m "\"You know...\""
m "\"That little stoat fella rode all the way across the sea just to hear about stuff like this.\""
show tse angry with dis
"He leers at me."
show tse angry talking with dis
ts "\"Yes.\""
show tse angry with dis
show tse angry talking with dis
ts "\"So he can bring it back across the sea.\""
show tse angry with dis
"I shrug."
m "\"So?\""
show tse angry talking with dis
ts "\"He’s a thief.\""
show tse angry with dis
m "\"Of what, exactly?\""
show tse angry talking with dis
ts "\"Of spirit and knowledge.\""
show tse with dis
m "\"So then what about me?\""
show tse talking with dis
ts "\"In truth, I’m telling you this because I do not think you have the capacity to remember the information to pass along.\""
show tse with dis
m "\"Huh?\""
show tse eyes talking with dis
ts "\"At least not details that matter.\""
show tse with dis
"I blink again."
m "\"You know what?\""
m "\"I think you’re really rude.\""
show tse talking with dis
ts "\"Or I just understand how things work.\""
show tse with dis
show tse talking with dis
ts "\"The people who come here to study us don’t want to make our lives better.\""
show tse with dis
show tse talking with dis
ts "\"They want to make us like them, or kill us.\""
show tse with dis
show tse talking with dis
ts "\"If not our forms, then our spirit.\""
show tse with dis
show tse talking with dis
ts "\"I do not have to be comfortable with that.\""
show tse angry with dis
m "\"...Huh.\""
show tse angry talking with dis
ts "\"What?!\""
show tse angry with dis
m "\"Nothing, it’s just...\""
show tse with dis
m "\"You look and sound a lot like somebody I know right now.\""
show tse talking with dis
ts "\"Who?\""
show tse surprised with dis
m "\"Do you know Cynthia Tsosie?\""
"For the first time, he looks genuinely curious."
show tse with dis
show tse talking with dis
ts "\"She is my cousin.\""
show tse eyes talking with dis
ts "\"Though the Begay and the Tsosie families have not interacted for a long time.\""
ts "\"None of them live here anymore.\""
show tse with dis
m "\"I know one in Echo.\""
show tse talking with dis
ts "\"I knew Istad and Kele.\""
"Now he’s nodding."
show tse talking with dis
ts "\"Cynthia was their daughter.\""
show tse with dis
m "\"That’s what she was called here too?\""
show tse talking with dis
ts "\"Her father converted to Christianity.\""
show tse eyes with dis
show tse eyes talking with dis
ts "\"Her mother did not.\""
show tse with dis
show tse talking with dis
ts "\"She traded in jewelry, and Cynthia helped her make this finery.\""
show tse with dis
show tse talking with dis
ts "\"This was a problem for the priests, because the nature of this work is religious, and their power to barter in the community was great.\""
show tse eyes with dis
show tse eyes talking with dis
ts "\"But the day they left was very strange.\""
show tse eyes with dis
"It looks like he’s trying hard to remember."
show tse eyes talking with dis
ts "\"Her father needed medicine, but nobody would disclose the nature of his ailment.\""
show tse with dis
show tse talking with dis
ts "\"I was told that the whole family packed up for Camp Rosa, and nobody had seen them since.\""
show tse with dis
show tse talking with dis
ts "\"Echo is in the opposite direction though.\""
show tse with dis
m "\"Have you been to Camp Rosa yourself?\""
show tse talking with dis
ts "\"Several times.\""
show tse with dis
m "\"Is there a railroad?\""
show tse talking with dis
ts "\"No, but Providence has one and it’s closer.\""
show tse angry with dis
m "\"...Could you take me there?\""
show tse angry talking with dis
ts "\"I don’t have any business there.\""
show tse with dis
m "\"I’ll pay you.\""
show tse talking with dis
ts "\"How much?\""
show tse with dis
m "\"I have a banking check for sixty dollars.\""
show tse talking with dis
ts "\"I could do this trip for twenty if you have something more material to offer up front...\""
show tse with dis
show tse talking with dis
ts "\"Paper money is fine when we get to our destination.\""
show tse angry with dis
show tse angry talking with dis
ts "\"Isn’t so good in the desert.\""
show tse with dis
m "\"Providence has a phone, right?\""
show tse talking with dis
ts "\"So what?\""
show tse with dis
m "\"I could get you a phone call with Cynthia.\""
show tse angry talking with dis
ts "\"What makes you think I would want that?\""
show tse angry with dis
m "\"Don’t you?\""
show tse with dis
m "\"You said she was family.\""
"He pauses."
show tse talking with dis
ts "\"I do.\""
show tse eyes talking with dis
ts "\"But I am also afraid of what I might find out if I do.\""
show tse with dis
"That’s an odd thing to say."
"Then again, family business is often odd."
"And more importantly, none of my business."
m "\"Is that enough to offer, or do I need to think of something else?\""
show tse talking with dis
ts "\"Supply the food and the water and I will agree to this.\""
show tse with dis
m "\"Deal.\""
show tse smile with dis
"I hold out my hand to him and he grabs it."
$ renpy.music.set_volume(0.2, delay=0.0, channel='sound')
"His grip is tight for a paw so small."
"It’s almost painful."
play sound "sfx/whinny.ogg"
show tse with dis
"He lets me go when we hear something."
stop sound
m "\"What was that?\""
show tse talking with dis
ts "\"Sounded like a whinny.\""
show tse with dis
m "\"Are there pack beasts nearby?\""
show tse talking with dis
ts "\"Yeah, there’s a ranch outside the gate.\""
show tse with dis
play sound "sfx/whinny2.ogg"
"We hear another whinny."
show tse surprised with dis
queue sound "sfx/bray1.ogg"
queue sound "sfx/gore.ogg"
"Then a startled bray, and something wet."
"There’s thrashing and galloping and the sound of something repeatedly slamming into wood."
stop sound
m "\"Do they normally make those sounds?\""
show tse angry with dis
m "\"You don’t think...\""
$ renpy.music.set_volume(1.0, delay=0.0, channel='sound')
show tse angry talking with dis
ts "\"Don’t assume the worst.\""
show tse angry with dis
show tse angry talking with dis
ts "\"Something probably snuck into the pen.\""
show tse angry with dis
show tse angry talking with dis
ts "\"We rely on these beasts for transport and food.\""
show tse angry with dis
show tse angry talking with dis
ts "\"If something’s wrong then we need to tell the rancher.\""
show tse angry with dis
show tse angry talking with dis
ts "\"This way.\""
show tse angry with dis1
scene bg black with dissolve
scene bg settlementwoods
show tse angry at center,nightbrown
with dissolve
$ renpy.music.set_volume(0.5, delay=3.0, channel='background')
play background ("sfx/crickets.ogg") fadeout 2.0 fadein 2.0
stop music fadeout 3.0
"It's a lot darker in these parts of the woods."
"If I try, I can make out some shapes that might be barns in the distance, but they look more like blobs to me."
"I feel the kit fox tug me by the cuff as he ducks, and I feel a board of a fence hit my stomach."
m "\"Oof.\""
"He makes a shushing sound to me."
m "\"Are we supposed to be out here?\""
"I can see enough of his face to tell he's rolling his eyes."
hide tse with dissolve
"He scampers through the fence, and I follow him mostly because I don't want to be by myself if somebody with a rifle comes across us."
"I stumble around, looking for the direction he went in."
show tse angry at center,nightbrown with dissolve
show tse angry talking with dis1
ts "\"Here.\""
show tse angry with dis
m "\"Oh, there ya are.\""
"He's leaning against something big."
"I think for a moment it must be a sleeping mule, but it doesn't look like it's breathing evenly."
show tse eyes talking with dis
ts "\"Cold wound.\""
show tse angry with dis
show tse angry talking with dis
ts "\"It wasn't emboldened enough to finish.\""
show tse angry with dis
m "\"Why's that?\""
show tse angry talking with dis
ts "\"Could be testing the boundaries of the herd.\""
show tse angry with dis
show tse angry talking with dis
ts "\"Could have been scared off or injured itself.\""
show tse angry with dis
"We look out to the pen in the woods and count more than fifty dark figures wading around."
show tse angry talking with dis
ts "\"What we might have heard was one of the pack animals smelling the wound of the other animal.\""
show tse angry with dis
"Nothing to worry about then?"
"I slack my shoulders and feel my neck relax."
m "\"Thank God there’s nothing out here now.\""
show tse with dis
m "\"Whatever it was must be gone.\""
$ renpy.music.set_volume(1.0, delay=3.0, channel='music')
scene bg black with dis
play music "music/refraction.ogg" fadein 3.0
"That’s when I feel something touch me."
"It confuses me at first because it feels like the dainty sort of caress of a hand on my lower leg, except curls close to grip me."
"That’s when I can feel how truly large the palm is."
play sound "sfx/thud.ogg"
"I yowl as I feel it yank me off of my feet, slamming my back into the dirt."
scene bg settlementwoods
show tse surprised at center,nightbrown
with dissolve
"I open my eyes and I see Tsela staring at me with wide eyes."
stop sound
scene bg black with dis
"And rapidly, he becomes smaller."
play ambient "sfx/dragged.ogg" fadein 3.0
"Something's dragging me."
scene bg nightsky
show treetop:
    subpixel True
    yalign 0.0
    linear 0.9 yalign 1.0
    repeat
show branches:
    subpixel True
    yalign 0.0
    linear 0.9 yalign 1.0
    repeat
show leaves:
    subpixel True
    yalign 0.0
    linear 1.0 yalign 1.0
with dis
"I can see the stars and the trees sweep by as I realize the speed that I’m going."
hide leaves
"Rocks and roots scrape against my shirt, ripping through, some scraping the skin."
show leaves:
    yzoom -1
    subpixel True
    yalign 0.0
    linear 1.0 yalign 1.0
$ renpy.music.set_volume(0.5, delay=8.0, channel='ambient')
"I try to look forward to see what’s dragging me."
"But I don’t see anything, despite feeling that awful, monstrous claw clipping into me with its nails."
"I think about how far above the canyon this settlement is."
"I think about a chasm littered with bones that gets thinner and thinner the harder you’re pulled."
stop ambient fadeout 1.5
"But then I stop moving."
scene bg nowherewoods with slow_dissolve
"I stand up and I’m out in the middle of nowhere."
"There’s no houses nearby."
"No people."
"And when I try to stand on my left leg, it hurts."
"It hurts real bad."
play sound "sfx/monsterbreath.ogg"
"And what’s worse is that I can hear something breathing."
"I feel like it wants me to walk."
"Wants me to try to make it back to town."
"There’s nowhere to go, or to hide, but back in the direction that I came from."
"I can still see the trail that my own body made."
"And I let out a yowl when I take my first step."
stop sound
"My ankle is swelling."
"I’m going to have to crawl."
$ renpy.music.set_volume(0.6, delay=0.0, channel='sound')
"So I get to my knees, and I cry out again, feeling the stab in my leg."
"Then I pull myself forward."
"Tears pool down my cheeks as I scrabble forward, careful not to let my left foot touch the ground."
"I feel a hot breath on my neck."
"A long, spongy tongue starts to lap at my neck."
play sound "sfx/distantgunshot.ogg"
"And then I hear the gunshot."
stop sound
"It’s gone as if it was never there."
show tse surprised at center,night
show expression AlphaMask("deepmine", At("tse surprised", center)) as mask
show expression AlphaMask("foliage", At("tse surprised", center)) as mask2:
    alpha 0.25
with dissolve
"And I see Tsela running towards me, hooking his rifle onto his back grabbing me by the suspenders and pulling me in quick bursts."
"He looks right, and then left, wide-eyed, almost frenzied as he takes me back through the woods."
hide tse
hide mask
hide mask2
with dissolve
"It’s hard to turn my head to look left or right."
play sound "sfx/breathright.ogg"
"Sometimes I think I hear breathing again on the right."
queue sound "sfx/breathleft.ogg"
"Sometimes it’s on the left."
"Sometimes its sounds like it’s coming from the trees, or from multiple places all at once."
stop sound
"Tsela doesn’t stop dragging me."
$ renpy.music.set_volume(1.0, delay=0.0, channel='sound')
ts "\"Use your legs if you can.\""
m "\"My right’s twisted!\"" #mentioned earlier that the left leg was the hurt one. Should this and other refs say left leg?
ts "\"Then just the one!\""
ts "\"You’re too heavy to drag.\""
ts "\"We have to move faster or I’ll have to drop you.\""
scene bg black with dissolve
"Back through the gate."
stop music fadeout 10.0
scene bg yistsecabinnight with dissolve
"Back to his cabin."
play sound ("sfx/doorshut.ogg")
$ renpy.music.set_volume(1.0, delay=0.0, channel='ambient')
$ renpy.music.set_volume(0.4, delay=3.0, channel='background')
"He slams the door and bolts the lock."
show tse angry at center,nightdeep with dissolve
stop sound
"He pulls me over to a rug on the ground."
show tse angry talking with dis
ts "\"Show me your foot.\""
show tse angry with dis
"I pull up the sleeve and he bends down, holding it with one of his paws."
show tse with dis
m "\"Don’t touch it!\""
"He brushes up against the direction of my fur."
show tse talking with dis
ts "\"Aside from the bruising, most of your skin is red, so no bleeding.\""
show tse with dis1
show tse talking with dis
ts "\"Your bones are in place.\""
show tse eyes with dis1
show tse eyes talking with dis
ts "\"But you shouldn’t walk on this for several days.\""
show tse with dis
m "\"But I...!\""
"I try to stand again and feel the sharp sting in my ankle."
show tse angry with dis
m "\"... have to!\""
m "\"Argh!\""
m "\"I only have a week to get out of this town...\""
"And I don’t even want to wait that long."
"Tsela shakes his head."
show tse angry talking with dis
ts "\"Foolish.\""
show tse angry with dis1
show tse angry talking with dis
ts "\"You won’t make it far on that leg.\""
show tse angry with dis
m "\"Do you have a car that could drive us?\""
show tse angry talking with dis
ts "\"I do.\""
show tse with dis
m "\"So what’s the problem?\""
show tse talking with dis
ts "\"Something might be following you.\""
show tse with dis
"I shake my head."
m "\"You can’t prove that.\""
show tse angry with dis
m "\"It’s just gotta be some starving animal.\""
"Even I don’t believe it when I say that, but I don’t want to think about any other possibility."
show tse angry talking with dis
ts "\"No animal would be bold enough to come here with all of the noise and the smoke.\""
show tse angry with dis1
show tse angry talking with dis
ts "\"It’s something else.\""
show tse angry with dis1
show tse angry talking with dis
ts "\"And it showed when your party did.\""
show tse angry with dis
m "\"I thought your group was attacked before us?\""
m "\"Maybe it’s hunting you?\""
show tse eyes with dis
"He mumbles something I don’t understand."
show tse eyes talking with dis
ts "\"We know that it will go after us at the very least.\""
show tse eyes with dis
m "\"Well I’ve still gotta leave town!\""
show tse with dis
"He looks out of a window, craning his head."
show tse talking with dis
ts "\"It sounded like it was bothering the animals, so it’s a problem for the whole settlement now.\""
show tse with dis1
show tse talking with dis
ts "\"You should tell your anthropologist friend, so he can tell the Christians.\""
show tse with dis1
show tse talking with dis
ts "\"If we put together a hunting party then we can be rid of it before it strikes.\""
show tse with dis
m "\"You’re gonna try and kill it?\""
show tse eyes talking with dis
ts "\"Ideally.\""
show tse with dis
m "\"But we couldn’t even see it the last time.\""
m "\"And it’s fast!\""
show tse talking with dis
ts "\"None of us are getting very far if this problem isn’t dealt with.\""
play sound "sfx/oneknock.ogg"
play music "music/bedhorror.ogg" fadein 3.5
show tse surprised with dis
"There’s a thump on the door."
stop sound
"It’s sudden and forceful, like a single knock."
"But that’s not exactly right either."
show tse angry with dis
"Tsela stands and walks up to the door."
show tse angry talking with dis
"He says something in his language."
show tse angry with dis
"There’s nobody there."
"Then he tries again in Albion."
show tse angry talking with dis
ts "\"Who’s there?\""
show tse with dis
"A deep, guttural voice replies?"
show tse talking with dis
ts "\"Yiska?\""
show tse with dis
"We both wait for a reply."
play sound "sfx/oneknock.ogg"
"There’s a soft shove again."
stop sound
show tse angry with dis
"???" "\"Yiska’s there.\""
show tse angry talking with dis
ts "\"What do you mean Yiska’s there?\""
show tse surprised with dis
ts "\"Who is this?\""
play sound "sfx/oneknock.ogg"
"Another thump."
stop sound
ysunk "\"This is Yiska.\""
"That sounded more like the bear this time."
m "\"Are y’all both roommates?\""
show tse angry with dis
"Tsela looks at me and holds up a single digit to his mouth."
show tse angry talking with dis
"He turns back to the door and makes noises I don’t understand."
show tse surprised with dis
"The person at the other side of the door makes those noises back in a deeper voice."
"And the fox steps away."
"He walks over slowly to the small window and pulls the curtains over it."
"A shadow passes, and he walks back slowly."
show tse angry with dis
"I’m about to ask him what’s going on, but he puts a hand over my mouth, giving me a taste of clay and bark."
"He leans close to my ear and whispers."
show tse angry talking with dis
ts "\"Spirit.\""
show tse angry with dis
"That confuses me."
"It sounded like Yiska."
show tse with dis
"I try to talk again but he shakes his head."
show tse talking with dis
ts "\"Do not leave tonight.\""
show tse with dis1
show tse talking with dis
ts "\"Do not let anybody in until morning.\""
show tse angry with dis
m "\"But what if it’s somebody we know?\""
show tse angry talking with dis
ts "\"Especially if it’s somebody we know!\""
show tse angry with dis
"The light behind the curtain blackens."
show tse eyes with dis
play sound "sfx/monstersniff.ogg"
"I hear sniffing sounds."
queue sound "sfx/nope.ogg"
"Then something wet."
queue sound "sfx/scrape3.ogg"
"A slow, scraping noise drags across the window."
"Then the shadow leaves."
stop sound
show tse eyes talking with dis
ts "\"Again.\""
show tse eyes with dis1
show tse talking with dis
ts "\"...Nobody.\""
show tse angry with dis
m "\"But what about your hunting partner?\""
show tse angry talking with dis
ts "\"That wasn’t him.\""
show tse angry with dis1
show tse angry talking with dis
ts "\"He won’t be back tonight.\""
show tse with dis
"We listen for the bugs, and the wind, and the trace of any footsteps."
stop music fadeout 5.0
"But there’s nothing."
show tse with dis1
show tse talking with dis
ts "\"Get some sleep.\""
show tse with dis1
show tse talking with dis
ts "\"I’ll know if you try to answer the door.\""
show tse with dis
m "\"How’s that?\""
show tse eyes talking with dis
ts "\"You make noise when you’re in pain.\""
show tse with dis1
show tse talking with dis
ts "\"I’ll know.\""
show tse eyes with dis1

label cliffroute3a:

$ renpy.music.set_volume(1.0, delay=5.0, channel='background')
scene bg black with slow_dissolve
"I try to sleep in spite of the pain and the anxiety."
"The bugs chirping outside sound uncomfortably close, like there ain’t much separating us besides stacked logs and flimsy glass."
"I try not to listen to anything, lest I hear something I shouldn’t."
scene bg yistsecabinnight with dis4
#sfx?
"I hear soft snores coming from the fox on the chair."
"I’m impressed that he can sleep sitting up, but I guess I shouldn’t be surprised."
"He’s still holding his gun."
"Now that I think about it, I thought they confiscated any weapons at the gate."
"Glad they didn’t or I’d most likely be dead."
play sound ("sfx/clothrustle.ogg")
"I shuffle against the fur blanket on the couch and turn my head away from the window, trying to sleep again."
"I feel heavier."
scene bg black with dis3
"My eyelids droop and my chest heaves heavier."
"I sink deeper into the couch, thinking of one of Benton’s piano pieces back at the Hip to drown out the sound of the bugs and taps of wood against the glass."
"I exhale."
scene bg yistsecabinnight
show deepmine:
    alpha 0.3
with dissolve
"I’m awake."
"And I feel hot, bubbling pain on my leg that fades, quickly."
"When I look down I see a welt on my foot that might be an insect bite."
"I’m worried it could be venomous because I didn’t see what did it."
"But it’s just itchy for now."
"I don’t hear Tsela snoring anymore."
"I probably woke him up when I shook the couch."
show tse eyes at center,night
show expression AlphaMask("nightshade", At("tse eyes", center)) as mask
with dis3
"Looking at the chair, I can see that he’s sitting there."
show tse eyes talking
show expression AlphaMask("nightshadetse2", At("tse eyes talking", center)) as mask
with dis
ts "\"Trouble sleeping?\""
show tse eyes
show expression AlphaMask("nightshade", At("tse eyes", center)) as mask
with dis
"I have to wait to let my eyes adjust to the dark."
m "\"Yeah.\""
show tse eyes talking
show expression AlphaMask("nightshadetse2", At("tse eyes talking", center)) as mask
with dis
ts "\"Losing sleep is a terrible thing.\""
show tse eyes
show expression AlphaMask("nightshade", At("tse eyes", center)) as mask
with dis1
show tse eyes talking
show expression AlphaMask("nightshadetse2", At("tse eyes talking", center)) as mask
with dis
ts "\"Some people say you never can get it back after you lose it.\""
show tse eyes
show expression AlphaMask("nightshade", At("tse eyes", center)) as mask
with dis
"I think I can just barely make out the shape of his snout moving."
show tse eyes talking
show expression AlphaMask("nightshadetse2", At("tse eyes talking", center)) as mask
with dis
ts "\"Bits of your brain just get strained and scrambled, and you just never get all of it back.\""
show tse eyes
show expression AlphaMask("nightshade", At("tse eyes", center)) as mask
with dis
m "\"You’re not really helping me get to sleep.\""
show tse eyes smile
show expression AlphaMask("nightshade", At("tse eyes smile", center)) as mask
with dis
ts "\"Who says I want to?\""
show tse eyes talking
show expression AlphaMask("nightshadetse2", At("tse eyes talking", center)) as mask
with dis
ts "\"Maybe I just want to talk right now.\""
show tse eyes
show expression AlphaMask("nightshade", At("tse eyes", center)) as mask
with dis
m "\"I feel like that’s surprising, considerin’ you rarely want to talk.\""
play sound ("sfx/creak1.ogg")
"I hear the chair creak as he adjusts himself in it."
stop sound
"I can’t see what he’s doing, but he’s moving around."

#IF FOUND JOHN’S PIPE:
if FollowCM == False:
    show tse eyes talking
    show expression AlphaMask("nightshadetse2", At("tse eyes talking", center)) as mask
    with dis
    ts "\"I hadn’t asked if you’re much of a smoker.\""
    show tse eyes
    show expression AlphaMask("nightshade", At("tse eyes", center)) as mask
    with dis
    m "\"I smoke from time to time.\""
    show tse eyes talking
    show expression AlphaMask("nightshadetse2", At("tse eyes talking", center)) as mask
    with dis
    ts "\"Y’know some folks say it’ll kill ya faster.\""
    show tse eyes
    show expression AlphaMask("nightshade", At("tse eyes", center)) as mask
    with dis1
    show tse eyes talking
    show expression AlphaMask("nightshadetse2", At("tse eyes talking", center)) as mask
    with dis
    ts "\"But there’s a whole lot of ways to die.\""
    show tse eyes smile
    show expression AlphaMask("nightshade", At("tse eyes smile", center)) as mask
    with dis
    ts "\"Best to enjoy yourself while you can, right?\""
    "I don’t know what he wants me to say."
    m "\"...Right.\""

#IF WENT THROUGH CABIN:
if FollowCM == True:
    show tse eyes talking
    show expression AlphaMask("nightshadetse2", At("tse eyes talking", center)) as mask
    with dis
    ts "\"You’re a bit of a pervert, aren’t you?\""
    show tse eyes
    show expression AlphaMask("nightshade", At("tse eyes", center)) as mask
    with dis
    m "\"...What?\""
    show tse eyes talking
    show expression AlphaMask("nightshadetse2", At("tse eyes talking", center)) as mask
    with dis
    ts "\"I mean you’ve seen plenty of things you’re not supposed to see.\""
    show tse eyes
    show expression AlphaMask("nightshade", At("tse eyes", center)) as mask
    with dis1
    show tse eyes talking
    show expression AlphaMask("nightshadetse2", At("tse eyes talking", center)) as mask
    with dis
    ts "\"And put your hands and mouth in all sorts of places.\""
    show tse eyes
    show expression AlphaMask("nightshade", At("tse eyes", center)) as mask
    with dis
    "His tone is stern."
    show tse eyes talking
    show expression AlphaMask("nightshadetse2", At("tse eyes talking", center)) as mask
    with dis
    ts "\"And you put your mind and body at the mercy of others, day after day.\""
    show tse eyes
    show expression AlphaMask("nightshade", At("tse eyes", center)) as mask
    with dis
    m "\"...How’s any of that your business?\""
    show tse talking
    show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
    with dis
    ts "\"Because I’m all too familiar with that sort of person, Mr. Ayers.\""

show tse with dis
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
play music ("music/contemplation.ogg") fadein 2.0
"He’s looking at me, and his eyes are open."
"But something’s wrong."
"His eyes look like dark glass, but there’s nothing much inside them."
"Nothing much but small lights, shining brightly, burning far far away."
"I think for a second that it must be his reflection, but I remember the windows are closed."
"The longer I look at him, the harder it is to make out anything else than the shine of his teeth and the glint of his eyes."
show tse talking
show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
with dis
nts "\"Where am I?\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis
"Whatever is shining must be coming from inside him."
m "\"What kind of a stupid question is that?\""
m "\"This is your house, ain’t it?\""
"Somehow I know it’s not his house."
"Because, somehow, I know that whoever I’m talkin’ to ain't Tsela."
"I want to play along, without making any sudden moves, like this is a dream and I’ll wake up soon."
"But he looks left, then right, then towards me again."
show tse talking
show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
with dis
nts "\"I’ve never been here before.\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis1
show tse talking
show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
with dis
nts "\"But I followed something, and now I am.\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis
m "\"Did you follow me?\""
show tse eyes
show expression AlphaMask("nightshade", At("tse eyes", center)) as mask
with dis
"He, or it, hums softly."
show tse eyes talking
show expression AlphaMask("nightshadetse2", At("tse eyes talking", center)) as mask
with dis
nts "\"Perhaps not.\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis1
show tse talking
show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
with dis
nts "\"There’s already somebody following you.\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis1
show tse talking
show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
with dis
nts "\"Will he speak?\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis
"He lets out a one-note laugh."
show tse eyes talking
show expression AlphaMask("nightshadetse2", At("tse eyes talking", center)) as mask
with dis
nts "\"Too shy?\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis1
show tse talking
show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
with dis
nts "\"Oh well.\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis1
show tse talking
show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
with dis
nts "\"You though.\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis
"He nods his snout."
show tse talking
show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
with dis
nts "\"I do know you though.\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis1
show tse talking
show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
with dis
nts "\"I’ve seen you plenty.\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis
m "\"Where?\""
"He tilts his head."
show tse smile with dis
nts "\"Don’t you mean where and when?\""
show tse eyes talking
show expression AlphaMask("nightshadetse2", At("tse eyes talking", center)) as mask
with dis
nts "\"I don’t suppose it matters.\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis1
show tse talking
show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
with dis
nts "\"It’s never fair what happens to us, though, is it?\""
show tse smile
show expression AlphaMask("nightshadetse", At("tse smile", center)) as mask
with dis
"He laughs again."
"It’s something that sounds like choking more than laughter."
show tse talking
show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
with dis
nts "\"You tell me so every time I meet you.\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis
m "\"I haven’t met you before.\""
show tse talking
show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
with dis
nts "\"Oh, I’ve met you.\""
show tse eyes
show expression AlphaMask("nightshade", At("tse eyes", center)) as mask
with dis1
show tse eyes talking
show expression AlphaMask("nightshadetse2", At("tse eyes talking", center)) as mask
with dis
nts "\"Unfair, unfair, unfair.\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis1
show tse talking
show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
with dis
nts "\"That’s your tune every time I meet you, isn’t it?\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis
"He takes something out of his pocket."
play sound ("sfx/knifeopen.ogg")
"I hear a flicking sound."
"In the low light, I can see it swinging."
stop sound
show tse talking
show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
with dis
nts "\"You always have the gall to say it to me.\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis1
show tse talking
show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
with dis
nts "\"In spite of your wealth of choices.\""
show tse eyes
show expression AlphaMask("nightshade", At("tse eyes", center)) as mask
with dis1
show tse eyes talking
show expression AlphaMask("nightshadetse2", At("tse eyes talking", center)) as mask
with dis
nts "\"And my lack of them.\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis1
show tse talking
show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
with dis
nts "\"But you choose so poorly, so many times.\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis
m "\"Who are you?\""
show tse eyes talking
show expression AlphaMask("nightshadetse2", At("tse eyes talking", center)) as mask
with dis
nts "\"It doesn’t matter.\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis1
show tse talking
show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
with dis
nts "\"I’m tired of telling you.\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis
m "\"Why are you here?\""
m "\"What do you want with me?\""
show tse eyes talking
show expression AlphaMask("nightshadetse2", At("tse eyes talking", center)) as mask
with dis
nts "\"I suppose you’re still not very smart yet.\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis1
show tse talking
show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
with dis
nts "\"I already told you.\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis1
show tse talking
show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
with dis
nts "\"I’m not here for any reason I can tell you.\""
show tse eyes
show expression AlphaMask("nightshade", At("tse eyes", center)) as mask
with dis1
show tse eyes talking
show expression AlphaMask("nightshadetse2", At("tse eyes talking", center)) as mask
with dis
nts "\"That would, again, imply I had a choice.\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis1
show tse talking
show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
with dis
nts "\"I’m just here to ride the wave.\""
play sound ("sfx/knifeclose.ogg")
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis
"He closes the knife and looks at his hands."
stop sound
show tse talking
show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
with dis
nts "\"These look like my hands.\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis1
show tse talking
show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
with dis
nts "\"But I know that they aren’t.\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis1
show tse talking
show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
with dis
nts "\"I haven’t ever seen them before.\""
show tse smile
show expression AlphaMask("nightshadetse", At("tse smile", center)) as mask
with dis
"For a moment he smiles."
show tse talking
show expression AlphaMask("nightshadetse3", At("tse talking", center)) as mask
with dis
nts "\"Maybe things will be different this time.\""
show tse
show expression AlphaMask("nightshadetse", At("tse", center)) as mask
with dis1
show tse eyes
show expression AlphaMask("nightshade", At("tse eyes", center)) as mask
with dis1
show tse
show expression AlphaMask("nightshade", At("tse", center)) as mask
with dis
"He blinks with both of his eyes and the lights go out."
show tse surprised
show expression AlphaMask("nightshade", At("tse surprised", center)) as mask
with dis
stop music fadeout 5.0
ts "\"Why are you awake?\""
show tse angry
show expression AlphaMask("nightshade", At("tse angry", center)) as mask
with dis
m "\"...what?\""
show tse angry talking
show expression AlphaMask("nightshade", At("tse angry talking", center)) as mask
with dis
ts "\"You should be sleeping.\""
show tse angry
show expression AlphaMask("nightshade", At("tse angry", center)) as mask
with dis
m "\"I thought I was.\""
show tse angry talking
show expression AlphaMask("nightshade", At("tse angry talking", center)) as mask
with dis
ts "\"You’re sitting up and staring at me in the dark like I’m a meal.\""
show tse angry
show expression AlphaMask("nightshade", At("tse angry", center)) as mask
with dis
m "\"We were talking...\""
m "\"We are talking and you were asleep.\""
show tse angry talking
show expression AlphaMask("nightshade", At("tse angry talking", center)) as mask
with dis
ts "\"I do not talk in my sleep.\""
show tse
show expression AlphaMask("nightshade", At("tse", center)) as mask
with dis1
show tse talking
show expression AlphaMask("nightshade", At("tse talking", center)) as mask
with dis
ts "\"Yiska or Avery would have told me.\""
show tse angry
show expression AlphaMask("nightshade", At("tse angry", center)) as mask
with dis
m "\"Hey.\""
"I hear a growl in my own voice."
show tse
show expression AlphaMask("nightshade", At("tse", center)) as mask
with dis
m "\"I ain’t makin’ shit up.\""
show tse talking
show expression AlphaMask("nightshade", At("tse talking", center)) as mask
with dis
ts "\"I’m sure you don’t think you are.\""
show tse eyes
show expression AlphaMask("nightshade", At("tse eyes", center)) as mask
with dis1
show tse eyes talking
show expression AlphaMask("nightshade", At("tse eyes talking", center)) as mask
with dis
ts "\"You’re injured and lack restful sleep.\""
show tse eyes
show expression AlphaMask("nightshade", At("tse eyes", center)) as mask
with dis1
show tse eyes talking
show expression AlphaMask("nightshade", At("tse eyes talking", center)) as mask
with dis
ts "\"Close your eyes and do not speak any more of this until the morning if you want to stay here.\""
show tse eyes
show expression AlphaMask("nightshade", At("tse eyes", center)) as mask
with dis
"I bite my lip."
"His home, his rules."
"I’m more than used to that concept."
hide tse
hide mask
with dis3
"I try closing my eyes a few times."
"And I feel myself slipping away."
play background ("sfx/birds.ogg") fadeout 4.5 fadein 4.5
scene bg black with slow_dissolve
pause 3.0
"There’s birds outside."
"Noisy little fuckers."

scene bg yistsecabin
show tse at right:
    xzoom-1
with dis4
play sound ("sfx/potsnpans.ogg")
"Pots and pans clang behind me and I can turn to see Tsela mill about his kitchen."
play sound ("sfx/choppingfast.ogg")
"I smell fried eggs and hear him chopping something fast."
queue sound ("sfx/pansizzle.ogg")
"He cups a handful of tubers and tosses it into a pan, making it sizzle."

show tse talking with dis:
    xzoom 1
ts "\"Good. You’re awake.\""
stop sound
#sfx?
show tse with dis
"He puts a plate on the end table near the couch."
show tse talking with dis
ts "\"Eat.\""
show tse with dis
"The warm scent of wilted greens, fried starch and fatty fish hits my face."

m "\"It smells delicious, but I think I might need to go.\""
show tse eyes talking with dis
ts "\"It’s light outside, so it’s safe to go.\""
show tse with dis
"I nod and make the motion to stand."

play sound ("sfx/thud.ogg")
"He looks at me with a doubtful face as a sharp feeling stabs through my leg."
m "\"SHIT!\""
show tse eyes talking with dis
stop sound
ts "\"Looks to me like you’re still not going anywhere.\""
show tse with dis1
show tse talking with dis
ts "\"Eat.\""
show tse with dis
"He knew this is what would happen."

"I shoot him a dirty look while I shovel a bit of runny egg and squash into my mouth."

"He finishes his meal very quickly without talking."

"Then he stands."
show tse talking with dis
ts "\"I’m going to get Avery.\""
show tse with dis
#IF STOLE MAP:
if HaveMap == True:
    "Him?"
    "Just the mention of his name makes me want to make sure I still have the map."
    "I don’t remember if I left it with my bags in Cliff’s room or not."
else:
    "I guess if there’s anybody who can help me right now, it’s him."
show tse talking with dis
ts "\"Don’t open the door for anybody, even if it sounds like me.\""
show tse with dis1
show tse talking with dis
ts "\"I won’t need any help getting back in.\""
show tse with dis1
hide tse with dis3
"I don’t think I could let anybody in even if I wanted to, unless I slid my way to the door."
"All I want to do now is focus on finishing my breakfast."
"It’s good, but the pain in my jaw and chest makes it hard to swallow anything at first."
if HaveMap == True:
    "Then I check one of the bags on me."
    "The map's there."
    scene hoganmap2 with dis3
    "I open it up to make sure it isn’t damaged, and I breathe in relief when I see it isn’t."
    scene bg yistsecabin with dissolve
play sound ("sfx/smallscratch.ogg")
"It’s not long before I hear scratching at the door."
play sound ("sfx/doorburst.ogg")
"I flinch and scoot back when I see the door burst open."
stop sound
show tse with dis3
"But it’s just the fox."
show ave serious at right behind tse with dis3
"The elk follows him behind looking a little more dour than before."
show ave serious talking with dis
$ renpy.music.set_volume(0.3, delay=2.5, channel='background')
play music ("music/quiet.ogg") fadein 2.0
av "\"Well if it isn’t Mr. Tibbits’s bodyguard.\""
show ave serious with dis
"I shake my head."
m "\"Just was for the journey here.\""
m "\"I’m off the hook now.\""
show ave serious eyes with dis
av "\"I hope he paid you well at least.\""
show ave angry eyes talking with dis
av "\"Bodyguarding’s a frightful business.\""
show ave serious with dis1
show ave serious talking with dis
av "\"This isn’t the first time I’ve had to patch you up.\""
show ave serious with dis
"I roll my eyes."
show tse angry with dis
"Tsela gives us both a suspicious look."
"He doesn’t know what Avery is talking about."
show tse with dis
show ave serious talking with dis
av "\"Now let’s see that leg.\""
show ave serious with dis1
show ave serious at center
show tse behind ave at right
with dis3
"I pull up my pant leg and place it on the table."
show ave shocked with dis
"Avery’s eyes widen a little."
show ave shocked talking with dis
av "\"Well I don’t think it’s broken but that’s definitely sprained.\""
show ave serious with dis1
show ave serious talking with dis
av "\"I have some cloth I can bind it with.\""
show ave serious with dis
m "\"Thanks, Doc.\""
show ave wink talking with dis
show tse smile with dis
av "\"I’m sorry to say that I didn’t bury a crutch in my bag.\""
show ave eyes with dis
"He shakes as he laughs at his own joke."
show ave with dis
m "\"...Thanks, Doc.\""
show ave talking with dis
av "\"A good, sturdy walking stick will do you just fine if you don’t want somebody in town to whittle you something.\""
show ave thinking with dis3
av "\"If it doesn’t look better in a week or two you might need a closer look.\""
show ave thinking eyes with dis
av "\"You can probably visit a real professional and get their opinions.\""
show ave serious talking with dis3
av "\"But I bet they’ll just charge you a pretty penny to say ‘keep it wrapped and don’t put pressure on it.’\""
show ave serious eyes with dis1
show ave serious eyes talking with dis
av "\"Though something like that is mostly common sense.\""
show ave serious eyes with dis
"He gets out gauze and a pin from his bag and starts dressing my foot firmly, but not too tight."
show ave serious with dis
hide tse with dis3
"Tsela retreats to the kitchen, cleaning pots and scraping waste into the fire."
"He looks and sounds a bit more cheerful than when he first came in."
show ave doubt with dis
m "\"So...\""
m "\"What have you been doing around the settlement since yesterday?\""
show ave serious eyes with dis
"He grunts."
show ave angry talking with dis
av "\"Let’s not talk about such things in Yiska’s house.\""
show ave shocked with dis
"He stops as his eyes linger over my chest."
show ave shocked talking with dis
av "\"Wow.\""
show ave shocked with dis1
show ave shocked talking with dis
av "\"Looks like you had a lot more excitement than me.\""
show ave serious with dis1
show ave serious talking with dis
av "\"There’s a lot of small cuts I’m seeing too.\""
show ave serious with dis1
show ave serious talking with dis
av "\"And... larger bruises.\""
show ave serious eyes with dis1
show ave serious eyes talking with dis
"He talks to Tsela in the Meseta language."
show ave serious with dis
"Tsela shakes his head before responding with what sounds like only a few words."
show ave doubt talking with dis
av "\"So it was only the two of you together last night?\""
show ave doubt with dis
m "\"Yeah.\""
"He doesn’t say anything for a while as he keeps dressing my foot."
show ave serious talking with dis
av "\"I was supposed to be back in Echo a few days ago.\""
show ave thinking with dis3
av "\"Another delay is going to be bad.\""
show ave thinking sad with dis
av "\"But if I can’t go out after dark then there’s not much else I can do but wait.\""
show ave serious
show tse at right
with dissolve
show tse talking with dis
ts "\"In two days I still plan to make the trip to Camp Rosa with Yiska.\""
show tse with dis
m "\"Are you still willing to take me?\""
show tse talking with dis
ts "\"Going there shouldn’t be a problem with the size of our cart.\""
show tse with dis1
show tse talking with dis
ts "\"You’d have to ride.\""
show tse eyes with dis1
show tse eyes talking with dis
ts "\"I don’t think you could keep up with us on foot.\""
show tse with dis1
show tse talking with dis
ts "\"And it won’t be comfortable, but it will definitely be possible.\""
show tse with dis
m "\"The back of the cart it is, then.\""
show tse talking with dis
ts "\"You just can’t come back with us since our cart won’t be empty.\""
show tse with dis
m "\"Trust me, that ain’t a problem.\""
show ave serious talking with dis
av "\"Regardless, it’s something to think about for later.\""
show ave eyes with dis1
show ave eyes talking with dis
av "\"As for right now, let’s go pick you out a walking stick.\""
show ave with dis
"Tsela and Avery talk to each other as Avery rises, giving me his arm to help me lean on him and stand."
stop music fadeout 2.0
$ renpy.music.set_volume(1.0, delay=2.5, channel='background')
scene reservation with dissolve
play sound ("sfx/keyopen.ogg")
"We all exit the cabin and Tsela locks the door behind us."
stop sound
"Tsela walks off in one direction without another word to me."
show ave serious with dissolve
m "\"Where’s he off to so fast?\""
show ave serious talking with dis
av "\"He’s meeting Yiska near the apiary.\""
show ave doubt with dis
m "\"The what?\""
show ave serious talking with dis
av "\"It’s a bee farm.\""
show ave serious with dis1
show ave serious talking with dis
av "\"Honey gets gathered there.\""
show ave serious with dis
"I want to express gratitude for what he did for me last night..."
"But what happened after that still unnerves me."
show ave thinking with dis3
av "\"Your stoat friend will be there too.\""
av "\"The reverend is letting him in.\""
scene bg black with dissolve
stop background fadeout 3.0
play music ("sfx/forestbirds.ogg") fadein 3.0
scene settlementforestday
show ave thinking eyes at center,forestlight
show expression AlphaMask("foliage", At("ave thinking eyes", center)) as mask:
    alpha 0.3
with dis3
m "\"How do you know that?\""
show ave serious talking
show expression AlphaMask("foliage", At("ave serious talking", center)) as mask:
    alpha 0.3
with dis3
av "\"I saw him and Yiska coming back from the mesa this morning.\""
show ave serious
show expression AlphaMask("foliage", At("ave serious", center)) as mask:
    alpha 0.3
with dis
m "\"While you were doing what?\""
show ave thinking sad
show expression AlphaMask("foliage", At("ave thinking sad", center)) as mask:
    alpha 0.3
with dis3
av "\"Just looking for the right pile of rocks based on what the elders who still live here could tell me.\""
play sound ("sfx/forestwalk.ogg")
"The pine needles crunch beneath our feet as I lean on Avery until we find a clearing with lots of fallen branches and dead saplings."
"There’s a sweet smell that lingers in the air — mostly likely from all the smoke of a small settlement waking up, along with the scent of pine sap."
stop sound
show ave serious eyes talking
show expression AlphaMask("foliage", At("ave serious eyes talking", center)) as mask:
    alpha 0.3
with dis
av "\"You know, there’s not a whole lot of places I can be with guards around.\""
show ave serious
show expression AlphaMask("foliage", At("ave serious", center)) as mask:
    alpha 0.3
with dis
"I feel my chest clench a bit."
m "\"So you were looking for your sister?\""
show ave angry talking
show expression AlphaMask("foliage", At("ave angry talking", center)) as mask:
    alpha 0.3
with dis
av "\"Where they put her body at the very least.\""
show ave serious
show expression AlphaMask("foliage", At("ave serious", center)) as mask:
    alpha 0.3
with dis
"He picks up a few sticks, swinging them for size and checking them for rot."
show ave serious eyes
show expression AlphaMask("foliage", At("ave serious eyes", center)) as mask:
    alpha 0.3
with dis
m "\"Did you find it?\""
show ave thinking sad
show expression AlphaMask("foliage", At("ave thinking sad", center)) as mask:
    alpha 0.3
with dis3
av "\"I think so, but I can’t be sure.\""
show ave thinking look
show expression AlphaMask("foliage", At("ave thinking look", center)) as mask:
    alpha 0.3
with dis
av "\"The graves are unmarked, and there were certainly some beneath the rocks.\""
show ave thinking
show expression AlphaMask("foliage", At("ave thinking", center)) as mask:
    alpha 0.3
with dis
av "\"I wasn’t going to disturb anybody’s resting place to confirm if it was hers or not.\""
show ave serious eyes
show expression AlphaMask("foliage", At("ave serious eyes", center)) as mask:
    alpha 0.3
with dis3
m "\"Again, I’m sorry.\""
show ave serious talking
show expression AlphaMask("foliage", At("ave serious talking", center)) as mask:
    alpha 0.3
with dis
av "\"I wasn’t expecting to find her anyway.\""
show ave serious eyes with dis1
show expression AlphaMask("foliage", At("ave serious eyes", center)) as mask:
    alpha 0.3
show ave serious eyes talking
show expression AlphaMask("foliage", At("ave serious eyes talking", center)) as mask:
    alpha 0.3
with dis
av "\"But it’s difficult never getting to know the exact place.\""
show ave serious
show expression AlphaMask("foliage", At("ave serious", center)) as mask:
    alpha 0.3
with dis
"He hands me two sticks."
show ave serious talking
show expression AlphaMask("foliage", At("ave serious talking", center)) as mask:
    alpha 0.3
with dis
av "\"Lift your leg and test them.\""
show ave serious
show expression AlphaMask("foliage", At("ave serious", center)) as mask:
    alpha 0.3
with dis
"The bark is gone, so it’s easy enough to hold onto both of them and swing my way through a triangular stance."
m "\"They’re working.\""
show ave serious talking
show expression AlphaMask("foliage", At("ave serious talking", center)) as mask:
    alpha 0.3
with dis
av "\"They should hold you for a least a week if you’re careful.\""
show ave serious
show expression AlphaMask("foliage", At("ave serious ", center)) as mask:
    alpha 0.3
with dis1
show ave serious talking
show expression AlphaMask("foliage", At("ave serious talking", center)) as mask:
    alpha 0.3
with dis
av "\"Some of the wood is still green.\""
show ave serious
show expression AlphaMask("foliage", At("ave serious", center)) as mask:
    alpha 0.3
with dis
m "\"Right.\""
show ave serious eyes talking
show expression AlphaMask("foliage", At("ave serious eyes talking", center)) as mask:
    alpha 0.3
with dis
av "\"Now that you’re mobile again I figure I’d better mention that your travel companions were looking for you yesterday.\""
show ave serious
show expression AlphaMask("foliage", At("ave serious", center)) as mask:
    alpha 0.3
with dis
m "\"Were they?\""
m "\"Cliff seemed pretty preoccupied if I remember right.\""
show ave serious talking
show expression AlphaMask("foliage", At("ave serious talking", center)) as mask:
    alpha 0.3
with dis
av "\"Jeb and the fox expected you back in your room.\""
show ave serious eyes
show expression AlphaMask("foliage", At("ave serious eyes", center)) as mask:
    alpha 0.3
with dis1
show ave serious eyes talking
show expression AlphaMask("foliage", At("ave serious eyes talking", center)) as mask:
    alpha 0.3
with dis
av "\"They looked pretty concerned.\""
show ave serious
show expression AlphaMask("foliage", At("ave serious", center)) as mask:
    alpha 0.3
with dis1
show ave serious talking with dis
av "\"I figure it’s early enough that they should still be at the inn your stoat friend checked in at.\""
show ave serious
show expression AlphaMask("foliage", At("ave serious", center)) as mask:
    alpha 0.3
with dis1
stop music fadeout 3.0
play background ("sfx/birds.ogg") fadein 3.0
scene bg black with dissolve
scene reservation
show ave serious
with dis3
m "\"I thought Jeb was staying with you.\""
show ave serious eyes talking with dis
av "\"For a night, but I need to be alone for a spell.\""
show ave serious with dis
"He’s much tenser here than he was in the woods."
show ave thinking look with dis3
av "\"I heard about his argument with the stoat though.\""
av "\"The fox managed to smooth things over, some, but I know his mane’s still caught up in a few knots.\""
av "\"You should probably tell your traveling companions when you head off by yourself for private business.\""
show ave thinking sad with dis3
"He looks out into the woods."
av "\"Considering the circumstances.\""
show ave serious talking with dis3
av "\"Wouldn’t want them getting hurt searching for somebody who might not want to be found.\""
show ave doubt with dis1
show ave doubt talking with dis
av "\"Know what I mean?\""
show ave serious with dis
m "\"...Yeah, I do.\""
show ave serious eyes talking with dis
av "\"Alright then.\""
show ave serious with dis1
show ave serious talking with dis
av "\"I’ll check up on your injuries before I leave, but I need to get back to Echo sooner rather than later.\""
show ave with dis1
show ave talking with dis
av "\"Keep your nose clean until then.\""
show ave with dis1
show ave talking with dis
av "\"The Madam would be pretty cross with me if she knew I ran into you and you came back too beat up.\""
show ave doubt with dis
m "\"You ain’t responsible for me.\""
"And I can’t let you know that I don’t intend to go back to Echo."
m "\"Don’t waste any time looking for me if I can’t be found.\""
m "\"If we cross paths and you can help me that’s great and good, but...\""
m "\"You’ve already done more than enough.\""
m "\"The Madam don’t need to fuss at you on account of my own choices.\""
show ave serious eyes talking with dis
av "\"She’s usually understanding.\""
show ave serious with dis
"He nods his head."
show ave serious talking with dis
av "\"’Til next we meet.\""
show ave serious with dis
"I nod."
hide ave with dis3
"In the woods, he whistled while he walked away, but now he stays quiet, increasing his distance until he disappears between the pine trees."
#IF SAM TOOK THE MAP
if HaveMap == True:
    "It’s not his fault, but the way he talks about going back to Echo puts me on edge."
    "He’s been nothing but friendly and helpful to me, but I can’t help but think about how much he knows about me, and how freely he talks about it."
    "He treated my injuries the day I killed Jack."
    "He knows the direction I went and the direction I’ll go when it comes to running away."
    "Some part of me knows it’s terrible, but I’d surely breathe a little easier if he never made his way back to Echo."
    "Or at least delayed long enough to make it far, far away, even from the station at Camp Rosa."

"I lift my injured ankle off the ground and put my weight on the walking sticks."
"I have to hobble a bit before I get a feel for using them."
"But I make steady progress toward the direction of the inn."
stop background fadeout 3.0
scene bg black with dissolve
play music ("music/quiet.ogg") fadein 2.0
scene bg innlobby with dissolve
"The innkeeper barely looks at me as I make it through the front door and start my struggle up the steep stairs."
"Thankfully, the railing is sturdy."
play sound ("sfx/thud6.ogg")
"When I get to the front door of our room I accidentally lose my footing and my body thuds against the wood."
stop sound
mu "\"Coming!\""
play sound ("sfx/pages.ogg")
"I hear the sound of Murdoch’s voice and the sounds of scrabbling through papers on a desk before a chair pushes out and somebody’s footsteps get closer."
scene bg innroom with dissolve
play sound ("sfx/dooropen.ogg")
"The door opens."
stop sound
show mur at center,inn with dis3
"I can see the fox’s{nw}"
show mur fear d with dis
extend " expression shift from relaxed to nervous."
mu "\"...Oh, Sam.\""
"He looks me up and down."
mu "\"I’m relieved that you're back, but what happened?\""
show mur fear d at right with moveinright
play sound ("sfx/doorshut.ogg")
"He moves out of the doorway to make room for me."
stop sound
show jeb shocked at left,inn with dis3:
    xzoom-1
"I hobble my way to the bed less than graciously, and I see Jeb sitting on the bed across from mine."
"I’m used to him being calm, but he looks pretty disturbed looking at me."
show jeb shocked talking with dis
jeb "\"The hell happened to you?\""
show jeb shocked with dis
m "\"Got foolish and messed with the wrong farm animals.\""
show jeb doubt with dis
"He gives me a look like he doesn’t believe me."
"I give him a look back that I’m not exactly trying to hide my lie."
"More that I’m not going to talk about it."
m "\"Why exactly are you askin’, anyway?\""
m "\"I thought you left.\""
"Jeb looks like he’s about to say something, but Murdoch butts in."
show mur concerned d with dis
mu "\"He came back once I reassured him that our issues in the forest weren’t his fault, and that Cliff is going to pay him in full.\""
"I grimace a bit."
m "\"And Cliff agreed to all that, then?\""
show mur eyes talking with dis
mu "\"Cliff isn’t stupid, Sam.\""
show mur concerned d with dis
mu "\"He knows that if we want to go back home then we’re going to need a guide.\""
show mur sideeye with dis
mu "\"Frankly, I wouldn’t want to take us back to Echo either if I were our guide and weren’t given my pay up front and a proper apology.\""
show jeb talking with dis
jeb "\"I’m not that delicate.\""
show jeb with dis1
show mur concerned d
show jeb talking
with dis
jeb "\"So long as I have my pay guaranteed both ways there won’t be a problem.\""
show jeb with dis
"I give Murdoch a look."
m "\"And you’re certain this isn’t going to blow back in your face?\""
show mur eyes with dis
mu "\"I’ve made tougher bargains.\""
show mur talking with dis3
mu "\"So yeah, I’m pretty confident.\""
show mur smile with dis
"I nod slowly and sigh, rubbing the back of my head and pulling a piece of a twig out of my fur."

if MT_Points == 1:
    show jeb shocked with dis
    show mur sideeye with dis
    mu "\"Jeb, would you mind stepping out for a moment?\""
    show jeb with dis
    mu "\"There’s something private I want to talk about with Sam.\""
    show mur smile with dis
    show jeb talking with dis
    jeb "\"Don’t need to tell me twice.\""
    show jeb with dis
    "He sits up and straightens his cap."
    show jeb talking with dis
    jeb "\"There’s something I need to talk to Avery about.\""
    show jeb with dis
    "I remember that Avery said he wanted to be alone, and I mean to stop him{nw},"
    hide jeb
    show mur concerned d
    with dis3
    extend " but he’s out the door before I can muster up a call deep enough to hear."
    show mur eyes talking at center with dis3
    stop music fadeout 2.0
    "Murdoch starts pacing around the room."
    show mur concerned d with dis
    m "\"Can you quit walking like that?\""
    m "\"Makes me nervous.\""
    "He stops and he takes a look at me."
    show mur angry with dis3
    mu "\"You’re nervous?\""
    mu "\"I thought you were gone for good last night.\""
    "I want to say {i}so what if I was{/i}, but that’s probably not fair."
    m "\"I’ll let you know before I go.\""
    show mur fear d with dis3
    "He gives me a look like I’m looney."
    show mur sideeye with dis
    mu "\"You’re still going to try and go off on your own after it looks like you got tossed around and mangled?\""
    show mur concerned d with dis
    "All I can do is shrug."
    m "\"Where I go is my business.\""
    m "\"The longer I stay here in this little settlement, the less safe I’m gonna feel.\""
    m "\"I want to make my way to Camp Rosa as soon as possible.\""
    show mur fear d with dis
    mu "\"And what if I told you nowhere was as safe as you think?\""
    "That’s a weird thing to hear him say."
    m "\"Then I’d say it sounds like you’re looking for an excuse to keep me around.\""
    show mur sideeye with dis
    mu "\"So you admit you’re not even gonna try to come back with us to Echo.\""
    show mur concerned d with dis
    m "\"Not unless you’re interested in packing up with me and heading north.\""
    show mur sad with dis3:
        xzoom-1
    mu "\"I have too many obligations to do something like that.\""
    m "\"So now we’re starting to understand one another.\""
    show mur concerned d with dis3:
        xzoom 1
    m "\"We both have places to be and obligations to fulfill.\""
    show mur fear d with dis
    mu "\"If you walk out of here I can almost guarantee you’re not gonna make it.\""
    "I lean forward in my bed."
    m "\"You threatening me?\""
    mu "\"Quite the opposite.\""
    "He walks over to a desk, pulls out one of the shelves, and pulls a photograph from the shelf."
    show mur concerned d with dis
    mu "\"Do you recall that calotype we made of Mr. Tibbits standing on the rock?\""
    "That feels like forever ago after what we’ve been through."
    m "\"Sort of.\""
    mu "\"I got the chance to freeze the image.\""
    show mur fear d with dis
    mu "\"Flip the photo over.\""
    mu "\"Then take a look.\""
    "I do what he says and hold the picture in my hand."
    play music ("music/bedhorror.ogg") fadein 2.0
    show photocliff1 at center,inn with dis3
    "What the..."
    "It looks like something big."
    "With something wrong and contorted about its face."
    "The longer I look at it, the more I can almost smell the corpses of Jeb’s donkeys."
    m "\"This some kind of magic trick?\""
    show mur concerned d with dis3
    hide photocliff1 with dis3
    mu "\"You think I have the time and the bad humor to pull something like that?\""
    show mur fear d with dis
    mu "\"People are missing, cargo is destroyed, and now you’re injured.\""
    show mur concerned d with dis
    m "\"But we didn’t see anything like this when you took this picture.\""
    show mur sad with dis3:
        xzoom-1
    mu "\"And yet it was clearly right there.\""
    m "\"Well it’s gotta be some kind of wild animal right?\""
    show mur fear d with dis3:
        xzoom 1
    mu "\"Can you think of any wild animals that can turn invisible and tear a pack animal to shreds in minutes?\""
    "His voice is shaking a bit."
    show mur eyes talking with dis
    mu "\"Whatever this thing is, it could be anywhere at any time.\""
    show mur fear d with dis
    mu "\"As far as I’m concerned, the only safety there is is safety in numbers.\""
    show mur concerned d with dis
    "I feel my ears lower and my eyes widen."
    show mur fear d with dis
    m "\"Oh God.\""
    m "\"Cliff went off on his own last night for research, didn’t he?\""
    show mur concerned d with dis
    mu "\"He’s with one of Avery’s friends.\""
    show mur sad with dis3:
        xzoom-1
    mu "\"We need to find him and tell him about this.\""
    m "\"Do you think he’s fine?\""
    show mur concerned d with dis3:
        xzoom 1
    mu "\"Of course.\""
    mu "\"He’s with Avery’s friends.\""
    "There’s a surety and a confidence in his voice that makes me feel better."
    "There’s a small shadow of his face that makes me think otherwise."
    "Like he’s scared."
    "Absolutely terrified."
    "So I grab my walking sticks and make myself stand."
    m "\"Let’s go find him.\""
else:
    show jeb talking with dis
    jeb "\"Don’t grind your teeth on my account.\""
    show jeb doubt with dis1
    show jeb doubt talking with dis
    jeb "\"I’ll leave if I’m not wanted.\""
    show jeb with dis
    m "\"I don’t mean that at all.\""
    show jeb with dis1
    show jeb talking with dis
    jeb "\"Oh?\""
    show jeb with dis1
    show jeb talking with dis
    jeb "\"Explain what you mean.\""
    show jeb with dis
    m "\"I’m just surprised to see that an argument that bad wasn’t enough to chase you off.\""
    show jeb doubt with dis
    "He snorts."
    show jeb talking with dis
    jeb "\"It takes more than words to get rid of me.\""
    show jeb with dis1
    show jeb talking with dis
    jeb "\"I’ve put up with far worse for a paycheck.\""
    show jeb sad with dis1
    show jeb sad talking with dis
    show mur concerned d with dis
    jeb "\"Granted I’ve never taken this much cargo damage before, nor lost any pack animals.\""
    show jeb with dis1
    show jeb talking with dis
    jeb "\"Still, we’ve had a lot of luck since the assault, so it’s hard to be too pessimistic about our success, or lack of it, depending on how you want to look at things.\""
    show jeb with dis
    m "\"You did a better job at keeping us safe than I did.\""
    show jeb talking with dis
    jeb "\"I wouldn’t bring that up if you think it’s true.\""
    show jeb with dis
    m "\"I’m not really a bodyguard.\""
    show jeb doubt with dis
    "Jeb snorts."
    show jeb doubt talking with dis
    jeb "\"I was waiting for you to admit it.\""
    show jeb doubt with dis
    m "\"I dunno if you heard...\""
    show jeb shocked with dis
    m "\"But at the beginning of the trip, Professor Tibbits said he’s like us when he was talkin’ to you.\""
    show jeb sad talking with dis
    jeb "\"I pretended not to, since there were still other people around in earshot.\""
    show jeb sad with dis
    m "\"Right.\""
    show mur sideeye with dis
    m "\"Well I’m like that, in particular... for pay.\""
    show jeb doubt with dis
    "Jeb scrunches up his face, as if confused,{nw}"
    show jeb shocked with dis
    extend " before his eyes widen."
    show jeb shocked talking with dis
    jeb "\"Oh.\""
    show jeb shocked with dis
    m "\"Yeah.\""
    "He takes off his hat and fans himself with it."
    show jeb shocked talking with dis
    jeb "\"Well, that makes more sense than anything else you could have told me.\""
    show jeb shocked with dis1
    show jeb shocked talking with dis
    jeb "\"By your physique, I assumed you were an army deserter who didn’t know how to use a gun or somethin’.\""
    show jeb shocked with dis
    m "\"Thanks.\""
    show jeb shocked talking with dis
    jeb "\"I’ve had to fend off predators and bandits before, if you ever need advice in protecting yourself or others.\""
    show jeb with dis1
    show jeb talking with dis
    jeb "\"Kind of becomes second nature when you’re running a farm.\""
    show jeb doubt with dis
    show mur fear d with dis
    mu "\"I think we’re going to need that advice sooner than you might think.\""
    show mur concerned d with dis
    show jeb doubt talking with dis
    jeb "\"And why’s that?\""
    show jeb doubt with dis
    show mur fear d with dis
    mu "\"I have a good reason to believe our employer might be in trouble.\""
    mu "\"But I don’t have a whole lot of time to share why.\""
    show mur concerned d with dis
    m "\"Would you help us find him?\""
    show jeb sad talking with dis
    jeb "\"I don’t like the idea of doing that for free, but I have to admit I feel sorry for y’all.\""
    show jeb with dis1
    show jeb talking with dis
    jeb "\"Just tell me where you want to start lookin’.\""
    show jeb with dis1

###[cliff talk with yiska]
stop music fadeout 3.0
scene bg black with slow_dissolve
pause 1.2
"Through all of my long nights and all of my bitter travels, it wasn’t until last night that I thought, “My God, maybe this really was all worth it.”"
"I saw families gathering on the mesa."
"The beatific joy, and the good-natured laughter, and the colors borrowed from the good earth itself were not something my Grandfather, nor all the scholars of Europa could begin to dream of."
"I know I am a stranger in their midst, but after just one night, I do not feel this way."
"I dare not share it."
play background ("sfx/birds.ogg") fadein 3.0
play music ("music/a-moment-of-solace.ogg") fadein 3.0
scene reservation
show yis smile at right
with dis3
"The big, humble bear smiles at me as we walk."
show yis talking with dis
ys "\"Did you sleep well, Mr. Tibbits?\""
show yis smile with dis
"His accent is quite thick, but his grammar is wonderful, so I can still understand what he says."
"I assume he must think the same, considering Albion isn’t my first language either."
show yis with dis
cl "\"Oh, better than ages, really!\""
show yis talking with dis
ys "\"On rocks and furs?\""
show yis eyes with dis1
show yis eyes talking with dis
ys "\"I would have thought you’d prefer a softer, western style bed like at the inn.\""
show yis with dis
"I put my paws on my hips."
cl "\"Now I know I might look precious, but I can assure you that I’m used to roughing it just as much, if not more, than some of my companions.\""
"I found out last night that his role in this community was far more important than I initially knew — leading the first night of one of the chants."
cl "\"I’m just thankful that you’re willing to accompany me through the settlement and help me get my bearings.\""
show yis eyes talking with dis
ys "\"That chant will go on until another night, so I do not think we will find many others in the village to talk to.\""
show yis with dis
cl "\"Another night?\""
"I’ve heard of such practices before, but it’s a bit different to think about when you just spent most of the previous day participating in one."
show yis talking with dis
ys "\"Yes?\""
show yis with dis1
show yis talking with dis
ys "\"That’s one of the shorter chants.\""
show yis with dis1
show yis talking with dis
ys "\"Sometimes they’re longer.\""
show yis with dis
cl "\"What’s the longest one you can remember?\""
show yis eyes with dis
"He pauses."
show yis talking with dis
ys "\"Seven days?\""
show yis with dis
cl "\"That’s so long!\""
show yis smile with dis
"He chuckles."
show yis eyes talking with dis
ys "\"Sometimes there’s a lot to cover.\""
show yis with dis
"I stop walking, turn to him, and give him a quick bow."
cl "\"Making you leave a chant early on my accord would leave a stain on my conscience.\""
cl "\"If my presence has intruded upon or interrupted your way of life in any way, I have to humbly apologize.\""
show yis smile with dis
"The bear smiles and scratches the back of his head."
show yis talking with dis
ys "\"That sort of chant is one we do whenever we feel a need for it.\""
show yis with dis1
show yis talking with dis
ys "\"There will be others like it.\""
show yis with dis1
show yis talking with dis
ys "\"And you know, we’ve had anthropologists visiting us for decades.\""
show yis with dis1
show yis talking with dis
ys "\"Some stay for much longer than a mere week, at least since the treaty of 1868.\""
show yis eyes with dis1
show yis eyes talking with dis
ys "\"Sometimes we get so used to them living in the community and asking questions they, as a joke, become considered a part of the family.\""
show yis with dis
cl "\"That’s so...\""
cl "\"Nice.\""
cl "\"It’s nice, really.\""
scene residential church
show yis at right
with dissolve
show yis talking with dis
ys "\"I don’t necessarily mean that it’s ideal for everybody.\""
show yis with dis
cl "\"Oh, of course.\""
show yis eyes talking with dis
ys "\"Just more so that it is a peculiarity we’ve had to get used to?\""
show yis with dis1
show yis talking with dis
ys "\"Anthropologists like you have aided missionaries in a group effort to translate and record our language and our beliefs.\""
show yis with dis1
show yis talking with dis
ys "\"But that doesn’t mean they are respected, or valued more than as a curiosity.\""
show yis with dis
cl "\"I see.\""
cl "\"Are there words that haven’t been translated yet?\""
show yis talking with dis
ys "\"Yes...\""
show yis with dis1
show yis talking with dis
ys "\"Especially ones they already have words for.\""
show yis with dis1
show yis talking with dis
ys "\"But we have our own names for wildlife and flowers.\""
show yis eyes with dis1
show yis eyes talking with dis
ys "\"There are customs that we do not feel comfortable sharing, too.\""
show yis with dis
"I point to a nearby oak tree that’s sitting next to the church."
cl "\"Could I hear your name for that?\""
show yis smile with dis
"The bear smiles and clears his throat."
show yis talking with dis
"I think I hear him say something along the lines of Alona but I can’t be certain."
show yis with dis
ca "\"Quite the odd couple you make.\""
show cal arm with dissolve
"Caldwell is standing outside of the church."
stop music fadeout 4.0
show cal angry arm talking with dis
ca "\"You’re late again.\""
show cal angry arm with dis
"I take a look at my pocket watch."
cl "\"Only fifteen minutes.\""
"The reverend rolls his eyes."
show cal eyes arm talking with dis
ca "\"Consistent at least.\""
show cal angry arm with dis1
show cal angry arm talking with dis
show yis eyes with dis
ca "\"Fifteen minutes may be nothing to you, but the children are on a schedule.\""
show cal arm with dis1
show cal arm talking with dis
ca "\"Given that the nature of your thesis centers on work, I thought it would be pertinent to show you how the sustainability of this settlement starts with school.\""
show yis with dis
show cal arm with dis
"He beckons us down the hallway leading to the chapel."
"It’s empty right now, and he leads us through a corridor on the left side of the crucifix-shaped building."
stop background fadeout 0.0
scene settlementschool
show cal arm
show yis at right
with dissolve
"It leads to a long room furnished modestly."

"Several dozen boys and girls dressed in white shirts and black pants are looking over the Bible, copying specific passages onto brown paper with quills and ink."

"It doesn’t look that different from my schooling experience."

"Aside from the fact that everybody is much better behaved."

"But what strikes me as odd is the quiet."

"Back in my schooldays, there would be whispers and giggles between compatriots in even the quietest of study halls, on occasion."
"But here the room is only filled with the sound of scratches on paper and the bubbling of ink."
show cal smug talking with dis3
ca "\"Heating and guaranteed lunch and morning meals that they would often otherwise miss are provided.\""
show cal smug with dis1
show cal smug talking with dis
ca "\"Access to books and writing tools are also ensured.\""
show cal arm with dis3
"He turns to me suddenly and his robe flutters with the sharp turn."
show cal arm talking with dis
ca "\"Do you have questions or concerns so far?\""
show cal arm with dis
cl "\"None, really.\""

"Based on Avery’s story about his sister, I expected to see starvation conditions, illnesses, injuries, or devices of misconduct."

"But everything here looks incredibly ordinary."

"I could easily see myself attending a school not unlike this in Batavia, had my parents been poorer."

show cal with dis3
"Caldwell makes a gesture with his wing for the two of us to follow him still."
show cal talking with dis3
ca "\"While every child must learn to read and write, few pursue scholarly paths in isolation.\""
show cal eyes with dis1
show cal eyes talking with dis
ca "\"It is crucial to train students to work with their hands just as well as their minds.\""
show cal arm with dis3
play sound ("sfx/schooldoor.ogg")
"As he opens the door to the outside we feel a wave of heat enter the building."
stop sound
play background ("sfx/bees.ogg") fadein 2.5
scene bees
show cal arm
show yis at right
with dissolve
"But we come upon a field with bright green grass, and the sky is crystal-blue."

"Goodness gracious is it difficult to conceal my excitement."

"There are wild flowers and fruit trees of many varieties placed perfectly into snug, raised beds."

"A low drone comes from boxes and boxes of honey bees, aligned in rows like soldiers."

"I can make them out even from far away, and I can see them flit to and fro, like fairies with iridescent wings, wiggling their wee fuzzy bodies free from pollen as a pixie would stardust."
show cal eyes talking with dis3
ca "\"Bees could be considered the forebears of a self-sufficient civilization.\""
show cal with dis1
show cal talking with dis
ca "\"Without them, the flowers wouldn’t breed.\""
show cal with dis1
show cal talking with dis
ca "\"Without them, the fruits wouldn’t grow.\""
show cal with dis1
show cal talking with dis
ca "\"They live in harmony, communicating with one another to serve their queen, bringing life and treasure to all of God’s creatures.\""
show cal eyes with dis1
show cal eyes talking with dis
ca "\"There is no nobler creature than the humble honey bee.\""
show cal with dis
"One is still wiggling its butt."
show cal arm talking with dis3
ca "\"Yiska can show you how they are tended.\""
show cal arm with dis
cl "\"Oh, truly?\""
show cal eyes talking with dis
ca "\"He was one of my best students.\""
show cal with dis1
show cal talking with dis
ca "\"That is why he still tends to the bees and is granted privileges here and there for his ongoing toils past graduation.\""
show cal with dis
show yis eyes talking with dis
ys "\"They are appreciated, Reverend.\""
show yis with dis
show cal smug talking with dis
ca "\"Though you do have your helpers, don’t you?\""
show cal with dis
show yis smile with dis
ys "\"Kids just like me.\""
show cal arm talking with dis3
ca "\"It takes particular tactics and temperaments to command respect.\""
show cal smug arm with dis1
show yis with dis
show cal smug arm talking with dis
ca "\"Take notes from him, Mr. Houwelinck.\""
show cal arm with dis
"He turns to go and then doubles back."
show cal arm talking with dis
ca "\"Oh. If you finish with the bees early, do show him some carpentry as well.\""
show cal arm with dis
ys "\"Yes, Reverend.\""
hide cal with dissolve
show yis eyes with dis
"The bear exhales when Caldwell is gone."
show yis talking with dis
ys "\"I take it you’ve never collected honey before?\""
show yis with dis
cl "\"I should say not.\""

cl "\"Why, I’d never forgive myself if I crushed some by accident, or made a mess of all the precious honeycomb.\""

cl "\"Besides...\""

cl "\"Stingers hurt!\""
show yis smile with dis
ys "\"We have ways to protect you from that.\""
show yis talking with dis
ys "\"Here, come to the shed.\""
show yis with dis
"We tromp on over to a white-washed shed with a padlock."
play sound ("sfx/padlock.ogg")
"Yiska unlocks it and lifts a heavy latch from several bars."
stop sound
"It’s very secure for a shed."
play sound ("sfx/doorcreakopen.ogg")
$ renpy.music.set_volume(0.20, delay=1.0, channel='background')
scene settlementshed
show yis at right,dark3
with dissolve

"Inside, there are hats with nets tied to the brim, and thick, hardy gloves made of reinforced canvas."
stop sound
"There’s an entire suit made of the material too."
show yis talking with dis
ys "\"You can try the bee suit on if you need full protection.\""
show yis with dis
cl "\"Hardly necessary.\""

cl "\"If my paws and peepers are covered, that’s more than ample protection for me!\""
show yis talking with dis
ys "\"Grab the hat and gloves then.\""
show yis eyes with dis1
show yis eyes talking with dis
ys "\"...You don’t need to put them on yet.\""
show yis with dis
cl "\"Right.\""
#sfx?
"Yiska pulls something off of a barrel. It looks like a metal can with a bellows attached behind it that has a long metal tip that’s stoppered with a cork."

cl "\"What kind of contraption is this?\""
show yis talking with dis
ys "\"It’s a smoker.\""
show yis with dis
"He takes the lid off and shows me a hollow well inside of the metal can."
show yis talking with dis
ys "\"We can start a flame with cardboard and pine needles that burns inside, and we can puff out the smoke using the spout and the bellows.\""
show yis with dis
cl "\"Why do you need to make smoke?\""
show yis eyes talking with dis
ys "\"It makes the bees docile.\""
show yis with dis
"He pulls a piece of cardboard off of the shelf and rolls it into a little band."
play sound ("sfx/lighteron.ogg")
"Then he takes a lighter from his pocket, ignites it, and puts it in the smoker."
$ renpy.music.set_volume(1.00, delay=3.0, channel='background')
scene bees
show yis at right
with dissolve
"We leave the shed, locking it behind us as the bear leans over to scoop dry pine needles off of the floor, stuffing them into the smoker."
stop sound
"He takes a while to do this, stuffing more pine nettles in than I had thought possible."

"But eventually he closes the top and squeezes the bellows a few times to show me the puffs of concentrated smoke that emit from the spout."
show yis talking with dis
ys "\"Now you want to put the netting on.\""
show yis with dis
cl "\"Righto.\""
#sfx
show beehat with dis3
"The bear squeezes the bellows and aims the nozzle at the opening of the box where bees are climbing out."
play music ("sfx/flies.ogg") fadein 4.0
"Thick puffs of smoke shoot their way into the boxes and the droning gets louder."
cl "\"I thought you said they’re supposed to calm down!\""
show yis eyes talking with dis
ys "\"Give them five minutes.\""
show yis with dis
"I look into the distance."
"I see a young squirrel in a school outfit, nailing planks together."
"An older, male dog monitors her."
"The shape of it reminds me of all the flower beds around us."
"I have to resist asking to get involved."
cl "\"While we wait...\""
cl "\"Is it true what the reverend said?\""
cl "\"That the kids like you?\""
show yis eyes with dis
"The {nw}"
show yis with dis
extend "bear blinks."
show yis talking with dis
ys "\"They can see that I’m strong... and can do some things they can’t, yet.\""
show yis with dis1
show yis talking with dis
ys "\"That often impresses children.\""
show yis with dis
cl "\"Right, but he said they like you.\""
cl "\"Do they tell you much about their experiences in school?\""
show yis eyes talking with dis
ys "\"No more than I already know.\""
show yis with dis
"So what do you know?"
show yis eyes talking with dis
ys "\"Rewards come if you behave.\""
show yis eyes with dis1
show yis eyes talking with dis
ys "\"Consequences come if you do not.\""
show yis with dis
cl "\"Consequences like what?\""
show yis talking with dis
ys "\"Weren’t you punished in school when you didn’t obey your teachers?\""
show yis with dis
cl "\"I’ve had my paws slapped by a ruler more times than I’d like to count.\""
show yis eyes with dis
"He nods."
show yis talking with dis
ys "\"I am treated well when I keep to myself, and when I listen.\""
show yis with dis
cl "\"I see.\""
stop music fadeout 6.0
$ renpy.music.set_volume(0.60, delay=6.0, channel='background')
"He wipes his brow."
show yis talking with dis
ys "\"The bees should be calm by now.\""
show yis with dis
play sound ("sfx/scrape4.ogg")
"He steps over to lift the box."
stop sound
"The bees are all jittering, moving slower than they were before."
"He pulls out a wooden sheath that’s covered on one side by drowsy looking bees, and a thick, golden, hive-like pattern of hexagons."
show yis smile with dis
cl "\"Oh, that’s beautiful.\""
show yis talking with dis
ys "\"The honey here has a distinct smell too.\""
show yis with dis
"It smells shyly of honeysuckle, but there is a strong, melony scent of saguaro flowers within."
cl "\"Beautiful.\""
show yis smile with dis
ys "\"As the reverend said, that’s just the miracle of bees.\""
show yis with dis
"He scrapes off a nugget of waxy honey comb and holds it out to my paw."
show yis talking with dis
ys "\"Try it.\""
show yis with dis
"I pick it off of his tool and pop it into my mouth."
"The crunch is followed by the bright, floral taste, and it melts in my mouth."
show yis smile with dis
"I can’t help but lick all of it off of my fingers, which makes the bear start laughing."
cl "\"What? It’s good.\""
show yis talking with dis
ys "\"I just pictured you as a more delicate eater.\""
show yis smile with dis
cl "\"Not when I’m ravenous.\""
"I forgot that we didn’t even eat breakfast, and my stomach rumbles."
"The honey should hold me over for now."
"A sudden draft blows in, and it blows soft ripples over the grass."
"The trees rustle as I feel the cool air against my skin and smell the honey hovering over me."

menu cliffchoice4:
    "I guess it might not be so bad here after all.":
        "This really is a beautiful area, and the people here are taken care of."
        "It’s wrong what this country is doing to their culture, but civilization creeps into every corner of the world eventually."
        "Pretty paintings and fantastic tales might have brought me this far, but the transcontinental railroad is what’s real."

    "There are too many implications which concern me.":
        "Of course a school like this would seem normal to me."
        "I’ve never known much different."
        "But it’s different for the people who live under the thumb of this country."
        "Despite how sweet the honey might taste or how beautiful the land is here, these people still aren’t given a choice in the matter, what this country tries to do with them."
        $ CorMor += 1


show yis surprised with dis
"But as soon as I pluck my own board of beeswax out of the hive, a sound disturbs the peace."
"Somebody barks out a call from the wheat field behind us."
"We both turn around and my heart sinks a bit to see Tsela."
"I can tell that he doesn’t much care for me, but I don’t want to cause any trouble."
show tse at left behind beehat with dissolve:
    xzoom-1
show tse talking with dis
"He starts talking in the Meseta language."
show tse with dis
"I don’t know if he knows, but I can understand him."
"I can make out injury, beast, white and corpses."
"Tsela is pointing over to something in the cornfield and Yiska is looking back."
show yis surprised talking with dis
"I can translate the bear’s response to something close to {i}are you sure{/i}?"
show yis surprised with dis
show tse talking with dis
"Tsela, undeniably, says {i}yes{/i} several times."
show tse with dis
cl "\"What are the two of you talking about?\""
show tse angry with dis
"Tsela sucks through his teeth."
show yis surprised talking with dis
show tse with dis
ys "\"He should know.\""
show yis surprised with dis
cl "\"Know what?\""
show tse angry with dis
"The fox gives me a dirty look,{nw}"
show yis angry with dis
show tse eyes with dis
extend " but the bear gives him one that makes him stand down."
show tse with dis
show yis talking with dis
ys "\"Follow.\""
stop background fadeout 3.0
$ renpy.music.set_volume(1.00, delay=6.0, channel='background')
scene cornfield
show beehat
with dissolve
"We walk for a few minutes towards the center of the corn field."
play background ("sfx/flies.ogg") fadein 2.0
"I hear bees swarming."
"Or at least things that look like bees."
"Beeflies."
play music ("music/horrorpiano.ogg")
scene cornmule
show beehat
with dis3
"And they’re swarming a large chunk of meat on the ground."
"It looks like what remains of a pack mule and I want to retch."
show yis surprised at right behind beehat
show tse angry at left behind beehat:
    xzoom-1
with dis3
cl "\"This is awful.\""
cl "\"How did it die?\""
show tse angry talking with dis
ts "\"This isn’t the only one.\""
show tse angry with dis1
show tse angry talking with dis
ts "\"Five penned pack animals were slaughtered last night that I’ve seen so far.\""
show tse angry with dis
cl "\"Is this the work of that animal that was tracking us in the woods?\""
show tse angry with dis
cl "\"What does this mean?\""
show tse angry talking with dis
"Tsela says something."
show tse angry with dis
"It sounds an awful lot..."
"...like {i}no way out on foot or cart{/i}."
cl "\"What does he mean by that?!\""
show tse eyes talking with dis
ts "\"Don’t concern yourself.\""
stop music fadeout 5.0
show tse angry with dis
ca "\"I think I have a right to be concerned.\""
play sound ("sfx/gravelwalk.ogg")
"We hear the voice of the reverend walking through the field in a surprisingly rapid gait."
show cal angry arm behind beehat with dissolve
show cal angry arm talking with dis
show yis surprised with dis
ca "\"I could hear all the way across the field that you both weren’t speaking Albion.\""
stop sound
show cal angry arm with dis1
show cal angry arm talking with dis
play music ("music/contemplation.ogg") fadein 2.0
ca "\"What’s this commotion all about?\""
show cal angry arm with dis
"Yiska suddenly looks very anxious."
hide tse with dis3
"Tsela spits on the ground and turns away."
show cal angry arm talking with dis
ca "\"Address me, Tsela Begay!\""
show cal angry arm with dis
"He keeps on walking as he disappears into the cornfield."
show cal angry arm talking with dis
ca "\"That man is out of order.\""
show cal angry arm with dis
show yis surprised talking with dis
ys "\"I apologize for his behavior, Reverend.\""
show yis surprised with dis
show cal angry arm talking with dis
ca "\"I’ll talk to him tonight.\""
show cal angry arm with dis1
show cal angry arm talking with dis
ca "\"I’m less concerned with him than I am with you, Yiska.\""
show cal angry arm with dis1
show cal angry arm talking with dis
ca "\"I know that you were not speaking Albion with him.\""
show cal arm with dis
show yis talking with dis
ys "\"It was urgent.\""
show yis eyes with dis1
show yis eyes talking with dis
ys "\"An old habit, nothing more.\""
show yis with dis
show cal angry arm talking with dis
ca "\"A habit that I thought had died, Yiska.\""
show yis eyes with dis
show cal angry arm with dis1
show cal angry arm talking with dis
ca "\"You know what we must do.\""
show yis with dis
show cal arm with dis1
show cal arm talking with dis
ca "\"Come along, Mr. van Houwelinck.\""
show yis with dis
show cal arm with dis
"I’m not sure what’s going on right now, but they’re both tense."
cl "\"Come along where?\""
show cal arm eyes talking with dis
ca "\"To the sink, where else?\""
stop background fadeout 1.0
show cal arm with dis1
scene black with dissolve
scene residential church
show cal arm
show yis at right
show beehat
with dissolve
"There’s a small lean-to against the church with a sink and a spicket."
#sfx
show cal with dis3
"Caldwell pulls out a bucket from beneath the sink, producing a white-grey slab of chalky substance."

"He slices a sliver of the stuff and holds it in front of the bear’s face."
show cal talking with dis
ca "\"Remember?\""
show cal with dis
"The bear isn’t looking directly at him."
show yis talking with dis
ys "\"Yes, Reverend.\""
show yis eyes with dis
show cal talking with dis
ca "\"Open.\""
show yis with dis
show cal with dis
"I’m not sure what’s happening in front of my eyes but I don’t like it one bit."
cl "\"Reverend...\""
cl "\"What is that?\""
show cal smug talking with dis
ca "\"It’s soap, Mr. van Houwelinck.\""
show cal with dis1
show cal talking with dis
ca "\"The cheapest you can make with lard and wood ash.\""
show cal eyes with dis1
show cal eyes talking with dis
ca "\"It’s the only thing you need to clean a dirty mouth though.\""
show cal with dis

menu cliffchoice5:
    "Don’t interfere.":
        "This is not my home, not my country."
        "These people are strange and barbaric to me."


    "Stop him.":
        show cal angry with dis
        cl "\"No, you can’t!\""
        "The words are blurted from my mouth before I can stop them."
        "The reverend tilts his head at me and stares."
        show cal angry talking with dis
        ca "\"I can’t do what, Mr. van Houwelinck?\""
        show cal angry with dis
        "He looks annoyed, like I’m some sort of petulant child making a scene rather than pointing out what he’s doing is dangerous."
        cl "\"Lye is toxic!\""
        cl "\"It can leave chemical burns inside of his mouth.\""
        show yis talking with dis
        ys "\"Reverend, please...\""
        show yis with dis
        "Yiska’s face looks very calm."
        "Too calm."
        show cal with dis
        show yis talking with dis
        ys "\"Don’t pay him any mind.\""
        show yis with dis1
        show yis talking with dis
        ys "\"Give me the soap.\""
        show yis with dis
        "I can’t believe what I’m hearing."
        show cal eyes talking with dis
        ca "\"Of course, my son.\""
        show cal with dis
        $ CorMor += 1

show yis eyes with dis
"As hard as it is to watch, I see the bear take the bar with very little hesitation and put it in his mouth."
"The reverend nods, and places his wing like a solemn parent on the bear’s back as he watches the bear choke and sputter on the suds."
show cal talking with dis
ca "\"That’s enough.\""
show cal with dis
"He speaks gently."
show cal eyes talking with dis
ca "\"Now spit it out.\""
play sound ("sfx/wsplash.ogg")
show cal with dis
"Some of the foam that hits the grass is pink."
stop sound
show yis with dis
"Despite forced tears, Yiska looks up with a determined facial expression."
show yis eyes with dis
"He heaves as he continues to spit."
show cal talking with dis
ca "\"Don’t let this memory fade as quickly as the last.\""
show cal with dis
show yis eyes talking with dis
ys "\"Yes, Reverend.\""
show yis angry with dis
"I want to say something, but when I start, the bear looks at me with the first flash of anger I’ve seen in his eyes."
"He’s angry at me."
show cal arm talking with dis3
ca "\"What were the two of these men talking about, Mr. van Houwelinck?\""
show cal arm with dis
cl "\"I...\""
"Does he want me to lie?"
"Does he want me to tell the truth?"
"I don’t know."
"This is horrible!"
cl "\"Something about corpses I think.\""
cl "\"Something from the woods might be killing all of the stock animals.\""
show cal angry arm with dis
"Caldwell looks at me like I’ve lost my mind."
show cal angry arm talking with dis
ca "\"All of the stock animals?\""
show cal arm with dis
show yis with dis
"He turns to Yiska."
show cal arm talking with dis
ca "\"Go home and clean yourself up.\""
show cal eyes arm with dis1
show cal eyes arm talking with dis
ca "\"Leave us.\""
show cal arm with dis
show yis eyes talking with dis
"He muffles something like {i}‘Yes, Reverend,’{/i} but it’s impossible to tell what he really said."
show yis eyes with dis1
hide yis
show cal angry arm
with dis3
"Caldwell takes a good look at me, as if I’m a child who dragged mud into his house, and trembles,"
show cal angry arm talking with dis
ca "\"Cornelis van Houwelinck...\""
show cal angry arm with dis1
show cal angry arm talking with dis
ca "\"Since the moment you stepped into this settlement, I’ve seen nothing but insubordination and instigation.\""
show cal angry arm with dis
cl "\"But I haven’t done anything, Reverend.\""
show cal angry arm talking with dis
ca "\"Does it matter if you did?\""
show cal angry arm with dis1
show cal angry arm talking with dis
ca "\"It’s certainly somebody you brought along.\""
show cal angry arm with dis1
show cal angry arm talking with dis
ca "\"I just made a loyal man clean his mouth until it bled for the first time in fifteen years.\""
show cal angry arm with dis1
show cal angry arm talking with dis
ca "\"These are extraordinary circumstances in the most nefarious sense.\""
show cal angry with dis3
"He grabs me by the shoulder and drags me to the white-washed shack."
play sound ("sfx/thud6.ogg")
queue sound ("sfx/doorslam.ogg")
scene settlementshed
show beehat at dark3
with hpunch
"He unlatches the locks and throws me in."
ca "\"And remove the church property you’re wearing at once!\""
stop sound
cl "\"Sir, this is a gross over-reaction to any sort of offense I could’ve afflicted you with!\""
cl "\"Address your quarrels with me at once, or I’ll be reporting this to either my father or Mr. Hendricks!\""
scene settlementshedback
show beehat at dark3
with dis3
"I look through the screen door covered in bars, expecting him to look back at me, angrily, ready to quarrel, but that’s not the case."

"His back is to me and he’s running away."

cl "\"What?\""
play sound ("sfx/doorrattle.ogg")
"I try to open the door, but I know it’s locked from the outside."
play sound ("sfx/thud7.ogg")
"My body thuds uselessly against the sound of shaped metal."
stop sound
cl "\"Caldwell!\""

cl "\"Come back here at once, Caldwell!\""
"I try to rattle the door, but it’s just too heavy."

"I’m starting to notice how warm it is in here."

"I’m sweating, and I try not to panic about how I haven’t drunk any water in hours."
play sound ("sfx/knock.ogg")
"I bang again, hoping to see the man or the young girl who was out on the lawn."
stop sound
"But I hear nobody."

"My arms and the back of my neck are already wet."

"I feel a little dizzy now, but I try not to panic."
#sfx
hide beehat with dis3
"Most of the things here are shovels, pots, and protective clothes."
"I can see that there’s something behind this counter."
"A hand shovel!"
"I look at the floor and sigh in relief."
"Dirt."
"I should be able to dig myself out."
"But I have to be careful not to waste energy or moisture."
"I look outside again for anybody."
cl "\"Help!\""
cl "\"Help me!\""
cl "\"I’m stuck in a shack!\""
"Nobody still."
"So that’s it then."
"I’m going to have to dig."
"I wipe my brow and look for the clearest space against a wall I can find."
play sound ("sfx/dig3.ogg")
"The first scoop of earth is very warm, very dry, and kicks up a cloud of dust. I have to turn my head not to inhale any."
stop sound
"Below that I’m happy to feel a cooler layer."
"It’s not as tough to move as I thought it would be."
play background ("sfx/digloop.ogg")
"But there’s a lot of it."
"I think I see where the wall of the shack ends and the beginning of the earth starts."
"Then I see concrete blocks."
"My heart sinks, knowing I’ll have to dig deeper."
"But there’s no time to waste."
show deepmine with dis3:
    alpha 0.25
"I can’t tell how long I do this for."
"The lighting outside has changed and I still hear nobody."
stop background fadeout 1.0
"I stand up to check for people every so often."
"Nobody comes on the lawn."
"Caldwell must have instructed them not to."
"Rail deal ambitions or no, this behavior is not acceptable."
"One of the first things I intend to do after breaking out of this god-forsaken cage is to find a telegraph machine and wire everything I know to my father and Mr. Hendricks."
play sound ("sfx/dig2.ogg")
"I do another scoop."
play sound ("sfx/dig1.ogg")
"Then another."
stop sound
"I think I'm on scoop four hundred or so, but I started to lose count in the 300’s."
show black with dis3
"Everything goes sideways for a moment{nw}"
hide black with dis3
extend " and I stop to breathe."
"I’m really thirsty."
play sound ("sfx/shovel1.ogg")
"I take another scoop and flinch when I hear a clang."
"What?"
stop sound
"I dig as quickly as I can with both hands."
cl "\"No...\""
"There’s a mixture of rock and concrete below."
"I can’t get out."
"The dirt was poured on top of the rocks and concrete."
"What is the purpose of this?"
"My heart’s beating faster."
show black with dis3
"I’m starting to feel dizzy."
hide black with dis3
play sound ("sfx/pipe.ogg")
"I throw down the trowel in frustration but the side catches the side of my nail."
stop sound
"An awful noise comes out of me, and I start to bleed a little."
ca "\"Oh, it doesn’t look that deep.\""
stop music fadeout 4.0
cl "\"You!\""
ca "\"Brush yourself clean and come on out of the dirt, you fool.\""
cl "\"Don’t you say another word!\""
scene bees
show cal arm at center,dark3
show screendoor
with dissolve
cl "\"Don’t say anything until you unlock this door.\""
show cal arm talking with dis
ca "\"Relax.\""
play sound ("sfx/keytake.ogg")
show cal smug with dis3
"He jingles the key in front of me."
stop sound
show cal angry arm talking with dis3
ca "\"I’ll let you out after you answer some of my questions.\""
show cal angry arm with dis
cl "\"What questions?\""
show cal angry arm talking with dis
ca "\"Like who among your party would have the strength to cleave the head off of a pack mule with a slicing weapon in one blow?\""
show cal angry arm with dis
"I freeze."
cl "\"You can’t possibly be blaming me for that.\""
"He looks me up and down and then scoffs."
show cal arm talking with dis
ca "\"Certainly not you directly.\""
show cal arm with dis1
show cal arm talking with dis
ca "\"What about that mountain lion?\""
show cal eyes arm with dis1
show cal eyes arm talking with dis
ca "\"He might be big enough.\""
show cal arm with dis
cl "\"Sam?\""
cl "\"I don’t think Sam knows how to use weapons.\""
cl "\"Besides, even if he could, I don’t think he would take something’s head off.\""
show cal angry arm talking with dis
ca "\"Then what would?\""
show cal angry arm with dis1
show cal angry arm talking with dis
ca "\"We’ve found eight carcasses already.\""
show cal angry arm  with dis
cl "\"Eight?\""
show cal angry arm talking with dis
ca "\"Eight!\""
show cal angry arm with dis1
show cal angry arm talking with dis
ca "\"If I don’t stop who’s doing it before long, we won’t have any long distance transportation in or out of the settlement.\""
show cal angry arm with dis1
show cal angry arm talking with dis
ca "\"Without a steady chain of supplies we’ll be behind schedule for all of our exports.\""
show cal arm with dis
cl "\"Why do exports matter if you’re self-sustaining?\""
show cal smug arm talking with dis
ca "\"Because there’s no harm in skimming some of the cream off the top here and there.\""
show cal angry arm with dis1
show cal angry arm talking with dis
ca "\"Imbecile.\""
show cal arm with dis
cl "\"You’re terrible!\""
show cal arm talking with dis
ca "\"No.\""
show cal arm with dis1
show cal arm talking with dis
ca "\"I simply live in the real world.\""
show cal smug arm with dis1
show cal smug arm talking with dis
play music ("music/spiraling.ogg") fadein 2.5
ca "\"Your father mentioned that you don’t, and I see what he means.\""
show cal smug arm with dis
"My father?"
cl "\"What do you mean?\""
show cal smug arm talking with dis
ca "\"He said you’re a little funny.\""
show cal smug arm with dis1
show cal smug arm talking with dis
ca "\"Perhaps not formed quite right.\""
show cal eyes arm with dis1
show cal eyes arm talking with dis
ca "\"Can’t be trusted to make necessary choices for the good of yourself or your family.\""
show cal arm with dis
cl "\"No he didn’t!\""
show cal arm talking with dis
ca "\"It was a bit harsh to me when I first heard it.\""
show cal eyes arm with dis1
show cal eyes arm talking with dis
ca "\"I thought to myself, {i}“certainly all God’s creations are made as he intended.”{/i}\""
show cal arm with dis1
show cal arm talking with dis
ca "\"But it seems as though you’re hellbent on establishing something other than what God made you.\""
show cal angry arm with dis1
show cal angry arm talking with dis
ca "\"What on earth is this Clifford Tibbits nonsense?\""
show cal arm with dis
cl "\"...Who told you about that?\""
"I didn’t share that with him."
show cal arm talking with dis
ca "\"Who hasn’t?\""
show cal smug arm with dis1
show cal smug arm talking with dis
ca "\"Don’t you know that people talk?\""
show cal smug arm with dis1
show cal smug arm talking with dis
ca "\"Do you really think that the conversations you air with other people are sealed into small boxes that only you can open with the right key?\""
show cal smug arm with dis
"He laughs."
"I’m trying not to cry."
show cal smug arm with dis1
show cal smug arm talking with dis
ca "\"Do you really think that becoming a different man is as simple as putting on makeup and wearing your father’s belt?\""
show cal smug arm with dis1
show cal smug arm talking with dis
ca "\"I can read your entire story just by your walk, your gait, your tone, your letters, and the impressions that men of character have sent to me in private.\""
show cal arm with dis1
show cal arm talking with dis
ca "\"People have been talking terribly about you for a long time before I ever met you. I can see now, right before me, that they are exonerated in their honesty.\""
show cal arm with dis
"Who’s been talking?"
"My father?"
"My mentor?"
"My traveling companions?"
"My employer?"
"...is it all of them?"
show cal angry arm talking with dis
ca "\"I see before me an emotional, impulsive, gormless thing, playing as a man, but stuck as something like a child. A... a thing.\""
show cal angry arm with dis1
show cal angry arm talking with dis
ca "\"A thing that’s neither man, nor child, nor anything I would want near God’s children, nor his creations.\""
show cal arm with dis
cl "\"...Why are you being this cruel?\""
"The more I talk, the more I hear my voice struggling to get any noise out."
"My tongue is parched and my throat is sore."
"I’m so dizzy now from the sickness and this unbearable weight that I feel in my body, I can’t see straight."
"He shakes his head."
show cal arm talking with dis
ca "\"At this point, nothing you can say will convince me that you are worthy of this partnership.\""
show cal arm with dis1
show cal arm talking with dis
ca "\"I’m afraid there won’t be any deal between you or me.\""
show cal arm with dis1
show cal arm talking with dis
ca "\"Your reputation wasn’t solid to begin with, Mr. van Houwelinck, and everywhere you go, it seems to crumble just a little bit more beneath your feet.\""
show cal angry arm with dis1
show cal angry arm talking with dis
ca "\"Now you have brought your misfortunes to me and my people.\""
show cal angry arm with dis1
show cal angry arm talking with dis
stop music fadeout 4.0
ca "\"I’ll let you out of here, but I want you gone from this place first thing in the morning.\""
show cal angry with dis3
play sound ("sfx/keydrop.ogg")

"He pulls a key from his pocket."
show cal eyes with dis1
show cal eyes talking with dis
stop sound
ca "\"{cps=20}And I’ll be telling Hendricks to send somebody more reliab—\"{w=0.3}{nw}"
play sound ("sfx/thud7.ogg")
hide cal with vpunch
"I hear a giant thud, like a tree trunk falling."
stop sound
play background ("sfx/heartbeat.ogg")
"Caldwell screams."
ca "\"Get away!\""
ca "\"I said get away!\""
play music ("sfx/death.ogg")
play sound ("sfx/gore.ogg")
"I can’t see what’s going on, but I hear a tearing noise."
stop sound
scene settlementshedback
show deepmine:
    alpha 0.25
with dis3
play music2 ("sfx/flies.ogg") fadein 3.5
"For some reason..."
"I start to hear the bees again."
"Or at least something that sounds similar to the bees."
"Caldwell screams more."
"I can see through a slat in the bars that he’s on the ground."
"His wing is bent the wrong way, and his breathing is raspy."
ca "\"God help me!\""
"His voice is different."
"It sounds wrong, like he’s inhaling while he speaks."
scene bees
show screendoor
with dis3
"I reposition myself to look outside."
"I don’t see anything."
play sound ("sfx/breathleft.ogg")
"But I hear breathing."
queue sound ("sfx/breathright.ogg")
"Soft, slow breathing."
"I want to back away from the door, but I don’t want to make any noise."
stop sound
"I know whatever out there is strong."
"It could rip the door open."
"It might even already know that I’m here, and it’s just waiting to rip off the door."
"I don’t know how long I stand there, listening to Caldwell cry out in pain, or listening for breathing sounds that I can’t tell if I’m hearing or imagining anymore."
show deepmine:
    alpha 0.45
show bees at night
show screendoor at night
with dis4
"But it gets darker."
"And nobody knows that I’m here but the priest, and he can’t get up."
#sfx
stop music2 fadeout 3.0
"Just as I start to cry, I hear a whistling sound."
"In the mist I see somebody big walk this way."
"They have horns. The light of the moon reflects off their glasses."
"My heart swells a little when I see Doc Avery."
"I call out to him."
"I’m saved."
"But I can’t make a sound."
"My voice is shot."
"Airy, breathy rasping sounds are all that I can make."
av "\"Huh?\""
av "\"What do we have here?\""
ca "\"Help me!\""
ca "\"You have to get me inside.\""
av "\"You look like you’re in real bad shape, Reverend.\""

av "\"Broken arm.\""

av "\"Broken rib.\""

av "\"Half-collapsed lung by the sound of you, I wager.\""

av "\"I’d hate to move ya.\""
av "\"Could cause any internal bleedin’ you might have to get worse.\""
"The reverend shakes his head, terrified."
ca "\"Do... car...\""
ca "\"..on’t ..are!\""
av "\"I’m sorry Reverend, but I can’t really tell what you’re saying.\""
"I see the heron look in my direction, like he’s asking me for help."
"I try to talk again but it’s not working."

ca "\"In..si..!\""
"The doc hunches on his legs and watches him from a squatting position."
av "\"You know, if you want help, all you have to do is ask, Reverend.\""

ca "\"Pu.. me...insi...!\""
av "\"That doesn’t sound much like Albion to me.\""
"He’s thrashing on the ground now."
"His breathing sounds a whole lot worse."

av "\"I guess I can’t really help those who don’t know how to ask.\""
"He stands up straight, watching the heron writhe."
av "\"But do you want to know what the worst thing about all of this is, Reverend?\""
"The heron is spasming in the wrong way now."
av "\"With enough time they’ll just send another one of you who looks the same and acts the same.\""
av "\"But I’m comfortable, now, knowing now that you’re the one who put the soap in her mouth.\""
"He wipes his glasses."
av "\"Have a good night, Reverend.\""
"He readjusts his backpack."
av "\"I know I will.\""
"And he starts to whistle."
"Then he starts to walk away."
"I panic again."
"I cry out to him, trying to force a noise."
"But there’s nothing."
play sound ("sfx/shovel2.ogg")
"I take the trowel and bang on the bars, hoping he hears something."
stop sound
"My heart leaps as his ears pick up."
"But he looks left, and then right."
play sound ("sfx/leafcrunch.ogg")
"And he starts to run."
"He’s running because I scared him."
stop sound
"He’s so far away now."
"I start to think again that I really am going to die here."

"And then I wonder who I’m going to die as."
"Will people remember who I wanted to be?"
"Will any of them see me as I saw myself?"
"Probably not."
stop music fadeout 4.0
scene bg black with dis4
"I start to wonder about what my tombstone will look like."
"It reads just Cornelis."
"And it’s buried nowhere near the rest of my family."
"I want to think that coming here was a mistake."
"But staying home would have been a mistake too."
"The mistake is me."
stop background fadeout 1.0
pause 3.0
m "\"Professor Tibbits?\""
play background ("sfx/crickets.ogg") fadein 4.0
"I hear Sam."
"I must be hallucinating."
scene bees at night
show sam surprised -talking at center,night
show screendoor at night
show deepmine:
    alpha 0.55
with slow_dissolve
show sam surprised talking with dis
m "\"Why’re you beating that door with a shovel?\""
show sam surprised -talking with dis1
show sam surprised talking with dis
m "\"We were looking for you all day.\""
show sam surprised -talking with dis
mu "\"Sam, there’s stains on the ground over here.\""
show sam annoyed talking with dis
m "\"I don’t care about that right now.\""
show sam surprised -talking with dis1
show sam surprised talking with dis
m "\"We found Professor Tibbits!\""
show sam surprised -talking with dis1
show sam surprised talking with dis
m "\"...He sort of smells though.\""
show sam shocked -talking with dis3
m "\"What are you doing in there!?\""
"I try to speak again, but it hurts."
cl "\"It was locked.\""
show sam surprised talking with dis3
m "\"Why do you sound like that?\""
show sam surprised -talking with dis1
show mur fear d at halfright,night behind sam with dis3:
    zoom 0.8
    yalign 0.25
mu "\"Sam, there’s a scrap of cloth over here that looks like a clergyman’s robe.\""
mu "\"I think it must have belonged to that priest.\""
show sam surprised talking with dis
m "\"You sure?\""
show sam surprised -talking with dis
show mur concerned d with dis
mu "\"It has to be.\""
show mur fear d with dis
mu "\"Do you think something might have happened to him?\""
mu "\"Like with the other animals the guards keep finding?\""
show mur concerned d with dis
show sam eyes talking with dis
m "\"He was old, right?\""
show sam neutral -talking with dis
show mur sideeye with dis
mu "\"But something might’ve happened to him if this is on the ground.\""
show mur concerned d with dis
show sam annoyed talking with dis
m "\"That’s too bad.\""
show sam annoyed -talking with dis1
show sam annoyed talking with dis
m "\"I didn’t know ‘im.\""
play sound ("sfx/shovel1.ogg")
show mur shock
show sam shocked -talking
with hpunch
"I start beating the door with the shovel to get his attention."
stop sound
m "\"Whoa there partner.\""
show sam surprised talking
show mur fear d
with dis3
m "\"Calm on down and we can figure a way to get you out.\""
show sam surprised -talking with dis
"I try to shout KEY."
show sam surprised talking with dis
show mur concerned d with dis
m "\"I think his lips are saying {i}key{/i}.\""
show sam surprised -talking with dis
show mur fear d with dis
play sound ("sfx/keytake.ogg")
mu "\"There’s keys on a ring over here in the dirt.\""
play sound ("sfx/shovel2.ogg")
show mur concerned d with dis
"I beat the door again, desperately."
stop sound
hide mur with dis3
show mur fear d at center,night behind screendoor with dis3
show sam surprised -talking at centerleft,night behind mur with dis3
"Murdoch steps in close and winces."
mu "\"Oh god, he looks dehydrated.\""
play sound ("sfx/keyopen.ogg")
show mur concerned d with dis
"He fumbles with the keys and within moments I hear the heavy latch lift."
play sound ("sfx/thud.ogg")
show black with dis1
hide screendoor
show sam surprised -talking at center
show mur concerned d at right
hide black
with dis3
"I stumble out and Sam catches me."
stop sound
show mur shock with dis
mu "\"Something’s wrong with him.\""
show mur fear d with dis
mu "\"We need to get him back to the hotel as soon as possible.\""
scene bg black with dis4
"Sam flips me onto his shoulder, but something is off."
"He’s holding onto two sticks, and he’s only using one of his legs."
"Murdoch is offering him his arm as a support, and they’re walking like contestants in a race where one is tied to the other’s ankle."
m "\"Easy enough. He’s lighter than his luggage.\""
"I bury my face in his chest and feel myself floating."
"I hear brushes in the distance."
"The wind."
"The chirp of the crickets."
stop background fadeout 3.0
pause 1.0
"And then it all gets muffled again."
pause 2.5
"I feel somebody pouring something down my throat."
"It hurts at first, but once I start drinking, I’m desperate for more."
m "\"Slow down or else you’ll chip the mug.\""
scene bg innroom
show sam surprised -talking at left,inn:
    xzoom-1
show mur concerned d at right,inn
with dis4
"I sit up in bed."
show sam neutral -talking with dis
play sound ("sfx/wsplash.ogg")
"A damp rag falls off my head and some of the water in the mug spills on my chest."
stop sound
if SMC_Points == 1:
    play music ("music/morningglory.ogg") fadein 3.0
else:
    play music ("music/quiet.ogg") fadein 1.0


if SMC_Points == 1:
    show sam annoyed with dis
    "Murdoch is stirring something into a large barrel and Sam gives me a withering look, holding the mug of water that’s just lost some of its contents."
    show sam neutral -talking with dis
    cl "\"...What’s going on?\""
    "I’m thankful that my voice is back."
    show mur talking with dis
    mu "\"We’re drawing you a bath.\""
    show mur sideeye d with dis
    show sam annoyed talking with dis
    m "\"Because you stink.\""
    show sam neutral -talking with dis
    "I want to say there’s no time to bathe."
    show mur sideeye with dis
    "Because Caldwell’s dead, and there’s no telling who else could be next."
    show mur eyes with dis
    "I try to protest as Sam lifts me under my arms, shakes his head, and whistles as Murdoch forms suds with a rag and a piece of the nice soap with oats in it from his family’s store."
    cl "\"Is this necessary?\""
    show mur sideeye with dis
    show sam eyes talking with dis
    m "\"If we don’t want the whole room to smell like weasel.\""
    show sam neutral -talking with dis1
    show sam talking with dis
    m "\"Ain’t any mint perfume gonna cover that. We need purifying soap.\""
    show sam surprised -talking with dis
    show mur concerned d with dis
    cl "\"Unhand me!\""
    show mur fear d with dis
    mu "\"You could have died from heat exposure today, Cliff.\""
    show mur concerned d with dis
    mu "\"Just let us do something nice for you.\""
    show sam eyes with dis
    show mur eyes talking with dis
    play sound ("sfx/splash2.ogg")
    "They take turns scrubbing my arms, aggressively."
    "Then my chest."
    stop sound
    "Then my neck."
    show mur eyes with dis
    show sam smile with dis
    cl "\"This can hardly be considered nice!\""
    show sam neutral -talking with dis
    "Murdoch’s paws are all over my face, rubbing mint-scented oil into my whiskers and cheeks, smooshing them with abandon."
    show black with dis
    play sound ("sfx/splash3.ogg")
    "Sam pours the bucket over my head without warning,{nw}"
    hide black with dis3
    extend " and I’m left in place, breathing."
    show mur smile with dis
    cl "\"Are you finished?\""
    stop sound
    "They both nod."
    cl "\"Okay.\""
    show mur concerned d with dis

cl "\"Please listen carefully.\""
cl "\"I think that the animal who hunted us at the camp in the woods is still stalking us.\""
show sam sad talking with dis
m "\"Oh, I know.\""
show sam sad -talking with dis1
show sam sad talking with dis
m "\"Got my leg.\""
show sam surprised -talking with dis
cl "\"...Just your leg?\""
show sam annoyed talking with dis
m "\"You sound disappointed.\""
show sam neutral -talking with dis
cl "\"More like impressed, really.\""
cl "\"It um...\""
"I struggle with whether or not I want to tell them or not."
"...But I struggle more to hold this in."
show sam surprised -talking with dis
show mur fear d with dis
cl "\"It got the reverend.\""
mu "\"Oh God.\""
show mur concerned d with dis
mu "\"He’s really dead?\""
show sam surprised -talking with dis
"I didn’t see him die explicitly."
"But somehow, I know."
cl "\"He’s really dead.\""
show mur fear d with dis
mu "\"It didn’t try to attack you?\""
show sam neutral -talking with dis
show mur concerned d with dis
cl "\"Somehow it didn’t even try to break into the shack.\""
cl "\"It might not have noticed me.\""
show sam talking with dis
m "\"Hard not to.\""
show sam neutral -talking with dis1
show sam talking with dis
show mur sideeye with dis
m "\"You really reeked.\""
show sam neutral -talking with dis
"My cheeks start to feel hot from embarrassment."
cl "\"Can you stop talking about that?\""


if SMC_Points == 1:
    play sound ("sfx/splash4.ogg")
    "I step out of the tub and hold my arms out to dry."
    show sam eyes with dis
    show mur eyes with dis
    "Sam and Murdoch start to pat me down."
    stop sound
    "I growl to get them to step back."
    show sam laugh with dis3
    show mur happy with dis3
    "But they just start to laugh."
    show sam happy talking with dis3
    show mur smile with dis3
    m "\"That’s what it sounds like when a stoat growls?\""
    show sam smile with dis
    show mur eyes with dis
    mu "\"Sam. Be nice.\""
    "But I can hear that he’s on the verge of cracking up too."
    show sam happy talking with dis
    m "\"I thought he had found a helium tank to suck on.\""
    show sam happy -talking with dis
    "I want to scream at them."
    show mur smile with dis
    show sam smile with dis
    cl "\"Let me dress myself!\""
    "They both step back."
    show sam eyessmile with dis
    show mur eyes with dis
    "I’m irritated that they bow."

scene bg black with dissolve
scene innroom with dissolve
play sound ("sfx/softknock.ogg")
"By the time I manage to slip into my pants, we hear a knock on the door."
stop sound
jeb "\"Hello?\""
cl "\"Just a moment!\""
"I slip into my shirt as quickly as possible."
show mur talking at center,inn with dis3
mu "\"I’m gonna let him in now.\""
show mur sideeye d with dis
cl "\"My tie isn’t even on!\""
show mur sideeye with dis3
play sound ("sfx/dooropen.ogg")
"Impatiently, the fox pulls the door open."
show jeb at left,inn with dis:
    xzoom-1
"Jeb shuffles in, then stops."
stop sound
show jeb shocked with dis
"He looks from the blisters on my hand to the wrap on Sam’s foot."
show jeb angry talking with dis
jeb "\"How are y’all gettin’ more injured in the settlement than on the journey?\""
show jeb doubt with dis
cl "\"Well...\""
show jeb doubt talking with dis
jeb "\"That was a rhetorical question.\""
show jeb with dis1
show jeb talking with dis
stop music fadeout 6.0
jeb "\"Anyways, I just wanted to bring the news as fast as I heard it.\""
show jeb with dis1
show jeb talking with dis
show mur concerned d with dis
jeb "\"Some of the natives are saying they got the beast that was hunting us on road.\""
show jeb with dis
show mur fear d with dis
mu "\"The thing that was following us?\""
show mur concerned d with dis
show jeb doubt talking with dis
jeb "\"Yep.\""
show jeb with dis1
show jeb talking with dis
jeb "\"Turns out it was just a wild hog.\""
show jeb with dis1
show jeb talking with dis
jeb "\"A big, old, territorial hog.\""
show jeb with dis
cl "\"And how do you know that?\""
show jeb doubt with dis
"Jeb sends me a look."
show jeb doubt talking with dis
jeb "\"’Cause they found it goring the reverend on the road last night the same way it was getting all the other animals.\""
show jeb doubt with dis
"As soon as he says that I feel the blood drain from my face."
show jeb shocked with dis
cl "\"...I want to see it.\""
show jeb shocked talking with dis
jeb "\"You sure about that?\""
show jeb shocked with dis1
show jeb shocked talking with dis
jeb "\"You might be a bit sensitive for carnage like that done to a person.\""
show jeb shocked with dis
cl "\"No, I’m quite sure.\""
show jeb with dis
cl "\"Show me.\""
"Murdoch grabs his camera."
show mur eyes talking with dis
mu "\"I want to be sure too.\""
show mur concerned d with dis
show sam neutral -talking at right,inn behind mur with dis3
"The only one who isn’t moving much is Sam."
show sam talking with dis
m "\"I’ll catch up with y’all. I just want to manage some things.\""
show sam eyes -talking with dis
show mur sideeye with dis
mu "\"Don’t take too long.\""
show sam neutral -talking with dis
show jeb talking with dis
show mur concerned d with dis
jeb "\"We won’t be going far down the road.\""
show jeb with dis1
hide jeb
hide mur
with dis3
"I wait until the other two leave the room and then walk up to Sam."
show sam surprised -talking with dis
"I bend down to sneak him a kiss."
"He looks surprised."
show sam surprised talking with dis
m "\"What was that for?\""
show sam surprised -talking with dis
cl "\"It’s just my way of saying thank you.\""
"More than ever."
show sam happy blush with dis
"He scratches the back of his head bashfully and shoos me away with his paw."
show sam -happy -blush talking with dis
m "\"Go on and get.\""
show sam neutral -talking with dis1
show sam talking with dis
m "\"Like I said, I just need some time!\""
show sam neutral -talking with dis1
show sam talking with dis
m "\"It won’t be long.\""
show sam smile with dis
"I nod, blushing, and open up the door, not much feeling the blisters on my hands right now."

scene bg black with slow_dissolve
play music ("music/contemplation.ogg") fadein 2.0
scene innroom with slow_dissolve
m "\"There’s no goddamn way that thing was a wild hog.\""
m "\"Hogs are something you can see.\""
m "\"They don’t go invisible all of a sudden, or look like monsters in photographs.\""
m "\"Whatever is out there still has to be out there.\""
if HaveMap == True:
    "I want to check again to see how far Camp Rosa is."
    "I search through my backpack and pull out the map, unwinding it."
    scene hoganmap3 with dis3
    "My confidence plummets again."
    "That journey looks almost as long as the one from Echo."
    "But if it’s farther away, maybe that means it’s safer."
    scene innroom with dis3
    "I roll it up again and put it back."

scene bg black with dissolve
play background ("sfx/birds.ogg") fadein 3.0
scene reservation with dissolve
"Once I’m outside it’s not very hard to see where I need to go."
"I follow the group of people arranged in a large circle in the middle of the road."
"What’s ahead is one of the strangest sights I’ve seen on my journey yet."
show yis at center with dis3
show tse at left with dis3:
    xzoom-1
"The bear, Yiska, is sitting on top of what I first think is an old sequoia tree stump, but the closer I look, the bark becomes hair and skin."
"He’s chatting with others in the Meseta language, although it sounds like he has a slight lisp he didn't have before, as if he had a tongue injury."
"He’s holding onto a spear in his left hand that has punctured beneath the jaw of the great pig, and Tsela is sitting next to him, comfortable."
"There is also a table cloth, soaked in red, over a patch which I assume must be the reverend."
hide yis
hide tse
with dis3
"I’m starting to wonder whether or not what we ran into in the forest really was just a big old pissed off hog."
"As Cliff suspected, maybe we were hallucinating due to the natural gasses."
"As I think about this, I notice something strange."
"I don’t see any guards around."
"Just our travel group, and Meseta townsfolk."
play music2 ("sfx/car engine loop.ogg") fadein 7.0
"But before I can react to this, something else sneaks up on me."
"It’s the sound of a car."
play sound ("sfx/car engine stop.ogg") fadein 0.5
stop music2 fadeout 0.5
"And it’s pulling up behind me."
"As I turn around to look, it stops, and two people come out of the car."
show jam neutral at center with dis3
stop sound
"The first I can recognize immediately."
"It’s James Hendricks."
"But the other I can’t make out."
"Until I hear him."

wiunk "\"Now just what the hell is going on, exactly?\""
show wil surprised at right with dis3
"Will walks up to the group, but then stops in his tracks when he sees me."
show wil talking with dis
wi "\"And just what the hell are you doing here?!\""
show wil with dis1



scene bg black with slow_dissolve
"To be continued..."
window hide
scene credits with slow_dissolve
pause
scene credits2 with slow_dissolve
pause
scene black with slow_dissolve
