label cliffroute2:
stop music fadeout 5.0
stop background fadeout 5.0
scene black with slow_dissolve
$ renpy.music.set_volume(1.0, delay=1.5, channel='background')
window hide
scene clich2 with slow_dissolve
pause
scene black with slow_dissolve
play music "sfx/nightdesert.ogg" fadein 10.0
window show
scene echodesertnight with slow_dissolve
window show
"In the cover of darkness, Jebediah leads us through the empty streets all the way to the outskirts of town, where he's prepared a small wooden wagon."
"It ain't a pretty one, but it looks well-maintained."
"The paint on the wood's cracked, but the wheels are in good shape, and the sailcloth canopy looks like it will offer decent coverage."
"I could do without the smell."
"That's coming from the pair of old donkeys standing in front."
"They seem well taken care of, at least. Though they don’t exactly look like they’re gonna be much help trekkin’ across the desert."
"I wonder if we're gonna be okay."
"Judging by the look on Murdoch's face, he feels much the same."
"I help with the heavy lifting."
"Most of Cliff’s gear goes on the wagon. Murdoch’s brought a few crates of supplies himself."
"More packs of canned food than I can count, and booze..."
"Is this all from the store?"
m "\"We really gonna need all this?\""
show cli at center,nightgreen with dissolve
show cli talking with dis
cl "\"Fortune favors the prepared, my friend. As much faith as I have in Jebediah and our group, disaster could strike at any moment.\""
show cli happy with dis
cl "\"It’s a good thing you came along, Samuel. Without a strongman such as yourself, or Murdoch on camera duty, I’d have had to delay my expedition even further.\""
show cli sad with dis
cl "\"Perhaps I wouldn’t have been able to go at all.\""
cl "\"My sponsor would have been so disappointed.\""
show cli with dis
m "\"That’s the first time I’ve heard about a sponsor.\""
"Figured he was paying for this out of pocket, rich as he probably is."
show cli talking with dis
cl "\"True. I suppose I haven’t told you yet, Samuel.\""
show cli happy with dis
cl "\"My expenses have been paid for graciously by my donor.\""
show cli talking with dis
cl "\"Now, I will be the first to admit that I have had a rather fortunate upbringing.\""
show cli with dis1
show cli talking with dis
cl "\"I do not want for money, and I’ve been able to see more of the world than I could ever have dreamed once I left for university.\""
show cli with dis1
show cli talking with dis
cl "\"But expeditions like these don’t come cheap! Without my sponsor, why, I wouldn’t be here right now.\""
m "\"Who is your sponsor?\""
show cli down with dis
cl "\"He...\""
"Cliff clears his throat with a soft ‘hem’."
show cli talking with dis
cl "\"He does not wish to be named unless I am speaking for him in an official capacity for diplomatic endeavors.\""
show cli with dis
"That ain't suspicious at all."
show cli happy with dis
cl "\"It'll be money well spent. My thesis will change how we view native populations across the world.\""
"Not sure spending money on whores counts as money well spent, but I ain't complaining."
"Especially when this is gettin' me out of Echo."
m "\"You really think so?\""
show cli talking with dis
cl "\"Researching the Meseta culture has been a dream of mine since I was but a first-year.\""
show cli with dis1
show cli talking with dis
cl "\"I've devoured every book, every newspaper clipping I could ever hope to find, and it's all led me right here.\""
show cli with dis
"Murdoch clears his throat."
show mur talking at right,nightgreen with dissolve
mu "\"Cliff isn't the only heavy reader in our midst.\""
mu "\"Right, Jebediah?\""
show mur at right with dis
"The horse, tending to one of the donkeys, grunts."
"Seeing them next to each other is kind of uncanny, and I struggle to keep my eyes on Cliff."
show cli doubt with dis
cl "\"The coming days have to be perfect. I cannot allow anything to go wrong.\""
cl "\"If I can't learn all there is to know about the Meseta, I might as well go home.\""
show mur talking with dis
mu "\"Those are some lofty expectations.\""
show mur with dis
show cli eyes talking with dis
cl "\"Not to say it won't be enjoyable, of course.\""
show cli eyes with dis
m "\"You bring a guitar or somethin'?\""
show mur talking with dis
mu "\"I did.\""
show mur with dis
show cli happy with dis
cl "\"And he has quite a good singing voice.\""
show mur mischief with dis
mu "\"Stop flattering me, Mr. Tibbits.\""
show cli talking with dis
cl "\"You’re too humble. It's the truth.\""
show mur with dis
show cli with dis
"This fox is anything but humble."
show cli blush eyes right with dis
cl "\"I’m looking forward to hearing you sing as well, Samuel.\""
"Sing?"
"Dancing was more than enough for me."
m "\"I don’t exactly have the voice of an angel.\""
show cli blush eyes closed talking with dis
cl "\"Ah, but you look like one.\""
if MT_Points > 0:
    show mur happy with dis
    "Murdoch laughs."
else:
    show mur sideeye with dis
"I know it shouldn't, but Cliff saying that makes my face all warm."
"Maybe because of how innocent it sounds coming out of his mouth."
"Maybe because I actually enjoyed being around him last night."
show mur with dis
"It's a good thing Jebediah isn't watching."
"I still don't know what to think of that horse."
show cli talking with dis
cl "\"Besides, singing's about enjoying yourself.\""
cl "\"It's not all about performing well.\""
cl "\"At least, that's what they told me every week at choir practice.\""
show cli blush eyes closed with dis
"He chuckles."
show cli blush eyes closed talking with dis
cl "\"I suppose I wasn't very good either.\""
show jeb at left,nightgreen with dissolve
"Jebediah steps back from the wagon, turning to Cliff."
show jeb talking with dis
jeb "\"Everything's packed. We should be ready to go.\""
show jeb with dis
show cli happy with dis
cl "\"Splendid!\""
hide all
stop music fadeout 4.0
scene bg black with slow_dissolve
scene bg desertmorning with slow_dissolve
play music "music/thegamesimissed.ogg" fadein 8.0
"We catch the first rays of sunlight just as we pass the town gates."
"I don't need to see much to know there’s a barren wasteland stretching out for miles in front of us."
"Still, makes me grin just looking at it. After all this time, I'm finally leaving Echo."
"Hoping we might see some of the woods. Ain't been in a forest for God knows how long."
"The clacking of hooves makes quite a racket this early in the morning."
"Jebediah's in his wagon, Cliff walking by his side."
"He's a fast walker. Murdoch and I are even lagging behind."
show mur smile at center,sunset with dissolve
show mur talking with dis
mu "\"Isn't that the prettiest sight you’ve ever seen?\""
show mur smile with dis
if MT_Points < 1:
    "At least he's talkin' again. I was starting to get a little uncomfortable."
m "\"You ain’t never seen a sunrise before?\""
show mur mischief with dis
$ renpy.music.set_volume(0.6, delay=7.0, channel='music')
mu "\"Come on Samuel, where’s your sense of adventure?\""
"Must've lost it with the blow to the back of my head."
"But I can't say that."
$ renpy.music.set_volume(0.05, delay=12.0, channel='music')
"Or talk about what Hendricks said earlier."
play background "sfx/whispers.ogg" fadein 10.0
"A pang of guilt hits me when I think again about what might happen to Nik if James can't stay calm about his whore leaving town."
"Is he gonna lose his job? Get killed?"
"It’d all be my fuckin’ fault."
"Add that to the list of terrible things I've done."
stop background fadeout 10.0
"I’m gonna have to live with it, somehow."
"For all I know, Hendricks was just making empty threats."
$ renpy.music.set_volume(0.2, delay=4.0, channel='music')
"Maybe talking will clear my mind."
m "\"You leave town often?\""
show mur talking with dis
mu "\"For errands and the occasional spot of nature photography, yes.\""
show mur eyes with dis
mu "\"But not for too long. I spend enough time trying to keep up with things at home as it is.\""
$ renpy.music.set_volume(1.0, delay=15.0, channel='music')
mu "\"How about yourself? It strikes me that I never did learn that much about you.\""
show mur mischief with dis
mu "\"You're not from around Echo, are you? Originally, I mean.\""
mu "\"I can tell by your accent.\""
"Of course he fucking knows."
if MT_Points < 1:
    "This fox knows exactly how to get under my skin."
    "Feels like the rays of sunlight are dying the desert blood red as I look in front of me again."
else:
    "I'm not surprised at this point."
    "I have to shield my eyes from the sun once I look forward again."
    "It’s coloring the desert a glittering orange, and I have to agree with Murdoch."
    "It does look beautiful."
"Cliff’s struggling with a heavy map that’s about as big as he is."
"He’s looking back at us when a gust of desert wind blows it against his face with a loud smack, knocking his glasses askew."
show mur happy with dis
"He squeaks in surprise."
"Jebediah, maybe in an act of mercy, takes the map from him without question, taking a peek at it himself."
show cli talking at right,sunset with dis
show mur with dis
cl "\"I too am rather curious.\""
show cli with dis
"The stoat slows down to join us, bottlebrush tail swaying side to side, and fixes his glasses."
"Seems I’ve got an audience."
m "\"I ain’t from ‘round here, no. Not even from the state.\""
show cli happy with dis
cl "\"South-eastern side of the country, perhaps?\""
"He managed to pick that up?"
m "\"The Magnolia State.\""
show mur smile with dis
show cli talking with dis
cl "\"I thought so.\""
show cli with dis
mu "\"You did?\""
show cli happy with dis
cl "\"His way of speaking clued me in.\""
show cli talking eyes with dis
cl "\"Linguistics might not necessarily be my area of expertise, but I like to pay attention.\""
show cli talking with dis
cl "\"After all, languages and how they’re spoken play a large role not only in communication, but in social and cultural identity as well.\""
cl "\"They can tell you a lot about a person's upbringing.\""
show cli with dis
m "\"You can tell all that just by listening to them?\""
"That's a scary thought."
show cli happy with dis
cl "\"Yes!\""
show cli talking with dis
cl "\"It’s rather interesting. I’d love to go over it in more detail at some point.\""
show mur talking with dis
mu "\"You seem to have an accent all your own, Cliff.\""
show mur smile with dis
show cli eyes talking with dis
cl "\"I may be Batavian, but I've lived abroad a few years now.\""
show cli talking with dis
cl "\"I haven't even gone back home to visit in half a decade.\""
show cli with dis
m "\"Do you still speak Batavian?\""
show cli talking with dis
cl "\"I haven't spoken it in a while.\""
show cli eyes talking with dis
cl "\"After I left for university, I never felt the need. All my courses were in Albion, and most of my students spoke Albion as well.\""
show cli eyes with dis
stop music fadeout 2.0
mu "\"Well, I'd love to hear some Batavian. What about you, Sam? Jebediah?\""
"The horse grumbles, canting his head as he looks at the map."
show cli blush eyes left with dis1
show cli blush eyes right with dis
play music "music/popgoestheweasel.ogg"
"Cliff starts stammering, eyes darting left and right."
m "\"Go ahead.\""
"At least I'm not the center of attention anymore."
show cli blush eyes closed talking with dis
cl "\"You're putting me on the spot.\""
show cli blush eyes closed with dis
"He's stiff as a board."
show mur mischief with dis
mu "\"I'm not asking you to recite the Declaration of Independence. Just a simple good morning will do!\""
show cli blush eyes right with dis
cl "\"A-alright...\""
show cli blush eyes closed talking with dis
cl "\"Goedemorgen.\""
"He mumbles it under his breath."
show mur talking with dis
mu "\"I didn't quite catch that.\""
show mur with dis
"Cliff knits his brows."
show cli angry with dis
cl "\"Goedemorgen!\""
show cli blush eyes closed with dis
"I'm not sure I've ever heard some of the sounds that just left his muzzle."
show mur fear d with dis
mu "\"Goo... Kchoot...\""
"He stands there for a moment, smacking his lips as he tries to repeat it."
show mur talking with dis
mu "\"I have officially given up on learning Batavian.\""
show cli happy with dis
"Cliff suppresses a laugh."
cl "\"Quite a shame. You were on the right track.\""
show mur mischief with dis
mu "\"I'm a salesman, not some cunning linguist.\""
show cli eyes talking with dis
cl "\"You seem cunning enough to me.\""
stop music fadeout 2.0
show cli talking with dis
cl "\"Ah, but we were talking about Sam.\""
"Shit."
show mur talking with dis
play music "music/thegamesimissed.ogg" fadein 10.0
mu "\"That we were. Language lessons will have to wait.\""
show mur with dis
show cli talking with dis
cl "\"There's one thing in particular I'm curious about.\""
show cli with dis
m "\"Such as?\""
show cli talking with dis
cl "\"How'd you end up working in a brothel of all places?\""
show mur shock with dis
show cli eyes talking with dis
cl "\"You're not exactly... you know...\""
show mur concerned d with dis
mu "\"Cliff...\""
"Murdoch leans in, voice lowering to a whisper."
show mur sideeye with dis
mu "\"Jebediah is right there.\""
show cli shocked with dis
"Cliff's eyes shoot wide open. Doesn't seem like Jeb notices, though."
show cli blush eyes right with dis
show mur happy with dis
cl "\"Well I'm sure Jeb has no problem with that sort of thing?\""
jeb "\"What sort of thing?\""
cl "\"Ah, don't concern yourself with our prattle.\""
cl "\"I was only curious.\""
cl "\"It's a little surprising, is all.\""
"Heard that before. Just looking at me, ya wouldn't expect me to be the whore type."
show cli happy with dis
cl "\"A short summary will do.\""
show mur smile with dis
m "\"Not much to say, really. I came here for the gold, same as everybody else.\""
show cli doubt with dis
m "\"Wasn't too good at mine work, though, so that dream ended right quick.\""
"Cliff nods urgently, little ears twitching."
show mur talking with dis
mu "\"And then what happened?\""
show mur with dis
"I catch Jebediah turning to us, map in hand. He's probably wondering why we've slowed down to a crawl."
"All eyes are on me."
m "\"Dora found me while I was doin' some odd jobs. Said she could help if I was willing to put in some work.\""
"I grind my teeth, my cheeks burning."
"Just this day and then it'll be over."
show mur mischief with dis
mu "\"I was expecting something a little more exciting.\""
show mur with dis
"You don't know the half of it."
show cli happy with dis
cl "\"I should've guessed you worked in the mines in the past.\""
cl "\"Your build says it all.\""
"I sheepishly shrug my shoulders."
m "\"Just for a few weeks.\""
"And I'm not sure I'd ever go back, even if I got offered all the gold in the world."
show cli talking with dis
cl "\"Still!\""
show mur mischief with dis
mu "\"This fellow's already picturing you in a miner's uniform, Sam.\""
show cli doubt with dis
cl "\"I most certainly am not!\""
"He definitely is."
"Jeb leans forward in his wagon, looking over at us."
show jeb at left,sunset behind mur with dissolve
show jeb talking with dis
jeb "\"Hate to break up this conversation, but we're gonna have to get a move on.\""
show jeb with dis
"I think that's one of the first full sentences I've heard him say on this expedition so far."
show jeb talking with dis
jeb "\"We want to be somewhere shady by noon, and we ain't gonna get anywhere at this rate.\""
show jeb with dis1
show jeb talking with dis
jeb "\"You don't want to end up dying of heat stroke before we've reached our first rest stop.\""
show jeb with dis1
show jeb talking with dis
jeb "\"And remember, your flask ain't for leisurely sippin'. Ration your water.\""
show jeb with dis1
show jeb talking with dis
jeb "\"We ain't gonna find clear drinking water for quite a while.\""
show jeb with dis1
show mur fear d with dis
"Murdoch, about to drink, quickly stows away his flask again."
hide all
scene bg deserttrail with slow_dissolve
"And so we keep walking."
show mur smile at center with dis
show cli at right with dis
"The sun's up now, and I can finally see my paws in front of my eyes."
"It ain't so cold anymore, either."
"Every now and then, Murdoch asks Cliff how to say a certain word in Batavian."
"Cliff's answers are starting to sound stranger every time."
show mur talking with dis
mu "\"Nature photography?\""
show mur smile with dis
show cli eyes talking with dis
cl "\"Natuurfotografie.\""
show cli eyes with dis
show mur eyes talking with dis
mu "\"You just keep surprising me.\""
show mur smile with dis
cl "\"Are you making fun of me, Mr. Byrnes?\""
show mur mischief with dis
mu "\"I assure you, I have nothing but respect for you and your language.\""
show mur talking with dis
mu "\"What about you, Jebediah?\""
"Another grunt from the horse."
"I think Murdoch likes getting a rise out of him."
"Then again, I think he likes getting a rise out of everyone."
show mur mischief with dis
mu "\"I think he's very impressed as well.\""
show mur talking with dis
mu "\"Okay, so what about this one...\""
hide cli with dis
hide mur with dis
stop music fadeout 7.5
play sound "sfx/rattle.ogg"
"Something makes the cart rattle."
"The donkeys bray as they pick up speed, dragging the cart far away from us."
"Murdoch barks in surprise and we both pick up our pace, Cliff sprinting ahead."
play sound "sfx/scrape.ogg"
"A nasty scraping sound goes off as the cart comes to a halt, the donkeys now kicking up dust."
"As we catch up, I can see Jeb holding the reins of his donkeys."
"Their eyes are turned up, and they’re showing their gums as they gibber and stomp."
play music "music/contemplation.ogg" fadeout 1.0 fadein 9.0
show jeb angry talking at center with dis
jeb "\"Don’t come no closer.\""
show jeb at center with dis
"He makes a shushing noise, whistling the wind between his teeth."
show jeb sad talking at center with dis
jeb "\"They’re scared.\""
show jeb sad with dis
"He waits until they stop kicking up dirt, then lets go of their reins, patting each on the head."
show jeb with dis
m "\"Scared of what?\""
show jeb talking with dis
jeb "\"Dunno. They usually ain’t like this.\""
jeb "\"Acting like a predator’s nearby.\""
show jeb with dis
show cli shocked at right with dis
cl "\"A predator?\""
show jeb talking with dis
jeb "\"Likely aught but the wind. Could’ve picked up the scent of a carcass baking under the sun.\""
show cli sad with dis
jeb "\"These beasties need a moment. We have to stay put for a while.\""
show jeb with dis
m "\"Got an idea for how long?\""
show jeb talking with dis
jeb "\"Shouldn’t be more than an hour at worst.\""
hide jeb
hide cli
with dissolve
"I see Murdoch hop into the wagon, his white-tipped tail poking out as he rummages through some things."
"When he reemerges, he pulls out a fairly thick wooden box and has a folder under his arm."
mu "\"Not a problem.\""
mu "\"Let’s go make some calotypes, Cliff.\""
"He hops out of the wagon and leads Cliff away through some pine trees."
"Hope they don’t get too reckless and lose track of the time."
stop music fadeout 5.0
play background "sfx/nightdesert.ogg" fadein 5.0
"I lean against the wagon and sigh."
show jeb at center with dissolve
"Jeb is walking to the front of the cart. I lift one of the canvas flaps to take a peek at him pulling on a lever while shoving forward."
m "\"So what’s the problem?\""
show jeb talking with dis
jeb "\"I had to slow the jennies down with the brakes while they were at full gallop.\""
show jeb with dis
m "\"...and?\""
show jeb shocked with dis
"Jeb gives me a look."
show jeb shocked talking with dis
jeb "\"You’re not supposed to do that.\""
show jeb shocked with dis1
show jeb shocked talking with dis
jeb "\"Brake drums could be stripped.\""
show jeb with dis
m "\"What’s a brake drum?\""
show jeb talking with dis
jeb "\"Metal pieces that press against a wheel axle.\""
show jeb with dis1
show jeb talking with dis
jeb "\"It’s what happens when you pull the brake lever.\""
show jeb with dis1
show jeb talking with dis
jeb "\"Stops it from movin’ as easy.\""
show jeb doubt with dis1
show jeb angry talking with dis
jeb "\"How come you don’t know that?\""
show jeb doubt with dis
m "\"Know what?\""
show jeb doubt talking with dis
jeb "\"How things work.\""
show jeb doubt with dis
"My face feels a little hot."
m "\"Didn’t have much opportunity to learn.\""
show jeb talking with dis
jeb "\"That’s surprising.\""
show jeb with dis
m "\"What is?\""
show jeb talking with dis
jeb "\"I just had you pegged for a handyman with a build like that.\""
show jeb with dis1
show jeb talking with dis
jeb "\"Maybe you’re more of a soldier.\""
show jeb with dis
"He’s nosier than I thought, too."
m "\"And you sure seem to think a lot for a farmer.\""
show jeb talking with dis
jeb "\"A dumb farmer’s a dead farmer.\""
show jeb happy2 with dis
jeb "\"More of a rancher, though.\""
jeb "\"Not the best growing soil in these parts.\""
show jeb talking with dis
jeb "\"Unless you eat pinecones.\""
show jeb with dis
m "\"Can’t say I have.\""
show jeb talking with dis
jeb "\"Could tell.\""
show jeb happy with dis
jeb "\"You ain't a string bean like that weasel, so you must eat well.\""
show jeb talking with dis
jeb "\"Speaking of which, mind getting behind the cart? I want to test the brakes.\""
show jeb with dis1
hide jeb with dis3
"I pull my head out from under the canvas and walk to the back of the cart, repositioning my stance and bending my knees."
"My paws rest on the tailgate plank."
jeb "\"Little bit lower. Try to push near the framework.\""
m "\"This fine?\""
jeb "\"That’ll do it.\""
"He pulls the wooden lever at the front of the wagon again."
jeb "\"Push as hard as you can.\""
"I put the weight of my core behind my forearms as I try to make the wagon budge."
"I grunt, and the wood creaks from the force I apply, but it doesn't give."
show jeb at right with dissolve
show jeb talking with dis
jeb "\"Looks like we’re good to go.\""
show jeb with dis
m "\"The others ain’t back yet.\""
"Jeb swears softly under his breath."
m "\"So...\""
m "\"How exactly did you run across getting those donkeys?\""
show jeb talking with dis
jeb "\"You mean Doris and Daisy?\""
show jeb with dis
m "\"You named 'em?\""
show jeb talking with dis
jeb "\"Nah.\""
show jeb with dis1
show jeb talking with dis
jeb "\"They belonged to somebody else.\""
show jeb with dis1
show jeb talking with dis
jeb "\"They named 'em.\""
show jeb with dis
m "\"Bit sentimental for a rancher to name their pack animals ain’t it?\""
show jeb talking with dis
jeb "\"Well, he was sentimental.\""
show jeb with dis
m "\"That's too bad.\""
show jeb talking with dis
jeb "\"Yeah, well, I liked that he was sentimental.\""
show jeb with dis
m "\"What do you mean was?\""
show jeb with dis
jeb "\"He's dead now.\""
show jeb with dis
m "\"Well shit.\""
m "\"I'm sorry.\""
show jeb talking with dis
jeb "\"Yeah, well so am I.\""
show jeb with dis
"Jeb crouches to double check the wheels again."
m "\"You know, my folks didn't want me to name any of the livestock.\""
m "\"Said it would make me too attached to the livelihood.\""
m "\"Even so, Doris and Daisy don't seem very fitting for jennies like them or a fella like you.\""
show jeb talking with dis
jeb "\"If you get your own pack animals you can call them what you please.\""
show jeb with dis1
show jeb talking with dis
jeb "\"But just in case you're still confused about them being my jennies...\""
show jeb with dis
"He points at the one on the left."
show jeb angry talking with dis
jeb "\"That's Doris.\""
show jeb angry with dis
"He points at the one on the right."
show jeb angry talking with dis
jeb "\"That's Daisy.\""
show jeb angry with dis
"I cackle."
m "\"Sorry Doris. Sorry Daisy.\""
show jeb doubt with dis
jeb "\"They can't understand you.\""
show jeb talking with dis
jeb "\"They don't have the brains or the speech capabilities we do.\""
show jeb with dis
m "\"I can't disagree.\""
m "\"I just did not mean to offend.\""
m "\"Like when I say that they smell bad.\""
show jeb talking with dis
jeb "\"It's not them you're offending.\""
show jeb doubt with dis
m "\"Noted.\""
"I take a little walk and let Jeb mind his business with the wagon checks."
"It takes about ten minutes for Cliff and Murdoch to show up again."
show cli happy at left with dis
show mur smile at center with dis
m "\"How’d it go, you two?\""
show cli talking with dis
cl "\"It was blistering.\""
show cli with dis
show mur talking with dis
mu "\"But we got some decent captures of the countryside, I think.\""
show mur with dis
show jeb talking with dis
jeb "\"We’re ready to move. Hop on in the wagon if any of you get dizzy.\""
show jeb with dis1
hide cli with dis3
hide mur with dis3
hide jeb with dis3
"We push on without much trouble."
"The fox and the weasel are the most talkative."
"Me and Jeb stay relatively quiet."
$ renpy.music.set_volume(0.25, channel='sound')
play sound "sfx/distant train.ogg"
"The noise of the trains is a quiet hoot in the distance."
stop background fadeout 1.5
scene bg black with dissolve
stop sound
$ renpy.music.set_volume(1.0, channel='sound')
scene bg trail2 with dissolve
play music "music/nostalgia.ogg" fadein 7.0
"We've been going for hours now."
"Echo’s a tiny dot behind us, but the load on my shoulders hasn’t gotten any lighter."
"We've gotten to a sloping path lined by boulders and sagebrush. It's more rocky than sandy, and it's absolute hell on my paws."
"I thought it couldn't get any warmer, but it has."
"My bag is starting to stick to my back, shirt as drenched as my fur is."
"It's getting cumbersome."
"I'd complain, but my mouth's so dry it's like I taste fire with every breath."
"I need a whiskey."
"Or a tall glass of sweet tea."
"Looking around, I ain't the only one. Both Cliff and Murdoch have their tongues lolling out their muzzles."
"It's more than a bit strange to see Cliff this sweaty and messy."
"Even after sleeping with him he still looked all prim 'n proper."
"The only one keeping a stern face is Jebediah, who's lowered his cap over his eyes."
m "\"So how long is this gonna take?\""
show jeb talking at center with dissolve
jeb "\"We’re about halfway to the sightseeing point right now.\""
show jeb with dis
m "\"It's that far?\""
show jeb happy with dis
jeb "\"And we ain't even gotten to the steep part yet!\""
m "\"The... steep part?\""
"There's... a steep part?"
show jeb talking with dis
jeb "\"Never been to the sightseeing point before? It's a pretty popular hiking spot.\""
jeb "\"Some of the best damn views in the state, if you ask me.\""
show jeb with dis
m "\"But it's such a long walk.\""
show cli talking at right with dis
cl "\"I've heard people say it's haunted.\""
show cli eyes talking with dis
cl "\"Baseless rumors, of course, but intriguing nevertheless.\""
show cli happy with dis
cl "\"Would you happen to know anything about it, Jebediah?\""
show jeb talking with dis
jeb "\"There are a few stories, yup.\""
show jeb happy with dis
jeb "\"Like how sometimes when you shout into the canyon at a specific time, you'll hear a voice. Sometimes more than one.\""
show jeb talking with dis
jeb "\"There's also tales of folks who peeked over the canyon's edge and saw corpses down below.\""
show jeb doubt with dis
jeb "\"When they went down to look, there was no one there.\""
show cli doubt with dis
cl "\"That sounds awful.\""
"I've heard that one too."
"Usually from miners too drunk to even walk out the door without tripping over themselves."
"So I'm not entirely convinced."
hide jeb with dis
show mur concerned d at left with dis
mu "\"People have actually died here.\""
show mur fear d with dis
mu "\"I’ve heard William mention it once or twice. People go out for a hike and never come back.\""
mu "\"Sometimes it’s dehydration, sometimes it’s—\""
"He winces."
mu "\"Sometimes it’s something worse.\""
m "\"What, suicide?\""
show mur concerned d with dis
mu "\"Maybe. Accidents are common. Especially when alcohol is involved.\""
mu "\"It doesn’t take much to slip and fall when you’re at the top.\""
"Well, don't that just fill me with confidence."
mu "\"Especially for the drunks showing off.\""
show mur with dis
m "\"So why are we goin’ there again?\""
"I wipe the sweat off my brow and undo one of the buttons on my shirt."
"Cliff doesn’t miss it, somehow managing to get his tongue back into his mouth before talking again."
show cli talking with dis
cl "\"It's the fastest way to our destination.\""
show cli eyes talking with dis
cl "\"Don't worry. There's no such thing as ghosts.\""
show cli with dis
m "\"You sure seem interested in hearing these stories, though.\""
show cli eyes talking with dis
cl "\"My friend, legends and myths play a large role in cultures all over the world.\""
show cli talking with dis
cl "\"Whether about the creation of the Earth or about the voices we hear when we're alone at night, these stories shape our very lives and how we perceive things.\""
show cli happy with dis
cl "\"I'm not exactly a pious man, Samuel, but there is something special about the unexplainable, or believing we're a part of some greater whole.\""
m "\"Do you believe in God?\""
show cli doubt with dis
cl "\"I don't know, to be honest.\""
show cli down with dis
cl "\"My mother and father were devout Catholics, as was my sister.\""
cl "\"I went to many a sermon in my youth.\""
cl "\"But as I got older and struck out on my own, I realized that who I am as a person—\""
"He takes a deep, shuddering breath, shaking his head."
show cli sad with dis
cl "\"Who I am as a person didn't exactly align with what was expected of me.\""
"I’m starting to understand what he meant by “kinship” last night."
show cli talking with dis
cl "\"Ah, but you didn’t join me on this expedition just to hear me prattle on about myself.\""
show cli with dis
m "\"It’s okay.\""
show mur talking with dis
mu "\"Indeed. We’re in this for the long haul, after all.\""
if MT_Points < 1:
    show mur mischief with dis
    mu "\"It wouldn’t do for us to keep secrets from one another.\""
    show mur sideeye with dis
    mu "\"Right, Samuel?\""
    "I freeze. We exchange glances, his cold stare more than matchin’ this damn heat."
    m "\"Uh, yeah.\""
    show cli happy with dis
    cl "\"Agreed. Thank you. All of you.\""
else:
    show mur smile with dis
    mu "\"We’re going to be relying on one another a lot.\""
    show cli talking with dis
    cl "\"That we are.\""
    cl "\"I couldn’t ask for better companions.\""
    show cli happy with dis
    cl "\"Thank you. All of you.\""
show mur talking with dis
mu "\"That includes you, Jebediah!\""
"The horse tips his hat at us."
if MT_Points < 1:
        "I’m left with an uneasy feeling."
else:
        "I grit my teeth. I’m gonna hate leaving them tonight."
        "But I need to."
mu "\"Actually...\""
"The fox stops in his tracks, grabbing his camera. He gestures at us."
show mur holdcamera with dis
mu "\"Would you mind?\""
cl "\"Oh? A picture? Won’t that be a waste of film?\""
mu "\"You underestimate me, Mr. Tibbits.\""
mu "\"I’ve brought enough film to last me a year.\""
cl "\"Oh! Alright, then.\""
mu "\"Don’t you worry, Cliff. I’ll capture your good side.\""
m "\"Do we have time for it?\""
jeb "\"We’re actually makin’ good headway. Should be fine.\""
"He stops the wagon, leaning back with a long sigh."
mu "\"Good lighting is the most important thing for an outdoor photograph.\""
mu "\"That boulder should do.\""
show cli at right with dis
cl "\"Won't it be blistering?!\""
mu "\"It's mottled with enough shade, should be fine.\""
show cli happy with dis
cl "\"Oh! So it is.\""
hide cli with dissolve
mu "\"I told you so.\""
show mur snapshot with dis
mu "\"Why don't you stand next to him, Sam?\""
m "\"Absolutely not.\""
mu "\"Suit yourself, sourpuss.\""
mu "\"Look slightly down and tilt your head to the left.\""
mu "\"I'll count down from three. Remember to sit still and give me your best smile.\""
play sound "sfx/camera windup.ogg"
mu "\"Three... two... one...\""
play sound "sfx/camera release.ogg"
mu "\"Got it!\""
mu "\"Now let's get one without your shirt.\""
cl "\"Why?\""
m "\"Because he's a sex pervert.\""
cl "\"In that case, the shirt comes off!\""
mu "\"I thought you'd be more understanding, Sam.\""
m "\"I just think it ain't the smartest move to leave evidence lying around for the people who might want to lynch me.\""
m "\"No tellin' what folks would do with this stuff in the wrong hands.\""
mu "\"With a body like Cliff's, I find it very easy to imagine what somebody would do with his image in their hands.\""
mu "\"Besides, he's only shirtless.\""
m "\"For now.\""
mu "\"For now.\""
"I shake my head as this sorry sight goes on for ten more minutes."
stop music fadeout 2.0
scene bg black with dissolve
scene bg canyon2 with dissolve
play background "music/windbirds.ogg" fadein 10.0
"The sagebrush is getting thicker as we climb the slope."
"Pretty soon, we’re almost at the top of the canyon trail."
"I ain’t been this high up in a while."
"Not since getting to Echo."
"I take a look at my watch. Almost noon, and we’ve been walking since dawn..."
"Counting the breaks we took, it must’ve been about seven hours."
"I can definitely feel it wearing me down, and I’m used to moving a lot during the day."
"Can’t imagine what Cliff must be going through."
jeb "\"Almost there, now. Just a short hike left.\""
cl "\"Is there shade at the top?\""
jeb "\"Some.\""
jeb "\"And a tree stump or two to sit on.\""
mu "\"Good. I can't feel my paws anymore.\""
"I can't either. I need to wring out my shirt."
cl "\"We can rest for about an hour. Perhaps we should try some of our rations.\""
jeb "\"The trek down's a mite easier, at least.\""
m "\"Where are we gonna make camp tonight?\""
"Jebediah points to the forest stretching out below us."
jeb "\"Might not look it, but there's a stream runnin' down there we can use to wash up an' fill our flasks.\""
jeb "\"And the trees provide plenty of cover.\""
"Might make it easier to slip away."
cl "\"That forest is gigantic. What if we get lost?\""
jeb "\"I've been there more times than I've drawn breaths at this point. Y'all follow my lead and everything'll be hunky-dory.\""
"I can tell by the look of his pouting face that Cliff isn’t too satisfied with Jebediah's answer."
"Murdoch notices too, clapping the weasel on the shoulder."
mu  "\"We'll be fine, Cliff.\""
"Cliff relaxes."
cl "\"Ah, sorry, it's just that—\""
m "\"Everything needs to be perfect? We know.\""
"Cliff laughs sheepishly."
cl "\"Yes.\""
"He sighs, pushing his glasses further up his snout. The lenses are starting to look a little foggy."
cl "\"You probably think it strange of me to worry so much.\""
mu "\"We’re all a little strange.\""
mu "\"Right, Jeb—\""
"The wagon comes to a halt, the wheels creaking. One of the donkeys starts balking."
"For a second, I think Jebediah's finally had enough of Murdoch, but the horse then gestures to a worn sign surrounded by a couple of tree stumps."
jeb "\"This is the spot. You folks can have a seat, I'll give the girls something to drink.\""
mu "\"Girls?\""
mu "\"Oh, the donkeys.\""
$ renpy.music.set_volume(0.2, delay=3.5, channel='background')
scene bg canyon3 with fade
play music "music/canyon.ogg" fadein 10.0
"The relief that comes over me when I finally sit down on a tree stump more than makes up for the agony of getting here."
"I look out over the woods in the canyon down below."
"They stretch out for miles and miles, so dense that I can't see the ground underneath."
"You definitely don't see this much green in Echo, that's for sure."
show jeb at right with dissolve
"Jeb’s checking some supplies we unloaded from the wagon."
show cli happy at center with dis
"He urged Cliff to take a break, but there the weasel is running his little paws over every crate and bag to make sure everything’s in there."
m "\"Got everything you need, professor?\""
"He takes his satchel from the heap of things still on the wagon."
show cli talking with dis
cl "\"Everything is accounted for. I suggest we get some rest.\""
show cli with dis
"You don’t gotta tell me twice."
hide cli with dissolve
hide jeb with dissolve
"First thing I do is decide to take off my shirt."
"The sweat’s startin’ to remind me of the Hip a little, and I feel a need to clean myself coming up."
if MT_Points > 0:
    "I got more than one pair of eyes on me."
    "Murdoch whistles."
    show mur mischief at left with dis
    mu "\"I’ve been told the views up here were nice, but I wasn’t quite expecting this.\""
    show cli blush eyes right at right with dis
    cl "\"{i}Murdoch!{/i}\""
    "His tone’s admonishing, but the stoat’s ogling me too."
    "As is the horse."
    show jeb shocked at center with dissolve
    "When I lock eyes with Jebediah, he immediately turns around, pretending to take care of the donkeys and taking a large swig of water."
    hide jeb with dis
    "I don’t pay it any mind. I’m used to folks looking."
    show mur blush with dis
    mu "\"It really is a sight to behold.\""
    m "\"Keep starin' like that and it's gonna cost ya.\""
    "He clears his throat, gesturing to the trees."
    show mur mischief with dis
    mu "\"I was talking about the canyon.\""
    m  "\"Sure ya were.\""
    hide cli with dissolve
    hide mur with dissolve
    hide jeb with dissolve
"Cliff pads on over, and I press my legs together to give him some extra space on the stump."
"He doesn’t hesitate, leaning up against me after tucking in his tail."
"His ears are red."
show cli blush eyes closed talking at center with dis
cl "\"Do you mind?\""
show cli blush eyes closed with dis
m "\"If I change my mind you won't be hard to shove off.\""
"He’s smelling strong again, though not at all like mint this time."
"It's that cloying, almost sweet kind of smell that otter and ferret folk tend to have."
"It ain’t bad, but it's unmistakable."
"A bit surprising what’s underneath all that perfume."
"He lets out a shaky breath. He tries to relax, but before long, he’s fidgeting again."
"I put a paw on his back."
m "\"You sick or somethin'?\""
show cli blush eyes right with dis
cl "\"No. I daresay this is the most I've enjoyed myself since...\""
show cli blush eyes closed talking with dis
cl "\"...well, since I met you, Sam.\""
show cli blush eyes closed with dis
"It’s a bit too much, and I think he has to know that, but I’ll let the weasel have his fun just for today."
"It's the last day I'm his."
m "\"That good, huh?\""
"I whisper so Murdoch and Jebediah can’t hear, and give his arm a squeeze."
"He squeaks."
show cli blush eyes closed talking with dis
cl "\"That good.\""
show cli blush eyes closed with dis
"He closes his eyes, breathing out through his nostrils."
m "\"Then why are ya fidgetin' so much?\""
show cli blush eyes right with dis
cl "\"I’m just anxious to get started on my research, is all.\""
show cli eyes talking with dis
cl "\"I suppose I can begin right here.\""
show cli talking with dis
cl "\"The rumors Jebediah mentioned should be easy to verify.\""
show cli with dis
m "\"You mean the ones about the voices?\""
show cli happy with dis
cl "\"Yes. I doubt their veracity, but it’ll make for a fun experiment.\""
show cli talking with dis
cl "\"Though I think I might enjoy the shade a little while longer.\""
cl "\"Heavens, I wish I could take a bath right now...\""
hide cli with dissolve
"He yawns, then gets comfy against me, lidding his eyes."
"Next to us, Murdoch gets up off the ground, dusting himself off with a grunt."
show mur talking at center with dissolve
mu "\"I'm going to be taking some pictures of the canyon, if you don't mind.\""
show mur mischief with dis
mu "\"The weather's perfect for some {i}natuurfotografie{/i}.\""
"It's aimed at Cliff, but the weasel's already fast asleep against my chest, snoring softly."
show mur eyes with dis
"Murdoch tsks."
show mur talking with dis
mu "\"If you need me for anything, I'll be a bit further down the trail.\""
show mur with dis
show jeb talking at left with dissolve
jeb "\"Be careful of where you're walking. I don't wanna have to scrape you off the rocks below.\""
show jeb with dis
show mur mischief with dis
mu "\"Of course. I don't want to break any of my equipment.\""
show jeb talking with dis
jeb "\"Or your neck.\""
show jeb with dis
"Murdoch chuckles."
show mur eyes with dis
mu "\"Jebediah, what do you take me for?\""
show jeb talking with dis
jeb "\"I know a rookie when I see one.\""
show jeb with dis
show mur mischief with dis
mu "\"These rocks have got nothing on my home life.\""
show mur talking with dis
mu "\"But I'll watch my footing if you'll watch my things.\""
show mur with dis
show jeb talking with dis
jeb "\"We're leaving in an hour.\""
show jeb with dis
show mur talking with dis
mu "\"I know, I know.\""
hide mur with dissolve
hide jeb with dissolve
"He walks off, camera in his paws."
stop music fadeout 3.0
"I turn to Jebediah, who's leaning against the wagon."
m "\"There's actually something I want to ask ya.\""
show jeb at center with dissolve
play music "sfx/nightdesert.ogg" fadein 5.0
"The stallion tilts his head."
m "\"Do you know anything about a monster around these parts?\""
show jeb talking with dis
jeb "\"Monsters?\""
jeb "\"I know some stories.\""
show jeb with dis
m "\"I, uh... A friend saw this big gray one.\""
m "\"Red eyes. Smelled real bad.\""
"He mulls it over for a moment."
show jeb happy2 with dis
jeb "\"Ain't no monster I've ever heard of. Sorry.\""
"Must really have been a dream then."
show jeb talking with dis
jeb "\"There's another creature that's been gettin' spotted 'round Echo though.\""
show jeb with dis
m "\"What's it look like?\""
show jeb doubt talking with dis
jeb "\"That's the strange part: it doesn't look like much of anything.\""
show jeb with dis1
show jeb talking with dis
jeb "\"My buddy Avery has a friend who has a sister who claims she saw it while doin' laundry.\""
show jeb with dis
m "\"Avery? The Meseta physician in town?\""
"I didn't think this horse would have all that many friends, much less that one of them would be the man who stitched me up after what happened."
"Odd couple."
show jeb talking with dis
jeb "\"That's him.\""
show jeb with dis
m "\"He never told me about any monsters.\""
show jeb talking with dis
jeb "\"That's because you ain't ever seen him after two beers.\""
show jeb with dis1
show jeb talking with dis
jeb "\"He'll tell you just about anything when he's shitfaced.\""
show jeb with dis1
show jeb talking with dis
jeb "\"Anyway, this friend's sister said the thing she saw had no fur an' smelled like burning flesh - like charcoal.\""
show jeb with dis1
show jeb talking with dis
jeb "\"It was so mangled-lookin' she didn't even know what species it was. Had holes where its face should have been.\""
show jeb with dis
m "\"That's odd.\""
show jeb talking with dis
jeb "\"Ain't that the truth?\""
show jeb with dis1
show jeb talking with dis
jeb "\"Anyway, it did nothin'. Just stood there.\""
show jeb with dis1
show jeb talking with dis
jeb "\"When she turned 'round, it was gone.\""
show jeb doubt with dis1
show jeb doubt talking with dis
jeb "\"That evening, all the chickens were dead in the coop.\""
show jeb doubt with dis1
show jeb doubt talking with dis
jeb "\"Avery told me they had to sell the farm.\""
show jeb with dis
m "\"Smells more like bullshit than burnin' flesh, if ya ask me.\""
show jeb talking with dis
jeb "\"Just a drinkin' story, yeah? It was probably sickness that did the chickens in, if it's true at all.\""
show jeb with dis1
show jeb talking with dis
jeb "\"Same goes for this canyon.\""
show jeb sad with dis1
show jeb sad talking with dis
jeb "\"People are just seein' things they want to see an' hearin' things they want to hear.\""
show jeb sad with dis1
show jeb sad talking with dis
jeb "\"I've been goin' on this route for years and I never once heard voices.\""
show jeb sad with dis1
show jeb sad talking with dis
jeb "\"Folks like to blame things on a boogeyman all too quick-like.\""
show jeb doubt with dis1
show jeb doubt talking with dis
jeb "\"Mr. Tibbits right there probably knows that all too well.\""
show jeb doubt with dis
"He gestures to the sleepin' weasel draped over my chest."
m "\"He said you were the only guide willing to take him.\""
show jeb talking with dis
jeb "\"I was. Not too many folks in Echo are keen on strangers and foreigners.\""
show jeb with dis1
show jeb talking with dis
jeb "\"Good thing your fox friend knew to take him to the Stag.\""
show jeb with dis
m "\"I keep hearing that name.\""
show jeb talking with dis
jeb "\"It's surprising you haven't been there considerin' the company you keep, if you catch my drift.\""
show jeb with dis1
show jeb talking with dis
jeb "\"But like your fox friend said, we're all a lil' strange.\""
show jeb with dis1
show jeb talking with dis
jeb "\"Gotta be, in a place where there's more tumbleweeds then there are single women.\""
show jeb with dis
"The weasel stirs and brings his paws to his eyes, rubbing underneath his foggy glasses."
"He yawns as he turns towards me, and I get a good whiff of his breath spray."
m "\"Mornin’, professor.\""
show cli shocked at right with dissolve
cl "\"Morning?!\""
"He looks around in a panic, flailing against me in an effort to get up. Damn near hits me in the face."
cl "\"How long did I sleep?!\""
m "\"A couple of minutes.\""
show cli talking with dis
cl "\"Oh!\""
show cli with dis
"He stops struggling and takes a breath like it's his first this year."
show cli talking with dis
cl "\"Thank goodness.\""
show cli eyes with dis
"He shuts his eyes again."
show cli eyes talking with dis
cl "\"Where's Murdoch?\""
show cli eyes with dis
m "\"A bit further down the trail. He left to take some pictures.\""
show cli talking with dis
cl "\"I don't suppose you could fetch him for me?\""
show cli with dis
m "\"What for?\""
show cli talking with dis
cl "\"I need a few pictures of myself taken for the thesis, and this would be the perfect backdrop.\""
show cli with dis
m "\"Sure ya don't wanna get some more sleep?\""
m "\"You were lookin' pretty peaceful there.\""
show cli eyes talking with dis
cl "\"You don't have to fret so much, Sam.\""
show cli talking with dis
cl "\"I can take care of myself.\""
show cli with dis
"I leer at the scrapes on his arms from a few days ago."
m "\"What are you going to do while I'm gone?\""
show cli talking with dis
cl "\"I shall prepare the food for this afternoon and go over our next course of action with Jebediah.\""
show cli happy with dis
cl "\"And perhaps change into something more comfortable, not to mention dry.\""
m "\"What kind of food are we gonna eat?\""
show jeb talking with dis
jeb "\"Best I can do is canned beans.\""
show cli doubt with dis
show jeb with dis
m "\"Oh.\""
hide cli
hide jeb
with dis3
"My favorite."
"The weasel gets off of me so I can leave, pressing his muzzle to my cheek for a moment."
cl "\"Thank you, Samuel. I appreciate it.\""
m "\"Don't mention it.\""
$ renpy.music.set_volume(0.15, delay=3.5, channel='background')
scene bg black with dissolve
scene bg canyon with dissolve
if MT_Points < 1:
    play music "music/bedhorror.ogg" fadeout 2.0 fadein 8.0
else:
    play music "music/quiet.ogg" fadeout 2.0 fadein 8.0
"Where did that damn fox run off to?"
"I've been walking down this trail for over ten minutes and still no sign of him."
"Did he slip and fall?"
if MT_Points < 1:
    "That'd be one less thing to worry about."
else:
    "I hope not."
    "Don't want to look any more suspicious than I already do."
"I finally see his bushy tail peeking out from behind a boulder a ways off, near the edge."
"I can catch his smell even from all the way over here."
"It’s got to be him."
play sound "sfx/gravelwalk.ogg"
"I near the boulder, dirt crunching underneath my paws."
"Step..."
"...by step."
play sound "sfx/camera release.ogg"
"The camera clicks."
"I hear him mumbling."
if MT_Points < 1:
    stop music fadeout 10.0
    "I won’t ever get a chance like this again."
    "He’s not too far away now."
    "I could be rid of him in seconds."
    "No one would know."
    "Accidents happen, right? He said so himself."
    "The camera clicks again."
    "I’m almost around the corner."
    "I thought I’d be scared of him noticing me, but I don’t feel anything."
    "His back is turned to me, ears twitching as I take the last few steps."
    "He's close to the edge."
    "Too close for comfort."
    "He doesn't look at me."
    "Perfect."
    "I put my paw just below his shoulder."
    "All it takes is one little push."
    menu shove_menu:
        "Shove him":
            "I catch myself right before I can do it."
            "What the fuck is wrong with me?"
            play music "music/bedhorror.ogg" fadein 10.0
            show mur shock at center with dis
            "The fox turns his head, green eyes looking straight through me."
            "He doesn’t seem to know what’s going on."
            mu "\"Sam?\""
            m "\"Cliff wants to see ya.\""
            show mur fear d with dis
            mu "\"So you sneak up on me?\""
            show mur concerned d with dis
            mu "\"You scared the whiskers off of me! I could have fallen right off!\""
            "Scared them off of me too."
            "He steps back from the edge of the canyon."
            m "\"I'm sorry. Didn't mean to.\""
            m "\"I, uh, thought you could hear me.\""
            "Of course I keep lying. It's about the only thing I'm good at nowadays."
            show mur eyes with dis
            stop music fadeout 5.0
            mu "\"I suppose this is as good a time as any.\""
            show mur sideeye with dis
            mu "\"Listen, Sam.\""
            m "\"Yeah?\""
            mu "\"We need to talk about what happened at the store.\""
            play music "music/murdochtheme.ogg" fadein 10.0
            mu "\"Why did you run?\""
            m "\"Uh...\""
            "I'm the one feeling backed against the edge right now."
            m "\"I forgot about an appointment.\""
            "I can't even convince myself."
            show mur angry with dis
            mu "\"Sam, please, tell me the truth.\""
            mu "\"If you know something about the murder, or about Huxley—\""
            m "\"I don't know anything about it.\""
            mu "\"Really? Because you've been acting awfully suspicious.\""
            m "\"Get off my case.\""
            show mur concerned d with dis
            mu "\"Samuel.\""
            "I grit my teeth. I feel like I could cry."
            show mur sad with dis
            mu "\"I want to {i}help you{/i}.\""
            mu "\"If there's anything you want to tell me, you can. I won't judge.\""
            m "\"You can't help me.\""
            show mur concerned d with dis
            mu "\"I've completed my fair share of impossible tasks.\""
            mu "\"As much as you don't want me here, we're in this together.\""
            show mur smile with dis
            mu "\"You, Cliff, Jebediah, and I.\""
            "His tone's lighter now."
            "The voice that was telling me to shove him off a cliff only a few minutes ago is quiet, and I can only hear the wind now.\""
            "I feel peaceful."
            "I catch myself sniff."
            "My eyes are warm and wet."
            m "\"I'm sorry.\""
            "It's the first real apology I've made this entire time."
            "I step back as the fox steps forward, letting him pass."
            show mur eyes with dis
            mu "\"I’m sorry, too.\""
            show mur eyes talking with dis
            mu "\"I'll see you at the sightseeing point, alright?\""
            m "\"Alright.\""
            hide mur with dis
            jump aftercanyon
else:
    m "\"Murdoch?\""
    show mur mischief at center with dis
    "The fox turns around, a grin on his face."
    show mur talking with dis
    mu "\"Samuel!\""
    show mur mischief with dis
    mu "\"Anyone ever tell you you shouldn’t sneak up on a man standing near the edge of a canyon?\""
    m "\"Anyone ever tell you standin’ so close to the edge ain’t a good idea?\""
    show mur talking with dis
    mu "\"Jebediah might have, once or twice.\""
    show mur with dis
    m "\"Heard you mumblin’.\""
    show mur talking with dis
    mu "\"I’ve been talking for a while, but what do you know, the canyon hasn't replied yet.\""
    show mur eyes with dis
    mu "\"Guess the stories weren't true after all.\""
    show mur mischief with dis
    mu "\"I'm almost disappointed.\""
    m "\"Cliff told me to come get you.\""
    m "\"Said he wants his pictures taken.\""
    show mur talking with dis
    mu "\"I’ll head right on over, then. Can’t leave the boss waiting.\""
    show mur mischief with dis
    stop music fadeout 8.0
    mu "\"I'm still dying to know what scared you off the other day.\""
    m "\"I already told ya.\""
    show mur talking with dis
    mu "\"Was it the truth?\""
    show mur with dis
    "I hesitate."
    show mur concerned d with dis
    play music "music/murdochtheme.ogg" fadein 10.0
    mu "\"Sam, if you have any information that can help—\""
    m "\"I don't.\""
    "Good. He doesn't know."
    mu "\"I'm worried about you.\""
    m "\"Why?\""
    show mur talking with dis
    mu "\"Because we're partners.\""
    mu "\"You, Jebediah, Cliff, and I.\""
    show mur smile with dis
    m "\"I already told you everything.\""
    show mur talking with dis
    mu "\"Alright, alright, we'll talk about this some other day.\""
    mu "\"There's something else on my mind anyway.\""
    stop music fadeout 3.0
    show mur with dis
    "He wipes the sweat from his brow with a sleeve."
    m "\"What is it now?\""
    show mur talking with dis
    mu "\"Cliff.\""
    play music "sfx/nightdesert.ogg" fadein 10.0
    show mur mischief with dis
    mu "\"You know, he’s rather smitten with you.\""
    m "\"I couldn’t tell.\""
    show mur talking with dis
    mu "\"I suppose he does make it rather obvious.\""
    mu "\"What about you? How do you feel?\""
    m "\"What are you gettin’ at? Are ya jealous or something?\""
    show mur eyes with dis
    mu "\"Oh, not at all. Quite the opposite, in fact.\""
    "The damn fox is speakin’ in riddles again."
    show mur mischief with dis
    mu "\"I’d like to make a proposition.\""
    m "\"Another wager of yours?\""
    m "\"It better not cost me any money.\""
    show mur talking with dis
    mu "\"I think you’ll like my terms this time.\""
    show mur with dis
    m "\"Which are?\""
    show mur blush with dis
    mu "\"I'd like to spend a night together. Just the three of us.\""
    "I tilt my head."
    m "\"You mean—\""
    show mur talking with dis
    mu "\"Yes.\""
    show mur with dis
    m "\"What makes you think he’ll say yes?\""
    "What makes him think I’LL say yes?"
    show mur mischief with dis
    mu "\"Call it a hunch.\""
    "I don’t care much for hunches."
    show mur talking with dis
    mu "\"I’ve seen the way he looks at you.\""
    m "\"I’ve seen the way you look at the both of us.\""
    show mur blush with dis
    mu "\"You're both easy on the eyes. I can't help myself.\""
    show mur talking with dis
    mu "\"It’s just a proposition, though. I don’t need an answer right away.\""
    m "\"Would I get paid?\""
    show mur mischief with dis
    mu "\"If Cliff’s to be believed, we’ll be famous men when we get back.\""
    mu "\"Perhaps even rich enough to afford you.\""
    mu "\"So yes.\""
    hide mur with dissolve
    "He walks past me, clapping me on the shoulder."
    mu "\"Give it some thought, why don't you?\""
    "With my plans being as they are, I don't have to."
    "The thought isn't too bad, though. There's worse-looking clients out there."
    jump aftercanyon




label aftercanyon:
stop background fadeout 4.0
play music "music/wind.ogg" fadeout 2.5 fadein 10.0
"Givin' me one of his grins again, Murdoch goes back up the trail, stuffing his paws in his pockets."
"Once I don't see him anymore, I walk over to where the fox stood, to the very edge."
"The wind's steady."
"It's warm and dry, kicking up a little sand."
"I have to shield my eyes."
"Damn near feels like I'm being cooked alive."
if MT_Points < 1:
    "I wipe the tears from my eyes."
else:
    "At least the view is pretty."
    "Not sure if it's worth hiking all the way, but I'd rather be here than with a client back home."
"Very, very carefully, I sit down and grab my flask."
"My legs dangle over the edge."
"I take a swig."
"The water's heaven on my tongue."
"I swallow, then have another drink right after."
"They can miss me for a little while."
"'Sides, after all that talk, I'm curious."
"Might as well try, right?"
m "\"Hello!\""
"I shout into the canyon, then lean back."
"Nothing."
"I don't know what I was expecting."
"I pour the rest of the flask's contents down my throat."
"The wind's howling around me now, whistlin' in my ears."
"Almost sounds like it's screaming."
play sound "sfx/thud5.ogg"
"A gust kicks up, knocking my flask out of my paws."
"I try and grab it before it falls, but it knocks me off-balance, forward."
play sound "sfx/clothrustle.ogg"
"For a moment, more than my legs are dangling off the canyon's edge."
"I get a sinking feeling in the pit of my stomach."
"This is how I die."
"I dig my claws into the ground, barely managing to keep myself from slidin' off."
"The flask tumbles down below."
play sound "sfx/voices.ogg"
"I can hear a garbled growl rise above the noise of the wind."
"What was that?"
"What is going on?"
"???" "\"Samuel!\""
stop music fadeout 8.0
play background "music/windbirds.ogg" fadein 10.0
$ renpy.music.set_volume(0.35, delay=4.0, channel='background')
"I crawl back from the edge, as far as I can."
"I’m still breathing hard."
"My throat burns."
"A brown paw on my shoulder brings me back."
show cli adv doubt at center with dissolve
"I look up and see Cliff looking down on me."
"He told me about them when we were walking to town hall this morning, but I almost don’t recognize him in his new clothes."
cl "\"What’s wrong?\""
m "\"N-nothing.\""
show cli adv talking with dis
cl "\"I wouldn’t say it’s nothing when you’ve been gone for an hour.\""
show cli adv with dis
"An hour?"
"I look at my watch again."
"An hour past noon."
"I could have sworn I’d only been here for two minutes."
show cli adv doubt with dis
cl "\"Murdoch returned a little while ago, but you never showed.\""
show cli adv blush eyes right with dis
cl "\"You had us worried.\""
show cli adv talking with dis
cl "\"Are you alright?\""
cl "\"You look rattled, to say the least.\""
show cli adv with dis
m "\"I’m fine. I just heard—\""
show cli adv talking with dis
cl "\"Voices?\""
show cli adv with dis
"I nod."
m "\"It might’ve been the wind.\""
show cli adv talking with dis
cl "\"True, the wind is rather strong up here.\""
show cli adv eyes talking with dis
cl "\"I must admit, I did try it myself.\""
show cli adv blush eyes closed talking with dis
cl "\"O-out of curiosity, of course. There's no way I'd believe such tall tales.\""
cl "\"No luck, however.\""
show cli adv blush eyes closed with dis
"Just like Murdoch."
m "\"I didn’t like it.\""
show cli adv talking with dis
cl "\"Look at it differently, Samuel.\""
cl "\"You should count yourself lucky to experience a phenomenon like that!\""
show cli adv with dis
m "\"I don’t feel lucky.\""
show cli adv blush eyes closed talking with dis
cl "\"Sorry.\""
cl "\"We’ll put a pin in it. What matters is that you’re safe.\""
show cli adv with dis
"He extends a paw I take all too happily."
show cli adv eyes talking with dis
cl "\"By the way...\""
"He leans in."
show cli adv blush eyes right with dis
cl "\"It’s a good thing you missed our afternoon meal.\""
show cli adv blush eyes closed talking with dis
cl  "\"I could barely stomach those beans. They were absolutely revolting.\""
"I can't help but feel like only somebody who's never had to miss a meal would considering going without a blessing."
"I'll have to ask Murdoch if he has anything quick to eat."
hide cli with dissolve
stop background fadeout 15.0
play music "music/samueltheme.ogg" fadein 15.0
"After meeting back up with the rest of the group, we pack up the gear before moving on."
"Jebediah gives me a piece of bread. It's a bit stale, but it's food nonetheless."
"Going down's much easier than climbing a steep hill."
"The scenery's getting more lush and less dusty."
"Thank God almighty. I was getting sick of the boulders."
"Even though the wagon's creaking an awful lot with every bump in the road, it doesn't break again."
"Not sure I could stand sitting around any longer."
"Cliff's in the wagon now, leaving Murdoch and me to walk side by side the rest of the way."
if MT_Points < 1:
    "After our talk a while ago, I don't mind too much."
else:
    "I'm still thinking about what he said earlier."
    "I have never had two clients at the same time."
    "Usually people keep to themselves, as they should in a town like Echo."
"Regardless, though, I've made up my mind."
"I'll sneak out of camp tonight."
"I've looked at Jebediah's map. I know where to go and what to do."
"If I want to, I can even take some of the supplies for myself."
"Cliff's brought too much food. He won't miss it."
"He'll miss me, but if I don't leave tonight, I'll have to go back to Echo."
"To Nik."
"To James."
"To William."
"Then to the gallows."
"I'd be a fool not to take this chance."
"At least whatever happens to Nik will have been for something."
$ renpy.music.set_volume(0.45, delay=5.0, channel='music')
"Nikolai..."
"I try and shake the thought out of my head."
"Put yourself first, Sam."
play music "music/cicadas.ogg" fadeout 6.0 fadein 10.0
scene bg black with slow_dissolve
$ renpy.music.set_volume(1.0, delay=3.0, channel='music')
scene bg forestnight with slow_dissolve
"We reach the heart of the forest by nightfall."
"Just like Jebediah said, there’s a stream nearby."
"Cliff and Murdoch go to wash up while me and Jebediah unpack the supplies and feed the donkeys."
$ renpy.music.set_volume(1.0, delay=0.0, channel='background')
play background "sfx/bonfire.ogg" fadein 10.0
"After gathering some firewood, we manage to get a fire with a good flame going."
"By the time the sun’s almost completely set, only orange light filtering through the tree leaves, we’re all huddled around it."
"Swapping stories."
"Drinking."
"Even Jebediah’s taking it easy for a change."
scene bg clicg3a with dissolve
mu "\"...he turned around, and there was the miner’s ghost, heaving a pickaxe high above his head!\""
mu "\"{i}You come for my gold, and I’ll come for your life!{/i}\""
mu "\"The soldier was never heard from again.\""
mu "\"They say that if you go near the mines at exactly midnight you can hear the miner striking rock, looking for gold.\""
mu "\"Thud...\""
mu "\"Thud...\""
mu "\"Thud.\""
"He continues to pantomime the entire thing."
cl "\"That was a terrible story.\""
cl "\"Why did the soldier even enter the mines in the first place?\""
cl "\"Why didn’t he just turn back the first time he heard the ghost?\""
cl "\"How could there be a message written in fresh blood if the ghost didn’t have any to begin with?\""
cl "\"There was no one else in the mines, and you didn’t mention a corpse.\""
"The fox waves his paw."
mu "\"Oh come on. The appeal of that story is in the sound effects, not the internal logic of the narrative.\""
cl "\"I could tell.\""
mu "\"If you'd like to tell a tale, go right ahead.\""
mu "\"I'm dying to hear some thrilling Batavian stories about being deprived of chocolate that is apparently better than everybody else's.\""
cl "\"I would, but I don’t want to terrify you, Murdoch. I’ll still require your services after tonight.\""
mu "\"Just admit you don’t have a story that's as fun as mine.\""
"He drinks from the whiskey flask being shared."
cl "\"I have plenty, I'll have you know! My grandfather was a storyteller like no other!\""
cl "\"I just think there’s nothing scary about ghost tales.\""
mu "\"Clifford.\""
mu "\"Do you really think I couldn't scare you if I wanted to?\""
cl "\"Not really, no.\""
mu "\"So you're just saying that I do need to try?\""
cl "\"Well, yes, but I still think you couldn't succeed if you wanted to with a ghost story.\""
m "\"Personally?\""
m "\"I don't need stories to scare me when we're out in the wilderness.\""
m "\"Silly ones are fine with me.\""
jeb "\"Hear hear.\""
play music "music/abyss.ogg" fadein 3.0
scene black with dissolve

scene clicg3c with dissolve:
    subpixel True
    truecenter
    zoom 1.0
    ease 300.0 zoom 1.7
mu "\"Well, then perhaps some of you will find this more informative than frightening.\""
"His tone of voice shifts in a way I'm not familiar with."
"The warm lilts and the lazy drawls are all gone."
mu "\"Pay attention to what I'm about to say.\""
"The sharp tone of voice he's using now sounds precisely practiced, and commands attention."
"Almost like something you'd hear from a carnival barker, but calmer than that."
mu "\"There's something that scientists have known for a long time about sensory experience and the truth.\""
mu "\"It's that all of our certain experiences are fascimiles of the truth.\""
mu "\"All of them.\""
mu "\"Everything from our excitement in the taste of good chocolate...\""
mu "\"To our relief when perceiving the form of a recognizable gaze through the fog or a mirror.\""
mu "\"And then there's pleasure in touch...\""
"He clasps his paws."
mu "\"...where I can feel the warm blood in my paws pulse against the blood in the other.\""
mu "\"And there's pain in separation, too.\""
mu "\"There's even exhilaration in the most basic of familiarities.\""
mu "\"Such as when you see your favorite color.\""
mu "\"But just know that even when we see something like the color red, we're not really seeing red.\""
mu "\"We're seeing all of the colors reflected back to us as light...\""
mu "\"Interpreted by the cones in our eyeballs that aren't absorbed by the color red.\""
mu "\"We only know red by what it isn't.\""
mu "\"Our experience of these realities that are objective to us are just a facsimile of the true experience...\""
mu "\"Compiled by the organic technology of the body.\""

m "\"What does fascimile mean?\""
cl "\"A reproduction.\""
"Murdoch nods again, the flicker lighting him in ways I don't think it ever has before."
mu "\"A fake.\""
"He punctuates that word so harshly."
cl "\"But how could that apply to something like tasting a piece of chocolate?\""
mu "\"What is taste but when the right combinations of molecules cause sensors on our tongue to send pleasing electrical signals to the brain?\""
mu "\"What you and I experience when tasting exactly the same thing could be close, but different, and we'd never be able to know.\""
m "\"...What?!\""
cl "\"That's merely a limitation of our biology then.\""
cl "\"Nothing so frightful about that.\""
mu "\"But what we're actually afraid of is not being able to know true difference.\""
mu "\"Or knowing something incredible through a freak accident of perception for only a moment, and then never getting to know it ever again.\""
mu "\"How many things in our world do you think cannot be perceived because we can only understand them through an absence of their true essence?\""
mu "\"How many colors are out there will we never be able to see because they're beyond our capability to fathom?\""
cl "\"If we'll never be able to know then we shouldn't have to worry about it.\""
mu "\"But you do want to know.\""
mu "\"You always want to know, because you are curious by nature.\""
"Cliff rolls his eyes but I can see a line on his face harden."
mu "\"What if this same idea that applies to senses could apply to things that are fully alive just as well as our sights and sounds and tastes?\""
mu "\"What secret world could be all around us at all times, intangible, unknowable, and unobtainable to our processing powers?\""
mu "\"What if I told you that there is such a world?\""
cl "\"Then I would say you were trying too hard.\""
mu "\"What if I told you that there are more worlds than one as well?\""
mu "\"Infinite worlds of unthinkable perception.\""
cl "\"But you said yourself that the unperceivable is exactly that.\""
cl "\"Intangible.\""
mu "\"But what if I told you there could be ways to perceive some things locked away in the brain, to let us perceive?\""
cl "\"Then I'd test them.\""
cl "\"Easy.\""
mu "\"Some people say there's a way.\""
cl "\"Well then I simply have to hear it, don't I?\""
mu "\"Just find a well that's dark enough and deep enough.\""
mu "\"It should be so dark that you shouldn't be able to see your reflection.\""
mu "\"Some people when they look down say they experience the overwhelming sense that something is looking back at them from the bottom of the well.\""
mu "\"And they feel that it's looking back every time.\""
cl "\"Sounds to me like they're scared of the idea of a reflection.\""
mu "\"Or...\""
mu "\"...Maybe it's just uncomfortable to be stared at?\""
scene black with dissolve

"I don't like that."
"I don't like that at all."
stop music fadeout 3.0
scene clicg3a with dissolve
cl "\"Alright, fine.\""
mu "\"What's fine?\""
cl "\"I'm admitting that was certainly better than the first attempt.\""
mu "\"So you're saying I scared you?\""
cl "\"I'm saying the story was successful.\""
cl "\"I'm not scared.\""
mu "\"But I can tell that it did scare you.\""
cl "\"Think what you like.\""
cl "\"I still have to go off of my experienced reality.\""
cl "\"Men frighten me more than monsters or ghosts ever could.\""
mu "\"Doesn’t seem to stop you from cozying up to Sam over there.\""
cl "\"Oh, come now!\""
mu "\"I'd certainly do the same if I could afford to hire a bodyguard.\""
"I look for a response from Jebediah, but the horse is still staring into the flames."
m "\"You alright, Jebediah?\""
"The fire crackles."
jeb "\"Fine enough.\""
mu "\"Just enough, huh?\""
jeb "\"You're a fine enough group to guide.\""
jeb "\"But very little beats the comfort of your own home.\""
mu "\"What's so comfortable about home?\""
mu "\"I'm plenty comfortable out here by the flames and under the stars.\""
jeb "\"Well at home you can drink as much as you want without fear of dehydrating.\""
"He jerks his head at the flask in Murdoch's paw."
jeb "\"And you can polish the banner whenever you like without the fear of somebody walking in on you whenever they need a jar of beans opened.\""
cl "\"That only happened one time.\""
"Murdoch looks incredulously at Jeb, then to Cliff."
cl "\"I mean the beans! Not the walking in!\""
m "\"That's the most frank I've ever heard you speak, Jeb.\""
mu "\"Yeah, well, you never saw him at the Stag.\""
jeb "\"Hush now.\""
cl "\"This is still a professional endeavor.\""
jeb "\"Quite.\""
mu "\"Right, but you're the one who brought beating off into the conversation.\""
"He shakes the bottle and more splashes out."
jeb "\"In peace.\""
jeb "\"Peace being the key word of that statement.\""
mu "\"Speaking along this train of thought!\""
mu "\"Jebediah, Cliff, and I want your opinion on something.\""
cl "\"No, don't!\""
"Murdoch licks the inside of his mouth, nodding and holding up a digit."
mu "\"We got talking while you were fixing the wagon, and...\""
"He pauses."
"He's really milking this for all it's worth."
"Cliff buries his face in his palms, groaning."
mu "\"You're a horse, right?\""
jeb "\"You only noticed just now?\""
mu "\"Beside the point.\""
mu "\"Cliff has asked me if it's true what they say about horses. That they've got big—\""
"He gestures to his crotch, spilling some whiskey on himself."
"Jebediah doesn't seem impressed."
jeb "\"It does its job.\""
mu "\"Sam, care to weigh in?\""
m "\"I'm not answering that.\""
mu "\"You sure? You spent quite some time alone together.\""
mu "\"Surely there must've been more going on than just fixing a wagon.\""
m "\"That's all we did.\""
"He's right about those horses, though."
mu "\"Dreadful, boys.\""
mu "\"I suppose we'll never know, Cliff.\""
cl "\"That's enough out of you. No more alcohol.\""
"The group laughs as Cliff tries to take the bottle and Murdoch pivots away."
"I look at my watch. Murdoch notices."
mu "\"I suppose it is about time, isn't it?\""
mu "\"What's our itinerary for tomorrow?\""
cl "\"We'll be cutting through the forest for most of it.\""
mu "\"The shade should be nice.\""
jeb "\"We'll be out by evening and reach the settlement by noon the day after.\""
m "\"The forest's that big?\""
jeb "\"And more treacherous than you might think.\""
jeb "\"Plenty of things that can kill you if they can sink their teeth into you.\""
mu "\"I thought we'd left Mr. Hendricks behind in Echo?\""
"Jeb and Murdoch laugh."
"I'd join in if he wasn't a client of mine."
jeb "\"Just keep an eye out. Snakes and spiders about.\""
m "\"What kinds of spiders?\""
jeb "\"Black widows and tarantulas.\""
jeb "\"And plenty of 'em.\""
"Makes the fur on the back of my neck stand on end."
jeb "\"Had one in my tent one time. Didn't end well—\""
m "\"Did you get bit?\""
jeb "\"—for the spider.\""
"He mimes smacking his arm."
mu "\"My heart palpitates, oh fearless leader.\""
jeb "\"Not fearless. Just not stupid.\""
"The fox stretches, handing Jebediah the whiskey bottle. The horse takes a swig."
mu "\"Knowing all of that, I think I'll retreat to my tent.\""
mu "\"We have a long day ahead of us, and I'd rather not be spending most of it nursing a hangover.\""
"The stoat looks at me with pleading eyes."
cl "\"I think I'll stay up for a little while longer. Perhaps I'll do some stargazing.\""
"Fuck."
mu "\"So long as you two stargaze quietly.\""
"Jebediah stands up as well, poking the fire with a stick."
jeb "\"I'll go to bed too. There's a book I want to finish. I'll see you fellas at dawn.\""
m "\"G'night.\""
"The fox and the horse both retreat for the night, leaving me and the stoat alone together."
"I can't believe he's not tired."
scene bg clicg3b with dissolve
"The cicadas are pretty loud."
"I doubt I could sleep even if I wanted to."
play music "music/mellowpiano.ogg" fadeout 2.0
m "\"So...\""
m "\"You're not joinin' them, huh?\""
cl "\"I need some quiet before bed.\""
m "\"You ain't gonna get it here.\""
cl "\"I didn't mean it quite so literally.\""
"He slips a little closer, grabbing my paw."
"I squeeze it a bit, mostly because I feel I'm supposed to."
cl "\"The stars are beautiful tonight.\""
cl "\"They don't shine this bright where I'm from.\""
m "\"I guess your painter friend can learn a thing or two from a visit.\""
cl "\"Anthonie van Houwelinck?\""
"He laughs."
cl "\"I suppose he could, were he still alive.\""
m "\"He's dead?\""
cl "\"Has been for quite a few years.\""
cl "\"You couldn't have known.\""
cl "\"I wonder what he'd have painted with this scenery.\""
cl "\"A warm, inviting, crackling fire, a beautiful full moon...\""
cl "\"And even better company.\""
"He squeezes my paw back, and I feel uneasy."
cl "\"Thank you for helping to realize my dream, Samuel.\""
"Doesn't feel like he's letting go anytime soon."
"Maybe if he runs his mouth a bit he'll get tired."
m "\"What are you gonna do once your feesus is finished?\""
cl "\"I intend to travel back to Europa and finish my studies. After that, I don't know.\""
cl "\"I might travel the world for a while.\""
cl "\"But I'll have to return to Batavia eventually.\""
m "\"To your family?\""
cl "\"Yes. My father isn't getting any younger, and they're expecting me to become the man of the house, as it were.\""
"He looks off to the side and his lip curls downward."
m "\"You don't sound too happy about it.\""
cl "\"Well you heard those men the other day, Samuel.\""
cl "\"You heard the sheriff.\""
"I don't think that's what William was upset about back there, but I don't think he needs to hear that right now."
cl "\"I'm not exactly the pinnacle of manhood.\""
cl "\"I'm not sure I even qualify as a man in my father's eyes.\""
cl "\"I might have sailed to a whole different continent, but the comments and the jeers are the same no matter where I go.\""
m "\"I always had the impression that most folks find you...\""
cl "\"Find me what?\""
m "\"Well the girls at the Hip were clamoring to see who you booked earlier.\""
m "\"A lot of them seemed pretty eager to get to spend the night with you.\""
m "\"So you always came across as desirable enough to me.\""
cl "\"Because I've never had problems socializing with women.\""
cl "\"Men have always been a different story.\""
cl "\"Perhaps I was foolish to think that in this wild, untamed frontier I'd be free to love who I want, no matter their gender.\""
"I'll say."
"But he's not wrong about how a man can treat other men."
"Out here, or anywhere."
"As soon as you're one foot out of step, they might not ever see you the same."
m "\"Well, fuck what the rest say about manhood and respectability.\""
m "\"You don't gotta answer to anyone but yourself.\""
"So long as you have money anyway."
"You're lucky you're loaded."
cl "\"I wouldn't have put it so bluntly, but yes.\""
cl "\"You have a point.\""
"He leans on over and hugs me tight, little weasel paws clamping on my back."
stop music fadeout 10.0
scene campfire with fade
m "\"So uh...\""
m "\"I was thinkin' about somethin'.\""
cl "\"Whatever you need.\""
m "\"Do you really need me much longer for this trip?\""
"He looks like he just got sucker punched."
cl "\"Sam?\""
cl "\"Whatever do you mean?\""
m "\"I mean, you're already in very good hands with Jeb, and Murdoch knows plenty of things.\""
m "\"You'll be in the settlement sooner than you know.\""
m "\"I could just take off early.\""
cl "\"But why?\""
cl "\"We're stronger traveling in a group.\""
cl "\"It's dangerous for you to just tromp off into the wilderness without rations or water.\""
cl "\"Plus. I...\""
"He swallows his spit."
cl "\"I've never had an experience like this before and I don't want it to end so soon.\""
cl "\"Do you?\""
m "\"Well I'm sorry Professor, but we agreed that this was entirely business from the beginning.\""
cl "\"Oh.\""
cl "\"I see.\""
m "\"So uh...\""
m "\"If you want me to give back the money I'll rip the check in half.\""
cl "\"No, no.\""
cl "\"I never specified how far you'd have to go.\""
cl "\"Keep the money.\""
"The fire crackles and I feel a lump in my throat."
m "\"Listen, Mr. Tibbits.\""
m "\"There's stuff you don't know about.\""
m "\"About me, I mean.\""
cl "\"I can assure you that the same applies for myself.\""
m "\"Right, well...\""
m "\"I don't think it would be in my best interest for me to go back to Echo.\""
m "\"So I need to go my own way.\""
cl "\"I understand.\""
m "\"I've had a decent time on this journey.\""
cl "\"And I have too.\""
"He lets that hang in the air for a while."
m "\"And I mean that genuinely.\""
cl "\"I'm glad.\""
m "\"I don't get a whole lot of opportunities to be genuine.\""
m "\"So there's something we definitely have in common.\""
"He chuckles, a bit forlorn."
cl "\"Too true.\""
m "\"I'll tell you what...\""
"His ears perk up and his eyes shine as he gives me his attention."
m "\"I'll stick this out until we get to the reservation.\""
"His entire posture straightens and he practically bounces up."
cl "\"Oh! Thank you, S—\""
play sound "sfx/monsterrage.ogg"
scene bg black with slow_dissolve
cl "\"W-what was that?!\""
scene bg forestnight with dis
play music "sfx/softwind.ogg"
play sound "sfx/samuel.ogg"
"Another roar sounds."
"Almost like a person, screaming."
play sound "sfx/monstersteps.ogg"
"But it isn't."
"Cliff clings to me. His fingers dig into my back."
"His breaths are short, shallow, and I catch the smell of peppermint."
show cli adv shocked at center,night
show expression AlphaMask("foliage", At("cli adv shocked", center)) as mask:
    alpha 0.35
with dis3
cl "\"Is — do you think it’s a predator?\""
"Can’t be. I heard footsteps."
"Heavy ones, just like the ones I heard that night Cliff was with me."
m "\"I don't reckon it is.\""
show jeb angry at right,night
show expression AlphaMask("foliage", At("jeb angry", right)) as mask2:
    alpha 0.35
with dis
"Jebediah crawls out of his tent, tossing his book behind him."
"He has a severe look on his face."
"Murdoch ain't too far behind, rubbing at his eyes with a dark paw."
mu "\"Did any of you hear—\"{w=0.2}{nw}"
"Jebediah hushes him."
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", center)) as mask:
    alpha 0.35
with dis
cl "\"You heard it as well?\""
"Jebediah nods with exasperation, holding a finger in front of his muzzle."
"He speaks, mouthing his words more than he whispers them."
show jeb doubt
show expression AlphaMask("foliage", At("jeb doubt", right)) as mask2:
    alpha 0.35
with dis
jeb "\"Douse the fire. The smoke will hide our scent.\""
show cli adv shocked
show expression AlphaMask("foliage", At("cli adv shocked", center)) as mask:
    alpha 0.35
with dis3
"Cliff looks at the horse, his brows twitching as if they can't decide on an emotion."
"They went from giddy, to concerned, to peaceful moments ago, but right now they're stuck somewhere between shock and tears."
"It's like he's seizing up."
cl "\"But—\""
"Jebediah frowns."
show jeb angry talking
show expression AlphaMask("foliage", At("jeb angry talking", right)) as mask2:
    alpha 0.35
with dis
jeb "\"{i}Douse the fire{/i}.\""
hide mask
hide cli
with dissolve
hide jeb
hide mask2
with dissolve
"I wrest myself free from Cliff, knocking him onto the forest floor."
"I struggle, clambering for the bucket of water we filled up earlier."
stop background fadeout 2.0
play sound "sfx/bucketsplash.ogg"
"The fire hisses and sputters as I empty its contents."
scene bg black with dis
"The wood smolders for a second."
play background "music/bedhorror.ogg" fadein 2.0
"Darkness and smoke follow."
"I drop the bucket."
"A splash of water hits my paw."
play sound "sfx/circling.ogg"
"Something rustles through the bushes."
"One moment it’s on one side, the next on the other side."
jeb "\"{i}Do not move a muscle.{/i}\""
"His voice is barely a whisper."
"The smoke’s damn near suffocating me and I'm struggling not to cough as my eyes tear up."
"I can’t see or hear Cliff, or Jebediah, or Murdoch."
"But whatever it is, whatever’s out there, I can hear it breathe."
"It's rasping like a dying man."
stop background fadeout 5.0
"My eyes sting and my throat burns."
"I've got to get out of this smoke."
"Leaves crunch under my paws."
play sound "sfx/snap.ogg"
play background "music/tension.ogg" fadein 2.0
"The snap of a twig sounds loud as thunder."
play sound "sfx/monstersprint.ogg"
"I can hear something sprint towards me."
"Red eyes shimmer in the dark."
"I can't make out its shape, but I remember that scent clear as day."
"The dirty gray fur."
"I bare my claws, putting myself between it and the others."
"I'm running on pure instinct now."
"I can only hope the others are still behind me."
"It grazes me, knocking me off-balance."
play sound "sfx/thud5.ogg"
"I can hear Cliff screaming before my head hits the ground hard."
"Pain surges through my entire body, and I grit my teeth just to stay awake."
"My vision is blurry. I see red, but I don't know if it's Murdoch's fur or the dying embers of the fire."
"I reach out to it, only for another scream to sound out, followed by utter chaos."
play sound "sfx/gore.ogg"
"Then flesh is torn."
queue sound "sfx/bonebreak.ogg"
"Bones break."
queue sound "sfx/bray2.ogg"
"I hear a donkey bray, followed by the clopping of its hooves."
queue sound "sfx/scrape.ogg"
"Something scrapes over the ground next to me."
"It's a dreadful sound."
"I sniff the air, catching a metallic scent."
"Blood. Fresh blood."
"I crack an eye open."
scene bg donkey with dissolve
play sound "sfx/bray1.ogg"
"Immediately, I wish I'd kept it closed."
"A donkey's face is staring straight at me, twisted in an unearthly way."
"Lifeless, almost, were it not for its still moving eye."
"Its body is a few yards behind it, contorted and broken."
scene bg forestnight with dis
"I look away just as the head is scraped further over the ground, rolling onto my other side."
"What the hell could do something like this so quickly?"
"The soil underneath me is warm and damp."
"It sticks to my shirt, coloring it shades of pink and red."
"I can see the streaks on my arm even in the dark."
"My arms go limp."
"I can't lift them."
stop background fadeout 4.0
"The last bits of strength I have drain from my body, and darkness takes me."
stop music fadeout 5.0
"My last words are a prayer. My last thoughts are of Hell."
"Of Hell, and of Echo."
scene bg black with slow_dissolve
"???" "\"Don't think you get to go softly.\""
"There's something tied around my neck. Thick, heavy, coarse."
"???" "\"You don't deserve to go softly. Not after what you did.\""
"The voice is right in my ear."
play background "sfx/crowd.ogg" fadein 8.0
"It's barely audible over the noise of..."
"...a crowd?"
scene bg burlap with dissolve
"There's cloth covering my eyes. I can see the pattern on it when I open them."
"I try raising my hands to take it off, but they're bound behind my back."
"The rope chafes against my fur and digs into my skin."
"The more I struggle, the more it hurts."
play music "music/mellowpiano.ogg" fadein 2.0
m "\"W-William? Is that you?\""
wi "\"There's no slipping out of this one.\""
"I hear footsteps on wood."
wi "\"Murder is a serious crime, Sam.\""
m "\"I didn't mean to, I swear it! He tricked me!\""
wi "\"You've only got yourself to blame.\""
"I can barely hear his voice as it's overpowered by the chanting of the crowd."
"All shouting for my head."
m "\"You've got to believe me, I didn't... didn't... he attacked me...\""
"I hang my head. The blindfold's getting damp."
"I can't even hear myself cry."
stop background fadeout 5.0
m "\"Please, William.\""
m "\"Please!\""
wi "\"But Sam, isn't this what you wanted?\""
wi "\"All this time, you've been running away.\""
"The voice grows colder, more distant. It shifts in tone, shifts in pitch."
"Like some sort of strange machine."
play background "sfx/radiotuning.ogg" fadein 4.0
md "\"From your home. From your state.\""
ja "\"From the mines.\""
cl "\"You've used people.\""
ni "\"Left people behind.\""
cy "\"And now you're running from Echo.\""
mu "\"Where's that gotten you?\""
m "\"I...\""
wi "\"Right here.\""
wi "\"{cps=20}At {nw}"
nwi1 "\"{cps=0}At {/cps}{cps=20}the {nw}"
wi "\"{i}{cps=0}At the {/cps}{cps=20}end {nw}"
nwi2 "{font=sin.ttf}\"{cps=0}At the end {/cps}{cps=20}of {nw}"
nwi3 "\"{cps=0}At the end of {/cps}{cps=20}my {nw}"
wi "\"{cps=0}At the end of my {/cps}{cps=20}rope.\""
stop background fadeout 1.5
"The voice is William's again, but it isn't him."
"It's far darker, dripping with hatred."
wi "\"Isn't this what you wanted, Sam?\""
"My chin is tipped up by a paw."
"I can feel something's hot breath on me."
"It reeks."
wi "\"To finally stop running?\""
wi "\"To stop going in circles?\""
"The wood underneath me creaks."
$ renpy.music.set_volume(0.3, delay=4.0, channel='music')
wi "\"All it takes is a pull of the lever.\""
"A laugh."
wi "\"It won’t hurt a bit.\""
wi "\"Unless you keep struggling.\""
"Something clicks."
wi "\"Any last words?\""
m "\"Please, don't—\""
stop music fadeout 2.0
wi "\"Goodbye, Sam.\""
"The floor gives way under me."
play sound "sfx/hanging.ogg"
$ renpy.music.set_volume(1.0, channel='music')
scene bg black
"The fall's an eternity compressed into a single second."
"Then the rope pulls taut."
"Something snaps."
"The sensation of falling stops."
stop sound fadeout 1.0
stop background fadeout 1.0
scene bg forestnight with dis
play music "music/forestambience.ogg" fadein 2.5
play background "sfx/bonfire.ogg"
"I'm in a sitting position, half-covered by a thin wool blanket."
"I cup my cheek in my paw. It's freezing, but I welcome any kind of feeling right now."
"Even the dull throb hammering away at the back of my head."
"I'm alive."
"My heart's pounding in my chest, but I'm alive."
"I recline again."
"The sky above me is a dark blue, barely visible from underneath the dense treeline."
"I reckon the sun's about to rise."
"I rub at my eyes, sniffing the air for any sign of the others."
"I catch a faint whiff of smoke and mint."
cl "\"You’re awake! Oh my goodness!\""
"I never thought I'd so be glad to hear Cliff speak."
"I look in the direction the voice came from. Sure enough, there's Cliff, Murdoch, and Jebediah, sitting around a smoldering campfire."
"It's a lot more modest than the one we made together."
"There's no sign of the supplies or tents."
"Did we move?"
"Cliff crawls over to me."
show cli adv shocked at center, night
show expression AlphaMask("foliage", At("cli adv shocked", center)) as mask:
    alpha 0.35
with dissolve
"His watery eyes get even wetter."
"He lets out a delighted squeak before turning."
play music2 "music/long-nights.ogg" fadeout 2.0
show cli adv happy
show expression AlphaMask("foliage", At("cli adv happy", center)) as mask:
    alpha 0.35
with dis3
cl "\"He’s awake!\""
"Murdoch follows - though rather than crawling over, he just walks."
"Jebediah stays put, not even glancing in my direction."
"He reaches for a flask. I can smell the alcohol from here."
show mur smile at right,night
show expression AlphaMask("foliage", At("mur smile", right)) as mask2:
    alpha 0.35
with dissolve
show mur talking
show expression AlphaMask("foliage", At("mur talking", right)) as mask2:
    alpha 0.35
with dis
mu "\"Well, I'll be.\""
show mur smile
show expression AlphaMask("foliage", At("mur smile", right)) as mask2:
    alpha 0.35
with dis1
show mur talking
show expression AlphaMask("foliage", At("mur talking", right)) as mask2:
    alpha 0.35
with dis
mu "\"How are you feeling, Sam?\""
show mur smile
show expression AlphaMask("foliage", At("mur smile", right)) as mask2:
    alpha 0.35
with dis
"It takes me a second to process that question."
"I'm feeling a lot of things right now."
"I scratch behind my ears."
m "\"Like I just wrangled a bear and lost.\""
show mur mischief
show expression AlphaMask("foliage", At("mur mischief", right)) as mask2:
    alpha 0.35
with dis
"He grins."
"No hidden meaning behind it this time."
mu "\"Not too far from the truth.\""
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", center)) as mask:
    alpha 0.35
with dis
cl "\"We thought you weren't going to make it.\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", center)) as mask:
    alpha 0.35
with dis
show mur concerned d
show expression AlphaMask("foliage", At("mur concerned d", right)) as mask2:
    alpha 0.35
with dis3
mu "\"You hit your head pretty hard.\""
m "\"What happened?\""
show cli adv sad
show expression AlphaMask("foliage", At("cli adv sad", center)) as mask:
    alpha 0.35
with dis3
cl "\"W-well, o-o-our camp was attacked by some manner...\""
"He swallows."
cl "\"...some manner of beast.\""
"His voice and the way he's trembling is making my head hurt."
m "\"Calm down, calm down.\""
show cli adv eyes
show expression AlphaMask("foliage", At("cli adv eyes", center)) as mask:
    alpha 0.35
with dis3
"He draws in a deep breath."
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", center)) as mask:
    alpha 0.35
with dis
cl "\"It tore through our tents and supplies as though they were made of paper.\""
cl "\"We managed to get to safety, but...\""
show mur sad
show expression AlphaMask("foliage", At("mur sad", right)) as mask2:
    alpha 0.35
with dis3
mu "\"It was either you or the supplies.\""
show cli adv blush eyes right
show expression AlphaMask("foliage", At("cli adv blush eyes right", center)) as mask:
    alpha 0.35
with dis
cl "\"I couldn't... {i}we{/i} couldn't risk losing you.\""
show cli adv blush eyes closed
show expression AlphaMask("foliage", At("cli adv blush eyes closed", center)) as mask:
    alpha 0.35
with dis
"He puts his paw on mine, then retracts it quickly."
show cli adv shocked
show expression AlphaMask("foliage", At("cli adv shocked", center)) as mask:
    alpha 0.35
with dis3
cl "\"You're cold.\""
show cli adv happy
show expression AlphaMask("foliage", At("cli adv happy", center)) as mask:
    alpha 0.35
with dis3
"Taking the corners of the blanket, he drapes it over me again."
"I warm up almost immediately."
m "\"I'm sorry.\""
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", center)) as mask:
    alpha 0.35
with dis3
cl "\"I'm just glad you're alive. Cold is better than dead, at any rate.\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", center)) as mask:
    alpha 0.35
with dis3
show mur talking
show expression AlphaMask("foliage", At("mur talking", right)) as mask2:
    alpha 0.35
with dis3
mu "\"You're lucky Cliff knew how to administer first aid.\""
show mur
show expression AlphaMask("foliage", At("mur", right)) as mask2:
    alpha 0.35
with dis3
"The weasel scratches the back of his head."
show cli adv blush eyes closed
show expression AlphaMask("foliage", At("cli adv blush eyes closed", center)) as mask:
    alpha 0.35
with dis
cl "\"Well I still would have tried, even if I didn't!\""
m "\"So what now?\""
show jeb at left,night behind cli
show expression AlphaMask("foliage", At("jeb", left)) behind cli as mask3:
    alpha 0.35
with dissolve
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", left)) as mask3:
    alpha 0.35
with dis
jeb "\"We wait until the sun's up.\""
show jeb
show expression AlphaMask("foliage", At("jeb", left)) as mask3:
    alpha 0.35
with dis1
show cli adv shocked
show expression AlphaMask("foliage", At("cli adv shocked", center)) as mask:
    alpha 0.35
with dis3
"The horse takes a swig from his flask."
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", left)) as mask3:
    alpha 0.35
with dis
jeb "\"Then, we go back.\""
show jeb
show expression AlphaMask("foliage", At("jeb", left)) as mask3:
    alpha 0.35
with dis
m "\"Back?\""
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", center)) as mask:
    alpha 0.35
with dis3
"He gets to his feet."
show jeb doubt talking
show expression AlphaMask("foliage", At("jeb doubt talking", left)) as mask3:
    alpha 0.35
with dis
jeb "\"We're slow without donkeys, but we're dead without the supplies.\""
show jeb doubt
show expression AlphaMask("foliage", At("jeb doubt", left)) as mask3:
    alpha 0.35
with dis
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", center)) as mask:
    alpha 0.35
with dis
cl "\"Is it even safe to go back?\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", center)) as mask:
    alpha 0.35
with dis
show mur concerned d
show expression AlphaMask("foliage", At("mur concerned d", right)) as mask2:
    alpha 0.35
with dis
mu "\"Sam still needs time to heal.\""
show jeb
show expression AlphaMask("foliage", At("jeb", left)) as mask3:
    alpha 0.35
with dis
m "\"I'm alright.\""
"I roll my shoulders and hear something crack."
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", center)) as mask:
    alpha 0.35
with dis
cl "\"Are you sure?\""
m "\"Fit as a fiddle.\""
show cli adv talking
show expression AlphaMask("foliage", At("cli adv doubt", center)) as mask:
    alpha 0.35
with dis
cl "\"We don't want your wounds getting infected. Even scrapes can fester and kill you out in the wilderness.\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", center)) as mask:
    alpha 0.35
with dis
"I wave them off."
m "\"I've had worse.\""
show mur
show expression AlphaMask("foliage", At("mur", right)) as mask2:
    alpha 0.35
with dis3
show cli adv happy
show expression AlphaMask("foliage", At("cli adv happy", center)) as mask:
    alpha 0.35
with dis3
cl "\"I should have some laudanum in my satchel.\""
m "\"Lauda-what?\""
"I don't need to hear complicated words right now, and this headache isn't making it any easier."
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", center)) as mask:
    alpha 0.35
with dis3
cl "\"Something for the pain.\""
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", center)) as mask:
    alpha 0.35
with dis
"He frowns."
cl "\"But my satchel's with the other supplies...\""
mu "\"I suppose we don't have much of a choice, then.\""
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", center)) as mask:
    alpha 0.35
with dis
cl "\"I do at least have some water in my pack.\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", center)) as mask:
    alpha 0.35
with dis1
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", center)) as mask:
    alpha 0.35
with dis
cl "\"It's not much, but we can fill up our flasks once we find the stream again.\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", center)) as mask:
    alpha 0.35
with dis
show mur concerned d
show expression AlphaMask("foliage", At("mur concerned d", right)) as mask2:
    alpha 0.35
with dis
mu "\"Can you stand, Sam?\""
stop music2 fadeout 5.0
m "\"Can try.\""
"I brace myself against the ground and push myself up."
"I'm sore all over."
"There's some scratches and scabs on my arm."
show cli adv sad
show expression AlphaMask("foliage", At("cli adv sad", center)) as mask:
    alpha 0.35
with dis3
"Cliff watches me with a pained expression, paws balled into fists."
"It takes me a moment, and even when I'm on my feet I don't feel all that stable."
"But at least I'm standing."
"I try walking next."
"The ground's uneven, and the dirt shifts underneath my paws. Every step's a gamble."
"But it doesn't hurt."
m "\"Think I'll be okay.\""
show mur talking
show expression AlphaMask("foliage", At("mur talking", right)) as mask2:
    alpha 0.35
with dis3
mu "\"You can lean on me.\""
show mur smile
show expression AlphaMask("foliage", At("mur smile", right)) as mask2:
    alpha 0.35
with dis
"He smiles a bit and looks away."
m "\"Thanks.\""
show mur talking
show expression AlphaMask("foliage", At("mur talking", right)) as mask2:
    alpha 0.35
with dis
mu "\"Don't mention it!\""
show mur mischief
show expression AlphaMask("foliage", At("mur mischief", right)) as mask2:
    alpha 0.35
with dis
mu "\"But the next time you decide to jump in front of some large creature, do tell me first.\""
mu "\"You might be used to taking a pounding, but my spine sure isn't.\""
mu "\"I've carried plenty of crates and none are as heavy as you.\""
stop background fadeout 2.0
stop music fadeout 4.0
scene bg black with slow_dissolve
scene bg forestmorning with slow_dissolve
play background "music/forestambience.ogg" fadein 4.0
"We start heading out when the sun comes up."
"It's still cool out, and the woods are still dead silent."
"There's less small talk."
"In fact, barely anyone's saying a word."
"Cliff's eyes never leave me, and Murdoch stays close to pick me up when I stumble."
"Once I'm used to being on my feet again, we pick up the pace just a little."
"Jebediah, for once, isn't walking in front."
"He doesn't make eye contact when I look over my shoulder."
m "\"You carried me this far?\""
show mur mischief at center,forest
show expression AlphaMask("foliage", At("mur mischief", center)) as mask:
    alpha 0.35
with dissolve
"Murdoch chuckles."
show mur talking
show expression AlphaMask("foliage", At("mur talking", center)) as mask:
    alpha 0.35
with dis
mu "\"It was a group effort. You're pretty heavy, you know that?\""
show mur
show expression AlphaMask("foliage", At("mur", center)) as mask:
    alpha 0.35
with dis
"I tilt my head."
m "\"And that thing didn't follow you?\""
show mur talking
show expression AlphaMask("foliage", At("mur talking", center)) as mask:
    alpha 0.35
with dis
mu "\"No. It—\""
"He looks back at Jebediah, then lowers his voice."
show mur sad
show expression AlphaMask("foliage", At("mur sad", center)) as mask:
    alpha 0.35
with dis3
mu "\"After it took you down, it chased one of the donkeys deeper into the woods.\""
"He winces."
show mur fear d
show expression AlphaMask("foliage", At("mur fear d", center)) as mask:
    alpha 0.35
with dis
mu "\"Took its head clean off.\""
m "\"And the other donkey?\""
show mur concerned d
show expression AlphaMask("foliage", At("mur concerned d", center)) as mask:
    alpha 0.35
with dis
mu "\"Ran away.\""
mu "\"It wasn't a pretty sight.\""
"He pauses, tapping his chin."
show mur eyes talking
show expression AlphaMask("foliage", At("mur eyes talking", center)) as mask:
    alpha 0.35
with dis
mu "\"Kind of strange, come to think of it.\""
show mur concerned d
show expression AlphaMask("foliage", At("mur concerned d", center)) as mask:
    alpha 0.35
with dis
mu "\"It could've killed us all pretty easily.\""
mu "\"So why didn't it?\""
m "\"Maybe it was just lookin' for a quick meal.\""
"He shrugs."
show mur talking
show expression AlphaMask("foliage", At("mur talking", center)) as mask:
    alpha 0.35
with dis
mu "\"Any of us would've sufficed.\""
mu "\"We've got more meat on our bones than those donkeys combined.\""
show mur
show expression AlphaMask("foliage", At("mur", center)) as mask:
    alpha 0.35
with dis
m "\"Did you {i}want{/i} to die?\""
show mur concerned d
show expression AlphaMask("foliage", At("mur concerned d", center)) as mask:
    alpha 0.35
with dis
mu "\"Not in this particular way, no.\""
show mur talking
show expression AlphaMask("foliage", At("mur talking", center)) as mask:
    alpha 0.35
with dis3
mu "\"I'm just happy my equipment survived the ordeal.\""
show mur
show expression AlphaMask("foliage", At("mur", center)) as mask:
    alpha 0.35
with dis1
show cli adv talking at right,forest
show expression AlphaMask("foliage", At("cli adv talking", right)) as mask2:
    alpha 0.35
with dis3
cl "\"Perhaps the creature meant to frighten us.\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", right)) as mask2:
    alpha 0.35
with dis
m "\"You think so?\""
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", right)) as mask2:
    alpha 0.35
with dis
cl "\"As Murdoch said, if it meant to kill us, it had ample time and strength to do so.\""
show cli adv eyes
show expression AlphaMask("foliage", At("cli adv eyes", right)) as mask2:
    alpha 0.35
with dis1
show cli adv eyes talking
show expression AlphaMask("foliage", At("cli adv eyes talking", right)) as mask2:
    alpha 0.35
with dis
cl "\"It's just a thought, of course.\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", right)) as mask2:
    alpha 0.35
with dis1
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", right)) as mask2:
    alpha 0.35
with dis
cl "\"I've not heard about any stories or urban legends regarding ratlike monsters in the region.\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", right)) as mask2:
    alpha 0.35
with dis
show mur fear d
show expression AlphaMask("foliage", At("mur fear d", center)) as mask:
    alpha 0.35
with dis
mu "\"It wasn't a rat, though.\""
show cli adv shocked
show expression AlphaMask("foliage", At("cli adv shocked", right)) as mask2:
    alpha 0.35
with dis3
cl "\"It was! I saw it!\""
show mur concerned d
show expression AlphaMask("foliage", At("mur concerned d", center)) as mask:
    alpha 0.35
with dis
mu "\"It was more fox-like.\""
mu "\"...A feral one, obviously, not like me.\""
mu "\"But big.\""
mu "\"Did you see anything, Sam?\""
"I try and remember what I saw, but I just end up drawing blanks."
"All I can remember is that nightmare, and I'd rather not think about that again."
m "\"I got knocked out before I could get a good look at it.\""
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", right)) as mask2:
    alpha 0.35
with dis3
cl "\"Strange.\""
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", right)) as mask2:
    alpha 0.35
with dis
cl "\"If we hadn't almost gotten ourselves killed, I would've said it bears investigating.\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", right)) as mask2:
    alpha 0.35
with dis1
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", right)) as mask2:
    alpha 0.35
with dis
cl "\"Perhaps the Meseta will know more.\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", right)) as mask2:
    alpha 0.35
with dis
m "\"Do you know anything, Jebediah?\""
show jeb doubt talking at left,forest
show expression AlphaMask("foliage", At("jeb doubt talking", left)) as mask3:
    alpha 0.35
with dis3
jeb "\"It didn't eat.\""
show jeb doubt
show expression AlphaMask("foliage", At("jeb doubt", left)) as mask3:
    alpha 0.35
with dis3
"His tone's surprisingly biting."
show cli adv doubt with dis
cl "\"What do you mean, it didn't eat?\""
show jeb doubt talking
show expression AlphaMask("foliage", At("jeb doubt talking", left)) as mask3:
    alpha 0.35
with dis3
jeb "\"I mean my jenny was torn to pieces and there weren't any chomps missin'.\""
show jeb angry
show expression AlphaMask("foliage", At("jeb angry", left)) as mask3:
    alpha 0.35
with dis1
show jeb angry talking
show expression AlphaMask("foliage", At("jeb angry talking", left)) as mask3:
    alpha 0.35
with dis
jeb "\"Hungry predators don't act like that.\""
show jeb angry
show expression AlphaMask("foliage", At("jeb angry", left)) as mask3:
    alpha 0.35
with dis
show cli adv sad
show expression AlphaMask("foliage", At("cli adv sad", right)) as mask2:
    alpha 0.35
with dis3
cl "\"There goes that hypothesis, then.\""
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", right)) as mask2:
    alpha 0.35
with dis3
cl "\"Alright, then.\""
cl "\"If you know anything else, let's hear it.\""
show jeb doubt talking
show expression AlphaMask("foliage", At("jeb doubt talking", left)) as mask3:
    alpha 0.35
with dis3
jeb "\"If there's anything to know, I'll let you know.\""
show jeb doubt
show expression AlphaMask("foliage", At("jeb doubt", left)) as mask3:
    alpha 0.35
with dis1
hide jeb
hide mask3
with dis3
"Cliff gives him a look as he walks off."
"Murdoch looks behind him."



"I yawn."
"I must've been out all night, and yet I'm exhausted all the same."
m "\"Are we going the right way?\""
show cli adv happy
show expression AlphaMask("foliage", At("cli adv happy", right)) as mask2:
    alpha 0.35
with dis3
cl "\"We should be. Look.\""
"He points to a large tree on the side of the path. An X is etched into the bark."
"No doubt marked by claws."
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", right)) as mask2:
    alpha 0.35
with dis3
cl "\"We marked some trees on the way so we wouldn't get lost.\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", right)) as mask2:
    alpha 0.35
with dis
m "\"Jebediah tell you to do that?\""
"Murdoch whispers again."
show mur talking
show expression AlphaMask("foliage", At("mur talking", center)) as mask:
    alpha 0.35
with dis
mu "\"It was Cliff's idea, actually.\""
show mur
show expression AlphaMask("foliage", At("mur", center)) as mask:
    alpha 0.35
with dis
"I raise a brow."
show mur fear d
show expression AlphaMask("foliage", At("mur fear d", center)) as mask:
    alpha 0.35
with dis
mu "\"Jebediah's been quiet ever since last night. Even for him.\""
m "\"Can you blame him?\""
m "\"Losing two pack animals at once is kind of a disaster.\""
show mur concerned d
show expression AlphaMask("foliage", At("mur concerned d", center)) as mask:
    alpha 0.35
with dis
mu "\"Yeah. I could tell he had an emotional attachment to them, too.\""
mu "\"Every man mourns in his own way.\""
"Somehow, that makes me wonder if anyone's out there mourning or even looking for Jack."
"He must've had somebody."
"Someone who cared for him despite everything he did."
"It sure as hell was never going to be me."
show mur fear d
show expression AlphaMask("foliage", At("mur fear d", center)) as mask:
    alpha 0.35
with dis
mu "\"But we still need his help or else things are going to get bad.\""
mu "\"Jebediah is our compass in these woods. We're like headless chickens without him.\""
show jeb doubt talking at left,forest
show expression AlphaMask("foliage", At("jeb doubt talking", left)) as mask3:
    alpha 0.35
with dis3
jeb "\"I got ears, you know.\""
show jeb doubt at left,forest
show expression AlphaMask("foliage", At("jeb doubt", left)) as mask3:
    alpha 0.35
show cli adv shocked
show expression AlphaMask("foliage", At("cli adv shocked", right)) as mask2:
    alpha 0.35
show mur sad
show expression AlphaMask("foliage", At("mur sad", center)) as mask:
    alpha 0.35
with dis3
"Murdoch seems to realize what he's said, ears pinned to his head."
mu "\"Terribly sorry.\""
mu "\"I'm just thinking aloud and it's not helping.\""
hide jeb
hide cli
hide mur
hide mask
hide mask2
hide mask3
with dis3
"Jebediah passes us."
"His eyes are unfocused, and he smells like he's soaked in whiskey."
m "\"Are you okay?\""
"He certainly doesn’t look it."
"I don't think he's in much of a state to lead anyone right now."
jeb "\"We're gettin' close. Any minute now.\""
"We reach a fork in the path. Jebediah takes a step forward, staggering."
"His mane is messy."
"The difference between him now and yesterday is like night and day."
"Cliff's already passed him, walking over to one of the trees on the left side and running his fingers up the bark."
show cli adv doubt at center,forest
show expression AlphaMask("foliage", At("cli adv doubt", center)) as mask2:
    alpha 0.35
with dis3
cl "\"Strange.\""
show cli adv shocked
show expression AlphaMask("foliage", At("cli adv shocked", center)) as mask2:
    alpha 0.35
with dis3
cl "\"This doesn't make sense.\""
play music "music/contemplation.ogg" fadein 2.0
cl "\"These trees should be marked.\""
"He eyes Murdoch."
show mur fear d at right,forest
show expression AlphaMask("foliage", At("mur fear d", right)) as mask:
    alpha 0.35
with dis3
mu "\"I marked them, alright. Don't think I'd forget.\""
"He laughs uncomfortably."
mu "\"Damn near ripped a claw or two off doing it, too.\""
show jeb angry at left,forest
show expression AlphaMask("foliage", At("jeb angry", left)) as mask3:
    alpha 0.35
with dis3
"Jebediah sighs, rubbing his temples."
show jeb angry talking
show expression AlphaMask("foliage", At("jeb talking", left)) as mask3:
    alpha 0.35
with dis
jeb "\"We don't have time for this shit.\""
show jeb angry at left,forest
show expression AlphaMask("foliage", At("jeb angry", left)) as mask3:
    alpha 0.35
with dis1
hide jeb
hide cli
hide mur
hide mask
hide mask2
hide mask3
with dissolve
$ renpy.music.set_volume(0.1, delay=15.0, channel='background')
play music "music/refraction.ogg" fadeout 3.0
scene bg forestmorning2 with dissolve
"He heads down the path to the left, and motions for us to follow."
"In spite of the sun rising, it isn't getting any brighter."
"The foliage is getting thicker, blocking out more and more of the morning sun."
"It's as though it never rose in the first place."
"Even the local wildlife's getting quieter the deeper we go."
"Before long, we get to another fork in the road."
"This time, we go right, passing a large rock."
"There are no marks on the trees in front of us."
"When I ask Jebediah, he insists we're going the right way."
"So we keep walking down winding paths."
"Bushes and weeds have completely overtaken some of them."
"Even for a forest, it feels abandoned, lost, as if we shouldn't be here."
"What happened last night only makes the feeling that much worse."
"We're hungry and tired."
"Our clothes are covered in stains and dust."
"The slightest noises have us looking around in a panic."
"I hate to say it, but I almost wish I was back in Echo."
"I'm starting to miss Will, and Nik."
"And Cynthia too."
"Wonder how she's doing right about now."
"What she'd say if she saw me here."
"What she'd say if she knew I'd been planning to run."
"Maybe she already knew."
"Wonder if Nik would look at me the way he looked when he saw me bloody that morning."
"The voices from my dream are still whispering in my ear."
"And part of me is starting to think they were right."
stop music fadeout 10.0
scene bg black with dissolve
scene bg forestmorning2 with dissolve
$ renpy.music.set_volume(0.4, delay=8.0, channel='background')
"We decide to take a little break after a while."
"It's getting warmer, but not any brighter."
"We've just about emptied Cliff's flask of water when the weasel speaks up."
show cli adv talking at left,forestdark
show expression AlphaMask("foliage", At("cli adv talking", left)) as mask2:
    alpha 0.45
with dis3
cl "\"We need to head back.\""
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv talking", left)) as mask2:
    alpha 0.45
with dis
cl "\"I hate to say it, Jebediah, but we're lost.\""
show jeb angry at right,forestdark
show expression AlphaMask("foliage", At("jeb angry", right)) as mask3:
    alpha 0.45
with dis3
"Jebediah furrows his brow and purses his lips."
show jeb angry talking
show expression AlphaMask("foliage", At("jeb angry talking", right)) as mask3:
    alpha 0.45
with dis
jeb "\"We can't be lost. It was this way.\""
show jeb angry
show expression AlphaMask("foliage", At("jeb angry", right)) as mask3:
    alpha 0.45
with dis
show cli adv sad
show expression AlphaMask("foliage", At("cli adv sad", left)) as mask2:
    alpha 0.45
with dis3
cl "\"We've been walking for over an hour now.\""
cl "\"I don't think we're any closer than when we started.\""
"The horse takes a step in the weasel's direction."
show jeb angry talking
show expression AlphaMask("foliage", At("jeb angry talking", right)) as mask3:
    alpha 0.45
with dis
jeb "\"I {i}know{/i} this forest—\""
show jeb angry
show expression AlphaMask("foliage", At("jeb angry", right)) as mask3:
    alpha 0.45
with dis
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
    alpha 0.45
with dis3
cl "\"Clearly not as well as you think you do.\""
play music "music/contemplation.ogg" fadein 2.0
show cli adv angry
show expression AlphaMask("foliage", At("cli adv angry", left)) as mask2:
    alpha 0.45
with dis
cl "\"What am I even paying you for?\""
show jeb angry talking
show expression AlphaMask("foliage", At("jeb angry talking", right)) as mask3:
    alpha 0.45
with dis
jeb "\"Think you can do better?\""
show jeb angry
show expression AlphaMask("foliage", At("jeb angry", right)) as mask3:
    alpha 0.45
with dis
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
    alpha 0.45
with dis
cl "\"I know so.\""
"Cliff takes a step towards Jebediah."
"This got ugly fast."
show jeb doubt talking
show expression AlphaMask("foliage", At("jeb doubt talking", right)) as mask3:
    alpha 0.45
with dis
jeb "\"Then by all means, lead the way.\""
show jeb doubt
show expression AlphaMask("foliage", At("jeb doubt", right)) as mask3:
    alpha 0.45
with dis
show cli adv angry
show expression AlphaMask("foliage", At("cli adv angry", left)) as mask2:
    alpha 0.45
with dis
cl "\"At the very least I can do so without getting ourselves killed.\""
show jeb angry talking
show expression AlphaMask("foliage", At("jeb angry talking", right)) as mask3:
    alpha 0.45
with dis
jeb "\"Excuse me?\""
show jeb angry
show expression AlphaMask("foliage", At("jeb angry", right)) as mask3:
    alpha 0.45
with dis
"The paw holding his flask is shaking."
"Cliff looks at it, and I see his nose twitching."
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
    alpha 0.45
with dis
cl "\"Is that alcohol?\""
show jeb angry talking
show expression AlphaMask("foliage", At("jeb angry talking", right)) as mask3:
    alpha 0.45
with dis
jeb "\"Leave me alone.\""
show jeb angry
show expression AlphaMask("foliage", At("jeb angry", right)) as mask3:
    alpha 0.45
with dis
cl "\"Have you been drinking all this time?\""
"He sighs."
cl "\"Hand me the flask, Jebediah.\""
"The horse grits his teeth."
cl "\"Hand. Me. The. Flask.\""
"Murdoch gets off the rock he's sitting on and steps in between the two, holding up a paw."
show mur angry at center,forestdark
show expression AlphaMask("foliage", At("mur angry", center)) as mask:
    alpha 0.45
with dis3
show cli adv shocked
show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
    alpha 0.45
with dis3
mu "\"Calm down, the both of you.\""
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
    alpha 0.45
with dis
mu "\"Fighting won't get us out of this damn mess.\""
show mur concerned d
show expression AlphaMask("foliage", At("mur concerned d", center)) as mask:
    alpha 0.45
with dis
mu "\"Jebediah, give me the flask.\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", right)) as mask3:
    alpha 0.45
with dis
"The horse grunts."
"He hesitates."
"He finally hands it over."
show mur eyes talking
show expression AlphaMask("foliage", At("mur eyes talking", center)) as mask:
    alpha 0.45
with dis
"Murdoch takes a sip of the flask and then hands it back to Jeb."
show cli adv shocked
show expression AlphaMask("foliage", At("cli adv shocked", left)) as mask2:
    alpha 0.45
with dis3
cl "\"What are you doing?!\""
show mur talking
show expression AlphaMask("foliage", At("mur talking", center)) as mask:
    alpha 0.45
with dis
mu "\"Calming myself.\""
show mur smile
show expression AlphaMask("foliage", At("mur smile", center)) as mask:
    alpha 0.45
with dis1
stop music fadeout 3.0
$ renpy.music.set_volume(1.0, delay=5.0, channel='background')
show mur talking
show expression AlphaMask("foliage", At("mur talking", center)) as mask:
    alpha 0.45
with dis
mu "\"Now, instead of wasting energy on yelling, let's use it on scouting attempts.\""
show mur smile
show expression AlphaMask("foliage", At("mur smile", center)) as mask:
    alpha 0.45
with dis
show jeb doubt talking
show expression AlphaMask("foliage", At("jeb doubt talking", right)) as mask3:
    alpha 0.45
with dis
jeb "\"I'm going to go take a piss.\""
show jeb doubt
show expression AlphaMask("foliage", At("jeb doubt", right)) as mask3:
    alpha 0.45
with dis1
show jeb doubt talking
show expression AlphaMask("foliage", At("jeb doubt talking", right)) as mask3:
    alpha 0.45
with dis
jeb "\"I'll see you all in ten minutes if you're still here.\""
show jeb doubt
show expression AlphaMask("foliage", At("jeb doubt", right)) as mask3:
    alpha 0.45
with dis1
hide jeb
hide mask3
with dis3
"The stallion trots off, staggering."

"Murdoch leans against a tree, watching him walk away."
show mur eyes
show expression AlphaMask("foliage", At("mur eyes", center)) as mask:
    alpha 0.45
with dis
mu "\"Okay.\""
show mur eyes talking
show expression AlphaMask("foliage", At("mur eyes talking", center)) as mask:
    alpha 0.45
with dis
mu "\"Listen.\""
show mur concerned d
show expression AlphaMask("foliage", At("mur concerned d", center)) as mask:
    alpha 0.45
with dis
mu "\"Despite all of the fun we were having when this expedition began, I think we have to face some facts.\""
mu "\"The four of us don't actually know each other very well.\""
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
    alpha 0.45
with dis
cl "\"Oh, come now—\""
show mur fear d
show expression AlphaMask("foliage", At("mur fear d", center)) as mask:
    alpha 0.45
with dis
mu "\"Let me finish, Mr. Tibbits.\""
show mur concerned d
show expression AlphaMask("foliage", At("mur concerned d", center)) as mask:
    alpha 0.45
with dis
mu "\"I've known you for less than a week, and Jeb for even less than that.\""
mu "\"I've known about Sam longer only through Mr. Adler's word.\""
show mur sideeye
show expression AlphaMask("foliage", At("mur sideeye", center)) as mask:
    alpha 0.45
with dis
cl "\"Oh, for heaven's sake.\""
show cli adv sad
show expression AlphaMask("foliage", At("cli adv sad", left)) as mask2:
    alpha 0.45
with dis3
cl "\"As if that man really knows anything about anybody.\""
show mur concerned d
show expression AlphaMask("foliage", At("mur concerned d", center)) as mask:
    alpha 0.45
with dis
mu "\"He knows people, and that's something I do trust based on my experience and time spent with him.\""
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
    alpha 0.45
with dis3
cl "\"So how any of this relevant?\""
show mur fear d
show expression AlphaMask("foliage", At("mur fear d", center)) as mask:
    alpha 0.45
with dis
mu "\"Because group survival odds increase when we trust each other.\""
show mur eyes talking
show expression AlphaMask("foliage", At("mur eyes talking", center)) as mask:
    alpha 0.45
with dis
mu "\"We really did almost die last night.\""
mu "\"Nobody's talking about it.\""
show mur concerned d
show expression AlphaMask("foliage", At("mur concerned d", center)) as mask:
    alpha 0.45
show cli adv sad
show expression AlphaMask("foliage", At("cli adv sad", left)) as mask2:
    alpha 0.45
with dis3
cl "\"Because we've been trying to press on.\""
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
    alpha 0.45
show mur sideeye
show expression AlphaMask("foliage", At("mur sideeye", center)) as mask:
    alpha 0.45
with dis3
mu "\"Then now's as good a time as any to just talk.\""
show mur talking
show expression AlphaMask("foliage", At("mur talking", center)) as mask:
    alpha 0.45
with dis
mu "\"No more secrets.\""
show mur smile
show expression AlphaMask("foliage", At("mur smile", center)) as mask:
    alpha 0.45
with dis
show cli adv eyes
show expression AlphaMask("foliage", At("cli adv eyes", left)) as mask2:
    alpha 0.45
with dis
"Cliff takes a deep breath."
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
    alpha 0.45
with dis
cl "\"Okay.\""
show cli adv sad
show expression AlphaMask("foliage", At("cli adv sad", left)) as mask2:
    alpha 0.45
with dis3
cl "\"I'll go first then.\""
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
    alpha 0.45
with dis3
cl "\"Everything I've said about myself has been true.\""
cl "\"This trip is a research endeavor.\""
cl "\"And though my time with everybody here has been brief, before the attack, it genuinely has been one of the best experiences of my life.\""
show cli adv happy
show expression AlphaMask("foliage", At("cli adv happy", left)) as mask2:
    alpha 0.45
with dis3
cl "\"I appreciate you both.\""
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
    alpha 0.45
with dis
cl "\"And Jeb too, even, though, I...\""
show cli adv sad
show expression AlphaMask("foliage", At("cli adv sad", left)) as mask2:
    alpha 0.45
with dis3
cl "\"I just said too much again.\""
show mur talking
show expression AlphaMask("foliage", At("mur talking", center)) as mask:
    alpha 0.45
with dis
mu "\"You're frustrated.\""
show mur smile
show expression AlphaMask("foliage", At("mur smile", center)) as mask:
    alpha 0.45
with dis1
show mur talking
show expression AlphaMask("foliage", At("mur talking", center)) as mask:
    alpha 0.45
with dis
mu "\"Reasonably so.\""
show mur fear d
show expression AlphaMask("foliage", At("mur fear d", center)) as mask:
    alpha 0.45
with dis
mu "\"I think I would be too if I wasn't so scared.\""
show mur smile
show expression AlphaMask("foliage", At("mur smile", center)) as mask:
    alpha 0.45
show cli adv eyes
show expression AlphaMask("foliage", At("cli adv eyes", left)) as mask2:
    alpha 0.45
with dis3
cl "\"That's not all.\""
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", left)) as mask2:
    alpha 0.45
with dis
cl "\"I'm, well...\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", left)) as mask2:
    alpha 0.45
with dis1
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", left)) as mask2:
    alpha 0.45
with dis
cl "\"I'd like to think I'm reinventing myself.\""
show cli adv happy
show expression AlphaMask("foliage", At("cli adv happy", left)) as mask2:
    alpha 0.45
with dis3
cl "\"This trip has already been something of a transformative experience for me, and I want to see it through to the end.\""
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
    alpha 0.45
with dis
cl "\"All the way through.\""
show cli adv eyes
show expression AlphaMask("foliage", At("cli adv eyes", left)) as mask2:
    alpha 0.45
with dis
cl "\"Whether anybody comes with me or not.\""
show mur talking
show expression AlphaMask("foliage", At("mur talking", center)) as mask:
    alpha 0.45
with dis
mu "\"We're already here, aren't we?\""
show mur smile
show expression AlphaMask("foliage", At("mur smile", center)) as mask:
    alpha 0.45
with dis
"The stoat looks at me."
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
    alpha 0.45
with dis
cl "\"And you, Sam?\""
"I shrug."
m "\"I already told you I'll go as far as the reservation at least.\""
"Murdoch's eyes narrow and he tilts his head."
show mur sideeye
show expression AlphaMask("foliage", At("mur sideeye", center)) as mask:
    alpha 0.45
with dis
mu "\"Just the reservation?\""
m "\"That's what I said.\""
if  MT_Points > 0:
    label MTconfession1:
    "I shift my weight and cross my arms as their eyes look over to me."
    m "\"Truth be told, I'm just trying to put as much distance between me and Echo as possible.\""
    show mur talking
    show expression AlphaMask("foliage", At("mur talking", center)) as mask:
        alpha 0.45
    with dis
    mu "\"But why?\""
    show mur smile
    show expression AlphaMask("foliage", At("mur smile", center)) as mask:
        alpha 0.45
    with dis
    m "\"I don't feel comfortable sharing that.\""
    m "\"I've probably already said too much, but the money and the ride are why I agreed to come at all.\""
    m "\"If you both really are serious about trust then that has to be enough for now.\""
    show cli adv happy
    show expression AlphaMask("foliage", At("cli adv happy", left)) as mask2:
        alpha 0.45
    with dis3
    cl "\"Of course.\""
    show mur talking
    show expression AlphaMask("foliage", At("mur talking", center)) as mask:
        alpha 0.45
    with dis
    mu "\"It's enough for me, too.\""
    show mur fear d
    show expression AlphaMask("foliage", At("mur fear d", center)) as mask:
        alpha 0.45
    with dis
    mu "\"I suppose it's my turn now, then.\""
    show cli adv doubt
    show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
        alpha 0.45
    with dis3
    "The fox pulls out something from his vest pocket."
    "He pulls forth a dainty cloth sachet tied with a string."
    show mur eyes talking
    show expression AlphaMask("foliage", At("mur eyes talking", center)) as mask:
        alpha 0.45
    with dis
    mu "\"I need this stuff to stay grounded.\""
    m "\"That's...\""
    cl "\"Oh.\""
    show mur fear d
    show expression AlphaMask("foliage", At("mur fear d", center)) as mask:
        alpha 0.45
    with dis
    mu "\"I think I have a month's supply here if I ration it out.\""
    show mur concerned d
    show expression AlphaMask("foliage", At("mur concerned d", center)) as mask:
        alpha 0.45
    with dis
    mu "\"If we're out here longer than that then I'll be in trouble.\""
    show mur shock
    show expression AlphaMask("foliage", At("mur shock", center)) as mask:
        alpha 0.45
    with dis
    mu "\"So trust me when I say nobody on this trip is as scared as me now.\""
    show mur eyes
    show expression AlphaMask("foliage", At("mur eyes", center)) as mask:
        alpha 0.45
    with dis
    show cli adv sad
    show expression AlphaMask("foliage", At("cli adv sad", left)) as mask2:
        alpha 0.45
    with dis3
    cl "\"I...\""
    show cli adv doubt
    show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
        alpha 0.45
    with dis3
    cl "\"I'll get us through the woods.\""
    show cli adv talking
    show expression AlphaMask("foliage", At("cli adv talking", left)) as mask2:
        alpha 0.45
    with dis
    cl "\"I promise.\""
    show cli adv doubt
    show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
        alpha 0.45
    with dis

else:
    m "\"You've been sending me the evil eye for most of this trip the moment you have an excuse to be suspicious of me, fox.\""
    mu "\"That's simply because you've been acting suspicious.\""
    show cli adv shocked
    show expression AlphaMask("foliage", At("cli adv shocked", left)) as mask2:
        alpha 0.45
    with dis
    cl "\"Murdoch!\""
    show cli adv doubt
    show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
        alpha 0.45
    with dis
    show mur fear d
    show expression AlphaMask("foliage", At("mur fear d", center)) as mask:
        alpha 0.45
    with dis
    mu "\"Now hold onto your reigns, gentlemen\""
    show mur sideeye
    show expression AlphaMask("foliage", At("mur sideeye", center)) as mask:
        alpha 0.45
    with dis
    mu "\"There's truth to my statement.\""
    m "\"Like hell there is.\""
    "My heart is racing."
    "Does he know?"
    show mur angry
    show expression AlphaMask("foliage", At("mur angry", center)) as mask:
        alpha 0.45
    with dis3
    mu "\"You're quick to lash out.\""
    mu "\"You're avoidant.\""
    mu "\"And you don't even want to entertain the idea that you have secrets.\""
    m "\"Because I don't.\""
    show mur sideeye
    show expression AlphaMask("foliage", At("mur sideeye", center)) as mask:
        alpha 0.45
    with dis3
    mu "\"Everybody has secrets.\""
    show cli adv sad
    show expression AlphaMask("foliage", At("cli adv sad", left)) as mask2:
        alpha 0.45
    with dis3
    cl "\"B-but Sam.\""
    show cli adv doubt
    show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
        alpha 0.45
    with dis3
    cl "\"Last night you told me—\""
    m "\"Stop.\""
    show mur concerned d
    show expression AlphaMask("foliage", At("mur concerned d", center)) as mask:
        alpha 0.45
    with dis
    mu "\"I'm not asking for your life story.\""
    show cli adv eyes
    show expression AlphaMask("foliage", At("cli adv eyes", left)) as mask2:
        alpha 0.45
    with dis
    mu "\"I just need to know if we're going to have open conversations about what we're really thinking, or not.\""
    show mur sideeye
    show expression AlphaMask("foliage", At("mur sideeye", center)) as mask:
        alpha 0.45
    with dis
    mu "\"Your choice.\""
    show expression AlphaMask("foliage", At("mur concerned d", center)) as mask:
        alpha 0.45
    with dis
    "I let somebody like Jack close once."
    menu mt2:

        "Should I do it again?"

        "Survival means putting yourself first.":
            "It's nothing personal."
            "I think that you have to be onto me, and that can't go anywhere good."
            m "\"I'm sorry, but you were right the first time.\""
            m "\"We don't know one another well.\""
            m "\"I don't think it's smart for us to show each other our weaknesses.\""
            show mur eyes
            show expression AlphaMask("foliage", At("mur eyes", center)) as mask:
                alpha 0.45
            with dis
            "The fox shakes his head."
            show mur talking
            show expression AlphaMask("foliage", At("mur talking", center)) as mask:
                alpha 0.45
            with dis
            mu "\"Regardless of how you feel, we're all survivors.\""
            show mur concerned d
            show expression AlphaMask("foliage", At("mur concerned d", center)) as mask:
                alpha 0.45
            with dis
            m "\"At least at the moment.\""
            show mur eyes talking
            show expression AlphaMask("foliage", At("mur eyes talking", center)) as mask:
                alpha 0.45
            with dis
            mu "\"I'd feel different about anybody if they'd been through what we've been through, and my sentinments about that aren't going to change.\""
            show mur eyes
            show expression AlphaMask("foliage", At("mur eyes", center)) as mask:
                alpha 0.45
            with dis
            "He starts to walk forward in the direction Jeb went, before looking behind at me and the professor."
            show mur fear d
            show expression AlphaMask("foliage", At("mur fear d", center)) as mask:
                alpha 0.45
            with dis
            mu "\"I hope you change your mind.\""
            m "\"Again, it's nothing personal.\""
            "Cliff adjusts his backpack and stands."
            show cli adv doubt
            show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
                alpha 0.45
            with dis
            cl "\"Let's put this all behind us, then.\""
            show cli adv happy
            show expression AlphaMask("foliage", At("cli adv happy", left)) as mask2:
                alpha 0.45
            with dis3
            cl "\"Chin up and feet forward, yes.\""
            show cli adv
            show expression AlphaMask("foliage", At("cli adv", left)) as mask2:
                alpha 0.45
            with dis3
            m "\"Sure, Professor.\""
        "We have to start communicating if we expect to get through this, now.":
            $ MT_Points += 1
            m "\"Okay\""
            m "\"Fine.\""
            jump MTconfession1


"Jeb eventually shows up again looking a little less flustered."

show jeb at right,forestdark
show expression AlphaMask("foliage", At("jeb", right)) as mask3:
    alpha 0.45
with dis3
show mur sideeye
show expression AlphaMask("foliage", At("mur sideeye", center)) as mask:
    alpha 0.45
with dis3
mu "\"Did you see anything out there while you were away?\""
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", right)) as mask3:
    alpha 0.45
with dis
jeb "\"Actually?\""
show jeb doubt
show expression AlphaMask("foliage", At("jeb doubt", right)) as mask3:
    alpha 0.45
with dis
jeb "\"Might have.\""
show jeb doubt talking
show expression AlphaMask("foliage", At("jeb doubt talking", right)) as mask3:
    alpha 0.45
with dis
jeb "\"I need somebody else to confirm it though just in case y'all question my credibility again.\""
show jeb doubt
show expression AlphaMask("foliage", At("jeb doubt", right)) as mask3:
    alpha 0.45
with dis
"He beckons us over to another part of the woods."
show jeb doubt talking
show expression AlphaMask("foliage", At("jeb doubt talking", right)) as mask3:
    alpha 0.45
with dis
jeb "\"This is about the right place.\""
show jeb doubt
show expression AlphaMask("foliage", At("jeb doubt", right)) as mask3:
    alpha 0.45
with dis
cl "\"What are we looking for?\""
show jeb
show expression AlphaMask("foliage", At("jeb", right)) as mask3:
    alpha 0.45
with dis
mu "\"Wait. Hold on.\""
show mur eyes talking
show expression AlphaMask("foliage", At("mur eyes talking", center)) as mask:
    alpha 0.45
with dis
"His nose twitches."
mu "\"Do you smell that?\""
show jeb shocked
show expression AlphaMask("foliage", At("jeb shocked", right)) as mask3:
    alpha 0.45
with dis
jeb "\"So you smell it too?\""
show mur eyes
show expression AlphaMask("foliage", At("mur eyes", center)) as mask:
    alpha 0.45
with dis
show cli adv eyes
show expression AlphaMask("foliage", At("cli adv eyes", left)) as mask2:
    alpha 0.45
with dis
"I sniff the air. Next to me, Cliff does the same."
"I just smell dry bark, dirt and mint."
"I sniff again, and catch something else this time."
"It's faint, but I smell ash and smoke on the wind."
show mur fear d
show expression AlphaMask("foliage", At("mur fear d", center)) as mask:
    alpha 0.45
with dis
mu "\"We’re not alone in these woods.\""
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
    alpha 0.45
with dis
cl "\"Someone must be nearby.\""
m "\"Could be trouble.\""
hide cli
hide jeb
hide mur
hide mask
hide mask2
hide mask3
with dis3
"Murdoch sniffs the air again, then walks off, beckoning for us to follow."
"We push through the shrubs and past trees, going off the beaten path."
"The smell of ash and burnt wood is getting stronger."
m "\"This is it. Stay close.\""
"I put myself between the source of the scent and the stragglers, baring my claws again."
"No matter what we end up finding, I'm not getting taken by surprise this time."
"I step into the clearing."
scene bg averycamp with dis
"There's a small campfire at the center. By the looks and smell of it, it wasn't put out that long ago."
"Next to it is a little group of four tents that I reckon could fit just about one person each."
"One of them's got patches sewn all over. Someone must've really wanted to keep it in one piece."
"Bags are haphazardly strewn across the clearing."
"Some have their contents spilling out on the forest floor."
"No doubt there's enough supplies here to feed a small group. No sign of any wagons, though."
cl "\"Do you see anyone?\""
m "\"Not yet.\""
mu "\"Good. I’ve had it up to here with the wilderness.\""
m "\"Keep your voice down.\""
"Claws still bared just in case, I walk into the camp."
"A tingle runs down my spine."
"A camp this deep into the woods can only mean trouble, right?"
cl "\"The campfire's still smoking.\""
cl "\"Whoever this camp belonged to must've left in a hurry.\""
mu "\"Maybe we weren't the only people to fall victim to whatever that creature was.\""
"Jebediah comes up behind me."
play music "music/quiet.ogg" fadein 4.0
jeb "\"I recognize that tent.\""
"His voice sounds urgent. Scared, almost."
"He runs past us, to the patched-up tent in the middle of it all."
"Without waiting for us, he opens the flaps."
"When he looks back at us, there are no words coming out of his muzzle at first."
"Only a pained grimace."
"Then—"
show jeb shocked at center,forestdark
show expression AlphaMask("foliage", At("jeb shocked", center)) as mask3:
    alpha 0.35
with dissolve
jeb "\"It’s empty.\""
"He buries his face in his hands."
show jeb angry talking
show expression AlphaMask("foliage", At("jeb angry talking", center)) as mask3:
    alpha 0.35
with dis
jeb "\"We-we gotta look. He can't have gone far.\""
show jeb angry
show expression AlphaMask("foliage", At("jeb angry", center)) as mask3:
    alpha 0.35
with dis
m "\"Who are you talking about?\""
show jeb sad talking
show expression AlphaMask("foliage", At("jeb sad talking", center)) as mask3:
    alpha 0.35
with dis
jeb "\"Avery. He's here.\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", center)) as mask3:
    alpha 0.35
with dis1
show jeb sad talking
show expression AlphaMask("foliage", At("jeb sad talking", center)) as mask3:
    alpha 0.35
with dis
jeb "\"I have to find him.\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", center)) as mask3:
    alpha 0.35
with dis1
hide jeb
hide mask3
with dis3
"He paces between the tents, looking in each and every one of them."
m "\"Avery?\""
"He says nothing. Just nods."
"His breathing is irregular, frantic."
"The physician's here? Why?"
"As I walk past the tents myself, I notice marks on the forest floor."
"They start at one side of the campfire and lead into the forest."
"What little plants there were in the way have been flattened and crushed beyond recognition."
"I kneel down next to them."
m "\"I found something.\""
show mur fear d at right,forestdark
show expression AlphaMask("foliage", At("mur fear d", right)) as mask:
    alpha 0.35
with dissolve
show jeb shocked at center,forestdark
show expression AlphaMask("foliage", At("jeb shocked", center)) as mask3:
    alpha 0.35
with dissolve
show cli adv doubt at left,forestdark
show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
    alpha 0.35
with dissolve
"The rest of the group joins me shortly."
mu "\"These marks...\""
show jeb shocked talking
show expression AlphaMask("foliage", At("jeb shocked talking", center)) as mask3:
    alpha 0.35
with dis
jeb "\"They're drag marks. Someone must've gotten carried away.\""
show jeb shocked
show expression AlphaMask("foliage", At("jeb shocked", center)) as mask3:
    alpha 0.35
with dis
"He runs his fingers over them."
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", center)) as mask3:
    alpha 0.35
with dis
jeb "\"They ain't too wide, or deep for that matter.\""
show jeb
show expression AlphaMask("foliage", At("jeb", center)) as mask3:
    alpha 0.35
with dis1
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", center)) as mask3:
    alpha 0.35
with dis
jeb "\"Fairly straight, too.\""
show jeb
show expression AlphaMask("foliage", At("jeb", center)) as mask3:
    alpha 0.35
with dis1
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", center)) as mask3:
    alpha 0.35
with dis
jeb "\"Whoever got dragged was thin. Light.\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", center)) as mask3:
    alpha 0.35
with dis
"He sighs."
show jeb sad talking
show expression AlphaMask("foliage", At("jeb sad talking", center)) as mask3:
    alpha 0.35
with dis
jeb "\"There wasn't much of a struggle.\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", center)) as mask3:
    alpha 0.35
with dis
show mur concerned d
show expression AlphaMask("foliage", At("mur concerned d", right)) as mask:
    alpha 0.35
with dis
stop music fadeout 6.0
mu "\"Let's... Let's not come to any hasty conclusions.\""
mu "\"Maybe they were carried to safety?\""
show cli adv sad
show expression AlphaMask("foliage", At("cli adv sad", left)) as mask2:
    alpha 0.35
with dis3
cl "\"Even if that's true... safety from what?\""
hide cli
hide jeb
hide mur
hide mask
hide mask2
hide mask3
with dissolve
$ renpy.music.set_volume(0.5, delay=5.0, channel='background')
"We look off into the woods."
"The trees are so dense we can't see too far out."
m "\"We need to move—\""
play sound "sfx/bush.ogg"
play music "music/contemplation.ogg" fadein 6.0
"There's a rustling noise off in the distance."
"I prick my ears up."
play sound "sfx/forestwalk.ogg"
"More footsteps."
"Leaves and twigs crunching."
m "\"Find a weapon.\""
"I scan the surrounding area for something, anything."
"I end up settling for one of the pieces of wood near the campfire."
"The footsteps sound closer, coming from the direction of the drag marks."
play sound "sfx/groupwalk.ogg"
"They ain't as heavy as the ones I heard last night."
"And there's more of them."
jeb "\"It's people.\""
mu "\"That a good or a bad thing?\""
jeb "\"I ain't sure yet. Stick close.\""
"Jebediah and I scramble back to our feet, getting in front of Murdoch and Cliff."
"I hear a man's voice coming from behind the trees."
tsunk "\"Is it safe out there?\""
"I see movement in the bushes."
"Another man, his voice much deeper, replies."
avunk "\"Hold on. There's people.\""
tsunk "\"People? What do you mean, people?\""
avunk "\"I said what I said. Quiet down.\""
play sound "sfx/thud4.ogg"
"Something hits the floor next to me."
stop music fadeout 5.0
"Jebediah has dropped the branch he was holding."
jeb "\"Avery? That you?\""
"The deeper voice answers."
avunk "\"Jeb?\""
avunk "\"One second. Goddamn branches are almost tearing my antlers off.\""
"The more I listen to it, the more I feel like I know that voice."
"I put my free paw on the back of my head, where the stitches had been."
play music "music/avery.ogg" fadein 3.0
show ave thinking scared shirt at center,forestdark
show expression AlphaMask("foliage", At("ave thinking scared shirt", center)) as mask4:
    alpha 0.35
with dis3
"A panting, heavyset elk comes stumbling out of the woods."
"The last time I saw this man, he was poking around with a needle in the back of my head."
"He takes a moment to catch his breath, peering straight at me."
"Behind his glasses, his brown eyes go big."
show ave shocked talking shirt
show expression AlphaMask("foliage", At("ave shocked talking shirt", center)) as mask4:
    alpha 0.35
with dis3
av "\"Sam?\""
show ave shocked shirt
show expression AlphaMask("foliage", At("ave shocked shirt", center)) as mask4:
    alpha 0.35
with dis
"Doc Avery."
"I don't know if he's a liscensed doctor or not, but that's what we call him, and he's done just good or better by Dora."
"She always said that some things can't leave a paper trail."
show jeb happy at right,forestdark
show expression AlphaMask("foliage", At("jeb happy", right)) as mask3:
    alpha 0.35
with dis3
jeb "\"Ave! It really is you!\""
"Jebediah walks up to him."
"Without saying a word, he embraces the much larger elk."
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", right)) as mask3:
    alpha 0.35
with dis
jeb "\"It's good to see you.\""
show jeb
show expression AlphaMask("foliage", At("jeb", right)) as mask3:
    alpha 0.35
with dis
show ave shocked talking shirt
show expression AlphaMask("foliage", At("ave shocked talking shirt", center)) as mask4:
    alpha 0.35
with dis
av "\"Awful nice to see you too, Jeb. Wish it was under better circumstances.\""
show ave shirt
show expression AlphaMask("foliage", At("ave shirt", center)) as mask4:
    alpha 0.35
with dis
"Avery stares on, rattled, but returns the hug nonetheless."
"We make eye contact once more."
"My cheeks feel red hot about now. I hope he doesn't mention the injury."
"But Jebediah's right."
"It's good to see someone familiar in this godforsaken forest."
show ave thinking happy shirt
show expression AlphaMask("foliage", At("ave thinking happy shirt", center)) as mask4:
    alpha 0.35
with dis3
av "\"And the Byrnes boy, too?\""
mu "\"Howdy, doc.\""
hide mask3
hide jeb
with dissolve
"Avery lets go of Jebediah."
"The horse wipes his eyes with his sleeves."
"There's wet streaks on them when he lowers his arms again."
show ave eyes talking shirt
show expression AlphaMask("foliage", At("ave eyes talking shirt", center)) as mask4:
    alpha 0.35
with dis3
av "\"Quite the odd posse you got here.\""
show ave wink talking shirt
show expression AlphaMask("foliage", At("ave wink talking shirt", center)) as mask4:
    alpha 0.35
with dis
av "\"Who's the short fella?\""
show ave shirt
show expression AlphaMask("foliage", At("ave shirt", center)) as mask4:
    alpha 0.35
with dis
show cli adv shocked at left,forestdark
show expression AlphaMask("foliage", At("cli adv shocked", left)) as mask2:
    alpha 0.35
with dis3
cl "\"Short?!\""
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
    alpha 0.35
with dis3
jeb "\"He's a customer I'm taking to the settlement.\""
jeb "\"At least I was until things went south.\""
jeb "\"Tried to go back the way we came, but I think somebody is messing with the landmarks.\""
show ave shocked talking shirt
show expression AlphaMask("foliage", At("ave shocked talking shirt", center)) as mask4:
    alpha 0.35
with dis
av "\"Oh! Pardon, sir. Didn't mean to offend, and all that. Rather on edge right now.\""
show ave shocked shirt
show expression AlphaMask("foliage", At("ave shocked shirt", center)) as mask4:
    alpha 0.35
with dis
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
    alpha 0.35
with dis
"Cliff seems offended all the same."
hide cli
hide mask2
with dissolve
"The elk turns his head."
show ave talking shirt
show expression AlphaMask("foliage", At("ave talking shirt", center)) as mask4:
    alpha 0.35
with dis
av "\"You can come out. They're friendlies.\""
show ave shirt
show expression AlphaMask("foliage", At("ave shirt", center)) as mask4:
    alpha 0.35
with dis1
show tse angry at right,forestdark
show expression AlphaMask("foliage", At("tse angry", right)) as mask5:
    alpha 0.35
with dis3
"A kit fox ducks out from behind a tree."
"Can’t be older than twenty, I’d reckon,  though the bags under his eyes make him look forty."
"He looks rather athletic, though I ain't sure whether the bulk under his shirt is fur or muscle."
show yis surprised at left,forestdark behind ave
show expression AlphaMask("foliage", At("yis surprised", left)) as mask6:
    alpha 0.35
with dis3
"A large bear wearing a worried expression on his face who looks about the same age follows suit."
show yis eyes
show expression AlphaMask("foliage", At("yis eyes", left)) as mask6:
    alpha 0.35
show tse
show expression AlphaMask("foliage", At("tse", right)) as mask5:
    alpha 0.35
with dis
m "\"What happened here?\""
show ave thinking shirt
show expression AlphaMask("foliage", At("ave thinking shirt", center)) as mask4:
    alpha 0.35
with dis3
av "\"I’d tell you, but you’d have me put in the madhouse.\""
m "\"Was it some sort of monster?\""
show ave shocked talking shirt
show expression AlphaMask("foliage", At("ave shocked talking shirt", center)) as mask4:
    alpha 0.35
with dis3
av "\"How... how’d you know?\""
show ave thinking shocked shirt
show expression AlphaMask("foliage", At("ave thinking shocked shirt", center)) as mask4:
    alpha 0.35
with dis3
jeb "\"Because the same thing got to us.\""
"Jeb closes his eyes."
jeb "\"It killed Doris, Ave.\""
"Avery goes quiet for a moment."
"Then he takes a step back."
show ave thinking scared shirt
show expression AlphaMask("foliage", At("ave thinking scared shirt", center)) as mask4:
    alpha 0.35
with dis
show yis
show expression AlphaMask("foliage", At("yis", left)) as mask6:
    alpha 0.35
with dis3
av "\"We’re missing a man, too. He was tending the fire when—\""
show ave eyes shirt
show expression AlphaMask("foliage", At("ave eyes shirt", center)) as mask4:
    alpha 0.35
with dis3
"He looks at the drag marks."
show ave talking shirt
show expression AlphaMask("foliage", At("ave talking shirt", center)) as mask4:
    alpha 0.35
with dis
av "\"We were looking for him, but he’s nowhere to be found.\""
show ave thinking shirt
show expression AlphaMask("foliage", At("ave thinking shirt", center)) as mask4:
    alpha 0.35
with dis3
av "\"Whatever it was didn’t leave any tracks. No blood, either.\""
av "\"It’s like he never existed at all.\""
show ave doubt shirt
show expression AlphaMask("foliage", At("ave doubt shirt", center)) as mask4:
    alpha 0.35
with dis3
show yis talking
show expression AlphaMask("foliage", At("yis talking", left)) as mask6:
    alpha 0.35
with dis3
"The bear talks to Avery in a language I don’t understand."
show yis
show expression AlphaMask("foliage", At("yis", left)) as mask6:
    alpha 0.35
with dis
show ave talking shirt
show expression AlphaMask("foliage", At("ave talking shirt", center)) as mask4:
    alpha 0.35
with dis
"Avery responds effortlessly."
show ave shirt
show expression AlphaMask("foliage", At("ave shirt", center)) as mask4:
    alpha 0.35
with dis
"I hear a small squeak behind me."
show cli adv shocked at halfleft,forestdark
show expression AlphaMask("foliage", At("cli adv shocked", halfleft)) as mask2:
    alpha 0.35
with dis3
cl "\"You’re with the Meseta?\""
"Ah, so that’s what it was."
"Cynthia only ever taught me some of the dirty words."
show ave thinking happy shirt
show expression AlphaMask("foliage", At("ave thinking happy shirt", center)) as mask4:
    alpha 0.35
with dis3
av "\"You know the language?\""
show ave doubt shirt
show expression AlphaMask("foliage", At("ave doubt shirt", center)) as mask4:
    alpha 0.35
with dis3
show cli adv blush eyes right
show expression AlphaMask("foliage", At("cli adv blush eyes right", halfleft)) as mask2:
    alpha 0.35
with dis3
cl "\"Only a little.\""
show cli adv blush eyes closed
show expression AlphaMask("foliage", At("cli adv blush eyes closed", halfleft)) as mask2:
    alpha 0.35
with dis
cl "\"I’m researching the Meseta for my thesis.\""
cl "\"We were on an expedition, but our journey so far has been a complete and utter disaster.\""
show cli adv sad
show expression AlphaMask("foliage", At("cli adv sad", halfleft)) as mask2:
    alpha 0.35
with dis3
cl "\"We only survived by the skin of our teeth last night.\""
show ave thinking shirt
show expression AlphaMask("foliage", At("ave thinking shirt", center)) as mask4:
    alpha 0.35
with dis3
av "\"That explains why Sam here looks more bloody and bruised than a miner after a tunnel collapse.\""
show ave doubt shirt with dis
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", halfleft)) as mask2:
    alpha 0.35
with dis3
cl "\"You know him?\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", halfleft)) as mask2:
    alpha 0.35
with dis
show ave wink talking shirt
show expression AlphaMask("foliage", At("ave wink talking shirt", center)) as mask4:
    alpha 0.35
with dis3
av "\"Of course I do. He’s a patient of mine.\""
show ave wink shirt
show expression AlphaMask("foliage", At("ave wink shirt", center)) as mask4:
    alpha 0.35
with dis
"I grit my teeth, silently praying he doesn’t bring up the stitches."
"He’s one of the few who can place me on the day I killed Jack."
"Gotta change the subject."
m "\"What were you doing out here in the woods, Doctor?\""
"He gestures to the bear and fox."
show ave talking shirt
show expression AlphaMask("foliage", At("ave talking shirt", center)) as mask4:
    alpha 0.35
with dis
show yis angry
show expression AlphaMask("foliage", At("yis angry", left)) as mask6:
    alpha 0.35
show tse angry
show expression AlphaMask("foliage", At("tse angry", right)) as mask5:
    alpha 0.35
with dis
av "\"These three—\""
show ave eyes shirt
show expression AlphaMask("foliage", At("ave eyes shirt", center)) as mask4:
    alpha 0.35
with dis
"He clears his throat."
show ave eyes talking shirt
show expression AlphaMask("foliage", At("ave eyes talking shirt", center)) as mask4:
    alpha 0.35
with dis
show tse
show expression AlphaMask("foliage", At("tse", right)) as mask5:
    alpha 0.35
with dis
show yis eyes
show expression AlphaMask("foliage", At("yis eyes", left)) as mask6:
    alpha 0.35
with dis
av  "\"These two are fishermen. Every two weeks or so, they come to Echo to sell their wares on the market.\""
show ave eyes shirt
show expression AlphaMask("foliage", At("ave eyes shirt", center)) as mask4:
    alpha 0.35
with dis1
show ave eyes talking shirt
show expression AlphaMask("foliage", At("ave eyes talking shirt", center)) as mask4:
    alpha 0.35
with dis
av "\"When they’re out of fish, they head home.\""
show ave eyes shirt
show expression AlphaMask("foliage", At("ave eyes shirt", center)) as mask4:
    alpha 0.35
with dis
show yis talking
show expression AlphaMask("foliage", At("yis talking", left)) as mask6:
    alpha 0.35
with dis
ysb "\"Tsela and Avery speak your language better than me.\""
show yis smile
show expression AlphaMask("foliage", At("yis smile", left)) as mask6:
    alpha 0.35
with dis
"The bear speaks in a way that sounds similar to Cynthia when she slips into a rant, but much friendlier."
show yis talking
show expression AlphaMask("foliage", At("yis talking", left)) as mask6:
    alpha 0.35
with dis
ysb "\"I think it is good to see more people right now.\""
show yis smile
show expression AlphaMask("foliage", At("yis smile", left)) as mask6:
    alpha 0.35
with dis
show tse angry
show expression AlphaMask("foliage", At("tse angry", right)) as mask5:
    alpha 0.35
with dis
"The kit fox glowers at us and doesn't say a word."
show tse
show expression AlphaMask("foliage", At("tse", right)) as mask5:
    alpha 0.35
with dis
show ave talking shirt
show expression AlphaMask("foliage", At("ave talking shirt", center)) as mask4:
    alpha 0.35
with dis
av "\"My folks live in these here woods, so I tag along most of the way every now and then.\""
show ave shirt
show expression AlphaMask("foliage", At("ave shirt", center)) as mask4:
    alpha 0.35
with dis1
show ave talking shirt
show expression AlphaMask("foliage", At("ave talking shirt", center)) as mask4:
    alpha 0.35
with dis
av "\"Never had much trouble until now. Forest's usually peaceful.\""
show ave shirt
show expression AlphaMask("foliage", At("ave shirt", center)) as mask4:
    alpha 0.35
with dis
"He shakes his head, sitting down next to the campfire and reaching for a nearby leather rucksack."
show tse angry talking
show expression AlphaMask("foliage", At("tse angry talking", right)) as mask5:
    alpha 0.35
with dis
ts "\"We should take what we can carry and leave before whatever that was comes back.\""
show tse angry
show expression AlphaMask("foliage", At("tse angry", right)) as mask5:
    alpha 0.35
with dis1
show tse angry talking
show expression AlphaMask("foliage", At("tse angry talking", right)) as mask5:
    alpha 0.35
with dis
ts "\"You saw what it did to Shilah, Avery. I'm not dying because of some strangers.\""
show tse surprised
show expression AlphaMask("foliage", At("tse surprised", right)) as mask5:
    alpha 0.35
with dis
show ave thinking sad shirt
show expression AlphaMask("foliage", At("ave thinking sad shirt", center)) as mask4:
    alpha 0.35
with dis3
av "\"I say we stay here for now, at least until it’s brighter out.\""
show tse angry
show expression AlphaMask("foliage", At("tse angry", right)) as mask5:
    alpha 0.35
with dis
show ave shirt
show expression AlphaMask("foliage", At("ave shirt", center)) as mask4:
    alpha 0.35
with dis3
"Avery turns to us."
show ave talking shirt
show expression AlphaMask("foliage", At("ave talking shirt", center)) as mask4:
    alpha 0.35
with dis
av "\"You folks best stay put too.\""
show ave shirt
show expression AlphaMask("foliage", At("ave shirt", center)) as mask4:
    alpha 0.35
with dis
show cli adv shocked
show expression AlphaMask("foliage", At("cli adv shocked", halfleft)) as mask2:
    alpha 0.35
with dis3
cl "\"But we have to get back!\""
show cli adv sad
show expression AlphaMask("foliage", At("cli adv sad", halfleft)) as mask2:
    alpha 0.35
with dis3
cl "\"Our supplies... my notes...\""
show ave angry talking shirt
show expression AlphaMask("foliage", At("ave angry talking shirt", center)) as mask4:
    alpha 0.35
with dis
av "\"No notes are worth getting killed over.\""
show ave angry shirt
show expression AlphaMask("foliage", At("ave angry shirt", center)) as mask4:
    alpha 0.35
with dis
cl "\"You don't understand. Without those notes, my life might as well be over.\""
show tse surprised
show expression AlphaMask("foliage", At("tse surprised", right)) as mask5:
    alpha 0.35
show yis surprised
show expression AlphaMask("foliage", At("yis surprised", left)) as mask6:
    alpha 0.35
with dis
cl "\"This expedition is the culmination of years of research into the Meseta culture.\""
show tse angry
show expression AlphaMask("foliage", At("tse angry", right)) as mask5:
    alpha 0.35
with dis
show yis
show expression AlphaMask("foliage", At("yis", left)) as mask6:
    alpha 0.35
with dis
"All three of the men exchange glances when they hear that."
"Cliff's on the verge of tears."
show cli adv angry
show expression AlphaMask("foliage", At("cli adv angry", halfleft)) as mask2:
    alpha 0.35
with dis3
cl "\"If I lose that research, I cannot hope to finish my thesis and—\""
show cli adv angry at left
show expression AlphaMask("foliage", At("cli adv angry", left)) as mask2:
    alpha 0.35
hide yis
hide tse
hide mask5
hide mask6
with dissolve
show ave eyes talking shirt
show expression AlphaMask("foliage", At("ave eyes talking shirt", center)) as mask4:
    alpha 0.35
with dis3
show cli adv shocked
show expression AlphaMask("foliage", At("cli adv shocked", left)) as mask2:
    alpha 0.35
with dis3
av "\"Quiet down and listen to me, fella.\""
show ave shirt
show expression AlphaMask("foliage", At("ave shirt", center)) as mask4:
    alpha 0.35
with dis3
show cli adv sad
show expression AlphaMask("foliage", At("cli adv sad", left)) as mask2:
    alpha 0.35
with dis3
"Save for a sniffle, Cliff goes dead silent."
show ave talking shirt
show expression AlphaMask("foliage", At("ave talking shirt", center)) as mask4:
    alpha 0.35
with dis
av "\"You ain't getting anywhere like this.\""
show ave shirt
show expression AlphaMask("foliage", At("ave shirt", center)) as mask4:
    alpha 0.35
with dis1
show expression AlphaMask("foliage", At("ave talking shirt", center)) as mask4:
    alpha 0.35
with dis
av "\"You're hungry. Tired.\""
show ave doubt shirt
show expression AlphaMask("foliage", At("ave doubt shirt", center)) as mask4:
    alpha 0.35
with dis
"He looks at me."
show ave thinking sad shirt
show expression AlphaMask("foliage", At("ave thinking sad shirt", center)) as mask4:
    alpha 0.35
with dis3
av "\"Wounded.\""
show ave talking shirt
show expression AlphaMask("foliage", At("ave talking shirt", center)) as mask4:
    alpha 0.35
with dis3
av "\"Your notes and your supplies ain't gonna just up and walk away from ya.\""
show ave serious shirt
show expression AlphaMask("foliage", At("ave serious shirt", center)) as mask4:
    alpha 0.35
with dis1
show ave serious talking shirt
show expression AlphaMask("foliage", At("ave serious talking shirt", center)) as mask4:
    alpha 0.35
with dis
av "\"I don't know a thing about the creature that attacked us. But going there in your state?\""
show ave shirt
show expression AlphaMask("foliage", At("ave shirt", center)) as mask4:
    alpha 0.35
with dis1
show ave talking shirt
show expression AlphaMask("foliage", At("ave talking shirt", center)) as mask4:
    alpha 0.35
with dis
av "\"Now that'd just make you easy pickings.\""
stop music fadeout 10.0
$ renpy.music.set_volume(1.0, delay=5.0, channel='background')
show ave serious shirt
show expression AlphaMask("foliage", At("ave serious shirt", center)) as mask4:
    alpha 0.35
with dis
"Cliff seems like he's about to speak up about it, but then he relents."
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", left)) as mask2:
    alpha 0.35
with dis3
cl "\"Very well.\""
show cli adv blush eyes closed
show expression AlphaMask("foliage", At("cli adv blush eyes closed", left)) as mask2:
    alpha 0.35
with dis
cl "\"I suppose I am rather peckish.\""
show ave thinking happy eyes shirt
show expression AlphaMask("foliage", At("ave thinking happy eyes shirt", center)) as mask4:
    alpha 0.35
with dis3
"Avery smiles, lowering the rucksack to the ground."
show ave talking shirt
show expression AlphaMask("foliage", At("ave talking shirt", center)) as mask4:
    alpha 0.35
with dis3
av "\"I'd be happy to trade some fruit for your name, Mister...\""
show ave shirt
show expression AlphaMask("foliage", At("ave shirt", center)) as mask4:
    alpha 0.35
with dis
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", left)) as mask2:
    alpha 0.35
with dis
cl "\"Tibbits. Clifford Tibbits.\""
show cli adv blush eyes right
show expression AlphaMask("foliage", At("cli adv blush eyes right", left)) as mask2:
    alpha 0.35
with dis
cl "\"Most people around here have taken to calling me Cliff... or less fortunate names.\""
show ave thinking flirty shirt
show expression AlphaMask("foliage", At("ave thinking flirty shirt", center)) as mask4:
    alpha 0.35
with dis3
play music "music/a-moment-of-solace.ogg" fadein 5.0
av "\"Cliff it is. My name's Avery.\""
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
    alpha 0.35
with dis
cl "\"No last name?\""
av "\"No last name, I already got the one.\""
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", left)) as mask2:
    alpha 0.35
with dis
cl "\"You're a doctor, correct?\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", left)) as mask2:
    alpha 0.35
with dis
show ave wink talking shirt
show expression AlphaMask("foliage", At("ave wink talking shirt", center)) as mask4:
    alpha 0.35
with dis3
av "\"Of sorts.\""
show ave wink shirt
show expression AlphaMask("foliage", At("ave wink shirt", center)) as mask4:
    alpha 0.35
with dis
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
    alpha 0.35
with dis
cl "\"Of sorts?\""
show ave eyes talking shirt
show expression AlphaMask("foliage", At("ave eyes talking shirt", center)) as mask4:
    alpha 0.35
with dis
av "\"This is gonna sound real funny to you, but I'm not a doctor the way you'd expect me to be.\""
show ave thinking happy shirt
show expression AlphaMask("foliage", At("ave thinking happy shirt", center)) as mask4:
    alpha 0.35
with dis3
av "\"Don't exactly have a license or a diploma. I'm just good at what I do.\""
av "\"Ask your friends.\""
show ave shirt
show expression AlphaMask("foliage", At("ave shirt", center)) as mask4:
    alpha 0.35
with dis3
"He takes an apple from the rucksack and hands it to Cliff."
"My own stomach growls."
cl "\"T-thank you, Mr. Avery.\""
hide cli
hide mask2
with dissolve
show ave talking shirt
show expression AlphaMask("foliage", At("ave talking shirt", center)) as mask4:
    alpha 0.35
with dis
av "\"I've got enough of those to share.\""
show ave shirt
show expression AlphaMask("foliage", At("ave shirt", center)) as mask4:
    alpha 0.35
with dis
"He offers Jebediah a shiny red one."
show jeb at right,forestdark
show expression AlphaMask("foliage", At("jeb", right)) as mask3:
    alpha 0.35
with dissolve
show ave talking shirt
show expression AlphaMask("foliage", At("ave talking shirt", center)) as mask4:
    alpha 0.35
with dis
av "\"Got your favorite too.\""
show ave shirt
show expression AlphaMask("foliage", At("ave shirt", center)) as mask4:
    alpha 0.35
with dis
"Jebediah swats his hand away."
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", right)) as mask3:
    alpha 0.35
with dis
jeb "\"I ain't hungry, Ave.\""
show jeb
show expression AlphaMask("foliage", At("jeb", right)) as mask3:
    alpha 0.35
with dis
show ave talking shirt
show expression AlphaMask("foliage", At("ave talking shirt", center)) as mask4:
    alpha 0.35
with dis
av "\"A man's gotta eat, Jeb.\""
show ave shirt
show expression AlphaMask("foliage", At("ave shirt", center)) as mask4:
    alpha 0.35
with dis
"He shakes the paw holding the apple."
"Jebediah reluctantly reaches out and takes it."
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", right)) as mask3:
    alpha 0.35
with dis
jeb "\"Fine.\""
show jeb
show expression AlphaMask("foliage", At("jeb", right)) as mask3:
    alpha 0.35
with dis1
hide jeb
hide mask3
with dissolve
hide ave
hide mask4
with dissolve
"Murdoch and I get one soon after, followed by the fishermen."
"It's nothing fancy, but right now, hungry as I am, I'll take it."
"I bite into it."
"It's so juicy I have to wipe my muzzle after I swallow."
"I notice the smell of blood from earlier still clinging to my torn sleeve."
show mur talking at right,forestdark
show expression AlphaMask("foliage", At("mur talking", right)) as mask:
    alpha 0.35
with dis3
mu "\"These are great. Thanks, doc.\""
show mur
show expression AlphaMask("foliage", At("mur", right)) as mask:
    alpha 0.35
with dis3
show ave talking shirt behind mur at center,forestdark
show expression AlphaMask("foliage", At("ave talking shirt", center)) as mask4:
    alpha 0.35
with dis3
av "\"Don't mention it. Got more if you need any.\""
show ave eyes talking shirt
show expression AlphaMask("foliage", At("ave eyes talking shirt", center)) as mask4:
    alpha 0.35
with dis
av "\"It ain't much, but it'll help with the hunger pangs, at least.\""
show ave shirt
show expression AlphaMask("foliage", At("ave shirt", center)) as mask4:
    alpha 0.35
with dis1
show ave talking shirt
show expression AlphaMask("foliage", At("ave talking shirt", center)) as mask4:
    alpha 0.35
with dis
av "\"Sam, mind joining me in my tent once you're done?\""
show ave shirt
show expression AlphaMask("foliage", At("ave shirt", center)) as mask4:
    alpha 0.35
with dis1
show mur mischief
show expression AlphaMask("foliage", At("mur mischief", right)) as mask:
    alpha 0.35
show cli adv shocked at left,forestdark
show expression AlphaMask("foliage", At("cli adv shocked", left)) as mask2:
    alpha 0.35
with dis3
"Cliff's eyes go wide once more."
"He nearly chokes on the apple in his mouth."
cl "\"Excuse me?\""
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
    alpha 0.35
show ave wink talking shirt
show expression AlphaMask("foliage", At("ave wink talking shirt", center)) as mask4:
    alpha 0.35
with dis3
av "\"It would be a good idea for me to check on his wounds.\""
show ave shirt
show expression AlphaMask("foliage", At("ave wink shirt", center)) as mask4:
    alpha 0.35
with dis1
show ave talking shirt
show expression AlphaMask("foliage", At("ave wink talking shirt", center)) as mask4:
    alpha 0.35
with dis
av "\"I don’t have the supplies or equipment to deal with an infection here. Or the stomach to deal with an amputation.\""
show ave shirt
show expression AlphaMask("foliage", At("ave shirt", center)) as mask4:
    alpha 0.35
with dis1
show mur
show expression AlphaMask("foliage", At("mur mischief", right)) as mask:
    alpha 0.35
with dis
show ave talking shirt
show expression AlphaMask("foliage", At("ave talking shirt", center)) as mask4:
    alpha 0.35
with dis
av "\"After that, perhaps we can see if it’s safe enough to go see my folks?\""
show ave shirt
show expression AlphaMask("foliage", At("ave shirt", center)) as mask4:
    alpha 0.35
with dis1
show ave talking shirt
show expression AlphaMask("foliage", At("ave talking shirt", center)) as mask4:
    alpha 0.35
with dis
av "\"Their hogan — their place, it isn't too far from here.\""
show ave serious shirt
show expression AlphaMask("foliage", At("ave serious shirt", center)) as mask4:
    alpha 0.35
with dis3
show cli adv shocked
show expression AlphaMask("foliage", At("cli adv shocked", left)) as mask2:
    alpha 0.35
with dis3
cl "\"Are you saying we're going to be visiting an authentic Meseta hogan?\""
show cli adv happy
show expression AlphaMask("foliage", At("cli adv happy", left)) as mask2:
    alpha 0.35
with dis3
"He seems to have forgotten all about his notes."
show ave shocked talking shirt
show expression AlphaMask("foliage", At("ave shocked talking shirt", center)) as mask4:
    alpha 0.35
with dis
av "\"Authentic?\""
show ave shocked shirt
show expression AlphaMask("foliage", At("ave shocked shirt", center)) as mask4:
    alpha 0.35
with dis3
show cli adv blush eyes closed
show expression AlphaMask("foliage", At("cli adv blush eyes closed", left)) as mask2:
    alpha 0.35
with dis3
cl "\"Wonderful! Splendid!\""
"I don't think he heard Avery."
"The bear’s looking at him from the corner of his eye, one brow raised."
show cli adv happy
show expression AlphaMask("foliage", At("cli adv happy", left)) as mask2:
    alpha 0.35
with dis3
cl "\"I've so many questions! Oh, if only I had a pen to jot them all down!\""
"He takes a big bite out of his apple."
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", left)) as mask2:
    alpha 0.35
with dis3
cl "\"We'd be most happy to join you.\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", left)) as mask2:
    alpha 0.35
with dis
"I didn't know his voice could go so high."
hide cli
hide mask2
with dissolve
show ave shirt
show expression AlphaMask("foliage", At("ave shirt", center)) as mask4:
    alpha 0.35
with dis
mu "\"Probably not a bad idea if that creature hunts at night. Right, Jebediah?\""
show jeb at left,forestdark
show expression AlphaMask("foliage", At("jeb", left)) as mask3:
    alpha 0.35
with dis3
"The horse grunts. He's getting back to his old self again."
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", left)) as mask3:
    alpha 0.35
with dis
jeb "\"So long as we get somewhere safe before nightfall. Ave's parents are nice folk.\""
show jeb
show expression AlphaMask("foliage", At("jeb", left)) as mask3:
    alpha 0.35
with dis
show ave thinking happy shirt
show expression AlphaMask("foliage", At("ave thinking happy shirt", center)) as mask4:
    alpha 0.35
with dis3
av "\"If you're lookin' for information on the Meseta, ain't no one in the region who knows as much as my ma.\""
show ave wink talking shirt
show expression AlphaMask("foliage", At("ave wink talking shirt", center)) as mask4:
    alpha 0.35
with dis3
av "\"Don't tell my pa I said that.\""
stop background fadeout 5.0
stop music fadeout 10.0
scene bg averytent with slow_dissolve
"Avery's tent is just big enough for the two of us."
"Even then, his antlers are pressing up against its roof, damn near tearing holes in the fabric."
"But it's somewhere private."
"Which is good, because I'm not decent right now."
"Avery's been cleaning my wounds for the past ten or so minutes, front and back."
"He's disinfected and applied bandages to my torso, and now most of his attention is focused on the wound on the back of my head."
show ave talking at center,avtent with dissolve
av "\"You have a knack for gettin' yourself into trouble, don't you, Sam?\""
show ave with dis
m "\"I'm a whore, Doctor. It's more like trouble has a knack for getting into me.\""
show ave talking with dis
av "\"Didn't hit your head too hard, if you're still cracking jokes.\""
show ave eyes with dis
"He hums a little ditty, wiping the back of my head and neck with a damp cloth."
"When he pulls it back, it's pink in hue, just like my shirt."
show ave thinking with dis3
av "\"It's a damn miracle you survived at all.\""
show ave with dis3
m "\"Heard that one before.\""
show ave thinking flirty with dis3
av "\"Didn't stop you from bumpin' your head again, now, did it?\""
"He moves the cloth down between my shoulderblades, over one of the spots that got scratched up the hardest."
show ave shocked with dis3
"I hiss."
m "\"Gotta keep you on your toes somehow.\""
show ave talking with dis
av "\"Believe me, boy.\""
show ave eyes with dis1
show ave eyes talking with dis
av "\"When you've worked in medicine for a while, nothing surprises you anymore.\""
show ave wink with dis1
show ave wink talking with dis
av "\"That's something our lines of work have in common, I reckon.\""
show ave wink with dis1
show ave wink talking with dis
av "\"Bet you got your fair share of stories.\""
show ave thinking nostalgia with dis3
av "\"Lord knows I do.\""
show ave talking with dis3
av "\"Why, just ask Jebediah.\""
show ave with dis
m "\"How do you two know each other?\""
play music "music/jebtheme.ogg" fadein 4.0
show ave talking with dis
av "\"Now that story I can share.\""
show ave with dis
"He wrings out the cloth in the bucket."
show ave thinking nostalgia with dis3
av "\"His family owns a ranch not too far outside of town.\""
av "\"When I was younger, before I came to Echo, I used to spend summers working there as a farmhand.\""
show ave eyes talking with dis3
av "\"The pay wasn't that great, but back then, it was my first job, and it meant the sun and stars to me.\""
show ave eyes with dis1
show ave eyes talking with dis
av "\"I've never met a kid as curious as Jeb was.\""
show ave thinking happy with dis3
av "\"Always asking me these questions.\""
av "\"At first it was 'How are you that tall?' and 'What are those things on your head, Ave? What're they for?'\""
show ave talking with dis3
av "\"As we got older, he started asking me about the Meseta. And what it was like out there.\""
show ave eyes with dis1
show ave eyes talking with dis
av "\"Don't think the boy ever wanted to be a rancher. He was always off writing his little stories and reading his books.\""
show ave with dis1
show ave talking with dis
av "\"Anyway, time went on. You know how it is.\""
show ave thinking happy with dis3
av "\"I packed up and moved to Echo eventually, but we stayed in contact.\""
m "\"Can't really picture him being all that talkative.\""
show ave thinking sad with dis
"He's quiet for a moment."
av "\"He's not as happy as he used to be.\""
show ave serious talking with dis3
av "\"Most of what troubles Jebediah happened after I left.\""
show ave thinking sad with dis3
av "\"Now that {i}ain't{/i} my story to tell.\""
av "\"If you really want to know, ask him.\""
stop music fadeout 10.0
show ave with dis3
"He pats my shoulder. It still hurts."
show ave talking with dis
av "\"My turn.\""
show ave thinking happy with dis3
av "\"What got you following a weasel out into the woods?\""
m "\"He's a client.\""
show ave talking with dis3
av "\"Must be some client if Dora's willing to let you out of her sight.\""
show ave with dis
m "\"He's a rich fella from Batavia. Came here to work on his... uh... fee... fees...\""
show ave thinking with dis3
av "\"He mentioned a thesis.\""
m "\"That's it.\""
m "\"Either way, he's payin', so.\""
"I'm not telling him my actual reason for coming along."
"I grab my shirt and pants."
show ave talking with dis3
av "\"You might want to throw those clothes away when we get to the hogan, by the way.\""
show ave with dis1
show ave talking with dis
av "\"They've got more holes in 'em than a Hendricks contract.\""
show ave thinking with dis3
av "\"Maybe not as much blood on 'em, but still plenty.\""
m "\"Brought some more clothes with me, but they're with the supplies.\""
show ave talking with dis3
av "\"We can probably squeeze you into some old clothes of mine.\""
show ave with dis1
show ave talking with dis
av "\"Might be a tight fit, though.\""
show ave with dis
"I look over my shoulder, at his belly, and raise a brow."
"He notices, and laughs."
"It's a deep, rumbling one that makes the tent quiver."
show ave talking with dis
av "\"I'll head out and let you get dressed.\""
show ave thinking with dis3
av "\"Can't say it'll stop hurting right away, but at least you won't die.\""
show ave thinking sad with dis
av "\"More than I can say for a lot of other men who take a tumble in these woods.\""
m "\"Thanks, Doctor. I owe ya one.\""
show ave wink talking with dis3
av "\"Do you now?\""
show ave wink with dis
"His smile turns bashful."
"His glasses slide down his snout a little."
show ave thinking flirty with dis3
av "\"I'll have to keep that in mind when we get back.\""
"He crosses his arms, as if he's deep in thought."
av "\"Been a while since we last had an appointment, hasn't it?\""
av "\"At least one that didn't involve me fixing you up.\""
m "\"Right.\""
"It has been a while."
"I don't see him around much, though Dora always seems to know how to find him."
"But I do remember those appointments very well."
"He's good with his hands."
show ave thinking with dis
av "\"Then I suppose I'll have to arrange something.\""
av "\"Dora ought to be keeping you in tip top shape for as hard as you work and for how many hazards you experience.\""
av "\"I'd say you're overdue for a physical.\""
m "\"I'd like that, Doc.\""
show ave talking with dis3
av "\"Though you better stop cracking your head open like an egg every time I see you.\""
show ave thinking flirty with dis3
av "\"Sooner or later it's gonna turn out scrambled.\""
hide ave with dis
"With another pat on the back, he crawls backwards, out of his tent."
"He leaves me alone with my dirty shirt and my thoughts."
$ renpy.music.set_volume(1.0, delay=2.0, channel='background')
$ renpy.music.set_volume(0.7, delay=2.0, channel='music')
play background "music/forestambience.ogg" fadein 5.0
scene bg forestmorning with slow_dissolve
play music "music/samueltheme.ogg" fadein 8.0
"Walking's a lot easier when I don't have to do it on an empty stomach."
"We're leaving the deepest parts of the forest behind, heading a little ways off the trail with Avery in tow."
"It's both a blessing and a curse. As the trees get sparser, I start feeling that familiar desert heat again."
"Avery, walking up front with Jebediah, seems to be feeling a bit better."
"He's singing. Loudly, at that."
"I wish I had half the energy he has right about now."
"The bear and the kit fox haven't said a word since we left."
show ave thinking happy at center,forest
show expression AlphaMask("foliage", At("ave thinking happy", center)) as mask4:
    alpha 0.35
with dissolve
av "\"Summertime, I'm jumpin' out and back into your skin...\""
show mur at right,forest
show expression AlphaMask("foliage", At("mur", right)) as mask:
    alpha 0.35
with dis3
"Murdoch hums along for a few bars, and I have to admit, Cliff was right about his voice."
show ave talking
show expression AlphaMask("foliage", At("ave talking", center)) as mask4:
    alpha 0.35
with dis3
av "\"You know it too, eh?\""
"The elk swings his head around, nearly whacking Jebediah with his antlers."
show mur mischief
show expression AlphaMask("foliage", At("mur mischief", right)) as mask:
    alpha 0.35
with dis
mu "\"Old favorite of mine.\""
show mur
show expression AlphaMask("foliage", At("mur", right)) as mask:
    alpha 0.35
with dis
show cli adv talking at left,forest
show expression AlphaMask("foliage", At("cli adv talking", left)) as mask2:
    alpha 0.35
with dis3
cl "\"I'm not sure I've ever heard it before.\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", left)) as mask2:
    alpha 0.35
with dis
show mur talking
show expression AlphaMask("foliage", At("mur talking", right)) as mask:
    alpha 0.35
with dis
mu "\"I'd love to play it for you when I get my paws on my guitar again.\""
show ave thinking happy
show expression AlphaMask("foliage", At("ave thinking happy", center)) as mask4:
    alpha 0.35
with dis3
av "\"You play?\""
show mur mischief
show expression AlphaMask("foliage", At("mur mischief", right)) as mask:
    alpha 0.35
with dis
mu "\"Why, yes, indeed!\""
show ave talking
show expression AlphaMask("foliage", At("ave talking", center)) as mask4:
    alpha 0.35
with dis3
av "\"I tried once. Couldn't get far, not with these sausages of mine.\""
show ave wink
show expression AlphaMask("foliage", At("ave wink", center)) as mask4:
    alpha 0.35
with dis
"He wiggles his thick fingers."
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", left)) as mask2:
    alpha 0.35
with dis
show mur
show expression AlphaMask("foliage", At("mur", right)) as mask:
    alpha 0.35
with dis
cl "\"So where exactly do your parents live, Avery?\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", left)) as mask2:
    alpha 0.35
with dis3
show ave thinking
show expression AlphaMask("foliage", At("ave thinking", center)) as mask4:
    alpha 0.35
with dis3
av "\"Oh! We're getting pretty close.\""
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", left)) as mask2:
    alpha 0.35
with dis
cl "\"This far off the main trail?\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", left)) as mask2:
    alpha 0.35
with dis
av "\"The hogan's hard to find if you don't know where to look.\""
av "\"Keeps out unwanted visitors.\""
show mur concerned d
show expression AlphaMask("foliage", At("mur concerned d", right)) as mask:
    alpha 0.35
with dis
mu "\"Don't we qualify as unwanted visitors?\""
av "\"Any friend of mine's welcome.\""
hide ave
hide mask4
show jeb at center,forest
show expression AlphaMask("foliage", At("jeb", center)) as mask3:
    alpha 0.35
with dissolve
"Jebediah looks over his shoulder, back at us."
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", center)) as mask3:
    alpha 0.35
with dis
jeb "\"Just mind your manners and you'll be fine. Ave's parents are the finest folk in this neck of the woods.\""
show jeb
show expression AlphaMask("foliage", At("jeb", center)) as mask3:
    alpha 0.35
with dis1
hide mask3
hide jeb
show cli adv blush eyes closed
show expression AlphaMask("foliage", At("cli adv blush eyes closed", left)) as mask2:
    alpha 0.35
with dis3
"Cliff's already shaking at the prospect."
cl "\"This is so exciting! I can't believe I'm about to enter an actual Meseta home!\""
"I'm more than a little worried about him."
"Or what he might say."
show cli adv eyes talking
show expression AlphaMask("foliage", At("cli adv eyes talking", left)) as mask2:
    alpha 0.35
with dis
cl "\"Calm down, Clifford. You're a researcher, not a tourist.\""
show cli adv eyes
show expression AlphaMask("foliage", At("cli adv eyes", left)) as mask2:
    alpha 0.35
with dis
"He takes a breath."
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", left)) as mask2:
    alpha 0.35
with dis
cl "\"Murdoch, is your camera still functional?\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", left)) as mask2:
    alpha 0.35
with dis
show mur talking
show expression AlphaMask("foliage", At("mur talking", right)) as mask:
    alpha 0.35
with dis
mu "\"It should work just fine. In layman's terms, everything still clicks the way it's supposed to.\""
show mur
show expression AlphaMask("foliage", At("mur", right)) as mask:
    alpha 0.35
with dis
show cli adv happy
show expression AlphaMask("foliage", At("cli adv happy", left)) as mask2:
    alpha 0.35
with dis3
cl "\"Splendid!\""
show ave behind mur at center,forest
show expression AlphaMask("foliage", At("ave", center)) behind mur as mask4:
    alpha 0.35
with dissolve
show ave talking
show expression AlphaMask("foliage", At("ave talking", center)) as mask4:
    alpha 0.35
with dis
av "\"You're awful excited about all this, aren't you?\""
show ave
show expression AlphaMask("foliage", At("ave", center)) as mask4:
    alpha 0.35
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", left)) as mask2:
    alpha 0.35
with dis3
cl "\"Of course! It's a once in a lifetime chance!\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", left)) as mask2:
    alpha 0.35
with dis
show ave talking
show expression AlphaMask("foliage", At("ave talking", center)) as mask4:
    alpha 0.35
with dis
av "\"Well their home isn't going anywhere anytime soon.\""
show ave
show expression AlphaMask("foliage", At("ave", center)) as mask4:
    alpha 0.35
with dis1
show ave talking
show expression AlphaMask("foliage", At("ave talking", center)) as mask4:
    alpha 0.35
with dis
av "\"And it's their life, you know?\""
show ave
show expression AlphaMask("foliage", At("ave", center)) as mask4:
    alpha 0.35
with dis
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", left)) as mask2:
    alpha 0.35
with dis
"Cliff tilts his head."
show ave serious talking
show expression AlphaMask("foliage", At("ave serious talking", center)) as mask4:
    alpha 0.35
with dis
av "\"All I'm saying is, ease into it. Listen to what they gotta say when they talk.\""
show ave
show expression AlphaMask("foliage", At("ave", center)) as mask4:
    alpha 0.35
with dis1
show ave talking
show expression AlphaMask("foliage", At("ave talking", center)) as mask4:
    alpha 0.35
with dis
av "\"Think you can do that, little fella?\""
show ave
show expression AlphaMask("foliage", At("ave", center)) as mask4:
    alpha 0.35
with dis
show cli adv blush eyes right
show expression AlphaMask("foliage", At("cli adv blush eyes right", left)) as mask2:
    alpha 0.35
with dis
cl "\"I... I'll try.\""
show ave thinking happy
show expression AlphaMask("foliage", At("ave thinking happy", center)) as mask4:
    alpha 0.35
with dis3
av "\"Thank you, Cliff.\""
stop music fadeout 3.0
play background "music/cicadas.ogg" fadeout 2.0 fadein 2.0
scene bg hoganoutside with slow_dissolve
"We walk for about thirty more minutes through the woods before we come upon a clearing."
"There’s a pen of livestock to the left where wooly animals graze."
"A large, round structure sits ahead of us."
"It looks like a dome covered in earth with a doorway."
"I certainly haven’t ever seen anything like it."
"Cliff is making strange noises beside me."
"Avery shuffles a bit."
$ renpy.music.set_volume(1.0, channel='music')
"He calls out in a language I don’t understand, and the reedy voice of a woman meets it."
"The door of the dwelling opens and a very old elk comes out to meet us."
"She wears a plain apron, and her hands are red with what looks like clay."
"She looks back and forth at all of us, folds in her brow growing prominent, then looks toward Avery, speaking slowly and calmly in that language."
"Avery laughs and replies in a carefree way."
"She does not return the laugh."
play music "music/hogan.ogg" fadein 3.0
maunk "\"Then it cannot be helped.\""
"Her accent is thicker than Avery’s is."
ma "\"I already know Jebediah. To the rest of you, I am Manaba.\""
ma "\"My son tells me that you met something evil in the woods.\""
ma "\"You may stay in my home for as long as you like, so long as you give as much as you take.\""
ma "\"And so long as you don’t bring what you met in the woods inside.\""
"She disappears into the door."
show cli adv happy at left with dissolve
cl "\"Not a single slaughtering beast among us at present, so we’re good!\""
"Murdoch crosses his arms."
show mur talking at center with dissolve
mu "\"Do you think she was being literal?\""
show mur with dis
show jeb at right with dissolve
"The horse grunts."
show jeb talking with dis
jeb "\"Yes and no.\""
hide jeb with dissolve
show ave talking at right with dissolve
av "\"She means that the evil in our own heads can upset the harmony in her home.\""
show ave thinking nostalgia with dis3
av "\"Home is a sacred place.\""
av "\"As long as we’re calm, she’ll let us stay. There’s nothing to worry about.\""
"So then what am I supposed to do?"
"What the fuck?"
"That doesn’t reassure me at all."
"Jeb has a nervous look on his face too."
"Cliff and Murdoch don’t."
show ave talking with dis3
av "\"One last thing.\""
show ave eyes with dis1
show ave eyes talking with dis
av "\"Make sure you go clockwise when you enter and leave the hogan.\""
show mur talking with dis
mu "\"Why?\""
show mur with dis
show cli adv talking with dis
cl "\"Because it’s like the sun.\""
show cli adv with dis
show ave thinking happy with dis
av "\"Oh. So you already know?\""
show cli adv eyes talking with dis
cl "\"Well, I believe the idea is that actively moving with the sun bolsters the natural order of the universe.\""
show cli adv talking with dis
cl "\"This contributes to harmony.\""
show ave thinking with dis
av "\"Well, sure.\""
av "\"But there’s a practicality to it, too.\""
show ave talking with dis
av "\"When your home is just one room, going in one order makes it feel bigger.\""
show ave with dis
m "\"Speakin’ of practicality, are we gonna go inside?\""
hide ave with dissolve
"Avery smiles and walks up to the doorway, opening it."
stop background fadeout 2.0
scene bg hoganinside with dissolve
"The first thing I see when we pass through is a big fire pit in the center of the room."
"The floor is bare dirt, but many woven rugs."
"Most of them line the walls made from branches."
"So is the ceiling, but there’s a big hole at the top letting light in from the outside."
"Manaba sits on the floor, pushing red clay between a slab and a smooth rock."
"Another elk sits to the north, handling the threads of a loom."
"He’s big, but he looks very old, and he speaks to Manaba again in that language."
"She reponds quietly, calmly, but looks more preoccupied with the clay she’s making."
"The big elk hums to himself."
ga "\"My name’s Gad, for the strangers among you.\""
show ave talking at right,hoganday with dissolve
av "\"Need me to tell them the rules, pa?\""
show ave with dis
"He tilts his antlers away from the loom to take a proper look at us through his glasses."
ga "\"Rules?\""
ga "\"I always forget we have those.\""
ga "\"The chores are still the same. I’m sure you remember those.\""
show ave thinking happy with dis3
"Avery scratches his head nervously, as if he’s suddenly remembering."
ga "\"Strangers, would you give me your names?\""
show cli adv happy at left,hoganday with dissolve
cl "\"Clifford Tibbits. I am so happy to make your acquaintances!\""
show mur talking at center,hoganday with dissolve
mu "\"I’m not so bubbly as this one, but charmed all the same. Murdoch Byrnes.\""
show mur with dis
m "\"Just Sam.\""
"Dunno why they’re making this so official."
hide mur with dissolve
hide cli with dissolve
hide ave with dissolve
ga "\"And now you’re no longer strangers.\""
ga "\"Neat trick, hrmm?\""
"He’s still preoccupying himself with his weaving."
ma "\"We haven’t had this many visitors in a long time.\""
ma "\"You can do better than that.\""
"This old woman is grinning about something."
"I feel my eyebrow lifting."
ga "\"But then you’d be closer to finishing than me.\""
ga "\"And that wouldn’t do.\""
"I look back to her hands dunking into a pitcher of water, then to his hands flipping through the loom strands carefully."
"It dawns on me that they’re competing."
"They keep at this for at least another minute with tense concentration until I hear a small rip."
"Gad sighs and Manaba smirks."
ga "\"Very well. I can’t recover from that.\""
"He starts looking from expression to expression in the room."
ga "\"I can tell by your faces that you all feel apprehensive.\""
ga "\"I’ll trade stories for stories to help with that.\""
"He looks to Jeb, then his son, then the two fishermen."
ga "\"Tell me what happened in the woods, but do not speak of any death.\""
"Jeb looks upset, but Avery clears the silence."
show ave talking at center,hoganday
show jeb at right,hoganday
with dissolve
av "\"I was coming to see you both, but for these two it started as an ordinary fishing trip.\""
show ave thinking with dis3
av "\"We were ambushed by the river and one of our party was taken.\""
av "\"We thought we saw the beast that did it, but it seems every person saw something different.\""
show ave thinking sad with dis
av "\"I saw a vast, greedy fish that flopped like a mudskipper, only faster than any I had seen before.\""
av "\"But its big, milky eyes looked diseased.\""
show ave serious talking with dis3
av "\"We met this group near the riverside.\""
show ave serious eyes with dis1
show ave serious eyes talking with dis
av "\"Jeb’s told me his wagon got attacked, and he lost his jennies.\""
show ave serious with dis
show jeb talking with dis
jeb "\"Same thing happened to us, more or less.\""
show jeb with dis
ga "\"Were you folks traveling from the north?\""
show jeb talking with dis
jeb "\"South, from Echo.\""
show jeb with dis
"Gad stops weaving and his expression meets Jeb’s."
ga "\"You don’t usually have problems coming that way.\""
show jeb sad talking with dis
jeb "\"Usually don’t.\""
show jeb sad with dis
ga "\"Enough do though.\""
ga "\"What was different this time?\""
show jeb doubt with dis
"Jeb looks like he’s thinking."
show jeb talking with dis
jeb "\"The marks in the trees weren’t there anymore.\""
show jeb with dis1
show jeb talking with dis
jeb "\"Reliable landmarks weren’t the same.\""
show jeb with dis
ysb "\"One of ours said that the trees looked different, that they could see things that shouldn’t normally be there.\""
show ave thinking with dis3
av "\"Trying not to get too descriptive.\""
ma "\"We have always told travelers to fish to the north, not the south.\""
av "\"I know that.\""
ysb "\"There haven’t been problems until now.\""
ma "\"Flesh forgets. Soil doesn’t.\""
hide jeb
hide ave
with dissolve
"She pulls the red clay from her slab and puts it in a ceramic bowl, folding it into the sides."
"There’s something relaxing about her pushing the clay in, folding, and spinning slowly, almost like it’s dough."
"Wish her words were just as relaxin’."
show cli adv doubt at center,hoganday with dissolve
cl "\"North?\""
show cli adv talking with dis
cl "\"You know, I’ve noticed that there aren’t many Meseta people who live in Echo.\""
show cli adv with dis
ga "\"There’s a few. And this one.\""
"He jerks his head to his son."
show ave thinking sad at right,hoganday with dissolve
"Avery looks a little flustered."
av "\"There’s work there that pays well.\""
ga "\"I still think not enough for the risk.\""
"I can’t help but feel this is a sore spot."
"Reminds me of how Cynthia won’t talk about it either."
ma "\"We avoid going there to sell, even with all the buyers.\""
ga "\"There are too many evil stories about that land.\""
ga "\"Such that we don’t like to talk about it.\""
show ave angry talking with dis3
av "\"So then why are we talking about it?\""
show ave angry with dis
ma "\"Because we are afraid for you.\""
"The elk looks at his wife curiously."
ga "\"I am not afraid for him.\""
ga "\"He is strong and intelligent.\""
ga "\"Our fathers were great warriors, Manaba.\""
"She says something that makes Gad’s brow furrow."
show ave serious eyes with dis
"Avery winces."
hide ave with dissolve
ma "\"This bowl is ready for firing.\""
show cli adv shocked with dis3
"She dusts off her apron as she stands, looking among the crowd of people and waving."
ma "\"Goodbye.\""
"I hear Cliff make a noise."
show cli adv happy with dis3
cl "\"Might I watch this process?\""
ma "\"Yes.\""
"She picks up several clay bowls and hands them to the weasel, whose hands quickly fill up."
show cli adv shocked with dis3
"He looks terrified of dropping any."
"I don’t think he expected to be participating."
ma "\"Follow.\""
hide cli with dissolve
"With a look of fear, he follows her out the door."
show mur mischief at center,hoganday with dissolve
"Murdoch gives me a look."
mu "\"...I have to see this.\""
hide mur with dissolve
"The fox leaves the building."
"Avery, his two companions, and Jeb sort of look at me."
m "\"...what?\""
show jeb talking at center,hoganday with dissolve
jeb "\"Mind joinin’ ‘em?\""
show jeb with dis
"There’s some air of anticipation, like they want to talk to Gad in private."
m "\"Don’t have to ask twice.\""
show jeb talking with dis
jeb "\"Thanks.\""
show jeb with dis1
scene bg hoganoutside with dissolve
play background "music/cicadas.ogg" fadein 3.0
show cli adv at right with dis
show mur at left with dis
"I walk out the door and see Murdoch, Cliff, and Manaba huddled around what looks like a small pit in the ground."
show cli adv talking with dis
cl "\"So you let the embers burn for hours before stacking the ceramics?\""
show cli adv doubt with dis
cl "\"And then you pile on more wood to light a second fire to bake the clay?\""
show cli adv happy with dis
cl "\"Extraordinary... just, extraordinary!\""
ma "\"You speak very fast.\""
show cli adv talking with dis
cl "\"I’m sure every piece is to be treasured.\""
show cli adv with dis
ma "\"These are just for when we eat.\""
ma "\"Practical pieces.\""
show cli adv eyes talking with dis
show mur concerned d with dis
cl "\"I consider them art.\""
show cli adv eyes with dis
ma "\"Not art.\""
"Cliff hums."
show cli adv doubt with dis
cl "\"Surely you must admit that there is something... sacred to this, yes?\""
ma "\"All things natural are sacred.\""
ma "\"I think what you call art — you put into a room, and you have people look with just their eyes.\""
show cli adv talking with dis
cl "\"In a manner of speaking, yes. For the sake of public awareness.\""
show cli adv with dis
ma "\"What we make, we use. Or we sell. Or we trade.\""
ma "\"The act of making influences respect.\""
ma "\"Respect for making turns into patience.\""
ma "\"Eyes alone do not teach patience.\""
"She looks at me and Murdoch."
ma "\"You will both bring me two logs from the pile.\""
"She looks at Cliff."
ma "\"You bring me five.\""
show mur happy with dis
show cli adv shocked with dis
cl "\"Why do I have to bring more?\""
cl "\"They’re bigger than me!\""
ma "\"They have shared more of themselves by their silence than you have with your words.\""
hide cli with dissolve
show mur with dis
"Cliff grimaces, but he doesn’t argue and walks on over to the log pile with determination in his eye."
"Whoa, that actually worked?"
"Maybe I should tell Cliff to go make a fire pit more often."
m "\"Two logs comin’ up.\""
"When I get to the pile I whistle."
m "\"These are chunky.\""
show mur mischief with dis
"Murdoch looks at the pile too and lets out a one note-laugh."
mu "\"It’s like if your thighs were made out of wood.\""
"Cliff isn’t paying any attention to us and hefts one of the logs, panting as he carries his first one back to the fire."
"I bend over to pick up two logs and haul them both over my shoulder."
"The logs are long, awkwardly shaped, and even I feel winded by their weight."
"Murdoch looks at me with some skepticism."
show mur concerned d with dis
mu "\"I think I’ll do these one at a time.\""
m "\"Probably wise.\""
"I wink, and he addresses me with a look."
hide mur with dissolve
"I set the logs down by the fire, feeling a grunt escape my body from the sudden decrease of all that weight."
"When Cliff and Murdoch’s first log arrives, she puts them in the embers, stacking them over the pottery in a triangle formation."
"The wood is so dry that it doesn’t take long for the logs to smoke."
"By the time Cliff brings his last log, he’s heaving hard, and flame takes to the wood."
"The smoke gets thick enough to look cloudy."
ma "\"Four hours.\""
"She stands, and starts hobbling back to the front door of the hogan."
scene bg hoganinsidenight with slow_dissolve
stop music fadeout 10.0
play background "sfx/bonfire.ogg" fadeout 1.0
"When I go through the doorway again, I see that Jeb and Avery’s group are sitting on a rug against the wall, discussing something in a low voice."
"Gad is stoking the fire in the center of the room, and Manaba is pouring what looks like a small amount of oil from a jar into a big cast iron pot."
ma "\"Did you bring fresh fish?\""
av "\"The bass was big today.\""
ma "\"Help me clean them. We’ll fry them with the bread. Peppers, too.\""
ma "\"We will eat in one hour.\""
ga "\"An hour?\""
ma "\"Why don’t you tell a story while they wait?\""
"The elk crosses his arms and tilts his antlers."
m "\"Could you tell us a story about Echo?\""
"His lips purse."
ga "\"We said that we don’t speak about that land.\""
m "\"I know. I was just curious why?\""
"Do they know things that they aren’t willing to talk about?"
ga "\"All you need to know about that land is that it’s unnatural.\""
m "\"But what does that really mean?\""
ga "\"If you ask again, I will have to take that as an attack upon our home, and I will have to ask you to leave.\""
"The mood of the room shifts from lively to something more tense and quiet."
"I didn’t mean to sour the evening, but if these people know something that we don’t, maybe it’s possible that they could help us?"
ga "\"You seem to think that we hide secrets.\""
ga "\"The truth is that part of what protects us is knowing little about evil things.\""
ga "\"I can tell you only one story about Echo, but it does not involve the unnatural.\""
ga "\"At least not directly.\""
play music "music/hoganstory.ogg" fadein 3.0
ga "\"The real boundaries of that land have been known to my grandfather’s grandfather, not the men who think in maps and railroads.\""
ga "\"Near the year 1600 in your calendar, it’s said that a band of warriors found locations where mother earth would cradle them and father sky couldn’t be blotted out.\""
ga "\"Bonfires were their beacons.\""
ga "\"The chanting and the dancing roused their spirits.\""
ga "\"It’s said even our most foolish warriors could whistle at these places at night with nothing to fear.\""
ga "\"I don’t necessarily believe that part, though.\""
ga "\"You’re not supposed to do that, you know.\""
ga "\"Gives away your position.\""
ga "\"But as they said, it was difficult to fear death when you were surrounded by loved ones.\""
ga "\"But the funny thing about these places is they weren’t keeping track of them.\""
ga "\"They had no reason to keep track of them.\""
ga "\"To be Meseta means to wander.\""
ga "\"Our people weren’t used to staying put.\""
ga "\"Staying put is more of a modern thing.\""
ga "\"Access to food keeps changing.\""
ga "\"But sometimes, it was known that the best thing to do was to leave your home behind and start anew elsewhere.\""
ga "\"The bonfires were more of a nod to peace of mind than anything else.\""
ga "\"So these warriors made many bonfires in their time.\""
ga "\"And so did their children.\""
ga "\"And so did their children’s children.\""
ga "\"New ones are made by younger people from time to time, but you can still find the sites of a lot of the old ones.\""
ga "\"Eventually, our people did have to start paying attention to maps and borders.\""
ga "\"Oral history would always be more important, and we had that too.\""
ga "\"Conquerors came with flags telling us where we could and couldn’t be.\""
ga "\"And not just one flag, either.\""
ga "\"No, there were many flags.\""
ga "\"But that’s less relevant.\""
ga "\"What was relevant was that maps and borders became necessary to avoid wanton death.\""
ga "\"My father, who was a descendant of one of these original warriors, or so he said, kept a lot of these maps, and updated them as they changed.\""
ga "\"Usually his concerns were the locations of the hostile armed colonies.\""
ga "\"But he had a hobby of marking down the bonfires over the years.\""
ga "\"I think it was just a thing that put his mind at ease.\""
ga "\"Just a thing to do.\""
ga "\"But over time, he felt less at ease.\""
ga "\"Because he found thousands of those sites.\""
"Gad reaches behind him and opens a wooden trunk."
stop music fadeout 10.0
"He rifles through some cloth, and some satchels, until he pulls out a cylindrical container..."
"He plucks what looks to be a folded piece of animal skin and starts to unfold it on his lap."
window hide
scene bg hoganmap with slow_dissolve
pause
window show
"I see drawings of rivers, names of places, and topographies."
"But the other thing I see is little red X’s marked on the skin."
"So many little red X’s."
play music "music/contemplation.ogg" fadein 2.0
ga "\"Strange that when you look at so many of the fires put on a map... they never appear inside the circle.\""
"What... the fuck?"
"What the FUCK?"
"It’s quiet enough in the room to hear the insects outside right now."
"But Murdoch’s making a clicking sound."
"I turn to look at him."
"It’s the sound of his teeth clicking together inside of his mouth."
"He's shaking."
ga "\"On a map, the people in Echo say that the border of their territory looks like a strange shape.\""
ga "\"But the Meseta know...\""
ga "\"...that it is a circle.\""
scene bg hoganinsidenight with slow_dissolve
"Manaba grabs Gad’s shoulder tightly."
stop music fadeout 4.0
"She crouches down, as if to whisper in his ear."
"Then she plants a kiss on his cheek."
"Gad starts laughing as Manaba brings him to his feet."
ga "\"So it’s like I said...\""
ga "\"...I can tell you the things we know about the outside of that place.\""
ga "\"But we will remain willingly ignorant of what is inside.\""
ga "\"I’ve had enough of stories tonight, let’s play some music!\""
cl "\"Music, you say?\""
"He perks up, paws folded in his lap."
ga "\"Good ears on this one. Yes, music.\""
cl "\"Pardon, sir. It's just that — despite all my years of research on the subject, I've never heard a Meseta song before.\""
ga "\"Research?\""
"He gives Cliff a puzzled look. The weasel's face falls, wringing his paws, brows twitching."
show cli adv blush eyes right at center,hogannight with dissolve
cl "\"I, uh, it's for... how do I put this...\""
"Avery raises a hand."
show ave serious talking at right,hogannight with dissolve
av "\"Mr. Tibbits here's writing a, a... book about the region, Pa.\""
hide cli with dissolve
hide ave with dissolve
ga "\"I see.\""
"Gad seems content with that answer, but the look on Manaba's face tells me she isn't buying it one bit."
show mur talking at center,hogannight with dissolve
mu "\"I think we could all use some music after today.\""
show mur with dis
"Saved by the fox."
show mur concerned d with dis
mu "\"Aren't you curious about the music, Sam?\""
"He gives me a pleading look."
hide mur with dissolve
"I nod, even though my mind's on anything but music right now."
"My eyes fall on the map, packed away in its cylindrical container once more."
"An entire region so unnatural these folks don't even want to talk about it..."
"What even is Echo?"
ga "\"That settles it, then!\""
ga "\"We have some time until dinner.\""
"The old elk turns his head to Manaba."
ga "\"Will you join me, my dear? You know the words better.\""
ma "\"Will you be able to keep up this time?\""
ga "\"I can try.\""
"Gad smiles at her, and Manaba responds in kind."
"He takes a wooden flute from a table and puts it to his lips. It looks small in his massive hands."
"Cliff watches the two intently, jaw slack, eyes wide, like he's in a trance."
"The bear and the kit fox, who had been whispering amongst themselves moments before, fall silent as well."
"Before long, I only hear the cicadas buzzing outside."
play music "music/hogan.ogg" fadein 3.0
"The flute's sound rings loud through the hogan as Gad plays the first notes of his song."
"Putting her hand on his shoulder, Manaba joins him, gently swaying as she sings."
"While I can scarcely understand what she's singing about, her voice is beautiful, and I can feel my fur standing on end just listening to her."
"It's better than any song I've heard the drunks sing at the Hip, that's for damn sure."
"The image of the map slips from my mind. I take a deep breath."
"Gad's fingers flit across the flute as he tries to keep up once Manaba reaches what I assume is the chorus."
"The size of his hands isn't making it easy on him."
"I close my eyes and listen."
"My mind wanders."
"For the first time in days, if not weeks, the thought of what happened in the mine leaves the space in the back of my mind."
"I feel lighter somehow."
"A little part of me hopes they don't stop playing."
stop music fadeout 4.0
stop background fadeout 4.0
scene black with slow_dissolve
pause
play background "sfx/bonfire.ogg" fadein 12.0
unk "\"I think he's fallen asleep.\""
unk "\"Sam?\""
scene bg hoganinsidenight with slow_dissolve
"I can hardly suppress a yawn when I open my eyes again."
"A strand of drool hangs from my muzzle, and I smear it away with one sleeve, rubbing my eyes with the other before the hogan finally comes into view."
show ave at center,hogannight with dissolve
"Avery sits in front of me, a bowl full of food in each hand. He extends one to me, and smiles."
"I yawn."
m "\"What time is it?\""
show ave thinking eyes with dissolve
av "\"Eight, I reckon?\""
show ave serious talking with dissolve
play music "music/avery.ogg" fadein 10.0
av "\"You've been out for about an hour, in any case.\""
show ave talking with dis
av "\"You were sleeping so soundly, we didn't want to wake you.\""
show ave with dis
m "\"Where is everyone?\""
show ave serious talking with dis
av "\"They're outside. Now eat.\""
hide ave with dissolve
"I take a piece of bread from the bowl and bite down without thinking."
"It's crisp and crunchy."
"I shovel more of it into my mouth, along with some red-looking thinly sliced vegetables I see."
"There's a flavor to them can't quite describe, at least until my eyes begin to water and my face heats up like a fireplace."
"I've heard about these before."
"Habanero peppers."
"I'd forgotten about the peppers."
"I swallow, which only makes it worse."
"I like my food spicy but this is just too damn much."
"Feels like there's a wildfire raging in my throat."
"Avery laughs at my sloppy coughing fit, fetching what looks like a pitcher of water next to him."
show ave wink talking at center,hogannight with dissolve
av "\"Careful, now. It's spicy.\""
show ave wink with dis
"I keep hacking."
m "\"You could've told me.\""
show ave doubt talking with dis
av "\"I would have if you'd waited a second.\""
show ave shocked with dis
"I take the pitcher from him, pouring a few cups' worth of cool water down my throat."
"Some of it leaks down the side of my muzzle, droplets staining my already dirty shirt."
"It extinguishes the fire burning in my throat, and I'm left with a pleasant aftertaste."
"But then it's back, and my eyes water again."
"Ugh."
"Right. I put some of the bread in my mouth to soak up the heat."
"I inspect the peppers closely."
show ave thinking flirty with dissolve
av "\"Packs way more of a punch than the stuff they serve at the Hip, right?\""
m "\"Tell me about it.\""
"I take another bite. This time I'm more careful."
"It's good in tiny bites. Really good."
"And the fish is even better."
"I could get used to this."
show ave serious talking with dissolve
av "\"Once you've finished up, I got some old clothes for you to try on.\""
show ave serious with dis
"Anything beats these rags."
m "\"Are your parents okay with it?\""
show ave wink talking with dis
av "\"Oh, they don't have to be. These are the clothes I used to wear at the ranch. Last time I wore them was almost a decade ago.\""
show ave with dis
"He starts on his own food, eating nearly the entire cut of fish as well as most of the peppers in a single bite."
show ave serious talking with dis
av "\"Didn't check for holes. I hope the moths haven't gotten to...\""
show ave shocked with dis
"He stops mid-sentence. His glasses slip down his large snout as his eyes bug out."
show ave thinking shocked with dissolve
"He gasps."
"He coughs."
"I see tears welling up in the corner of his eyes."
show ave shocked with dissolve
"Wordlessly, he yanks the pitcher from my hand, dipping a piece of bread in it and stuffing it into his mouth."
"When it's finally died down, he looks at me, panting, sweat running down his forehead."
"He narrows his eyes."
show ave angry talking with dis
av "\"Not. A. Word.\""
show ave angry with dis
"I smirk back at him."
m "\"I wasn't going to say anything.\""
show ave serious eyes talking with dis
av "\"You're many things, but you're not a good liar.\""
show ave serious with dis
"I can't resist."
m "\"Packs more of a punch than the stuff they serve back home.\""
show ave eyes talking with dis
av "\"Ha!\""
show ave eyes with dis1
show ave eyes talking with dis
av "\"Too clever for your own good.\""
show ave serious with dis
"He sets the bowl down and reaches behind him, taking out a white shirt and a pair of overalls."
"They look a little large, even for me."
m "\"Thanks. I'm sure these will do nicely.\""
show ave serious talking with dis
av "\"Let me know if you find any holes. If there's one thing I'm good at, it's stitching.\""
show ave serious with dis
m "\"Alright. By the way...\""
show ave doubt talking with dis
av "\"Yeah?\""
show ave doubt with dis
"I swallow the last piece of fry bread, setting the bowl aside."
stop music fadeout 10.0
m "\"The map. What your father said — is that all true?\""
show ave thinking shocked with dissolve
m "\"Is Echo really—\""
"I stop, watching Avery's eyes dart around the room."
show ave thinking scared with dis
av "\"I don't think we should talk about it here.\""
m "\"I'm sorry.\""
show ave serious talking with dissolve
av "\"It's alright. We can talk on the road, yeah?\""
show ave serious with dis
m "\"You're coming with us?\""
show ave serious talking with dissolve
av "\"With all that's...\""
show ave serious with dissolve
"He clears his throat."
show ave thinking eyes with dissolve
av "\"...transpired, I think there's safety in numbers.\""
show ave talking with dissolve
av "\"And I can't just leave Jebediah behind.\""
av "\"Or you, for that matter.\""
show ave with dis
m "\"Won't they miss you at your clinic?\""
show ave thinking flirty with dissolve
av "\"I make these trips all the time. My assistant's skilled enough to handle things in my absence.\""
show ave thinking eyes with dis
av "\"You're headed for the settlement, yeah?\""
m "\"Yeah. You ever been?\""
show ave serious talking with dissolve
av "\"Used to visit all the time.\""
show ave serious with dis
"Maybe I can get some information out of him."
m "\"Anything we should look out for?\""
"He frowns."
show ave angry talking with dis
av "\"Well, maybe not for you.\""
play music "music/hoganstory.ogg" fadein 2.0
av "\"In Echo the hatred's behind closed doors. The settlement's more of a valley of rattlesnakes.\""
show ave angry with dis
m "\"No one's really told me anything about it.\""
m "\"Not even Cynthia.\""
show ave thinking sad with dis3
av "\"I can imagine. The state of that place now's just a reminder of all the things we've come to lose.\""
show ave thinking look with dis
av "\"Losses too many of my relatives would rather not speak of.\""
show ave serious talking with dis3
av "\"And they're doing this all out in the open, too.\""
show ave serious with dis
m "\"They?\""
show ave serious talking with dis
av "\"The ones in charge.\""
show ave serious with dis
"His voice gets shakier with every word."
show ave thinking sad with dis3
av "\"Our sacred places were taken from us.\""
show ave angry with dis3
av "\"Men and women, taken from us.\""
show ave thinking look with dis3
av "\"Children...\""
show ave thinking sad with dis
av "\"Taken from us.\""
av "\"Even our way of life.\""
show ave angry with dis3
av "\"And they continue to take until there's nothing left.\""
show ave thinking look with dis3
"He pauses, tapping his chin and shaking his head like he’s trying to shrug off a bad dream..."
show ave angry talking with dis3
av "\"But maybe it's just this distant thing. But for us, it's our past, present and future.\""
show ave serious with dis
"No wonder Cynthia never talks about it."
show ave doubt talking with dis
av "\"Some of us, like myself and your friend Cynthia, are doing what we can to - in a way, move past it.\""
av "\"But when your own people try to push away the thought of a gaping wound like that, it'll begin to fester sooner or later.\""
show ave serious talking with dis
av "\"Your friend, Mr. Tibbits. I hope he'll come to realize, too.\""
show ave thinking sad with dis3
av "\"That we are a people, not curiosities to be cataloged.\""
"I struggle to form a reply. In the end, I just stay silent."
"He stares at his feet for a long time, finally getting up with a grunt."
show ave thinking look with dis
av "\"I'll be outside.\""
hide ave with dissolve
"He pushes his glasses up to his brows with a trembling hand."
m "\"I don’t know how to help you.\""
"It feels stupid, but it's the one thing I can think to say in a situation like this."
av "\"It's quite alright that you can't. I need some... fresh air.\""
stop music fadeout 3.0
"The elk exhales through his nostrils, turns, and walks out of the hogan, taking our empty bowls with him."
"I can hear the crickets before he closes the door."
"Alone again, I look up at the stars through the hole in the roof."
"There's a lot I want to ask Cynthia about if I ever see her again."
"I shake my head, trying my best not to dwell on it."
"Taking the clothes Avery left behind for me, I start getting changed."
"I've worn these clothes for so long now that taking them off almost feels like I'm peeling off a layer of skin."
"They're so tattered at this point I might as well throw them into the fire in front of me."
"Starting to sound like Cliff, but I'd kill for a nice bath right now."
"The overalls are a bit baggier than I'm used to, but at least they don't slip off or hang too low."
"They're easy to move around in, at any rate."
"I get up and walk a few paces around the still roaring fire, warming my bones a little now that it's gotten chilly out."
play music "music/contemplation.ogg" fadein 3.0
"Something clicks in my mind as I pace through the room."
"I consider my options and look around."
"I know I told Cliff that I'd part when we got to the reservation..."
"But I could run now."
"Everyone’s distracted."
"I’m fed. Clothed."
"Doubt they’d see me in the dark."
"If I can get my hands on that map, I can probably make it out of the forest on my own."
"That creature might still be around, but I’ll have to take my chances."
"No way they'll follow me if it is."
"I reach for the map in the cylindrical holder next to Gad’s seat."
"I take it out and unfurl it."
scene hoganmap with fade
"Where are we now?"
"I run a finger across all the red markings, looking for any indication until I spot a black one among them."
"That must be it."
"That means Camp Rosa to the east must be my best shot."
"Could get to Providence from there. Follow the stream."
"All I have to do is figure out where east is."
"I know Cliff has a compass. I watched him pack before we left Echo."
"He probably has some other supplies I could use, too."
"Food. Bandages. Anything."
scene hoganinsidenight with fade
menu maphogan1 :
    "Take the map":
        $ HaveMap = True
        "I take it, open Cliff's pack up, and stuff the map inside, placing the cylindrical container back exactly where Gad left it."
        "I can’t take any chances."
        "I sling the pack over my shoulder."
    "Leave the map":
        $ HaveMap = False
        "I just can't just take the map with me."
        "Avery helped me."
        "His family helped me."
        "This isn't mine."
        "I carefully roll it back up and put the cylindrical container exactly where Gad left it."
        "I sling the pack over my shoulder."
"There’s no turning back now."
"I have to—"
play sound "sfx/doorcreakopen.ogg"
"The door opens without warning."
cl "\"Samuel!\""
stop music fadeout 2.5
play sound "sfx/doorcreakclose.ogg"
"Shit."
"The weasel stands there, in the doorway, frozen."
show cli adv shocked at center,hogannight with dis3
cl"\"What are you doing?\""
show cli adv doubt with dis3
cl"\"Is that my pack?\""
"The weasel slinks closer, step by step, wary."
"He looks me up and down."
"His brow furrows."
m"\"I was just about to—\""
show cli adv sad with dis3
cl"\"Steal my things and leave?\""
"He sounds more confused than angry."
"Sad, even."
show cli adv angry with dis3
cl"\"Explain yourself.\""
cl"\"Now.\""
m"\"It’s not what you think it looks like. I ain’t—\""
"I stop."
"I can't keep doing this."
"I drop the pack."
m "\"I can’t stay here.\""
"I catch myself breathing hard."
"He raises a brow."
show cli adv sad with dis3
cl "\"What's wrong?\""
hide cli with dissolve
"I turn away. Anything to avoid looking into those big blue eyes of his."
m "\"It's... it ain't anything for you to worry about.\""
cl "\"I think it's obvious that this is not nothing, Sam.\""
cl "\"I thought we had talked about this.\""
m "\"I know.\""
m "\"We did.\""
cl "\"Then as your employer, I think it's in my best interests to know.\""
"I feel a warm paw on my back."
"Rubbing in circles."
"I take a deep breath."
"No use hiding it now, even if I wanted to."
m "\"I’m not staying with you a second longer.\""
"The weasel lets out a small gasp."
cl "\"W-What do you mean?\""
m "\"I have to go.\""
cl "\"You -- you can't just up and leave! We're making history here!\""
m "\"You don't understand.\""
"I raise my voice so I can hear myself over the sound of my brain going a hundred miles a minute."
m "\"I can't go to that reservation. If I do, I'll probably get caught and have to go back to Echo, and something bad'll happen to me.\""
"Just like in my dream."
"My lips feel dry."
"There's a pit in my stomach."
cl "\"What... are you even saying, Sam?\""
"He's speaking louder too."
cl "\"If there's -- if there's any—\""
m "\"A man died because of me, Cliff!\""
m "\"The miner who got murdered.\""
m "\"I'm the one who...\""
"I can't even get it out without feeling like I'm going to vomit up my dinner."
play music "music/mellowpiano.ogg"
m "\"I'm the one who did it.\""
"He's quiet for a moment."
"I hear a shuddering breath."
cl "\"You're serious, aren't you?\""
"His voice is hoarse now."
"I look back at him, over my shoulder."
"His brows are furrowed."
"I don't know if he's angry, or sad, or if he hates me now."
"For the first time, he's a mystery to me."
"He rubs his temples."
cl"\"Heaven’s sake, Sam...\""
m "\"He... he was a customer of mine. Promised me the world.\""
cl "\"He was?\""
m "\"He t-t-t-took me down to the mines. I trusted him. I can't believe I trusted him.\""
"Tears are rolling down my cheeks."
m "\"He tried to rob me. Attacked me and left me for dead.\""
m "\"I-I never meant to kill him.\""
"I try to slow my breathing."
m "\"I couldn't tell anyone. I just couldn't.\""
m "\"I didn't know what to do.\""
m "\"I just wanted to run.\""
m "\"Ever since we left town, I've been thinking of running away.\""
m "\"I'm a dead man standing.\""
cl "\"Sam...\""
"I hear the cicadas chirp outside."
"I want him to say something. Anything."
"Just when I'm about to turn, Cliff surges forward, wrapping his arms around me to the best of his ability."
cl "\"I had no idea you went through so much.\""
"His voice is muffled by my shirt."
"His tone is soft, gentle."
cl "\"You're alive so long as I have anything to say about it. I doubt any man would know what to do in your situation.\""
m "\"Y-you're not angry?\""
"I was expecting him to be."
"Almost hoping he would be."
"That would make all of this easier."
"Just so I wouldn't feel as guilty as I do now."
cl "\"Angry? No. That's not... one of the emotions I feel right now.\""
m "\"But I... I, Cliff, I killed someone. Tried to run away with your things. I'm a monster.\""
cl "\"If what you're saying is true, if he did try to rob you, if he did hurt you - I think you were right to defend yourself.\""
cl "\"I know you are a good man, Samuel.\""
"Hearing that only makes me cry harder."
"He's quiet for a long moment, his arms still wrapped around me."
cl "\"If you really think it right to leave, as much as it pains me, I will not stop you, nor will I report you to any authorities.\""
cl "\"I only implore you to stay with us until it's safe.\""
cl "\"I do not think I could rest easy sending you off into the great unknown while that creature is still roaming about.\""
"I wipe my eyes dry, sniffling one last time before finally turning around."
show cli adv blush eyes right at center,hogannight with dissolve
m "\"Thank you.\""
show cli adv happy with dis3
cl "\"Please. If it hadn't been for you, I think I'd have been dead several times over by now.\""
cl "\"I should be the one thanking you.\""
"I finally return the smile he gave me, cupping his cheek in my paw and feeling the heat against my paw pads."
"He puts his paw on mine."
"His whiskers tickle my wrists."
show cli adv talking with dis3
cl "\"I won't tell Murdoch or the others. You have my—\""
hide cli with dissolve
"I lean down and kiss him."
"Not because I have to, not because I'm getting paid to, not because I have to maintain a charade."
"This time, it's because I want to."
"He tastes like peppers."
"When I pull back, he looks more than a little dazed."
show cli adv blush eyes closed at center,hogannight with dissolve
cl "\"...You have my word.\""
hide cli with dissolve
"He leans forward to give me another peck on the lips."
"It's one I return."
"I hold him in my arms like that for a good while as we watch the fire burn together."
cl "\"...You know, Sam...\""
"I stir and rumble."
m "\"Mmm?\""
"His voice lowers to a whisper."
cl "\"If you really think that the map will help us, I won't tell anybody about that either.\""
m "\"I...\""
"It dawns on me now that he's talking about the fact that the map is still hanging out of its case in the open."
"I had completely forgot about it."
cl "\"But if you're going to put it back, then you should do that quickly.\""
cl "\"We wouldn't want our group to fracture over such a paltry misunderstanding as that.\""
"I didn't think we'd need it anymore?"
"But now I have doubts again."
"We got lost so easy the first time."
"If I end up on my own again I can't rely on anybody else."
cl "\"Whatever you choose to do, I won't judge you.\""
menu maphogan2 :
    "Take the map":
        $ HaveMap = True
        "I can't get lost in that forest again."
        "And I think Cliff knows I'll have to make a break for it if I do run into any trouble at the reservation."
        "I tuck it out of site and into our equipment as fast as we can."
        "I can't read Cliff's expression."
        "His glare is obscured by the firelight bouncing off of his glasses."
        "But I curl up against him and drift off to sleep."
    "Leave the map":
        $ HaveMap = False
        m "\"No.\""
        "It was wrong before."
        "It's wrong again now."
        "This isn't just a map."
        "It's their family history."
        "I thought that Cliff would be the most sensitive to that."
        "More so out of anybody in our group."
        "But maybe he really does care about me that much."
        "So much that he would cast his principles aside."
        "I don't know."
        "I can't read Cliff's expression."
        "His glare is obscured by the firelight bouncing off of his glasses."
        "But I curl up against him and drift off to sleep."



stop music fadeout 5.0
stop background fadeout 4.5
scene black with slow_dissolve
scene hoganoutside with slow_dissolve
play background "sfx/birds.ogg" fadein 7.0
show ave serious talking at center with dissolve
av "\"We're all set to go, yeah?\""
show ave serious with dis
"The birds have only just started singing when we leave the dwelling."
"Once again, we're walking at the crack of dawn."
"This time, I feel much better, even if sleeping with nine people in one tiny room is much more cramped than I'd have liked."
"Cliff's stuck close to me this morning, even moreso than usual."
"True to his word, he hasn't spoken to anyone about what we discussed."
"In fact, he's acting like last night never happened."
"And I think I prefer it like that."
"As for the forest, it's a lot more peaceful than it felt the day before."
"Our better spirits probably play a large part in that..."
"Jeb addresses Avery's hanging question, looking winded from all the packing he's done."
show jeb talking at left with dissolve
jeb "\"Think so.\""
show jeb
show ave thinking eyes with dissolve
av "\"Let's hope the woods cooperate today, eh?\""
hide ave
hide jeb
with dissolve
"Gad follows us out, looking at us from the doorway."
"Manaba stands next to him. Her expression is hard to read - she almost looks relieved."
ga "\"I suppose this is where we say our goodbyes.\""
av "\"I'll be back before you know it.\""
"As soon as he sees them, Cliff pushes past us, briskly walking over to the pair."
"He extends a hand."
"Gad takes it with some hesitation."
show cli adv happy with dissolve
cl "\"Thank you so much for letting us stay in your beautiful home.\""
cl "\"I shall carry this experience with me for the rest of my life.\""
"He's laying it on thick, for sure."
ga "\"Be safe on your travels.\""
"The weasel shows his toothiest grin."
show cli adv talking with dis
cl "\"Oh, we shall.\""
hide cli with dissolve
"They shake paws, after which Cliff walks back on over to us."
show ave thinking at center with dissolve
av "\"You boys know where your camp is?\""
"Jebediah nods his head."
show jeb at left with dissolve
show jeb talking with dis
jeb "\"I always camp in the same spot. It's about a day's travel from the settlement.\""
show jeb with dis
show ave serious talking with dissolve
av "\"Right. We'll have to be careful. There's no telling what we'll find out there.\""
show ave thinking with dissolve
"He rubs the bridge of his snout with a small sigh."
show ave thinking eyes with dis
av "\"And even if we get there unscathed, we'll still need to take inventory.\""
m "\"What do you mean?\""
show jeb sad talking with dis
jeb "\"Without the donkeys and the wagon, there's no way we're going to be able to get all of our supplies to the settlement.\""
show jeb sad with dis
"He looks down."
show jeb talking with dis
jeb "\"There's only so much we can carry ourselves.\""
show jeb with dis
show mur concerned d at right with dissolve
mu "\"That's assuming everything's still in one piece.\""
hide mur
hide ave
hide jeb
with dissolve
show cli adv sad at center with dissolve
cl "\"Even if we carry as much as can, will we have enough supplies for the journey back?\""
cl "\"We don't know if we can restock at the settlement.\""
show ave thinking eyes at right with dissolve
av "\"Hard to say.\""
hide cli
hide ave
with dissolve
"Everyone goes quiet."
show mur talking at center with dissolve
mu "\"We don't really have a choice, do we?\""
show mur with dissolve
show jeb talking at right with dissolve
jeb "\"Worst case scenario, we'll have to live off the land. Berries and mushrooms aplenty if you know where to look.\""
show jeb with dis
show jeb talking with dis
jeb "\"Many poisonous ones, too, if you don't.\""
show jeb with dis
show mur concerned d with dis
"Murdoch whistles."
show mur sideeye with dis
mu "\"I almost thought we ran out of deadly things to find in this forest.\""
show mur eyes with dis
m "\"Seems it still has some surprises in store.\""
show mur talking with dis
mu "\"We might want to pack extra water to prepare for the heat.\""
show mur with dis
m "\"Still chilly out. We should be good for a while.\""
show mur talking with dis
mu "\"Until noon comes around, yes.\""
show mur smile with dis
show mur sideeye with dis
mu "\"After that...\""
show cli adv talking at left with dissolve
cl "\"Let's be off, then, before it gets too warm.\""
hide cli
hide mur
hide jeb
with dissolve
"He turns his head to wave at Avery's parents, but they've already closed the door to the hogan."
stop background fadeout 3.0
scene bg forestmorning with fade
play music "music/forestambience.ogg" fadein 5.0
"Following one of Avery's maps, we get back on the trail, Avery and Jebediah leading the group."
"Jebediah says we need to follow it until we reach the third fork in the road, about a couple of hours of walking at a leisurely pace."
"Thankfully, the air's still cool, which makes it a lot easier and far less sweaty."
"I'm walking between Murdoch and Cliff while the bear and kit fox keep a steady pace in front of us."
"I still don't remember their names."
"There's plenty of plump huckleberry bushes on the way."
"Birds singing in the distance and the slow trickle of water beside us are music to my ears."
show mur talking at center,forest
show expression AlphaMask("foliage", At("mur talking", center)) as mask:
    alpha 0.35
with dissolve
mu "\"You're actually smiling?\""
show mur
show expression AlphaMask("foliage", At("mur", center)) as mask:
    alpha 0.35
with dis3
"It takes me a moment to realize he's talking to me."
"I didn't even know I was smiling."
show mur sideeye
show expression AlphaMask("foliage", At("mur sideeye", center)) as mask:
    alpha 0.35
with dis
"I stop smiling."
show mur eyes
show expression AlphaMask("foliage", At("mur eyes", center)) as mask:
    alpha 0.35
with dis
mu "\"Well that didn't last long.\""
m "\"Yeah, yeah. You should count yourself lucky I ain't chargin' you to see it.\""
show mur talking
show expression AlphaMask("foliage", At("mur talking", center)) as mask:
    alpha 0.35
with dis
mu "\"It must have something to do with getting good food and rest for a change.\""
show mur mischief
show expression AlphaMask("foliage", At("mur mischief", center)) as mask:
    alpha 0.35
with dis
mu "\"Certainly couldn't have anything to do with Cliff here stopping by when you two were alone last night, now, could it?\""
show mur sideeye
show expression AlphaMask("foliage", At("mur sideeye", center)) as mask:
    alpha 0.35
with dis
show cli adv shocked at right,forest
show expression AlphaMask("foliage", At("cli adv shocked", right)) as mask2:
    alpha 0.35
with dissolve
cl "\"I was merely getting some things from my pack!\""
show cli adv blush eyes right
show expression AlphaMask("foliage", At("cli adv blush eyes right", right)) as mask2:
    alpha 0.35
with dis3
cl "\"I'd misplaced the rag I normally use to clean my glasses, see, and—\""
show mur mischief
show expression AlphaMask("foliage", At("mur mischief", center)) as mask:
    alpha 0.35
with dis
mu "\"Stayed inside for a solid hour?\""
show cli adv blush eyes closed
show expression AlphaMask("foliage", At("cli adv blush eyes closed", right)) as mask2:
    alpha 0.35
with dis
cl "\"It was hard to find...\""
show mur eyes
show expression AlphaMask("foliage", At("mur eyes", center)) as mask:
    alpha 0.35
with dis
mu "\"You can tell me the truth, you know. I won't cast judgement.\""
show mur
show expression AlphaMask("foliage", At("mur", center)) as mask:
    alpha 0.35
with dis
"Cliff hushes Murdoch louder than he was talking just now."
show cli adv blush eyes left
show expression AlphaMask("foliage", At("cli adv blush eyes left", right)) as mask2:
    alpha 0.35
with dis
cl "\"Quiet down, they'll hear you.\""
show mur eyes
show expression AlphaMask("foliage", At("mur eyes", center)) as mask:
    alpha 0.35
with dis
"The fox shrugs."
show mur talking
show expression AlphaMask("foliage", At("mur talking", center)) as mask:
    alpha 0.35
with dis
mu "\"So now you care about being quiet.\""
show mur
show expression AlphaMask("foliage", At("mur", center)) as mask:
    alpha 0.35
with dis1
hide mur
hide mask
show cli adv shocked
show expression AlphaMask("foliage", At("cli adv shocked", right)) as mask2:
    alpha 0.35
with dis3
"The weasel looks away, red as a beet, nearly tripping over a branch on the road while he isn't paying attention."
"The kit fox overhears and turns. He looks a little angry."
show tse surprised at left,forest:
    xzoom -1
show expression AlphaMask("foliage", At("tse surprised", right)) as mask3:
    alpha 0.35
    xzoom -1
with vpunch
ts "\"Careful!\""
show cli adv blush eyes closed
show expression AlphaMask("foliage", At("cli adv blush eyes closed", right)) as mask2:
    alpha 0.35
with dis3
cl "\"Terribly sorry!\""
show tse angry talking
show expression AlphaMask("foliage", At("tse angry talking", right)) as mask3:
    alpha 0.35
    xzoom -1
with dis
ts "\"Just watch where you're walking. One thing to trip over a branch. Snakes tend not to like being stepped on.\""
show tse angry
show expression AlphaMask("foliage", At("tse angry", right)) as mask3:
    alpha 0.35
    xzoom -1
with dis
cl "\"I'll be more careful in the future, um...\""
"It takes the kit fox a second and another 'um' from Cliff to realize he's waiting on a name."
show tse talking
show expression AlphaMask("foliage", At("tse talking", right)) as mask3:
    alpha 0.35
    xzoom -1
with dis
ts "\"I'm Tsela.\""
show tse angry
show expression AlphaMask("foliage", At("tse angry", right)) as mask3:
    alpha 0.35
    xzoom -1
with dis
show yis smile at center,forest
show expression AlphaMask("foliage", At("yis smile", center)) as mask4:
    alpha 0.35
with dis3
"He points at the bear walking beside him with his thumb."
show tse talking
show expression AlphaMask("foliage", At("tse talking", right)) as mask3:
    alpha 0.35
    xzoom -1
with dis
ts "\"The bear's name is Yiska.\""
show cli adv happy
show expression AlphaMask("foliage", At("cli adv happy", right)) as mask2:
    alpha 0.35
with dis
show tse
show expression AlphaMask("foliage", At("tse", right)) as mask3:
    alpha 0.35
    xzoom -1
with dis
cl "\"Tsela and Yiska. Got it!\""
cl "\"They're lovely names. Are you two from the settlement?\""
show tse talking
show expression AlphaMask("foliage", At("tse talking", right)) as mask3:
    alpha 0.35
    xzoom -1
with dis
ts "\"It's where we were born and raised.\""
show tse
show expression AlphaMask("foliage", At("tse", right)) as mask3:
    alpha 0.35
    xzoom -1
with dis
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", right)) as mask2:
    alpha 0.35
with dis
cl "\"You must have a lot of stories to tell!\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", right)) as mask2:
    alpha 0.35
with dis
show tse angry talking
show expression AlphaMask("foliage", At("tse angry talking", right)) as mask3:
    alpha 0.35
    xzoom -1
with dis
ts "\"Not any I'd share with someone like you.\""
show tse angry
show expression AlphaMask("foliage", At("tse angry", right)) as mask3:
    alpha 0.35
    xzoom -1
with dis
show cli adv eyes talking
show expression AlphaMask("foliage", At("cli adv eyes talking", right)) as mask2:
    alpha 0.35
with dis
cl "\"O-oh. I'm terribly sorry, didn't mean to offend!\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", right)) as mask2:
    alpha 0.35
with dis
"I feel my own lips purse."
"This is just getting awkward."
show yis talking
show expression AlphaMask("foliage", At("yis talking", center)) as mask4:
    alpha 0.35
with dis
ys "\"You apologize a lot.\""
show yis
show expression AlphaMask("foliage", At("yis", center)) as mask4:
    alpha 0.35
with dis
show cli adv blush eyes right
show expression AlphaMask("foliage", At("cli adv blush eyes right", right)) as mask2:
    alpha 0.35
with dis
cl "\"Oh-oh, pardon me...\""
show yis eyes talking
show expression AlphaMask("foliage", At("yis eyes talking", center)) as mask4:
    alpha 0.35
with dis
"Yiska says something in the Meseta language."
show yis eyes
show expression AlphaMask("foliage", At("yis eyes", center)) as mask4:
    alpha 0.35
with dis
show tse eyes smile
show expression AlphaMask("foliage", At("tse eyes smile", right)) as mask3:
    alpha 0.35
    xzoom -1
with dis
"Tsela replies, then laughs."
show yis talking
show expression AlphaMask("foliage", At("yis talking", center)) as mask4:
    alpha 0.35
with dis
ys "\"He did not mean to alarm you.\""
show yis angry
show expression AlphaMask("foliage", At("yis angry", center)) as mask4:
    alpha 0.35
show tse angry
show expression AlphaMask("foliage", At("tse angry", right)) as mask3:
    alpha 0.35
    xzoom -1
with dis1
hide yis
hide tse
hide mask3
hide mask4
with dissolve
show mur talking at left,forest
show expression AlphaMask("foliage", At("mur talking", left)) as mask:
    alpha 0.35
with dis3
mu "\"I keep hearing vague stories about this settlement, but I don't really know what to expect.\""
show mur
show expression AlphaMask("foliage", At("mur", left)) as mask:
    alpha 0.35
with dis1
show cli adv happy
show expression AlphaMask("foliage", At("cli adv happy", right)) as mask2:
    alpha 0.35
with dis3
cl "\"I know! Isn't it exciting?\""
"I think again about what Avery said back at the Hogan."
"He and Cliff really have different ideas about things."
m "\"Only thing I'm excited for is to be out of these woods.\""
"Never thought I'd be so sick of trees so fast."
"Murdoch smirks."
show mur mischief
show expression AlphaMask("foliage", At("mur mischief", left)) as mask:
    alpha 0.35
with dis
mu "\"I've grown content with it.\""
mu "\"Brushes with death aside, I got to do a season’s worth of nature photography in just a few days.\""
show mur
show expression AlphaMask("foliage", At("mur", left)) as mask:
    alpha 0.35
with dis
"He pats his trusty camera, still hanging 'round his neck as always."
"It's a wonder it hasn't gotten caught on any branches yet."
"It's just about the only thing of ours that got through this journey unscathed."
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", right)) as mask2:
    alpha 0.35
with dis
cl "\"And I could fill a book with all the things I learned yesterday alone.\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", right)) as mask2:
    alpha 0.35
with dis
"At least these two are having a good time."
hide cli
hide mur
hide mask
hide mask2
with dissolve
"I wonder how far we are from Echo."
"How far away we are from the circle."
"At the front of the group, I hear Jebediah and Avery chat amongst themselves."
show jeb talking at left,forest
show expression AlphaMask("foliage", At("jeb talking", left)) as mask5:
    alpha 0.35
show ave thinking at center,forest
show expression AlphaMask("foliage", At("ave thinking", center)) as mask6:
    alpha 0.35
with dissolve
jeb "\"You sure you're not just holding the map upside down again?\""
show jeb
show expression AlphaMask("foliage", At("jeb", left)) as mask5:
    alpha 0.35
show ave angry talking
show expression AlphaMask("foliage", At("ave angry talking", center)) as mask6:
    alpha 0.35
with dis3
av "\"That happened {i}once{/i}.\""
show ave angry
show expression AlphaMask("foliage", At("ave angry", center)) as mask6:
    alpha 0.35
with dis
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", left)) as mask5:
    alpha 0.35
with dis
jeb "\"One time too many. Took us half a day to make up for.\""
show jeb
show expression AlphaMask("foliage", At("jeb", left)) as mask5:
    alpha 0.35
with dis
show ave doubt talking
show expression AlphaMask("foliage", At("ave doubt talking", center)) as mask6:
    alpha 0.35
with dis
av "\"Cut me some slack, will ya, Jeb? That was three years ago.\""
show ave doubt
show expression AlphaMask("foliage", At("ave doubt", center)) as mask6:
    alpha 0.35
with dis
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", left)) as mask5:
    alpha 0.35
jeb "\"I would, if you'd bought me the drink you said you were gonna.\""
show jeb
show expression AlphaMask("foliage", At("jeb", left)) as mask5:
    alpha 0.35
with dis
"Cliff gestures to us."
cl "\"Excuse me for a moment.\""
"As he leaves me, Murdoch's tail sways back and forth, and he gives me a look."
"So I follow Cliff over to Avery and Jebediah, and the fox rolls his eyes."
"I don't think I could stand getting questioned by Murdoch if I was left alone with him right now."
show cli adv doubt at right,forest
show expression AlphaMask("foliage", At("cli adv doubt", right)) as mask2:
    alpha 0.35
with dissolve
cl "\"What's wrong?\""
"Avery turns his head with a sigh."
show ave thinking eyes
show expression AlphaMask("foliage", At("ave thinking eyes", center)) as mask6:
    alpha 0.35
with dis3
av "\"Jebediah here thinks I can't read a map.\""
show jeb doubt talking
show expression AlphaMask("foliage", At("jeb doubt talking", left)) as mask5:
    alpha 0.35
with dis
jeb "\"We were supposed to pass by a fork in the trail half an hour ago, but we haven't seen anything of the sort.\""
show jeb doubt
show expression AlphaMask("foliage", At("jeb doubt", left)) as mask5:
    alpha 0.35
show cli adv shocked
show expression AlphaMask("foliage", At("cli adv shocked", right)) as mask2:
    alpha 0.35
with dis3
cl "\"What?\""
show ave serious talking
show expression AlphaMask("foliage", At("ave serious talking", center)) as mask6:
    alpha 0.35
with dis3
av "\"We're going the right way. I know it.\""
show ave serious
show expression AlphaMask("foliage", At("ave serious", center)) as mask6:
    alpha 0.35
with dis
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", left)) as mask5:
    alpha 0.35
with dis
jeb "\"Like what happened yesterday?\""
show jeb
show expression AlphaMask("foliage", At("jeb", left)) as mask5:
    alpha 0.35
show cli adv sad
show expression AlphaMask("foliage", At("cli adv sad", right)) as mask2:
    alpha 0.35
show ave thinking eyes
show expression AlphaMask("foliage", At("ave thinking eyes", center)) as mask6:
    alpha 0.35
with dis3
av "\"It sure does feel like the forest itself is trying to steer us wrong.\""
show jeb doubt talking
show expression AlphaMask("foliage", At("jeb doubt talking", left)) as mask5:
    alpha 0.35
with dis
jeb "\"Or there's still the possibility that you can't read a map.\""
show jeb doubt
show expression AlphaMask("foliage", At("jeb doubt", left)) as mask5:
    alpha 0.35
with dis1
show jeb doubt talking
show expression AlphaMask("foliage", At("jeb doubt talking", left)) as mask5:
    alpha 0.35
with dis
jeb "\"There's also that.\""
show jeb doubt
show expression AlphaMask("foliage", At("jeb doubt", left)) as mask5:
    alpha 0.35
with dis1
hide jeb
hide ave
hide mask5
hide mask6
with dissolve
"The shit from yesterday again?"
"Can't be, could it?"
show mur concerned d at center,forest
show expression AlphaMask("foliage", At("mur concerned d", center)) as mask:
    alpha 0.35
with dissolve
mu "\"Or maybe there's something it wants us to see.\""
"Murdoch's voice and serious tone startle me."
"This tone is so different from the one he was using just minutes ago."
"This tone sounds more like the one he used at the campfire."
"I hadn't noticed him creeping up beside me."
m "\"...You think so?\""
show mur talking
show expression AlphaMask("foliage", At("mur talking", center)) as mask:
    alpha 0.35
with dis
mu "\"It almost feels like the forest led us to Avery's camp, and then to Avery's parents.\""
show mur fear d
show expression AlphaMask("foliage", At("mur fear d", center)) as mask:
    alpha 0.35
with dis
mu "\"I know it sounds ridiculous, but—\""
show cli adv happy
show expression AlphaMask("foliage", At("cli adv happy", right)) as mask2:
    alpha 0.35
with dis3
"Cliff laughs incredulously."
cl "\"Hogwash!\""
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", right)) as mask2:
    alpha 0.35
with dis3
cl "\"Are you suggesting the forest is alive somehow?\""
show mur concerned d
show expression AlphaMask("foliage", At("mur concerned d", center)) as mask:
    alpha 0.35
with dis
mu "\"Well, trees are certainly alive, but that’s not what I meant.\""
show cli adv eyes talking
show expression AlphaMask("foliage", At("cli adv talking", right)) as mask2:
    alpha 0.35
with dis
cl "\"What nonsense!\""
show cli adv eyes
show expression AlphaMask("foliage", At("cli adv eyes", right)) as mask2:
    alpha 0.35
with dis
show mur sideeye
show expression AlphaMask("foliage", At("mur sideeye", center)) as mask:
    alpha 0.35
with dis
mu "\"Well then, what does your scholar's intuition suggest?\""
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", right)) as mask2:
    alpha 0.35
with dis
cl "\"There has to be a logical explanation for this phenomenon.\""
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", right)) as mask2:
    alpha 0.35
with dis
cl "\"Trees don't just... uproot and migrate to a new location in the dead of night.\""
show mur concerned d
show expression AlphaMask("foliage", At("mur concerned d", center)) as mask:
    alpha 0.35
with dis
mu "\"Then what about the thing that raided our camp?\""
mu "\"We all saw something different. A rat. A fox.\""
show mur fear d
show expression AlphaMask("foliage", At("mur fear d", center)) as mask:
    alpha 0.35
with dis
mu "\"Sam here doesn't even know what he saw.\""
mu "\"Is there a logical explanation for that?\""
"The weasel falls silent."
hide mask
hide mask2
hide cli
hide mur
with dissolve
show ave serious talking at center,forest
show expression AlphaMask("foliage", At("ave serious talking", center)) as mask6:
    alpha 0.35
with dis3
av "\"Let's all keep a clear head here, now.\""
show ave serious
show expression AlphaMask("foliage", At("ave serious", center)) as mask6:
    alpha 0.35
with dis
"Next to us, Jebediah stops walking."
"Yiska bumps into him by accident, shoving him forward a little."
show jeb talking at right,forest
show expression AlphaMask("foliage", At("jeb talking", right)) as mask5:
    alpha 0.35
with dis3
jeb "\"Hold on. Do you see that?\""
show jeb
show expression AlphaMask("foliage", At("jeb", right)) as mask5:
    alpha 0.35
with dis
"He points up, behind the trees, a little off the trail."
"It looks like some sort of wooden roof."
"Another dwelling?"
show ave doubt talking
show expression AlphaMask("foliage", At("ave doubt talking", center)) as mask6:
    alpha 0.35
with dis
av "\"That is not supposed to be here.\""
show ave thinking scared
show expression AlphaMask("foliage", At("ave thinking scared", center)) as mask6:
    alpha 0.35
with dis3
av "\"I've been here more times than I can count, and that is not—\""
show jeb angry talking
show expression AlphaMask("foliage", At("jeb angry talking", right)) as mask5:
    alpha 0.35
with dis
jeb "\"Definitely looks like it is, though.\""
hide mask5
hide mask6
hide jeb
hide ave
with dissolve
show mur happy at center,forest
show expression AlphaMask("foliage", At("mur happy", center)) as mask:
    alpha 0.35
with dissolve
mu "\"I didn’t want to feel right this soon.\""
"He laughs softly."
show mur mischief
show expression AlphaMask("foliage", At("mur mischief", center)) as mask:
    alpha 0.35
with dis3
mu "\"Maybe they could make me a professor at that school of yours.\""
show cli adv shocked at right,forest
show expression AlphaMask("foliage", At("cli adv shocked", right)) as mask2:
    alpha 0.35
with dis3
cl "\"Sh-should we investigate, then?\""
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", right)) as mask2:
    alpha 0.35
with dis3
"His squeaking makes half of the words hard to understand."
show mur sideeye
show expression AlphaMask("foliage", At("mur sideeye", center)) as mask:
    alpha 0.35
with dis3
mu "\"Why so nervous? I thought everything had a logical explanation to it.\""
"He’s glaring at that house."
show cli adv eyes
show expression AlphaMask("foliage", At("cli adv eyes", right)) as mask2:
    alpha 0.35
with dis
cl "\"T-That's exactly why we should investigate!\""
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv eyes", right)) as mask2:
    alpha 0.35
with dis
"His bad attempt at a brave face ain't fooling anyone."
m "\"They might have supplies we can use.\""
show mur fear d
show expression AlphaMask("foliage", At("mur fear d", center)) as mask:
    alpha 0.35
with dis
mu "\"Or there might be a crazed hermit sharpening his axe by the front door!\""
show cli adv sad
show expression AlphaMask("foliage", At("cli adv sad", right)) as mask2:
    alpha 0.35
with dissolve
hide cli
hide mur
hide mask
hide mask2
with dissolve
stop music fadeout 15.0
play background "sfx/forestbirds.ogg" fadein 15.0
scene cabinfront with fade
"I think we all expected to see something closer to the house that belonged to Avery’s folks, but this is just a log cabin."
"Or what’s left of it."
"What used to be windows have cracked in their frame, and moss is eating away at the roof."
"The doorway is so warped that it’s slanted to the side."
show cli adv doubt at center,dark4
show expression AlphaMask("foliage", At("cli adv doubt", center)) as mask2:
    alpha 0.55
with dissolve
cl "\"What nature of desolation is this?\""
hide cli
hide mask2
with dissolve
"Cliff starts walking through the doorway."
m "\"Uh, wait.\""
"The weasel is already inside the building."
"The rest of us exchange glances."
show cli adv talking at center,dark4
show expression AlphaMask("foliage", At("cli adv doubt", center)) as mask2:
    alpha 0.55
with dis3
cl "\"Well? What are the rest of you waiting for?\""
hide cli
hide mask2
with dissolve
m "\"Y’all following him in?\""
show jeb angry talking at center,dark4
show expression AlphaMask("foliage", At("jeb angry talking", center)) as mask5:
    alpha 0.55
with dis3
jeb "\"Fuck no.\""
show jeb angry
show expression AlphaMask("foliage", At("jeb angry", center)) as mask5:
    alpha 0.55
with dis1
show jeb angry talking
show expression AlphaMask("foliage", At("jeb angry talking", center)) as mask5:
    alpha 0.55
with dis
jeb "\"The hell’s he thinking?\""
show jeb doubt
show expression AlphaMask("foliage", At("jeb doubt", center)) as mask5:
    alpha 0.55
with dis
m "\"Well, ah...\""
show ave thinking eyes at right,dark4
show expression AlphaMask("foliage", At("ave thinking eyes", right)) as mask6:
    alpha 0.55
with dis3
av "\"I doubt I could fit through the doorway.\""
show ave thinking sad
show expression AlphaMask("foliage", At("ave thinking sad", right)) as mask6:
    alpha 0.55
with dis
av "\"That structure doesn’t look safe.\""
show mur eyes at left,dark4
show expression AlphaMask("foliage", At("mur eyes", left)) as mask:
    alpha 0.55
with dis3
mu "\"I don’t mind risking it.\""
show mur sideeye
show expression AlphaMask("foliage", At("mur sideeye", left)) as mask:
    alpha 0.55
with dis
mu "\"Plus, if one of us hurts ourselves, we can help out the other.\""
hide mur
hide mask
with dissolve
"The fox walks up to the door frame and slips on through."
show ave thinking
show expression AlphaMask("foliage", At("ave thinking", right)) as mask6:
    alpha 0.55
with dis
av "\"Might as well scope out our surroundings while they're inside.\""
show jeb doubt talking
show expression AlphaMask("foliage", At("jeb doubt talking", center)) as mask5:
    alpha 0.55
with dis
jeb "\"Might as well nail a pair of wooden crosses to the trees 'cos goin' in there is thick as pigshit.\""
show jeb doubt
show expression AlphaMask("foliage", At("jeb doubt", center)) as mask5:
    alpha 0.55
with dis
"The bear and the kit fox talk to each other in the Meseta language."
show jeb doubt talking
show expression AlphaMask("foliage", At("jeb doubt talking", center)) as mask5:
    alpha 0.55
with dis
jeb "\"And what about you?\""
show jeb doubt
show expression AlphaMask("foliage", At("jeb doubt", center)) as mask5:
    alpha 0.55
with dis
m "\"Uh.\""
menu hh:
    "Follow Cliff and Murdoch":
        $ FollowCM = True
        m "\"This muscle ain't just for show. My client says he needs me, he needs me.\""
        show jeb doubt talking
        show expression AlphaMask("foliage", At("jeb doubt talking", center)) as mask5:
            alpha 0.55
        with dis
        jeb "\"Your funeral.\""
        show jeb doubt
        show expression AlphaMask("foliage", At("jeb doubt", center)) as mask5:
            alpha 0.55
        with dis
        show ave serious
        show expression AlphaMask("foliage", At("ave serious", right)) as mask6:
            alpha 0.55
        with dis3
        "Avery gives Jeb a look."
        show ave serious talking
        show expression AlphaMask("foliage", At("ave serious talking", right)) as mask6:
            alpha 0.55
        with dis
        av "\"First sign of trouble, just holler and we’ll be on over.\""
        show ave serious
        show expression AlphaMask("foliage", At("ave serious", right)) as mask6:
            alpha 0.55
        with dis1
        hide mask5
        hide mask6
        hide jeb
        hide ave
        with dis3
        "Jeb sulks away and Avery whispers to him in a stern tone."
        play background "sfx/cabininside.ogg" fadeout 1.0 fadein 0.5
        scene cabininterior1 with slow_dissolve
        "But I don’t waste any time walking up to the house, mostly because I want those two in and out of here fast."
        "The inside of this place has the sickly sweet smell of wood rot."
        "Shrivelled up pine nettles cover all but the last bit of dirty flooring."
        "When I step inside I can hear Murdoch and Cliff speaking, but their voices sound muffled, like they’re in another room."
        mu "\"It doesn’t look like anybody’s lived here for a long time.\""
        cl "\"Well there has to be something.\""
        "I turn a corner into a hallway, looking for doors or a stairwell, trying to follow their voices."
        "There’s isn’t much light in here."
        cl "\"Surely we’ll find a letter or an old newspaper if we look long enough.\""
        mu "\"Folks don’t always have access to print out in places like this.\""
        play sound "sfx/creekysteps.ogg"
        "Then I turn another corner."
        scene cabininterior2 with dissolve
        "The room looks similar to the front room, but there’s a busted wood stove and a broken table."
        "I’m surprised to see our kit fox friend Tsela sitting on a chair near the table."
        m "\"I thought you and your friend out there were givin' this place the evil eye?\""
        nts "\"You’ve never been away this long.\""
        "I stumble back when the fox’s voice is several timbres higher."
        "Now that I have a clearer look in the dark, I can tell he’s wearing a white button up shirt and slacks; much looser than Tsela’s leathers."
        $ renpy.music.set_volume(0.2, delay=15.0, channel='background')
        m "\"Uh, I’m sorry? I’ve never been here before, and I’ve never seen you.\""
        m "\"Me and my associates assumed this place was abandoned.\""
        m "\"We’ll be out of your hair in a spell.\""
        play music "music/horrorpiano.ogg"
        dkf "\"You’ve got a gun, don’t ya?\""
        "I actually don’t, but I don’t think I want to let him know that."
        "I’m starting to wonder if I should yell or not, but I see his hand placed beneath the table, and if I make a sudden move..."
        "I feel a pit form in my stomach."
        m "\"I don’t mean no harm.\""
        dkf "\"I always wanted to see a {i}real{/i} pistol.\""
        dkf "\"They say only the navy has access to those, and they’re faster than any piece of junk we could barter for around here.\""
        "Wait a minute."
        "I know that kinda voice."
        "That’s a flirtin’ voice."
        "Is this boy sick?"
        "Maybe he’s just feral?"
        dkf "\"Wait, where are you going?\""
        "My brow furrows at this queer kit fox, considerin’ I wasn’t going anywhere, but he’s getting up now."
        "When I see he wasn’t holding a gun, I back up."
        "He stands up and walks on over to a counter full of cobwebs with a large orb weaver spider on it."
        "I flinch when he puts his hand on the counter like it’s nothing and then sits on it."
        "The golden orb weaver is twitching in place; my guess would be from the sudden crowding."
        "At this point I don’t know if I should feel more bad for him or the spider."
        "The Hell is wrong with him?"
        "Is he confused?"
        dkf "\"I wouldn’t even have minded one of those crummy pepperbox models you hate so much.\""
        "No, he’s sad."
        "I can hear it now in his voice."
        "He’s sad."
        "Sad at me, like I’m the one who’s in the wrong."
        "Like I’m somebody who did something."
        "As if it’s my fault."
        dkf "\"You don’t tell me anything anymore.\""
        "He bends his neck, looking in a hanging cabinet space, pulling out a cup, pulling out plates, setting them beside him like he’s used to doing this all of the time."
        dkf "\"I thought you told me we could be different?\""
        "There he goes trying to guilt me about somethin’ again."
        "This boy I ain’t ever seen in my life."
        dkf "\"You know that if you don’t show me your world... the colonizer world, I mean, I’ll just end up seeing it for myself, anyhow.\""
        "That one was said all sing-song and teasy, which is exactly the tone I don’t want to hear from a stranger."
        dkf "\"I’m sorry. I was just trying to make you mad.\""
        "I’m just walking slowly backwards."
        dkf "\"I shouldn’t have said that.\""
        "The fox moves his paw down the front of his shirt."
        "He’s unbuttoning it."
        "His eyes look terrified. Like he’s about to beg me for something that he’s scared he won’t ever get back."
        dkf "\"I’ll even do that, you know.\""
        "His pants come off."
        m "\"No!\""
        m "\"You get the hell away from me!\""
        scene black with dissolve
        "I scramble down the hallway, running into the sides of the walls."
        m "\"CLIFF! MURDOCH!\""
        "Nobody answers."
        "The sound of my heart thumping in my chest drowns out the sound of him crying."
        stop music fadeout 5.0
        $ renpy.music.set_volume(1.0, delay=10.0, channel='background')
        "I feel like I’m getting turned around more than I should in a cabin this small, because I have to turn a few extra times to find the front room."
        scene cabininterior1 with dissolve
        "I don’t hear him come after me, so I know I should be relieved."
        "But I won't feel calm until I'm out of this place."
        "It's creepy what he said to me."
        "Almost like he was coercing me, a total stranger, into feeling how afraid he felt."
        "Awfully inconsiderate."
        "I can’t be out the front door sooner."
        "The front porch squeals when my foot paws land on it, but I won’t slow down."
        play background "sfx/forestbirds.ogg" fadeout 1.0 fadein 2.0
        scene cabinfront with fade
        show cli adv doubt at center,dark4
        show expression AlphaMask("foliage", At("cli adv doubt", center)) as mask2:
            alpha 0.55
        show mur eyes at right,dark4
        show expression AlphaMask("foliage", At("mur eyes", right)) as mask:
            alpha 0.55
        with dissolve
        "Cliff and Murdoch are already outside, yammering at one another, like it’s another goddamn Tuesday."
        "I gasp and pant, holding my chest."
        show mur fear d
        show expression AlphaMask("foliage", At("mur fear d", right)) as mask:
            alpha 0.55
        with dis
        mu "\"You don’t look so good.\""
        show cli adv doubt
        show expression AlphaMask("foliage", At("cli adv doubt", center)) as mask2:
            alpha 0.55
        with dis
        cl "\"Did you find something?\""
        show cli adv
        show expression AlphaMask("foliage", At("cli adv", center)) as mask2:
            alpha 0.55
        with dis
        "I don’t want to tell them that there’s a person in there."
        "Because I don’t ever want to see that person again."
        "I can’t."
        "I won’t."
        "I used to think I was always the most pathetic person within a 200 mile proximity."
        "But I didn’t like that."
        $ renpy.music.set_volume(1.0, delay=0.0, channel='background')
        "I didn’t like that at all."
        hide mask
        hide mask2
        hide cli
        hide mur
        with dissolve

    "Stay with Jeb and Avery":
        $ FollowCM = False
        m "\"They’ll be fine on their own.\""
        show jeb talking
        show expression AlphaMask("foliage", At("jeb talking", center)) as mask5:
            alpha 0.55
        with dis
        jeb "\"Whatever you say, fella.\""
        show jeb
        show expression AlphaMask("foliage", At("jeb", center)) as mask5:
            alpha 0.55
        with dis
        show ave serious
        show expression AlphaMask("foliage", At("ave serious", right)) as mask6:
            alpha 0.55
        with dis3
        m "\"Who y’all reckon this house belonged to?\""
        show jeb talking
        show expression AlphaMask("foliage", At("jeb talking", center)) as mask5:
            alpha 0.55
        with dis
        jeb "\"Can’t say, considerin’ it looks like it’s been in disrepair for decades and we ain't ever seen it.\""
        show jeb
        show expression AlphaMask("foliage", At("jeb", center)) as mask5:
            alpha 0.55
        with dis
        "The bear booms something I don’t understand and Avery starts walking to the back of the house behind some bushes."
        m "\"What’s he hollerin’ about?\""
        show jeb talking
        show expression AlphaMask("foliage", At("jeb", center)) as mask5:
            alpha 0.55
        with dis
        jeb "\"Dunno. Let’s have a look.\""
        hide mask5
        hide mask6
        hide jeb
        hide ave
        with dissolve
        scene cabinbonfire with dis
        "We see the others crouching over a clearing where there’s no plants growing anywhere."
        "It smells like ash."
        m "\"This one of those bonfires your daddy was talkin’ about?\""
        show ave thinking eyes at center,dark4
        show expression AlphaMask("foliage", At("ave thinking eyes", center)) as mask6:
            alpha 0.25
        with dis3
        av "\"That would be the case.\""
        show ave serious talking
        show expression AlphaMask("foliage", At("ave serious talking", center)) as mask6:
            alpha 0.25
        with dis3
        av "\"There’s a buildup of ash here, so it had to be used plenty.\""
        show ave doubt
        show expression AlphaMask("foliage", At("ave doubt", center)) as mask6:
            alpha 0.25
        with dis
        av "\"Strange to see this here, though.\""
        show ave thinking
        show expression AlphaMask("foliage", At("ave thinking", center)) as mask6:
            alpha 0.25
        with dis3
        av "\"That style of cabin looks more like something your people would build.\""
        hide ave
        hide mask6
        with dissolve
        "I feel the ash with my paw and sift through it."
        "It’s soft and silky to the touch."
        "Then it’s hard and cold."
        "I feel a lump."
        m "\"Hrm? What’s this?\""
        show jeb doubt at left,dark4
        show expression AlphaMask("foliage", At("jeb doubt", left)) as mask5:
            alpha 0.25
        with dissolve
        show jeb doubt talking
        show expression AlphaMask("foliage", At("jeb doubt talking", left)) as mask5:
            alpha 0.25
        with dis
        jeb "\"What’s what?\""
        show jeb doubt
        show expression AlphaMask("foliage", At("jeb doubt", left)) as mask5:
            alpha 0.25
        with dis
        "I pull out what’s in the ash carefully, tipping it over as more dirt falls out of a hollow end."
        "I brush away the caked on grime and feel the smooth sides of it."
        show jeb shocked
        show expression AlphaMask("foliage", At("jeb shocked", left)) as mask5:
            alpha 0.25
        with dis
        m "\"Looks like a pipe?\""
        "I feel it a little more until my paws rub against something course."
        m "\"Feels like there’s something engraved, too.\""
        show pipe1 at center,dark4 with dissolve
        "I hold the pipe away from my face and look at it."
        m "\"Huh.\""
        m "\"There’s an engraving on it.\""
        m "\"Either of you know somebody who goes by these initials?\""
        show ave serious talking behind pipe1 at right,dark4
        show expression AlphaMask("foliage", At("ave serious talking", right)) behind pipe1 as mask6:
            alpha 0.25
        with dis3
        av "\"No.\""
        show ave serious
        show expression AlphaMask("foliage", At("ave serious", right)) as mask6:
            alpha 0.25
        with dis3
        show jeb talking
        show expression AlphaMask("foliage", At("jeb talking", left)) as mask5:
            alpha 0.25
        with dis3
        jeb "\"Not a soul.\""
        show jeb
        show expression AlphaMask("foliage", At("jeb", left)) as mask5:
            alpha 0.25
        with dis
        hide pipe1 with dissolve
        m "\"Must have abandoned it.\""
        hide mask5
        hide mask6
        hide jeb
        hide ave
        with dissolve
        "Or died."
        "Maybe in that house."
        "But I don’t want to say that out loud."
        "We hear crunchy footsteps behind us."
        show cli adv doubt at center,dark4
        show expression AlphaMask("foliage", At("cli adv doubt", center)) as mask2:
            alpha 0.25
        show mur eyes at right,dark4
        show expression AlphaMask("foliage", At("mur eyes", right)) as mask:
            alpha 0.25
        with dissolve
        "Murdoch’s wearing the same quiet smile he went into that house with, but his clothes are a little more dirty."
        "Cliff looks even dirtier, and unamused."
        m "\"So the two of you lived after all.\""
        show cli adv sad
        show expression AlphaMask("foliage", At("cli adv sad", center)) as mask2:
            alpha 0.25
        with dis3
        cl "\"Well, no thanks to you, Samuel.\""
        show mur talking
        show expression AlphaMask("foliage", At("mur talking", right)) as mask:
            alpha 0.25
        with dis
        mu "\"He’s mad at you.\""
        show mur
        show expression AlphaMask("foliage", At("mur", right)) as mask:
            alpha 0.25
        with dis
        m "\"Wait, what did I do?\""
        show cli adv doubt
        show expression AlphaMask("foliage", At("cli adv doubt", center)) as mask2:
            alpha 0.25
        with dis3
        cl "\"There are beams and undergrowth every which way.\""
        show mur talking
        show expression AlphaMask("foliage", At("mur talking", right)) as mask:
            alpha 0.25
        with dis
        mu "\"The place is trashed.\""
        show mur
        show expression AlphaMask("foliage", At("mur", right)) as mask:
            alpha 0.25
        with dis
        cl "\"I could have gone further into the kitchen had you been there.\""
        m "\"...You mean the support beams?\""
        show cli adv eyes talking
        show expression AlphaMask("foliage", At("cli adv eyes talking", center)) as mask2:
            alpha 0.25
        with dis
        cl "\"They were in the doorway! I can assure that they held no purpose for their intended structural integrity any longer.\""
        show cli adv
        show expression AlphaMask("foliage", At("cli adv", center)) as mask2:
            alpha 0.25
        with dis
        show mur eyes talking
        show expression AlphaMask("foliage", At("mur eyes talking", right)) as mask:
            alpha 0.25
        with dis
        mu "\"I told him you wouldn’t have moved them anyway.\""
        show mur sideeye
        show expression AlphaMask("foliage", At("mur sideeye", right)) as mask:
            alpha 0.25
        with dis
        show cli adv doubt
        show expression AlphaMask("foliage", At("cli adv doubt", center)) as mask2:
            alpha 0.25
        with dis
        cl "\"Well at least he would have been capable of moving them!\""
        cl "\"Beneath the fluff you’re just fat and leg muscles.\""
        show mur concerned d
        show expression AlphaMask("foliage", At("mur concerned d", right)) as mask:
            alpha 0.25
        with dis
        mu "\"Since when did that bother you?\""
        show cli adv angry
        show expression AlphaMask("foliage", At("cli adv angry", center)) as mask2:
            alpha 0.25
        with dis3
        show mur sideeye
        show expression AlphaMask("foliage", At("mur sideeye", right)) as mask:
            alpha 0.25
        with dis3
        cl "\"Since I needed to move a beam!\""
        hide mask
        hide mask2
        hide cli
        hide mur
        with dissolve
show jeb talking at center,dark4 with dis3
if FollowCM == False:
    show expression AlphaMask("foliage", At("jeb talking", center)) as mask5:
        alpha 0.25
else:
    show expression AlphaMask("foliage", At("jeb talking", center)) as mask5:
        alpha 0.55
jeb "\"Alright, let's get a move on before the sun starts cooking us alive. We've wasted enough time here as is.\""
hide jeb
hide mask5
with dissolve
stop background fadeout 8.0
play music "music/forestambience.ogg" fadein 8.0
scene black with slow_dissolve
scene forestmorning with slow_dissolve
"It's around noon when we slow down to take a break."
"Gad and Manaba packed us some bread, but it's hardly enough to share among the seven of us."
"So we eat most of it on foot."
"Stomach's growling pretty bad. Those supplies can't come fast enough."
m "\"How are we holding up?\""
show ave thinking at center,forest
show expression AlphaMask("foliage", At("ave thinking", center)) as mask6:
    alpha 0.35
show jeb at right,forest
show expression AlphaMask("foliage", At("jeb", right)) as mask5:
    alpha 0.35
with dissolve
av "\"Not too bad, if I do say so myself!\""
"Avery taps a thin pair of lines on the map."
"I guess they're the path we're on now."
"What I guess are the supplies are marked by a large circle."
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", right)) as mask5:
    alpha 0.35
with dis
jeb "\"Paths seem to be lining up again.\""
show jeb
show expression AlphaMask("foliage", At("jeb", right)) as mask5:
    alpha 0.35
with dis1
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", right)) as mask5:
    alpha 0.35
with dis
jeb "\"Should reach the supplies any moment now.\""
show jeb
show expression AlphaMask("foliage", At("jeb", right)) as mask5:
    alpha 0.35
with dis1
show ave eyes talking
show expression AlphaMask("foliage", At("ave eyes talking", center)) as mask6:
    alpha 0.35
with dis3
av "\"See? I know how to read a map just fine.\""
show ave eyes
show expression AlphaMask("foliage", At("ave eyes", center)) as mask6:
    alpha 0.35
with dis
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", right)) as mask5:
    alpha 0.35
with dis
jeb "\"I never said you couldn't.\""
show jeb
show expression AlphaMask("foliage", At("jeb", right)) as mask5:
    alpha 0.35
with dis
show ave thinking sad
show expression AlphaMask("foliage", At("ave eyes talking", center)) as mask6:
    alpha 0.35
with dis3
av "\"You did. Multiple times.\""
hide jeb
hide ave
hide mask5
hide mask6
with dissolve
show mur concerned d at center,forest
show expression AlphaMask("foliage", At("mur concerned d", center)) as mask:
    alpha 0.35
show cli adv at right,forest
show expression AlphaMask("foliage", At("cli adv", right)) as mask2:
    alpha 0.35
with dissolve
mu "\"But if we ended up going the right way...\""
show mur fear d
show expression AlphaMask("foliage", At("mur fear d", center)) as mask:
    alpha 0.35
with dis
mu "\"Then what was with that house?\""
"Cliff shrugs."
show cli adv eyes talking
show expression AlphaMask("foliage", At("cli adv eyes talking", right)) as mask2:
    alpha 0.35
with dis
cl "\"Most likely just abandoned by the previous owner. You saw what a terrible state it was in.\""
show cli adv eyes
show expression AlphaMask("foliage", At("cli adv eyes", right)) as mask2:
    alpha 0.35
with dis
mu "\"But Avery said it wasn't supposed to be there.\""
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", right)) as mask2:
    alpha 0.35
with dis
cl "\"He may have just missed it before.\""
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", right)) as mask2:
    alpha 0.35
with dis
cl "\"It was quite well-hidden among the trees and bushes.\""
hide cli
hide mur
hide mask
hide mask2
with dissolve
"I'm not entirely sure what it was."
"All I know is that it gives me a bad feeling."
"Much like the smell that's been hanging in the air these past few minutes."
"It's getting to the point where I have to pinch my nose."
$ renpy.music.set_volume(0.0, delay=0.0, channel='background')
m "\"What the hell is that?\""
$ renpy.music.set_volume(0.2, delay=5.0, channel='background')
play background "sfx/flies.ogg" fadein 4.0
mu "\"It smells like a sewer.\""
"That's putting it mildly. Makes shit smell like Cliff's perfume."
show jeb at center,forest
show expression AlphaMask("foliage", At("jeb", center)) as mask5:
    alpha 0.35
with dissolve
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"It's a carcass.\""
show jeb
show expression AlphaMask("foliage", At("jeb", center)) as mask5:
    alpha 0.35
with dis
$ renpy.music.set_volume(0.4, delay=5.0, channel='background')
"As we round the corner, I hear flies buzz louder and louder."
show jeb shocked talking
show expression AlphaMask("foliage", At("jeb shocked talking", center)) as mask5:
    alpha 0.35
with dis3
jeb "\"...Wait, a carcass must mean—\""
show jeb shocked
show expression AlphaMask("foliage", At("jeb shocked", center)) as mask5:
    alpha 0.35
with dis3
m "\"We're close.\""
hide jeb
hide mask5
with dissolve
"Jeb's eyes go wide, and his breathing speeds up. He runs ahead of us to look into the clearing, then stops."
stop music fadeout 5.0
$ renpy.music.set_volume(0.7, delay=5.0, channel='background')
"His chest rises and falls rapidly."
jeb "\"N-no...\""
"He steps back, and his legs give way."
"He falls."
av  "\"Jebediah!\""
"The elk rushes over to the collapsed horse, putting his large hand under his head."
"He, too, looks into the clearing."
show ave thinking shocked at center,forest
show expression AlphaMask("foliage", At("ave thinking shocked", center)) as mask6:
    alpha 0.35
with dissolve
av "\"Shit.\""
$ renpy.music.set_volume(1.0, delay=5.0, channel='background')
play music "music/contemplation.ogg" fadein 3.0
show cli adv shocked at right,forest
show expression AlphaMask("foliage", At("cli adv shocked", right)) as mask2:
    alpha 0.35
with dis3
cl "\"What's wrong?\""
"He tips his muzzle to the clearing, and we all gather around him to look at..."
"...our old campsite."
hide mask2
hide mask6
hide cli
hide ave
with dissolve
"Or what's left of it."
ys "\"Fuuuck. This is...\""
ts "\"It's unnatural.\""
if FollowCM == True:
    "I thought what happened in that house would be the most offputting thing we'd experience today."
else:
    "I thought that strange house would be the most unnatural thing I'd see today, but this has it beat."
"The tents have collapsed, the wagon is busted beyond repair, or hell, recognition."
"Papers are strewn all over the forest floor."
"I think I can see what remains of Cliff's satchel. It's been torn to ribbons, just like the rest."
"At the center of it all sits the donkey's corpse, twisted and mangled to the point it doesn't even resemble one anymore."
"Its head is missing, and what's left of the rest is being feasted upon by bugs."
"Next to me, Murdoch's usual smug grin completely disappears from his face."
"He holds a paw to his muzzle."
$ renpy.music.set_volume(1.0, delay=0.0, channel='background')
"I can hear him retch."
"I'm getting close to it, myself."
show ave thinking sad at center,forest
show expression AlphaMask("foliage", At("ave thinking sad", center)) as mask6:
    alpha 0.35
with dis3
av "\"I don't think this was done by some creature hunting to survive.\""
av "\"It left most of the body.\""
mu "\"That's what Jeb said before.\""
show cli adv sad at right,forest
show expression AlphaMask("foliage", At("cli adv sad", right)) as mask2:
    alpha 0.35
with dissolve
cl "\"...And took the head as a trophy.\""
"The weasel's expression is grim, unfocused."
m "\"Is Jebediah going to be okay?\""
show ave serious talking
show expression AlphaMask("foliage", At("ave serious talking", center)) as mask6:
    alpha 0.35
with dis3
av "\"Out cold. Shock, most likely. He'll come around in a few.\""
show ave thinking eyes
show expression AlphaMask("foliage", At("ave thinking eyes", center)) as mask6:
    alpha 0.35
with dis3
av "\"Don't blame him. Seeing something like this... it can do things to the body just as well as the mind.\""
show ave thinking sad
show expression AlphaMask("foliage", At("ave thinking sad", center)) as mask6:
    alpha 0.35
with dis
av "\"Terrible things.\""
"Tell me about it."
"I pinch my nose shut."
"Doesn't help."
"The only thing I can do is try not to look."
m "\"You seem to be doin' okay.\""
"He shakes his head."
show ave serious talking
show expression AlphaMask("foliage", At("ave serious talking", center)) as mask6:
    alpha 0.35
with dis3
av "\"This is unlike anything I've seen in person before.\""
show ave thinking sad
show expression AlphaMask("foliage", At("ave thinking sad", center)) as mask6:
    alpha 0.35
with dis3
av "\"Like ritualistic slaughter.\""
"Murdoch wipes his muzzle with the back of his paw."
"I haven't seen him this rattled before."
show mur fear d at left,forest
show expression AlphaMask("foliage", At("mur fear d", left)) as mask:
    alpha 0.35
with dis3
mu "\"Let's be quick about this.\""
mu "\"I'd rather not be here any longer than I have to.\""
show ave serious talking
show expression AlphaMask("foliage", At("ave serious talking", center)) as mask6:
    alpha 0.35
with dis3
av "\"I think that goes for all of us.\""
show ave serious
show expression AlphaMask("foliage", At("ave serious", center)) as mask6:
    alpha 0.35
with dis1
hide mask
hide mask6
hide mur
hide ave
with dis3
"I glance at Cliff."
"The weasel's still staring straight ahead. His eyes are empty."
"I put a paw on his back."
m "\"Cliff?\""
show cli adv shocked
show expression AlphaMask("foliage", At("cli adv shocked", right)) as mask2:
    alpha 0.35
with dis3
"He jumps."
cl "\"Y-y-y-yes!\""
hide cli
hide mask2
with dissolve
show ave serious talking at center,forest
show expression AlphaMask("foliage", At("ave serious talking", center)) as mask6:
    alpha 0.35
show mur fear d at right,forest
show expression AlphaMask("foliage", At("mur fear d", right)) as mask:
    alpha 0.35
with dissolve
av "\"Yiska, Murdoch, Sam, and I are going to see what supplies we can carry.\""
m "\"Right.\""
show mur concerned d
show expression AlphaMask("foliage", At("mur concerned d", right)) as mask:
    alpha 0.35
with dis
mu "\"What do we do about...\""
"His eyes shift to the donkey."
show ave thinking sad
show expression AlphaMask("foliage", At("ave thinking sad", center)) as mask6:
    alpha 0.35
with dis3
av "\"We leave it be.\""
hide mask
hide mask6
hide mur
hide ave
with dissolve
jeb "\"No...\""
"Jebediah jolts awake, wheezing, coughing."
"Avery rolls him onto his side."
show jeb sad at center,forest
show expression AlphaMask("foliage", At("jeb sad", center)) as mask5:
    alpha 0.35
with dissolve
show jeb sad talking
show expression AlphaMask("foliage", At("jeb sad talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"I want to bury her, Ave.\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", center)) as mask5:
    alpha 0.35
with dis
"His voice is weak."
show ave serious at right,forest
show expression AlphaMask("foliage", At("ave serious", right)) as mask6:
    alpha 0.35
with dis3
"Avery frowns."
show ave serious talking
show expression AlphaMask("foliage", At("ave serious talking", right)) as mask6:
    alpha 0.35
with dis
av "\"Jeb, I don't think that it's safe to—\""
show ave serious
show expression AlphaMask("foliage", At("ave serious", right)) as mask6:
    alpha 0.35
with dis
show jeb angry
show expression AlphaMask("foliage", At("jeb angry", center)) as mask5:
    alpha 0.35
with dis
jeb "\"You don't get it at all, do you?\""
"He forces himself into a sitting position."
show jeb sad talking
show expression AlphaMask("foliage", At("jeb sad talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"I have to do good by her.\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", center)) as mask5:
    alpha 0.35
with dis1
show jeb sad talking
show expression AlphaMask("foliage", At("jeb sad talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"I promised him I'd take care of her, so I will.\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", center)) as mask5:
    alpha 0.35
with dis
m "\"Promised who?\""
"He mentioned this person before."
"I can tell now that this was more about whoever he was than the donkeys."
"Jebediah ignores me, and looks out into the clearing once more."
"He fixes his hat."
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"There's shovels in the wagon.\""
show jeb
show expression AlphaMask("foliage", At("jeb", center)) as mask5:
    alpha 0.35
with dis
m "\"I'll help.\""
show jeb shocked
show expression AlphaMask("foliage", At("jeb shocked", center)) as mask5:
    alpha 0.35
with dis
"He gives me the same look he gave me when we were fixing the wagon just the other day."
"Genuine surprise."
show jeb shocked talking
show expression AlphaMask("foliage", At("jeb shocked talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"Thank you, Sam.\""
show jeb shocked
show expression AlphaMask("foliage", At("jeb shocked", center)) as mask5:
    alpha 0.35
with dis
"It might be the first time he's called me by name."
m "\"Can you stand?\""
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"Yeah...  I'll be right as rain in a little while.\""
show jeb
show expression AlphaMask("foliage", At("jeb", center)) as mask5:
    alpha 0.35
with dis
"He grabs Avery's hand and rises to his feet with a grunt."
show ave serious talking
show expression AlphaMask("foliage", At("ave serious talking", right)) as mask6:
    alpha 0.35
with dis
av "\"Be careful, you hear?\""
show ave serious
show expression AlphaMask("foliage", At("ave serious", right)) as mask6:
    alpha 0.35
with dis
m "\"I'll keep an eye on him.\""
show mur concerned d at left,forest
show expression AlphaMask("foliage", At("mur concerned d", left)) as mask:
    alpha 0.35
with dissolve
mu "\"I'll check the food.\""
hide mur
hide mask
with dissolve
"Jebediah gives me an expecting look as he passes."
m "\"I'll be with ya in a second.\""
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"Right.\""
show jeb
show expression AlphaMask("foliage", At("jeb", center)) as mask5:
    alpha 0.35
with dis1
hide jeb
hide ave
hide mask5
hide mask6
with dissolve
"He heads out into the clearing, too."
m "\"What are you going to do, Cliff?\""
show cli adv sad at center,forest
show expression AlphaMask("foliage", At("cli adv sad", center)) as mask2:
    alpha 0.35
with dis3
cl "\"I don't know. I shall gather what I can of my research, probably.\""
cl "\"What's left of it.\""
"Even that's going to be hard. Half of the pages I see on the ground are either completely torn or smudged beyond recognition with mud or sand."
play music "music/forestambience.ogg" fadeout 7.0 fadein 4.0
m "\"I can help you after we dig.\""
show cli adv happy
show expression AlphaMask("foliage", At("cli adv happy", center)) as mask2:
    alpha 0.35
with dis3
"The weasel lights up."
cl "\"You will?\""
m "\"'Course.\""
cl "\"Splendid!\""
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", center)) as mask2:
    alpha 0.35
with dis3
cl "\"If you're helping me, I'm sure we'll finish in no time at all.\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", center)) as mask2:
    alpha 0.35
with dis1
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", center)) as mask2:
    alpha 0.35
with dis
cl "\"But first...\""
show cli adv sad
show expression AlphaMask("foliage", At("cli adv sad", center)) as mask2:
    alpha 0.35
with dis3
"He looks at Jebediah, who's clearing the bugs off the carcass."
cl "\"...I'd like to pay my respects...\""
cl "\"...not for the farm animal, but for Jebediah.\""
stop background fadeout 15.0
hide cli
hide mask2
with dissolve
"I wipe the sweat from my brow."
"I've done some digging during my time in the mines, but that experience isn't making this any easier."
"We found some more shovels among the remains of the wagon, and we're up to our necks in dirt about now."
"Even Cliff is helping us dig."
"Haven't heard him complain yet, surprisingly."
"Maybe all that work with Manaba did him some good."
m "\"Reckon this is deep enough?\""
show jeb at center,forest
show expression AlphaMask("foliage", At("jeb", center)) as mask5:
    alpha 0.35
with dissolve
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"We're getting there. How are you holding up?\""
show jeb
show expression AlphaMask("foliage", At("jeb", center)) as mask5:
    alpha 0.35
with dis
m "\"I'm fine.\""
m "\"More worried about you at this point.\""
show cli adv at right,forest
show expression AlphaMask("foliage", At("cli adv", right)) as mask2:
    alpha 0.35
with dissolve
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", right)) as mask2:
    alpha 0.35
with dissolve
cl "\"I've been wondering something.\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", right)) as mask2:
    alpha 0.35
with dis
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"Yeah?\""
show jeb
show expression AlphaMask("foliage", At("jeb", center)) as mask5:
    alpha 0.35
with dis
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", right)) as mask2:
    alpha 0.35
with dis
cl "\"You told Avery you promised 'him' you'd take care of the do—\""
show cli adv eyes
show expression AlphaMask("foliage", At("cli adv eyes", right)) as mask2:
    alpha 0.35
with dis
"He clears his throat."
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", right)) as mask2:
    alpha 0.35
with dis
cl "\"That you'd take care of Doris.\""
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", right)) as mask2:
    alpha 0.35
with dis
cl "\"Who is the man you're referring to?\""
m "\"That's what I've been asking for days.\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", center)) as mask5:
    alpha 0.35
with dis
"Jebediah leans on his shovel."
show jeb sad talking
show expression AlphaMask("foliage", At("jeb sad talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"It's a long story.\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", center)) as mask5:
    alpha 0.35
with dis1
show cli adv happy
show expression AlphaMask("foliage", At("cli adv happy", right)) as mask2:
    alpha 0.35
with dis3
cl "\"We'll be digging for some time yet.\""
show jeb shocked talking
show expression AlphaMask("foliage", At("jeb shocked talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"I... uh, hell.\""
show jeb shocked
show expression AlphaMask("foliage", At("jeb shocked", center)) as mask5:
    alpha 0.35
with dis1
show cli adv
show expression AlphaMask("foliage", At("cli adv", right)) as mask2:
    alpha 0.35
with dis3
"He scratches the back of his head."
show jeb talking
show expression AlphaMask("foliage", At("jeb shocked", center)) as mask5:
    alpha 0.35
with dis
jeb "\"I can tell you, I suppose.\""
$ renpy.music.set_volume(0.4, delay=6.0, channel='music')
play background "music/jebtheme.ogg" fadein 6.0
show jeb
show expression AlphaMask("foliage", At("jeb", center)) as mask5:
    alpha 0.35
with dis1
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"Doris wasn't mine to begin with.\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", center)) as mask5:
    alpha 0.35
with dis1
show jeb sad talking
show expression AlphaMask("foliage", At("jeb sad talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"She belonged to my... she was my partner's.\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", center)) as mask5:
    alpha 0.35
with dis1
show cli adv doubt
show expression AlphaMask("foliage", At("cli adv doubt", right)) as mask2:
    alpha 0.35
with dis
cl "\"I didn't know you were married.\"" #Is same sex marriage a thing in this version of the 20s? Why would Cliff say this, knowing it's a *he*?
show jeb shocked talking
show expression AlphaMask("foliage", At("jeb shocked talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"I was never... uh, I was never—\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", center)) as mask5:
    alpha 0.35
with dis1
show jeb sad talking
show expression AlphaMask("foliage", At("jeb sad talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"I was sixteen. After Avery left for Echo, there was no one on the ranch who really got me.\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", center)) as mask5:
    alpha 0.35
with dis1
show jeb sad talking
show expression AlphaMask("foliage", At("jeb sad talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"He was the only friend I had.\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", center)) as mask5:
    alpha 0.35
with dis1
show jeb sad talking
show expression AlphaMask("foliage", At("jeb sad talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"Then my parents hired a new farmhand, just a little older than I was at the time. He was Meseta.\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", center)) as mask5:
    alpha 0.35
with dis
"He stops digging to wipe at his eyes."
show jeb happy
show expression AlphaMask("foliage", At("jeb happy", center)) as mask5:
    alpha 0.35
with dis
jeb "\"We got on like a house on fire. I... I wrote these stories, see, and he would always read them. Tell me what he thought of them.\""
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"One of those stories... it was about him. Didn't mean for him to find it, but he did.\""
show jeb happy
show expression AlphaMask("foliage", At("jeb happy", center)) as mask5:
    alpha 0.35
with dis
jeb "\"Told me he'd been feeling the same way. That's how we started.\""
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", right)) as mask2:
    alpha 0.35
with dis
cl "\"That's sweet.\""
show cli adv
show expression AlphaMask("foliage", At("cli adv", right)) as mask2:
    alpha 0.35
with dis
"Jebediah smiles."
show jeb talking with dis
jeb "\"I couldn't let my parents find out, so we made a plan to run for it and make a living someplace else.\""
show jeb
show expression AlphaMask("foliage", At("jeb", center)) as mask5:
    alpha 0.35
with dis1
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"Maybe get a book published.\""
show jeb happy
show expression AlphaMask("foliage", At("jeb happy", center)) as mask5:
    alpha 0.35
with dis
jeb "\"So one night, we went for it. Got all the way to Echo and bought ourselves two donkeys and an old wagon with the money he'd made working at the ranch.\""
jeb "\"I couldn't find anyone to publish my books, so until I could we'd make money as guides to and from the settlement.\""
jeb "\"Things were good for a while.\""
show jeb sad talking
show expression AlphaMask("foliage", At("jeb sad talking", center)) as mask5:
    alpha 0.35
with dis3
jeb "\"Then he got sick. Real sick.\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", center)) as mask5:
    alpha 0.35
with dis1
show jeb sad talking
show expression AlphaMask("foliage", At("jeb sad talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"He was... he was losing weight fast, coughing, running high fevers.\""
show jeb angry
show expression AlphaMask("foliage", At("jeb angry", center)) as mask5:
    alpha 0.35
with dis3
show cli adv shocked
show expression AlphaMask("foliage", At("cli adv shocked", right)) as mask2:
    alpha 0.35
with dis3
jeb "\"Eventually he'd lost so much there wasn't any of him left.\""
show cli adv sad
show expression AlphaMask("foliage", At("cli adv sad", right)) as mask2:
    alpha 0.35
with dis3
m "\"What was it?\""
show jeb sad talking
show expression AlphaMask("foliage", At("jeb sad talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"Avery said it was consumption. We couldn't treat it in time.\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", center)) as mask5:
    alpha 0.35
with dis
"He sighs."
cl "\"Terrible disease. I'm so sorry.\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", center)) as mask5:
    alpha 0.35
with dis1
show jeb sad talking
show expression AlphaMask("foliage", At("jeb sad talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"I could only promise him I'd take care of 'em as best I could.\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", center)) as mask5:
    alpha 0.35
with dis1
show jeb sad talking
show expression AlphaMask("foliage", At("jeb sad talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"They were the only things we had. The only things that were really ours.\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", center)) as mask5:
    alpha 0.35
with dis1
show jeb sad talking
show expression AlphaMask("foliage", At("jeb sad talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"But I was just a scared kid. I could barely take care of myself.\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", center)) as mask5:
    alpha 0.35
with dis1
show jeb sad talking
show expression AlphaMask("foliage", At("jeb sad talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"So I drank instead.\""
show jeb angry
show expression AlphaMask("foliage", At("jeb angry", center)) as mask5:
    alpha 0.35
with dis
jeb "\"I couldn't sell any books and I couldn't protect our investment.\""
jeb "\"That was that last thing we did together before he left me forever.\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", center)) as mask5:
    alpha 0.35
with dis1
show jeb sad talking
show expression AlphaMask("foliage", At("jeb sad talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"And now Doris is dead, and who knows where Daisy could be.\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", center)) as mask5:
    alpha 0.35
with dis
cl "\"I'm sorry. I dragged you into this.\""
"You paid him for a service, Cliff."
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"Don't apologize. It's not like you brought that beast here.\""
show jeb
show expression AlphaMask("foliage", At("jeb", center)) as mask5:
    alpha 0.35
with dis
"He thrusts his shovel into the ground with a grunt."
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"I think we're done.\""
show jeb
show expression AlphaMask("foliage", At("jeb", center)) as mask5:
    alpha 0.35
with dis1
hide jeb
hide mask5
with dissolve
hide mask2
hide cli
with dissolve
"He turns, climbing out of the open grave."
"After helping Cliff out, I follow suit."
"Jebediah's already got Doris wrapped in the remains of his own tent."
"I can feel my eyes start to water when he drags her near."
"Don’t know if it’s emotional exhaustion or the smell."
"Cliff's clasped his paws together. His eyes are closed, and he's murmuring softly to himself."
"Praying."
show ave thinking eyes at right,forest
show expression AlphaMask("foliage", At("ave thinking eyes", right)) as mask6:
    alpha 0.35
with dis3
"Avery's joined us, pack in hand."
av "\"Looks like a fine resting place.\""
show jeb sad at center,forest
show expression AlphaMask("foliage", At("jeb sad", center)) as mask5:
    alpha 0.35
with dissolve
show jeb sad talking
show expression AlphaMask("foliage", At("jeb sad talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"It'll have to do.\""
show jeb sad
show expression AlphaMask("foliage", At("jeb sad", center)) as mask5:
    alpha 0.35
with dis
"He swallows."
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"How are the supplies?\""
show jeb
show expression AlphaMask("foliage", At("jeb talking", center)) as mask5:
    alpha 0.35
with dis3
show ave serious talking
show expression AlphaMask("foliage", At("ave serious talking", right)) as mask6:
    alpha 0.35
with dis3
av "\"We managed to salvage a lot of them. Should be more than enough to reach the settlement, at the very least.\""
show ave serious
show expression AlphaMask("foliage", At("ave serious", right)) as mask6:
    alpha 0.35
with dis1
hide mask5
hide mask6
hide jeb
hide ave
with dissolve
"He helps Jebediah lift Doris up. Together, they lower her into the grave as gently as possible."
"Jebediah takes off his hat. His legs buckle a little, and for a moment, I'm scared he's going to faint again."
"Avery notices, and takes Jebediah's hand in his."
"The horse inhales through his nostrils."
"He leans on Avery's shoulder."
stop background fadeout 7.0
$ renpy.music.set_volume(1.0, delay=6.0, channel='music')
"The elk wraps an arm around him, muffling the sobs that ring out through the camp."
stop music fadeout 3.0
scene black with slower_dissolve
scene forestnight with slow_dissolve
play background "sfx/crickets.ogg" fadein 3.0
$ renpy.music.set_volume(1.0, delay=5.0, channel='background')
"The trail gives us little trouble after the stop at the camp."
"Starting to think what Murdoch said might have been true."
"About the forest wanting to show us things, whether we wanted to see them or not."
"Things I'm not sure I'll ever be able to understand."
"Doesn't keep me from wondering."
"And I'm sure the rest are mulling it over too."
"By the time we've finally gotten to the outskirts of the forest, we're as tired as we were yesterday morning."
"Tired, but relieved."
"I never want to see this forest again once this is all over."
show jeb talking at center,night
show expression AlphaMask("foliage", At("jeb talking", center)) as mask5:
    alpha 0.35
with dissolve
jeb "\"Almost dark out.\""
show jeb
show expression AlphaMask("foliage", At("jeb", center)) as mask5:
    alpha 0.35
with dis
m "\"Where are we camping?\""
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"Usually stop around here, but I'm not willing to risk that right now.\""
show jeb
show expression AlphaMask("foliage", At("jeb", center)) as mask5:
    alpha 0.35
with dis
"The horse points at the map in his hand."
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"We'll have to walk past sundown for a little while, but there's a spot a ways out of the forest that should be safe.\""
show jeb
show expression AlphaMask("foliage", At("jeb", center)) as mask5:
    alpha 0.35
with dis1
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"It's a small outpost, if you can even call it that.\""
show jeb
show expression AlphaMask("foliage", At("jeb", center)) as mask5:
    alpha 0.35
with dis1
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"I don't know if we can get any supplies from other folks, but we'll have a place to sleep and bathe.\""
show jeb
show expression AlphaMask("foliage", At("jeb", center)) as mask5:
    alpha 0.35
with dis1
show cli adv shocked at right,night
show expression AlphaMask("foliage", At("cli adv shocked", right)) as mask2:
    alpha 0.35
with vpunch
cl "\"We can bathe?\""
show cli adv happy
show expression AlphaMask("foliage", At("cli adv happy", right)) as mask2:
    alpha 0.35
with dis3
"I'd almost forgotten Cliff was walking next to me."
"He's been unusually quiet since we left the camp."
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", center)) as mask5:
    alpha 0.35
with dis
jeb "\"Yep. There's a spring. Always let the jennies drink there.\""
show jeb
show expression AlphaMask("foliage", At("jeb", center)) as mask5:
    alpha 0.35
with dis3
show cli adv talking
show expression AlphaMask("foliage", At("cli adv talking", right)) as mask2:
    alpha 0.35
with dis3
cl "\"Finally! It's been so long!\""
show cli adv happy
show expression AlphaMask("foliage", At("cli adv happy", right)) as mask2:
    alpha 0.35
with dis3
"For once, I agree with him."
hide cli
hide mask2
with dissolve
hide jeb
hide mask5
with dissolve
show ave thinking eyes at center,night
show expression AlphaMask("foliage", At("ave thinking eyes", center)) as mask6:
    alpha 0.35
with dis3
av "\"Maybe we can find out more about whatever that thing was.\""
show mur sideeye at right,night
show expression AlphaMask("foliage", At("mur sideeye", right)) as mask:
    alpha 0.35
with dis3
mu "\"I'd rather forget, myself.\""
hide mur
hide mask
with dis3
m "\"There many folks at this outpost?\""
show ave serious talking
show expression AlphaMask("foliage", At("ave serious talking", center)) as mask6:
    alpha 0.35
with dis3
av "\"A fair amount. Most of them are only passing through.\""
show jeb at left,night
show expression AlphaMask("foliage", At("jeb", left)) as mask5:
    alpha 0.35
show ave serious
show expression AlphaMask("foliage", At("ave serious", center)) as mask6:
    alpha 0.35
with dissolve
show jeb talking
show expression AlphaMask("foliage", At("jeb talking", left)) as mask5:
    alpha 0.35
with dis
jeb "\"It can get pretty rowdy, depending on the crowd.\""
show jeb
show expression AlphaMask("foliage", At("jeb", left)) as mask5:
    alpha 0.35
with dis
show ave thinking flirty
show expression AlphaMask("foliage", At("ave thinking flirty", center)) as mask6:
    alpha 0.35
with dis3
av "\"It ain't all bad. Plenty of music and dance, when the mood strikes.\""
"The weasel hums, his tail bristling."
hide jeb
hide mask5
with dissolve
show cli adv happy at left,night
show expression AlphaMask("foliage", At("cli adv happy", left)) as mask2:
    alpha 0.35
with dis3
cl "\"It sounds like a wonderful place.\""
av "\"Yiska, Tsela, you boys coming too?\""
show tse at right,night
show expression AlphaMask("foliage", At("tse", right)) as mask3:
    alpha 0.35
with dis3
"Tsela scratches at one of his big ears."
show tse talking
show expression AlphaMask("foliage", At("tse talking", right)) as mask3:
    alpha 0.35
with dis
ts "\"I ain't got any better places to be. Suicide to walk all the way to the settlement right now.\""
show tse
show expression AlphaMask("foliage", At("tse", right)) as mask3:
    alpha 0.35
with dis1
show tse talking
show expression AlphaMask("foliage", At("tse talking", right)) as mask3:
    alpha 0.35
with dis
ts "\"Just don't expect me to start singing and dancing.\""
show tse
show expression AlphaMask("foliage", At("tse", right)) as mask3:
    alpha 0.35
with dis1
hide mask3
hide tse
show yis at right,night
show expression AlphaMask("foliage", At("yis", right)) as mask4:
    alpha 0.35
with dissolve
show yis talking
show expression AlphaMask("foliage", At("yis talking", right)) as mask4:
    alpha 0.35
with dis
ys "\"I will join you as well.\""
show yis with dis1
hide yis
hide mask4
show mur at right,night
show expression AlphaMask("foliage", At("mur", right)) as mask:
    alpha 0.35
with dissolve
show mur talking
show expression AlphaMask("foliage", At("mur talking", right)) as mask:
    alpha 0.35
with dis
mu "\"Now that's what I like to hear. The more, the merrier.\""
show mur
show expression AlphaMask("foliage", At("mur", right)) as mask:
    alpha 0.35
with dis1
hide mask
hide mask2
hide mask6
hide mur
hide cli
hide ave
with dis3
"I'm starting to look forward to this, too."
"Maybe I can start looking into where to head first if I do end up running."
"If there's travelers about, there's bound to be someone who knows the area."
"And if there isn't, I can at least wash up and get some rest. Maybe celebrate getting out of these fucking woods."
"I hope someone has whiskey. I could really use a drink."
stop background fadeout 4.0
scene echodesertnight with fade
play music "sfx/desertmorning.ogg" fadein 5.0
"It's strange to see the desert again after so long."
"The only way I can tell this place apart from the wasteland right outside Echo is by looking at the plants."
"There's more of them here. More colorful ones, too."
"The girls back home would have liked these."
"Can't see any sign of the settlement yet, but I do see what I suppose is the place we'll be resting for the night in the distance."
"A large camp, with lots of tents, lit by a single bonfire that must be nearly thrice the size of the one in the hogan."
"I can't make out the people sitting around it very well, but I can hear their voices, carried by the wind."
"Seems like Avery and Jebediah were right - it is pretty crowded."
"Suppose the spring Jebediah mentioned is behind all those tents."
"Out of sight, hopefully. I need some time to myself."
"Been a couple days since I worked, and so much has happened the urge's kinda snuck up on me."
"Good thing these overalls are so baggy."
"As we draw near, a coyote huddled up close to the fire is the first to notice us."
"He reminds me of William, though he's a fair bit less bulky. His brown shirt's ragged and dirty, the results of days' worth of travel clear to see."
"He shouts at us, bottle in hand."
"I can smell the beer from here."
edunk "\"Well, if it ain't ol' Jebediah!\""
play music "music/ontheroad.ogg" fadein 5.0
"I look at the horse from the corner of my eye."
show jeb shocked at center,nightgreen with dis3
m "\"This a friend of yours?\""
show jeb talking with dis
jeb "\"Wouldn't push it that far, buddy. I run into him on the trail every now and then, is all.\""
show jeb with dis1
show jeb talking with dis
jeb "\"He's good people. Don't let him scare ya, he's all bark and no bite.\""
show jeb with dis1
show jeb talking with dis
jeb "\"Hey, Ed.\""
show jeb with dis
"The others around the campfire start looking to us as well."
"By the looks of their clothes, quite a few of them are from Echo, though they look far less ragged than we do."
ed "\"Ain't like you to come all this way without the girls.\""
m "\"Girls?\""
"Oh. The donkeys."
ed "\"Motley crew you got here.\""
show cli adv happy at left,nightgreen with dissolve
cl "\"We're on our way to the settlement.\""
"The coyote whistles."
ed "\"Settlement, eh? Quite the hike from Echo.\""
show cli adv talking with dissolve
cl "\"Oh, we're...\""
show cli adv doubt with dis
"The stoat glances at the ground, then back up again."
cl "\"Very aware.\""
hide cli with dissolve
hide jeb with dissolve
ed "\"Well, it ain't so far now. Should be half a day's walk if you leave in the morning.\""
ed "\"Wouldn't recommend going that way right now. Folks say there's all sortsa monsters afoot.\""
"Silence follows."
"Ed's eyes follow Jebediah's to me."
"He nearly drops his bottle trying to pick his jaw up off the floor."
ed "\"You! Ain't I seen you at the Hip before?\""
"Fuck."
"I can hear some stammering from our group. As for me, my cheeks are on fire."
m "\"Uh, I tend bar there sometimes.\""
"The coyote nods excitedly."
ed "\"Right. That's what it was!\""
ed "\"Memory's getting a bit spotty. Coulda sworn you was one of the whores.\""
"A middle-aged bat lady with dark gray fur sitting behind him speaks up."
"Bat" "\"Then maybe you should stop drinking.\""
ed "\"Hey, the night's just getting started, and so am I.\""
"He seems to already have forgotten about the donkeys. Or me, for that matter."
ed "\"Let me introduce myself.\""
"He clambers to his feet, and already I'm not sure this fellow can stand much longer."
"Best thing I can say about this man is that he seems to have no shortage of confidence."
ed "\"Name's Edward Purcell.\""
ed "\"Know that's quite the mouthful, so most folks just call me Ed. I'm a trader from up north.\""
"Just as we're all still taking in this guy's personality, Cliff steps forward, offering him a paw."
show cli adv happy at center,nightgreen with dissolve
cl "\"My name is Clifford Tibbits, leader of this expedition— Ow!\""
show cli adv shocked with dissolve
"Ed grips Cliff's hand, damn near tearing his arm off while shaking it.\""
ed "\"Fancy title for a fancy fella. Not sure I've ever seen a weasel in the wild before.\""
show cli adv doubt with dissolve
cl "\"I beg your pardon?\""
"I'm pretty sure we just found a guy who can out-talk even Cliff."
"The weasel retracts his paw and shakes it about as if it was bitten by some sort of insect."
"The coyote appraises the rest of us."
ed "\"I can see why Yiska and Tsela would be here...\""
ed "\"...but how'd you end up with the Byrnes boy and the doctor?\""
show cli adv blush eyes right with dis
cl "\"It's quite the story.\""
"The coyote laughs."
"It's a loud, booming, gravelly laugh, and several of his companions give him agitated looks."
ed "\"One to tell over a beer, I reckon.\""
ts "\"We can't say no to a beer, can we, Yiska?\""
ys "\"I would like one very much.\""
show cli adv talking with dis
cl "\"A drink would be nice indeed. I'm rather parched.\""
show cli adv with dis
cl "\"But I think I might take a long bath in that spring first.\""
show jeb talking at right,nightgreen with dissolve
jeb "\"I think... I'll sit at the fire for a while. Got some things to think about.\""
show jeb with dis1
show ave serious talking behind cli at left,nightgreen with dis3
av "\"We can bathe later.\""
show ave serious with dis1
hide jeb
hide ave
with dissolve
m "\"I want to take a look at that spring, too.\""
ed "\"It's a short walk from behind the tents and trees. Can't miss it.\""

show mur smile at left,nightgreen with dissolve
show cli adv blush eyes left with dis
show mur talking with dis
mu "\"Mind if I join you both, then?\""
show mur smile with dis1
show mur talking with dis
mu "\"I could use a wash myself.\""
show mur smile with dis
menu smc1:
    "Do I?"

    "Three's a crowd.":
        "I need some peace."
        m "\"Sorry fox.\""
        m "\"Cliff's noisy enough and it's been too noisy.\""
        show mur talking with dis
        mu "\"Fair enough.\""
        show mur smile with dis1
        show mur talking with dis
        mu "\"I'll go with Jeb and the others when they get to it.\""
        show mur smile with dis
        "I'm grateful he doesn't seem to press me on this."
        m "\"Thanks.\""
        jump scbath

    "It's about time I saw this fox naked.":
        $ SMC_Points += 1
        m "\"Only if you wash my back.\""
        show cli adv blush eyes right with dis
        cl "\"I was going to do that!\""
        mu "\"Don't worry.\""
        show cli adv blush eyes closed with dis
        mu "\"You can get his front.\""
        show cli adv happy at center with dissolve
        cl "\"Thank you.\""
        "He lets out an excited squeak as he turns to me."
        cl "\"Shall we get going?\""
        hide cli with dissolve
        "He goes on ahead, leaving Murdoch and me to look at one another."
        "The fox smirks at me."
        "I get the feeling this is what he was hoping for."
        show mur talking at center with dissolve
        mu "\"You don't want to make him wait, do you?\""
        show mur with dis
        m "\"Can't have him running into trouble again.\""
        show mur mischief with dissolve
        mu "\"He does make it a habit.\""
        play music "music/cicadas.ogg" fadeout 5.0 fadein 3.0
        scene black with slow_dissolve
        scene springsnight with slow_dissolve
        "The spring isn't all that big, but it's quiet, which is all I can really ask for."
        "Quiet and private."
        "And I've had little privacy these past few days."
        stop music fadeout 10.0
        play background "sfx/spring.ogg" fadein 5.0
        "I kneel next to the water, getting a feel for the temperature."
        "Water's nice and warm."
        "A hot spring."
        "Cliff's already pulling his shirt over his head. His pack and hat are already on the ground."
        "Some of the scrapes from the scrap with Reed and Huxley still show on his body."
        mu "\"What a view.\""
        "I'm not complaining, either."
        "After I've lowered the straps, my overalls just fall to the ground."
        "I can feel their eyes on me now. Cliff stammers. Murdoch clears his throat."
        mu "\"Yep. Almost worth the hike over here.\""
        cl "\"I do agree!\""
        play sound "sfx/splash2.ogg"
        "With my shirt undone, too, I step into the shallow water, splashing some of it on my face."
        "Feels like a slice of heaven."
        "Murdoch follows behind me, rubbing the water into the white fur on his chest."
        "From the corner of my eye, I watch, even if just to see if the white trail from his muzzle goes all the way down."
        "I can tell he's appreciating me too. Hard scent to mistake."
        show mur nocam naked talking at center,night with dis3
        mu "\"Cliff, are you joining us?\""
        show mur nocam naked with dis
        "The weasel's still at the edge, toes barely touching the water. It looks like his mind is elsewhere, glance avoidant and ears twitching."
        "He's picked up his hat to cover himself. Doin’ a piss-poor job of it, too."
        cl "\"I’ll just be a moment.\""
        show mur nocam naked concern with dis
        mu "\"Are you serious?\""
        show mur nocam naked mischief with dis
        mu "\"Why so shy all of a sudden? This kind of thing seems right up your alley.\""
        cl "\"Oh really, now?\""
        show mur nocam naked eyes with dis
        mu "\"Well. You know.\""
        show mur nocam naked mischief with dis
        mu "\"Just a couple of active men who need a wash together.\""
        mu "\"Along with their swords.\""
        cl "\"No fencer in their right mind would dip a foil in a hot spring.\""
        show mur nocam naked sideeye with dis
        m "\"...\""
        m "\"He’s talking about cocks, Cliff.\""
        cl "\"I understood the jape!\""
        cl "\"I’m merely pointing out that the analogy was clumsy.\""
        "The weasel chuffs a bit, tail sticking up as a noisy chitter escapes between his teeth."
        cl "\"I thought this would be simple and natural, but now I'm having second thoughts.\""
        show mur nocam eyes naked with dis
        mu "\"Cliff.\""
        "The fox shakes his head and wades over to the weasel, putting a hand on his side."
        show cli blush hard eyes left behind mur at left,night with dissolve
        show mur nocam naked concern with dis
        mu "\"You always have second, third, and fourth thoughts, but I promise that nothing gets more natural than this. You’re among friends!\""
        show mur nocam naked dick mischief with dis3
        mu "\"Sam here's probably seen so many pricks nothing surprises him anymore. No offense, Sam.\""
        m "\"Full offense taken.\""
        m "\"You seem plenty familiar with handling balls too, but at least I get paid to do it.\""
        show mur nocam naked dick sideeye with dis3
        m "\"Polishin’ cock for free? Now that’s what’s incorrigible.\""
        m "\"But that just pushes a new point professor.\""
        m "\"Ain't you already been with both of us?\""
        show cli blush hard eyes closed with dis
        cl "\"M-Murdoch, you told him?\""
        show mur nocam naked eyes dick with dis
        mu "\"He mostly figured it out on his own.\""
        show cli blush hard eyes right with dis1
        show cli blush hard eyes left with dis1
        show cli blush hard eyes closed with dis
        cl "\"Well, it's true...\""
        m "\"So what's stoppin' you?\""
        show cli doubt hard with dis
        "The weasel gives me a steely look, then the fox."
        "I can see his eyelids narrow."
        show cli eyes talking hard with dis3
        cl "\"Ah... to hell with it!\""
        show cli eyes hard with dis
        "He throws the hat aside."
        hide cli with dissolve
        hide mur with dissolve
        "Neither of us are much surprised with why he was covering himself."
        "He's hard, and we can both smell it."
        "The long trail of pre he’s dripping swings and clings to his thigh when he breaks into a run and then practically splashes waist-deep into the warm water."
        "Waist-deep for me, at least. Almost reaches his chest."
        "He sighs loudly."
        cl "\"Just what my body needed.\""
        mu "\"Not all it needs, clearly.\""
        "The weasel, already washing himself, freezes for a moment. He groans."
        cl "\"Murdoch...\""
        mu "\"It's alright. Just the three of us here.\""
        mu "\"I can tell we're all a little worked up.\""
        m "\"He’s not wrong.\""
        "Cliff looks to me."
        "Down, right above the water."
        m "\"Been too fucking long since I shot into a hot mouth or a tight ass.\""
        "His eyes go wide and his face flushes."
        "I slide a hand down over my stomach, keeping my eyes trained on him, and grab myself."
        "His breath catches in his throat."
        "I'm back in my element, and it feels good."
        m "\"Nothing to be ashamed of, Professor.\""
        "I pump it slowly just to watch his face contort as he tries to contain himself."
        "The stoat's eyes linger on me."
        "Then his own hand sinks below the water as well."
        "He grits his teeth and moans."
        "I hear Murdoch chuckle beside me."
        mu "\"You folks mind if I join?\""
        "I feel a smile spread across my face."
        m "\"Depends. Can you keep up?\""
        "I don’t always feel like I know what’s going through this fox’s head..."
        "But I definitely do right now."
        mu "\"Of course. I don't make wagers I know I can't win, Sam.\""
        "The stoat looks like his mind is elsewhere, suddenly."
        "It looks like he's thinking about what he's going to say next very carefully, with considerable deliberation."
        cl "\"I wager I’d very much like having you both.\""
        "He's so quiet I have to perk up my ears to hear him."
        mu "\"Wager accepted, then.\""
        mu "\"Let's take this to the water's edge.\""
        "The fox is as hard as the both of us coming out of the water."
        "I wasn't looking before, but I definitely am now. He's pretty big too."
        "He sits down at the edge of the spring, russet pase still planted in the water."
        "I follow, Cliff trailing behind me. The stoat sits between us both."
        "He looks at me, and I don't need to hear him speak to know what he wants."
        "I put my hand on his thigh, earning a little squeak from him before Murdoch does the same to his other leg."
        "He twitches, leaking some."
        "Tells me all I need to know I'm doing well."
        cl "\"Heavens...\""
        mu "\"Just from a single touch?\""
        "The fox's lips stretch into a smirk as he takes hold of the weasel delicately, running a thumb over the bead of precum at his tip."
        "The weasel moans. Loudly."
        "Instinctively, I tilt his head towards me, shutting him up with a kiss."
        "He tastes like mint again."
        " ...Not surprising, considering he seemed to expect this."
        "He moans into my mouth as Murdoch pumps him."
        "The fox reaches over with his free hand, bringing a finger under his muzzle to tip him in his direction."
        "I watch them lock muzzles. It's strange looking from the outside in. Unlike the girls, I usually don't get more than one customer at a time."
        "When they pull away, my eyes meet Murdoch's."
        "I lean over the weasel, now resting on his back."
        "We both get to our knees."
        "The fox tilts his head one way, I tilt mine another."
        "Kissing him's very different compared to kissing Cliff."
        "He uses a lot more tongue, and his fangs are bigger."
        "I can taste a hint of the weasel on him."
        "He's good at this, but I want more."
        "The weasel's shaking beneath us. Murdoch's squeezing him tightly."
        cl "\"I’m...\""
        mu "\"Not done yet.\""
        "He lets go of Cliff, our foreheads pressing together."
        "The weasel's cock's left a trail of pre on his stomach."
        "I grab my own, pointing it at him."
        m "\"C'mon. Just like I taught you.\""
        "Cliff lets out a pitiful whine."
        "He pushes himself up a little, enough to be able to wrap a hand around me."
        "I can feel his breath on me."
        "See his nose twitch as he takes in my scent."
        "He opens his muzzle wide."
        m "\"Easy...\""
        mu "\"Let me help.\""
        "Murdoch puts a paw on the back of Cliff's head, pushing him forward."
        "The weasel squeaks, then moans as I push into him."
        "Warm. Wet. Tight."
        "I missed this."
        m "\"Cover your teeth... yeah, like that...\""
        m "\"That's it. Slowly. You're getting better.\""
        "I scratch his ears, before pushing him off."
        "He looks at me with confusion in his eyes before I push him on his back, watching his cock spring back into the air."
        m "\"We’re all the same right now.\""
        "I dip down, feeling my throat rumble, swallowing his whole cock without any trouble at all."
        "I look up, see Murdoch watching me, and he understands."
        "I push off, and he bows down to take his turn too."
        "When I watch him taste my spit and Cliff’s pre, we all know that this is more intimate than any kiss."
        "Cliff has to push him off with shaking hands."
        "I’ve already repositioned myself, spreading my legs, pulling Cliff up again and back to my lap."
        m "\"Once again...\""
        "I open my legs to him."
        "He doesn’t hesitate this time as he dips."
        mu "\"I believe we were in the middle of something as well, Sam.\""
        "Murdoch buries his face in the fur on my neck, inhaling deeply."
        "In turn, I nibble and lick at the tips of those ears of his."
        "He shudders."
        "I'm looking forward to seeing what else I can make him do."
        m "\"Right.\""
        "I take his cock in my hand right before kissing him again, letting the determined weasel do most of the work below."
        "Murdoch's drizzling my fingers with his need, even more when I rub a finger over his tip."
        "His scent hangs thick in the air."
        "All I can smell now is the three of us."
        "All I can feel right now is the three of us."
        "The fox's tongue lolls from his mouth once we break apart, a string of spit connecting us."
        "His breaths are short, shallow. So are mine."
        "I rock my hips slowly."
        "It's taking me some effort not to come right now."
        mu "\"Mmm. I want a turn.\""
        "I look down at the weasel."
        m "\"You hear that, Professor?\""
        "I thrust all the way into his muzzle, until I feel his snout and whiskers against me."
        "Murdoch holds him in place for a few moments."
        "He makes a sound."
        m "\"Think he likes the idea.\""
        mu "\"Do you now?\""
        "Murdoch takes his paw off the back of Cliff's head, and the weasel comes up for air."
        "He licks his lips, chest heaving with every heavy breath he takes."
        "I aim Murdoch's cock at his muzzle, and he seems to take the hint."
        "He turns his head and licks the fox's tip."
        "Murdoch pushes out a loud breath."
        m "\"Take it slow. Savor the taste.\""
        "Cliff shuts his eyes, tongue swirling about the head of the fox's cock."
        "Murdoch cranes his neck back, pushing out a loud breath through his nostrils."
        mu "\"He's a natural.\""
        m "\"He is.\""
        "I brush my muzzle against Murdoch's neck, dragging my tongue over the white fur that trails down to his chest, and rub myself again."
        "He moans, thrusting forward, right into Cliff's mouth."
        "The weasel struggles and gags for a moment, but doesn't pull back."
        mu "\"You take the other end, Sam.\""
        m "\"Think he can take it?\""
        mu "\"Oh, he's a lot more adventurous than you think. Aren't you?\""
        "He hilts himself all the way in Cliff's muzzle."
        "The weasel's eyes go wide, then lid."
        "He lifts his tail with a hand."
        "I lick my lips."
        "I'm getting real close just watching the two of them."
        "Not about to say no to an invitation like this."
        m "\"Hands and knees.\""
        "The fox, still buried in his muzzle, helps the weasel shift."
        "Cliff's eyes find mine as I get behind him, raking my fingers down his back."
        "I grip his tail at the base, tugging it up. He lets go, putting his hand on Murdoch's thigh instead."
        "Murdoch's got his eyes on me, but I have different plans."
        "I shuffle backwards on my knees, touching the shallow water with my legs."
        "I lean down."
        "He's clean."
        "Good."
        "I lap at his balls, lifting them with my tongue, getting a small moan from him."
        "Then, I move upwards, licking my way to the pink pucker under his tail."
        "I feel him shudder as I run my tongue over it."
        "Just like he taught me."
        "He cries out, voice muffled by Murdoch's cock."
        "His tail sways, almost swatting me. I grip it tighter."
        "I hear wet noises, and grunts coming from Murdoch."
        "The fox is thrusting, shaking the weasel's body."
        "Almost makes it hard to do my job."
        "I keep licking, pressing down with my tongue until it gives way and I'm inside him."
        "His tail thrashes."
        "The sounds he's making and the way he's dribbling precum make me wish I'd tried this before."
        "Once he's slick enough, I get back up on my knees."
        "Judging by his expression, the fox is on the brink."
        "I better keep up."
        scene clicg4a with slow_dissolve
        "I line myself up with the weasel, rubbing the head of my cock against his hole."
        "I push forward. Just a little bit."
        "He squeaks, and I put a paw on his back."
        m "\"Keep breathing. You're doin' good...\""
        "I grunt, pushing in further. Soon, his warmth is all I feel."
        "He's the tightest I've had in a long time."
        m "\"Almost all the way in. You holdin' up okay?\""
        "He grunts affirmatively."
        "Guess Murdoch was right."
        "I let myself slip the rest of the way in. My balls touch his."
        "He's squeezing me from every angle, in all the right ways."
        "Fuck, this is good."
        "I start moving my hips, thrusting into the stoat just as Murdoch's hips push him against me."
        "Our moans and heavy breathing fill the air."
        mu "\"I'm not going to last much longer here...\""
        m "\"Giving up?\""
        "He's struggling to get his tongue back in his muzzle right now."
        mu "\"...Hardly.\""
        "He grabs the back of Cliff's head again, thrusting harder, faster."
        "I see the stoat tilt his head to get better angles."
        "He really is a natural."
        "I lean over him, face nearly touching Murdoch's chest, and put as much of my weight as I can into my thrusts."
        "I grit my teeth."
        "The stoat cries out."
        "Tightens around me."
        "Ropes of seed spray the ground below."
        "I'm not far behind."
        "I can hear myself purr as I thrust into him one last time. My balls tighten. The purr grows louder, turning into a growl as I utterly empty myself inside the stoat."
        "He squeezes me tight the entire time, whining, moaning, leaking."
        "I can hear Murdoch's breathing speed up before he finally gasps above me."
        "He pulls out of Cliff's mouth, grabbing his cock again."
        "He thrusts into his hand, and I watch as the weasel opens his muzzle wide, only for his brown snout to get painted white by the fox's seed."
        "With a cackle, he aims it upward for about a second, and I catch some of it on mine, too."
        "I lick my chops, savoring the taste on my tongue."
        "On his own accord, the weasel wraps his muzzle around the head of Murdoch's cock again as soon as he lets go."
        "I hear him swallow what's left."
        "He lingers for a few long moments before finally pulling off."
        scene springsnight with slow_dissolve
        mu "\"Attaboy, Professor.\""
        cl "\"That was... lovely...\""
        "His arms and knees buckle when I'm about to pull out of him."
        "He turns his head."
        cl "\"Could you... stay... a few moments... longer?\""
        "Don't have to tell me twice. Not when he's this tight."
        "I grab him tight, slowly rolling the both of us onto our backs."
        stop background fadeout 8.0
        play music "music/morningglory.ogg" fadein 5.0
        scene clicg4b with slow_dissolve
        "Practically glowing, he sighs, arching his back against my chest."
        "Murdoch gets down next to me. I wrap an arm around the fox, and he accepts, pressing against my side."
        "He gives my neck a nuzzle before caressing Cliff's cheek."
        mu "\"Told you I could keep up.\""
        "I chuff."
        m "\"Concerned me a few times there.\""
        "A soft, one-note laugh escapes Murdoch."
        mu "\"Lies and slander.\""
        cl "\"You were both... not quite what I expected.\""
        "I wonder what he means by that, but he looks so carefree."
        "The stoat seems to have caught his breath."
        "Murdoch lays his head on my chest, snout pressed against Cliff's head."
        mu "\"We're going to need another bath.\""
        m "\"We've got time.\""
        "The three of us look up at the sky together."
        "The sun's gone down completely, and I can't even begin to count the number of stars I see."
        "It's a beautiful night out."
        "At least, it is, for a brief moment."
        stop music fadeout 2.0
        play sound "sfx/guitartune.ogg"
        play background "sfx/spring.ogg" fadein 5.0
        "Someone's plucking at a guitar off in the distance. That coyote, no doubt."
        "Has to be. It's sounding less like music and more like something being put out of its misery."
        "Just hope our companions aren't awake to hear it."
        "The fox tsks."
        mu "\"And so the moment is spoiled.\""
        cl "\"But quite the moment it was.\""
        mu "\"No second or third thoughts this time, Mr. Tibbits?\""
        mu "\"What about a fourth?\""
        cl "\"Do shut up, Mr. Byrnes, or I might just change my mind.\""
        mu "\"So cocky all of a sudden! What brought this on?\""
        cl "\"Well, I... I've not yet had my turn on top, have I? I can't let you boys have all the fun.\""
        m "\"Smells like you had fun, all the same.\""
        mu "\"Speaking of smells...\""
        "He gestures to the glistening white stain still visible on his stomach. Looks like Cliff didn't get all of it."
        mu "\"I'm not sure I can get this out of my fur with just hot water.\""
        cl "\"Oh. Right you are. I hadn't considered that.\""
        cl "\"I've some perfume left, if you'd like to use it.\""
        "Murdoch puts a hand on his side, one eyebrow cocked."
        mu "\"After all this time? How much of that stuff did you bring?\""
        cl "\"A considerable amount. Us stoats, we tend to get rather... err, what's a polite way to put it?\""
        m "\"We're a little past prim and proper after what we just did.\""
        "He laughs."
        cl "\"Alright, we tend to reek.\""
        mu "\"Harsh, but true.\""
        m "\"Foxes aren't much better.\""
        mu "\"Sam!\""
        "He shakes his head, slicking back the wet fur between his ears."
        mu "\"Still, perfume?\""
        cl "\"I'm quite aware most men prefer cologne. I just fancy floral scents, is all.\""
        cl "\"The women in my life seem to like it.\""
        "He turns his head to me as he washes himself, tail thumping against the shallow water."
        cl "\"What about you, Sam?\""
        m "\"I'm comin' around to it.\""
        m "\"Most men I'm with don't even bother with the cologne. They just smell like they crawled out of a hole.\""
        mu "\"Well, it is a mining town. By all accounts, they probably did!\""
        m "\"Yeah. So I prefer a guy who bathes.\""
        cl "\"See?\""
        mu "\"I never said I didn't like it, it's just... well, it's unique.\""
        mu "\"Speaking of, did you say women?\""
        mu "\"You don't have a missus waiting for you at home, do you?\""
        "Cliff laughs."
        cl "\"Not quite, although my father's certainly tried to pair me off.\""
        cl "\"Numerous times.\""
        mu "\"Numerous times, he says. Popular fellow, aren't you?\""
        cl "\"I suppose he just wants me to carry on the family name.\""
        cl "\"I've had my fair share of dalliances and courtships, but none of them bore fruit.\""
        "Hard to imagine him as a father."
        cl "\"Of course, I'm expected to return and marry someday.\""
        cl "\"Loathe as I am to admit it, I have certain responsibilities and duties to my family I cannot shirk so easily.\""
        "Murdoch's ears splay backwards, and for a moment, his expression cracks."
        "There's no witty retort this time."
        m "\"Is that something you want, though?\""
        cl "\"If you ask me, in my heart of hearts... no. It is not something I desire.\""
        cl "\"I desire to be free. To continue exploring. Not throw it all away to live in a dusty mansion because my father once did the same.\""
        cl "\"What I desire at this moment is for this night to last forever.\""
        cl "\"But we both know that's just a wish. Soon, the sun will come up, and we will have to keep going.\""
        cl "\"Much like I will have to return to my family someday.\""
        m "\"What happens if you don't?\""
        cl "\"I would be disowned, first and foremost. I'd lose my funds, lose my home... it's unthinkable.\""
        m "\"What you're describing don't sound much like a home to me.\""
        cl "\"True. But who am I if not a... a Tibbits?\""
        cl "\"Be honest with me. Would either of you have joined me were it not for the money involved? Or my status?\""
        "Murdoch's eyes fall on mine."
        cl "\"So it has been for most of my life.\""
        cl "\"I... quite frankly, I've never had friends. Real friends, I mean.\""
        cl "\"Father had associates from all over the world, and they had children they'd bring along to our estate, but they'd always leave sooner or later.\""
        cl "\"They weren't... really there to be my friends. They were just there out of happenstance.\""
        cl "\"Because my father was one of the richest men in the city.\""
        mu "\"I think I understand what you mean. But your assumptions aren't correct.\""
        mu "\"True, we joined the expedition because of the money involved. But that doesn't make tonight any less special.\""
        mu "\"I wouldn't have joined you here or done what we just did if I didn't care. I'm sure Sam feels the same way.\""
        m "\"He's right. Don't give just about anyone a free ride.\""
        cl "\"Thank you both so much.\""
        mu "\"And who knows, I could see this partnership lasting quite a while.\""
        mu "\"Now let's get to bathing before they send out a search party. We've been gone for a long time.\""
        scene black with slow_dissolve
        "I submerge myself in the spring until the water's at my shoulders, closing my eyes."
        "Feels a lot nicer than taking a bath at home."
        "I'm gonna miss this..."
        "By the time we're clothed and ready to head back, it's a good half hour later."
        "My fur's still a little damp, and the perfume's way too much, but the thoughts that were eating me up just hours ago seem to have quieted down."
        "I'm at ease. Relaxed."
        "More mindful of the smells and sights around me."
        "I know it's temporary."
        "The thoughts are gonna come back sooner or later."
        "They're never really gone, and at this point, I'm not sure if they ever will be, even if I leave everything behind."
        "For now, though, I don't see the harm in letting myself just enjoy tonight."
        scene springsnight
        show mur smile at center,night
        show cli adv at right,night
        with slow_dissolve
        show mur talking with dis
        mu "\"You think they're missing us?\""
        show mur with dis3
        m "\"They haven't come to look for us yet.\""
        show mur mischief with dis3
        "He smirks at me as he buttons up his vest."
        mu "\"So what's keeping us from enjoying ourselves just a little longer?\""
        show cli adv doubt with dis3
        cl "\"You know very well we can't dawdle. If we're to leave for the settlement at dawn, we'll need all the rest we can get.\""
        show mur talking with dis3
        mu "\"We've had a rough couple of days. The settlement will still be there tomorrow, you know.\""
        show mur concerned d
        show cli adv shocked
        with dissolve
        "I hear far-off rustling in the bushes, underscored by a deep, rumbling laugh."
        "My claws come out, but I see nothing come out from between the trees."
        "Another voice joins it, this one even deeper."
        "Sounds like Avery."
        "Cliff looks like he's about to pipe up again, but we gesture for him to keep quiet."
        show cli adv doubt
        show mur sideeye
        with dissolve
        av "\"Mmm, c'mon, Jeb, what if someone sees?\""
        jeb "\"Been waiting too long to see you again.\""
        av "\"It's only been a week or two...\""
        show mur mischief with dissolve
        mu "\"Seems like we're not the only ones active tonight.\""
        m "\"They're up to somethin', for sure.\""
        cl "\"You don't think they heard us, do you?\""
        m "\"They would've said something if they did.\""
        "We wait around for a bit to see if the voices get closer, but they don't."
        "I just hear more rustling."
        show mur talking with dis
        mu "\"HELLO?\""
        show mur with dis3
        av "\"Shit!\""
        hide cli
        hide mur
        with dissolve
        "Cliff shoots an annoyed glance at Murdoch. The fox seems to just shrug it off."
        "We hear more rustling as Avery comes out from behind a tree, Jebediah right behind him. That's the second time I've mistaken his antlers for branches."
        show ave shocked at center,night
        show jeb shocked at right,night
        with dissolve
        av "\"Well, heheh, fancy running into you folks here.\""
        show ave thinking
        show jeb
        with dissolve
        av "\"We were, uh, just heading out to the spring for a couple minutes. I take it you boys are all finished up?\""
        mu "\"You could say that.\""
        m "\"Water's nice and warm.\""
        cl "\"I feel better already!\""
        show ave wink talking with dis
        av "\"That so? Well, then, I suppose we'll follow your example.\""
        show ave wink with dis
        show jeb shocked with dis
        "He drags Jebediah down the path by his wrist. The horse looks a little startled."
        mu "\"We'll see you at camp!\""
        jeb "\"Don't wait up for us.\""
        m "\"You folks have fun now.\""
        hide jeb
        hide ave
        with dissolve
        stop background fadeout 1.0
        jump campsong





label scbath:
scene black with slow_dissolve
stop music fadeout 5.0
play background "sfx/spring.ogg" fadein 5.0
scene springsnight with slow_dissolve
m "\"Well, ain't this a sight for sore eyes?\""
cl "\"I can hardly believe a barren desert like this can harbor a place of such beauty.\""
m "\"And we've got it all to ourselves.\""
cl "\"Yes. No one should be bothering us for a little while.\""
show cli adv blush eyes right at center,night with dissolve
"He turns around, training those bright blue eyes on mine."
"We walked all the way to this spring, hand in hand."
"The rest of the group probably thinks we've gone to get cleaned up, but both of us know why we really came here."
"I can smell it on him."
"Smell it on me."
"Rarely gone so long without, and it's showing."
"So we stop pretending."
"Only takes a moment before his muzzle's on mine again."
"This kiss is sloppier, more hurried, as his small hands claw at the straps of his overalls."
"I toss his hat to the ground and unbutton his shirt."
show cli adv blush eyes closed with dis3
cl "\"Oh, Sam...\""
"The tent forming in his pants presses against my leg."
"His hot breath's in my ear as I bury my muzzle in the crook of his neck."
"I lick and bite at the exposed fur. He just moans louder."
"It's a cute little noise."
"I run a hand over his chest, down to his stomach, trying to see what other cute little noises I can get out of him."
cl "\"Ooh...\""
"Plenty, it turns out."
hide cli with slow_dissolve
"Once I've gotten him out of his clothes, I take his hand, leading him to the edge of the water."
"It's warm, a thick cloud of steam hovering over it."
"We wash ourselves, sticking close."
"When we're all clean, I sit myself down on the soft sand at the water's edge, all but yanking the weasel down with me."
"He doesn't protest, nor does he complain when I get on top of him to explore him further."
"He looks at me through half-lidded eyes, his breathing shallow and irregular."
"It only gets faster when I lick my way down his chest and stomach."
"He's leaking so much that his scent is all I can smell now."
"With every touch, his length twitches."
"I'm the same right now."
cl "\"Sam?\""
m "\"Yeah?\""
cl "\"There's something I'd like to try, if you'll let me.\""
m "\"Another lesson?\""
"I run a thumb over his tip as I continue my way down."
"He's so sensitive he almost starts thrashing."
cl "\"I'd-I'd like to take you.\""
"Not what I was expecting to hear."
"I was hoping to get him on all fours, myself, but I'm not going to turn down a good fuck either way."
m "\"Alright, but we're doing it my way.\""
cl "\"Are you sure you want—\""
m "\"Did I stutter?\""
"He greets my grin with one of his own."
cl "\"I'll defer to you.\""
"His voice trails off as I take his length into my mouth, tongue swirling over the sensitive head."
"He grabs a fistful of fur on the back of my head, bucking into my mouth."
"I let him set the pace. I can take it."
"I'm used to folks a lot larger than him being a lot rougher."
"Still, he's stronger than I gave him credit for."
"He's going all the way in on every stroke now, thrusting hard."
"I know how badly he needs this."
cl "\"A-aah, stop, stop.\""
"Sharply exhaling, he lets go of my head, and I pull off, dragging my tongue along his shaft as I do."
"Saliva still connects my lips to it when I sit back up."
cl "\"Could you, uh, turn around for me, please?\""
"I grin at him. His face turns red as a beet."
m "\"Getting impatient, Professor?\""
cl "\"I am not!\""
cl "\"I just... can't let you have all the fun, is all.\""
cl "\"There's something I didn't quite get to finish last time we were together, if you recall.\""
"He almost sounds a little cocky now."
"Must be from all that time he's spent with Murdoch."
m "\"Oh.\""
"I do as he asks, raising my tail for him."
"As soon as I do, I feel his hands on me, groping, squeezing."
"He lifts my balls up, fondling them in his palm until I'm biting my bottom lip."
"I push back against him, leaning my upper body forward until I have to support myself with my hands."
"I feel his breath on my fur, and then his cold snout against my balls."
"He keeps gently kneading them, breathing in my scent, and I hear him moan very softly."
"I feel him shift underneath me as he licks me."
"He's careful at first, running his small tongue over my balls and taint in circular motions. Probably not looking to get swatted by my tail again."
m "\"Feels good, Professor. Keep goin'.\""
"That seems to give him the courage he needs to lick his way up the rest of my taint, and before long, that strange sensation I felt during our first night's back again."
"Warm. Slippery. Wet."
"This time, I resist the urge to pull away, instead pushing against it."
"A moan escapes me."
cl "\"My goodness, are you... purring?\""
"Was I?"
cl "\"You were!\""
"He giggles."
cl "\"I'm not sure I've heard you make such a sound before.\""
m "\"Don't get used to it.\""
"Just for him, I play it up a little."
cl "\"We'll have to see, won't we?\""
m "\"See what?\""
cl "\"How I can make you purr louder yet.\""
"His tongue's on me again without warning, taking even me by surprise."
"I hike my tail up, and he seems to take the hint, poking, prodding, trying to push into me using nothing but his tongue."
"And I let him, not even trying to stifle the moan that passes my lips."
m "\"That'll do the trick...\""
"I ain't ever felt anything quite like this before, but I already know I want more."
"I get back on my knees again, putting more of my weight into it, forcing the back of his head down into the soft sand."
"He doesn't protest, nor does he make a sound when I lower myself onto him all the way, into a sitting position."
"His prick twitches, precum beading at its glistening tip as his breathing grows shaky and his tongue finally slips into me."
"I grab his prick and mine, pumping them in a slow rhythm."
"I can feel him trembling underneath me, moaning against me, and yet his tongue never stops moving."
"Every time I pull off to let him breathe he pulls me back down right after."
"Every sound I make, every slight movement of my hips, just gets him more excited."
"I could keep this up for hours, but I'm pretty sure he's already getting close."
"There's no trace of his perfume left on him. His scent's all natural now, and it's one I know very well."
"When I finally get off of him, he's a panting, slippery mess, tongue openly hanging from his muzzle."
"It's satisfying to see a prim and proper fellow like him as disheveled as he is now."
m "\"You ready?\""
"He says nothing. Instead, he just nods, still breathing hard."
scene clicg5 with slow_dissolve
"Still straddling him, I crawl forward until my hands touch the water. Then, looking back at him, I push myself up into a squatting position."
"He supports me with shaking hands as I grab his cock again, guiding it underneath my tail. It's only then that I feel I'm just as slick as he is, and when I lower myself, it goes in smoother than anything I've taken before."
"And even though I've had far bigger than him, that feeling of fullness is still there, enough to make my breath catch in my throat."
cl "\"Sam...\""
m "\"You just lay back and let me take care of you.\""
"I push myself up until only his tip is inside me. I feel his breath in my neck, hear him groan in my ear."
"Then I lower myself again. He thrusts up to meet me, as much as he can manage with my weight on top of him, hilting himself repeatedly."
"This angle hits all the right spots for me. I can smell myself in the air as I begin to ride him, slow and hard, taking him all the way every time."
m "\"That's it... feels real nice, right?\""
cl "\"W-wonderful...\""
m "\"Good. Now reach around and grab my cock...\""
"I feel his hand snake around my side, caressing my stomach before taking a hold of me."
"I tilt my head up, exhaling through my nostrils and shutting my eyes as he pumps me in time with the movement of my hips."
m "\"How's that feel?\""
"I hear him swallow."
cl "\"Warm... firm...\""
"He licks his lips."
cl "\"Wet.\""
m "\"Means you're doing a good job.\""
cl "\"I'm very glad to h—\""
"I slam myself down hard on him. His nails dig into my thigh, and he grabs me even tighter as his sentence trails off into a needy whine."
m "\"Couldn't hear ya.\""
cl "\"Bloody hell...\""
"I'm riding him proper now, hard, fast, not giving him any time to breathe as I bring myself down on him again and again, making him moan louder and louder."
"His hand's moving at a frenzied pace now, trying to keep up with me, but falling behind as the stoat gets close."
cl "\"Sam... I can't...\""
m "\"It's alright... let it out...\""
cl "\"A-aaaah...\""
"He grips me tight and leans back, his back arching and his body tensing up as a familiar warmth floods me for the first time in a long while."
m "\"That's it... fuck...\""
"I take him to the hilt one more time before I grunt and follow right after, ropes of thick, warm seed hitting my chest."
"I don't bother aiming or trying to avoid a mess this time. Nothing I can't wash off."
"We linger like that for a moment that seems to go on forever, panting in unison, enjoying this afterglow under a sea of stars."
"When I finally roll off and pull him close, the music at camp has stopped, and it feels like we're the only people on the planet."
scene springsnight with slow_dissolve
cl "\"Thank you, Sam. That was wonderful.\""
m "\"You're not so bad yourself, Professor.\""
cl "\"Only because I was taught by the best.\""
m "\"And don't you forget it.\""
cl "\"It'll be quite hard to after tonight.\""
m "\"Heh.\""
"I don't think I'll forget tonight anytime soon either."
cl "\"Do you think they've noticed that we're gone?\""
m "\"They can miss us for a little while.\""
"He arches his back against me, getting comfortable."
cl "\"I suppose.\""
"He opens his mouth, eyes not meeting mine."
"He looks hesitant."
cl "\"It's a lovely night out, isn't it?\""
m "\"What's on your mind?\""
cl "\"I... was just thinking, is all.\""
cl "\"Are you still considering leaving us behind?\""
m "\"You know I can't go back to Echo.\""
cl "\"I know that, Sam. I know.\""
cl "\"I was merely entertaining an idea.\""
"I chuckle."
m "\"Usually your ideas get us in trouble.\""
cl "\"Harsh, but true.\""
m "\"What's the idea?\""
cl "\"I was just picturing us walking down the Batavian countryside together, somewhere no one can see us.\""
cl "\"Sitting down in the evening, sharing a bottle of wine as we talk.\""
cl "\"And then I'd take you home, and we'd... we'd dance, and laugh, and...\""
cl "\"It's rather silly of me, I know.\""
m "\"It's a nice thought.\""
cl "\"You think so?\""
m "\"Yeah.\""
"I laugh."
"Together, we look up at a sky full of stars."
"It's a beautiful night out."
"By the time we're clothed and ready to head back, it's a good half hour later."
"My fur's still a little damp, and the perfume's way too much, but the thoughts that were eating me up just hours ago seem to have quieted down."
"I'm at ease. Relaxed."
"More mindful of the smells and sights around me."
"I know it's temporary."
"The thoughts are gonna come back sooner or later."
"They're never really gone, and at this point, I'm not sure if they ever will be, even if I leave everything behind."
"For now, though, I don't see the harm in letting myself just enjoy tonight."
jump campsong









label campsong:
scene echodesertnight with slow_dissolve
play background "sfx/bonfire.ogg"
play sound "sfx/guitartune.ogg"
"When we get to camp, it's a fair bit less crowded than it was before we left."
"Think some folks already went to bed for the night."
"Though they won't get much sleep with this coyote trying to put his guitar out of its misery."
"I don't know the first thing about musical instruments, but I know they ain't supposed to sound like that."
if  SMC_Points > 0:
    show cli adv doubt at center,nightgreen
    show mur concerned d at right,nightgreen
    with dissolve
    mu "\"It's even worse hearing it up close.\""
    mu "\"And yet I can't look away.\""
    show cli adv sad with dis3
    cl "\"Good God.\""
    m "\"It's not too late to head back to the spring.\""
    show mur eyes talking with dis3
    mu "\"Disturb Jebediah and Avery, no doubt ruining their night, or listen to this for one moment longer...\""
    show mur mischief with dis
    mu "\"Difficult choice.\""
    show mur talking with dis
    mu "\"Strenuous activity will do that to you.\""
    show mur with dis3
    m "\"Avery give you that line?\""
    show mur mischief with dis
    "Murdoch shrugs, an all-too cocky grin plastered on his face."
    "I'm surprised he still has the energy for it."
    "I'm starting to get more than a little tired, myself."
    show mur smile with dis
    show cli adv talking with dis
    cl "\"Let's just sit down and have a drink. I'm quite parched.\""
    show cli adv with dis
else:
    "Our line of thought is interrupted by Murdoch stepping into the light of the fire, looking a bit damp."
    show cli adv happy at center,nightgreen with dis3
    cl "\"Oh, Murdoch!\""
    show mur at right,nightgreen with dis3
    "He waves at us as Cliff beckons him over."
    show cli adv talking with dis3
    cl "\"Are Jeb and Avery finished up too?\""
    show cli adv with dis
    show mur talking with dis3
    mu "\"With the washing, yeah. I suspect they should be coming along back to camp soon.\""
    show mur smile with dis


ed "\"There you fellas are! Reckoned you'd drowned in the spring with how long you've been gone.\""
show cli adv doubt with dis
cl "\"That sort of thing doesn't happen often, I hope?\""
ed "\"Only once or twice.\""
"That's once or twice too many."
"The fox's eyes flash as he sees the coyote strum his guitar and one of his ears twitch."
show mur talking with dis3
mu "\"Well, hello there, Ed!\""
show mur smile with dis1
show cli adv with dis
show mur talking with dis
mu "\"What have you been up to?\""
show mur smile with dis
ed "\"Just been plucking away.\""
ed "\"I swear this ol' thing is starting to lose its sound.\""
show mur eyes with dis3
mu "\"It might be a little out of tune.\""
show mur with dis
show cli adv doubt with dis
cl "\"More than a little, I'd say.\""
show mur talking with dis
show cli adv with dis
mu "\"Could you hand it over? I'll see what I can do.\""
show mur smile with dis
ed "\"You play?\""
show mur eyes with dis3
mu "\"I sneak in some practice where I can.\""
show mur with dis
ed "\"A man after my own heart, I do say.\""
ed "\"Think you could help a fella out?\""
show mur talking with dis3
mu "\"Sure! Hand it over.\""
show mur smile with dis
"Cliff and I watch as Murdoch takes the guitar and proceeds to busy himself with it for the next half hour."
hide mur
hide cli
with dissolve
"Before long, it's starting to sound less offensive to my ears, and by the time Avery and Jebediah return, it sounds almost like a real instrument."
"Murdoch really does have a lot of talents."
mu "\"That'll do the trick.\""
ed "\"You fixed 'er up right quick!\""
mu "\"Not a problem! Hopefully she'll treat you better from now on.\""
"And our eardrums, too."
ed "\"Plenty of beer to go around for all of us and then some.\""
"Bat" "\"Not if you keep hoggin' it. When's the last time you been sober?\""
ed "\"Ah, shut yer trap.\""
"The coyote scrambles over to the campfire as though he didn't hear her, opening up a crate with bottles just like the one he was holding."
"I can smell the booze in the air."
"He thrusts one into my paw, then raises an eyebrow at Cliff."
show cli adv blush eyes right at center,nightgreen with dis3
cl "\"Oh, I don't—\""
show cli adv shocked with dis3
"He gets a bottle too."
"He stares at it for a moment, studying it, like it's some artifact he's never seen before."
show cli adv doubt with dis3
cl "\"It's... warm.\""
ed "\"Beggars can't be choosers.\""
"I uncork the bottle, sniffing the opening."
"Smells more like piss than beer."
"I take a sip."
"Tastes even worse."
"Still, a drink's a drink. Good enough for me."
play music "sfx/crickets.ogg" fadeout 8.0 fadein 4.0
play background "sfx/bonfire.ogg" fadein 8.0
scene black with slow_dissolve
scene echodesertnight with slow_dissolve
"Before long, we're all sitting around the campfire."
"Yiska and Tsela talk amongst themselves in the Meseta language. Avery interjects occasionally."
"The elk's got an arm wrapped around Jebediah, the horse leaning on his shoulder."
"He's reading a book, though his expression is distant, and he hasn't flipped a single page in about half an hour."
"Cliff's stuck to me like a bad stain all evening. The weasel seems on the verge of falling asleep."
"Every now and then, he yawns loudly, like he's letting me know he's still alive."
"He looks cute when he does it."
"Ed and Murdoch seem to have become fast friends, though it might be the booze talking."
show mur mischief at center,nightgreen with dissolve
mu "\"...and then he ran off. Never saw him again.\""
"While I wasn't paying attention to Murdoch's story, the coyote's laughter that follows is a lot harder to ignore."
"It gets more grating every time."
ed "\"You've got to be shittin' me. You sure know how to spin a tale.\""
show mur talking with dis
mu "\"Well, when you work in a general store long enough, you hear enough stories from all sorts of people. \""
show mur with dis
ed "\"Stories liken to...?\""
show mur talking with dis
mu "\"Some good ones. Mostly bad ones.\""
stop music fadeout 3.0
show mur sideeye with dis
mu "\"And many odd ones.\""
ed "\"So what’s your oddest?\""
"The fox whistles low and shakes his head."
play music "music/murdochtheme.ogg" fadein 2.0
show mur talking with dis
mu "\"Most of them are bizarre or incoherent.\""
show mur mischief with dis
mu "\"There are the usual stories about witches who climb onto your back and make you do wicked deeds well into the midnight hour.\""
show mur eyes talking with dis
mu "\"Then there are stories where every egg in a chicken coop will have bloody chicks in them despite the rooster being separated.\""
show mur with dis
show mur talking with dis
mu "\"Although...\""
show mur with dis
show mur concerned d with dis
mu "\"A few of the stories about the train tracks heading through Echo unnerve me.\""
"The fox’s paw jitters a bit, as if he wishes there was something in it to fiddle with."
"Then it goes still."
show mur talking with dis
mu "\"But as far as a where-on-earth-is-this-going kind of tale?\""
show mur mischief with dis
mu "\"Well, I don’t really get this one, but I’ll share it all the same.\""
show mur talking with dis
mu "\"The story goes: you have to be all alone in the middle of the desert when the sun is hottest and highest in the sky.\""
show mur with dis
"Cliff stirs next to me, eyes wide open."
"World of difference compared to the last campfire story Murdoch told him."
show mur talking with dis
mu "\"You have to have no map, no waterskins, no food, no nothing.\""
show mur with dis
ed "\"Nothing but the clothes on your back, yeah?\""
"Murdoch cocks an eyebrow."
show mur sideeye with dis
mu "\"That was the specific phrasing.\""
mu "\"You heard this one too, then?\""
ed "\"Keep going.\""
show mur talking with dis
mu "\"Well, what’s comes next is that if you make it until dark without having a heat stroke, you’ll get a crystal clear vision of the night sky.\""
show mur smile with dis
show mur talking with dis
mu "\"You’ll be so close to death that you can see the light of the stars that were once there, which have long been snuffed out.\""
show mur smile with dis
show mur talking with dis
mu "\"And if you say hello to each and every one...\""
show mur with dis
show mur eyes talking with dis
mu "\"...then if you did it right, you fall fast asleep.\""
show mur eyes with dis
show mur talking with dis
mu "\"When you wake up, if you did it right, you’ll see a red sky above you, and you have to search around a little more.\""
show mur smile with dis
show mur talking with dis
mu "\"And if you walk straight ahead without turning back once, you'll find a pole lodged in the sand.\""
show mur smile with dis
show mur talking with dis
mu "\"And tied to the top of the pole there’s a red sack.\""
show mur smile with dis
show mur talking with dis
mu "\"If you open it up, the thing you need most will be inside of it.\""
show mur smile with dis
show mur talking with dis
mu "\"Money. The affection of an unrequited love. Good health and a long life.\""
show mur smile with dis
show mur talking with dis
mu "\"You name it.\""
show mur smile with dis
show mur with dis
m "\"How’s a truth like long life supposed to fit in a sack?\""
show mur happy with dissolve
mu "\"I presume that it just happens and there’s nothing there.\""
show mur mischief with dissolve
mu "\"But it’s a lie, so it’s not like the original storyteller thought that through.\""
"Okay, fox."
"But finding something like that sounds pretty good right now."
"The thin coyote whistles and slaps his shins."
ed "\"Damn, you’ve got that down nearly word-for-word.\""
show mur sideeye with dissolve
mu "\"Why do you look so pleased with that?\""
mu "\"Are you the person who made it up?\""
"Bat" "\"No, but we know who did.\""
show mur with dis
show mur talking with dis
mu "\"Makes sense to me.\""
show mur smile with dis
show mur talking with dis
mu "\"Word of mouth must travel pretty quickly down these roads.\""
show mur with dis
ed "\"But usually the words get a little mixed up.\""
ed "\"Like, you hear that the sack is blue, or there’s a feather attached or something.\""
show mur mischief with dis
mu "\"True enough. Maybe I heard it from the source.\""
ed "\"If you did he musta hated you.\""
show mur sideeye with dis
mu "\"That... would surprise me.\""
show mur talking with dis
mu "\"I just presumed it was a joke told to pass the time.\""
show mur smile with dis
show mur talking with dis
mu "\"I can’t imagine anybody going off to do those things unless they’re kids.\""
show mur fear d with dis
ed "\"Nah. Larry’s used that story to try and get people killed.\""
"Bat" "\"Sure has. Can guarantee it worked a couple of times, too.\""
"Oh."
show mur concerned d with dis
mu "\"Excuse me?\""
ed "\"Fucked up, ain’t it?\""
ed "\"The gold in these hills never did tend to attract the best and brightest.\""
ed "\"Most of the people who started coming around here near fifty years ago just wanted to make some money and make it quick.\""
ed "\"Still lots of ‘em. Larry hates those types.\""
ed "\"Especially if they’re immigrants.\""
show mur sad with dis3
mu "\"I doubt he thought I was foreign, considering my accent.\""
"The coyote strokes his wiry whiskers."
ed "\"True.\""
ed "\"But you are a ginger. You’ve got that sly, emerald look about you, if catch my drift.\""
show mur sideeye with dis3
mu "\"Yes. I think I do.\""
"Murdoch’s tone becomes considerably more formal."
ed "\"My point, more or less, is that most of these fun little bedtime stories ain't just for fun.\""
ed "\"Everything comes from somewhere, don’t it?\""
"The fox just looks into the fire."
show mur mischief with dis3
mu "\"I’m not surprised, really.\""
"There’s a bit of fang to his smile as his face glows in the light of the embers."
mu "\"What other sorts of stories have you heard recently, then?\""
hide mur with dissolve
stop music fadeout 3.0
play music "music/hoganstory.ogg" fadein 2.0
"He takes a swig from his bottle."
"I'm surprised it isn't empty yet by this point."
ed "\"When you've been a-travelin' to and from Echo as long as I have, ya hear people talk about all sorts of things.\""
ed "\"'Course, most of 'em are just tall tales meant to scare folks out of causin' trouble. Doin' shit they're not supposed to.\""
ed "\"But there's usually a truth to 'em. People 'round these parts, around Echo, have seen everything.\""
cl "\"Such as?\""
ed "\"Things and people goin' missing. Doors not leading where they're supposed to. Voices whispering in the night.\""
"He wipes his muzzle with his sleeve, eyes darting around the fire as if waiting for any of us to start asking questions any moment now."
ed "\"Impossible creatures appearing out of thin air.\""
ed "\"Folks say the land itself is cursed.\""
ed "\"Abandoned by God and the Devil alike.\""
ed "\"That no man was ever supposed to be there.\""
ed "\"And when man ignores the warnings, does not listen, the land itself will drive him to the brink of sanity.\""
ed "\"Unable to trust. Unable to recognize the faces of his brothers and sisters.\""
ed "\"Death follows you there. Yours, or someone else's.\""
"I feel a shiver run down my back just like the one I felt when Gad unfurled the map in front of us."
mu "\"What was it you said about creatures?\""
m "\"We've seen a creature too.\""
ed "\"What did it look like?\""
ts "\"I saw a man with rotten, singed flesh hanging from his bones.\""
ts "\"Gasping for air.\""
ts "\"My friend here—\""
"He points to Yiska. The bear's staring into the fire, the hand holding his bottle of beer trembling a little when we turn our eyes to him."
ts "\"—says he saw a snake the size of a tree.\""
"The bear swallows."
ys"\"I was scared.\""
ys"\"And then it took Shilah.\""
"He looks at his feet, muttering something under his breath."
m "\"We all saw different things, too.\""
ts "\"Your friends mentioned.\""
cl "\"It was more like a rat than anything.\""
mu "\"For me it was a fox.\""
jeb "\"I saw him.\""
"He clears his throat."
jeb "\"I saw my...\""
"The stallion looks warily at the coyote before stopping himself."
jeb "\"My old associate.\""
jeb "\"Well, I-I saw... it was wearing his skin, his fur, and it... it talked like him, but it wasn't.\""
m "\"It talked to you?\""
"The horse casts his eyes aside."
jeb "\"I wasn't gonna mention it when we talked at Avery’s folks’. You can't talk about death... dead people in them.\""
"He shakes his head and takes a swig of water. I find my eyes drawn to Cliff as an eerie feeling takes hold."
mu "\"What did it say?\""
jeb "\"...\""
av "\"There was nothing you could have done.\""
jeb "\"I know that, Ave.\""
jeb "\"I knew it wasn't him, but...\""
av "\"I wasn't entirely truthful, either.\""
cl "\"About the mudskipper?\""
"The elk shakes his head, a somber expression appearing on his face."
av "\"My parents would not have let us stay had I spoken the truth.\""
"He inhales deeply. His glasses light up a little in the dim glow of the fire."
av "\"I saw my sister.\""
"Jebediah takes his head off Avery's shoulder, turning so fast his hat almost falls from his head."
jeb "\"You gotta be shittin' me.\""
av "\"I wish I was.\""
m "\"Your sister?\""
av "\"Her name was Enola.\""
av "\"She was ten years younger than I was. She'd have been around thirty now if she were still alive.\""
cl "\"What happened to her?\""
av "\"One day the men from the government came to our home and took her away.\""
av "\"She died there at the school, away from her mother, and father, and me.\""
av "\"Every Meseta child was to be taught at a boarding school in the settlement.\""
av "\"That is what they'd decided upon.\""
m "\"Why?\""
av "\"To eat your people's food. Learn their stories. Sing their songs. Praise their God.\""
av "\"I had moved to Jeb's family's ranch by then, but my parents told me what happened.\""
av "\"She went into that school building healthy and happy, and came back out in a shroud.\""
av "\"My father wanted her body so he could bury her properly, but he was turned away.\""
av "\"They had guns.\""
av "\"I tried to take it up with the state capital, but they probably already knew and didn't care.\""
av "\"Most of what happens in that place isn't really a secret.\""
cl "\"That's...\""
"He opens his mouth to speak, but in the end, he goes quiet."
mu "\"Awful. And not surprising.\""
av "\"Scary stories are well and good, but the real things happening in the world every day are usually worse.\""
av "\"It's... the first time I've thought about her in a long while, to be honest.\""
av "\"To think some spirit would be wearing her face...\""
mu "\"Well, something...\""
mu "\"We still have no idea what we actually saw.\""
cl "\"I have a... speculation, but it might be far-fetched.\""
m "\"Which would be?\""
cl "\"Have you ever heard of dancing mania?\""
m "\"Can't say I have.\""
"The others, save for Avery, shake their heads as well."
cl "\"It's a quite fascinating phenomenon, really.\""
cl "\"A long time ago, back in Europa, in the middle ages–\""
m "\"This isn't going to be some sort of fairy tale, is it?\""
"The weasel raises a hand."
cl "\"Let me finish!\""
cl "\"As I was saying, there were mysterious outbreaks of groups of people numbering in the thousands all breaking out in dance and song, as if possessed.\""
cl "\"It spread from person to person. Nobody knew if it was disease or something beyond our comprehension. Victims would hallucinate, convulse.\""
cl "\"They'd continue dancing until they collapsed of fatigue. Some did not survive.\""
m "\"That all actually happened?\""
cl "\"It did, yes.\""
cl "\"More modern theories suggest that victims suffered from an altered state of mind. The world's first case of mass hysteria.\""
m "\"So let me get this straight.\""
m "\"Are you saying it's some sort of... hallucination, that we're all experiencing together?\""
m "\"That we're all going insane?\""
av "\"...But nobody has convulsion symptoms.\""
cl "\"But there could be some similar disease.\""
cl "\"Like I said, it's a speculation.\""
cl "\"I'm not entirely certain. What I am certain of is that we've been experiencing things that don't seem natural in the least.\""
cl "\"The forest changed around us. We witnessed our worst fears and regrets quite literally coming to life right before our eyes.\""
cl "\"How else would you explain these things?\""
cl "\"Surely you don't believe the land is actually cursed?\""
"Something comes to mind."
"I don't know if what Cliff's saying is true, if what Ed's saying is true, but I do know there's something seriously wrong with Echo, either way."
"Curse or not."
m "\"The circle.\""
cl "\"Hm?\""
m "\"Remember what we saw at the hogan?\""
cl "\"Right, the map!\""
mu "\"It’s clear to me that Avery’s family line had some idea about it.\""
mu "\"Maybe some of the other Meseta might, as well.\""
m "\"At least enough to stay away from Echo.\""
"With an entire forest between them."
mu "\"I just hope whatever it is didn't follow us all the way here.\""
stop music fadeout 3.0
"The silence between us that follows is so stifling that the sound of the crickets becomes deafening by comparison."
"The coyote sitting on the other side of the fire clears his throat."
"At this point, it's clear he's had more than a few too many drinks, but none of us are in any mood to make a fuss about it."
ed "\"Seems like you boys been through a lot.\""
"Cliff nods somberly."
"The distant look he had in his eye when we were at our old campsite comes back for a moment."
cl "\"I've seen more strange things over the past two days than I've seen in a lifetime.\""
ed "\"Sounds like you've earned a little rest, then.\""
cl "\"I'm... inclined to agree.\""
ed "\"How's about a little song and dance to lighten the mood?\""
"The stoat lights up at the mention of song."
"Not just him."
"There's a wave of relief washing over our little circle."
"Something else to occupy our minds."
cl "\"That sounds splendid! Although I'm afraid we don't have any instruments...\""
mu "\"My guitar didn't quite make the trip.\""
ed "\"It's all good! Got a perfectly fine one right here. Some other fine musicians, too.\""
"The old coyote points behind him with a thumb."
"Then, he turns his head, spitting the tobacco he's chewing into the bowl sitting at his feet."
ed "\"You know how to play?\""
mu "\"I already told you that I did.\""
mu "\"Hand me that guitar.\""
mu "\"Got a good song in mind, too.\""
mu "\"Want me to give it a try?\""
"I think he's just hesitant to give it back to him."
ed "\"You know any songs?\""
mu "\"Only a couple raunchy ones.\""
ed "\"You really are a keeper.\""
ed "\"We got a couple of other musicians with us today who might be willing to join.\""
cl "\"Wouldn't that disturb the people currently in their tents?\""
"The coyote waves him off."
ed "\"They've heard worse.\""
cl "\"Well, if you say so!\""
cl "\"Fancy a dance, Samuel?\""
m "\"In front of these people?\""
cl "\"You'll be alright. I'll lead.\""
"That's not what I'm worried about..."
mu "\"I know just the song...\""
cl "\"Heavens! I've been looking forward to this!\""
stop background fadeout 3.0
window hide
scene black with slow_dissolve
$ renpy.movie_cutscene("movies/cliffanimatic.webm", delay=211, loops=0, stop_music=True)
window show
m "\"Can't believe you made me dance.\""
cl "\"And I can't believe what we did moments ago.\""
m "\"Got a lot left to teach you, Professor.\""
cl "\"We'll have time.\""
"He rests his head on my chest, a content sigh escaping him."

jump cliffroute3
