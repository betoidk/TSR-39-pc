label williamroute3:
scene black with slow_dissolve
play music "sfx/sportcrowd.ogg" fadein 7.0
window hide
scene wilch3a with slow_dissolve
pause
stop music fadeout 2.0
play sound "sfx/sportcrowd2.ogg"
$ renpy.pause(3.7, hard=True)
scene wilch3b with dis
pause 3.5
stop sound
scene black
play background "sfx/desertmorning.ogg" fadein 15.0
pause 4.0
window show
play music "music/quiet.ogg" fadein 5.0
"Is it getting dark already?"

scene echodesertnight with slow_dissolve
"Nine fifteen PM."

"Which means it’s really seven fifteen."

"...Seven fifteen here, anyway."

"This watch has never been wrong before."

"Maybe a bit too flashy for me..."

"But never too fast."

"Never too slow."

"It just keeps on going from one day to the next."

"It’s even water-proof!"

"That’s what my first boss said, anyway."

"WATERPROOF, BY GEORGIA!"

scene echoroadnight with slow_dissolve

"God, he was so proud of that."

"As if anybody gives a shit if a wrist watch is waterproof or not."

"I feel my muzzle split into a grin."

"But only for a bit."

"People get nervous when I smile."

"That’s not the case with Sam, though."

"People around here have come to expect a sort of coldness from him."

"So when he smiles it looks sweet enough to thaw winter."

"But he’s in a bad mood again."

"It has to be because of Nik."

"There’s still some frostiness between the two of them."

"It ain't usual to see Nik that distant from Sam."

"But then again, Sam had been treating us like strangers for the last few weeks."

"At least I know he’s not lying to me anymore, now."

"But I guess what’s good enough for me ain't always enough for Nik."

"It’s a good thing that that weasel didn’t come with us."

"The both of us don’t need to be more on edge."

"I’m glad he said no when Nik suggested he stay at the office."

"Because he really {i}should{/i} say no."

"At least, if he has any shame."

"He already put Sam in danger."

"Twice."
"If his mouth leads a goddamn lynch mob to Sam or Nik and gets them killed, I might up and join the next one."

"That bullet already broke the skin on the Byrnes boy."
"..."
"But he put himself in the way."
"That fox wants approval too much."
"Maybe..."
"Goddamn it."
"That’s not important now."
"What is important is who placed the hit and if they’ll place another."
"Huxley Greene wouldn’t leave his wife over a grudge from a stranger."
"He’s too controlling."
"So where did he go... and what did he do with the gun?"
"I just need to move faster and think about what I already know."
"...Christ."
"It’s hard to focus on anything when I’m annoyed."
wi "\"Hey, Sam?\""
"I hear him padding behind me, but his breath is louder than his footsteps."
wi "\"Can we talk about what you said at the lake a little more?\""
"I hear his footsteps stop."
m "\"Which thing?\""
wi "\"Let’s keep walking.\""
m "\"Okay.\""
m "\"But which thing, William?\""
wi "\"The thing about needing more excitement.\""
wi "\"You’ve been thinkin’ about leaving town for a long time, haven’t you?\""
wi "\"Even before the night you told me about earlier.\""
m "\"...And if I have?\""
"His tone has an edge in it again."
wi "\"I’m just curious why.\""
wi "\"Things aren’t easier just because you go someplace else.\""
m "\"It ain't about things bein’ easy.\""
m "\"It’s just somethin’ about this place.\""
"He lowers his voice."
m "\"And the brothel.\""
m "\"Most folks I talk to there feel the same way.\""
m "\"Like this is a place you move to, you stay for a while, and then you keep on moving once you scrape together enough money.\""
m "\"Everybody’s just constantly coming and going.\""
m "\"Sometimes it feels like the whole goddamn city is a glorified train station and the only people who stay behind are the ones who lose their fare.\""
wi "\"Me and Nik aren’t stuck.\""
m "\"Nik will be gone the moment he finds gold.\""
"I think he deserves a little more credit than that."
m "\"And you’re out of a job the moment the public turns against you.\""
m "\"You plannin’ on keeping that badge forever?\""
m "\"Or did I miss you building houses on a day I wasn't paying enough attention?\""

m "\"Because if you ain't, you’re on your way out too, as far as I’m concerned.\""
"What a mouth."
wi "\"There’s not a whole lot of competition for this job in this location, Sam.\""
wi "\"But you're right. If I’m out, I’m out.\""
wi "\"That being said--as far as I’m concerned, pessimism is only for losers.\""
m "\"Whatever, William.\""
play music "music/spiraling.ogg" fadeout 4.0 fadein 5.0
"So that’s it, then?"
"This is just a transitional period for you?"
"You probably planned to leave before you even arrived."
"I can’t completely blame you."
"My life has only ever been transitional too."
"Always coming."
"Always going."
scene white with slow_dissolve
scene chicagotrain with slow_dissolve
"From place to place, in one of the most transitional places in the country."
$renpy.sound.set_volume(0.2, delay=0.0, channel='sound')
play sound "sfx/l-train.ogg"
"I remember seeing hundreds of new faces I couldn’t recognize, every new day."
"Our lives shared briefly."
"Our time cut short chronically."
"Viciously."
"By the L-train."
play sound "sfx/l-train.ogg"
"By the streets."
"By the churches, the businesses, the people."
"You find yourself begging for the transitions to end."
"No matter who you are."
"Or what you do."
stop sound
"Or what you live."
"There’s always another train stop."
"Tick, tock, says the clock."
scene chicagostadium with slow_dissolve
"How much of my life have I spent, thinking it was another transition?"
play sound "sfx/baseballcrowd.ogg"
"How many baseball games did I end in my head early because I knew my team wasn’t going to win?"
"Too damn many."
hat "\"William?\""
"But it doesn’t matter if I’m here or there."
stop sound
scene black with slow_dissolve
scene chicagobar with slow_dissolve
hat "\"You have a thoughtful look on your face.\""
"Because the transitions?"
hat "\"I want to know what you’re thinking about.\""
"They never stop."
wi "\"I’m just enjoying my drink.\""
"Despite how much you want them to stop with you."
hat "\"You never enjoy your drink.\""
"Because they can’t."
wi "\"Today I am.\""
"Your life transitions still, no matter where in time your mind is stuck."
wi "\"I have something I have to tell you.\""
show sam neutral at center,dark2 with dissolve
show sam talking with dis
stop music fadeout 3.0
$renpy.sound.set_volume(1.0, delay=0.0, channel='sound')
m "\"Then what is it?\""
show sam neutral -talking with dis
"Sam?"
"What is he..."
show sam surprised -talking with dis
m "\"Hello?\""
window hide
show sam surprised -talking at center,nightbrown
show bg echoroadnight behind sam
with medium_dissolve
play music "music/long-nights.ogg" fadeout 4.0 fadein 5.0
window show
"We’re staring at the front door of the department."
"I could have sworn that we still had half a mile to walk before we got here."
wi "\"I think you should stay here for the night again.\""
show sam eyes talking with dis3
m "\"That’s kind, but I have my own bed.\""
show sam eyes -talking with dis
wi "\"I meant that I’d pay.\""
show sam surprised -talking with dis
m "\"Oh.\""
show sam neutral talking with dis
m "\"I’ll have to increase the rate to justify spending the night.\""
show sam neutral -talking with dis
wi "\"Done.\""
show sam surprised talking with dis
m "\"...I didn’t say how much yet.\""
show sam surprised -talking with dis
wi "\"Better described indoors then, yeah?\""
show sam eyes talking with dis
m "\"...yeah...\""
show sam eyes -talking with dis
"I finally manage to fish the goddamn keys out of my pocket and fit them in the lock."
show sam neutral -talking with dis
"I, ah, would feel more graceful if I weren’t bumping into the lock."
"Won’t be damned by how stiff my gait is when I’m inside."
scene black with fade
scene jailnight with dissolve
show sam surprised -talking at center,prisonnight with dissolve
show sam talking with dis
m "\"We sleeping near the jail again?\""
show sam -talking with dis
wi "\"No.\""
wi "\"My bedroom. Upstairs.\""
show sam smile with dis
m "\"Oh.\""
show sam neutral talking with dis
m "\"I’ve never seen it.\""
show sam neutral -talking with dis
wi "\"It’s messy.\""
show sam laugh with hpunch
m "\"I don’t mind.\""
show sam smile with dissolve
wi "\"I do.\""
wi "\"But it can’t be helped.\""
scene black with fade
"When we climb the stairs and reach the foyer, the tobacco smell is cloying."
scene willapartmentnight with dissolve
show sam eyes at center,willroom1night with dissolve
show sam talking with dis
m "\"How much do you smoke, William?\""
show sam eyes -talking with dis
wi "\"That ain't my fault, though.\""
"At least not entirely."
"The place reeked of cigarettes before I moved in."
"Pipe smoke smells a hell of a lot sweeter."
show sam eyes talking with dis
m "\"I’ll get used to it.\""
show sam -talking with dis1
show sam talking with dis
m "\"You usually reek of somethin’ or other.\""
show sam neutral -talking with dis
wi "\"You’re no bed of flowers yourself when you get riled up.\""
show sam smile with dis
m "\"At least I use cologne.\""
wi "\"You mean perfume.\""
show sam neutral talking with dis
m "\"I mean cologne, William.\""
show sam neutral -talking with dis
"Soap and water’s just fine."
"I open the cupboard and fetch a glass and the whiskey bottle."
wi "\"Need a drink before we start?\""
show sam neutral talking with dis
m "\"Not much in the mood to drink.\""
show sam neutral -talking with dis
wi "\"Suit yourself.\""
"I pour myself a shot and wash it down."
"The burn wakes me up a bit."
"The pressure in my pants is starting to hurt."
wi "\"My bedroom.\""
scene black with fade
stop music fadeout 3.0
"I jerk my head and he follows me down the hall."
scene willbedroomlight with dissolve
show sam eyes at center,willroom2night with dissolve
show sam eyes talking with dis
m "\"We don’t have to rush if I’m gonna be here all night, you know.\""
show sam eyes -talking with dis
"I’m rushing?"
show sam neutral -talking with dis
wi "\"Guess I’m just used to having somewhere else to be.\""
wi "\"And there aren’t as many windows in my room.\""
"I feel the heat rise from my body when I start to strip."
"I can smell Sam’s perfume when he follows my lead, but there’s still the trace of his own scent underneath."

"We both take a seat on my bed, and the tension in the air between us is a bit thick."
wi "\"You uh... gonna get on your knees again soon?\""
show sam neutral talking with dis
m "\"Could do.\""
show sam smile with dis
m "\"But I figured we could try something else since this is the first time you’ve had more than an hour with me.\""
"The heat is rushing between my legs."
wi "\"Like putting me inside you?\""
show sam neutral talking with dis
m "\"You have a condom?\""
show sam smile with dis
"He’s making me too damn embarrassed."
wi "\"You think I have that sort of thing just lying around?\""
show sam neutral talking with dis
m "\"Dumb question I guess.\""
show sam smile with dis
"He puts his hand between my legs."
show sam neutral talking with dis
m "\"I’m the only one who really touches this, aren’t I?\""
show sam smile with dis
wi "\"...’m fine with that.\""
"He slips his hand under the tent in my trousers and touches me."
"And squeezes."
"It's a slow, slimy sound."
show sam eyes talking with dis
m "\"It’s a miracle you don’t have to buy many slacks.\""
show sam eyes -talking with dis
m "\"Seems like you ought to have ruined them by now.\""
show sam smile with dis
wi "\"It’s your fault.\""
show sam neutral talking with dis
m "\"Nah.\""
show sam smile with dis
"He curls his digits and strokes me once."
show sam neutral talking with dis
m "\"This is all you.\""
show sam smile with dis
wi "\"And how do you know that?\""
show sam eyes talking with dis
m "\"Because you’re the one who brought up burying it in me.\""
show sam -talking with dis
"Huh."
show sam smile with dis
"I guess it slipped off my tongue."
wi "\"Might be just the alcohol talking.\""
show sam neutral talking with dis
m "\"Then I guess you don’t want to be inside me.\""
show sam neutral -talking with dis
wi "\"I didn’t say that.\""
show sam neutral talking with dis
m "\"So what do you want?\""
show sam smile -talking with dis
"I exhale."
"I don’t want to deal with awkward small talk."
"If we’re gonna talk like this, I guess we’re gonna talk for real."
show sam surprised -talking with dis3
wi "\"How much shame do you feel when a man finishes in you?\""
"Sam stops stroking me."
show sam annoyed -talking with dis
"He glares."
show sam talking with dis
m "\"Why do you want to know?\""
show sam -talking with dis
wi "\"I just want to know what goes through your head when you do all this.\""
wi "\"Maybe so I can better understand myself.\""
wi "\"So let’s talk about it... man to man.\""
show sam surprised -talking with dis
"His glare turns into a surprised look."
show sam talking with dis
m "\"Never thought I’d be talking about this with you.\""
show sam surprised -talking with dis
wi "\"Well, me neither, so fair.\""
"...but I need to know."
show sam eyes talking with dis
m "\"I always feel a little foul after doing the deed, but the build up is heaven.\""
show sam eyes -talking with dis1
show sam eyes talking with dis
m "\"And the need comes often.\""
show sam eyes -talking with dis
wi "\"Does the shame ever feel good?\""
show sam surprised talking with dis
m "\"What makes you ask that?\""
show sam surprised -talking with dis
wi "\"For me, I think the pain and the pleasure start to blur sometimes.\""
wi "\"The depravity, I mean.\""
show sam eyes -talking with dis
wi "\"You ever feel like the more somebody tells us what’s right or wrong, the more satisfying it feels to just give them the finger?\""
wi "\"Especially because we know it feels good, and it’s not hurting nobody?\""
show sam eyes talking with dis
m "\"I understand.\""
show sam eyes -talking with dis1
show sam eyes talking with dis
m "\"That’s how I feel every time I break one of your laws.\""
show sam eyes -talking with dis
"That’s not how the government works."
wi "\"They ain't my goddamn laws, Sam.\""
show sam eyes talking with dis
m "\"Whatever you say, William.\""
show sam eyes -talking with dis1
show sam neutral talking with dis
m "\"But I want to understand more of what you mean.\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"About shame and pleasure blurring.\""
show sam neutral -talking with dis
"Oh."
"Shit."
"Maybe I told him too much."
wi "\"I don’t think you want to go through that, Sam.\""
show sam surprised talking with dis
m "\"Well, maybe I already do... to some extent.\""
show sam eyes -talking with dis1
show sam eyes talking with dis
m "\"Help me explore that, a bit.\""
show sam eyes -talking with dis
wi "\"You said you don’t have condoms.\""
show sam laugh with dis3
"He lets out a short laugh."
show sam neutral talking with dis3
m "\"You don’t have any bumps on your cock and you fuck nobody.\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"I think I’ll be fine.\""
show sam surprised -talking with dis
"His eyes shift away and he puts on a sheepish expression."
show sam neutral talking with dis
m "\"...Your stove work?\""
show sam neutral -talking with dis
wi "\"Yeah. There’s wood in the living room.\""
show sam neutral talking with dis
m "\"What about rags?\""
show sam eyes -talking with dis1
show sam eyes talking with dis
m "\"I need to make sure I’m clean.\""
show sam neutral -talking with dis
"Christ on a cracker."
"What debonair bullshit did I walk myself into now?"
wi "\"Cloth scraps are under the sink.\""
hide sam with dissolve
"He’s already rushing out of the bedroom."
"I sigh, feeling my shaft twitch in my pants."
"That one... always has to make himself immaculate, doesn’t he?"
"Can we just go, Sam?"
"..."
"Goddamn it."
"I read a small piece of literature on the city’s zoning laws to kill my erection while I hear pots and pans banging in the kitchen along with some swears."
"He’s lucky the sink works here."
"I wait for nearly 10 minutes before I hear some sloshing around and a cloth being wrung."
show sam eyes -talking s at center,willroom2night with dissolve
"And five more minutes before he’s finally back in the room."
wi "\"Was all that really necessary?\""
show sam neutral talking s with dis
m "\"I assure you. It was for what we’re about to do.\""
show sam neutral -talking s with dis
wi "\"Fine. I won’t make a fuss, then.\""
"He takes a seat next to me, and I hook my arm around his waist."
"His hand is on my thigh again."
show sam neutral talking s with dis
m "\"Talk me through what it’s like when I touch you.\""
show sam smile s with dis
"Jesus."
"This is hard."
wi "\"Feels like I’m touching a friend in a way I shouldn’t be touching them.\""
wi "\"And there’s a pit in my stomach.\""
wi "\"Like anybody could open the door at any moment and shout so loud that it makes my ears ring.\""
show sam neutral talking s with dis
m "\"That scare you?\""
show sam smile s with dis
wi "\"Should.\""
wi "\"But somehow, the look of disgust on their faces makes me want to rip off your pants and smile back while they watch, and they can’t do anything about it.\""
show sam neutral talking s with dis
m "\"They can’t do a damn thing if they ain't real.\""
show sam smile s with dis
wi "\"And they have to deal with me making your big damn dick swell up in your trousers while the smell fills the room.\""
show sam eyes -talking s with dis
m "\"The way you describe this stuff sticks with me...\""
m "\"...even though you make it sound a little foul.\""

show sam surprised -talking s with dis
wi "\"Men are foul, Sam.\""
"I stick my tongue down his throat and he’s all too receptive."
"He savors it, but I pull away with a soft smack."
wi "\"Filthy, even.\""
show sam eyes -talking s with dis
"I give more tongue."
"He sucks on it again. Like he’s nursing on it."
"Then I pull off again."
wi "\"I think I’m at peace with that, at least.\""
"His chest is heaving and his throat is starting to rumble."
show sam eyes talking s with dis
m "\"Is that why you can’t keep your hands off me?\""
show sam eyes -talking s with dis1
show sam eyes talking s with dis
m "\"Because you know it’s dirty?\""
show sam eyes -talking s with dis
"I feel my heartbeat in my shaft, pulsing with angry spurts of warm liquid."
wi "\"Because I want to empty into you more than I want to make another life with this.\""
wi "\"And I want the energy from that life to change you from the inside out.\""
show sam eyes talking s with dis
m "\"...change me, how?\""
show sam eyes -talking s with dis
"Maybe I’m going too far."
show sam neutral -talking s with dis
wi "\"Do you really want me to?\""
show sam neutral talking s with dis
m "\"I think I do.\""
show sam neutral -talking s with dis
"I don’t think I can tell you."
"I just have to show you."
show sam surprised -talking s with dis
wi "\"Okay.\""
"I stand up and I start to take the rest of my clothes off."
"My pants. My garters. My undergarments."
"A bit of me drips to the floor."
"I’ll clean it up later."
wi "\"First thing I’ll ask is... what else do you have to prep for to make yourself comfy enough for this?\""
"I cup my paw and bring it over my cock, forcing one slow thrust through it."
show sam smile s with dis
m "\"I hope you don’t mind but I saw you had some oil in the kitchen.\""
"He uncorks the stopper, pours some of the slick contents in his paw, and smears it on me."
show sam neutral talking s with dis
m "\"We’ll have to use more when we’re ready, but that’s a good start.\""
show sam smile s with dis
"I pick up my underwear and put them on the bed."
"Then I take a handkerchief out of the drawer."
"I fetch a bit of rope, too."
show sam surprised -talking s with dis
"He looks a little worried when I show him that."
"I feel guilt for what I’m about to do."
wi "\"Are you sure you want me to keep going?\""
show sam eyes -talking s with dis1
show sam surprised -talking s with dis1
show sam eyes -talking s with dis1
show sam surprised -talking s with dis
"He pauses this time."
"I think he’s still relaxed, but I can see that he’s still hard with his pants on."
show sam neutral -talking s with dis
"That’s good."
show sam neutral talking s with dis
m "\"I meant it when I said it.\""
show sam surprised -talking s with dis
wi "\"Then put your wrists behind your back.\""
"My heartbeat is pounding in my throat."
"Is this what you feel like all the time, Sam?"
show sam neutral -talking s with dis
"But he obeys me."
"Good boy."
show sam eyes -talking s with dis
wi "\"I’m going to put these ropes on your wrists to make you feel trapped.\""
"I shuffle up behind him, dangling a line of pre while I approach him."
show sam neutral -talking s with dis
"The ropes aren’t as soft as they probably should be."
"He might get burns if he struggles too hard, but his fur is pretty thick."
wi "\"They’re going on now.\""
show sam annoyed talking s with dis
m "\"Just do it...\""
show sam smile s with dis
wi "\"Alright. Goddamn...\""
"I loop them around as he holds still for me."
show sam neutral -talking s with dis
"I tie it in a way that I know he can’t get out of."
wi "\"Comfortable?\""
show sam neutral talking s with dis
m "\"As much as I can be with rope around my wrists.\""
show sam neutral -talking s with dis
wi "\"Okay.\""
wi "\"I wanted you to feel trapped while you’re hard.\""
wi "\"Do you?\""
show sam eyes talking s with dis
m "\"Aside from the rope, not really.\""
show sam neutral -talking s with dis
wi "\"I think I’m gonna loosen you up.\""
show sam smile s with dis
"Sam hums."
show sam neutral talking s with dis
m "\"You know how?\""
show sam smile s with dis
"He thinks I’ve never teased an asshole before."
"That’s cute."
wi "\"Course I know how. Lift those legs...\""
"He struggles to adjust himself properly without the use of his arms for leverage."
"I get some of that oil onto my middle finger until I can see it shine."
show sam neutral talking s with dis
m "\"I don’t really need a finger, you know.\""
show sam neutral -talking s with dis
wi "\"Relax. It loosens the muscles.\""
wi "\"Makes going in a hell of a lot more comfortable for both of us.\""
hide sam with dissolve
show sam surprised -talking d at center,willroom2night with dissolve
"He lies back and lifts his legs in the air, looking a little uncomfortable."
"Ugh."
show sam neutral -talking d with dis
wi "\"Don’t worry. I won’t be a priss about it.\""
"I pour some of the oil in my hands and rub it between my digits."
"Then I go to the bed and sit on my knees and grab him by the ankles, lifting them up in the air."
hide sam with dissolve
scene wilcg5 with slow_dissolve
"I’ve never been this close to his balls before."
"And beneath them?"
"He can brag about wearing perfume as much as he wants, but that smell is all him."
"Even lower I see that pale ring of muscle."
"I prod at it with my middle digit."
"The fur on his legs stands up when I do."
"Then I slide against it, curling into a hook for an easy opening."
wi "\"...and there it goes.\""
"He sucks on his teeth as the pressure gives way, and I slide on into him."
"And he groans."
wi "\"Now I’ll pull out slow.\""
"It’s easy enough to slip out of him."
"He sighs, like he’s steeling himself for something."
wi "\"Going back in.\""
"I go up to the knuckle and he grits his teeth."
wi "\"I just have to keep this up and it’ll tire you out.\""
wi "\"And you won’t clench when I’m sliding in.\""
"The next time my finger goes in I curl upward."
"He looks back at me with something close to panic in his eyes as his length is the one going stiff now."
wi "\"I guess I found your special spot too, huh?\""
m "\"I didn’t think you’d know about that.\""
wi "\"Course I do.\""
wi "\"I knew there had to be another reason why men put things up there.\""
wi "\"Some even get addicted to it.\""
"Every curl just makes him bigger."
wi "\"You think of yourself as one of those people, Sam?\""
"I don’t need to hear him say yes or no, really."
"He loves being a slut."
"Can smell it on him and see it in his eyes."
"And I’ve made him really big."
m "\"I don’t really think much on it.\""
wi "\"Then don’t think.\""
wi "\"Your body already knows what it wants, don’t it?\""
m "\"Yeah.\""
wi "\"So what does it want right now, Sam?\""
"He grunts and pushes back against me as best as he can and his tip starts to leak, too."
m "\"The real deal.\""
"I have to watch him for a bit."
"His chest is heaving."
"He’s leaking uncontrollably."
"He reeks with need."
"I envy him."
"Maybe he’s starting to understand."
"Then I slide away and grab him by the arm."
wi "\"Stand up.\""
"He complies, and sprays from his tip fall to the floor."
"I grab my undergarments on the bed and pick them up."
wi "\"Open your mouth.\""
m "\"Why--\""
"That’s all I need to stuff it in."
wi "\"Because a bandana alone isn’t enough to act like a gag.\""
"And you’ll only be able to focus on how I taste when I do all these things to you."
"I wrap the scarf around his head."
wi "\"This will help you remember not to spit anything out while you yell.\""
"I bend him over the bed."
"Then I hook my finger in his ass again."
"I wiggle it to make him yell-- as much as he can with the dampened rag."
wi "\"It’s good that you’re yelling.\""
wi "\"You can do it as much as you like and nobody will hear it.\""
"I grab the length of my cock to the opening of his rear and slide my tip against it."
wi "\"I think our bodies were meant to scream, sometimes.\""
"My tip is pressing beneath his tail right now."
"I can feel the muscles about to give way."
wi "\"Don’t yell that you want it.\""
wi "\"Yell out because you want it.\""
scene wilcg4 with slow_dissolve
"And when he shifts, and I start to sink in, he does what I say."
"I hilt my cock in his pert cheeks until I feel my balls touch his, and then I roll my hips."
"I go in and out, just like my finger did, and it don’t take long for the both of us to feel too warm."
"So I slip on out and roll him over, feeling how heavy he is."
wi "\"We’re like prisoners in these bodies, Sam.\""
wi "\"Doesn’t matter what the heart or the mind really wants.\""
"His fat monster of a cock is just drumming against his belly now."
"Like he’s hurting for a release."
"But I can’t let him have that yet if he wants to understand."
wi "\"Our instinct drives us toward a particular direction.\""
"I grab his ankles and lift them again."
"Then I walk forward again, letting gravity and his legs bear my weight as I sink into him another time, deeper than before."
"Sweat rolls down my back as I move in him."
wi "\"See? It’s always about control.\""
"I roll my hips into him, inside of him."
"Then I clamp my mouth over his neck and bite into his scruff."
"I feel him writhe under me, and I can’t help but smile."
wi "\"The control your own body has over you.\""
"Faster."
wi "\"The control others have over your needs and your feelings.\""
"Harder."
wi "\"And you. Just have. To take it.\""
"He cries out when I lap his nipples too beneath the fur, making his head thrash left and right."
"Please him like I would a woman, though every cell in my body knows he isn’t."
"And doesn’t want him to be."
"Because I see him jab the air every time I dip in deep."
"I look down between his legs, deeper into his prick's drooling eye, sinking as more of my body weight shifts over him."
scene willbedroomlight with dissolve
"Reminding me what my instinct demands."

menu willbedchoice:
    "..."
    "Take care of that, Cocksucker.":
        $ SW_Points +=1
        "Well... fuck that idea, I ain't gonna suck it."

        "But goddamn is this the slimiest he’s ever made himself."

        "And if it goes like that too much longer, it might turn blue."

        "Well..."

        "He’s a good boy, though."

        "And I’ve touched my own, plenty."

        "And besides..."

        wi "\"Bit fucked up when it’s somebody else who decides what your body can do, ain't it?\""
        "I smear my paw over the pre on his prick and then rub it on his nose."
        wi "\"You have no control over that.\""
        "The stickiness is so fucking loud when I start to stroke him."
        wi "\"As good as that feels, it’s still terrifying.\""
        "The more I make his prick shine, the more of a mess the tip makes."
        wi "\"So the two can start to blend.\""
        "I wipe the excess on his abs and the rest of it around his length and balls."
        wi "\"You get it now?\""
        "His eyes close shut and the muffled scream is lengthy this time."
        "Wait a minute, is he already..."
        wi "\"Shit!\""
        "He’s blasting off like a cannon and it’s too late to move my hands."
        "There’s already more than three bursts of it coating my paw, the rest hitting him beneath the chin."
        "The smell is pungent, and it’s familiar enough to my own that I..."
        "Feel the pressure in my balls pull back."
        "And jolts fire off in my body."
        wi "\"Shiiiiit!\""
        "I’m finishing in him, filling him up, without even any protection..."
        "And that makes me bury myself deeper."
        "Like I’m stuck in him."
        "And we can be trapped here together in this... well, this mess."
        "...the hell did he do to my paw?"
        show handwil cum at center,willroom2night with dissolve
        "Christ."
        hide handwil with dissolve
        "There aren’t any rags in the kitchen."
        "His eyes flick to his gag impatiently, so I untie the bandana."
        "I cringe a bit as I stain it."
        "He pushes my underwear out of his mouth with his tongue and lets it slop to the floor, then starts taking deep breaths."
        m "\"Mind letting me loose, William?\""
        wi "\"Once I figure out where I can wipe my hand.\""
        m "\"You could always lick it clean.\""
        wi "\"Hell no.\""
        scene willapartmentnight with dissolve
        "I go out to fetch some newspaper from the living room."
        "It’s not perfect, but it’ll do for the moment."
        show handwil ohno at center,willroom1night with dissolve
        "Shit, there’s terrible opinions sticking to my hand now."
        scene willbedroomlight with dissolve
        "My paws are as clean as they're gonna get, so I undo the bonds of rope behind his hands and pull the coils off of his wrists."
        wi "\"Sorry.\""
        "That’s all I can really say about this."
        "I really did go too damn far, this time."
        "But then Sam hooks his arms around my neck and pulls me in."
        m "\"Don’t be.\""
        "And he makes me taste myself on his tongue."
        "Making me remember what I used to do between my legs in private when I bent over far enough."



    "He’ll be able to use his own hands once I’m done with this.":
        "I close my eyes and think about my own dick more than his."
        "And I picture it firing off, louder than any pistol, hotter than any bullet."
        "Putting this embarrassing act to a close."
        "And I feel myself pumping into him, as clarity and relaxation wash over me."
        "Then I pull out of him and undo his bonds."
        "He doesn’t bother to take off the gag before he finishes himself off."
        "I look away to give him some decency, but I can still hear him finish."

scene black with slow_dissolve
stop background fadeout 3.0
"...Christ, that was exhausting."
"What the hell got into me last night?"
play sound "sfx/knock.ogg"
"Somebody’s banging on the door to the office downstairs."
scene willbedroomnight with slow_dissolve
stop sound
play music "music/typical day.ogg" fadeout 4.0 fadein 5.0
"It’s morning?"
"Shit."
"I don’t remember us falling asleep."
"But we did so much I must’ve conked out."
"Sam is on his side with his back to me and his tail resting between my legs."
"I check my watch."
"It’s almost seven A.M. there, so five A.M..."
"Shit."
"I touch my temples and rub."
"Then I shake his shoulder."
wi "\"Time to wake up, sunshine.\""
m "\"Already am.\""
"What the..."
"I stop shaking."
wi "\"And when did you get up?\""
m "\"Can’t be sure.\""
m "\"Feels like hours ago.\""
wi "\"You get enough shut-eye?\""
m "\"Enough. Yeah.\""
m "\"Say... William?\""
"He still hasn’t turned around yet."
"He’s looking up the walls."
m "\"Are the walls in this building hollow?\""
"Bit of a queer thing to say."
"...especially first thing in the morning."
wi "\"Sounds don’t get out too well, so they’re insulated with somethin’.\""
wi "\"Why do you ask?\""
show sam sad -talking n at center,night with dissolve
"He turns around, still looking up."
show sam sad talking n with dis
m "\"Heard things crawling around.\""
show sam sad -talking n with dis1
show sam sad talking n with dis
m "\"Sometimes it sounded like somethin’ was gonna break out.\""
show sam sad -talking n with dis
"Sometimes I have to wonder if his head is completely okay."
"That Jack fella really fucked him up."
show sam neutral n with dis
wi "\"...See any cracks in the walls, then?\""
show sam neutral talking n with dis
m "\"No.\""
show sam sad -talking n with dis1
show sam sad talking n with dis
m "\"At least, I don’t think so.\""
show sam neutral -talking n with dis
wi "\"Then tell me if you do.\""
show sam sad -talking n with dis
"I glide my hand over his shoulder but take it back as he sits up."
"His back is hunched and his head is hanging low."
"He could probably use some water."
play sound "sfx/knock.ogg"
show sam surprised -talking n with dis
"Jesus."
"That banging’s just getting louder."
stop sound
"It better not be Todd."
"I peek through the shutters and guard the sunlight from my eyesight."
"It’s him."
"I’ve told him a dozen times where the spare key to the office is."
"Though it’s not like I can complain."
"I just slept in and got caught with my pants down, so to speak."
"...let’s fix that."
"I get dressed as quickly as I can."
"Then I remember that I was going to get Sam some water."
"...Todd can wait a little longer."
scene willapartmentnight with dissolve
"I fetch a glass in the living room, fill it up, then bring it to him."
scene willbedroomnight
show sam n at center,night
with dissolve
wi "\"Drink. Some fluid will help you wake up.\""
play sound "sfx/knock.ogg"
show sam surprised -talking n with dis
pause
show sam surprised talking n with dis
m "\"Who’s makin’ that fuss outside?\""
show sam surprised -talking n with dis
wi "\"It’s just Todd.\""
stop sound
show sam neutral talking n with dis
m "\"Sounds urgent.\""
show sam -talking n with dis
"It’s probably not."
"Because if it were urgent he’d remember where I put the spare key."
wi "\"Might be.\""
show sam annoyed -talking n with dis
wi "\"But I’m not letting you out of my sight until you finish that glass of water.\""
"He glares, then tips his head back to chug it."
"A bit cheeky, but if it gets the job done..."
show sam annoyed talking n with dis
m "\"There. All done.\""
show sam annoyed -talking n with dis1
show sam eyes n with dis1
show sam annoyed -talking n with dis
"He pushes the covers off and plants his feet on the floor a little stiffly, then blinks."
"His eyes aren’t rolling back or drifting out of focus, and his pupils aren’t contracting and dilating, so that’s a relief."
show sam annoyed talking n with dis
m "\"You done staring me down, Sheriff?\""
show sam annoyed -talking n with dis
"Is he really going to judge me for staring as if asking if somebody’s walls are hollow or not is normal?"
play sound "sfx/knock.ogg"
"That’s the kind of stuff that makes me worry about you, Sam."
show sam n with dis
wi "\"No need. My gaze had its fill of you last night.\""
stop sound
show sam neutral talking n with dis
m "\"Must have been hard for you.\""
show sam -talking n with dis
play sound "sfx/knock.ogg"
"Todd’s still banging on the door."
show sam neutral talking n with dis
m "\"You gonna get that?\""
stop sound
show sam -talking n with dis
wi "\"Not until you’re dressed and ready to go downstairs.\""
show sam eyes talking n with dis
m "\"I’ll be quick about that.\""
show sam eyessmile -talking n with dis1
hide sam with dissolve
pause 0.45
show sam neutral -talking s at center,night with dissolve
"He steps over his undergarments and drawers on the floor and tugs the fabric up his legs."
wi "\"So you’re the one volunteering to get the door, then?\""
show sam eyes -talking s with dis
"He waddles towards the shades and tilts his head."
play sound "sfx/knock.ogg"
pause
show sam neutral talking s with dis
m "\"Nah.\""
show sam annoyed -talking s with dis
stop sound
wi "\"Then hurry up. I have to lock the door behind me.\""
show sam annoyed -talking -s with dis3
"He’s mumbling about eating his ass under his breath, as if I can’t hear him while he snatches his shirt, tucks it in, and then hooks his suspenders over his shoulders."
scene black with fade
stop music fadeout 3.0
"Finally he’s ready to go, and I lock the door on the way out."
scene jailnight with dissolve
play sound "sfx/knock.ogg"
pause
"Todd’s still pounding on the door like a madman."
stop sound
wi "\"Hold your goddamn horses, I’m coming.\""
scene black with fade
"I let him finish his flurry of blows before turning the knob, letting the door creak open."
scene echoroadnight with dissolve
show tod talking at center,nightbrown with dissolve
to "\"Well there you are, Sheriff.\""
show tod with dis
play music "music/quiet.ogg" fadeout 4.0 fadein 5.0
"He looks a bit of a mess."
show tod surprised with dis
wi "\"Did you forget about the key, Todd?\""
show tod sad with dis
to "\"Oh, right.\""
show tod arms happy with dissolve
to "\"Well that ain't important right now.\""
show tod surprised with dissolve
to "\"I needed to tell you that I met Huxley Greene.\""
"Well, that’s good news at least."
wi "\"Oh, yeah? And what sort of state was he in?\""
show tod sad with dis
to "\"Well, none too good, considering he didn’t have a head.\""
"What?!"
show tod surprised with dis
wi "\"You mean he’s dead?\""
show tod talking with dis
to "\"Well that’s what the wallet in his pocket said, but I brought his body just to make sure.\""
show tod surprised with dis
"I grab his shoulder to move him aside and see the carcass-sized pillow case."
wi "\"You dragged this all the way here?!\""
show tod talking with dis
to "\"I figured you would like to look at him before the bugs and buzzards got the rest of him.\""
show tod surprised with dis
"I lift my shirt up over my nose and crouch down, then lift the sheets off of the body."
"It’s frozen, so the smell isn’t as bad as it could be, but there are pieces of fur and flesh missing."
"Those are definitely his clothes, though-- I’d recognize Marcy’s stitchwork anywhere."
"And hard to mistake the thick, bald rat tail that looks more like a pale worm than anything else."
wi "\"Yeah. That’s probably him.\""
wi "\"Let’s haul him inside.\""
show tod annoyed with dis
to "\"Yes sir.\""
scene black with fade
"Todd carries one side and I carry the other into that open jail cell we had used the other night for the same purpose."
scene echoroadnight with slow_dissolve
show tod surprised at center,nightbrown with dissolve
"I check outside again to see if we’ve dropped anything, but there’s nothing much to look at."
wi "\"I would have thought this man was lying low or hopped a train out of town.\""
wi "\"But something like this in a place like here?\""
wi "\"It’s just yet another thing that don’t make much sense.\""
show tod sad with dis
to "\"Well... you know what they say...\""
show tod talking with dis
to "\"When it’s your time, it’s your time.\""
show tod surprised with dis
wi "\"Who’s they exactly?\""
show tod arms happy with dissolve
to "\"Some Jesuits down the street.\""
wi "\"The man had his head ripped off. He didn’t die of old age.\""
show tod surprised with dissolve
to "\"Well I already know that.\""
wi "\"I mean that if he’s been dead for, let’s be honest, what looks like at least a few days...\""
wi "\"Then he would have had to be real quick about issuing a hit on Mr. Tibbits.\""
wi "\"...See what I’m saying?\""
show tod eyes happy with dis
show tod surprised with dis
"Todd blinks at me."
"Come on, you can put it together."
show tod talking with dis
to "\"Are you saying he just hated what he couldn’t understand?\""
show tod with dis
wi "\"...I’m saying he might not have placed the hit, Todd.\""
show tod sad with dis
to "\"If not him, then who?\""
show tod surprised with dis
wi "\"Now that’s a great question, Todd.\""
$ renpy.notify("Notebook updated.")
$ quick_menu = False
$ quick_menu_will = True
$ unlocked_journal_pages += 1
$ willnote = True
wi "\"This is why I always bring my notebook with me when I'm keeping track of my thoughts.\""
$ renpy.notify("Notebook updated.")
$ unlocked_journal_pages += 1
$ current_journal_page = 1
wi "\"You ought to start picking up the practice yourself.\""
wi "\"Now what do you say we do what we should have done in the first place and pay Mr. Tibbits a visit?\""
hide tod with dissolve

"I turn and see the red of Sam’s eyes staring from my office."
show sam neutral -talking at center,nightbrown with dissolve
wi "\"We’ll be back soon. Keep the interior locked.\""
show sam eyes talking with dis
m "\"...Okay.\""
show sam eyes -talking with dis1
hide sam with dissolve
"He disappears behind the window and we hear the heavy lock of the door click."
wi "\"Shouldn’t be long.\""
show tod at center,nightbrown with dissolve
"I don’t know if that’s true, but he is just next door."
show tod surprised with dis
to "\"So wait. What’s Sam doing in there at this hour?\""
wi "\"Debriefing.\""
"Technically not wrong."
show tod happy arms with dissolve
to "\"Gee. I guess he does work late hours, doesn’t he?\""
wi "\"He works hard.\""
show tod eyes happy with dissolve
to "\"And there’s no shame in that.\""
show tod surprised with dissolve
wi "\"I didn’t exactly say that, Todd.\""
show tod talking with dis
to "\"I just mean that I think he must have to do all sorts of really difficult things.\""
show tod sad with dis
"I give him a look."
show tod surprised with dis
wi "\"You think about those things a lot, Todd?\""
show tod talking with dis
to "\"No.\""
show tod surprised with dis
hide tod with dissolve
"He doesn’t say anything else for the rest of the walk."
"When we reach the door to Mr. Tibbits’ apartment, some things immediately don’t make sense."
wi "\"This lock is scratched to hell and back.\""
"I swivel the knob to see if it’s still locked, but it’s completely loose."
cl "\"I told you once and I’ll tell you again that you aren’t welcome here!\""
cl "\"I’ll have you know that if you knock down that door the authorities will be here in an instant!\""
wi "\"It's just us, Mr. Tibbits.\""
cl "\"Oh, thank goodness!\""
"I hear some of the furniture move around and something rattles against the door."
"The door pops open and the twitchy little man takes a step back."
cl "\"Please come in. I’ll put on some tea.\""
scene cliffroom with slow_dissolve
show cli at left,cliffroomnight:
    xzoom -1
show tod talking at right,cliffroomnight
with dissolve
to "\"What kind?\""
show tod
show cli talking
with dis
cl "\"Black with a bit of bergamot, surely!\""
show cli with dis
wi "\"That won’t be necessary Mr. Tibbits, but do what makes you feel comfortable.\""
wi "\"Just get straight to the point and tell us what the hell is going on up here.\""
show cli doubt with dis
cl "\"Well I had thought it was patently obvious that I am frightened, Sheriff.\""
wi "\"Don’t be cute. Frightened of who?\""
show cli frustrated with dissolve
cl "\"Of that brute and bully who calls himself Reed!\""
show cli eyes talking with dissolve
$ unlocked_journal_pages += 1
$ current_journal_page = 2
$ renpy.notify("Notebook updated.")
cl "\"That wolf came clawing at my door tonight and broke the lock!\""
show tod sad
show cli eyes
with dis
to "\"That’s terrible!\""
show tod surprised with dis
show cli angry with vpunch
cl "\"That’s not the half of it!\""
show cli sad with dissolve
cl "\"He would have been upon me if I hadn't barricaded the door with all of the furniture I could put together in this ramshackle apartment!\""
wi "\"So you know it was him for sure?\""
show cli doubt with dissolve
play sound "sfx/match.ogg"
"The stoat is filling his kettle and striking a match beneath the wood stove."
show cli eyes talking with dis
cl "\"I’d know that greasy grey fur and those dumpy little ears anywhere.\""
show cli eyes with dis
show cli eyes talking with dis
cl "\"And if I were blind, there’d of course be the smell.\""
show cli eyes with dis
show cli eyes talking with dis
cl "\"You know, mustelids get all sorts of earfuls about how we put off an offensive odor simply for our ordinary body scents.\""
show cli eyes with dis
show cli eyes talking with dis
cl "\"But canines have a particular kind of reek to them that’s unmistakable.\""

show cli blush eyes closed with dis
"He stops all of a sudden, a bit flushed in the ears."
show tod talking with dis
to "\"Well he’s right about that, William.\""
show tod with dis
"I do not give one iota of a fuck about this conversation."
show cli doubt with dis
wi "\"Mr. Tibbits? Please focus. I’ll check into Reed.\""
show cli frustrated with dissolve
cl "\"That’s splendid, but I won’t feel a moment’s peace with that madman on the loose.\""
wi "\"I’d like you to stay at the station for a while.\""
show cli doubt with dissolve
cl "\"You think I’d feel safer inside of a prison cell?!\""
wi "\"Nobody said nothin’ about any prison cells.\""
show tod happy arms with dissolve
to "\"William has a comfy couch in his office. Heck, I’ve slept there plenty of times.\""
show tod surprised with dissolve
show cli talking with dis
cl "\"Not on taxpayer dollars, I hope.\""
show cli doubt with dis
"Todd looks like he just got hit in the face with a shovel."
"There’s no way he’d be able to handle somebody like Cliff on his own."
wi "\"Let’s talk about the other things to do to keep you safe.\""
"He turns to look at me as he fills a few metal capsules with dry leaf and flower bundles."
show cli eyes talking with dis
cl "\"Such as?\""
show cli eyes with dis
wi "\"It’s common protocol to investigate a victim a little closer after they’ve been attacked.\""
wi "\"Helps us piece together a few things.\""
"He places three teacups on his little table."
show cli happy with dis
cl "\"I think you’ll find I’m an open book, so ask away.\""
wi "\"Let’s start with who you think might want you dead.\""
show cli doubt with dis
cl "\"Seems rather obvious, doesn’t it?\""
wi "\"Just tell me who you think it is.\""
show cli eyes talking with dis
cl "\"Huxley and Reed, without a doubt?\""
show cli eyes with dis
wi "\"Okay.\""
"I watch his expression as he puts down his little teacups onto the table."
wi "\"But who else?\""
show cli doubt with dis
"His lip curls and he looks sideways."
show cli eyes with dis
"...which probably means that he was thinking about it before I asked him."
show cli eyes talking with dis
cl "\"Perhaps somebody who doesn’t want me here.\""
show cli eyes with dis
"Now we’re getting somewhere."
wi "\"But why go through all the trouble to use violence to stop your academic endeavor?\""
"I lean in a little bit closer."
wi "\"I hear plenty of stories about how cutthroat a field academia is without even needing any bloodshed.\""
show cli doubt with dis
play sound "sfx/kettle.ogg"
"The kettle whistles."
show cli eyes talking with dis
cl "\"A moment!\""
show cli eyes with dis
hide cli with dissolve
stop sound fadeout 2.0
"I can tell that he’s relieved by this distraction."
show cli happy at left,cliffroomnight with dissolve:
     xzoom -1
cl "\"Sugar and cream?\""
show tod eyes happy with dis
to "\"Sugar and cream!\""
show cli doubt with dis
show tod with dis
wi "\"So who do you think might use violence against you, Cliff?\""
wi "\"Because they don’t want you here?\""
show cli eyes with dis
"He pours his own cup of tea first, then Todd’s, then mine."
show cli talking with dis
cl "\"Perhaps some greedy businessmen who don’t see eye to eye with my benefactor.\""
show cli eyes with dis
show cli eyes talking with dis
cl "\"I doubt I’d know their names.\""
show cli eyes with dis
wi "\"So who is the benefactor that brought you to Echo?\""
show cli doubt with dis
cl "\"The same man who drew you here, from what I understand.\""
wi "\"Name him, please.\""
show cli eyes talking with dis
cl "\"Sorry, but that’s confidential.\""
show cli eyes with dis
wi "\"Mr. Tibbits.\""
wi "\"Just because I asked you nicely doesn’t mean you can withhold that information.\""
wi "\"This is basic information pertinent to whether or not your worker’s permit can be deemed valid.\""
show cli sad with dissolve
cl "\"Well bend my arm, why don’t you?\""
wi "\"The name, Tibbits...\""
show cli doubt with dissolve
cl "\"Very well!\""
show cli talking with dis
$ unlocked_journal_pages += 1
$ current_journal_page = 3
$ renpy.notify("Notebook updated.")
cl "\"It’s Mr. Hendricks, of course.\""
show cli with dis
"I’m not surprised at all."
"This is exactly the kind of clown shit that would have his name all over it."
"But I want to rely on as few assumptions as possible."
wi "\"Could I see your official paperwork?\""
show cli eyes talking with dis
cl "\"I don’t see how that’s relevant to anything, but of course.\""
show cli eyes with dis
"He picks up the satchel by his feet, unlatches it, then plucks a gray folder from it and passes it to me."
"I thumb through it."
"It states his full name, Clifford Tibbits, and his job title, consultant, in gold letters. Health information follows."
wi "\"This is beautiful stationery.\""
show cli happy with dis
cl "\"Thank you!\""
"I hand it back to him."
wi "\"Government issue type face is bare-bones and clinical. This is a CGCS form, not an official government verification.\""
show cli shocked with vpunch
show tod surprised with dis
cl "\"I’m afraid that my work permit is still moving through the post.\""
show cli sad with dissolve
cl "\"If I’m lucky it should arrive in a week or two, and you’ll have your paperwork then.\""
"As far as I can tell, everything this man has told me has been truthful."
"But I can tell that his cards still aren’t all on the table."
show cli doubt with dissolve
wi "\"What’s something official you have that can prove you are who you say you are?\""
show cli talking with dis
cl "\"Would travel tickets suffice, Mr. Adler?\""
show cli with dis
wi "\"It’s better than nothing.\""
show cli doubt with dis
cl "\"Well it’s the last thing that I have.\""
"He slides me a ticket."
"It states a passage for one person on an ocean liner. A Cornelis van Houwelinck."
wi "\"Your ticket, Mr. Tibbits.\""
show cli talking with dis
cl "\"That’s mine.\""
show cli doubt with dis
wi "\"This is a ticket for a man named Cornelis.\""
show cli down with dis
"He looks down."
show cli blush eyes right with dis
$ current_journal_page = 4
$ unlocked_journal_pages += 1
$ renpy.notify("Notebook updated.")
cl "\"And that’s my, ah, birth name.\""
show cli doubt with dis
cl "\"I don’t believe it is criminal to have an alias, is it Sheriff Adler?\""
wi "\"Not really, no.\""
show cli eyes with dis
cl "\"Lots of people do it.\""
show cli eyes talking with dis
cl "\"Especially when they’re writing books.\""
show cli eyes with dis
show cli talking with dis
cl "\"It’s a bit romantic to be able to choose your own name, isn’t it?\""
show cli blush eyes right with dis
cl "\"All you have to do is pick your mother’s maiden name as your own and suddenly you can turn yourself into a sports writer rather than a romance author.\""
show cli blush eyes left with dis
cl "\"You can become anything you want, really.\""
show cli blush eyes closed with dis
"But there’s a difference between calling yourself something new and living out a good part of your life as that something."
"You might not want to be what you choose to become."
"A life isn’t a pen name, or a book cover, or a change of scenery."
"It’s everything you are."
"...my wrist watch sounds too damn loud again."
wi "\"It’s just a bit concerning, what with everything that’s happened around you, is all.\""
show cli doubt with dis
cl "\"Oh, and that’s my fault, is it?\""
"The weasel sips his tea."
show cli eyes talking with dis
cl "\"You bit off more than you can chew when you took this job, didn’t you?\""
show cli shocked
show tod yell
with vpunch
to "\"Hey!\""
show cli doubt with dis
show tod annoyed with dis
to "\"Why are you being so unneighborly with us?\""
show cli eyes with dis
"The stoat gestures broadly to his wrecked living room."
show cli frustrated with dissolve
cl "\"Because I’m a little bit frightened right now, Mr. Bronson.\""
show cli doubt with dissolve
cl "\"I think we want the same things though, right, Sheriff?\""
show cli talking with dis
cl "\"I help you unmask some of the monsters trying to murder me, and I just keep telling you the truth like I always have.\""
show cli happy with dis
cl "\"But just let me hold onto the idea of what I want to be a little longer, and let me keep using that new name.\""
"So there it all is, then."
stop music fadeout 3.0
wi "\"I can recognize a fair deal when I see one.\""
show cli doubt with dis
"I hold out my paw to him."
show cli eyes with dis
play music "music/toddtheme.ogg" fadein 5.0
"He clasps it cautiously."
show cli with dis
wi "\"You gonna stay at the station then, or what?\""
show cli talking with dis
cl "\"...Let me go wake Mr. Byrnes first and I’ll be on my way shortly.\""
show cli with dis
wi "\"Byrnes is here?\""
show cli sad with dissolve
cl "\"He has work early.\""
show cli doubt with dissolve
cl "\"I didn’t want to wake him.\""
wi "\"I thought you said you were attacked?\""
show cli eyes talking with dis
cl "\"You think I can’t riposte Mr. Adler?\""
show cli happy with dissolve
cl "\"I told you that I can take care of myself.\""
show cli eyes talking with dis
cl "\"Mr. Byrnes was running a fever, and he’s practically naked at the moment.\""
show cli with dis
wi "\"...I’ll give y’all some space then.\""
show cli happy with dissolve
cl "\"Very good. I shan't be long.\""


scene black with fade
scene echoroadnight with slow_dissolve
"We wait a while outdoors until we see a very weary-looking Murdoch emerge from the apartment."
"He looks from side to side, rubbing his snout before making his way toward the direction of his father’s store."
show mur eyes at center,nightbrown with dis3
"He staggers a bit, but he makes his way there."
hide mur with dissolve
show cli happy at center,nightbrown with dis3
"Mr. Tibbits leaves the apartment five minutes later with a heavily stuffed bag and follows us to the station."
scene black with fade
stop background
scene officeday with slow_dissolve
"I feel like I’m in the calm of a hurricane before the storm comes."
"I think I was right about disaster following this weasel, but I don’t think he’s the only one stirring up trouble by far."
"Considering the way Huxley died, and with Cliff having ties to James, I’m almost certain now that the rat didn’t place the hit on the stoat."
"But if that’s the case, then how did he get the gun?"
"And if Cliff is telling the truth, then why was Reed trying to break into his apartment?"
"Did they plan the hit together and then something happened to Mr. Greene before he lost the gun?"
"Maybe."
"I’ll have to have a chat with Reed again before I have any reason to believe he has that much spite."
"Because as of now, that still don’t make much sense to me."
"I’d pin down Reed as a guy willing to get his own hands dirty."
"Or to start shit when he’s bored."
"He could definitely beat a man to death in broad daylight if he were mad and drunk enough."
"But plotting a murder while sober?"
"I just can’t see it."
"If the two of them already jumped this weasel in broad daylight then what’s the point of giving a kid a traceable gun to take care of him in secret?"
"Maybe they just fucked it up."
"Simple as that."
"Case closed."
"...but then how did he get his goddamn head severed?"
"I have more than a few things to consider now."
"I could go to the mayor and have a little chat about how things are going."
"...Any time, really. He spends most of his time in his office doing nothing when there isn’t a ribbon to cut or a speech to unload."
"And he has no real jurisdiction over me."
"Or I could go to the Stag that Nik and the Byrnes boy keep bringing up from time to time."
"It’s the biggest men’s club in town."
"And more importantly, I know that the mining union tends to congregate there."
"Perhaps the suggestion to go wouldn’t be a waste of time after all."
"Tricky thing is... wherever I go first will take all day."
"If I want Nik’s help at the Stag, it will have to be at night."
"But if I want a more private audience with the mayor, and I don’t WANT Nik there at the Stag with me, I should maybe go to the Stag first."
$ current_journal_page = 5
$ unlocked_journal_pages += 2
$ renpy.notify("Notebook updated.")
"Regardless, I shouldn’t stall."

menu willinvestigation1:
    "Where am I going first?"
    "City Hall.":
        jump cityhallday

    "The Stag.":
        jump stagday

label cityhallday:
$ CITYHALLDAY_Points +=1
label cityhallnight:
wi "\"Alright, I’m off to see mayor Testerman.\""
wi "\"Are you still able to keep watch over everything while I’m gone, Todd?\""
show tod arms happy at right,prisonday with dissolve
to "\"Sure thing!\""
show tod talking with dissolve
to "\"Did I hear that you’re paying old Franz another visit?\""
show tod with dis
show tod talking with dis
to "\"Why, that’s basically an honor.\""
show tod with dis
wi "\"Not really.\""
wi "\"He just wants to ask me whether or not the city is close to a state of emergency.\""
show tod arms happy with dissolve
to "\"That sounds like him alright.\""
show tod eyes happy with dissolve
to "\"Old Franz always looks out for us.\""
show tod talking with dis
to "\"Seems like only yesterday when I was a pup that he gave old woman Willoughby his own jacket on Easter Sunday.\""
show tod with dis
show tod talking with dis
to "\"I remember how she said her feet turned so cold!\""
show tod with dis
show tod talking with dis
to "\"And when the doctors paid her a house call, they said she nearly died!\""
show tod with dis
show tod talking with dis
to "\"But she dreamed about Franz.\""
show tod surprised with dis
to "\"In her dreams he was an angel, William!\""
show tod talking with dis
to "\"And he brought her back from the cold while she was asleep.\""
show tod with dis
wi "\"So you’re saying that he did the bare minimum that most people would do for an old woman, and then took credit for saving her life?\""
show tod eyes happy with dis
to "\"Well, the Lord works in mysterious ways, William.\""
show tod arms happy with dissolve
to "\"I think you could argue that he pretty much did save her life, no matter how you look at it.\""
"This poor man."
wi "\"That’s nice, Todd.\""
show tod eyes happy with dissolve
to "\"Lots o’ things are nice when you just stop to think about 'em.\""
show sam annoyed at left,prisonday with dissolve:
    xzoom -1
show sam annoyed talking with dis
show tod surprised with dis
m "\"{i}...These things hast thou done, and I kept silence; thou thoughtest that I was altogether such a one as thyself: but I will reprove thee, and set them in order before thine eyes.{/i}\""

show sam annoyed -talking with dis
"Sam is staring down at a pocket Bible."
"He looks angry."
show sam annoyed talking with dis
m "\"{i}Now consider this, ye that forget God, lest I tear you in pieces, and there be none to deliver.{/i}\""
show sam annoyed -talking with dis1
show sam annoyed talking with dis
m "\"Psalm fifty. Twenty-one, twenty-two.\""
show sam annoyed -talking with dis
play sound ("sfx/bookclose.ogg")
"He shuts the pages between his paws with a crisp snap."
show tod talking with dis
stop sound
to "\"You just sounded like a genuine preacher man, Sam.\""
show tod with dis
show sam annoyed talking with dis
m "\"Well, I’m not.\""
show sam annoyed -talking with dis1
show sam annoyed talking with dis
m "\"I just thought it was an important thing to share.\""
show sam neutral -talking with dis
show tod talking with dis
to "\"I’ll admit I need to brush up on my Old Testament, but the way you said that made me feel I was sweating in the pews.\""
show tod with dis1
show tod talking with dis
to "\"You ever read any of the Book of Mormon?\""
show tod with dis
show sam eyes -talking with dis
show cli doubt at center,prisonday with dissolve
"Sam still looks a bit mad, and now Cliff looks uncomfortable."
wi "\"Well, I’ll leave this thrilling theological conversation to the both of you.\""
stop music fadeout 3.0
wi "\"...Bye!\""


if  CITYHALLNIGHT_Points > 0:
    scene echoroadnight with slow_dissolve
    $ BG_Light =1
else:
    scene echobackalley with dissolve
    $ BG_Light =0
play music "music/quiet.ogg" fadeout 4.0 fadein 5.0
"Sam sure is invested in the Bible."
"You’d think he sucked off enough men to be put off by all the bitching about adultery, but he keeps getting wrapped up in all the metaphysics."
"I know why he’s mad at Todd."
"Todd believes in a loving, affectionate God."
"Sam believes in a wrathful God."
"It’s like he wants there to be something real that he can be afraid of."
"Alright... I think that’s enough Church for me today."

if  CITYHALLNIGHT_Points > 0:
    scene bg townhallnight with dissolve
else:
    scene bg townhall with dissolve
"Downtown is always so wide open when I go there."
"The wind picks up between the tall buildings and makes the wooden shutters rattle."
"It’s the closest reminder of my city."

"Other than the bars after dark."

"Bars always have the same sticky smell, no matter where you are in the world."

"I expected to run into Judge Miller or the clerk Chrissy Smalls, or somebody filing for their liquor license."
if BG_Light == 0:
    show ree with dissolve
else:
    show ree at center,night with dissolve
"But what I see instead is Reed Morris."
play music "music/tension.ogg" fadeout 4.0 fadein 5.0
wi "\"You stop right there Reed!\""
show ree talking with dis
re "\"Oh God fucking DAMN it.\""
show ree with dis
wi "\"I have some questions for you.\""
show ree talking with dis
re "\"I don’t have time for your flea-bitten ass today.\""
show ree with dis
wi "\"That’s not how this works.\""
wi "\"Keep your hands where I can see them and don’t make a scene.\""
show ree talking with dis
re "\"Why? Am I under arrest for the fiftieth fucking time?\""
show ree with dis
wi "\"I guess it depends.\""

wi "\"It’ll be just like old times! We’re used to each other by now!\""
show ree talking with dis
re "\"You gonna feel me up like a fucking faggot and strip me of my rights again?\""
show ree with dis
wi "\"You’re the one who’s thinking that, not me.\""
show ree talking with dis
re "\"Go ruin somebody else’s day, you ugly son of a bitch.\""
show ree with dis
wi "\"Cut the shit.\""
wi "\"Did you break into Mr. Tibbits’ apartment last night or not?\""
show ree eyes with dis
"He looks guilty."
show ree talking with dis

re "\"There’s a whole lot more to it than that.\""
show ree with dis
wi "\"So you’re not even trying to lie about it?\""
show ree talking with dis
re "\"That fucking fruit did something to Huxley.\""
show ree with dis1
show ree talking with dis1
re "\"I goddamn KNOW that he did.\""
show ree with dis
wi "\"And what if he didn’t, Reed?\""

wi "\"You just went off and beat his door down like a goddamn lunatic?\""
show ree talking with dis

re "\"He started some shit, he got his ass beat, and he took revenge on my friend!\""
show ree with dis1
show ree talking with dis
re "\"And I’m sure as hell not gonna trust your shady ass to lift a finger over it, because you don’t even like me in the first place.\""
show ree with dis
wi "\"I need you to stop talking for a few minutes and start listening.\""
stop music fadeout 3.0
wi "\"Some kid tried to shoot up my office two nights ago using {i}Huxley’s{/i} pistol.\""
show ree talking with dis
play music "music/quiet.ogg" fadeout 4.0 fadein 5.0
re "\"His revolver?\""
show ree with dis1
show ree talking with dis
re "\"He pawned it. Anybody coulda bought it.\""
show ree with dis
wi "\"Not a fifteen year old without a job and no parents.\""

wi "\"Sales records indicate he bought it back.\""
if  CITYHALLDAY_Points > 0:
    $ unlocked_journal_pages += 3
$ current_journal_page = 7
$ renpy.notify("Notebook updated.")
$ huxley1 = "According to Reed, Huxley's gun was pawned. Sales records indicate Huxley repurchased it."
show ree eyes with dis
"Now he’s sweating."
show ree with dis

wi "\"That’s a hell of a lot of evidence that could implicate the two of you for attempted murder, damaging government property, and endangering the life of two officers.\""

wi "\"Hell, that’s more than enough to string you up!\""
show ree talking with dis

re "\"We didn’t do NONE of that.\""
show ree with dis
wi "\"I don’t think you did either you dumb asshole.\""
show ree eyes with dis1
show ree with dis1
show ree eyes with dis1
show ree with dis
"He blinks and looks confused."

wi "\"Breaking and entering is unacceptable, and you will pay for that crime in time.\""
wi "\"But just talk to me for a bit, and I'll have it so you won’t have to spend the rest of the day in jail.\""
show ree talking with dis

re "\"Okay. Shoot.\""
show ree with dis

wi "\"Why did he pawn the gun in the first place?\""
show ree talking with dis

re  "\"...He was having money troubles.\""
show ree with dis

wi "\"And why’s that?\""
show ree talking with dis

$ renpy.notify("Notebook updated.")
$ current_journal_page = 9
$ huxley3 = "Huxley was an alcoholic who needed more money for his drinking habit. I wonder where he was getting the cash?"
re "\"A man with troubles has gotta drink.\""
show ree with dis
wi "\"A little too much maybe?\""
show ree talking with dis

re "\"That’s rich, based on what I hear about you.\""
show ree with dis
wi "\"I can afford my drinks, Reed.\""
wi "\"What made him live beyond his means?\""
show ree talking with dis

re "\"He has problems.\""
show ree with dis
"Had problems, but I don’t think you can handle that yet."

wi "\"Yeah, I know. I saw what his {i}problems{/i} did to Marcy.\""
show ree talking with dis
re "\"What, you think she doesn’t like it that way, too?\""
show ree with dis

"His greasy fur bends into a slow, cracked smile and his eyes wrinkle."

"His moldy cotton smell reminds me of how my father smelled at his wake, and it makes me want to puke up bile."
show ree eyes talking with dis

re "\"...But now that I think about it, he was actin’... different, lately.\""
show ree with dis
wi "\"Different how?\""
show ree talking with dis

re "\"Longer hours at the bank.\""
show ree with dis1
show ree talking with dis

re "\"Sounded paranoid.\""
show ree with dis

wi "\"Of Mr. Tibbits?\""
show ree talking with dis

re "\"No, Tibbits just made him laugh.\""
show ree with dis1
show ree talking with dis
re "\"He wasn’t scared at all of that mouthy little fairy.\""
show ree eyes with dis
"Now something’s troubling him, like he’s starting to get it."
show ree talking with dis

re "\"He kept talking about buying back that pistol, like he was gonna need it to defend himself soon, but I thought he hadn’t yet.\""
show ree with dis
wi "\"And this was after you both had your quarrel with Mr. Tibbits?\""
show ree talking with dis
re "\"No, this was happening before.\""
show ree with dis
wi "\"So who would have had an eye on the gun?\""
show ree talking with dis
$ renpy.notify("Notebook updated.")
$ current_journal_page = 8
$ huxley2 = "Marcy may know what happened to the gun."

re "\"Marcy would know where he hid it. He always kept it close to her.\""
show ree with dis
"Of course he did."

wi "\"So maybe a chat with Marcy would have been a little smarter than tearing down Mr. Tibbits’ apartment then, huh?\""
show ree talking with dis
re "\"...May I go now?\""
show ree with dis
wi "\"Sure. But I don’t want to see you within 100 yards of that stoat or we’re gonna have ourselves a more punctual problem.\""
show ree talking with dis
re "\"I don’t give a damn if he didn’t take the gun.\""
show ree with dis1
show ree talking with dis
re "\"But if Marcy says that he did take it, I’ll kill him.\""
show ree with dis
wi "\"To ask somebody to shoot at him?\""
show ree eyes talking with dis
re "\"...Maybe.\""
show ree eyes with dis

wi "\"Brilliant. That would make a whole lot of sense.\""
show ree talking with dis
re "\"I’ll find out soon enough anyway.\""
show ree with dis
"He turns away and walks stiffly into the alley."
hide ree with dissolve
wi "\"Don’t think I won’t come looking for you later when it’s time to pay repair costs for that apartment!\""

"He flips me the bird."

"What a living waste of space if ever I saw one."

"But at least I know who to visit later."

"Marcy Greene might be the key to all of this after all, even if her husband played no part in trying to kill somebody."

"Maybe Huxley thinks he was acting paranoid when he bought back the gun."

"But considering his current state... it sounds like he was right to be afraid."

"But who’s strong enough to rip a head clean off of a body?"

"That’s just another question for later."

scene townhallinterior with dissolve

play music "music/byrneshouse.ogg" fadeout 4.0 fadein 5.0

"City Hall is predictably empty on a Monday."

"Most town meetings are on Saturdays, and that’s also when people tend to pick up their licenses."

"Chrissy isn’t at reception right now, but I’ve been through these halls so much I won’t need to wait for her."

show jam happy with dissolve

jam "\"Well goodness gracious, if it isn’t my favorite public servant.\""
show jam with dis
if CITYHALLDAY_Points > 0:
    $ current_journal_page = 10
    $ unlocked_journal_pages += 1
$ renpy.notify("Notebook updated.")
"So that’s why Franz called today."

wi "\"Shaking the mayor down for favors again?\""
show jam eyes with dis
jam "\"Well, what else is a mayor good for, anyway?\""
show jam talking with dis
jam "\"He’s very grateful to have more things to do.\""
show jam with dis
show jam eyes with dis
jam "\"Besides, baring fangs is more your line of work, is it not?\""
show jam with dis
wi "\"Only when I have to.\""
show jam happy with dis
jam "\"Of course, of course.\""
show jam talking with dis
jam "\"You’ve had ample time to practice burying your guilt.\""
show jam with dis
wi "\"I’m not talking to you because I want to make merry and exchange quips.\""

wi "\"I know something that could help you and I’m willing to trade information.\""
show jam happy with dis
jam "\"Well why didn’t you say so?!\""
show jam talking with dis
jam "\"And here I thought you were just talking to me to pout about the ex-wife.\""
show jam with dis
wi "\"Oh, we’ll be having a talk about that too.\""
show jam talking with dis
jam "\"Then why not move this conversation to the city library?\""
show jam with dis
show jam happy with dis
jam "\"It’s the perfect place for sharing information for men with noble character.\""
show jam with dis
wi "\"I still have to talk to the mayor.\""
show jam eyes with dis
"James rolls his eyes."
show jam talking with dis
jam "\"He’s always available.\""
show jam with dis
wi "\"And so are you?\""
show jam happy with dis
jam "\"Now there’s a private fantasy!\""
show jam talking with dis
jam "\"Since you have such a great sense of humor, I’ll make sure to dally at the library so that you can catch me there.\""
show jam eyes with dis
jam "\"Feel free to speak with the mayor first if you insist.\""
show jam talking with dis
jam "\"Until then, Sheriff.\""
show jam with dis
hide jam with dissolve
stop music fadeout 3.0
"I could follow up on James's offer."
play music "music/quiet.ogg" fadeout 4.0 fadein 5.0
"But then again, I’m already here."

menu williamchallmenu:
    "What should I do right now?"
    "Talk to the Mayor." if willchall1interview == False:
        "Let’s get this over with, then."

        scene mayoroffice with dissolve
        "I step into Testerman’s office."

        "The big rat is pecking away at his typewriter, but he stands up when he sees me."
        show fra sweat talking with dis
        fr "\"Well it’s about time, Adler!\""
        show fra sweat with dis
        wi "\"There were some road bumps on the way, but I’m here.\""
        show fra sweat talking with dis
        fr "\"Hendricks is threatening to cut all sorts of donation money if we don’t set this right, fast.\""
        show fra sweat with dis
        "I start laughing."
        show fra glare talking with dis
        fr "\"What in the Lord’s name is funny about that?\""
        show fra glare with dis
        wi "\"Let’s start with the essentials.\""
        wi "\"The mining operation continues to place blame on CGCS management for the death of this particular miner.\""
        wi "\"Tension is calm on the surface but resentment brews below.\""
        show fra with dis
        wi "\"Deputy Bronson found another dead body last night.\""
        show fra sweat with dis
        "His expression changes from one of anxiety to a look of sheer panic?"
        show fra sweat talking with dis
        fr "\"Another miner?!\""
        show fra sweat with dis
        wi "\"No.\""
        wi "\"This one’s a banker.\""
        show fra eyes with dis
        "I see relief wash over him."
        show fra talking with dis
        fr "\"So this wasn’t related to the other case, then?\""
        show fra with dis
        wi "\"A man is still dead, Mr. Testerman.\""
        show fra eyes with dis
        "He starts mumbling to himself."
        show fra eyes talking with dis
        fr "\"Well, sometimes it can’t be helped.\""
        show fra eyes with dis
        show fra eyes talking with dis
        fr "\"Men take all sorts of risks to make it out here, and not everybody can.\""
        show fra eyes with dis
        show fra eyes talking with dis
        fr "\"There are fights, and freak accidents, and hasty decisions accompanying immoral acts.\""
        show fra sweat with dis
        wi "\"His head was ripped off.\""
        show fra sweat talking with dis
        fr "\"Oh. So probably an animal.\""
        show fra with dis
        wi "\"Could be.\""
        show fra talking with dis
        fr "\"Now I feel a lot better.\""
        show fra with dis
        wi "\"Are you sure that you should?\""
        wi "\"I didn’t say that this was an animal for certain.\""
        show fra sweat talking with dis
        fr "\"Do any of your discoveries call for a state of emergency evacuation?\""
        show fra sweat with dis
        wi "\"I wouldn’t say so.\""
        wi "\"Unless this death isn’t an isolated incident.\""
        wi "\"I have reasonable suspicion to think that it could be linked to a targeted attack on one of the CGCS employees.\""
        show fra glare talking with dis
        fr "\"But you just have suspicions.\""
        show fra glare with dis
        show fra glare talking with dis
        fr "\"Not proof.\""
        show fra glare with dis
        show fra glare talking with dis
        fr "\"That’s what you said, right?\""
        show fra glare with dis
        wi "\"That would be right.\""
        wi "\"But odds are--\""
        show fra sweat talking with dis
        fr "\"I think it would be kind not to sensationalize a tragedy.\""
        show fra sweat with dis
        "He looks into my eyes as if he’s looking for approval for what he’s about to say."
        show fra sweat talking with dis
        fr "\"Wouldn’t it?\""
        show fra sweat with dis
        wi "\"I think that should always be a priority.\""
        wi "\"But what I’m telling you is that whatever this is, it probably ain't over, and it probably ain't isolated from CGCS affairs.\""
        wi "\"So you might want to prepare a statement ahead of time if things go to hell in a handbasket and you don’t want to be caught with your britches down.\""
        show fra talking with dis
        fr "\"I think I would prefer to be optimistic about the future Mr. Adler.\""
        show fra with dis
        show fra talking with dis
        fr "\"Just keep me informed about the present, please?\""
        show fra with dis
        wi "\"Okay then!\""
        wi "\"There are presently some signs of very clear scandals at that company that will make their way to the surface soon.\""
        show fra glare talking with dis
        fr "\"That {i}company{/i} is our town’s life-blood, Adler!\""
        show fra glare with dis
        wi "\"Well, that’s fine, but ignoring it won’t make it all go away.\""
        show fra glare talking with dis
        fr "\"But isn’t it your job to prevent a state of panic?\""
        show fra glare with dis
        wi "\"I’m saying that if all these problems go back to CGCS management, then the panic is just going to keep coming back like clockwork.\""
        show fra eyes talking with dis
        fr "\"But you still need proof before you can bandy about these claims.\""
        show fra eyes with dis
        "I swear to God this man is as thick as pig shit."
        show fra glare with dis
        wi "\"I didn’t make claims.\""
        wi "\"I shared suspicions.\""
        show fra sweat with dis
        wi "\"Let me make something very clear to you, Franz Testerman.\""
        wi "\"I don’t work for you.\""
        wi "\"But if you ask me for help and aren’t willing to take it, there’s not much I can do for you.\""
        wi "\"I do think this could lead to a public crisis.\""
        wi "\"So I think you should prepare for that.\""
        show fra glare talking with dis
        fr "\"And I’ll tell {i}you{/i} something, Mr. Adler!\""
        show fra glare with dis
        show fra glare talking with dis
        fr "\"I will say it once, I will say it a hundred times over.\""
        show fra glare with dis
        show fra glare talking with dis
        fr "\"I must see the evidence before I am swayed to act!\""
        show fra glare with dis
        show fra glare talking with dis
        fr "\"Why is that so hard for you to accept?\""
        show fra glare with dis
        "The more I look into this man’s eyes, the more I know he has no interest in evidence."
        "He’ll see what he wants to see when he needs it to be true."
        wi "\"Do you already have a contingency plan in place for evacuating a population of over six thousand, then?\""
        show fra eyes with dis
        fr "\"There’s precedents in place if such a need arrives.\""
        show fra sweat with dis
        wi "\"And you’ve practiced them?\""
        show fra sweat talking with dis
        fr "\"Once again, I will not disrupt daily routines on the basis of an assertion!\""
        show fra sweat with dis
        "Alright, this is going nowhere."
        wi "\"Then let’s conclude this meeting.\""
        "I turn around and put my hand on the knob."
        show fra sweat talking with vpunch
        fr "\"Wait...\""
        show fra sweat with dis
        wi "\"Yes?\""
        show fra sweat talking with dis
        fr "\"Do you really think things are that bad?\""
        show fra sweat with dis
        wi "\"Yes.\""
        show fra sweat with dis
        "He wipes his brow with a kerchief."
        show fra eyes talking with dis
        fr "\"I could... review the evacuation plans.\""
        show fra sweat with dis
        show fra sweat talking with dis
        fr "\"But quietly, and without getting the public involved.\""
        show fra sweat with dis
        show fra sweat talking with dis
        fr "\"But just as a backup plan! I still have no intention of officiating an evacuation.\""
        show fra eyes with dis
        "That’s what I’ve been saying, Testerman."

        wi "\"That’s better than nothing.\""
        wi "\"I have to go now.\""
        show fra talking with dis
        fr "\"...You’ll keep me updated, then?\""
        show fra sweat with dis
        wi "\"I’ll call if it’s important.\""
        hide fra with dissolve
        "What a headache."
        $ willchall1interview = True
        jump williamchallmenu
    "Talk to James." if willchall2interview == False:
        "Information shared among noble souls?"
        "And here I thought we were a couple of bastards."
        if  CITYHALLNIGHT_Points > 0:
            scene bg townhallnight with dissolve
        else:
            scene bg townhall with dissolve
        "At least I can understand that."
        "Pitiful."
        if  CITYHALLNIGHT_Points > 0:
            scene echolibraryinteriornight with dissolve
        else:
            scene echolibraryinteriorday with dissolve

        "The library is big, but it’s pretty underutilized."
        "Because, well, let’s face it... not a whole lot of people here like to read."
        "Which I don’t entirely get, considering how little there is to do."
        if BG_Light == 0:
            show jam eyes at center,sunset with dissolve
        else:
            show jam eyes at center,night with dissolve
        "It doesn’t take me long to find him."
        "He’s reading a newer book by the looks of it."
        #Elihere
        "{i}Dubliners{/i}, by James Joyce."
        "His bodyguards are sitting in a corner, flipping through magazines."
        wi "\"Let’s keep this quick.\""
        show jam talking with dis
        jam "\"Don’t act so suburban, Mr. Adler, there’s a treasure trove of knowledge all around you.\""
        show jam eyes with dis1
        show jam talking with dis
        jam "\"Enjoy yourself.\""
        show jam with dis
        wi "\"Not interested.\""
        wi "\"You really did bring Hattie here.\""
        wi "\"Why?\""
        show jam happy with dis
        jam "\"My, my. You’re so accusatory.\""
        wi "\"That’s because I’m accusing you of something.\""
        show jam talking with dis
        jam "\"You’re wrong to, you know.\""
        show jam with dis
        "He flips a page to the beginning of another short story."
        "{i}Araby{/i}."
        show jam talking with dis
        jam "\"She’s the one who reached out to me, not the other way around.\""
        show jam eyes with dis

        jam "\"I only did for her what I did for you.\""
        show jam talking with dis
        jam "\"She just needed some money to stay on her feet to orient herself in someplace new.\""
        show jam with dis
        wi "\"How generous of you.\""
        show jam happy with dis
        jam "\"I am generous.\""
        wi "\"When it’s inconvenient for me. Sure.\""
        show jam with dis

        wi "\"Why’d you tell her where I live?\""
        show jam talking with dis
        jam "\"Now {i}that{/i} I can’t talk about.\""
        show jam with dis

        wi "\"Did your generosity suddenly run dry?\""
        show jam eyes with dis

        jam "\"No. I mean I simply don’t know.\""
        wi "\"Horse shit.\""
        show jam happy with dis

        jam "\"Why would I need to lie?\""
        show jam talking with dis
        jam "\"I genuinely don’t know, and that’s going to put you in the most amusing little tizzy.\""
        show jam eyes with dis
        jam "\"But how about granting me some of {i}your{/i} generosity now?\""
        show jam talking with dis
        jam "\"Share.\""
        show jam with dis
        wi "\"I guess you’ll have to ask yourself why somebody would try to assassinate one of your business associates.\""
        "He lifts an eyebrow."
        show jam talking with dis
        jam "\"Which?\""
        show jam with dis
        wi "\"Little fella who goes by the name Clifford Tibbits.\""
        show jam eyes with dis

        "He hums."
        show jam talking with dis

        jam "\"Well that’s no good at all.\""
        show jam with dis1
        show jam talking with dis

        jam "\"He’s such a card... and much more fun than you.\""
        show jam with dis1
        show jam talking with dis
        jam "\"What kind of cad would put their hands on such a delightful boy?\""
        show jam with dis1
        show jam talking with dis
        jam "\"I’ll have to keep a much closer eye on him from now on.\""
        show jam with dis
        wi "\"I could help you with that.\""
        show jam eyes with dis
        jam "\"Your stalwart sense of justice really is invigorating.\""
        show jam happy with dis
        jam "\"I always knew deep down that you liked me.\""
        show jam eyes with dis
        "It takes a lot of willpower not to rip that book out of his hands and beat him with it."
        wi "\"So help me understand.\""
        show jam talking with dis
        jam "\"Well, let’s see.\""
        show jam with dis1
        show jam talking with dis
        jam "\"As is typical of your older workhorses, too many of them tend to keep very old-fashioned ideas.\""
        show jam with dis1
        show jam talking with dis
        jam "\"They might not approve of a foreigner in a higher ranking consultation position.\""
        show jam with dis1
        show jam talking with dis
        jam "\"Particularly the men closest to my most important business partner, Mr. Briggs.\""
        show jam with dis
        wi "\"And do you have the names of these men?\""
        show jam eyes with dis

        jam "\"Not really.\""
        show jam with dis1
        show jam talking with dis
        jam "\"There’s simply too many, and they’re all very closed-minded.\""
        show jam with dis1
        show jam talking with dis
        jam "\"But it shouldn’t be too complicated to pick them out of a crowd.\""
        show jam with dis1
        show jam talking with dis
        jam "\"They tend to smell like raw earth, after all.\""
        show jam with dis
        "He snaps his book shut."
        show jam eyes with dis
        if CITYHALLDAY_Points > 0:
            $ current_journal_page = 11
            $ unlocked_journal_pages += 1
            $ renpy.notify("Notebook updated.")
        jam "\"If it wasn’t one of them, then I’m out of ideas.\""
        show jam talking with dis

        jam "\"Then again, that one does have a bleeding heart.\""
        show jam with dis1
        show jam talking with dis
        jam "\"I wouldn’t be surprised if he spilled his guts out to some savage and they took it the wrong way.\""
        show jam eyes with dis
        wi "\"You stop speaking.\""
        show jam with dis
        wi "\"Now.\""
        show jam eyes with dis
        jam "\"Oh don’t be so sensitive, Adler.\""
        show jam with dis1
        show jam talking with dis
        jam "\"I’m not a monster.\""
        show jam with dis1
        show jam talking with dis
        jam "\"And I don’t begrudge you for the primal blood on your mother’s side.\""
        show jam happy with dis
        jam "\"In fact, I think you’re the best of two worlds.\""
        show jam eyes with dis
        jam "\"The raw and the refined.\""
        "I see a pebble on the table."
        "I pick it up, then flick it at his cheek."
        show jam talking with dis
        jam "\"Oh, what the fuck?\""
        show jam neutral with dis1
        show jam talking with dis
        jam "\"Am I bleeding?!\""
        show jam neutral with dis
        "Oh damn."
        "He is."
        "Hope it stings, you son of a bitch."
        #elihere
        "His guards rush over but he puts up his hand to make them stop."
        show jam happy with dis
        "He smiles real big at me."
        show jam talking with dis
        jam "\"And that’s exactly what I’m talking about!\""
        show jam happy with dis
        "He waves at me with his bloody hand."
        show jam talking with dis
        jam "\"Until next time.\""
        show jam happy with dis
        wi "\"Always an affable time.\""
        hide jam with dissolve
        "It doesn’t take too long for James and his men to clear out of the library."
        $ renpy.notify("Notebook updated.")
        $ current_journal_page = 10
        $ jamestext = "Made James bleed. Was funny."
        $ jamesimage = "wn8"
        "I never much cared for Joyce."

        if  CITYHALLNIGHT_Points > 0:
            $ PORINT_Points +=1
            "I hear somebody else stir behind the library stacks."
            wi "\"Who’s there?\""
            wi "\"Come on out and show yourself.\""
            show por talking at center,night with dissolve
            pounk "\"It’s only me.\""
            show por with dis
            "I hear a thin, cheery voice."
            wi "\"Who the hell’s me?\""
            show por eyes talking with dis
            pounk "\"The librarian.\""
            show por eyes with dis
            "Oh."
            show por with dis
            "That makes sense."
            "Now I feel silly."
            wi "\"My apologies. I didn’t think I’d hear anybody there.\""
            show por talking with dis
            po "\"Porter Moore.\""
            show por eyes with dis
            po "\"But don’t bother apologizing.\""
            show por talking with dis
            po "\"After all, I did happen to hear a good chunk of your conversation.\""
            show por with dis
            wi "\"Fair game in a public library.\""
            wi "\"We are supposed to be quiet in them, after all.\""
            show por eyes with dis
            po "\"I’m afraid I must insist!\""
            show por talking with dis
            po "\"You are looking for reliable information, aren’t you?\""
            show por with dis
            wi "\"Well, what would you know?\""
            show por talking  with dis
            po "\"I know that you collect information from the prostitutes at the Hip in exchange for a loose adherence to the law.\""
            show por with dis1
            show por talking with dis
            po "\"But other than that, not much about you, I’m afraid.\""
            show por with dis
            wi "\"Alright, who the hell are you?\""
            show por talking with dis
            po "\"I already told you.\""
            show por with dis1
            show por talking with dis
            po "\"I’m just a librarian.\""
            show por with dis1
            show por talking with dis
            po "\"You’d trade information with the co-owner of CGCS but not with me?\""
            show por with dis1
            show por talking with dis
            po "\"Now that feels unfair.\""
            show por with dis1
            show por talking with dis
            po "\"At least allow me to give you something free as a token of good will...\""
            show por with dis
            wi "\"Alright then.\""
            wi "\"What do you got?\""
            show por smug talking with dis
            po "\"James has a voracious sexual appetite.\""
            show por with dis1
            show por talking with dis
            po "\"You’ll find that he sleeps with many of the workers at the Hip to satisfy his curiosities.\""
            show por with dis1
            show por talking with dis
            po "\"One of them is loyal to him now, and will tell you nothing useful.\""
            show por with dis1
            show por talking with dis
            po "\"They will be an active hindrance to you.\""
            show por with dis1
            show por smug talking with dis
            po "\"Would you like to know their name?\""
            show por smug with dis
            wi "\"Sure. Why not?\""
            show por talking with dis
            po "\"Now that’ll cost you something.\""
            show por with dis
            wi "\"Oh, does it now?\""
            show por talking with dis
            po "\"You can pay me money, or you can pay me in information.\""
            show por with dis
            wi "\"How much?\""
            show por talking with dis
            po "\"Fifty dollars.\""
            show por with dis
            wi "\"I think I see.\""
            show por talking with dis
            po "\"Is the price too high?\""
            show por with dis
            wi "\"Not necessarily.\""
            show por surprised with dis
            wi "\"But I understand what diminishing returns are.\""
            wi "\"My secrets are more valuable when I’m the source.\""
            wi "\"And that will go farther than putting it up in your information market.\""
            show por smug talking with dis
            po "\"Well done.\""
            show por smug with dis1
            show por serious talking with dis
            po "\"Just don’t compete with me or you might regret it.\""
            show por serious with dis
            wi "\"I assure you. We’re in different businesses.\""
            show por with dis1
            hide por with dis3
            $ renpy.notify("Notebook updated.")
            $ current_journal_page = 6
            $ chnighttext = "Apparently, at least one person who works at the hip is leaking information to James."
            "He flashes me a smile and walks away."
        else:
            "Where's Baroness Orczy when you need her?"
        "So there are people who'd have a motive to hurt Mr. Tibbits."
        $ willchall2interview = True
        jump williamchallmenu




label endofwillchallinterviews1:
"I think I’ve learned all that I can."
"That’s just about enough of this place for now."

if CITYHALLNIGHT_Points > 0:
    "Time to go."
    scene black with fade
    jump hipinvestigation
else:
    scene black with fade
    jump samstation

label stagday:
$ STAGDAY_Points +=1
label stagnight:
wi "\"Todd! Watch over the station while I head to The Stag.\""
show tod surprised at right,prisonday with dis
to "\"Oh!\""
show tod talking with dis
to "\"So are ya finally gonna learn how to dance, Sheriff?\""
show tod with dis
wi "\"This isn’t for fun, Todd. I’m going to scope the place out and ask some questions.\""
wi "\"And I already know how to dance.\""
show tod eyes happy with dis
to "\"I guess I shouldn’t be surprised. You do know an awful lot.\""
show tod with dis
show sam smile at left,prisonday with dissolve:
    xzoom -1
m "\"Why don’t you show him how, Sheriff?\""
show sam neutral talking at left,prisonday with dis:
    xzoom -1
m "\"He seems eager.\""
show sam smile at left,prisonday with dis:
    xzoom -1
"Oh shut the hell up Sam."
show sam surprised -talking at left,prisonday:
    xzoom -1
show tod surprised
show cli eyes talking at center,prisonday

cl "\"I’ve been told I can be very eager.\"" with vpunch
show cli happy with dis
show sam surprised -talking with dis
show tod surprised with dis
cl "\"Numerous times.\""
show sam neutral talking  at left,prisonday with dis:
    xzoom -1
m "\"Nah. This is something I think the Sheriff should do.\""
show sam smile  at left,prisonday with dis:
    xzoom -1
"Smarmy shit."
wi "\"You’re the expert on moving your legs. You do it.\""
show tod talking with dis
to "\"Sam’s a dancer?\""
show tod with dis
show sam eyes talking  at left,prisonday with dis:
    xzoom -1
m "\"Uh... no?\""
show sam eyes -talking at left,prisonday:
    xzoom -1
show cli talking with dis
cl "\"Oh, nonsense. Everybody’s a dancer when they find the right rhythm.\""
show cli with dis
show cli happy with dissolve
cl "\"Now let’s find some music or make some ourselves.\""
show sam surprised -talking at left,prisonday with dis:
    xzoom -1
wi "\"Have fun, Sam!\""
stop music fadeout 3.0



if  STAGNIGHT_Points > 0:
    scene echoroadnight with slow_dissolve

else:
    scene echobackalley with slow_dissolve
"I guess it’s time to finally make my way to this club."
play music "music/quiet.ogg" fadeout 4.0 fadein 5.0
"I know the directions, roughly."

"Which means I’m gonna be walking for a while."

if  STAGNIGHT_Points > 0:
    scene stagtrailnight with slow_dissolve

else:
    scene mineroad with slow_dissolve

"For one of the busiest places in town, it sure is out of the goddamn way of everything."

"Though, considering the kinds of things that go down there, I suppose that’s part of the point."

if  STAGNIGHT_Points > 0:
    scene stagexteriornight with slow_dissolve
else:
    scene stag with slow_dissolve

"It looks like a massive barn."

"But it doesn’t smell like one."

"I know what a barn smells like."

"The wide double doors are held open by a big rock, so it doesn’t look like this place is closed often."

if  STAGNIGHT_Points > 0:
    "There’s a big figure in the distance lumbering toward me."
    wi "\"That you, Nik?\""
    show nik neutral flaccid hoff at center,night with dissolve
    show nik talking with dis
    ni "\"If you wanted to go for a drink we should have invited all the others.\""
    show nik neutral flaccid hoff with dis1
    show nik talking with dis
    ni "\"I am sure they would love to see how drunk I could get you.\""
    show nik smile with dis
    wi "\"The last thing I want is a scene here.\""
    wi "\"Could you help me fit in?\""
    wi "\"Maybe get cozy with some of the regulars?\""
    show nik talking with dis
    ni "\"Well do not wear the badge obviously.\""
    show nik neutral flaccid hoff with dis
    wi "\"I already took it off Nik.\""
    show nik disappointed with dis3
    ni "\"Pah! It is dark.\""
    show nik talking with dis3
    ni "\"Just put in an effort to have a good time and people will talk without asking.\""
    show nik smile with dis
    wi "\"I’m on a time crunch, Nik.\""
    wi "\"There are other places I still have to be.\""
    show nik disappointed with dis3
    ni "\"Very well, very well.\""
    show nik neutral flaccid hoff with dis3
    "He beckons toward the front door."
    show nik sidelook with dis3
    ni "\"Shall we, then?\""
    stop music fadeout 3.0
    "I nod and sigh."
    play music "music/stag1.ogg" fadeout 4.0 fadein 5.0
    wi "\"After you.\""
else:
    "I hope this is worth it."

if  STAGNIGHT_Points > 0:
    scene stagnight with dissolve
    $ BG_Light =1
else:
    scene stag with dissolve
    $ BG_Light =0


if STAGNIGHT_Points > 0:
    "It’s packed so dense I can hardly move."
else:
    "There’s barely a crowd right now."
    $ current_journal_page = 5
    $ unlocked_journal_pages += 5
    $ renpy.notify("Notebook updated.")
menu williamstagmenu:
    "Where should I look right now?"
    "Check the upper beams" if willstag1interview == False:
        if  STAGNIGHT_Points > 0:
            scene stagloftnight with dissolve
            $ BG_Light =1
        else:
            scene stagloft with dissolve
            $ BG_Light =0
        if willstag1interview2 == False and STAGNIGHT_Points > 0:
            show nik at center,light1 with dissolve
            show nik talking at center,light1 with dis
            ni "\"Move to the ladder and we can escape the crowd.\""
            show nik neutral flaccid hoff with dis1
            show nik talking with dis
            ni "\"I know some people we could talk to.\""
            show nik neutral flaccid hoff with dis1
            hide nik with dissolve
        else:
            "There's got to be somebody useful to talk to nearby."
        if willstag1interview2 == False:
            "It might be easier to scope out the place if I look from a higher position."
            "Might as well climb up the ladder and see what I’ve got to work with."
        else:
            "God it's getting stuffy up here."

        label loftjump:

        if willstag1interview2 == False:
            "There’s a severe looking fellow in eastern clothing sitting by the rails by himself."
            "He looks like a sable."
        else:
            "Now then..."

        if willstag1interview2 == False and STAGNIGHT_Points > 0:
            wi "\"Say, Nik...\""
            wi "\"Do you know any folks in these parts who’d be comfortable to share what they know with me?\""
            wi "\"Maybe somebody a little less cagey.\""
            show nik happy at center,light1 with dissolve
            ni "\"This is a spirited place, Will. Especially after a few drinks.\""
            show nik smile with dissolve
            ni "\"But I know some good union men who will share what they know if they believe in the cause.\""
            show nik talking with dis
            ni "\"Over there, for example.\""
            show nik neutral -talking with dis1
            show nik talking with vpunch
            ni "\"Oiy!\""
            show nik neutral flaccid hoff with dis1
            hide nik with dissolve
        else:
            jump willstagmenu2


        menu willstagmenu2:
            "Who should I approach?"
            "Talk to the sable." if willstag1interview2 == False:
                $ willstag1interview2 = True
                if BG_Light == 0:
                    show cha at center,dark4 with dissolve
                elif BG_Light == 1:
                    show cha at center,light1 with dissolve
                else:
                    show cha at center,stagback with dissolve
                "He might think that he was minding his business, but I caught him staring multiple times."
                "Which either means he’s curious about me or he wants me to leave."
                "Let’s find out which."
                wi "\"Mind if I take a seat?\""
                show cha eyes with dis
                "He dabs his pen in the ink again, and keeps writing."
                show cha talking with dis
                unkch "\"If you insist, though I will be involved in my work.\""
                show cha with dis
                wi "\"What sort of work?\""
                show cha talking with dis
                unkch "\"Translation.\""
                show cha with dis
                wi "\"You kept giving me looks, so you know who I am, don’t you?\""
                show cha talking with dis
                unkch "\"Difficult not to.\""
                show cha smile with dis
                wi "\"Well I promise I’m not here to give you a hard time.\""
                wi "\"I just hoped that the good people here could help me understand a little more about James Hendricks and his relationship with his employees.\""
                wi "\"I have reason to believe that somebody might be trying to hurt his employees, and some folks are already hurt.\""
                show cha eyes talking with dis
                unkch "\"I no longer work there, so I would not know.\""
                show cha eyes with dis
                wi "\"But do you know anything that might support the claim that Mr. Hendricks is putting his own employees in danger?\""
                "The sable looks like he’s thinking."
                show cha talking with dis
                unkch "\"I can tell you something general.\""
                show cha with dis
                wi "\"Anything helps.\""
                show cha talking with dis
                unkch "\"Mr. Hendricks, very blatantly, has favored employees.\""
                show cha with dis1
                show cha talking with dis
                unkch "\"However, so does Mr. Briggs.\""
                show cha with dis1
                show cha talking with dis
                $ renpy.notify("Notebook updated.")
                $ current_journal_page = 11
                $ changtext = "{s}Could a CGCS employee have placed a hit on Cliff, or was it somebody else?{/s} Seems like the CGCS employees loyal to the company don't even get along. Some favor James. Some favor Briggs."
                unkch "\"There was very little overlap in those two groups, and it traditionally bred resentment.\""
                show cha with dis1
                show cha talking with dis
                unkch "\"But that’s all I can tell you.\""
                show cha with dis
                wi "\"Thanks. You’ve been very helpful. Mr... what was your name again?\""
                show cha talking with dis
                chji "\"Call me Ji Ba.\""
                show cha with dis
                "I try to pronounce it, but it’s a bit of a mouthful."
                wi "\"Thank you, Mr. Ji Ba.\""
                show cha smile with dis
                chji "\"Oh, call for me any time.\""
                hide cha with dissolve
                "Strange fella."
                if willstag1interview2 == True and willstag2interview2 == True:
                    $ willstag1interview = True
                    jump williamstagmenu
                else:
                    "Shame about his hand."
                    $ willstag1interview = True
                    if STAGNIGHT_Points > 0:
                        jump willstagmenu2
                    else:
                        jump williamstagmenu
                if STAGNIGHT_Points > 0:
                    jump williamstagmenu
                else:
                    $ willstag1interview = True
                jump willstagmenu2
            "Talk to the miners." if willstag2interview2 == False and STAGNIGHT_Points > 0:
                play music "music/stag2.ogg" fadeout 4.0 fadein 5.0
                scene stagloftbacknight with dissolve
                $ BG_Light =2
                $ MININT_Points +=1
                show nik neutral flaccid hoff at center,stagback with dissolve
                "Nik keeps nudging me towards a round table where a few men are talking."
                show nik talking with dis
                ni "\"Dimitri, Paul, Felipe.\""
                show nik neutral flaccid hoff with dis1
                hide nik with dissolve
                show dim coat at center,stagback
                show pau at left,stagback:
                    xzoom -1
                show fel at right,stagback
                with dissolve
                "He points to the bear, the wolverine, and the jackrabbit respectively."
                ni "\"Say hello to Sheriff Adler.\""
                show pau angry talking with dis
                pa "\"Sheriff, you say?\""
                show pau angry with dis
                show dim coat smile talking with dis
                di "\"We’d be happy to speak with him.\""
                show dim coat smile
                show fel talking
                with dis
                fe "\"Would we?\""
                show fel with dis
                ni "\"He is working on more than a few dangerous cases.\""
                show pau angry talking with dis
                pa "\"So what?\""
                show pau angry with dis
                ni "\"One of the men involved shot at me.\""
                show pau surprised with dis
                pa "\"Oh.\""
                show pau eyes smile with dis
                pa "\"Well that changes things.\""
                show pau talking with dis
                pa "\"You hurt?\""
                show pau with dis
                ni "\"Not yet, thankfully, but for how long?\""
                ni "\"Who can say...\""
                show pau eyes smile talking with dis
                pa "\"Just tell us what you need already, damn it...\""
                show pau eyes smile
                show dim coat smile talking
                with dis
                di "\"I’m glad you changed your tune Paul.\""
                show dim coat smile with dis1
                show dim coat talking with dis
                di "\"Now what might we help you with?\""
                show dim coat with dis
                wi "\"I know it’s not exactly a secret that your folks aren’t happy with the management at CGCS.\""
                show pau angry talking with dis
                pa "\"I don’t give a damn about the management, I just want more pay.\""
                show pau angry with dis
                show fel talking with dis
                fe "\"The management could also be better.\""
                show fel
                show dim coat eyes smile talking
                with dis
                di "\"Our chapter isn’t exactly united on every front, but frustrations are certainly at an all time high.\""
                show dim coat eyes with dis
                wi "\"Know anybody frustrated enough to assassinate one of James’s higher ranking employees?\""
                show pau talking with dis
                pa "\"If you’re here to sniff around for information about James, the Stag won’t do you much good.\""
                show pau with dis1
                show pau talking with dis
                pa "\"The Hip is more his speed.\""
                show pau with dis
                wi "\"In what way?\""
                show pau eyes smile talking with dis
                pa "\"The carnal way.\""
                show pau eyes smile with dis
                wi "\"Noted.\""
                show pau eyes smile talking with dis
                pa "\"I hear that man gets stuck in women more times than Taft got stuck in the presidential bathtub...\""
                show pau eyes smile with dis
                "Is he trying to make me vomit?"
                wi "\"That paints a picture alright.\""
                wi "\"Anything else you can tell me?\""
                show dim coat talking with dis
                di "\"I think he doesn’t seem to like the barkeep much?\""
                show dim coat with dis1
                show dim coat talking with dis
                $ renpy.notify("Notebook updated.")
                $ current_journal_page = 6
                $ stagnighttext = "Harlan gets into fights with James? He usually keeps things professional."
                di "\"Sounded like he gets in fights with him enough.\""
                show dim coat with dis
                show pau talking with dis
                pa "\"Not enough to get him banned from the establishment, apparently.\""
                show pau with dis
                show fel eyes talking with dis
                fe "\"Well we all know what he’s like.\""
                show fel eyes with dis
                "You’re a life-saver, Nik."
                wi "\"I think I might have enough here gentlemen.\""
                wi "\"It’s been a pleasure.\""
                show dim coat talking with dis
                di "\"Why don’t you stay for a little while longer?\""
                show dim coat with dis1
                show dim coat smile talking with dis
                di "\"I’m sure we have other mutual interests we could discuss other than James three.\""
                show dim coat with dis
                wi "\"I'm on a time crunch, I’m afraid, but I think that’s not a bad idea once this case is under control.\""
                show dim coat smile talking with dis
                di "\"I’ll hold you to that.\""
                show dim coat smile with dis
                wi "\"People usually do.\""
                hide fel
                hide pau
                hide dim
                with dissolve
                "There’s a bar and a dance floor downstairs."
                "There could be somebody down there with loose lips from all the alcohol."
                if willstag1interview2 == True:
                    $ willstag1interview = True
                    $ willstag2interview2 = True
                    jump williamstagmenu
                else:
                    $ willstag2interview2 = True
                    jump willstagmenu2
        label endofwillstaginterviews2:
    "Check out the bar." if willstag3interview == False:
        if  STAGNIGHT_Points > 0:
            scene stagnight with dissolve
            $ BG_Light =1
        else:
            scene stag with dissolve
            $ BG_Light =0

        "I see an opening to fit into the bar, so I sit on one of the bar stools right now so I don’t miss my chance."
        if BG_Light == 0:
            show tre smile br w at center,stagday with dis3
        else:
            show tre smile br w at center,light1 with dis3
        "The bartender strolls over slowly."
        show tre talking with dis
        bartre "\"What will it be?\""
        if STAGNIGHT_Points > 0:
            show tre -talking with dis
        else:
            show tre -talking -smile with dis
        wi "\"Just a scotch on the rocks.\""
        if STAGNIGHT_Points > 0:
            show tre eyes talking with dis
            bartre "\"Comin’ right up...\""
            show tre -talking -eyes -smile with dis
        else:
            show tre eyes talking with dis
            bartre "\"Ain't it a bit early for that?\""
            show tre -talking with dis
            wi "\"You want me to just order a water instead?\""
            show tre -eyes with dis

        "The barkeep turns his head towards me and squints at me."
        show tre surprised talking with dis
        bartre "\"Hey, I know you.\""
        show tre -talking with dis
        "Oh boy. Here comes trouble."
        show tre -surprised talking with dis
        bartre "\"You’re Sheriff Adler.\""
        show tre -talking with dis
        "I hear some adjustments in the seats next to me."
        wi "\"Right now I’m just thirsty, thanks.\""
        show tre talking with dis
        bartre "\"How come you’re not wearing your badge?\""
        show tre -talking with dis
        wi "\"Because I don’t tend to need it for folks to know who I am.\""
        wi "\"And I’m on a case.\""
        wi "\"Are you saying you have time to talk with me?\""
        show tre eyes talking with dis
        bartre "\"Your drink will be right up.\""
        show tre -talking with dis
        "He hurries away and{nw}"
        hide tre with dis3
        extend " I can feel the breath leaving my lungs."
        "That’s what I thought."
        "That was a scene that didn’t need to be one."
        "Some folks clear the seats beside me."
        "A big Sonoran wolf stares at me through the space they leave behind."
        if BG_Light == 0:
            show kan smile at center,stagday with dissolve
        else:
            show kan smile at center,light1 with dissolve
        "He stands up, saunters over with a bit of a swagger, then takes the seat next to me."
        show kan eyes smug with dis
        kaunk  "\"Bit hard out there for a law man, ain't it?\""
        wi "\"Hard out there for most people.\""
        wi "\"Patronizing me won’t get you far.\""
        show kan smug with dis
        kaunk  "\"Easy there, tough guy.\""
        show kan smug talking with dis
        kaunk  "\"Who says I’m looking to get anywhere?\""
        show kan sneer with dis
        "He leans in and strokes the edge of his  beer glass with an index finger."
        wi "\"Your posture. Your tone. Your gaze.\""
        wi "\"You like to play games.\""
        show kan eyes smug with dis
        kaunk  "\"What’s so wrong with a game or two?\""
        show kan talking with dis
        ka "\"Kane’s the name.\""
        show kan smile with dis
        "I feel a groan rumble out of my throat."
        wi "\"That don’t even rhyme.\""
        show kan sneer with dis
        ka "\"You callin’ me a poet?\""
        show kan sneer talking with dis
        ka "\"Careful now. I could take offense to that.\""
        show kan sneer with dis
        "I sip a little deeper and don’t mind the burn."
        wi "\"If you want to waste your own time, go ahead, but there’s not a whole lot of scotch in this glass.\""
        show kan eyes talking with dis
        ka "\"Truth be told, I just like to think your scars are interesting.\""
        show kan eyes smug with dis
        wi "\"Be careful about what you call interesting.\""
        show kan smug with dis
        ka "\"Can I know how you got ‘em?\""
        wi "\"The swipe to the face was me getting too close to a thug after knocking a gun out of his hand.\""
        wi "\"Sliced me to ribbons.\""
        show kan smug talking with dis
        ka "\"And what about the chunk out of your ear?\""
        show kan smile with dis
        wi "\"That was just a bit of good old-fashioned torture.\""
        show kan talking with dis
        ka "\"You say that pretty casual-like.\""
        show kan with dis
        wi "\"I was trained for it.\""
        show kan sneer talking with dis
        ka "\"It’s good that you know how to bounce back.\""
        show kan sneer with dis
        wi "\"Most men don’t get far if they don’t.\""
        show kan smug with dis
        ka "\"Too true.\""
        show kan smug talking with dis
        ka "\"Say, do you like to brawl, Sheriff?\""
        show kan smile with dis
        wi "\"Why, you want to find out?\""
        show kan sneer talking with dis
        ka "\"Would you fight me if I gave you a kiss?\""
        show kan sneer with dis
        wi "\"That’s real cute.\""

        ka "\"Who’s joking?\""
        show kan wink with dis1
        show kan smile with dis
        "The hell is with this guy?"
        wi "\"Thanks, but I don’t have the time.\""
        show kan smug with dis
        ka "\"Pity.\""
        show kan smug talking with dis
        ka "\"Hard to find folks anywhere who can push as hard as they give.\""
        show kan smug with dis
        wi "\"I suppose that’s true.\""
        wi "\"But I’ve finished my drink.\""
        show kan sneer with dis
        ka "\"Find me some other time if you want to get physical, law man.\""
        show kan sneer talking with dis
        ka "\"Just for a bit of fun.\""
        show kan sneer with dis
        wi "\"...I’m flattered.\""
        hide kan with dissolve
        "I feel his eyes on my back as I rise out of my seat."
        "Good thing I can see him in the mirror across the room if he tries any sudden moves."
        $ willstag3interview = True
        jump williamstagmenu
label endofwillchallinterviews2:
"That's probably all I'm gonna get out of people right now."
"I think I’m done here."

if STAGNIGHT_Points > 0:
    play music "music/stag1.ogg" fadeout 4.0 fadein 5.0
    wi "\"Thanks for all the help, Nik, but I don’t think there’s a whole lot left for me to learn here.\""
    wi "\"You want to come back to the station with me?\""
    if BG_Light == 1:
        show nik sad at center,light1 with dissolve
    else:
        show nik sad at center,stagback with dissolve
    ni "\"Sam will still be there, won’t he?\""
    "He sounds resentful."
    wi "\"Possibly, unless one of his little friends called him back to the brothel for chores.\""
    show nik sidelook with dis3
    ni "\"I think I’ll stay here a little while longer.\""
    wi "\"Did something happen between the two of you?\""
    show nik talking with dis3
    ni "\"He lied to us for weeks, Will.\""
    show nik -talking with dis
    wi "\"He had his reasons, didn’t he?\""
    show nik disappointed with dis3
    ni "\"For you? Absolutely.\""
    show nik sidelook with dis3
    ni "\"But me?\""
    show nik talking with dis3
    ni "\"I expected more trust.\""
    show nik -talking with dis
    wi "\"He told us eventually, didn’t he?\""
    show nik angry with vpunch
    ni "\"He told {i}you{/i}.\""
    wi "\"I think that’s because he had given up.\""
    show nik sidelook with dis3
    wi "\"He seemed ready for the worst.\""
    show nik talking with dis3
    ni "\"But he should know that he can come to me for anything.\""
    show nik -talking with dis
    wi "\"And I think he would have if he were in a better state of mind.\""
    wi "\"Maybe you should take some comfort in that?\""
    show nik sidelook with dis3
    ni "\"Maybe.\""
    wi "\"So are you in a better state, now?\""
    show nik disappointed with dis3
    ni "\"No.\""
    show nik talking with dis3
    ni "\"But you’re right.\""
    show nik -talking with dis1
    show nik talking with dis
    ni "\"So I will be, eventually.\""
    show nik sidelook with dis3
    "He shifts the weight from the left foot to his right and looks over at the bar."
    show nik eyes with dis3
    ni "\"Goodnight.\""
    show nik -eyes -talking with dis
    wi "\"Until next time.\""
    hide nik with dissolve
    "I hope he means what he says."
else:
    "I’m tired of the smell of sweat and rye whiskey."

    "That seems like all I can learn from here at the moment."

if STAGNIGHT_Points > 0:
    "Time to go."
    stop music fadeout 5.0
    jump hipinvestigation
else:
    "I think it’s about time to head back to the station."
    jump samstation

pause 0.5
label samstation:
scene white with fade
scene black with slow_dissolve
scene officeday with slow_dissolve
play music "music/quiet.ogg" fadeout 4.0 fadein 5.0
window show
$ quick_menu = True
$ quick_menu_will = False
$ willnote = False
"William’s been away for a while."
"It’s hard not to think about that whole experience last night."
"How he described the body fighting against the mind."
"And our bodies being cages."
"...and how we come to love and hate our cages at the same time."
"Paul says, {i}For the mind that is set on the flesh is hostile to God, for it does not submit to God's law; indeed, it cannot.{/i}"

"Never much cared for Paul."
"He didn’t even know Jesus."
"And he doesn’t have much interest in living through the struggle of sin."
"His advice is, more or less, {i}just don’t have it.{/i}"
"Which makes me think he lied a lot."
"To make people only hate their cages."
"To revel in death. To revel in breaking out of them as soon as we can."
"To rush into someplace they don’t know."
"Blind faith, or eternal death."
"...that doesn’t sound like Jesus at all."
"{i}If he sins against you seven times in one day, and each time he comes to you saying, 'I repent,' you must forgive him.{/i}"
"{i}Not seven times. But seventy-seven times.{/i}"
"Jesus believed that sin and redemption were a journey."
"Paul didn’t seem to want to walk at all, so to speak."
show cli angry at left,prisonday:
      xzoom -1
with vpunch
cl "\"Who in blazes does this?\""
show cli doubt with dissolve
show tod talking at right,prisonday with dissolve
to "\"I think he has a lot of special jazz numbers that he worries about getting scratched or taken.\""
show tod with dis
"There’s not been a whole lot to do for those two since they found out Will locks his record cabinet."
show cli talking with dis
cl "\"Surely he could leave something cheap out.\""
show cli doubt with dis
cl "\"At the very least a holiday jingle or two?\""
show tod sad with dis
to "\"I wouldn’t say the sheriff is much of a Noel type.\""
show cli shocked
show tod surprised
with vpunch
play sound "sfx/softknock.ogg"
"They both flinch when somebody knocks at the door."
show cli doubt
show tod annoyed
with dis
m "\"Is Will finally back?\""
show tod talking with dis
to "\"Naw, he has his own key, so it wouldn’t make much sense for him to be knocking.\""
show tod with dis
show tod talking with dis
to "\"Back in a jiffy.\""
hide tod with dissolve
show cli talking with dis
cl "\"...bit of an odd expression.\""
show cli happy with dis
cl "\"Samuel, would you happen to know the increment of time that constitutes a jiffy?\""
m "\"Don’t know.\""
m "\"It’s just an expression people say.\""
show cli talking with dis
cl "\"I’ve heard people use it before at my university, but it’s much more prevalent here.\""
show cli with dis
show cli talking with dis
cl "\"How fun.\""
show cli with dis
show tod talking at right,prisonday with dis
to "\"Sam, you have a lady friend at the door.\""
show tod with dis
"He lowers his voice."
show tod eyes happy with dis
to "\"And she smells real nice.\""
show tod surprised with dis
to "\"Like apples.\""
show cyn a at center,prisonday with dissolve
"Cynthia walks on up to us through the doorway."
"She looks more dolled up than usual."
m "\"Cynthia?\""
show cyn talking a with dis
cy "\"Good afternoon Sam.\""
show cli eyes talking with dis
show cyn a with dis
cl "\"Hello miss Cynthia.\""
show cli eyes with dis
show cyn surprised a with dis
cy "\"Oh.\""
show cyn happy a with dis
cy "\"You took me by surprise.\""
show cyn talking a with dis
cy "\"Good afternoon, Mr. Tibbits.\""
show cli talking with dis
show cyn a with dis
cl "\"You look absolutely radiant today!\""
show cli with dis
show cyn talking a with dis
cy "\"Thank you!\""
show cyn a with dis
show cyn talking a with dis
cy "\"Now I don’t mean to be curt, but might I have some privacy with Mr. Ayers?\""
show cyn a with dis
show cli happy with dis
cl "\"Well of cou--\""
show cli shocked with dis
show tod yell with vpunch
to "\"You heard the lady! Now move out!\""
hide cli
hide tod
with dissolve
"Todd practically tackles Cliff out of the office, leaving Cynthia alone with me."
"Christ Todd, if this was somebody else it could have been a problem."
show cyn serious a with dis
cy "\"It’s been a few days.\""
m "\"Yeah, I suppose it has.\""
m "\"I guess I kind of lost track.\""
hide cyn with dissolve
"She walks over to Will’s desk and starts rifling through his drawers."
m "\"Whoa, whoa, whoa!\""
m "\"What are you doing?\""
show cyn talking a at center,prisonday with dissolve
cy "\"Learning.\""
hide cyn with dissolve
m "\"That’s illegal, Cynthia.\""
show cyn happy a at center,prisonday with dissolve
cy "\"Tremendous.\""
hide cyn with dissolve
"She pulls out a notebook, flips through a few pages, and rips them out."
m "\"Lord have mercy, what are you up to?\""
show cyn serious a at center,prisonday with dissolve
cy "\"Just taking a few things about me and some friends that he has, that’s all.\""
show cyn angry a with dis
cy "\"I don’t see the big deal.\""
m "\"He’s gonna know you took them.\""
show cyn serious a with dis
cy "\"Then I’ll just lie.\""
show cyn talking a with dis
cy "\"He shouldn’t have this stuff in the first place.\""
show cyn a with dis
m "\"He’s working on a case for Christ’s sake.\""
m "\"You might screw something up.\""
show cyn angry a with dis
cy "\"If he wants to record this information then he can ask these girls for it to their faces himself.\""
show cyn serious a with dis
cy "\"That sound good?\""
m "\"Whatever.\""
show cyn angry a with dis
cy "\"Is he using you to spy on people?\""
m "\"He hasn’t asked.\""
show cyn serious a with dis
cy "\"Make sure he doesn’t.\""
"I roll my neck."
m "\"If he does then that’s my call to make, isn’t it?\""
"She puts the journal back as neatly as she found it."
show cyn angry a with dis
cy "\"I’m warning you, Sam.\""
show cyn serious a with dis
cy "\"Folks in our line of work are the first to get blamed when shit hits the fan.\""
show cyn eyes a with dis
cy "\"Happens to friends in Coalville. And in Payton. It’s definitely happened before here, too.\""
show cyn serious a with dis
m "\"Wouldn’t he have done that to me already if he was gonna do it?\""
show cyn surprised a with dis
cy "\"I never said I think he dislikes you Sam.\""
"She flaps the pages she tore out of the book loudly, then she stuffs them into her purse."
show cyn angry a with dis
cy "\"I just can’t ignore what he is, and I don’t think you should either.\""
show cyn serious a with dis
cy "\"Just find a way to protect yourself, even if you don’t have to use it.\""
show cyn happy a with dis
cy "\"And come back to work tonight. We miss you.\""
show cyn a with dis
m "\"Alright, alright, I’ll go in.\""
show cyn fear a with dis
play sound "sfx/dooropen.ogg"
"We hear the front door open."
show cyn serious a with dis
"I feel my throat drop into my stomach when I hear William’s voice."
show wil talking at right,prisonday with dissolve
wi "\"I’m back Sam.\""
show wil with dis
show wil shocked with dissolve
"I look back and forth from him to Cynthia and she just crosses her arms."
show wil sideeyes with dissolve
wi "\"And Cynthia too?\""
show cyn talking a with dis
cy "\"Didn’t think I’d be dropping by here either, but if it’s the only way to see Sam for days then I guess it’s all I can do.\""
show cyn a with dis
"She adjusts her purse and walks past Will into the doorway."
show cyn happy a with dis
cy "\"Enjoy the rest of your afternoon, gentleman.\""
show cyn a with dis
show cyn talking a with dis
cy "\"You know where to find me.\""
show cyn a with dis
hide cyn a with dissolve
"Will watches her leave."
show wil surprised at center with dissolve
wi "\"The hell was going on in here?\""
m "\"She’s mad that I’m not at the brothel enough.\""
show wil talking with dissolve
wi "\"Perfect timing, then.\""
show wil with dis
"He takes some money out of his pocket and puts it in my hand."
show wil embarrassed with dissolve
wi "\"For last night.\""
show wil talking with dissolve
wi "\"Should be enough to get them off your back for a while, right?\""
show wil smile with dis
m "\"It won’t hurt.\""
m "\"But I think she wants to see me more.\""
show wil eyes with dis
"Will shrugs."
show wil talking with dis
wi "\"Then maybe she should start paying.\""
show wil smile with dis
m "\"Hilarious.\""
show wil talking with dis
wi "\"I brought you something to eat.\""
show wil with dis
m "\"What? More beans?\""
"It’s... a sandwich."
"A really nice looking one."
m "\"Is that smoked salmon?\""
show wil talking with dis
wi "\"There’s a nice place downtown that was open.\""
show wil smile with dis
m "\"Did you get anything for yourself?\""
show wil eyes with dis
stop music fadeout 3.0
wi "\"I ate on the way.\""
hide wil
scene black with fade
play music "music/toddtheme.ogg" fadeout 4.0 fadein 5.0
$ quick_menu = False
$ quick_menu_will = True
$ willnote = True
"I'm glad Sam likes the sandwich."
$ current_journal_page = 12
$ unlocked_journal_pages += 1
$ renpy.notify("Notebook updated.")
"...Cats are supposed to like salmon, right?"
scene officeday with slow_dissolve


if STAGDAY_Points > 0:
    $ CITYHALLNIGHT_Points +=1
    jump cityhallnight
else:
    $ STAGNIGHT_Points +=1
    jump stagnight

label hipinvestigation:

scene echoroadnight with dissolve
stop music fadeout 3.0
play background "sfx/desertmorning.ogg" fadein 3.0
"Everywhere I’ve been today seems to be pointing me in the same direction."
$ current_journal_page = 14
$ unlocked_journal_pages += 2
$ renpy.notify("Notebook updated.")
"The Hip."
"Dora’s carved out a sizable space in this podunk."
"The CGCS put Echo on the map economically, but the brothel is the only thing in town that attracts genuine celebrities."
stop background fadeout 3.0
scene black with fade
scene saloon2 with slow_dissolve
"Not everybody might be able to afford the Hip daily."
"But everybody’s been there at least once."
"And it’s not just the prostitutes who love the madam."
"Mormons and Meseta; Marxists and capitalists; atheists and Protestants; suffragettes and satirists; bull moose boys and yes-men conservatives."
"They might not break bread together, but they mingle in and out, day and night, under the uneasy solidarity of sex and socialization."
"It’s one AM there, so it’s eleven PM here."
scene white with dissolve
"I walk up the stairs and go through the double doors."
scene powderroom with slow_dissolve
play music "music/powderroom.ogg" fadeout 4.0 fadein 5.0
"The powder room is fully active."
"The first person I look for is the person I don’t want to see."
"And I don’t see her, for now."
"But I have no idea how long I’ll have."
"I might have time to interview only one person."

show cyn a with dissolve
"Cynthia is flitting to and from nearly every single male in the room, starting conversations."
wi "\"Evening, Cynthia.\""
show cyn serious a with dis
"She gives me a look."
show cyn talking a with dis
cy "\"Evening, Adler.\""
show cyn a with dis
wi "\"Saw you coming back from the station today.\""
show cyn talking a with dis
cy "\"And?\""
show cyn serious a with dis
wi "\"Just wondering what it’s all about.\""
wi "\"You left in a bit of a hurry when you saw me walk through the door.\""
show cyn talking a with dis
cy "\"It’s hard to have a conversation with Sam when you’re monopolizing him.\""
show cyn serious a with dis
"The hell?"
wi "\"That’s crazy talk.\""
show cyn angry a with dis
cy "\"Is it now?\""
show cyn talking a with dis
cy "\"I’ve barely seen him at work now that he’s running around town with you.\""
show cyn serious a with dis
wi "\"He’s a free agent.\""
show cyn happy a with dis
cy "\"Funny how you’re saying that.\""
show cyn serious a with dis
cy "\"You know he told me, don’t you?\""
"He did {i}what{/i}!?"
show cyn angry a with dis
cy "\"It seems like that scares you.\""
wi "\"Because it does.\""
show cyn serious a with dis
cy "\"Now why’s that, exactly?\""
"I lower my voice to a whisper."
wi "\"Because it could get him into deep trouble.\""
show cyn happy a with dis
cy "\"Or maybe you’re just scared that I’ll convince him that you’re taking advantage of his fear.\""
show cyn serious a with dis
"What the hell has gotten into her?"
wi "\"You tell that story to anybody with loose lips and you’ll damn him, woman.\""
show cyn happy a with dis
cy "\"You really think the word of one Meseta hooker is more trustworthy than the big shot sheriff?\""
show cyn serious a with dis
cy "\"I thought you were supposed to be smart, Adler.\""
"God, she gets really squeaky when she’s mad."
show cyn angry a with dis
cy "\"If you use him like you use the rest of this brothel and then leave him to rot, you'll take some damage.\""
"She's never been this brazen with me before."
show cyn serious a with dis
wi "\"I’m not doing any of that.\""
show cyn serious a with dis
cy "\"Are you kidding me?\""
show cyn angry a with dis
cy "\"His habits are completely different now.\""
show cyn talking a with dis
cy "\"I don’t believe for a second that you aren’t influencing him to stay with you.\""
show cyn serious a with dis
wi "\"Calm yourself.\""
wi "\"I’m just trying to teach him to protect himself for once in his life.\""
wi "\"What he does with that is up to him.\""
wi "\"But he’s not safe being on his own yet.\""
wi "\"There are things going on that you don’t know about.\""
show cyn eyes a with dis
"She holds up a digit."
show cyn serious a with dis
cy "\"I’ll give you one chance Adler.\""
show cyn angry a with dis
cy "\"One.\""
show cyn serious a with dis
cy "\"If you fuck him up, I promise I will find some way to make you pay.\""
wi "\"One chance is all I need.\""
show cyn angry a with dis
cy "\"Don’t you dare make me regret this.\""
hide cyn with dissolve
$ renpy.notify("Notebook updated.")
$ current_journal_page = 12
$ cynthiatext = "Maybe Cynthia does too."
"I take a deep breath as she walks away."
"Shit."
"I wonder who pissed in her grits this morning."
"I’ve got to shake this off."
"I’m here for a reason besides Sam tonight."
"Too many people pointed me in this direction for me to ignore that."
"The first strange thing I see is Harlan, serving drinks."
"Dora is on the couch. She's been watching me ever since I entered the room."
"The only other person who’d be easy to access is Ethel, sitting alone on the couch."

menu hipinvestigation1:
    "Now, who would be the most useful to talk to?"
    "Talk to Dora.":
        $ DORINT_Points +=1
        show dor cig talking with dissolve
        md "\"Back so soon, Sheriff?\""
        show dor cig with dis
        wi "\"Duty calls, ma’am.\""
        wi "\"Your office?\""
        show dor cig profile thinking with dissolve
        md "\"Very well.\""
        hide dor with dissolve
        "She puts out her cigarette in her glass and Harlan doesn’t have to be asked to attend to it at once."
        scene doraofficenight with dissolve
        show dor cig profile squint at center,saloon with dissolve
        "Once we’re alone in her office, she gives me her classic glare."
        show dor cig profile talking with dis
        md "\"Could you please do me the favor of keeping this meeting short?\""
        show dor cig profile thinking with dis
        md "\"It’s the start of the week, and it’s already been a long day.\""
        show dor cig profile squint with dis
        wi "\"Any information your girls collect on James would be useful to have.\""
        show dor cig amused with dissolve
        md "\"Good heavens.\""
        show dor cig talking with dis
        md "\"Is this just another dick waving contest between you two?\""
        show dor cig with dis
        wi "\"Ma’am, no.\""
        wi "\"I have reason to believe somebody is targeting him by targeting one of his valued employees.\""
        show dor cig talking with dis
        md "\"Well there’s not a whole lot to know about him that you don’t know already, is there?\""
        show dor cig profile thinking with dissolve
        md "\"He fucks a lot of my girls and wants to bed Samuel, too.\""
        wi "\"And you’re still blocking that, right?\""
        show dor cig profile talking with dis
        md "\"I prioritize him last, but he’s persistent, so he’s bound to get a booking one of these days.\""
        show dor cig profile with dis
        show dor cig profile talking with dis
        md "\"I won’t be surprised when he becomes brazen enough to ask Sam himself.\""
        show dor cig profile squint with dis
        md "\"Why do you care so much about that anyway?\""
        wi "\"I don’t.\""
        wi "\"I just think it’s funny.\""
        show dor cig talking with dissolve
        md "\"Well you better keep up with the price tag if you think it’s so funny.\""
        show dor cig with dis
        wi "\"I pay well in advance, don’t I?\""
        show dor cig talking with dis
        md "\"You slip up sometimes.\""
        show dor cig with dis
        show dor cig talking with dis
        md "\"But regardless of that, I’m sorry that I don’t know much more unless you want very niche specifics, and even then, I couldn’t promise to know.\""
        show dor cig worried with dis
        md "\"The man’s tiresome.\""
        show dor cig talking with dis
        md "\"Is there anything else?\""
        show dor cig with dis
        "Well, shit."
        "I’ve got nothin’."
        wi "\"I think that’s it for now.\""
        show dor cig talking with dis
        md "\"Then let’s return to the powder room, shall we?\""
        show dor cig with dis
        scene powderroom with dissolve
        "I can never read that woman well."
        "When I get back to the powder room, I check my watch."
        jump hattie

    "Talk to Harlan.":
        show har
        show dor cig at left
        with dissolve
        wi "\"Harlan Perkins, might I have a word?\""
        show har eyebrows
        show dor cig profile
        with dissolve
        "He looks to Dora, who swirls the contents of her glass, then he looks back to me."
        show har eyes with dis
        ha "\"If we must, Sheriff Adler.\""
        show har talking with dis
        ha "\"I do have a job to do, and we’re on the clock.\""
        show har eyes with dis
        wi "\"I’ll try not to keep you long.\""
        wi "\"Might we use your office, ma’am?\""
        show har angry with dis
        ha "\"Is that necessary?\""
        show dor cig profile thinking with dis
        md "\"Go ahead.\""
        show dor cig profile talking with dis
        md "\"The last thing we need is the both of you putting a damper on the atmosphere.\""
        show dor cig profile thinking with dis
        wi "\"Much appreciated.\""
        show har angrier with dis
        ha "\"...\""
        scene doraofficenight with dissolve
        "I lead the way to Dora’s office, and I close the door behind us."
        show har talking at center,saloon with dis
        ha "\"Now what’s the meaning of this?\""
        show har with dis
        "I shrug and put up my hands."
        wi "\"No need to be so defensive, Mr. Perkins.\""
        wi "\"I’m on a case, and it might be helpful if you could answer a few of my questions.\""
        show har talking with dis
        ha "\"Might a man feel indignant when he’s shaken down by the law?\""
        show har annoyed with dis
        wi "\"That’s not the situation Mr. Perkins.\""
        wi "\"I’m asking you questions all peaceful-like.\""
        wi "\"Helping me helps you if there’s trouble in our community.\""
        show har talking with dis
        ha "\"And I’m trouble now, is that it?\""
        show har annoyed with dis
        "He sure is dancing around anything that I ask him."
        "He throws out a hell of a lot of questions to statements I don’t make."
        "That alone is a bit suspicious."
        if  MININT_Points > 0:
            $ HARINT_Points +=1
            wi "\"I hear you don’t get along with Mr. Hendricks so much.\""
            wi "\"That true?\""
            show har angry with dis
            ha "\"He stands on the shoulders of giants and makes problems for better men.\""
            "Huh."
            "He didn’t even bother to deflect that one."
            "It came out a little more heated than I expected."
            wi "\"What sorts of problems?\""
            show har angrier with dis
            ha "\"He brings the wrong sort of people into town.\""
            "That’s true."
            "He brought in me, for example."
            show har talking with dis
            ha "\"We need sturdy, practical men, not dreamers and idealists.\""
            show har angrier with dis
            show har talking with dis
            ha "\"Men who can rear a family and keep their noses to the grind.\""
            show har angrier with dis
            show har talking with dis
            ha "\"Those kinds of men are the backbones of society, and we serve them.\""
            show har angrier with dis
            show har talking with dis
            ha "\"Men like you, for instance.\""
            show har angrier with dis
            show har talking with dis
            ha "\"You’re more familiar with a pistol in your hand than a cocktail glass.\""
            show har annoyed with dis
            wi "\"You’re making me swoon, Mr. Perkins.\""
            "But you’re digging yourself an impressive hole."
            wi "\"Do you know anybody else who might share these views on the type of riff-raff James drags into town?\""
            show har smug with dis
            ha "\"Far more folks than you’d think.\""
            "So you aren’t naming names, you have a grudge against James and the people he hires, and you have constant contact with Dora."
            $ current_journal_page = 13
            $ renpy.notify("Notebook updated.")
            $ harlantext = "Harlan has a grudge against James and has regular access to most of Dora's information."
            "That’s very interesting."
        else:
            "But then again most people don’t like James."
        wi "\"How would you describe your relationship with Mr. Hendricks?\""
        show har smug with dis
        ha "\"I serve him drinks and redirect his drudgery when he flummoxes patrons in the bar area.\""
        wi "\"And does that create a lot of problems in the bar?\""
        "The hare uncrosses his arms."
        show har unamused with dis
        ha "\"When the other patrons like him, they love him.\""
        show har unamused talking with dis
        ha "\"It’s the staff he tends to flummox.\""
        show har unamused with dis
        wi "\"Have you ever seen his business partners come into the saloon together?\""
        wi "\"Maybe for a drink, or a company lunch?\""
        show har talking with dis
        ha "\"They do, from time to time.\""
        show har with dis
        wi "\"And do any of them seem to dislike one another?\""
        show har talking with dis
        ha "\"He tends to keep them isolated, so they don’t really know each other.\""
        show har with dis
        "By the way I phrased that question, I didn’t expect him to know anything."
        "But he did."
        "Huh."
        wi "\"I think that’s all I have to ask for now, Mr. Perkins.\""
        show har talking with dis
        ha "\"Was it so urgent that I had to be pulled away on the clock?\""
        show har with dis
        wi "\"Urgent enough by my standards.\""
        wi "\"Thank you for your time.\""
        show har talking with dis
        ha "\"It’s precious, so don’t squander it.\""
        show har with dis
        wi "\"Let’s return to the powder room then, shall we?\""
        hide har with dissolve
        scene powderroom with slow_dissolve
        "When I get back to the powder room, I check my watch."
        jump hattie

    "Talk to Ethel.":
        show eth with dissolve
        wi "\"Evening, ma’am.\""
        show eth talking with dis
        et "\"Are you talking to little old me?\""
        show eth with dis
        wi "\"I’m not talking to anybody else, am I?\""
        show eth talking with dis
        et "\"You’ve got a big mouth.\""
        show eth with dis
        show eth talking smug with dis
        et "\"I wonder if that applies the rest of you?\""
        show eth with dis
        "Whoa."
        "She’s laying it on a bit thick, ain't she?"
        wi "\"I’m not interested in your cunt, ma’am.\""
        show eth talking sus with dis
        et "\"Oh wait a minute.\""
        show eth with dis
        show eth talking shock with dis
        et "\"You’re the fucking sheriff, aren’t you?\""
        show eth talking sus with dis
        et "\"Oh God fucking damn it, of course you are.\""
        show eth talking frown with dis
        et "\"What the hell do you want?\""
        show eth frown with dis
        wi "\"I want to ask some questions is all.\""
        show eth talking sideeye frown with dis
        et "\"Then hand over some money. This isn’t a charity.\""
        show eth frown with dis
        wi "\"Easy enough.\""
        "I hand her a few dollars."
        "But she still isn’t pleased."
        show eth talking frown with dis
        et "\"What, you think that’s all I’m worth.\""
        show eth frown with dis
        wi "\"I’m not exactly paying by the hour now, am I?\""
        if  PORINT_Points > 0:
            $ ETHINT_Points +=1
            wi "\"Be careful about how you proceed though.\""
            wi "\"You probably want to act calm and lower your voice.\""
            show eth talking sideeye frown with dis
            et "\"And why should I?\""
            show eth frown with dis
            wi "\"Because the law in this city discovers lots of things.\""
            "I lean forward."
            show eth talking shock with dis
            wi "\"And if it turned out you had a bad habit of breaching the confidentiality of your coworkers’ clients...\""
            "I look over in the direction of the madam."
            wi "\"Your employer might not take so kindly to that.\""
            "She looks really uncomfortable now."
            $ current_journal_page = 14
            $ renpy.notify("Notebook updated.")
            $ etheltext = "Ethel reacted to a hollow threat of exposure. She's probably the one leaking information to James."
            "It looks like what the librarian said was true."
        else:
            show eth smug with dis
            "She just gives me another shitty smirk."
        wi "\"What can you tell me about James Hendricks?\""
        show eth talking smug with dis
        et "\"Oh, I can tell you plenty.\""
        show eth with dis
        show eth talking smug with dis
        et "\"He’s good, and he pays well.\""
        show eth with dis
        show eth talking smug with dis
        et "\"And he can definitely manage to make me climax.\""
        show eth smug with dis
        wi "\"That’s not the sort of information that I’m looking for, ma’am?\""
        show eth frown with dis
        et "\"And why not?\""
        show eth talking frown with dis
        et "\"I bet you’re one of those sorts who finishes and then rolls over and falls asleep.\""
        show eth with dis
        show eth talking smug with dis
        et "\"I’d still take your money though.\""
        show eth with dis
        show eth talking smug with dis
        et "\"Less work for me if you’re asleep.\""
        show eth smug with dis
        "They’re not paying me enough for this."
        wi "\"Anything else?\""
        show eth talking smug
        et "\"Well, he gives my cunt a fantastic cleaning.\""
        show eth smug with dis
        wi "\"Charming.\""
        show eth talking sideeye with dis
        et "\"Oh, I’m sorry, were you suddenly expecting me to become a prude?\""
        show eth with dis
        show eth talking smug with dis
        et "\"We’re in a brothel, Sheriff.\""
        show eth with dis
        show eth talking smug with dis
        et "\"Or are you just getting shy because you haven’t tried it?\""
        show eth with dis
        wi "\"I’m not much interested in discussing that, ma’am.\""
        show eth talking smug with dis
        et "\"You know, I always suspect a man might be a fairy until they can prove they’re not afraid to go down south.\""
        show eth smug with dis
        wi "\"Probably true.\""
        show eth talking smug with dis
        et "\"So you do have a pulse, after all.\""
        show eth smug with dis
        "I’m starting to wish that I didn’t."
        show eth talking smug with dis
        et "\"I was starting to think I was talking to a man made out of ice.\""
        show eth smug with dis
        show eth talking smug with dis
        et "\"But deep down, there’s always something that gets you men hot.\""
        show eth smug with dis
        "I look her straight in the eye."
        show eth with dis
        wi "\"I know you think you’re slick, ma’am, but this was sloppy.\""
        show eth eyes with dis
        show eth with dis
        show eth eyes with dis
        show eth with dis
        "She’s blinking at me."
        wi "\"Clean yourself up.\""
        show eth frown with dis
        "She starts to shake and then puts out her cigarette."
        show eth talking shock with vpunch
        et "\"Hurry back to your station so you can masturbate, pig.\""
        hide eth with dissolve
        "Then she gets up and stomps off."
        "I can’t help but chuckle."
        "I wish I could tell her that I jerk off plenty."
        "It’s free--and besides. Men know how to make it feel good better than women can, anyway."
        "We’re the ones who know what a cock feels like, after all."
        "I check my watch."
        jump hattie
    "Talk to Cynthia.":
        $ CYNINT_Points +=1
        wi "\"Just one more thing, Cynthia.\""
        show cyn serious a with dissolve
        "She turns on the balls of her heels and stares me down."
        show cyn talking a with dis
        cy "\"What?\""
        show cyn serious a with dis
        wi "\"If you really do care about Sam and the people in this town, I could use your help with my current case.\""
        show cyn angry a with dis
        cy "\"I’m not interested in any of your crackdowns.\""
        show cyn serious a with dis
        "Luckily the room is still crowded enough to drown out our voices."
        wi "\"It’s murder, Cynthia.\""
        show cyn surprised a with dis
        "She lowers her voice too."
        show cyn fear a with dis
        cy "\"...Another?\""
        "I nod."
        wi "\"Can you tell me anything... and I mean anything about James Hendricks?\""
        show cyn serious a with dis
        cy "\"Well, I hate the man’s guts.\""
        show cyn talking a with dis
        cy "\"He buys up Meseta land as quick as he can for much lower than its value and then families have to turn to the reservation.\""
        show cyn serious a with dis
        wi "\"So it’s personal for you.\""
        show cyn angry a with dis
        cy "\"I decided a long time ago that I’d rather sell my body than let another man like that take away my freedom.\""
        show cyn serious a with dis
        cy "\"He’s a client I will never take.\""
        wi "\"I saw earlier that you had Mr. Tibbits as a client.\""
        wi "\"Did he ever talk Hendricks or his business partners?\""
        wi "\"Or maybe he named some folks who don’t like ‘em?\""
        show cyn eyes a with dis
        cy "\"Not really, aside from the men who hurt him earlier.\""
        show cyn serious a with dis
        cy "\"He asked me more about my life than he talked about himself.\""
        show cyn talking a with dis
        cy "\"And then he asked if I could braid some of his fur.\""
        show cyn happy a with dis
        cy "\"Then, he asked if it was a special Meseta braid, but I was just honest and told him it’s how Lucy makes challah bread.\""
        "Yikes."
        show cyn serious a with dis
        cy "\"Oh, don’t give me that look.\""
        show cyn happy a with dis
        cy "\"He’s just another man.\""
        show cyn talking a with dis
        cy "\"Most of you have the bad habit of becoming overfamiliar too soon.\""
        show cyn a with dis
        show cyn happy a with dis
        cy "\"It doesn’t bother me that much because I never let it go too far.\""
        show cyn serious a with dis
        wi "\"Well, I guess that’s all that comes to mind.\""
        wi "\"Thank you for your time.\""
        hide cyn with dissolve
        "I check my watch."
        jump hattie

label hattie:
"Shit, it's already been half an hour."
"I can keep coming back here every so often for reports."
stop music fadeout 3.0
"But for now, I think I’ve lingered here long enough."
scene saloon2 with dissolve
"The safest thing I can do right now is look for Sam."
"He talks to the girls, and I don’t have to be out in the open to reach him."
"If he’s not with a client he’s going to be by himself."
scene smokeroomdark with slow_dissolve
"Odd thing is, his door is open when I get to his room."
wi "\"Samuel?\""
"Nobody answers, which is strange."
"Sometimes he stalks the bar at night when nobody’s there anymore."
"Nik found him drunk there once... after downing a whole glass of absinthe."
"He won’t make that mistake again."
scene saloon2 with slow_dissolve
"As I go down the stairs and turn the corner, I hear somebody rattling around."
hat "\"Back so soon, Will?\""
play music "music/reminiscence.ogg" fadeout 4.0 fadein 3.0
"Shit."
show hat eyes at center,saloon with dissolve
"I see Hattie step out from behind the counter."
"I don’t even want to see her, but there she is."
show hat with dis1
show bg chicagobar behind hat with slow_dissolve
"Still as bright as spun gold as she was back there."
"But just a bit more frayed around the edges."
show hat talking with dis
hat "\"Are you ready to talk yet, or are you just going to yell some more like a big old baby?\""
show hat smile with dis
wi "\"Ain't much to talk about, is there?\""
wi "\"You’re in danger here.\""
show hat angry talking with dis
$renpy.sound.set_volume(0.2, delay=0.0, channel='sound')
hat "\"I keep getting told that I’m in danger everywhere, Will.\""
show hat angry with dis1
show bg chicagotrain behind hat with dissolve
play sound "sfx/l-train.ogg"
show hat angry talking with dis
hat "\"If not here, then it’s the city.\""
show hat angry with dis1
show bg chicagobar behind hat with dissolve
show hat angry talking with dis
stop sound fadeout 3.0
hat "\"If not there, then it’s any city in the north.\""
show hat angry with dis1
show hat angry talking with dis
hat "\"Fact of the matter is, the whole wide world’s a pretty dangerous place for a single mother.\""
show hat angry with dis
wi "\"You had a support system there.\""
wi "\"There were people who would protect you and Andy.\""
show bg chicagotrain behind hat with dissolve
play sound "sfx/l-train.ogg"
show hat angry talking with dis
hat "\"It was cramped and dirty.\""
show hat angry with dis1
show hat angry talking with dis
hat "\"And it was expensive, Will.\""
show hat angry with dis
wi "\"I would have sent you money if you asked.\""
show hat talking with dis
hat "\"Maybe I didn’t want your money.\""
show hat with dis
wi "\"If not mine, then whose?\""
stop sound fadeout 3.0
show bg saloon2 behind hat with dissolve
show hat eyes with dis
"She pulls a lighter and a cigarette from her pocket."
"She’s trembling as she struggles to light it."
"She always did have frail hands."
show hat angry talking with dis
hat "\"I’m paying my own way from now on.\""
show hat angry with dis1
show hat angry talking with dis
hat "\"Besides, Andy’s past the age for alimony.\""
show hat with dis1
show hat talking with dis
hat "\"Mr. Hendricks needs a house cook.\""
show hat with dis1
show hat talking with dis
hat "\"I already took the position.\""
show hat with dis
wi "\"Don’t do it.\""
wi "\"The man’s a two-faced pervert.\""
show hat talking with dis
hat "\"Aren’t you too?\""
show hat eyes with dis1
show bg chicagobar behind hat with dissolve
"She takes a drag on her cigarette."
wi "\"No.\""
show bg saloon2 behind hat with dissolve
wi "\"I told you the truth.\""
show hat shock with dis
wi "\"It would have been wrong to stay together that way.\""

show bg chicagobar behind hat with slow_dissolve
show hat shock talking with dis
hat "\"We built a life together and you put a child in me.\""
show hat shock with dis1
show hat angry talking with dis
hat "\"I’m sorry I couldn’t be the woman you wanted me to be.\""
show hat angry with dis
"All these years and she still doesn’t get it."
show hat eyes with dis
wi "\"I cared about you a lot.\""
show hat smile with dis
wi "\"And you still look good.\""
show hat talking with dis
hat "\"So then what was the goddamn problem, Will?\""
show hat with dis1
show bg saloon2 behind hat with slow_dissolve
wi "\"It’s useless to retread this.\""
show hat talking with dis
hat "\"So then we won’t.\""
show hat with dis
wi "\"Hendricks told me you reached out to him.\""
show hat with dis
wi "\"Is that true?\""
show hat talking with dis
hat "\"Only after I had already arrived.\""
show hat with dis
wi "\"You moved here before speaking with Hendricks?\""
show hat talking with dis
hat "\"In truth, the reason I’m here is because I’m worried about Andy.\""
show hat eyes with dis
wi "\"Why worry about him?\""
show hat angry talking with dis
hat "\"He wants to join the army, Will.\""
show hat angry with dis
wi "\"What’s so wrong with that?\""
wi "\"I served my country in my own way.\""
show bg chicagotrain behind hat with dissolve
play sound "sfx/l-train.ogg"
show hat angry talking with dis
hat "\"And look where that got us.\""
show hat angry with dis
wi "\"My job had nothing to do with what happened to us. You’re just going to have to trust me on that.\""
show hat angry talking with dis
hat "\"I just don’t think it’s a good idea for him to go into the military what with what’s happening in the world right now.\""
stop sound
show hat angry with dis1
show bg chicagostadium behind hat with dissolve
show hat angry talking with dis
play sound "sfx/baseballcrowd.ogg"
hat "\"He needs a strong male influence in his life to set him straight.\""
show hat angry with dis
wi "\"Then you definitely don’t want me involved.\""
wi "\"I’d probably encourage him to go.\""
show hat angry talking with dis
hat "\"And why the hell would you do that?\""
show hat angry with dis
wi "\"If the draft comes around he might not have a choice.\""
stop sound
wi "\"Better to get a head start on an officer position than get dragged in as a foot soldier with everybody else, right?\""
show hat eyes with dis1
show bg chicagobar behind hat with dissolve
show hat eyes talking with dis
hat "\"I don’t want to think about that possibility.\""
show hat eyes with dis1
show bg saloon2 behind hat with dissolve
wi "\"We might have to.\""
show hat shock with dis
"She drops her cigarette into a glass of water."
show hat shock talking with dis
hat "\"Shit!\""
show hat eyes with dis
"I pluck one from my pocket and hand it to her."
"She takes it."
"Then I light it for her."
show hat talking with dis
stop music fadeout 3.0
hat "\"I don’t want to lose him how I lost you.\""
show hat with dis1
show bg chicagobar behind hat with slow_dissolve
wi "\"I told you before.\""
if  SW_Points > 2:
    show bg saloon2 behind hat with slow_dissolve
    play music "music/williamtheme.ogg" fadeout 4.0 fadein 5.0
    wi "\"You didn’t lose me Hattie.\""
    wi "\"I was never yours in the first place.\""
    show hat angry talking with dis
    hat "\"...that supposed to make me feel better, or somethin’?\""
    show hat angry with dis
    wi "\"It’s just the truth.\""
    wi "\"I’m sorry there isn’t any rhyme or reason to it.\""
else:
    play music "music/spiraling.ogg" fadeout 4.0 fadein 5.0
    wi "\"Everything I did was done to keep us safe.\""
show hat eyes with dis
"She exhales."
show hat eyes talking with dis
hat "\"I’ve been having all sorts of bad feelings, Will.\""
show hat eyes with dis
wi "\"Bad how?\""
show hat talking with dis
hat "\"Feelings like I’m being watched.\""
show hat with dis1
show hat talking with dis
hat "\"Or that there’s always somebody waiting around the corner for me.\""
show hat with dis1
show hat talking with dis
hat "\"Like those months when we were stalked.\""
show hat with dis1
show hat talking with dis
hat "\"It’s like they’re back again.\""
show hat eyes with dis1
show hat eyes talking with dis
hat "\"Or more like they never stopped.\""
show hat eyes with dis
"I’ve been feeling the same way."
"But I don’t know if it’s helpful or not to tell her that right now."
wi "\"How did you know how to contact Mr. Hendricks?\""
show hat talking with dis
hat "\"A letter.\""
show hat with dis
wi "\"What was the return address?\""
show hat talking with dis
hat "\"...Didn’t have one.\""
show hat with dis
wi "\"Do you still have it?\""
show hat eyes with dis
"She lowers her paw into the purse at the side and unclasps the copper buckle."
"Then she slips her hand inside."
"She pulls out an envelope with a sliced opening and hands it to me."
"I pull out the letter and read it."
"Some photographs are taped to it, too."
wi "\"What is this?\""
show hat talking with dis
hat "\"That one is the inside of my apartment.\""
show hat with dis1
show hat talking with dis
hat "\"The inside of my bedroom, when I’m asleep.\""
show hat with dis
"Some how... some way..."
"James made this happen."
wi "\"...I’ll kill that man.\""
show hat talking with dis
hat "\"But wouldn’t leaving his own phone number incriminate himself?\""
show hat eyes with dis
wi "\"I don’t think he sent the letter.\""
wi "\"But I bet it’s his fault, some way, some how.\""

show hat talking with dis
hat "\"Can you just look after our son if something happens to me, Will?\""
show hat with dis1
show hat talking with dis
hat "\"That’s all I’m asking.\""
show hat with dis
wi "\"...That’s a big ask, Hattie.\""
show hat shock talking with vpunch
hat "\"Please!\""
show hat shock with dis
stop music fadeout 3.0
wi "\"...I’ve got to go.\""
show hat eyes with dis
play music "music/quiet.ogg" fadeout 4.0 fadein 5.0
wi "\"Call me at the station if you don’t feel safe.\""
$renpy.sound.set_volume(1.0, delay=0.0, channel='sound')
scene echoroadnight with dissolve
"She’s saying something as I go out the back door of the saloon, but I block it out."
"I can’t be mad at her if she was coerced into coming here."
"But I know there were other places she could go and other people she could go to."
show andy angry at center,nightbrown with dissolve
show andy angry talking with dis
an "\"I thought I saw you stalking around out here.\""
show andy angry with dis
wi "\"Good eyes, good ears.\""
wi "\"I’m not surprised.\""
"Guess I ought to learn how to tread even lighter around here from now on."
show andy angry talking with dis
an "\"Save your breath.\""
show andy angry with dis1
show andy angry talking with dis
an "\"It’s your fucking fault we’re out here in the middle of the goddamn desert now.\""
show andy angry with dis
"Lord have mercy."
"Where to start?"
show andy shock with dis
wi "\"First of all... groom your whiskers better.\""

wi "\"They’re gonna look like shit until your mid-twenties.\""
show andy angry talking with dis
an "\"Oh, fuck off.\""
show andy angry with dis
wi "\"Second, what your mom does is her business.\""
wi "\"I know that you work.\""
show andy talking with dis
an "\"Somebody has to stay with her and support her.\""
show andy with dis1
show andy talking with dis
an "\"It’s not you.\""
show andy with dis
"He still thinks he can pull this out on me."
wi "\"That so?\""
show andy shock with dis
wi "\"What’s this I hear about you runnin’ off to the military then?\""
show andy angry talking with dis
an "\"Don’t use that tone on me like you’re my pa.\""
show andy with dis
wi "\"Well, I am.\""
wi "\"But if that’s not good enough for you then just think of me as a concerned third party.\""
show andy talking with dis
an "\"You don’t know what concern even is.\""
show andy with dis
wi "\"Cut the crap, Andy.\""
wi "\"You signing up or not?\""
show andy talking with dis
an "\"A man’s meant to know what to do with a gun in his hands.\""
show andy smile with dis
"I feel more of my breath escape me."
show andy shock with dis
wi "\"You’d do better knowing how to trim first, Andy.\""
show andy angry talking with dis
an "\"I told you to cut that out!\""
show andy angry with dis
wi "\"If you really want to enlist, then you should do it.\""
show andy with dis
wi "\"Better to regret a choice you made yourself than to regret a choice somebody else made for you.\""
show andy eyes with dis
wi "\"It hurts a lot less.\""
show andy eyes talking with dis
an "\"Will you promise to keep ma safe if I do?\""
show andy eyes with dis
if  SW_Points > 2:
    "... I’m not gonna lie here."
    show andy shock with dis
    wi "\"No.\""
    show andy angry talking with vpunch
    an "\"The hell do you mean, no?\""
    show andy angry with dis
    wi "\"Exactly what I said.\""
    wi "\"This place isn’t safe and I told her not to come.\""
else:
    wi "\"I always have, haven't I?\""
    show andy talking with dis
    an "\"And what if you can't this time?\""
    show andy with dis
    wi "\"I expect they'd have to get the drop on me good then, wouldn't they?\""
    "He doesn't look like he's listening to me."
show andy angry talking with dis
an "\"I’ll protect her then.\""
show andy angry with dis1
show andy angry talking with dis
an "\"I’ll do it with my own two hands.\""
show andy angry with dis1
show andy angry talking with dis
an "\"It’s more than you’ve ever done.\""
show andy angry with dis
wi "\"You have no idea what I’ve been through to protect your mom and you probably never will.\""
show andy shock with dis
wi "\"Now you listen and listen good.\""
wi "\"There are people here who absolutely will murder you and your mother if you let them get close.\""
show andy with dis
wi "\"She said that she’s here for... other reasons, but she was coerced without a doubt.\""
wi "\"If you really care about her then you’ll buy her a ticket out of town.\""
show andy eyes talking with dis
an "\"That’s not gonna work.\""
show andy eyes with dis
wi "\"She’ll do whatever you say if you don’t enlist.\""
show andy talking with dis
an "\"It’s okay, Will.\""
show andy with dis1
show andy smile with dis
an "\"I’m a warrior.\""
show andy with dis
wi "\"You are nothing of the sort.\""
wi "\"Now go inside before I beat your ass. It’s not safe after dark.\""
show andy talking with dis
an "\"...Pussy.\""
show andy with dis
wi "\"The fuck you just say?\""
show andy angry talking with vpunch
an "\"PUSSY!\""
show andy angry with dis1
hide andy with dis
play sound ("sfx/doorslam.ogg")
"He slams the door."
stop sound
"Well god damn."
"That boy is in over his head."
"Maybe the military would do him some good."
show sam shocked at center,nightbrown with vpunch
label williamroute3a:
m "\"...Will?\""
show sam surprised -talking with dissolve
wi "\"Sam!\""
show sam neutral talking with dis
m "\"What are you doing here right now?\""
show sam surprised -talking with dis
wi "\"Just catching up on old business.\""
show sam neutral talking with dis
m "\"Fair enough.\""
show sam surprised -talking with dis1
show sam neutral talking with dis
m "\"I’m the one who lives here, though, so stop lookin’ at me like I’m suspicious.\""
show sam surprised -talking with dis
wi "\"I’m not suspicious.\""
"At least not of you."
show sam neutral -talking with dis
wi "\"That was my kid back there.\""
show sam neutral talking with dis
m "\"Seemed prickly.\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"Hardly surprising I s’pose.\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"You see the Mrs. too?\""
show sam neutral -talking with dis
wi "\"Ex-Mrs., but yes.\""
show sam surprised -talking with dis
wi "\"More to the point, whenever they’re close by, there’s no telling who else is.\""
wi "\"Let’s get back to the station.\""
wi "\"Quickly.\""
scene black with slow_dissolve
play sound "sfx/knock.ogg"
pause 1.2
$ quick_menu = True
$ quick_menu_will = False
$ willnote = False
to "\"Hold on to your horses...\""
scene echoroadnight
show wil eyes at right,nightbrown
with slow_dissolve
play sound "sfx/dooropen.ogg"
show tod sigh a at left,nightbrown with dissolve:
    xzoom -1
"Todd’s tired face pokes past the slip of the opening in the door."
show wil surprised at nightbrown with dis
"His fur is a bit mussed and his shirt is extra wrinkled."
stop sound
show wil talking with dis
wi "\"You alright Todd?\""
show wil with dis
show tod surprised a with dis
to "\"Well, ah...\""
to "\"Sir yes sir!\""
show tod sigh a with dis
to "\"Nothing a bit of hot soup and a few laps around town won’t fix.\""
show tod surprised a with dis
m "\"Runnin’ at this hour?\""
"Wouldn’t he trip over his tail?"
show wil talking with dis
wi "\"Seems like you’re trying to go awful quick.\""
show wil with dis
show tod eyes happy a with dis
to "\"A good night’s sleep keeps me spry, sir!\""
show tod talking a with dis
to "\"I need to check in with my folks soon anyway.\""
show wil talking with dis
show tod surprised a with dis
wi "\"You’re leaving like Clifford isn’t in there behind you.\""
show wil with dis
to "\"Oh.\""
show tod sad a with dis
show wil surprised with dis
to "\"Well that’s because he isn’t!\""
show wil talking with dis
wi "\"What do you mean, he isn’t?\""
show wil surprised with dis
show tod surprised a with dis
to "\"He said he was ready to leave.\""
show wil frustrated with dissolve
wi "\"You were supposed to be watching him.\""
wi "\"It was for his own safety.\""
show tod sad a with dis
to "\"Well he wasn’t under arrest now, was he?\""
show wil talking with dissolve
wi "\"No, but that’s not the point.\""
show wil with dis
show tod surprised a with dis
to "\"Well I ran out of things to distract him with, and I didn’t feel good about makin’ him stay.\""
show tod sigh a with dis
show wil surprised with dis
to "\"But I really oughta get some rest, Sheriff.\""
to "\"These shorter naps ain’t cuttin’ it.\""
hide tod with dissolve
"The otter hops down the stoop and waddles across the street with a distracted look on his face."
show wil talking with dis
wi "\"Todd, wait!\""
show wil surprised with dis
show tod surprised a at left,nightbrown with dissolve:
    xzoom -1
to "\"Sir?\""
show wil talking with dis
wi "\"Before you go, I need to ask.\""
show wil with dis
show wil talking with dis
wi "\"Whereabouts did you first find Huxley’s body?\""
show wil with dis
show tod sad a with dis
"He scratches the back of his head, as if trying to remember."
show tod talking a with dis
to "\"In a ditch on the side of the road, coming back the direction from Payton.\""
show wil eyes with dis
show tod a with dis
show tod talking a with dis
to "\"About a fifteen minute’s walk east from the station.\""
show tod a with dis
show wil eyes talking with dis
wi "\"Close enough to plenty of houses with an icebox then.\""
show wil eyes with dis
show wil talking with dis
wi "\"Was anybody near the body?\""
show wil with dis
show tod surprised a with dis
$ update_unlocked_pages(1, 15)
to "\"Sir no sir!\""
show tod talking a with dis
to "\"The road was clear.\""
show tod annoyed a with dis
show wil talking with dis
wi "\"He must have been dumped.\""
show wil with dis
show tod talking a with dis
to "\"By a wagon?\""
show tod annoyed a with dis
show wil talking with dis
wi "\"Something like that.\""
show tod eyes happy a with dis
show wil eyes with dis
to "\"Well, I was glad to be of help!\""
show wil eyes talking with dis
hide tod
with dissolve
wi "\"Well you could also let me know--\""
show wil surprised with dis
"But he's already gone."
show wil frustrated with dissolve
"William exhales."
m "\"He looked distracted.\""
show wil eyes talking with dissolve
wi "\"It comes and goes in waves.\""
show wil eyes with dis
show wil talking with dis
wi "\"But he’s been clumsier with just about everything the last few days.\""
show wil with dis
m "\"What do you think the sudden exit was about?\""
show wil eyes talking with dis
wi "\"No doubt somethin’ irritating.\""
show wil eyes with dis
show wil talking with dis
wi "\"Bound to find out soon though.\""
show wil eyes with dis
wi "\"I always do.\""
scene black with dissolve
scene jailnight with dissolve
show wil at center,prisonnight with dissolve
"The inside of the prison is a lot less dusty than we left it, which would explain the filth on Todd's shirt."
show wil surprised with dis
"Will’s eyebrow lifts as he examines the floor, resting his paws on his hips."
hide wil with dissolve
"Then he walks past the door to his office, stops, then walks backwards, cocking his head as he turns it, pursing his lips as he squints."
show wil frustrated at center,prisonnight with dissolve
wi "\"Oh for the love of...\""
scene officenight with dissolve
"I walk in through the door to see what he’s fussing about."
"The scattered papers look cleaner and are stacked neatly."
"His office is remarkably clean."
"The papers are stacked, the stamps are organized, and there aren’t any stray sheets of paper lying around."
show wil frustrated at center,prisonnight with dissolve
wi "\"I told Todd not to mess with anything.\""
m "\"But ain’t everything better organized this way?\""
show wil talking with dissolve
wi "\"I already had an organized system.\""
show wil with dis
show wil talking with dis
wi "\"Now I just won’t be able to find anything for days.\""
show wil frustrated with dissolve
wi "\"Great.\""
"I see a note of patterned stationery placed on the table."
"It has a mint scent to it."
show wil eyes talking with dissolve
wi "\"What else did he leave...\""
show wil eyes with dis
"There’s fancy lettering in ink."
show wil with dis
m "\"It says something.\""
show wil talking with dis
wi "\"Says what?\""
show wil surprised with dis
m "\"{i}I do so love a desk with a shine,{/i}\""
m "\"{i}And I do so love the scent of pine,{/i}\""
m "\"{i}For a sheriff of reputable achievance,{/i}\""
m "\"{i}To address every public grievance,{/i}\""
m "\"{i}Whilst not buried ‘neath papers, supine!{/i}\""
m "\"Big words.\""
show wil talking with dis
wi "\"Big ego.\""
show wil frustrated with dissolve
wi "\"Insolent bastard.\""
show wil eyes talking with dissolve
wi "\"Should have known better than to leave Todd alone with somebody that pushy.\""
show wil with dis
m "\"Nice of them to clean up for you though.\""
m "\"’Cause I ain’t doing that.\""
show wil talking with dis
wi "\"Didn’t ask you to.\""
show wil with dis
show wil talking with dis
wi "\"But if complete strangers are organizing my personal documents, then they have more than enough opportunities to steal information.\""
show wil with dis
show wil talking with dis
wi "\"I have to at least check to see if everything’s here, now.\""
show wil with dis
m "\"Yeah. All hell’s gonna break loose when people find out who’s pissing in the watering trough.\""
"I pocket my paws and start walking to the direction of the front door."
show wil talking with dis
wi "\"Or maybe where Nik saw you walking back a month ago.\""
show wil with dis
"I swivel on my heel."
m "\"...You wrote that down?\""
show wil eyes talking with dis
wi "\"You’re lucky I burned it.\""
show wil with dis
show wil talking with dis
wi "\"There’s all sorts of information in my notes, Sam.\""
show wil with dis
show wil talking with dis
wi "\"They’re not for just anybody to look at.\""
show wil with dis
m "\"We don’t know if they even looked at anything.\""
show wil talking with dis
wi "\"You’re right.\""
show wil eyes with dis
wi "\"We don’t know.\""
show wil with dis
m "\"I’m worried enough about what is, not what might be.\""
show wil talking with dis
wi "\"Not askin’ you to be worried.\""
show wil with dis
show wil talking with dis
wi "\"Just to prepare for ugly possibilities whenever something like this happens.\""
show wil with dis
m "\"I think you’re on edge.\""
m "\"Do you really need to go and drag me back here just to scare me about Cliff looking at your papers?\""
m "\"Or did you find out somethin’ important in the last 3 hours?\""
show wil talking with dis
wi "\"Found out my ex-wife is working for Mr. Hendricks.\""
show wil with dis
m "\"Bet that stings, but so what?\""
show wil sideeyes with dissolve
wi "\"She showed me a photograph somebody took of her while she was sleeping.\""
wi "\"It was her apartment back at the city...\""
wi "\"Which means it’s almost certainly a mobster.\""
"I click my tongue."
m "\"Didn’t you think it was mobsters back at the tunnel?\""
show wil eyes talking with dissolve
wi "\"I don’t know what I heard back there, but a photograph’s a photograph.\""
show wil eyes with dis
wi "\"And I don’t think she’s lying to me.\""
show wil with dis
m "\"So what?\""
m "\"You think Hendricks is responsible for that?\""
show wil talking with dis
wi "\"Could be.\""
show wil with dis
show wil talking with dis
wi "\"I never talked much with him about my wife.\""
show wil surprised with dis
m "\"Or anybody, for that matter.\""
show wil eyes with dis
"His lips tighten and he nods."
show wil eyes talking with dis
wi "\"So somebody I’m not close to had to tell him about her.\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"That means he has contacts who can supply him with information that isn’t easy to get.\""
show wil eyes with dis
show wil talking with dis
wi "\"The closeness of his contacts is the question.\""
show wil with dis
show wil talking with dis
wi "\"Either he’s paying somebody a pretty penny for knowledge, or he’s making deals with long-founded partnerships.\""
show wil with dis
m "\"Any idea which?\""
show wil with dis
show wil talking with dis
wi "\"Certainly the former since the man is loaded.\""
show wil with dis
show wil talking with dis
wi "\"But as for the latter, I don’t know how many bridges his father or his grandfather burned.\""
show wil sideeyes with dissolve
wi "\"There’s a lot of nasty rumors still dogging them from what I hear around town.\""
show wil with dissolve
m "\"Nasty, how?\""
show wil talking with dis
wi "\"The stories I hear go something like this...\""
show wil with dis
show wil talking with dis
wi "\"Over fifty years ago, James’ grandfather, James the first, hired a Meseta manservant who he had a good social relationship with.\""
show wil with dis
show wil eyes talking with dis
wi "\"Over the course of that partnership, said manservant allegedly murdered over two dozen children, Meseta and settlers alike, and only some of the bodies were recovered.\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"The man was lynched by the town before there was a trial.\""
show wil eyes with dis
show wil talking with dis
wi "\"People also tend to say that James was very reluctant about this series of events, leaving the manor and the mine to his son, James the second.\""
show wil with dis
m "\"So why’s there so much pressure on Hendricks if it was the servant’s fault?\""
show wil talking with dis
wi "\"Some people say James the first was too concerned with his beloved homestead getting associated with the actions of a serial killer and he was too slow to act.\""
show wil with dis
show wil talking with dis
wi "\"Others say the killer was James the first’s lover.\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"But folks around here always try to say that deviant behavior all leads to the same end, so I don’t know how much stock I can put into that version of events.\""
show wil with dis
show wil talking with dis
wi "\"Either way, those events cast a shadow on that family despite James the second’s success with the co-ownership of the mine, and James the first’s success with the food industry by the coast.\""
show wil with dis
m "\"I don’t see what his problems would be finding out what he needs if he has money.\""
show wil talking with dis
wi "\"Well, money can get you a lot of things from people who need money.\""
show wil with dis
show wil talking with dis
wi "\"But when it comes to deals and interactions between families who have had money for generations, well, that’s when money only goes so far.\""
show wil with dis
show wil eyes talking with dis
wi "\"If James is responsible for directing Hattie here, then his family might still have some of those old connections.\""
show wil sideeyes with dissolve
wi "\"But if he didn’t, then somebody else is responsible for what happened to her apartment.\""
wi "\"And if somebody had the ability to find her up north, they certainly have the ability to keep tabs on her here.\""
wi "\"And me too.\""
show wil with dissolve
m "\"...You think that has something to do with everything that’s been going on in Echo?\""
show wil talking with dis
wi "\"Maybe not everything.\""
show wil with dis
show wil talking with dis
wi "\"But somebody wants to keep me busy.\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"Preoccupied at the very least.\""
show wil with dis
m "\"Seems like their plan’s working.\""
m "\"I’m guessing you didn’t pick up any leads again.\""
show wil smile with dis
wi "\"Good news!\""
show wil eyes smile with dis
wi "\"You’re wrong.\""
m "\"Oh yeah?\""

if HARINT_Points > 0:
    show wil talking with dis
    wi "\"That barkeeper at the Hip is a real creep.\""
    show wil with dis
    m "\"Harlan?\""
    m "\"He’s just intimidating, and hard to approach.\""
    m "\"Sort of like somebody else I know.\""
    show wil talking with dis
    wi "\"Hates James’ guts.\""
    show wil with dis
    m "\"So do you.\""
    show wil talking with dis
    wi "\"Has something against Mr. Tibbits too.\""
    show wil with dis
    m "\"So do you.\""
    show wil frustrated with dissolve
    wi "\"You a parrot or something now, Sam?\""
    show wil with dissolve
    m "\"I’m just trying to see where you’re going with this.\""
    show wil talking with dis
    wi "\"He has the means and a motive to want to hurt Mr. Tibbits.\""
    show wil with dis
    show wil talking with dis
    wi "\"He doesn’t want James to do well here.\""
    show wil with dis
    m "\"So what are you going to do about it?\""
    show wil eyes talking with dis
    wi "\"Keep a close tab on him for certain.\""
    show wil eyes with dis
    show wil talking with dis
    wi "\"I also found out Huxley’s gun was pawned and then repurchased.\""
elif ETHINT_Points > 0:
    show wil talking with dis
    wi "\"Your friend Ethel is a snake.\""
    show wil surprised with dis
    m "\"She’s a salamander.\""
    show wil frustrated with dissolve
    wi "\"I mean figuratively.\""
    show wil talking with dissolve
    wi "\"She’s selling brothel information to James.\""
    show wil with dis
    m "\"Are you kidding me?\""
    m "\"She bursts into my room all of the time.\""
    show wil eyes talking with dis
    wi "\"So you should have known ahead of time.\""
    show wil eyes with dis
    m "\"I was always suspicious, sure.\""
    show wil with dis
    m "\"But if you tell the madam she’ll be fired for sure.\""
    show wil talking with dis
    wi "\"So what?\""
    show wil with dis
    m "\"She’ll have no place to go.\""
    show wil talking with dis
    wi "\"None of you will if everybody leaves once they find out all of their personal information is compromised.\""
    show wil with dis
    m "\"Maybe we can resolve this without anybody finding out.\""
    show wil eyes with dis
    wi "\"Maybe.\""
    show wil eyes talking with dis
    wi "\"I’ll see what I can do.\""
    show wil with dis
    show wil talking with dis
    wi "\"I also found out Huxley’s gun was pawned and then repurchased.\""
else:
    show wil smile with dis
    wi "\"Why yes indeedy, Sam.\""
    show wil talking with dis
    wi "\"I found out Huxley’s gun was pawned and then repurchased.\""
show wil with dis
m "\"So how’s that helpful?\""
show wil talking with dis
wi "\"Because it was bought real close to the days it went into somebody else’s hands.\""
show wil with dis
show wil talking with dis
wi "\"His drinking buddy, Reed, didn’t know he was missin’ at the time, so he couldn’t have taken the gun to his usual haunts.\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"So he left the house with the gun, or he didn’t, and Marcy was around to see what happened to it.\""
show wil eyes with dis
show wil talking with dis
wi "\"She’d at the very least know if somebody broke into her home.\""
show wil with dis
m "\"So you’re going back to Marcy’s in the morning?\""
show wil smile with dis
wi "\"Yep.\""
show wil talking with dis
wi "\"Come with me again.\""
show wil with dis
m "\"Why?\""
show wil talking with dis
wi "\"Because you notice some things that I miss.\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"And I need to bounce ideas off of somebody other than Todd.\""
show wil with dis
m "\"If Todd’s not useful, why don’t just you fire him?\""
show wil talking with dis
wi "\"Because he’s good with people.\""
show wil with dis
show wil talking with dis
wi "\"And he’s been a deputy longer than I’ve been a sheriff.\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"Locals wouldn’t be happy.\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"He served under the former sheriff.\""
show wil eyes with dis
m "\"Shouldn’t he have been the sheriff after the old guy left?\""
show wil eyes talking with dis
wi "\"Usually that’s how these things go, but that didn’t happen.\""
show wil eyes with dis
wi "\"Might be because he was too young.\""
show wil sideeyes with dis
wi "\"The prior sheriff’s leave was... sudden, but the City Hall sent out a scouting campaign, paraded me around town to talk about my experiences, then held the election.\""
show wil eyes talking with dis
wi "\"The rest is history.\""
show wil with dis
m "\"You came off a lot more strict back then.\""
show wil eyes talking with dis
wi "\"Because I was.\""
show wil with dis
show wil talking with dis
wi "\"I wasn’t used to six o’clock meaning six fifteen whenever anybody makes plans around here.\""
show wil with dis
show wil talking with dis
wi "\"But I’ve found that the nature of a place changes you more than you’d like to change it.\""
show wil with dis
show wil talking with dis
wi "\"It breaks you when you’re stiff, so you can choose to bend.\""
show wil with dis
m "\"I’m sorry us hicks have disgraced you so.\""
show wil smile with dis
wi "\"I meant no harm by it.\""
show wil eyes with dis
wi "\"Had to bend for the big city too.\""
show wil eyes talking with dis
wi "\"Hard sometimes to take my mind off how where you’re from in the past is just as much a part of who you are as where you live now in the present.\""
show wil with dis
m "\"Is that just a fancy way of saying the past will catch up with you?\""
show wil sideeyes with dissolve
wi "\"More like the past is always here.\""
"He looks like he wants to say something, but won’t allow that for himself."
show wil eyes with dissolve
"But then he takes a seat in his chair, sitting on it backwards while he drapes his arm over the back and holds his wrist."
show wil talking with dis
wi "\"Stay the night again, Sam.\""
show wil with dis
m "\"You need me to take care of you again already?\""
show wil talking with dis
wi "\"Just to sleep.\""
show wil with dis
show wil talking with dis
wi "\"Might as well since it would save you the walk in the morning.\""
show wil eyes with dis
"His leg begins to bounce like he can’t sit still."
m "\"You’re still paying, right?\""
show wil smile with dis
wi "\"What, you think I’m cheap?\""
"I pull back the curtains to see if I see anybody moving around outside."
"The street looks pretty dead."
m "\"Just making sure.\""
"He spins in his chair, almost like a kid."
show wil eyes talking with dis
wi "\"I’m wounded, Sam.\""
show wil eyes smile with dis
m "\"I’ll get you a bandage in the morning if I remember.\""
show wil talking with dis
wi "\"You comfortable sleeping in my bed again?\""
show wil with dis
m "\"Well I already done it once.\""
show wil talking with dis
wi "\"Just making sure.\""
show wil with dis
show wil talking with dis
wi "\"It’s no trouble putting together a pallet for you.\""
show wil with dis
m "\"I said it’s fine.\""
show wil smile with dis
"He smirks a bit."
show wil surprised with dis
m "\"Did I just see you wag?\""
show wil eyes talking with dis
wi "\"Coyotes don’t wag, Sam.\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"You saw me use my tail to keep balance, yes.\""
show wil eyes with dis
"Bullshit."
stop music fadeout 5.0
scene black with slow_dissolve
play background "sfx/crickets.ogg" fadein 5.0
scene bg willbedroomnight with slow_dissolve
"William’s arm holds me by the waist while I sleep."
"I can tell he’s asleep by the way his chest is rising."
"Usually I worry about getting too hot, but I often forget how cold it can get until it’s dark again."
"I sit in silence, wondering if I’m going to hear those noises again."
"Scratches inside the walls."
"I try to listen for them, but there’s nothing."
"That’s when I realize how tired I am."
"Sleep takes me."
$renpy.sound.set_volume(0.3, delay=0.0, channel='sound')
$renpy.sound.set_volume(0.3, delay=0.0, channel='music')
stop background fadeout 5.0
scene black with slow_dissolve
pause 1.5
play sound "sfx/knock.ogg"
pause 1.2
"Fuck."
stop sound
scene bg willbedroom with slow_dissolve
play music ("music/a-moment-of-solace.ogg")
"I throw the thin sheet off of me."
play sound "sfx/knock.ogg"
scene bg willapartment
show wil eyes p at left
with dissolve
"William is sitting by his desk, smoking his pipe as he ignores the beatings against the door."
m "\"That’s not Todd again is it?\""
stop sound
show wil eyes talking p with dis
wi "\"I can tell it is by the way he knocks on the door.\""
show wil eyes p with dis
m "\"Does he do that every morning?\""
show wil talking p with dis
play sound "sfx/knock.ogg"
wi "\"Only when I don’t beat him to the lock.\""
show wil p with dis
m "\"Why don’t you just...\""
stop sound
m "\"Give him a key?\""
show wil talking p with dis
wi "\"I told you before that he ought to know where the spare is hidden.\""
show wil p with dis
m "\"I mean one of those dangly ones on a chain?\""
m "\"For his belt?\""
show wil talking p with dis
play sound "sfx/knock.ogg"
wi "\"For his belt...\""
show wil p with dis
stop sound
m "\"Maybe.\""
show wil talking p with dis
wi "\"You know...\""
show wil eyes p with dis
show wil eyes talking p with dis
wi "\"I stay in bed longer when my temperature’s higher.\""
show wil eyes smile p with dis
wi "\"So it’s technically your fault he’s out there bangin’.\""
show wil eyes p with dis
"He shakes a tin of instant coffee into his mug and starts downing it before it’s completely dissolved."
m "\"You gonna add any sugar or honey to that?\""
play sound "sfx/knock.ogg"
show wil p with dis
"His glance flicks to me, then he tips the mug higher, downing it as fast as possible."
"The empty mug clatters to the table as he lets it sit."
stop sound
show wil talking p with dis
$renpy.sound.set_volume(0.5, delay=0.0, channel='sound')
wi "\"You want any?\""
show wil p with dis
m "\"Nah.\""
play sound "sfx/knock.ogg"
"The banging gets louder while William yawns into one paw and gestures towards the window with his mug."
show wil eyes talking p with dis
wi "\"You get used to it, you know.\""
stop sound
$renpy.sound.set_volume(1.0, delay=0.0, channel='sound')
show wil eyes p with dis
m "\"Let’s let him in already.\""
hide wil with dissolve
scene black with dissolve
play sound "sfx/knock.ogg"
"We dress ourselves and get to the bottom of the stairs."
scene officeday
show wil at right,prisonday
with dissolve
play sound "sfx/dooropen.ogg"
"I’m the one who opens up the door."
stop sound
show tod arms happy at center,prisonday behind wil with dissolve
to "\"Well it’s about time!\""
show tod surprised with dissolve
to "\"Oh howdy, Sam!\""
m "\"Hello.\""
show tod talking with dis
to "\"You got here earlier than me two times in a row?\""
show tod with dis
m "\"I slept here.\""
show tod eyes happy with dis
to "\"Now there’s a relief.\""
to "\"I was about to whup myself for slackin’ more than the volunteer!\""
show tod with dis
show wil talking with dis
wi "\"No need for any of that.\""
show wil with dis
show wil talking with dis
wi "\"But I will need you in top form today.\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"Can you do that for me, Todd?\""
show wil with dis
show tod eyes happy with dis
to "\"Sir yes sir.\""
show tod with dis
show wil talking with dis
wi "\"Good.\""
show wil with dis
show wil talking with dis
wi "\"We’re visiting Marcy Greene again today.\""
show wil with dis
show wil talking with dis
wi "\"I’ve got a keen suspicion that she’s going to know what happened to her husband’s gun the day that he went missing.\""
show wil with dis
show wil talking with dis
wi "\"But even if she knows, she might not tell us.\""
show wil sideeyes with dissolve
wi "\"That gun is crucial to the progress of our case, ‘cause it’s connected to the deaths of at least two people, the attempt of a life on a third, and injuring a fourth.\""
show wil with dissolve
show tod eyes happy with dis
to "\"Well, Marcy’s real nice.\""
to "\"I’m sure she’s gonna help us.\""
show wil eyes with dis
show tod surprised with dis
m "\"She still doesn’t know her husband’s dead, does she?\""
show wil eyes talking with dis
wi "\"Not unless she helped do it.\""
show wil with dis
show tod sad with dis
to "\"You think little old Marcy would do such a thing?!\""
show tod surprised with dis
show wil talking with dis
wi "\"Not really, but we can’t rule anything out too early.\""
show wil with dis
show wil talking with dis
wi "\"She’s certainly a suspect, unlikely as it may be.\""
show wil with dis
show tod sad with dis
to "\"But what would make you suspect such a thing?\""
show wil talking with dis
wi "\"Clear evidence of domestic abuse, for one.\""
show wil with dis
show wil talking with dis
wi "\"I found out from his buddy Reed that he was a heavy drinker.\""
show wil sideeyes with dissolve
wi "\"I also found out from the madam of the Hip that he’d brag about controlling her.\""
show wil talking with dissolve
show tod sad with dis
wi "\"Keeping her in line, so to speak.\""
show wil with dis
show wil talking with dis
wi "\"The last time we were there, it looked to me like she was stuck in place...\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"Like he had made her depend on him as a part of her routine.\""
show wil eyes with dis
show wil talking with dis
wi "\"Depend on him for so long that she couldn’t live an ordinary life without him.\""
show wil with dis
m "\"Why would she hurt him if she relied on him?\""
show wil talking with dis
wi "\"Sometimes desperate people still need an out.\""
show wil with dis
show wil talking with dis
wi "\"Take into account that she flinches when you speak to her.\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"Baggy clothes are good for hiding bruises.\""
show wil eyes with dis
show wil talking with dis
wi "\"I don’t know the extent of what he was doin’ to her, but I have a pretty good idea about what this situation looked like.\""
show wil with dis
show wil talking with dis
wi "\"If he went too far, she could have fought for her life.\""
show wil with dis
show tod sigh with dis
to "\"Sir...\""
to "\"With talk like that, you’re really makin’ it seem like she did kill ‘im.\""
show tod sad with dis
show wil talking with dis
wi "\"Except there’s still the matter of the gun, deputy Bronson.\""
show wil with dis
show wil talking
show tod surprised
with dis
wi "\"If it didn’t go missing with him, why didn’t she use it on him?\""
show wil with dis
show wil talking with dis
wi "\"And if she had used it on him, why would she try to throw it away or give it to somebody else?\""
show wil sideeyes with dissolve
wi "\"She doesn’t strike me as a schemer.\""
show wil with dissolve
m "\"So, the gun...\""
show wil with dis
show wil talking
show tod
with dis
wi "\"I think if we can find out what happened to the gun, we can get a little bit closer to finding out who was involved in the death of Huxley Greene, as well as who was responsible for a hit on Mr. Tibbits.\""
show wil with dis
show wil talking with dis
wi "\"And she’s the only one who might know.\""
show wil with dis
show tod talking with dis
to "\"So what are y’all waiting for?\""
show tod with dis
show wil talking with dis
stop music fadeout 5.0
wi "\"You ready to go, Todd?\""
show wil with dis
show tod surprised with dis
to "\"Ready as I’ll ever be, I suppose.\""

scene black with slow_dissolve
$renpy.sound.set_volume(1.0, delay=4.0, channel='music')
scene bg greenecottage with slow_dissolve
$ quick_menu = False
$ quick_menu_will = True
$ willnote = True
"When we come upon Marcy’s cottage, it’s close to the state it was in a few days ago."
"Except there isn’t that pastry kind of smell anymore, with cinnamon and baked butter."
"It doesn’t smell much like anything."
"Just a bit of overturned earth and dust."
show sam neutral -talking at left:
    xzoom -1
show tod at right
with dissolve
wi "\"Marcy?\""
play sound "sfx/softknock.ogg"
"My knuckles rap against her door."
wi "\"It’s the sheriff.\""
stop sound
wi "\"I want to to talk to you again.\""
play sound "sfx/dooropen.ogg"
"I hear something hobbling around on the opposite side of the door and then it creaks open."
play music "music/mellowpiano.ogg"
show mar dazed with dissolve
show sam surprised
show tod surprised
with dis
"The vacant gaze of Mrs. Greene stares back at us."
stop sound
mar "\"You’re here again?\""
wi "\"Yes, Marcy.\""
wi "\"We need your help again.\""
show mar eyes with dis
mar "\"Have you found him?\""
"I can’t tell her yet."
wi "\"The investigation is underway.\""
show mar eyes talking with dis
mar "\"Come on in, then.\""
show mar eyes with dis
scene bg greenecottageinterior dark with dissolve
show mar at center,house1 with dissolve
show sam surprised -talking at left,house1 :
    xzoom -1
show tod surprised at right,house1
with dissolve
"The state of her house is darker and dingier compared to our last visit."
"There’s so many more dolls."
"All dirty and dingy too."
"I can see clusters of half-filled teacups scattered about the house, some still with fluid in them, catching flies and bugs and specks of grime."
"Yarn has been tacked to the ceiling, like spandrels."
"I think the idea is that it’s supposed to look like the inside of a big-top."
"But the way the banners move makes me think it looks more like the insides of something alive."
wi "\"Thank you for seeing us again, Marcy.\""
wi "\"Truly.\""
show mar talking with dis
show tod sad with dis
mar "\"I just want to see him again.\""
show mar with dis
wi "\"My records indicate that Mr. Greene owned a firearm, pawned, and then repurchased within days of his disappearance.\""
wi "\"This firearm to be exact.\""
show mar dazed with dis
"I put the gun on the table and her eyes go blank."
wi "\"He had this the day he went missing, didn’t he?\""
"She lifts her thumb and sticks out her finger, mouthing gun noises as she points it at me."
show mar eyes talking with dis
mar "\"He’s a good shooter.\""
show mar dazed eyes with dis
mar "\"Rodeo Romeo.\""
mar "\"Gonna take me away.\""
mar "\"Rodeo Romeo.\""
mar "\"Gonna save the day.\""
mar "\"Rodeo Romeo.\""
mar "\"Got time to play.\""
wi "\"What are you singing?\""
show mar smile eyes with dis
"She wheezes first, and then giggles."
show mar smile with dis
mar "\"Our song.\""
wi "\"Marcy...\""
wi "\"Are you dodging my question?\""
show mar with dis
"She pouts."
show mar eyes talking with dis
mar "\"Yes...\""
show mar eyes with dis
wi "\"And why is that?\""
show mar with dis
"She leans away."
show mar talking with dis
mar "\"Bet you think I’m slow, don’t ya?\""
show mar with dis
wi "\"What?\""
show mar eyes talking with dis
mar "\"He ain’t never coming back, is he?\""
show mar eyes with dis
"Maybe you did kill him."
show mar with dis
wi "\"Now why would you say something like that?\""
show mar talking with dis
mar "\"’Cause the dollies don’t lie.\""
show mar with dis
show mar talking with dis
mar "\"They always tell the truth.\""
show mar with dis
wi "\"Your dollies aren’t alive, Marcy...\""
wi "\"They can’t tell you anything.\""
show mar talking with dis
mar "\"If they can tell the truth, they why can’t you?\""
show mar with dis
show tod sigh
to "\"You’re right Mrs Greene, he’s not comin’ back!\""
show tod surprised
show sam -surprised
with vpunch
wi "\"Todd!\""
show mar talking with dis
mar "\"I knew.\""
show mar with dis
show mar talking with dis
mar "\"I knew the whole time he ain’t comin’ back.\""
show mar with dis
show tod sigh with dis
to "\"But there’s other people out there who need your help!\""
show mar talking with dis
show tod surprised with dis
mar "\"I knew.\""
show mar with dis
show sam neutral talking with dis
m "\"Ma’am...\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"We just need to talk to you about the gun!\""
show sam neutral -talking with dis
show mar eyes with dis
"She closes her eyes and starts whispering to herself."
show mar eyes talking with dis
show sam surprised
show tod sad
with dis
mar "\"I knew, I knew, I knew, I knew.\""
show mar eyes with dis
wi "\"Marcy...\""
wi "\"Could we have permission to search your house and the property?\""
show mar dazed with dis
mar "\"...Hmm?\""
wi "\"I can get permission from somebody else if you tell me no, but I don’t want to go through all the trouble.\""
show mar dazed eyes with dis
mar "\"Not like anything matters anymore anyway.\""
wi "\"...I’ll take that as a yes.\""
show mar dazed with dis
wi "\"Again, if you remember anything about this gun, or where it was stored, or who your husband was going to visit the last time you saw him, it could save lives.\""
show mar dazed eyes with dis
mar "\"I knew. I knew. I knew, I knew, I knew.\""
"She keeps repeating the phrase, like it’s a psalm."
hide tod
hide sam
with dissolve
scene black with slow_dissolve
$ quick_menu = True
$ quick_menu_will = False
$ willnote = False
scene bg greenecottage at sunset with slow_dissolve
play sound ("sfx/doorshut.ogg")
show tod sad at right,sunset
show wil eyes at center,sunset
with dissolve
"The door shuts behind us on our way out of the cottage and the window gets shuttered."
"I can hear soft wailing from the inside."
m "\"...I’m afraid of that woman.\""
stop sound
show wil sideeyes with dissolve
wi "\"She’s traumatized, Sam.\""
show wil frustrated with dissolve
wi "\"And now more so because Deputy Bronson couldn’t keep his fuckin’ mouth shut for just a little while longer.\""
show tod surprised with dis
to "\"Well I don’t think you should have lied to her...\""
show wil talking
show tod sad
with vpunch
wi "\"I thought I had explained to you that she’s a suspect?!\""
show wil with dis
show wil eyes talking with dis
wi "\"Now if she’s got something to hide then we’ll never get it out of her willingly.\""
show wil eyes with dis
stop music fadeout 9.0
m "\"So now what do we do?\""
show wil frustrated with dissolve
wi "\"Scout the property and wait for her to calm down.\""
m "\"And how long is that gonna take?\""
show wil with dissolve
show wil eyes with dissolve
wi "\"Could be a few hours, could be a few days.\""
show wil talking with dis
wi "\"Now we just gotta hope for the best that she isn’t guilty and that she’ll be in the right mind to cooperate in the future.\""
show wil with dis
show wil talking with dis
wi "\"Until then we ought to look around.\""
show wil eyes with dissolve
show wil eyes talking with dis
show tod surprised with dis
wi "\"Why don’t you and Todd search the grounds surrounding the house while I search the road.\""
show wil with dissolve
m "\"What should we be looking for?\""
show wil talking with dis
wi "\"Trash, or wheel marks, or scraps of clothing.\""
wi "\"I don't think we'll find anything, but something is better than nothing.\""
show wil with dis
show wil talking
show tod
with dis
wi "\"You could start with her shed.\""
show wil with dissolve
show wil talking with dis
wi "\"She probably has more outdoor storage around here and that’s worth checking too.\""
show wil with dis
"I scratch the back of my head."
m "\"You know, this ain’t my job, Will.\""
show wil talking with dis
wi "\"I know, but it's close to where I'll be for the next few days, and I think it would be best for you to keep by.\""
show wil with dis
m "\"I get that, but I have other things that I could be doing right now.\""
show wil with dis
wi "\"Like I said before, I don't think we're going to find anything.\""
show wil talking with dis
wi "\"I know it's been a long day.\""
wi "\"If y'all don't find anything in a few hours, you and Todd can head off home or back to the office.\""
show wil sideeyes with dissolve
wi "\"I need some time to myself to think about how we’re going about this again.\""
show wil with dissolve
m "\"Alright.\""
m "\"Guess I’m with you for the next few hours, Mr. Bronson.\""
show tod talking with dis
to "\"Looks like I’ll get to show you the ropes for a spell!\""
show tod with dis
show wil talking with dis
wi "\"Let’s try to meet back in front of the house in a few hours.\""
show wil eyes with dis
show wil eyes talking with dis
wi "\"Hopefully no more than two at most.\""
show wil eyes with dis
hide wil with dissolve
"Will trots off down the dusty road, disappearing as he turns past an outcropping of rocks."
m "\"So, how are we supposed to go about this again?\""
show tod talking with dis
to "\"We can start with a general sweep of the perimeter.\""
show tod with dis
show tod talking with dis
to "\"Just think about it like it’s a nice walk.\""
show tod with dis
m "\"Ain’t there more to it than that?\""
show tod talking with dis
to "\"I think it’s best to get a general impression before we get bogged down by any details.\""
show tod eyes happy with dis
to "\"Just keep your eyes and ears open and enjoy yourself.\""
show tod with dis
play background ("sfx/birds.ogg") fadein 8.0
scene bg greeneshed with dissolve
"The Greenes’ property is a lot bigger than I thought it would be, though I suppose it makes sense they’d have more room per how far away from down town they are."
"It takes us about a ten minute hike before we see any trace of anything at all down the dirt road."
"We can see Emma in the distance through a copse of trees, and there are a few shallow creeks and ditches full of smooth pebbles around."
show tod at right,sunset with dissolve
m "\"Just how big is the Greene property?\""
show tod talking with dis
to "\"Fifty acres, roughly.\""
show tod with dis
"That's a huge amount of land for the little cabin to sit on."
"Up ahead, I see a ramshackle building under a thick pine tree that looks like it might be a tool shed, considering it ain’t that big."
show tod at right,sunset
m "\"Think it’s locked?\""
show tod talking with dis
to "\"I’d reckon so.\""
show tod sigh with dis
to "\"Mr. Greene always did get touchy about people stayin’ away from his things.\""
show tod with dis
m "\"Let’s just try.\""
"We walk past pots of succulents here and there, next to squatting ornaments of cast-iron imps, and gnomes, and angels, all with pudgy baby faces."
"There’s a thick padlock over a horseshoe-shaped bar shoved into very thin, very rickety wood."

show tod eyes happy with dis
to "\"Take a look at this puppy.\""
show tod with dis
"He pulls out a pocket knife and pulls out its sides, showing off a set of oddly shaped blade ends."
show tod talking with dis
to "\"I bet if I can fiddle with this for about half an hour and get the right feel, I just might be able to get us inside.\""
show tod surprised with dis
play sound ("sfx/padlock.ogg")
"I jiggle the u-shaped bar and it comes clean out of the wood with the lock falling to the ground."
show tod sigh with dis
to "\"Well, yeah, that was a good idea too.\""
stop sound
play sound "sfx/doorcreakopen.ogg"
"The door creaks as we walk inside the dusty shed."
stop sound
$renpy.sound.set_volume(0.2, delay=0.1, channel='background')
scene bg greeneshedinterior with dissolve

show tod at right,dark3 with dissolve
"Specks of light play off the surface of rusty tools on their racks, and the cobwebs in the corners of the room glimmer."
m "\"You see anything out of the ordinary?\""
show tod talking with dis
to  "\"There’s a hoe, a shovel, a can of oil...\""
show tod annoyed with dis
to "\"A well-used bin with some pine needles on the bottom, a few cans of paint...\""
show tod sigh with dis
to "\"Nothing much out of the ordinary.\""
show tod talking with dis
to "\"I guess we can put the lock and the door handle back into place.\""
show tod with dis
m "\"Shouldn’t we look a little longer?\""
show tod sigh with dis
to "\"I guess we could, but I think we’ve seen everything.\""
show tod with dis
m "\"Right...\""
m "\"But we’ve been here less than a few minutes.\""
m "\"We probably missed something.\""
show tod talking with dis
to "\"Sure, but there’s still a whole lot of land to cover.\""
show tod sigh with dis
to "\"Sometimes there ain’t a whole lot beneath the surface, you know?\""
show tod annoyed with dis
m "\"I’d think it depends.\""
show tod surprised with dis
m "\"Maybe you’re not trying as hard as you could be because you knew ‘em.\""
show tod annoyed with dis
to "\"Know who exactly?\""
show tod with dis
m "\"Well, you’ve known Mrs. Greene for a while, right?\""
show tod talking with dis
to "\"’Course I have.\""
show tod eyes happy with dis
to "\"My uncle works for the bank, so my family always exchanged gifts with the Greenes.\""
show tod with dis
m "\"For some reason I thought your uncle owned a barber shop.\""
show tod talking with dis
to "\"No, that’s my other uncle, Amos Bronson.\""
show tod with dis
m "\"How many uncles you got?\""
show tod talking with dis
to "\"Seven I think, but four of ‘em live up in Camp Rosa so I only see them at the reunion.\""
show tod with dis
m "\"And how many kids they got?\""
show tod eyes happy with dis
to "\"They all got at least three but some of ‘em have up to seven.\""
show tod with dis
m "\"That’s too many.\""
show tod eyes happy with dis
to "\"Ain’t no such thing when it comes to family!\""
to "\"More family just means more to love!\""
show tod with dis
m "\"But how do y’all keep track of each other?\""
show tod talking with dis
to "\"Same way as everybody else does, I suppose.\""
show tod with dis1
show tod talking with dis
to "\"Writin’. Keepin’ picture albums, swappin’ gossip and makin’ memories when we can.\""
show tod with dis1
show tod talking with dis
to "\"And the local family sees one another every Sunday.\""
show tod with dis
m "\"Sounds busy.\""
show tod talking with dis
to "\"When do you see your family?\""
show tod surprised with dis
m "\"I don’t.\""
show tod talking with dis
to "\"How come?\""
show tod surprised with dis
m "\"Don’t like ‘em.\""
show tod sigh with dis
to "\"Well, what for?\""
show tod annoyed with dis
m "\"They had a lot of ideas about what I should be doing, I suppose.\""
m "\"Which trade I should learn.\""
m "\"How often I should be available for them.\""
m "\"They broke the law a lot.\""
show tod talking with dis
to "\"Doin’ what?\""
show tod annoyed with dis
m "\"Nothing too big.\""
m "\"Mostly moonshine.\""
m "\"Sometimes even riskier stuff.\""
show tod sigh with dis
to "\"Bonafide smugglers, huh?\""
show tod annoyed with dis
m "\"I wasn’t proud of them.\""
m "\"But if they knew me now I guess they wouldn’t be proud of me, neither.\""
m "\"And I guess I was scared I’d go down with them one day.\""
show tod talking with dis
to "\"Think they’re in jail by now?\""
show tod surprised with dis
m "\"Who knows if they’re even alive.\""
m "\"I wouldn’t shed any tears for ‘em.\""
m "\"Lord knows they wouldn’t shed none for me.\""
show tod sad with dis
to "\"That’s so sad.\""
show tod surprised with dis
m "\"I think it’s simple.\""
m "\"And fair.\""
m "\"I didn’t agree to be born to those people.\""
show tod sad with dis
to "\"I just don’t like to see a family neglecting one another.\""
show tod sigh with dis
to "\"Family is supposed to help each other.\""
show tod talking with dis
to "\"If not to one another’s dishes at the Sunday potluck, then at least when they’re in trouble.\""
show tod annoyed with dis
m "\"Your family ever try to make you wash your mouth out with bleach if you swore?\""
show tod surprised with dis
to "\"Of course not!\""
show tod sigh with dis
to "\"And we don’t swear at one another because we respect each other.\""
show tod with dis
m "\"That must be nice.\""
m "\"How often did your family visit the Greenes'?\""
show tod talking with dis
to "\"I’ve been over there more times than I can remember.\""
show tod eyes happy with dis
to "\"Since I was a baby, I reckon!\""
hide tod with dissolve
"I know Todd said he wanted to leave but I make sure to turn over every shovel, every can, every piece of junk I can find."
"Todd just awkwardly stands by the door, looking out of it as if he won't leave until I go with him."
"When he figures out I'm determined to be thorough, he sags a bit and starts helping me sort through the junk."
"After a decent while we sort through more paint cans than I can count."
"I check under the slats in the floorboard."
"One of them goes back in quick-like when I see an angry looking black scorpion skittering towards the direction of my arm."
"I wipe my brow with the back of my arm and keep looking."
"Todd looks at me back with that wide stare."
show tod at center,dark3 with dissolve
m "\"Find anything yet?\""
show tod sigh with dis
"He shakes his head."
m "\"Well, we've got just a few more things to look through.\""
show tod with dis
m "\"Do you know if Marcy owned the house before Huxley?\""
show tod talking with dis
to "\"Oh, no, they’ve been together my whole life.\""
show tod with dis
m "\"You know, Mrs. Greene doesn’t look that old.\""
show tod sigh with dis
to "\"Well it’s rude to ask a lady her age, Mr. Ayers.\""
show tod with dis
m "\"So you never did?\""
show tod eyes happy with dis
to "\"No siree-bob.\""
show tod with dis
m "\"Huh.\""
show tod surprised with dis
m "\"You seem tense around women in general.\""
show tod annoyed with dis
to "\"No I don’t.\""
"You can’t just tell somebody that they didn’t experience an observation, Todd."
m "\"What I mean is that you tense up when it comes to asking even basic questions of a woman.\""
m "\"But when you talked with me at the sheriff’s office a few days ago, you got real personal.\""
show tod surprised with dis
to "\"I didn’t mean to!\""
show tod sigh with dis
to "\"I just thought you were used to hearin’ about stuff like that from people.\""
show tod with dis
m "\"I’m not angry.\""
m "\"I just think it’s funny.\""
show tod annoyed with dis
to "\"And I just think it’s important to respect women, okay?\""
show tod sigh with dis
to "\"There’s all sorts of bad people out here here who’d jump at the opportunity to dishonor them.\""
show tod surprised with dis
m "\"People like Mr. Greene?\""
show tod annoyed with dis
to "\"Now wait just a minute...\""
to "\"I never said any of that, now.\""
m "\"You didn’t seem very upset when you showed us Mr. Greene’s body, though?\""
show tod angry with dis
to "\"You trying to imply something?\""
show tod annoyed with dis
m "\"Not much else besides you clearly didn’t like ‘em.\""
m "\"Marks me as queer considerin’ you knew him since you were a baby.\""
show tod angry with dis
to "\"Well it can be hard to make a fuss over bad people when they kick the bucket.\""
show tod annoyed with dis
m "\"You think those rumors William was saying about Huxley were true?\""
show tod angry with dis
to "\"Probably worse, but I don’t like to think about it.\""
show tod sigh with dis
to "\"Mrs. Greene seemed happy enough so I just helped when I could.\""
show tod sad with dis
to "\"She isn’t so good with chores.\""
m "\"I can see that.\""
m "\"I just wanted you to know that most women aren’t like Marcy.\""
show tod surprised with dis
m "\"You treat ‘em like special linens and they’ll be offput by the disrespect.\""
m "\"If you’re not willing to get a little personal with somebody once in a while they’ll think you aren’t interested.\""
m "\"And if you’re always more personal with men than women, well...\""
m "\"You’ll probably find yourself in bed with a man sooner than a woman.\""
show tod annoyed with dis
to "\"Now don’t you go making any presumptions about me, y’hear?\""
m "\"I don’t think it’s presumptuous to say most people get lonely.\""
show tod surprised with dis
m "\"I could tell what you were doing in Will’s attic.\""
m "\"You mentioned Mr. Tibbits before you did.\""
show tod annoyed with dis
m "\"I’ve gotta ask an honest question if you’ll humor me.\""
show tod talking with dis
to "\"Ain’t nobody else out here, so fine.\""
show tod surprised with dis
m "\"...Were you thinking about some she-otter, or were you thinking about him?\""
show tod sigh with dis
to "\"Neither actually.\""
m "\"Then who?\""
show tod surprised with dis
to "\"Those thoughts ain’t pure.\""
m "\"The company you’re in ain’t exactly pure.\""
to "\"Ah...\""
show tod sigh with dis
to "\"You’re definitely sleepin’ with Mr. Adler, then, ain’t you?\""
m "\"I thought you knew.\""
show tod surprised with dis
to "\"Well, ah, I pretty much figured.\""
show tod annoyed with dis
to "\"It's just a lot to take in when I start to really think about it.\""
to "\"I respect Mr. Adler a lot.\""
to "\"He’s sort of like another father to me.\""
show tod surprised with dis
to "\"Sort of like one who tells you all sorts of stuff you’re not supposed to know.\""
m "\"So what?\""
show tod sigh with dis
to "\"So, uh...\""
show tod surprised with dis
to "\"It’s kind of awkward picturing you doing things for him.\""
"He pauses, stammering a bit, like he's trying to spit something out."
show tod sigh with dis
to "\"Mostly because I know he's not supposed to.\""
show tod talking with dis
to "\"And also because I think it’s easy to see why he’d want you to.\""
"Now there's a confession."
"I knew there was something funny about this one when I worked him up to spankin' himself off at the sheriff's office."
"But something's put him in an earnest mood."
"Maybe the all the anxiety's loosened his tongue a bout."
"I heard before from Cynthia that otters get squeaky when they're scared, and also when they're in a mood."
"Maybe Todd's the kind to mix those two emotions up."
show tod surprised with dis
m "\"You saying I make you stiff, Mr. Bronson?\""
to "\"Well I try not to get stiff at all, Mr. Ayers.\""
show tod sigh with dis
to "\"Thoughts lead to actions.\""
to "\"And if I do something like that, I know I ain’t ever gettin’ into heaven unless I marry, and who knows if I’ll ever have the chance.\""
show tod surprised with dis
m "\"You really think all that’s true?\""
to "\"That’s what my family taught me.\""
show tod surprised with dis
m "\"How specific did they get?\""
show tod annoyed with dis
to "\"Mr. Ayers...\""
to "\"Nobody ever goes into the details about things like that.\""
show tod surprised with dis
m "\"So what you’re saying is you don’t know how far is wrong?\""
show tod annoyed with dis
to "\"I think I have a pretty good idea.\""
show tod surprised with dis
m "\"Seed’s gotta go somewhere if it’s not going in a wife, right?\""
show tod sigh with dis
to "\"It’s a violation of something we call the law of chastity.\""
show tod surprised with dis
m "\"But you’ve finished in your paw before, right?\""
show tod sad with dis
"His ears droop."
to "\"I’m not proud of all that.\""
show tod sigh with dis
to "\"Sometimes it comes out and you can’t help it.\""
show tod sad with dis
m "\"So you’re already breaking the rules, ain’t you?\""
show tod sigh with dis
to "\"That path to chastity is a road any man can walk, even after they stray.\""
m "\"So why not stray and walk the path later?\""
show tod annoyed with dis
to "\"Mr. Ayers...\""
m "\"There’s plenty you can do with another man that ain’t quite close to christenin’ your wedding bed.\""
m "\"Sometimes it’s just a matter of helpin’ each other get the stuff out.\""
show tod sigh with dis
to "\"How far could we go if I wanted to stop?\""
m "\"As far as you want if we’re quick about it.\""
show tod sad with dis
to "\"I don’t know if I'd feel right doing something like that in Marcy’s shed.\""
show tod surprised with dis
m "\"A few minutes ago it sounded like you didn’t want to do anything at all.\""
"There’s that ottery smell in the air again."
"Pretty certain he does want to."
show tod sigh with dis
to "\"Can it be outside?\""
m "\"Out in the open?\""
show tod talking with dis
to "\"Feels less disrespectful to indulge in earthly pleasures out in nature.\""
to "\"Plus, there’s coverage behind the shed.\""
to "\"And ain’t nobody comes this way.\""
show tod sigh with dis
to "\"You, ah, really wanna do this?\""
m "\"Do you?\""
show tod with dis
"I'm asking him and myself both the question at the same time."
"I don’t know."
"Another steady customer seems too good to turn up."
"And we already know William is preoccupied in a different direction."
show tod surprised with dis
m "\"How about I just give you a taste of the experience?\""
m "\"We can do something quick and easy and then you can visit me later...\""
m "\"...with money.\""
show tod sigh with dis
to "\"Well how quick is quick?\""
show tod surprised with dis
m "\"Take your shirt off and follow me outside.\""
hide tod with dissolve
pause 0.2
show tod surprised p at right,dark3 with dissolve
pause 0.2
$renpy.sound.set_volume(1.0, delay=1.0, channel='background')
scene bg greeneshed with dissolve
show tod p at center,sunset with dissolve
"We get to the back of the shed, and while it’s not perfectly concealed, I still get the feeling that we’re very much alone, and will be for a long time."
m "\"After we start, no finishing.\""
show tod talking p with dis
to "\"...Why not?\""
show tod p with dis
m "\"Because it has a smell to it.\""
show tod surprised p with dis
m "\"William don’t need an explanation for that, does he?\""
m "\"’Cause if he asks for the truth, I’m just gonna tell him.\""
to "\"Oh God no.\""
m "\"Saying the Lord’s name in vain already?\""
"I tsk."
show tod sigh p with dis
"I touch him through his pants."
show tod arms sigh p with dissolve
"He’s stiff."
"Bigger than I thought he’d be too."
"Then I give him a squeeze through the slacks."
show tod surprised p with dissolve
m "\"Keep these on in case we have to cover up quick if somebody comes our way.\""
show tod sigh p with dis
to "\"D-don’t remind me.\""
show tod surprised p with dis
"I set down a sheet covering a crate and lay it on the dirt."
m "\"Now lie on your back.\""
"He looks left, then he looks right, then bends his knees, scooting backwards."
hide tod with dissolve
"His chest rises as he looks up at me."
"I sink down on my knees, looming over him."
window hide
pause 0.5
scene bg wilcg6a with slow_dissolve
pause 1.0
window show
m "\"What’s the matter?\""
m "\"Scared?\""
"He shuffles a bit, and licks his whiskers."
to "\"Well not of you, no.\""
"I dip my hands down his pants and fish him out."
"God damn, he’s leaking."
"I bow down my head and smirk."
"Then I fish out my own cock and his eyes widen."
"I bring it as close as I can to his cock without touching it."
m "\"Well maybe you should be?\""
to "\"I don’t...\""
m "\"Want to stop yet?\""
to "\"I don’t know.\""
"I scoot in, leaning in closer over him, and hold his wrist down with my paw."
"He isn’t struggling."
m "\"If you don’t want to admit that you like it, you can just blame it on me, you know.\""
"I press us together and he lets out a squeak of surprise."
"His tongue is slipping out of his mouth, and his cock is throbbing with his pulse beneath mine."
window hide
pause 0.5
scene bg wilcg6b with slow_dissolve
pause 1.0
window show
"We're practically stuck to one another now between the two of us because of our pre, and his cock is making sounds each time it pulls away."
m "\"Gonna ask you again...\""
"I punctuate it with slow, deliberate rub, squeezing us together, producing a sloppy sort of sound that’s always much louder than you think it should be."
m "\"Do you want me to stop yet?\""
play sound ("sfx/branch2.ogg")
scene black
stop background fadeout 3.0
"A twig snaps."
scene bg greeneshed:
    zoom 1.03
    truecenter
play sound ("sfx/tumble.ogg")
show tod surprised2 p at right,sunset
with hpunch
"We slide off of one another like we’re the opposite ends of a magnet."
"Fuck, fuck, fuck!"
stop sound
#EDIT1
play music ("music/bedhorror.ogg")
"I look around."
"I don’t see nobody."
play sound ("sfx/belt.ogg")
show tod surprised p with dissolve
"I look at Todd, who’s flailing with the ends of his belt like it’s two heads of fighting snakes."
"I snatch my shirt from off of a beam, toss it on myself, and crouch behind a crate."
stop sound
"He mouths ‘don’t leave me!’ and I try to mouth back ‘you’re just one person, it’s fine!’"




############## cut1

window hide
pause 1.0
stop music fadeout 4.0
scene black with slow_dissolve
stop sound
play background ("music/cicadas.ogg") fadein 5.0
scene bg echoforest at sunset with slow_dissolve:
    zoom 1.03
    truecenter

$ quick_menu = False
$ quick_menu_will = True
$ willnote = True
window show
"I still can’t believe Todd spilled the beans on Huxley."
"If Marcy falls through, or we can’t find any evidence of where the gun went, we’re out of leads and probably out of time."

"I’m pretty sick of carrying around this pistol."
"Usually a weapon alone wouldn’t connect this many people."
"If I were the sort to believe in curses, I’d have this thing melted down after the conclusion of this investigation."
"I’d leave that up to Marcy, but she’s not looking too good."
"I come to the part of the road that’s a three-way juncture."
"East to downtown, west to Payton, south to the railway tracks."

"If there were a road directly north, I’d be at Hendricks manor."
"Sooner or later, I’m going to have to investigate there."
"Even if she’s gonna be there."
"I wonder what sort of game he’s playing with her."
"Did he put her there to keep me away, or did he put her there because he knew I’d be too stubborn to resist an investigation?"
play sound ("sfx/gravelwalk.ogg")
"Up ahead I see something bright sticking up out some of the rocks."
"It’s a discarded gum wrapper."
stop sound
"Tutti-frutti, huh?"
"I don’t recall ever seeing Marcy chewing much gum."
"And Huxley was usually too busy with a bottle."
$ update_unlocked_pages(1, 16)
$ renpy.notify("Notebook updated.")
"This doesn’t look old."
"Makes you wonder who’s been putting this stuff in their mouths."
kaunk "\"Afternoon, lawman.\""
play sound "sfx/branch.ogg"
play music "music/foreman.ogg"
show kan smile at center,sunsetkane with vpunch
"I take a big step backwards."
stop sound
wi "\"Christ on a cracker!\""
wi "\"Ain’t you a sneak.\""
show kan wink with dis
ka "\"Wouldn’t be satisfied with myself if I wasn’t.\""
show kan smile with dis
wi "\"That’s enough tomfoolery.\""
wi "\"This path’s somethin’ of a detour from the main roads.\""
show kan with dis
wi "\"What’s a fella like you doing all the way out here?\""
show kan talking with dis
ka "\"Truth be told, I was looking for ya.\""
show kan with dis
wi "\"Looking for me?\""
wi "\"And how did you know I was going to be here?\""
show kan smug with dis
ka "\"Trailed ya.\""
show kan smile with dis
wi "\"Trailed me?\""
wi "\"Bit suspicious to admit that, yeah?\""
show kan eyes sneer with dis
ka "\"More than a bit! But I’m impatient.\""
show kan smile with dis1
show kan talking with dis
ka "\"Why come there’s such a lack of bounties posted up in this area?\""
show kan smug with dis
ka "\"A man’s gotta eat, as well as wet his whistle.\""
show kan with dis
wi "\"You look plenty well-fed to me.\""
wi "\"And I regret to inform you that we’re a bit of a podunk.\""
wi "\"Not a whole lot of high profile criminals to apprehend around here, so not much need for any bounties.\""
show kan smug with dis
ka "\"That tale’s a little bit different from the ones I hear.\""
show kan smile with dis
"He plucks a piece of grass off of the side of the road and twirls it between his claws."
show kan talking with dis
ka "\"Your families selling off houses.\""
show kan with dis1
show kan talking with dis
ka "\"Your coal workers all up in arms.\""
show kan with dis1
show kan talking with dis
ka "\"And now a banker’s turned up dead for sure?\""
show kan smile with dis
wi "\"Eavesdropping on us, were you?\""
show kan eyes talking with dis
ka "\"Troubling times, Mr. Adler.\""
show kan smile with dis
wi "\"What do you want, stranger?\""
show kan talking with dis
ka "\"I think you missed the part where I told you that I’m very food-motivated, Sheriff.\""
show kan smug with dis
ka "\"You give me a bounty and I’ll be happy to deliver a head.\""
show kan smile with dis
wi "\"Fuck off.\""
show kan eyes sneer with dis
ka "\"Two heads within a day, and they can even be alive if you’re one of those bleedin’ heart types.\""
show kan with dis
wi "\"Only thing that’s bleedin’ is my stomach from the ulcer you gave me.\""
wi "\"Scram.\""
show kan talking with dis
ka "\"Oh come on now, don’t be such a poor sport.\""
show kan eyes with dis1
show kan eyes talking with dis
ka "\"I know how much y’all rely on bounty hunters, so there’s no need to be so prideful.\""
show kan eyes with dis1
show kan talking with dis
ka "\"I’ve helped plenty of lawmen in the course of my career.\""
show kan with dis
wi "\"And how many of ‘em are dead or scandalized now?\""
show kan wink with dis
ka "\"Only the ugly ones.\""
show kan smile with dis
wi "\"Charmers don’t last long around here.\""
show kan sneer with dis
ka "\"Who says I plan to stick around that long?\""
show kan smug with dis
ka "\"I just need a few names, a few pictures, and a fatter wallet, and I’ll be merrily out of your fur.\""
show kan with dis
wi "\"I’ll let you know names once I have some.\""
show kan eyes sneer with dis
"He whistles."
show kan sneer with dis
ka "\"I didn’t take a man with that many scars for bein’ a slacker.\""
show kan with dis
wi "\"I’ll take an extra nap today and think of you.\""
show kan talking with dis
ka "\"You can’t be dumb enough to turn down help when it’s sitting in front of you.\""
show kan with dis1
show kan talking with dis
ka "\"You’re stumbling around. I’m hungry.\""
show kan eyes with dis1
show kan eyes talking with dis
ka "\"And bored.\""
show kan eyes with dis1
show kan talking with dis
ka "\"Let’s come to an understanding?\""
show kan with dis
wi "\"I need information more than I need a maniac pumping lead into suspects right now.\""
show kan smug with dis
ka "\"That’s always part of the job.\""
show kan with dis
wi "\"No killing, no violence.\""
wi "\"Do we have an understanding?\""
show kan eyes talking with dis
ka "\"Unfortunately.\""
show kan with dis
wi "\"Okay then.\""
"I unclench my fist and show him what’s inside."
wi "\"This your gum wrapper?\""
show kan eyes with dis1
show kan with dis
"He blinks at the pack I hold up for him, more than a little derisively."
show kan talking with dis
ka "\"Sure ain’t.\""
show kan with dis
wi "\"That’s all I’ve got to go off of right now.\""
show kan eyes with dis
ka "\"You’ve gotta be funnin’ me.\""
show kan with dis
wi "\"Do I look much like the funny sort to you?\""
show kan talking with dis
ka "\"Fine.\""
show kan eyes with dis1
show kan eyes talking with dis
ka "\"I can work with that.\""
show kan eyes with dis1
show kan talking with dis
ka "\"What’s my rate?\""
show kan with dis
wi "\"An eagle if you tell me something useful.\""
show kan eyes smug with dis
"He whistles."
show kan smug with dis
ka "\"Not a bad start for just a little word of mouth.\""
show kan talking with dis
ka "\"I’m not bullshitting you, you know.\""
show kan smile with dis1
show kan wink with dis
ka "\"I’m good.\""
show kan smile with dis
wi "\"Guess we’ll see.\""
hide kan with dissolve
stop music fadeout 7.0
$ update_unlocked_pages(1, 17)
$ renpy.notify("Notebook updated.")
play sound ("sfx/gravelwalk.ogg")
"I walk away, leaving him to the weeds and the creek as I push past infant pine trees back in the direction of the house."
play sound ("sfx/crunch.ogg")
"But I hear a small crunch where I thought I’d hear nettles."
"I look below my feet and it can tell that what I’m stepping on isn’t any plant debris."
stop sound
"It looks like a small tube with a spool on the end."
"Weird place for something like this to be."
$ update_unlocked_pages(1, 18)
$ renpy.notify("Notebook updated.")
"Probably worth noting."
"Once I’m done sketching it and put it in my pocket, I take a look at my watch."
"It’s six PM there, so it’s four PM here."
"Time to head back."
window hide
pause 0.5
stop background fadeout 6.0
label updatemarcy:
$ quick_menu = True
$ quick_menu_will = False
$ willnote = False

scene black with slow_dissolve
#EDIT2
#play ambient ("sfx/wind2.ogg") fadein 3.0
play ambient2 ("sfx/crows.ogg") fadein 3.0 volume 0.5
#play background ("sfx/birds.ogg") fadein 8.0
scene bg greeneshed:
    zoom 1.03
    truecenter
show tod surprised p at right,sunset
with slow_dissolve
pause 0.5
window show

############ cut2


"I see the otter's muscles tense up, then he crabwalks slowly toward my direction, looking up at the forest."
to "\"Do you think, ah...\""
to "\"Think somebody’s out there, Mr. Ayers?\""
"I perk up my ears."
m "\"Can’t hear nothin’.\""
m "\"Can’t smell nothin’ either.\""
"Well, at least not much else other than a flustered otter."
m "\"You’re twitchy.\""
show tod angry p with dis
"He grits his teeth."
to "\"Well there’s no reason to go on about my nerves being uncomely...\""
show tod annoyed p with dis
m "\"...I mean you must be bothered by that woman.\""
"The otter shakes his head."
show tod sigh p with dis3
to "\"No, that ain’t it at all.\""
show tod annoyed p with dis3
"We stop moving, and we listen."

"Nothing."

show tod sigh p with dis3
to "\"I thought I heard somebody.\""
show tod annoyed p with dis3
m "\"Well, like I said...\""
m "\"It’s probably just your delayed reaction.\""
m "\"You saw that she took the news pretty hard.\""
#adjust
play music ("music/quiet.ogg") fadein 3.0
play sound ("sfx/clothrustle.ogg")
#adjust?
show tod sigh with dis3
"He starts scrambling to button up his trousers and put the rest of his clothes back on."
stop sound
show tod annoyed with dis3
to "\"Now Mr. Ayers...\""
to "\"I know Marcy is upset now and all...\""
show tod talking with dis
to "\"But in the long run, it’s not gonna be so bad.\""
show tod with dis
"I scratch the back of my head."
show tod annoyed with dis
m "\"You mean with Huxley being dead?\""
m "\"I don’t know.\""
m "\"Wasn’t he her provider?\""
show tod angry with dis
to "\"He was her {i}user{/i}, Mr. Ayers.\""
show tod sigh with dis3
to "\"She was the one who did all the chores.\""

#sam?
to "\"He never let her do things how she wanted.\""
show tod annoyed with dis3
to "\"So trust me when I say that I have a good feeling she’s gonna be way happier from now on.\""
"I wipe the sweat off my brow."
m "\"Maybe so.\""
m "\"You know her better than me.\""
"Todd nods his head impatiently."
to "\"So it ain’t nerves.\""
to "\"I heard something.\""
"I clear my throat."
show tod surprised with dis
m "\"You think somebody saw us?\""
"He looks back at me and his mouth trembles."
show tod annoyed with dis
to "\"Nah.\""
to "\"I’m sure somebody woulda said somethin’, right?\""
show tod surprised with dis
m "\"Not necessarily.\""
"The insides of his ears go pale."
show tod sigh with dis3
"Then he shakes his head a bit {nw}"
show tod eyes happy with dis3
extend "and cackles."
show tod talking with dis
to "\"Well. It was just like I was sayin’ before...\""
show tod with dis1
show tod talking with dis
to "\"No reason to worry about somethin’ that ain’t happened yet.\""
show tod annoyed with dis
m "\"I still don’t think there was anybody out there, Todd.\""
"Doesn’t mean some{i}thing{/i} wasn’t out there."
"But I don’t think I should say that out loud."
m "\"Maybe it’s Mr. Greene’s killer coming back to finish the rest of us off.\""
"I expect him to start twitching again, or for his stubby ears to flick back."

play sound ("sfx/holster1.ogg")
"But instead he draws his gun."
stop sound
#sfx?
"He twirls it in his hands like a performer."
"Earlier in the day I might be ducking for cover, half expecting him to drop it."
#toddthezodiackillerconfirmed
"But there’s something about how smooth it spins around his webby claws that lets me know he won’t."
show tod talking with dis
to "\"You sure do say some silly things, Mr. Ayers.\""
show tod with dis
m "\"It wasn’t that funny.\""
show tod eyes happy with dis
play sound ("sfx/holster2.ogg")
"He looks very pleased with himself, slipping the gun back into his holster."
stop sound
show tod talking with dis
to "\"Just be a little more careful about sayin’ something like that when I’m armed.\""
show tod annoyed with dis
"I think the clear skepticism ingrained in my face makes him nervous again."
show tod surprised with dis
m "\"You ever killed a man, Todd?\""
to "\"Well...\""
show tod sigh with dis3
to "\"Never on purpose.\""
show tod annoyed with dis3
"I blink."
m "\"...really now?\""
show tod sad with dis3
to "\"Bad people everywhere often want to hurt the good ones.\""
to "\"Sometimes you have to shoot before they do.\""
m "\"So you think people are just bad or good then?\""
show tod annoyed with dis3
to "\"Well, I don’t know about all that...\""
show tod sad with dis3
to "\"But if they’re pointing a gun at a lil’ old lady and about to rob ‘em blind, then they’re probably bad.\""
show tod annoyed with dis3
m "\"That don’t sound like a thing that ever really happened.\""
show tod sigh with dis3
to "\"Shoot, I wish that were true!\""
show tod annoyed with dis3
"We both look out in the bushes again."
"Todd crouches a bit as if expecting something to jump out at us."

m "\"...so who did you kill?\""
show tod sigh with dis3
to "\"Well, sometimes it’s a lot if they’re all shooting at ya at once.\""
to "\"The {i}who{/i} ain’t always certain or particularly memorable.\""
to "\"But usually it’s cases where the disarming shot is non-lethal, they take to the desert rather than turning themselves in, and they turn up dead elsewhere.\""
show tod annoyed with dis3
m "\"I thought western shoot-outs like that don’t happen no more.\""
to "\"Oh, they still happen.\""
show tod sigh with dis3
to "\"Just tend to end a whole lot quicker than you hear about in stories.\""
show tod annoyed with dis3
m "\"I figured your and William’s jobs were a lot more cushy than that.\""
show tod talking with dis
to "\"Truth be told we haven’t had stuff happen like that publicly since Mr. Adler was elected.\""
show tod with dis1
show tod talking with dis
to "\"I think people are less keen on tryin’, considering his reputation and connections.\""
show tod eyes happy with dis
to "\"It’s like we’re livin’ in a proper residential area now, not just the frontier.\""
show tod with dis
"I nod, slowly."
show tod surprised with dis
m "\"Were you gonna shoot somebody if they saw us?\""
to "\"Huh?\""
to "\"You brought up the killer comin’ back.\""
m "\"Yeah but you didn’t...\""
"He blinks."
show tod annoyed with dis
to "\"Didn’t what?\""
"You didn’t seem that worried about {i}that{/i}."
show tod surprised with dis
m "\"...let’s just drop it.\""
to "\"Okay.\""
show tod annoyed with dis
"We’re both still staring out into the woods."
show tod sigh with dis3
to "\"If you’re wonderin’ whether I liked it or not--\""
show tod surprised with dis3
m "\"I ain’t wonderin’.\""
m "\"I could tell you did.\""
"He gulps."
to "\"Well uh.\""
to "\"I haven’t really had a whole lot of chances to be actin’ up for most of my life.\""
m "\"Actin’ up, huh?\""
show tod sigh with dis3
to "\"Most days I’m up before six AM helping uncle with the horses.\""
to "\"And that’s only when I don’t get called in for any early patrols or late patrols.\""
show tod annoyed with dis3
to "\"The rest of the day it’s police work, then I go home before five where I have to help weed the garden and make sure ma has what she needs for supper.\""
to "\"Then I help with the laundry, wash-up, and I’m in bed by 8:30.\""
show tod surprised with dis
to "\"So there’s not a whole lot of time or privacy to, ah.\""
to "\"Well, you know?\""
m "\"Yeah Todd, I know.\""
show tod sigh with dis3
to "\"...so, uh...\""
to "\"I want to try again.\""
#sfx
show tod surprised with dis
wi "\"Try what again?\""
"Shit."
play sound ("sfx/gravelwalk.ogg") fadein 3.0
"Neither of us had heard Will walking up the road behind us."
"If Huxley’s killer shooting Deputy Bronson from the woods wouldn’t have taken him down right there and then, Todd's surprise might do the trick."
stop sound
show wil at left,sunset with dis3:
    xzoom-1
to "\"William!\""
show wil eyes talking with dis
wi "\"...Yes, that is my name.\""
show wil surprised with dis
"He stops for a moment, and his nostrils flare."
show wil with dis
"Then he looks in between me and Todd."
show wil talking with dis
wi "\"...How did investigating the grounds go?\""
show wil with dis
to "\"...uh.\""
"Just lie if you don’t want to talk about it, Todd..."
show wil eyes talking with dis
wi "\"Y’all were fucking around, weren’t you?\""
show wil with dis
"Todd bites his lip."
show wil talking with dis
wi "\"This ain’t the time or place to be taking things lightly, boys.\""
show wil with dis1
show wil talking with dis
wi "\"The longer we take to find our leads, the quicker our trails will go cold.\""
show wil with dis1
show wil talking with dis
wi "\"Next thing you know, somebody else will end up dead.\""
show wil with dis
m "\"...We did do some looking in the shack.\""
show wil eyes talking with dis
wi "\"Zip up your pants, Sam.\""
show wil with dis
"I look down."
"Huh."
"I’m still kind of hanging out."
"Whoops."
to "\"...I uh.\""
"The otter shuffles awkwardly, looking extremely embarrassed."
to "\"I promise I didn’t do nothin’...\""
show wil talking with dis
wi "\"Yes, Deputy...\""
show wil frustrated with dis3
wi "\"That’s the problem.\""
show tod sad with dis3
to "\"I ah... well, shit...\""
show wil talking with dis3
wi "\"Let’s talk about it later.\""
show wil with dis1
show wil talking with dis
wi "\"I saw Marcy heading into town. Probably towards the Hip.\""
show wil with dis1
show wil talking with dis
wi "\"Do you still have her house key?\""
show wil with dis3
show tod annoyed with dis3
to "\"’Course...\""
show wil talking with dis
wi "\"We should take a look around.\""
show wil with dis1
show wil talking with dis
show tod surprised with dis
wi "\"It’s not impossible nor improbable that Marcy had something to do with the murder.\""
to "\"She wouldn’t!\""
show wil eyes with dis1
show wil eyes talking with dis
wi "\"We don’t know that, but let’s go find out.\""
show wil with dis1
stop music fadeout 3.5


# cut3

window hide
scene black with medium_dissolve
#adjust
scene bg greenecottage at sunset
show tod surprised at right,sunset
show sam surprised at left,sunset:
    xzoom-1
with medium_dissolve

$ quick_menu = False
$ quick_menu_will = True
$ willnote = True
window show
$ update_unlocked_pages(1, 19)
$ renpy.notify("Notebook updated.")
play sound ("sfx/keyopen.ogg")
"When we get to the front door, Todd unlocks it and I make a beeline for the kitchen."
stop ambient2 fadeout 3.0
scene bg greenekitchen at sunset with dissolve
stop sound
play music ("music/contemplation.ogg") fadein 3.5
"For the love of God, what is wrong with this place?"
"I stumble around the kitchen that’s cluttered with half-filled cups and soiled dishes, shuffling past piles of soiled linens."
play sound "sfx/doorcreakopen.ogg"
"I open the cupboard to see if there’s any indication of what might be going on here."
stop sound
"Mostly sealed jars of perishables."
"And a jar of something else."
"I’ve seen this root before."
$ update_unlocked_pages(1, 20)
$ renpy.notify("Notebook updated.")
"These kinds of plant are more commonly found in whorehouses than the cupboards of housewives."
"Maybe Huxley was having her take them."
"I’m afraid to think about the things Huxley Greene might have been doing that I didn’t know about."
"But I’ll have to think about that later."
"There’s a big enough pot below her stove to make large batches of medicine."
"The gas stove is covered in dirty pots and pans, so it doesn’t look like it gets much use."
"Once I’m satisfied with a general scope of the kitchen I move on into the living room."
scene bg greenecottageinterior dark with dissolve
"Her couch is so covered with these damn dolls that she has no place to sit."
"I try not to move anything I’ll forget the placement of, or she might get upset."
"I go to her bedroom."
scene bg greenebedroom with dissolve
"Thankfully it’s a little less cluttered than her living room."
"But her bed..."
"More dolls?"
"No, that’s just one big lump beneath the sheets."
"I don’t know if I can take it if it’s a big doll that looks like Huxley."
"Thankfully it isn’t."
"It’s just more of the little ones."
"She shouldn’t be sleeping with these."
"They’re covered in mold."
"No wonder she looked sick earlier."
"I start to push the dolls off of the bed, but they have a weird feel to them."
play sound "sfx/nope.ogg"
"They land wetly on the ground and make a noise that makes me want to gag."
#adjust
#$ update_unlocked_pages(1, 20)
#$ renpy.notify("Notebook updated.")
stop sound
"This bed is unsanitary."
"She can’t really be sleeping here, can she?"
"I’ll just start with the living room after all."
scene bg greenecottageinterior dark with dissolve
"I can feel the eyes of the dolls on me again when I come back to the room."
"Marcy’s not the first grown woman I’ve known to accumulate baby dolls, and this isn’t even the biggest collection I’ve seen."
"But it’s clear to me that Huxley wasn’t letting her display these when he was around."
"That much I can gather from Todd."
"I know that sometimes, doll collecting is used to fill a caretaking void in ex-mothers or would-be mothers."
"If Huxley hated the idea of having kids, then it makes sense she’d explore those urges when he wasn’t around to take them down."
"But you’d think somebody who don’t want kids for financial reason wouldn’t mind a few dolls here and there lying around."
#adjust
"Todd might be able to walk me through what was going on there."
show tod annoyed at right,house1
show sam neutral at left,house1:
    xzoom-1
with dis3
wi "\"Let’s talk in the kitchen.\""
"They both follow me."
scene bg greenekitchen at sunset with dissolve:
    zoom 1.03
    truecenter
show tod annoyed at right,sunset
show sam neutral at left,sunset:
    xzoom -1
with dissolve
#adjust
wi "\"Todd, Marcy never had dolls out when Huxley was around, right?\""
show tod talking with dis
to "\"Yeah, that’s right.\""
show tod annoyed with dis
wi "\"If there’s this many of them, then Huxley must have been storing them all somewhere, yeah?\""
wi "\"Is there someplace in the house Marcy was never allowed to go?\""
wi "\"Or somewhere Huxley would go but she never would?\""
show tod surprised with dis
to "\"The strangest thing to me was that she always kept her fruits frozen.\""
to "\"So I know she has an icebox.\""
wi "\"You do?\""
show tod sigh with dis3
to "\"She used to make tarts.\""
to "\"The kind with frozen fruits.\""
show tod surprised with dis3
wi "\"Think real hard, Todd.\""
show tod annoyed with dis
wi "\"Where did she used to go before she’d make those desserts?\""
show tod talking with dis
to "\"Well, here, in the kitchen.\""
show tod with dis1
show tod talking with dis
to "\"But it was always Mr. Greene who’d get the fruit.\""
play sound "sfx/thud7.ogg"
show tod surprised
show sam surprised
"I jump in the air and listen." with vpunch
show sam
show tod annoyed
with dis
wi "\"These boards sound hollow to y’all?\""
stop sound
show tod talking with dis
to "\"They do.\""
show tod annoyed
show sam eyes
with dis
wi "\"Help me move the table.\""
hide tod
hide sam
with dissolve
play sound ("sfx/tablemove.ogg")
"All three of us give it a good shove, letting the dolls fall off as we move them."
"There’s a rug beneath the floor that matches the color of the wood pretty well."
stop sound
"I bend down and give it a tug."
show tod annoyed at right,sunset
show sam neutral -talking at left,sunset:
    xzoom -1
with dissolve
show tod talking with dis
to "\"Well, I’ll be...\""
show tod with dis1
show tod talking with dis
to "\"To think that was here the whole time?\""
show tod annoyed with dis
wi "\"I think we might have found where they keep the ice.\""
show tod talking with dis
to "\"Is it locked?\""
show tod annoyed with dis
show sam eyes -talking with dis
wi "\"Not securely.\""
show sam neutral -talking with dis
"I point at the hinges."
wi "\"Doesn’t look like the kind of lock designed to keep anybody out.\""
wi "\"More like the kind of lock that keeps you out long enough to get caught trying to break in.\""
play sound ("sfx/doorrattle.ogg")
"I shake the lock and chains to show off how noisy the setup is."
show tod surprised with dis
"Todd flinches."
stop sound
"I grab the hammer I saw under one of the counters earlier and hold it against a hinge."
wi "\"I think I have more than enough excuses to do this by now...\""
play sound ("sfx/bonebreak.ogg")
"The tops of the planks crunch as the hinges come off."
show tod surprised with dis
to "\"Well, wait, what if you don’t find an icebox down there?\""
show sam eyes -talking with dis
wi "\"Then I’ll make some repairs and issue my apology.\""
play sound ("sfx/bonebreak.ogg")
show sam neutral -talking with dis
"I position the hammer again, putting my body weight down on it until I hear the crunch."
play sound ("sfx/impact1.ogg")
"The trapdoor made of planks flips out easily from the top, rattling."
stop sound
wi "\"I guess Mr. Greene thought he was slick.\""
show tod sigh with dis
show sam annoyed -talking with dis
to "\"It worked on me.\""
"Yeah, that’s not that surprising."
show tod annoyed with dis
wi "\"Mostly because you don’t tend to expect something as eccentric as this from a banker.\""
scene black with dissolve
"We climb down an iron set of stairs that wobbles as we move beneath it."
"It’s dank and dirty down here."
"There’s plenty of cobwebs, and I’m sure I see a few things crawling around the floor out of the corners of my eye."
play sound ("sfx/stringswitch.ogg")
scene bg greenebasement with dis
"I see a dangling lightbulb and pull the string."
stop sound
"There’s not much down here but a tall, black chest, and a wooden crib, painted white."
show sam neutral -talking at halfright,basement1
show tod annoyed at right,basement1
with dissolve
show tod talking with dis
to "\"Well what’s somethin’ like that doing down here?\""
show tod annoyed with dis
"I slide my fingers along it, expecting to find grime or dust from being in storage."
wi "\"It’s clean.\""
"There’s a doll here too."
show tod sigh with dis3
to "\"This looks expensive.\""
show tod sad with dis
show sam eyes -talking with dis
$ update_unlocked_pages(1, 21)
$ renpy.notify("Notebook updated.")
wi "\"It’s definitely not like the other ones we’ve seen around the house.\""
show sam neutral -talking with dis
wi "\"What’s in the icebox, Todd?\""
show tod surprised with dis3
to "\"Well, ah...\""
to "\"Ice.\""
wi "\"And?\""
show tod sigh with dis3
to "\"Huckleberries.\""
show tod surprised with dis3
"I follow him to it."
"And he opens it."
"The ice box is separated into different sorts of shelves."
show tod sigh with dis3
to "\"Hey William?\""
wi "\"Yes Todd?\""
show tod annoyed with dis3
show sam eyes -talking with dis3
to "\"That really doesn’t look big enough to store a body.\""
"I can’t disagree with him here."
show sam neutral -talking with dis
"There’s far less down here than I would have expected."
"If Huxley had plans for this space, it looks like he never got down to them."
show sam neutral talking with dis
m "\"Is this another dead end?\""
show sam neutral -talking with dis
wi "\"I sure hope not.\""
"The two of them stare at me as if they’re waiting for what to do next."
wi "\"So... the crib and this doll...\""
show tod surprised with dis
wi "\"Todd, are you sure you never saw Marcy go down to the cellar?\""
show tod sigh with dis3
to "\"Cross my heart.\""
show tod annoyed with dis3
show sam annoyed -talking with dis3
wi "\"Huxley doesn’t mark me as a fellow who’d play with dolls.\""
show sam annoyed talking with dis
m "\"Hell no, he wouldn’t.\""
show sam annoyed -talking with dis
show tod sigh with dis
to "\"So why is this down here?\""
show tod annoyed with dis
wi "\"I might have a few ideas.\""
wi "\"But I think we’re out of time.\""
wi "\"Let’s put everything back where it was and get out of here as soon as possible.\""
"We climb up the stairs and head back to Marcy’s kitchen."
hide sam
hide tod
with dissolve
scene bg greenekitchen at sunset
show tod annoyed at right,sunset
show sam neutral -talking at left,sunset:
    xzoom-1
with dissolve
"We put the tablecloth back over the stairs and I double check to make sure all of the dolls are in their right spots."



scene bg greenecottage at sunset with dissolve
"Once we’re outside and Todd locks up the door, I tell them to start walking, so we can avoid being seen by Marcy on her way back."
scene bg black with dissolve
#adjust
scene bg deserttrail at sunset
show sam neutral at halfright,sunset
show tod annoyed at right,sunset
with dissolve
show tod surprised with dis
wi "\"Did you ever see Marcy pregnant, Todd?\""
to "\"Huh?\""
to "\"I think she might have been, once.\""
show tod sad with dis3
to "\"She lost the baby, though.\""
show tod surprised with dis3
wi "\"You sure it was just once?\""
"Todd doesn’t answer for a while."
show tod sigh with dis3
to "\"Twice.\""
show tod sad with dis
to "\"At least as far as I know.\""
show tod surprised with dis3
to "\"Why d’ya ask?\""
"I nod."
wi "\"I found some medicine in Marcy’s cabinet.\""
show sam eyes with dis
wi "\"The kind that prevents childbirth.\""
show sam neutral with dis
wi "\"The cabinet wasn’t locked, nor was it particularly hidden, which probably means Marcy was the one who put it there.\""
wi "\"It wasn’t local medicine, neither, so somebody probably gave it to her.\""
wi "\"Did y’all come across any stones that might look like they’re stacked over recently disturbed ground?\""
show sam eyes talking with dis
m "\"Not that I could see.\""
show sam neutral -talking with dis3
show tod sigh with dis3
to "\"Me neither.\""
show tod surprised with dis3
wi "\"If any of the pregnancies were late to term then Mr. or Mrs. Greene would have had to bury the evidence.\""
wi "\"There could be something in the house but the place is a wreck, and we have no time.\""
wi "\"If we can find out why Marcy was taking that medicine, then we might figure out the motive for why somebody wanted Mr. Greene gone.\""
show tod sigh with dis3
to "\"Now hang on William...\""
show tod annoyed with dis3
to "\"The way you’re talkin’ almost sounds like you’re saying Marcy did it.\""
show sam annoyed talking with dis
m "\"Ain’t she actin’ weird though?\""
show sam annoyed -talking with dis1
show sam annoyed talking with dis
m "\"Maybe she did have somethin’ to do with it.\""
show sam annoyed -talking with dis
wi "\"It’s certainly possible.\""
"Todd’s lips go a little thin as he shuts up with a snort."
show sam neutral with dis
wi "\"But that’s not the only lead I got.\""
wi "\"There was recent trash from a pack of gum and a film roll.\""
wi "\"I believe they only sell these at Red’s General Store.\""
wi "\"One of the workers there might know a thing or two about what was going on between Marcy and Huxley.\""
show tod talking with dis
to "\"Is that where we’re goin’ next then?\""
show tod annoyed with dis
wi "\"Frankly Todd?\""
show tod surprised with dis
wi "\"I think you should take the rest of the day off.\""
to "\"What do ya mean?\""
"I’m not sure how delicately I can put this."
wi "\"I can’t have you quite literally fuckin’ around on the clock.\""
wi "\"If you want to give a whore a handjob then just stay home.\""
"Todd’s cheeks flush red as a beet."
show tod sigh with dis3
to "\"Listen, um...\""
show tod sad with dis
to "\"I’m real, real sorry.\""
to "\"It won’t ever happen again.\""
wi "\"Not on the clock it won’t.\""
wi "\"What you do on your own time is your business.\""
show tod surprised with dis
to "\"So you ain’t gonna report what happened?\""
wi "\"Frankly, I should, were the consequences measured.\""
wi "\"But men have needs and it ain’t the rest of the world’s business.\""
show tod sad with dis3
wi "\"Don’t act stupid again, Todd. You alone should know better.\""
show sam smile with dis
"Samuel droops his eyelids at me and smirks."
m "\"So what about me?\""
"Little bit of anger wells up in my belly."
show sam annoyed with dis
wi "\"You’re a whore, Sam.\""
wi "\"You’ll never know better.\""
"He lets out a one-note laugh and mutters something under his breath."
wi "\"Take him back to the Hip and wash him up.\""
show tod surprised with dis
show sam surprised with dis
wi "\"I’ve got a feeling it’s gonna be a while.\""
hide sam
hide tod
with dis3
play sound ("sfx/gravelwalk.ogg")
"I leave them there standing awkwardly on the dirt road and I make the long trek back into town."
"Alone."
stop sound
"I probably shouldn’t have said that to Sam."
"But I can’t say he didn’t deserve it."
stop music fadeout 4.0

############## cut3.5



scene bg black with dissolve
"Once I leave the cloying smell of that house behind me, the tension in my shoulders loosens up."
play music ("music/quiet.ogg") fadein 1.0
scene bg generalexterior at sunset with dissolve
"The general store is probably closing up by now."
"I can usually find Mr. Byrnes and his son there after hours."
"As I walk on over I mull over the things I’m going to say, and how I’m going to approach this."
play sound ("sfx/softknock.ogg")
"I knock on the front door with the back of my wrist."
stop sound
show ral frown c at center,sunset with dis3
"Ralph greets me at the door."
show ral stoic c with dis3
ra "\"Don’t you know it’s closing time?\""
show ral frown c with dis3
wi "\"It’s the sheriff.\""
show ral angry c with dis
ra "\"And I don’t care if you’re George Albert the fifth.\""
show ral frown c with dis
ra "\"We’re tired.\""
ra "\"Come back tomorrow.\""
show mur concerned d at right,sunset with dis3
"I smell the scent of shoe polish and lemons before I see Murdoch Byrnes at the door, giving me a curious look."
"It’s probably better that he came to the door and not his father."
"He’s the one I work with most."
mu "\"William?\""
show ral stoic c with dis3
wi "\"Afternoon.\""
show mur sideeye with dis
mu "\"This is a bit of a bad time.\""
mu "\"We have our hands full.\""
"I can tell by the sheen of his neck that he’s had a long day."
"Somehow I doubt it was anything like mine though."
show mur concerned d with dis
wi "\"I’m afraid it’s urgent.\""
mu "\"How urgent?\""
show mur fear d with dis
show ral angry c with dis
wi "\"Urgent enough to make a few arrests if I have to.\""
"The rat glares at me and the fox’s eyebrows lift."
show mur concerned d with dis
wi "\"But I know you’re more reasonable than that.\""
wi "\"That urgent enough?\""
"Murdoch’s brow furrows in confusion."
show mur eyes talking with dis
mu "\"Fine, come in.\""
show mur concerned d with dis3
show ral stoic c with dis3
"The fox opens the door and the rat exhales."
scene bg generalinterior at sunset with dissolve
show ral stoic c at left,sunset
show mur concerned d at right,sunset
with dis3
wi "\"Take me somewhere we can talk where it’s just the two of us.\""
show mur sideeye with dis
mu "\"The darkroom will work for that.\""
show ral frown c with dis
"I feel Ralph’s eyes on me as Murdoch walks me to a dinky little closet and opens the door."
scene bg darkroom with dissolve
show mur concerned d at center,red with dis3
"It smells strongly of chemicals and him in here."
wi "\"Tell me where this is from?\""
"I pull out the cartridge I found on Marcy’s road."
show mur sideeye with dis
mu "\"That’s a Kodak film canister.\""
mu "\"The kind our store uses.\""
show mur concerned d with dis
wi "\"The kind your camera uses, right?\""
show mur eyes talking with dis
mu "\"Yes, but we have several.\""
show mur concerned d with dis
wi "\"Found it near Huxley Greene’s property in the woods by the road.\""
wi "\"Can’t recall them having many pictures, or a camera for that matter.\""
show mur sideeye with dis
mu "\"They’ve never purchased any photography, either.\""
show mur concerned d with dis
mu "\"At least not to my knowledge.\""
wi "\"Where were you the day of the poker game?\""
show mur eyes talking with dis
mu "\"I was at the store all day.\""
show mur concerned d with dis
mu "\"Then I ate supper by myself before going over to Mr. Tibbits’ apartment.\""
wi "\"You didn’t eat at home?\""
show mur sideeye with dis
mu "\"Not since it wasn’t a Sunday or a special occasion, no.\""
show mur concerned d with dis
"Based on when Jimmy had the gun, Huxley had to have it taken from him either past the afternoon of the riot, or any part of the day before the poker game."
"That’s not a long time for somebody to get killed and have their gun taken from them."
"I saw Murdoch most of Thursday."
"I didn’t see him at all on Friday before the poker game though."
"He’s clean, unless he’s lying."
"I have to wonder if that’s the case."
"Or if he’s covering for any of his family."
wi "\"So you didn’t see your parents on Friday night?\""
show mur sideeye with dis
mu "\"I didn’t.\""
wi "\"Or on Thursday, after all of the excitement?\""
mu "\"No.\""
show mur sad with dis3:
    xzoom -1
"He winces as he rolls his neck."
wi "\"How’s your shoulder?\""
mu "\"It stings still.\""
wi "\"You redressing it every day?\""
show mur fear d with dis3:
    xzoom 1
mu "\"Is there something you’re trying to get at with this?\""
mu "\"I thought you said this was urgent.\""
show mur concerned d with dis
wi "\"I needed somewhere nobody would listen.\""
show mur fear d with dis
mu "\"I don’t like being scared like that.\""
show mur concerned d with dis
wi "\"...I’m sorry.\""
wi "\"Today has been too much.\""
show mur eyes talking with dis
mu "\"You’re forgiven, then.\""
show mur concerned d with dis
wi "\"And I had to go through a lot to get this far.\""
wi "\"Who in your family drives the company carriage?\""
show mur eyes talking with dis
mu "\"Mostly my father.\""
show mur sideeye with dis
mu "\"Sometimes my mother.\""
show mur concerned d with dis
wi "\"How about your sisters?\""
show mur sideeye with dis
mu "\"Holly’s taken it on joyrides before, but she’s not supposed to.\""
show mur concerned d with dis
wi "\"Do you know where any of your family were on those two nights?\""
show mur sideeye with dis
mu "\"I have my guess, but no.\""
mu "\"Past six o’clock, my life is mine.\""
show mur concerned d with dis
mu "\"If I ran into them before all of that they’d have favors and chores for me, and I try keep that all to the workday.\""
show mur sideeye with dis
mu "\"Although...\""
wi "\"Don’t keep me waiting, fox.\""
show mur eyes talking with dis
mu "\"Cordelia Hendricks threw a party on Thursday night.\""
show mur sideeye with dis
mu "\"I saw the invitation.\""
show mur concerned d with dis
$ update_unlocked_pages(1, 22)
$ renpy.notify("Notebook updated.")
"Interesting."
"Is this all leading back to the Hendricks mansion?"
"Now I have to check in on that next."
"No doubt in my mind."
"Not looking forward to talking to that prick again so soon."
wi "\"Do you know who attended this party?\""
show mur eyes talking with dis
mu "\"My mother for sure.\""
show mur eyes with dis1
show mur eyes talking with dis
mu "\"Perhaps my father.\""
show mur sideeye with dis
mu "\"I’d have to ask my sisters if they did, though.\""
mu "\"I don’t know.\""
show mur concerned d with dis
wi "\"I have just a few more questions...\""
show mur shock with dis
grunk "\"If you have more questions, then you should be asking me.\""
show gre f frown at left,red with dissolve
label williamroute3b:
show gre f frown talking with dis
gr "\"The men have work to do at closing time.\""
show gre f frown with dis
show mur concerned d at center with dis
wi "\"I don’t mean to be intrudin’ on your family livelihood ma’am, but–\""
show gre f sq frown talking with dis
gr "\"Don’t you?\""
show gre f frown with dis1
show gre f frown talking with dis
show mur sad with dis3
gr "\"Pennies down the drain seem like the only recourse in this interrogation.\""
show gre f frown eyes with dis1
show gre f frown eyes talking with dis
gr "\"My son has work to do.\""
show gre f frown with dis
wi "\"Ma’am, if pennies are a concern I’ll line the tip jar once I’m through.\""
show gre f sq with dis
wi "\"There’s an urgent matter.\""
show gre f sq frown talking with dis
gr "\"I’m not a fan of how you seem to handle ‘urgent matters’.\""
show gre f sq with dis
"She’s just ignoring me."
show gre f sq talking with dis
gr "\"My boy has work to do.\""
show gre f sq with dis1
show gre f sq frown talking with dis

gr "\"Work that won’t get him shot.\""
show gre f with dis
show mur fear d with dis3
wi "\"Ma’am, I am investigating the murder of Huxley Greene.\""
show gre a down with dis3
"Her eyebrows rise."
$ update_unlocked_pages(1, 23)
$ renpy.notify("Notebook updated.")
"Either she’s genuinely surprised, or she’s got a lot of experience practicing."
"Just peaches."
show gre a eyes talking with dis
gr "\"Can’t say I’m saddened by the news.\""
show gre a frown eyes with dis
show mur concerned d with dis
"I feel my ears perk up."
show gre f frown eyes with dis3
"I get that tingling sensation that violence is in the air."
"The kind that lets you know a fight is about to break out."
"It’s an unsettling sensation coming from somebody like her."
show gre f frown with dis
wi "\"And why’s that?\""
show gre f sq frown talking with dis
gr "\"I’m certain you know why.\""
show gre f sq with dis
wi "\"Refresh me.\""
show gre f frown eyes with dis
"She leans against one of the counters, crossing her legs as she balances on one foot."
"Her words are slow."
"Specific."
show gre f sq frown talking with dis
gr "\"The man was a drunk.\""
show gre f sq frown with dis1
show gre f sq frown talking with dis
gr "\"He gave Marcy bruises.\""
show gre f sq frown with dis1
show gre f sq frown talking with dis
gr "\"Spent all his earnings on booze.\""
show gre f sq frown with dis1
show gre f sq frown talking with dis
gr "\"Barely kept up the house.\""
show gre f frown eyes with dis1
show gre f frown eyes talking with dis
gr "\"Something was bound to happen, sooner or later.\""
show gre f frown eyes with dis
"I tuck my notebook into my pocket and scratch the back of my head."
show gre f sq with dis
wi "\"And what gave you that impression?\""
show gre f eyes with dis
"She shrugged."
show gre f eyes talking with dis
gr "\"Justice. Common sense. God’s grace.\""
show gre f sq frown with dis1
show gre f sq frown talking with dis
gr "\"I happen to have the belief that if you do enough wrong then something will come your way to right it.\""
show gre f sq grit with dis
gr "\"It’s too bad the law seldom does.\""
show gre f frown with dis
wi "\"Did you know this was going on?\""
show gre f frown talking with dis
gr "\"Practically all of the women in the damn town knew it was going on.\""
show gre f sq grit with dis
gr "\"Sheriff McKinney knew, but he’d never convicted him and his snooping only made things worse for Marcy.\""
show gre f frown eyes talking with dis
gr "\"You knew it was happening too, didn’t you?\""
show gre f frown with dis
wi "\"I suspected.\""
"The accusation in her voice isn’t entirely fair."
"The Greenes have lived on that patch of land since the founding of the town."
"There’s only so much an outsider can do against an insider without rolling up his sleeves and dragging her off to testify against her husband."
"And she was as terrified of being alone as she was terrified of being with him."
wi "\"Only confirmed it today.\""
show gre f frown eyes with dis
wi "\"It was much worse than I thought it might be.\""
show gre f frown eyes talking with dis
gr "\"I’m glad the reaper got to him first, slow as you were to act.\""
show gre f frown eyes with dis1
show gre f frown eyes talking with dis
gr "\"In the days of my father, society didn’t wait around for the right postage to arrive to protect their women.\""
show gre f frown with dis1
show gre f frown talking with dis
gr "\"The men without character wouldn’t be allowed near their daughters in the first place.\""
show gre f sq grit with dis
gr "\"They didn’t have to lock them up like mongrels who’d be set loose upon the world again after a perfunctory stretch of time.\""
show gre f frown talking with dis
gr "\"They’d send the problems out the front gate of the village with nothing but the clothes on their backs and tell them ‘good luck’.\""
show gre f sq frown with dis
wi "\"We have due process now, Ma’am.\""
show gre f sq frown talking with dis
gr "\"There’s that good old fixation on response instead of prevention.\""
show gre f sq grit with dis
gr "\"Due process means diddly squat to people with permanent injuries and bodies that don’t hold a soul anymore.\""
show gre f frown eyes talking with dis
gr "\"I can never quite decide if I was born too late to live among men of action, or too early for the much needed revision of the judicial process.\""
show gre f eyes with dis1
show gre f eyes talking with dis
gr "\"Marcy will be far better off without that devil darkening her doorway.\""
show gre f eyes with dis
show mur fear d with dis
wi "\"She might not make for much longer, the state she’s in.\""
show gre f frown with dis
"Gretchen Byrnes’ brow furrows deeply."
show gre f frown talking with dis
gr "\"And what’s that supposed to mean?\""
show gre f frown with dis
wi "\"I mean either she’s drugging herself, or somebody's doing it for her.\""
show gre a down with dis3
wi "\"Her house is a wreck.\""
wi "\"The bed she sleeps in is covered in rot and mildew.\""
"Her eyes widen and I see the airs about her slip away."
show gre a talking with dis
gr "\"Where is she now?\""
show gre a with dis
wi "\"Still at home as far as I know.\""
show gre a eyes with dis1
hide gre with dis3
#sfx?
"She struts out of the dark room, grabbing her coat on the door handle and walks away without looking at me."
show mur concerned d with dis
"I think about stopping her for a moment."
"She said plenty of suspicious things."
"But I mostly want space between me, her, and her son for now."

wi "\"Now that she’s gone, is there anything else you’d like to say?\""
show mur sideeye with dis
mu "\"I’m not hiding anything, Will.\""
mu "\"But if I were, my first step would to be to tamper with your evidence.\""
show mur concerned d with dis
mu "\"Has anybody done that lately?\""
show mur fear d with dis
wi "\"Your little weasel friend messed around my office.\""
"But so did Cynthia."
if  SW_Points > 2:
    "I could ask Sam what he saw."
else:
    "Then again, Sam was too."
show mur concerned d with dis
mu "\"So what? You think Cliff is up to something?\""
wi "\"Well, that’s for certain.\""
wi "\"Doesn’t mean he’s trying to mess with my progress, though.\""
"At least not on purpose."
show mur sideeye with dis
mu "\"That serious, huh?\""
show mur concerned d with dis
mu "\"What exactly has he done?\""
wi "\"All I know is his real name ain’t Cliff, and he was brought into town to work on a project for James.\""
show mur sideeye with dis
"The fox’s brow furrows."
mu "\"The first part is strange.\""
mu "\"But over half the town works for Mr. Hendricks.\""
show mur concerned d with dis
mu "\"Hardly surprising.\""
wi "\"Like I said.\""
wi "\"It’s suspicious, but hardly worth hounding him over.\""
wi "\"Doesn’t exactly mean I want to keep him too close either.\""
show mur fear d with dis
mu "\"Are you mad I invited him to poker night?\""
show mur concerned d with dis
wi "\"I’m a little more upset that you took a bullet for him.\""
show mur sideeye with dis
mu "\"I told you he was being followed.\""
mu "\"He could have died if I hadn’t done something.\""
wi "\"You don’t even know ‘im.\""
show mur concerned d with dis
mu "\"So what?\""
wi "\"The way you see it, you took a bullet for a stranger.\""
wi "\"The way I see it, my friend took a bullet for a stranger.\""
wi "\"See how that’s different?\""
show mur sad with dis3:
    xzoom-1
mu "\"When you put it that way... I guess.\""
wi "\"I wish you wouldn’t act like this ain’t a big deal.\""
wi "\"You ain’t out of the woods yet.\""
wi "\"If your shoulder gets infected, there’s no cutting it off or burning the sick away.\""
show mur eyes with dis3:
    xzoom 1
mu "\"Well, don’t get weepy on my account.\""
show mur talking with dis
mu "\"I’m cleaning and dressing it before and after work every day.\""
show mur smile with dis
wi "\"I bet you’d pay good money to see me cry.\""
show mur eyes with dis
"He snorts."
show mur talking with dis
mu "\"I doubt I could afford something so rare.\""
show mur smile with dis1
show mur talking with dis
mu "\"I’d also check outside to see if it was hailing.\""
show mur smile with dis
wi "\"Plenty of things make me want to cry.\""
show mur eyes with dis
wi "\"Have you met my deputy?\""
mu "\"Cliff complained about him too.\""
show mur mischief with dis
mu "\"That’s another thing you two have in common.\""
"I raise my finger at him."
wi "\"Don’t start.\""
show mur smile with dis
"He shrugs at me like he’s innocent."
show mur talking with dis
mu "\"I just figured if we’re all going out to the Stag tomorrow night you’d enjoy yourself better if you talked to everybody else more.\""
show mur smile with dis
wi "\"I talk to Nik and Sam plenty.\""
show mur angry with dis3
"He crosses his arms and gives me a look."
mu "\"They barely talk.\""
wi "\"So then it works for me.\""
show mur sideeye with dis3
"I feel the strain in my brow and the bristle at the back of my neck."
wi "\"To be honest, I don’t even know if that’s happening tomorrow.\""
show mur fear d with dis
mu "\"What?\""
show mur sideeye with dis
mu "\"Why not?\""
show mur concerned d with dis
wi "\"Because today was exhausting and bore little fruit.\""
wi "\"There’s too much that I have to do right now if I don’t want to lose my trail.\""
"I’ve had difficult challenges."
"Far more difficult."
"Just not here."
"And I know that Marcy and Huxley aren’t going to be the end of it."
"If I’ve gotten a little rusty I need to shake it off, and quick."
wi "\"Let’s get back to business.\""
wi "\"I have to ask you, Murdoch...\""
"I get out my notebook and show him the picture of a gum wrapper in my notebook."
wi "\"You sell this gum in the store, don’t you?\""
"I watch his expression while he looks."
"There’s a glimmer in his eye, but no facial tic or wrinkles."
"If he’s surprised to see it then I can’t tell."
show mur sideeye with dis
mu "\"We do.\""
show mur concerned d with dis
mu "\"It’s not cheap in bulk, but that’s the only way to get it.\""
wi "\"So it ain’t a stretch to say that you’re the only supplier downtown who sells this gum?\""
show mur sideeye with dis
mu "\"I suppose it isn’t.\""
wi "\"So who buys it?\""
show mur concerned d with dis
mu "\"Mostly just kids with enough pocket money.\""
wi "\"Who in the past week?\""
show mur sideeye with dis
"I can tell that he’s thinking."
show mur eyes talking with dis
stop music fadeout 3.0
mu "\"There was a wolf in a yellow dress and a headband.\""
show mur concerned d with dis
mu "\"You know her?\""
"Shit."
show mur fear d with dis
wi "\"I know where to find her.\""
play music ("music/contemplation.ogg") fadein 3.0
scene bg generalinterior with dissolve
"The cool air hits my face as I open the door."
"Murdoch says something as I leave but I can’t hear it."
"I’m too mad."
scene bg generalexterior at sunset with dissolve
"Every direction is pointing me to Hendricks’ manor."
"It’ll take me at least 20 minutes to walk there but there’s nothing on this earth or off of it that’s going to stop me from putting my feet in front of the other."
scene echobackalley at sunset with dissolve
"I can see that manor on the hilltop through the trees and the alleyways."
"But I stop, and lean against the shady side of the post office."
"I feel a rush to my head as I dig through my pockets for a cigarette."
"It’s 6:22 here, so it’s 8:22 there."
"I try to think about what I’m going to say."
"I’m scared for my ex-wife because of the chewing gum you made her buy?"
"I’d sound like a lunatic."
"But everything keeps leading back to James."
"Hattie’s new job."
"The party at the manor being held on the same day of Huxley’s disappearance."
"The body flung to a ditch from what had to be a fast-moving vehicle."
if  HARINT_Points == 1:
    "Harlan and the other half of CSCG wanting James gone."
    "Why?"
elif ETHINT_Points == 1:
    "He’s even convinced one of the prostitutes to betray their own."
else:
    "There’s gotta be more he’s done."

"He’s never at the center of the crimes committed in this town, but his name and his home keep getting brought up around them."
"He’s like a bug at a campfire."
"Flitting around, dive-bombing you so you can see him out of the corner of your eye, but he won’t dare buzz too close to the fire."
"So now the question is--why him?"
"Or, why his house?"
"Either he must be responsible..."
"Or there’s got to be a reason all of this is happening around him."
"So which is it?"
"Both?"
"That’s not the important question right now."
"{i}What am I going to say to give me enough time to snoop around in that mansion?{/i}"
"That’s the important one."
"There ought to be something in there that answers some of my questions."
"Shit."
"I’ve finished my cigarette already."
"Oh well."
scene deserttrail with dissolve
play background ("music/cicadas.ogg") fadein 2.5
play sound ("sfx/gravelwalk.ogg")
"What I need to say will come to me."
"It always does."
stop sound
"The sun beats down on the back of my neck as I climb the hill."
scene mansionexterior with dissolve
"A raccoon on the porch goes inside when he sees me."
#eilihere? probably not
"The wolf at the gate looks me up and down."
"So I do the same."
wi "\"I take it by your stares that you know who I am?\""
"Wolf" "\"Master Hendricks has been notified of your presence.\""
"He has a hard look to him."
"I crouch down on my knees, staring up at him."
"I toss a pebble."
"He doesn’t look."
"His eyes stare straight out into the desert horizon."
"They wander lonely roads and bone-picked fields."
"It’s as if he hasn’t had one challenging thought in years."
"There’s no complication whatsoever in what he has to do to protect his master."
"I’m looking at a living corpse who stares back and doesn’t see me."
"Sometimes the officers would get like that in the city, too."
"When you spend your life shambling on, you can forget how to stop."
show jam with dissolve
show jam talking with dis
stop music fadeout 6.0
jam "\"Is this a stakeout, Sheriff?\""
#sfx
show jam with dis
"The guard presses a button and the gate opens, letting James stand aside, swiveling on his walking stick."
show jam talking with dis
jam "\"You don’t seem like the sort to squat unless you had your paws on your pistol.\""
show jam with dis
wi "\"Everybody likes a little shade now and again, Mr. Hendricks.\""
show jam happy with dis
jam "\"There’s far more of it inside.\""
jam "\"Shall you come in?\""
show jam with dis
wi "\"That’s why I’m here.\""
show jam eyes with dis
jam "\"Good, good.\""
show jam annoyed with dis
"His face sours when he looks at my claws."
jam "\"No pebbles this time.\""
show jam neutral with dis
"I show him my hands to let him know that they’re clean."
stop background fadeout 2.5
scene mansionfoyer with fade
show jam at right with dis3
#sfx
play music ("music/acastle.ogg") fadein 3.0
"The raccoon opens the door for us, and I feel his gaze linger on the back of my head as we pass through the door."
counk "\"James, dear, who’s that at the door?\""
"The sweet voice of a grown woman calls from the doorway."
"But the head of a small ram pokes around the door frame."
noaunk "\"Papa, who’s this?\""
show jam happy with dis
jam "\"A very special guest, my bonny boy.\""
show jam with dis1
show jam talking with dis
jam "\"Go wait with your mother in the den.\""
show jam neutral with dis
noaunk "\"But is that an {i}automatic{/i} handgun he has?\""
show jam talking with dis
jam "\"Noah, if you please.\""
show jam neutral with dis
"The boy’s lip curls and his posture turns into a sulk as he disappears around the door again."
show jam happy with dis
jam "\"So very eager to end their childhoods early, boys.\""
show jam eyes with dis
jam "\"They’ll miss it when it’s gone.\""
show jam with dis
"He takes my hat and puts it on his coat rack, regarding me carefully."
show jam talking with dis
jam "\"Perhaps that’s a bit of a sore spot for you?\""
show jam with dis
"I can never tell if he’s trying to get under my skin or if he’s just stupid."
"I don’t really care which is true so I go with the funnier answer."
wi "\"I don’t speak for others, generally.\""
show jam eyes with dis
jam "\"Of course, of course.\""
show jam happy with dis
jam "\"Assumptions make an ass out of us all, don’t they?\""
show jam neutral with dis
"The cheer in his voice drops."
jam "\"So which assumptions have led you here today?\""
wi "\"I’m here to talk to you about that list you dropped on me in your fancy automobile.\""
show jam surprised with dis
jam "\"You are?\""
show jam happy with dis
"He sounds pleasantly surprised."
"Good."
show jam eyes with dis
jam "\"One of the ones I’m watching closely is here today.\""
show jam with dis
wi "\"Oh is he now?\""
show jam talking with dis
jam "\"His lips are tight, but perhaps butter and honey can grease wheels better than oil.\""
show jam with dis
"That’s a malapropism."
wi "\"Okay.\""
show jam happy with dis
"James is still saying things but I’m too distracted to listen."
$renpy.sound.set_volume(0.3, delay=5.0, channel='music')
"The grand entrance of their foyer shows off a massive painting of an older Ram looking down at us."
show jam neutral with dis
"It’s positioned low enough to the ground that it gives me pause."
wi "\"Before we move on, tell me a bit about that painting.\""
show jam with dis
"He looks up and smiles."
show jam talking with dis
jam "\"That painting?\""
show jam with dis
wi "\"Yeah.\""
show jam talking with dis
jam "\"Well, he’s the true lord of the manor.\""
show jam eyes with dis
jam "\"That’s my grandfather.\""
show jam with dis
"Oh."
"Him."
"I’ve heard a lot about him."
"But not from James."
wi "\"So what was he like?\""
show jam talking with dis
jam "\"Determined. Persistent.\""
show jam happy with dis
jam "\"My mother said that he was the most charming man in our family.\""
show jam with dis1
show jam talking with dis
jam "\"Hardly surprising, considering you’d {i}have{/i} to be to get this many people to pack up their things and live here out in the middle of the desert in the first place.\""
show jam with dis
"I squint, staring a little more at the painting."
wi "\"Oh yeah?\""
wi "\"Tell me more.\""
show jam talking with dis
jam "\"There’s a lot to tell.\""
show jam with dis1
show jam talking with dis
jam "\"You know, we wouldn’t be standing here if it weren’t for him.\""
show jam with dis1
show jam talking with dis
jam "\"He and a business partner scouted the wilderness for months before they struck gold at the first site, which would become the CSCG mining operation.\""
show jam with dis
wi "\"Business partner?\""
wi "\"Was that Briggs’ father?\""
show jam happy with dis
jam "\"No, no, Briggs was just a pup when he worked under my father.\""
show jam with dis1
show jam talking with dis
jam "\"Alas, he did not know my grandfather.\""
show jam with dis
"Most paintings have a gap in their frames."
"That one looks welded to the wall."
wi "\"So what can you tell me about his original business partner?\""
#sfx
"I start climbing the stairs."
show jam eyes with dis
jam "\"Well, he’s not very important.\""
show jam neutral with dis
"He clears he throat loudly enough for me to turn around."
show jam talking with dis
$renpy.sound.set_volume(1.0, delay=3.0, channel='music')
jam "\"This way, Sheriff.\""
show jam neutral with dis
"I bite the inside of my cheek."
"I want to get a closer look at that painting."


scene bg mansionlivingroom with fade
show jam at right with dissolve
play background ("sfx/bonfire.ogg")
"He directs me down the right hall, which leads into a richly decorated parlor."
"It smells like lemon, huckleberries, earl grey and honey cakes."
"I get a quick look around the room."
"The child from the hallway is poking at logs in the fire place with a red iron poker."
"But then I see somebody I didn’t expect to see here."
show mrs eyes at left:
    xzoom-1
show nik sad behind jam
with dis3
"It’s Nikolai, who looks very uncomfortable, stuffed into a wicker basket chair, holding a very fine teacup in one hand."
"A well-dressed ewe, who I can only assume is Mrs. Hendricks, is reading a book on her wicker basket lounge."
show mrs shocked with dis
"She puts the book down when we enter the room and stands up."
show mrs xtr shocked with dis
mrs "\"Oh my goodness gracious is that the sheriff?\""
show mrs wtf with dis
"The boy shuffles sideways, pretending not to look at me, but his eyes are on my gun holster."
show nik neutral flaccid hoff with dis3
"Nik turns slowly to see me."
"He looks almost grateful."
show mrs xtr shocked with dis
mrs "\"I do hope we’ve not done anything wrong?\""
show mrs wtf with dis
"That remains to be seen."
show mrs with dis
wi "\"I’m just here to talk some business over with Mr. Hendricks.\""
wi "\"You keep a very lovely home.\""
show mrs giggle with dis
mrs "\"Oh please, sir, I’m just an amateur decorator!\""
show mrs eyes with dis1
show mrs eyes talking with dis
mrs "\"The real credit should go to our principled and fastidious staff.\""
show mrs eyes with dis1
show mrs giggle with dis
mrs "\"Please, come sit with us!\""
show nik sidelook with dis3
ni "\"Yes, come join us for tea William.\""
show mrs with dis
"This is really fuckin’ weird."
"James points in between myself and the badger."
show jam eyes with dis
jam "\"The two of you know one another, yes?\""
show jam with dis
wi "\"It’s part of my job to know most people.\""
show jam happy with dis
jam "\"You can drop the rough and tumble act.\""
jam "\"Even a man as sullen as yourself who’s married to duty has to have friends.\""
show jam with dis
"I feel my hand slip into my pocket for a cigarette out of habit but stop myself."
wi "\"Yes.\""
wi "\"Nik is a friend of mine.\""
show jam eyes with dis
jam "\"I would like to think of Nicholas as a friend of mine too.\""
show nik surprised with dis3
"Nik gives me a sidelook telling me this is absolutely not the case."
"Not that I would have needed a confirmation."
show jam with dis3
show nik sidelook with dis3
show mrs giggle with dis3
mrs "\"Aww, well that’s just so sweet!\""
show mrs with dis1
show mrs talking with dis
mrs "\"It can be really hard for James to make friends out here, what with the awkwardness that comes from the nature of my husband’s work.\""
show mrs with dis
"She means the fact that almost everybody works under him."
show jam talking with dis
jam "\"Well that’s not entirely true.\""
show jam with dis
show mrs shocked with dis
mrs "\"Oh, please do forgive me if I misspoke!\""
show mrs with dis
"She seems nice, but my mind isn’t really a part of this conversation."
"I’m thinking about why Nik is here, and when I’m going to have the opportunity ask him about it."
"I think it should happen before I go."
"I look around the room to see if there are any clues."
"Nik’s clothes look clean, which means he probably didn’t go to work today."
"James’ eyes are on me, naturally, so I don’t make any sudden glances."


"On the coffee table I notice a replica of the house made out of cardboard."
"The front is the very familiar facade of a federalist plantation style home."
"But the back extrudes much farther than expected."
"There are wings, and turns, and what looks to be a center room with what’s meant to be a glass roof."

wi "\"Who built the cardboard model?\""
show mrs eyes talking with dis
mrs "\"Oh, I’d call that thing more of an endeavor than a model.\""
show mrs with dis
show jam talking with dis
jam "\"Quite so.\""
show jam with dis
wi "\"What do y’all mean by that?\""
show jam talking with dis
jam "\"This is my attempt at scaling the house.\""
show jam with dis
"I cock my brow at the both of them."
wi "\"Make it simple for me.\""
show jam eyes with dis
jam "\"My grandfather, the original architect of this house, had many planned renovations that he never entreated to share.\""
show jam with dis
"Goddamn."
"So they have so much room up on this hill that they’ve gone and lost track of it."
wi "\"You mean he didn’t leave floor plans of his own house to y’all?\""
show jam neutral with dis
jam "\"If he did, he lost them.\""
show mrs eyes with dis
"Mrs. Hendricks makes a noise while sipping her tea and shaking her finger."
#sfx?
"She puts the cup down, wipes her mouth with a kerchief, and then speaks up."
show mrs talking with dis
mrs "\"But I have a theory that he had no interest in sharing them.\""
show mrs with dis
show jam talking with dis
jam "\"Well he had a great deal of interest in antiquity, but an even greater interest in the late medieval period.\""
show jam with dis
wi "\"You don’t say.\""
show jam eyes with dis
jam "\"Take the outside of our house for instance.\""
show jam talking with dis
jam "\"The exterior belies a homey manor, but the bones are something else entirely.\""
show jam with dis
show mrs shocked with dis
mrs "\"There are doors to nowhere.\""
show mrs with dis
show jam neutral with dis
jam "\"Or more like they were clearly doors to somewhere, but that somewhere never got to be built.\""
show jam talking with dis
jam "\"My grandfather didn’t want a manor. He wanted a citadel.\""
show jam neutral with dis
wi "\"So what do you want?\""
show jam talking with dis
jam "\"Me?\""
show jam neutral with dis
wi "\"Do you plan to take up his work?\""
show jam happy with dis
jam "\"I’ve already started plans, hence the maquette.\""
show jam with dis1
show jam talking with dis
jam "\"But what’s most interesting to me is how committed he was to his heritage.\""
show jam with dis1
show jam talking with dis
jam "\"My grandfather grew up experiencing a country full of green hills with expanding ruins.\""
show jam with dis1
show jam talking with dis
jam "\"He was a lord without a castle, until he came to this country, and he started to build.\""
show jam eyes with dis
jam "\"His vision is certainly unfinished, and I don’t need any floor plans to confirm that.\""
show jam with dis
"There’s a lot of convenient deniability in his story."
"If something were occurring in his house he could claim he didn’t know about it."
"What makes me nervous is that I don’t entirely think he’s lying to me."
"This place is huge, and according to the town records, it was huge before his birth."
"Who knows what he’s added or removed to the interior?"
show mrs shocked with dis
mrs "\"The problem with big houses is that they were meant for big company.\""
show mrs with dis
show jam happy with dis
jam "\"I feel we have plenty of regular company, wife.\""
show jam neutral with dis
show mrs eyes talking with dis
mrs "\"Don’t you wife me.\""
show mrs eyes with dis
"She crosses her hooves and clasps them to her bosom."
show jam with dis
show mrs talking with dis
mrs "\"I just meant to say that most of my family still lives out east, and they’re very close to James.\""
show mrs shocked with dis
mrs "\"It would take them a week just to travel and see me.\""
show mrs wtf with dis1
show mrs shocked with dis
mrs "\"The only time we get to see them is late August when we go off to see the coast.\""
show mrs giggle with dis
mrs "\"But Mr. Krol is such the perfect gentleman that I should love it if he kept coming back.\""
show mrs eyes with dis
show nik eyestalking with dis3
ni "\"Thank you Mrs. Hendricks.\""
show mrs laugh with dis
show nik neutral flaccid hoff with dis
mrs "\"Please, call me Cordelia.\""
show mrs with dis1
show nik sidelook with dis3
"So she’s lonely then?"
"Lonely people love to talk."
"Good."
"This is my chance."
"I have to lay this on thick, but not come across desperate."
"My chances will reveal themselves in the pauses."
stop music fadeout 5.0
show mrs wtf with dis
wi "\"Ma’am, I’m afraid I have a terrible confession to make.\""
show mrs shocked with dis
mrs "\"A confession?\""
show mrs wtf with dis
show nik neutral flaccid hoff with dis3
show jam neutral with dis3
"Nik and James turn to me and give me looks as if they want to know what's going on through my head and what I’m going to say next."
show jam with dis
wi "\"First let me start by saying that before coming to Echo I worked with the BOI as a detective.\""
wi "\"Most of my cases pertained to stalkers and agents of foreign interference.\""
wi "\"But corruption at home became my priority when I caught on to the activities of the son of one of the city’s biggest mafiosos by sticking my nose where it didn’t belong.\""
wi "\"His name was Phillip Momo Antonelli, but he liked to call himself Big Momo, after his granddaddy.\""
wi "\"In spite of his criminal acts, he was well-liked.\""
"I give James a look to make sure he’s paying attention to that."
"But he’s just listening patiently, wearing the false smirk of a soda jerk."
wi "\"Antonelli was a deeply religious man.\""
wi "\"Most are in those circles, as paradoxical as it may seem.\""
wi "\"But part of what made him so hard to catch wasn’t just his pristine reputation-- it was that he rarely conducted his crimes himself.\""
wi "\"He always had an ironclad alibi.\""
wi "\"His orders of these violent crimes couldn’t be linked to any of the outfits loyal to him.\""
wi "\"But funny enough...\""
"I look around to make sure if the rest of the room is listening."
wi "\"He always left something behind for me to look for.\""
wi "\"In his case, that something was handwritten notes carried in several copies of identical looking suitcases through the L-Train in broad daylight.\""
show mrs shocked with dis
mrs "\"What’s the L-train?\""
show mrs wtf with dis
wi "\"The jewel of the city.\""
show jam talking with dis
jam "\"It’s just a rail train that rides above the street.\""
show jam with dis
show mrs giggle with dis
mrs "\"Oh, how lovely!\""
show mrs eyes with dis1
show mrs giggle with dis
mrs "\"Could we ride it one day?\""
show mrs with dis
show jam eyes with dis
jam "\"I doubt it will run for much longer.\""
show jam talking with dis
jam "\"Once everybody has access to automobiles, trains will belong in the past just as well as the other elements of antiquity.\""
show jam with dis
wi "\"Back to what I was sayin’.\""
"I can hear the impatience in my own voice, but soften it."
wi "\"His use of the L-train made sense because every crime conducted happened within a block of the railway, and during service hours.\""
wi "\"I started riding at prime times and saw the suitcase transfers before the crimes occured.\""
wi "\"I didn’t even know anything about this man by the time I caught him.\""
wi "\"But once I did, every part of society all around me started falling like a stack of cards.\""
wi "\"People affiliated with Antonelli got busted left and right.\""
wi "\"This included some of our own on the police force, who’d later come to hate my guts.\""
wi "\"My testimony and the evidence that I gathered put a lot of important people away-- not just Antonelli.\""
wi "\"A whole lot of folks didn’t like me too much after that.\""
show mrs shocked with dis
wi "\"I lost parts of my ear following an ambush, and my wife at the time lived in fear whenever we went outside after dark.\""
show mrs wtf with dis
wi "\"If I knew that’s what would have happened to us even after Big Momo got arrested, then maybe I could have ignored those suitcases.\""
wi "\"But I might have gone crazy never knowing who was doing these terrible crimes to my friends and my city when I knew I had the skills to find out.\""
show jam talking with dis
jam "\"But why bring this all up now?\""
show jam neutral with dis
wi "\"Because I can’t shake the notion that there’s organized crime in Echo as well.\""
"I sit up again to make sure every last person in the room is hanging onto the edge of my next words."
show mrs shocked with dis
wi "\"Part of the reason that I’m here is because I’m investigating a series of terrible crimes, and I think I need the help of you folks to get anywhere.\""
show mrs wtf with dis
noa "\"Did you say terrible crimes?\""
"This is the first time I hear his son say anything in this room."
"He’s lying on his belly, legs behind him, kicking as he watches me with his head in his hands."
"I give him a quick wink."
wi "\"Awful ones.\""
show jam talking with dis
jam "\"Enough of this--\""
show jam neutral with dis
show mrs xtr shocked with dis
mrs "\"Please, husband, let him speak!\""
stop music fadeout 5.0
show mrs wtf with dis
"...And those are the words that I needed to hear to know that I’d have free reign over this mansion."
"A wave of relief washes over me."
show jam talking with dis
jam "\"Well it’s not like I’m putting a muzzle over him.\""
show mrs eyes with dis
show jam with dis
"She tsks at him gently."
play music ("music/quiet.ogg") fadein 2.0
show jam neutral with dis
show mrs eyes talking with dis
mrs "\"We can all hear your tone, James.\""
show jam talking with dis
show mrs with dis
jam "\"Well let’s not go overboard--\""
show jam neutral with dis1
show jam talking with dis
jam "\"Who might we suspect he’s talking about?\""
show jam neutral with dis1
show jam talking with dis
jam "\"If there’s anybody to point a finger at it should be the picketers!\""
show jam angry with dis
show mrs wtf with dis
jam "\"That’s why I wanted you to nip this in the bud days ago you stubborn coyote!\""
show nik eyes with dis
show jam surprised with dis
ni "\"Boo.\""
show nik neutral flaccid hoff with dis
"James flinches as if remembering that Nikolai is still in the room."
show jam annoyed with dis
jam "\"Oh, come now!\""
show mrs with dis
show jam talking with dis
jam "\"That wasn’t lobbed at you.\""
show jam happy with dis
jam "\"I know a demure giant when I see one.\""
show jam with dis
show nik eyes with dis
"Nikolai puts his hands in his pockets."
"Knowing his habits, his fists are balled."
play sound ("sfx/doorslam.ogg")
show mrs shocked
show jam surprised
show nik surprised
with vpunch
"There’s a sudden slam on the door."
stop sound
show nik neutral flaccid hoff with dis
show mrs wtf with dis
"It’s enough to make Noah sit up and Mrs. Hendricks cover her mouth."
show jam neutral with dis
"James looks confused for a moment and then looks at his watch."
show jam annoyed with dis
jam "\"Oh, for the love of--\""
show jam neutral with dis
"He looks between all of us."
show jam talking with dis
show mrs with dis
jam "\"I have to take somebody in my office at the moment.\""
show jam neutral with dis1
show jam talking with dis
jam "\"Please excuse my absence. I doubt it will be brief.\""
show jam neutral with dis1
hide jam with dis3
"He walks stiffly to the hall and out of sight."
show nik surprised with dis
jam "\"Good evening Briggs.\""
show nik sad with dis3
show mrs wtf with dis3
"Nikolai stands, putting his teacup down on the coffee table."
"He shuffles away from the doors and the halls until he hears the footsteps of the two men disappear out the door."
show mrs shocked with dis
mrs "\"Are you alright Mr. Krol?\""
show nik sidelook with dis3
show mrs with dis3
ni "\"Shyness.\""
"It’s the most bold faced lie he’s ever told."
show mrs eyes talking with dis
mrs "\"Well it’s been an excitable day, hasn’t it?\""
show mrs with dis3
show nik neutral flaccid hoff with dis3
wi "\"Could I ask Mr. Krol a few questions in private?\""
show mrs shocked with dis
mrs "\"Didn’t you want to look around the house?\""
show mrs eyes talking with dis
mrs "\"Please feel free to roam the house, and ask the staff what you like.\""
show mrs with dis

menu willinvestigation2:
    "Where am I going [investigorder]?"
    "The portrait." if willmanorportrait1 == False:
        wi "\"Mrs Hendricks, you said that there are all sorts of doorways to nowhere in this house, correct?\""
        show mrs talking with dis
        mrs "\"Well I believe so?\""
        show mrs with dis
        wi "\"You don’t sound very sure.\""
        show mrs talking with dis
        mrs "\"Well some of the doors lead to passages that the servants use.\""
        show mrs with dis1
        show mrs talking with dis
        mrs "\"Elmer, the butler, would know about that, but I’m afraid we don’t speak so often.\""
        show mrs wtf with dis1
        show mrs shocked with dis
        mrs "\"But I try not to get in the way of the servants, and after dark, the mansion gets too strange for my liking.\""
        show mrs wtf with dis
        wi "\"Strange how?\""
        show mrs shocked with dis
        mrs "\"Well,{nw}"
        show nik sidelook with dis3
        extend " there’s voices of people I’ve never heard before.\""
        show mrs wtf with dis1
        show mrs shocked with dis
        mrs "\"And there’s noises that I’ve never heard before at any other place and time.\""
        show mrs wtf with dis
        wi "\"What kinds of noises?\""
        show mrs shocked with dis
        mrs "\"Sometimes it’s like quick, scratchy scrambling...\""
        show mrs wtf with dis1
        show mrs shocked with dis
        mrs "\"Sometimes it sounds more like noises coming from a machine.\""
        show mrs wtf with dis1
        show mrs shocked with dis
        mrs "\"But nothing about the noises ever strikes me as natural.\""
        show mrs wtf with dis
        wi "\"Have you ever considered that there might be passages the architect put in place that he didn’t want to find?\""
        wi "\"Maybe rooms only accessible at certain times of the day?\""
        wi "\"Or rooms that won’t open properly if you don’t turn a wench or flip a lever?\""
        show mrs with dis
        "She tilts her head."
        show mrs eyes talking with dis
        mrs "\"Well I suppose that’s possible?\""
        show mrs with dis
        wi "\"I have my suspicions about a certain location.\""
        show mrs xtr shocked with dis
        mrs "\"Do be careful!\""
        show mrs wtf with dis1
        show mrs shocked with dis
        mrs "\"I wouldn’t want you to run into any traps if you poke around too aggressively.\""
        show mrs wtf with dis
        wi "\"There are traps in this house?\""
        show mrs shocked with dis
        mrs "\"Mostly harmless ones.\""
        show mrs wtf with dis
        mrs "\"I think.\""
        show mrs wtf with dis1
        show mrs shocked with dis
        mrs "\"One of the doors out in the garden opens to a series of smaller doors, and then a mirror you have to crouch down to see.\""
        show mrs wtf with dis1
        show mrs shocked with dis
        mrs "\"Another time I used a dumbwaiter that was hiding behind a book case.\""
        show mrs wtf with dis1
        show mrs shocked with dis
        show nik surprised with dis3
        mrs "\"When I opened it a lead ball fell out and left a dent in the wooden floor.\""
        show mrs wtf with dis1
        show mrs shocked with dis
        mrs "\"We had to replace that part of the floor.\""
        show mrs wtf with dis
        "That doesn’t sound harmless to me."
        show mrs with dis
        show nik neutral flaccid hoff with dis
        wi "\"Thanks for the warnings.\""
        show mrs giggle with dis
        mrs "\"Of course!\""
        show mrs with dis
        show nik talking with dis
        ni "\"I can lend some assistance.\""
        show nik eyes with dis
        wi "\"I think that would be a good idea.\""
        stop background fadeout 1.0
        scene mansionfoyer with fade
        show nik neutral flaccid hoff at right with dis3
        "Nik follows me to the foyer and keeps his voice low until we get a good distance away from the hall and start to climb the stairs."
        "I feel a lot more relaxed being alone with him, but not relaxed enough to feel at ease in this house."
        wi "\"It’s good to have you watch my back, Nik.\""
        show nik eyestalking with dis
        ni "\"The feeling is mutual.\""
        show nik neutral flaccid hoff with dis
        wi "\"So what are you actually doing here?\""
        show nik sidelook with dis3
        ni "\"I was invited.\""
        ni "\"That was the truth.\""
        show nik neutral flaccid hoff with dis3
        wi "\"Don’t you think your friends down at the mine will have a problem with that?\""
        show nik talking with dis
        ni "\"On the contrary, they encouraged it.\""
        show nik neutral flaccid hoff with dis1
        show nik talking with dis
        ni "\"The whole point of our movement is to keep negotiations open.\""
        show nik disappointed with dis3
        ni "\"But it is not like I could have told him no even if they didn’t approve.\""
        ni "\"He is my boss.\""
        "I exhale."
        show nik neutral flaccid hoff with dis3
        wi "\"I get it.\""
        show nik sidelook with dis3
        ni "\"But the union isn’t why he’s interested in me.\""
        "Huh."
        wi "\"Is that so?\""
        show nik disappointed with dis3
        ni "\"I’m certain.\""
        show nik neutral flaccid hoff with dis3
        wi "\"If not that, then what.\""
        show nik talking with dis
        ni "\"What he is interested in is Samuel.\""
        show nik surprised with dis
        "I inhale a bit of my own spit, then start coughing."
        wi "\"Sam?\""
        "I sputter a bit and Nik hits my back a few times with the back of his palm."
        ni "\"Are you alright?\""
        show nik neutral flaccid hoff with dis
        wi "\"Let’s not change the subject.\""
        wi "\"What does he want with Sam?\""
        wi "\"Sam’s not important, he’s just Sam.\""
        show nik sidelook with dis3
        ni "\"I know.\""
        ni "\"You do not have to raise your voice at me about that.\""
        wi "\"I wasn’t raising it at {i}you{/i}, I was--\""
        wi "\"Forget it.\""
        show nik sad with dis3
        "He shifts his weight from one foot to the other, uncomfortable-like."
        ni "\"Anyway...\""
        ni "\"I have never told another soul besides you and one other friend about my visits with Sam.\""
        ni "\"But somehow, he knows.\""
        show nik eyestalking with dis3
        ni "\"He has asked me a good number of details about Sam’s habits and preferences.\""
        show nik neutral flaccid hoff with dis1
        show nik talking with dis
        ni "\"He wants to invite us both to luxurious distractions and lavish meals.\""
        show nik sidelook with dis3
        ni "\"I do not think he knows that he’s spending more time with you lately than me yet.\""
        wi "\"Well isn’t that partly your fault?\""
        show nik neutral flaccid hoff with dis3
        "He grits his teeth."
        show nik eyestalking with dis
        ni "\"I am not going to talk about this now.\""
        show nik neutral flaccid hoff with dis
        wi "\"Well good, because I’m not the one you need to talk about it with.\""
        "He already has Hattie and Andy wrapped around his finger."
        if SW_Points > 1:
            "If he finds out how much time I’m spending with Sam, then I bet he’ll try to control Sam because he thinks he’ll be able to control me."
            "Then he’ll be able to get away with anything."
        else:
            "Does he really think I won’t be able to help them?"
        "I really hate this man."
        wi "\"Well he won’t be getting any tea parties out of me.\""
        show nik sidelook with dis3
        ni "\"Yet here you are.\""
        show nik smile with dis3
        ni "\"Shall I go grab you a macaroon?\""
        wi "\"I’d rather guzzle piss.\""
        show nik talking with dis
        ni "\"Don’t you drink instant coffee?\""
        show nik eyessmile with dis
        ni "\"That is already piss.\""
        show nik smile with dis
        wi "\"I’ll drink whatever wakes me up so long as it isn’t out of one of his teapots.\""
        ni "\"As long as you admit you are a piss drinker.\""
        wi "\"Isn’t tea too rich for your blood anyway?\""
        show nik eyestalking with dis
        ni "\"Not when you are friends with Huaxians.\""
        show nik neutral flaccid hoff with dis
        wi "\"I need something quick and strong.\""
        show nik smile with dis
        ni "\"Also like piss.\""
        wi "\"Let’s stop talking about piss, Nik.\""
        show nik eyessmile with dis
        ni "\"You’re the one who started it.\""
        show nik smile with dis
        wi "\"Anyway...\""
        "We reach the top of the stairs."
        show nik neutral flaccid hoff with dis
        play sound ("sfx/hollowknock.ogg")
        "I knock on the wood next to the painting as hard as I can without making a dent."
        "At least not a big dent."
        stop sound
        "There’s a deep, vacuous sound."
        wi "\"Y’hear that?\""
        show nik sidelook with dis3
        ni "\"Yeah.\""
        $ portraittext = "The Hendricks house has hollow walls that the owners claim not to understand, entirely. The painting at the top of the stairs in the foyer has hinges."
        if willmanorkitchen1 == False:
            $ unlocked_journal_pages += 1
        $ current_journal_page = 24
        $ renpy.notify("Notebook updated.")
        show nik neutral flaccid hoff with dis3
        wi "\"The walls directly behind this are hollow.\""
        wi "\"And you look closely at the gold and black paint on the side of the frame, there’s hinges.\""
        show nik talking with dis
        ni "\"The painting opens?\""
        show nik neutral flaccid hoff with dis
        wi "\"Yeah, but I’m not sure how or when.\""
        show nik talking with dis
        ni "\"What do you mean, when?\""
        show nik neutral flaccid hoff with dis
        wi "\"Some buildings can have clockwork mechanisms to make doors passages useable at only certain times of day, or under certain conditions.\""
        show nik talking with dis
        ni "\"Do you think that’s the case?\""
        show nik neutral flaccid hoff with dis
        wi "\"Can’t say for sure, but I think it’s unlikely.\""
        wi "\"Systems like that are generally noisy and need to be maintained.\""
        wi "\"If they’re truthful about not understanding the house, which is yet to be proven, by the way, then a mechanism like that would have broken a long time ago.\""
        wi "\"There’s probably a more simple way to open it.\""
        wi "\"Might only work on one side, or have a hidden switch somewhere.\""
        show nik talking with dis
        ni "\"Are you going to try to open it?\""
        show nik neutral flaccid hoff with dis
        wi "\"I don’t think there’s time to poke around like that.\""
        wi "\"I want a general overview of the mansion before I fiddle with any potentially dangerous bits.\""
        wi "\"Let’s go back to the living room for now.\""
        show nik eyestalking with dis
        ni "\"Okay.\""
        show nik neutral flaccid hoff with dis1
        scene bg mansionlivingroom with fade
        play background ("sfx/bonfire.ogg")
        show nik
        show mrs eyes at left:
            xzoom-1
        with dis3
        "Mrs. Hendricks is still there, flipping cards on the coffee table."
        show mrs talking with dis
        mrs "\"Back so soon?\""
        show mrs with dis
        wi "\"Briefly.\""
        "Now where else is most important to check?"
        "I’ve got a bad feeling that I don’t have a whole lot of time."
        $ investigorder = "next"
        $ willmanorportrait1 = True
        if willmanorlivingroom1 == False or willmanorkitchen1 == False:
            jump willinvestigation2
        else:
            jump postwillinvestigation2

    "The kitchen." if willmanorkitchen1 == False:
        wi "\"Ah, Mrs. Hendricks?\""
        show mrs talking with dis
        mrs "\"Yes Sheriff?\""
        show mrs with dis
        wi "\"I was told you have a new in-house chef for hire.\""
        show mrs giggle with dis
        mrs "\"Oh yes, Hattie’s phenomenal!\""
        show mrs eyes with dis
        wi "\"Would she be in the kitchen, then?\""
        show mrs eyes talking with dis
        mrs "\"Well, I should say so?\""
        show mrs with dis1
        show mrs talking with dis
        mrs "\"She usually makes dinner about this time.\""
        show mrs with dis
        wi "\"Right then.\""
        wi "\"I’d like to ask a few questions.\""
        show mrs eyes talking with dis
        mrs "\"Just follow along the hall and you’ll eventually come to the kitchen.\""
        show mrs with dis
        show nik eyestalking with dis
        ni "\"I can go with you.\""
        show nik neutral flaccid hoff with dis
        "I give him a look, and he seems to know what’s on my mind."
        wi "\"Thanks, but I want to do this alone.\""
        show nik sidelook with dis3
        ni "\"Ah.\""
        ni "\"I understand.\""
        wi "\"Thanks.\""
        show nik neutral flaccid hoff with dis3
        show mrs giggle with dis3
        mrs "\"I have a story I can tell you while we wait Mr. Krol.\""
        show mrs with dis
        show nik talking with dis3
        ni "\"Oh?\""
        show nik neutral flaccid hoff with dis
        show mrs eyes talking with dis
        mrs "\"Mhm. About my home. My old home.\""
        show mrs eyes with dis1
        stop background fadeout 1.0
        scene mansionfoyer with fade
        stop music fadeout 4.0
        "Their voices fade as I go further into the hallway, taking turns, passing parlor rooms and the entrance to the cellar."
        "I smell the kitchen before I see it."
        "Brown butter scents mixing with onions and peppers."
        scene mansionkitchen
        show hat eyes at right:
            xzoom-1
        with fade
        play background ("sfx/chopping.ogg") fadein 3.0
        "The hallway leads to the open entrance of the kitchen and I see her there, back turned to me and chopping vegetables."
        "I stop, because I feel cold."
        "There’s a familiar sense of danger that crawls up my spine as I see her chop vegetables just like how she used to."
        stop background fadeout 2.0
        "She glides from one end of the kitchen island to the pot on the wood stove like a familiar ghost."
        play music ("music/spiraling.ogg") fadein 2.0
        "Memories flash through my head."
        play background ("sfx/chopping.ogg") fadein 3.0
        scene bg chicagobar
        show hat eyes at right,dark1:
            xzoom-1
        with dissolve
        "They speak Hattie Willowby. They speak Conrad Adler. They speak Aiden Fletcher."
        scene bg chicagotrain
        show hat eyes at right,house1:
            xzoom-1
        with dissolve
        "Slipping past me in the yellow lights of a subway."
        scene mansionkitchen
        show hat eyes at right:
            xzoom-1
        with dissolve
        "The specter of death sneaks up on me and takes a seat right on the kitchen island."
        "It has no form, and cannot speak but I know it takes up space."
        "And I know it wants to convince me that life is just another transition."
        "That when you get accustomed to wasting time, you can only waste more."
        "I turned my back on it once, but it knows I have to walk into this kitchen."
        show hat shock with dis
        wi "\"Hello Hattie.\""
        stop background
        stop music fadeout 4.0
        "The chopping stops."
        show hat shock with dis3:
            xzoom 1
        "She turns, wearing a bemused expression."
        show hat shock talking with dis
        hat "\"Will?\""
        show hat shock with dis
        wi "\"Yeah, it’s me.\""
        show hat angry talking with dis
        play music ("music/contemplation.ogg") fadein 3.0
        hat "\"What on earth are you doing here?\""
        show hat angry with dis
        "She sounds angry."
        "I can’t entirely blame her."
        show hat angry talking with dis
        hat "\"What, are you finally ready to talk?\""
        show hat angry with dis
        wi "\"I’m here to talk.\""
        wi "\"Just not necessarily about what you want to talk about.\""
        show hat eyes talking with dis
        hat "\"Spare me.\""
        show hat angry with dis
        wi "\"I wouldn’t be here if I didn’t think you were in danger.\""
        show hat angry talking with dis
        hat "\"You kidding me?\""
        show hat angry with dis1
        show hat angry talking with dis
        hat "\"This is one of the safest places I’ve ever worked.\""
        show hat angry with dis1
        show hat angry talking with dis
        hat "\"The place is literally guarded.\""
        show hat angry with dis
        wi "\"I’m following a murder case.\""
        show hat with dis3:
            xzoom-1
        "She picks up a handful of chopped tomato and drops it into the pot with a sizzle."
        show hat eyes talking with dis
        hat "\"Hardly new territory for you then.\""
        show hat shock with dis
        wi "\"Every piece of evidence I come across keeps leading me back to this manor...\""
        show hat shock with dis3:
            xzoom 1
        "She turns around, looking a little less calm."
        show hat shock talking with dis
        hat "\"Evidence like what?\""
        show hat shock with dis
        wi "\"The location of where a body was dumped, the speed at which it was dropped, the temperature, the trash found near where the body was discovered...\""
        wi "\"It’s very possible that a serious crime was committed in or near the mansion last Thursday.\""
        "She wobbles a bit and looks around her as if she’s expecting somebody to jump out of the shadows."
        "And she’s tongue-tied."
        show hat eyes with dis
        "After muttering some gibberish she composes herself and clears her throat."
        show hat talking with dis
        hat "\"Well is there anything I can do to help you?\""
        show hat with dis
        wi "\"Did you buy a large packet of tutti-frutti gum at Red’s general store last Wednesday?\""
        show hat eyes with dis3:
            xzoom-1
        play background ("sfx/chopping.ogg") fadein 3.0
        "She shakes her head then shrugs as she goes back to her cooking."
        show hat eyes talking with dis
        hat "\"Well yeah?\""
        show hat with dis1
        show hat talking with dis
        hat "\"Master Hendricks likes that brand of gum.\""
        show hat eyes with dis1
        show hat eyes talking with dis
        hat "\"It’s a popular brand of gum.\""
        show hat with dis
        wi "\"Maybe in the city where we come from. In case you haven’t noticed, here it’s a bit of a luxury.\""
        stop background fadeout 2.0
        show hat talking with dis
        hat "\"Well sure, but gum can last a long time.\""
        show hat with dis1
        show hat talking with dis
        hat "\"I could keep packs of the stuff around for months and get a craving one day and chew a piece.\""
        show hat with dis
        wi "\"You’d tell me if Mr. Hendricks had you doing anything illegal, wouldn’t you, Hattie?\""
        "She juts her chin out at me as she stirs the pot."
        show hat eyes talking with dis
        hat "\"Oh brother.\""
        show hat with dis1
        show hat talking with dis
        hat "\"He hasn’t asked me to do anything illegal, Will.\""
        show hat with dis1
        show hat talking with dis
        hat "\"Just chores. Some cooking. Some minor housekeeping. And keeping the lady of the house company.\""
        show hat eyes with dis1
        show hat eyes talking with dis
        hat "\"Poor dear is completely isolated up here.\""
        show hat with dis
        wi "\"And you still don’t know who put you in contact with Mr. Hendricks, or why he’d be interested in importing a cook?\""
        show hat eyes talking with dis
        hat "\"Nope and nope.\""
        show hat with dis
        wi "\"Not even a letter?\""
        wi "\"There’s nothing--?\""
        show hat talking with dis3:
            xzoom 1
        hat "\"Taste this étouffée.\""
        show hat with dis
        "She shoves a spoon in my mouth that’s very close to being too hot and makes me slurp on it."
        wi "\"It’s fine, Hattie.\""
        show hat angry talking with dis
        hat "\"I’m not going for {i}just fine{/i} Will!\""
        show hat angry with dis1
        show hat angry talking with dis
        hat "\"They’re paying me.\""
        show hat with dis
        wi "\"More salt, more heat.\""
        show hat eyes smile with dis
        hat "\"Attaboy.\""
        #sfx
        show hat with dis3:
            xzoom-1
        "She gives the pot a stir and clanks the spoon on the side."
        show hat with dis3:
            xzoom 1
        "Then she takes a look at me, drops the spoon, and sighs."
        show hat talking with dis
        hat "\"You know, I’d tell you if I thought this job was putting me in danger, Will.\""
        show hat with dis1
        show hat talking with dis
        hat "\"But it’s been extremely mundane.\""
        show hat with dis1
        show hat talking with dis
        hat "\"You know, after all we’ve been through back home, frankly I think I need a little bit of mundanity.\""
        show hat with dis
        wi "\"I’m just letting you know that I think there’s gonna be trouble for you here.\""
        show hat angry with dis
        wi "\"Even if we managed to outrun our old enemies--\""
        show hat angry talking with dis
        hat "\"Your enemies, Will.\""
        show hat with dis1
        show hat talking with dis
        hat "\"The only thing I ever did to those crooks was marry you.\""
        show hat with dis
        wi "\"Unfortunately that’s enough.\""
        wi "\"They see the family as one unit.\""
        show hat eyes talking with dis
        hat "\"I wish you would have taken a page out of their book then.\""
        show hat with dis
        "I feel myself getting frustrated again."
        show hat shock with dis
        wi "\"I would never treat anybody I’m with like a mere extension of myself.\""
        wi "\"It’s not sweet, nor loving, nor romantic.\""
        wi "\"It’s just the most traditional way for somebody to unperson you.\""
        "She looks a little taken aback."
        show hat with dis3:
            xzoom-1
        "But then she goes back to her pot."
        show hat talking with dis
        hat "\"At least tradition doesn’t sound so lonely.\""
        show hat with dis
        wi "\"It was for me.\""
        "She juts out her chin again."
        show hat talking with dis
        hat "\"So then why do you still seem to care about me?\""
        show hat with dis
        "I exhale."
        wi "\"They don’t want us to smoke in the kitchen, do they?\""
        show hat talking with dis
        hat "\"No, but I certainly wouldn’t want you to either.\""
        show hat eyes with dis1
        show hat eyes talking with dis
        hat "\"Stop evading the question.\""
        show hat with dis
        wi "\"I’ll tell you when I either have nothing else left to lose...\""
        wi "\"Or when it’s safe to.\""
        "And there’s more than a million miles between us."
        show hat eyes talking with dis
        hat "\"For all your flaws, you were always honest, Will.\""
        show hat with dis
        "She turns the flame down low."
        show hat talking with dis3:
            xzoom 1
        hat "\"There is something strange I found.\""
        show hat with dis1
        show hat talking with dis
        hat "\"Come on.\""
        show hat with dis1
        scene bg black with dissolve
        scene mansionbasement
        show hat at right,dark3
        with dissolve
        "She leads me around a corner and into what looks like the opening of the basement."
        "Beside the door, there is what looks like an old vanity cabinet."
        play sound ("sfx/scrape4.ogg")
        "She opens one of the drawers and what I see shocks me."
        if willmanorportrait1 == False:
            $ unlocked_journal_pages += 2
        else:
            $ unlocked_journal_pages += 1
        $ manortext = "There is a vanity full of hand mirrors near the basement of the Hendricks mansion. The amount and variety of them is more than excessive."
        $ current_journal_page = 25
        $ renpy.notify("Notebook updated.")
        stop sound
        "She pulls out the biggest collection of hand mirrors I’ve ever seen."
        wi "\"What?\""
        show hat eyes talking with dis
        hat "\"I know what you might be thinking.\""
        show hat with dis1
        show hat talking with dis
        hat "\"Mrs. Hendricks must be an eccentric to own all of these hand mirrors.\""
        show hat with dis1
        show hat talking with dis
        hat "\"Nah.\""
        show hat with dis1
        show hat talking with dis
        hat "\"She doesn’t know they’re here.\""
        show hat with dis
        wi "\"But why are they here?\""
        show hat eyes talking with dis
        hat "\"I was hoping you could tell me.\""
        show hat with dis1
        show hat talking with dis
        hat "\"Please get back to me if you figure it out.\""
        show hat with dis
        "What the hell?"
        show hat eyes talking with dis
        hat "\"Anyways, I’m on the clock still.\""
        show hat eyes with dis1
        show hat eyes talking with dis
        hat "\"I have a dinner to prepare.\""
        show hat with dis1
        show hat talking with dis
        hat "\"If you need to find me again then you know where I’ll be.\""
        show hat with dis1
        hide hat with dis3
        "She leaves me with my thoughts in the cellar."
        "The closer she gets to dinner time the more likely Mr. Hendricks will come home and limit where I can look."
        stop music fadeout 3.0
        scene bg black with dissolve
        scene bg mansionlivingroom
        play background ("sfx/bonfire.ogg")
        show nik smile
        show mrs giggle at left:
            xzoom-1
        with dissolve
        "I make my way back to the living room."
        "Nik and Mrs. Hendricks seem to be deep in conversation when I return."
        play music ("music/quiet.ogg") fadein 2.0
        show mrs with dis1
        show mrs talking with dis
        mrs "\"Did you make it to the kitchen alright?\""
        show mrs with dis
        wi "\"Not a lick of trouble, ma’am.\""
        show nik neutral flaccid hoff with dis
        "I should spend the rest of my time wisely."
        $ investigorder = "next"
        $ willmanorkitchen1 = True
        if willmanorlivingroom1 == False or willmanorportrait1 == False:
            jump willinvestigation2
        else:
            jump postwillinvestigation2


    "Ask a few more questions in the living room." if willmanorlivingroom1 == False:
        show mrs wtf with dis
        wi "\"Aside from the noises and the strange doors, is there anything else odd about the house I should know?\""
        show mrs shocked with dis
        mrs "\"Well I would like to know where an occasional smell is coming from.\""
        show mrs wtf with dis
        wi "\"A smell?\""
        show mrs shocked with dis
        mrs "\"Well yes, but it’s not a smell that lingers like a foul miasma.\""
        show mrs wtf with dis1
        show mrs shocked with dis
        mrs "\"It comes and goes.\""
        show mrs wtf with dis1
        show mrs shocked with dis
        mrs "\"Like a wave at the beach.\""
        show mrs wtf with dis
        mrs "\"It’s just instead of feeling a force that makes you float, you smell something.\""
        show nik sidelook with dis3
        ni "\"Smell what exactly?\""
        show mrs wtf with dis
        show nik sidelook with dis3
        "She looks away, as if thinking,{nw}"
        show mrs shocked with dis
        extend " opens her mouth before shutting it,{nw}"
        show mrs wtf with dis
        extend " tapping her chin."
        show mrs shocked with dis
        mrs "\"Burning.\""
        show mrs wtf with dis
        wi "\"Burning what?\""
        wi "\"Wood? Plastic?\""
        show mrs eyes talking with dis
        mrs "\"Just a very deep, very powerful smell.\""
        show mrs eyes with dis1
        show mrs eyes talking with dis
        mrs "\"I almost want to say the burning scent of everything imaginable.\""
        show mrs eyes with dis1
        show mrs eyes talking with dis
        mrs "\"But there’s a fatty smell.\""
        show mrs wtf with dis1
        show mrs shocked with dis
        mrs "\"Almost like bacon fat?\""
        show mrs wtf with dis
        wi "\"There’s no chance that’s coming from your cook?\""
        show mrs wtf with dis1
        show mrs shocked with dis
        mrs "\"No, the kitchens are vented.\""
        show mrs wtf with dis1
        show mrs shocked with dis
        mrs "\"And those scents tend to linger then fade.\""
        show mrs wtf with dis1
        show mrs shocked with dis
        mrs "\"These are here then gone.\""
        show mrs wtf with dis
        noa "\"Mommy I’m bored.\""
        show mrs giggle with dis
        mrs "\"I’m sorry sweetie.\""
        show mrs with dis1
        show mrs talking with dis
        mrs "\"Papa has plenty of nice books we can read together?\""
        show mrs eyes with dis1
        show mrs eyes talking with dis
        mrs "\"Would you like me to pick one out?\""
        show mrs eyes with dis
        noa "\"Maybe later.\""
        #sfx?
        "The young ram brushes against me."
        "He’s looking down at my gun again."
        "Now he’s actually going for it."
        show mrs shocked with dis
        show nik surprised with dis
        wi "\"Whoa whoa whoa, that’s not for you!\""
        show mrs wtf with dis
        "I push his hands away and he freezes."
        "He looks embarrassed, like he didn’t think he was going to get caught."
        "Then he stops and looks up at me."
        show mrs shocked with dis
        noa "\"Do you kill people?\""
        show mrs wtf with dis1
        show mrs xtr shocked with dis
        mrs "\"Noah! Don’t ask him that!\""
        show mrs wtf with dis
        "I scratch the back of my head."
        "This is real awkward."
        wi "\"I do my best to make sure that doesn’t have to happen.\""
        "He stands on his tip-toes and wobbles his head."
        noa "\"But that’s not answering the question.\""
        "He stares at me a bit, wiggling his lips like he’s not entirely sure how to make the right sorts of faces for adult situations yet."
        show nik sidelook with dis3
        wi "\"Yes, son. I’ve killed people.\""
        noa "\"Wow!\""
        "I wait for him to follow up on that."
        "But he doesn’t."
        "Frankly I had expected him to say a little more than just {i}wow{/i}."
        wi "\"Who exactly is teaching you to talk like that?\""
        "He frowns and shakes a bit."
        noa "\"Well you’re Andy’s papa, right?\""
        "I exhale."
        wi "\"Something like that.\""
        "The outsides of his cheeks are red."
        noa "\"It was his idea!\""
        wi "\"Oh was it?\""
        noa "\"He said he’d tell me more stories about the army if I could get a hold of it.\""
        noa "\"But we’re just playing around mister! That’s all!\""
        wi "\"Then you should play with less dangerous things.\""
        wi "\"These aren’t toys.\""
        noa "\"Okay.\""
        noa "\"Mama, I’m going to go play with my blocks now.\""
        show mrs shocked with dis
        mrs "\"...Okay, Noah.\""
        show mrs wtf with dis1
        show mrs shocked with dis
        mrs "\"Please make sure to play safely!\""
        show mrs wtf with dis
        "She looks very worried, but twice as tired."
        wi "\"Children.\""
        wi "\"They’re little people.\""
        "Who don’t know that taking a weapon from a sheriff isn’t a smart thing to do yet."
        show mrs shocked with dis
        mrs "\"Yes...\""
        show mrs wtf with dis1
        show mrs shocked with dis
        mrs "\"And so much personality for a body that size.\""
        show mrs eyes with dis
        "Mrs. Hendricks sinks into her chair and lets out a sigh."
        show mrs with dis
        show nik neutral flaccid hoff with dis3
        "Sometimes the things kids ask you are the scariest thing that can happen in a day on the job."
        "But I probably shouldn’t spend much more time in the living room."
        "I need to make sure I can learn as much as I can."
        $ investigorder = "next"
        $ willmanorlivingroom1 = True
        if willmanorkitchen1 == False or willmanorportrait1 == False:
            jump willinvestigation2
        else:
            jump postwillinvestigation2



label postwillinvestigation2:
show nik eyestalking with dis
ni "\"Ma’am, do you mind if I show the sheriff something upstairs?\""
show nik eyes with dis1
show nik eyestalking with dis
ni "\"There’s something I think he should see.\""
show nik neutral flaccid hoff with dis
show mrs talking with dis
mrs "\"If that’s the case then please do your best to help him.\""
show mrs with dis
show nik eyes with dis
wi "\"Lead the way, Nik.\""
scene bg mansionfoyer with fade
stop background fadeout 1.0
show nik neutral flaccid hoff at right with dis3
"He leads me back to the foyer, and we’re in front of the portrait again."
"He looks behind his shoulder at the hall and the front door before he speaks."
show nik sidelook with dis3
ni "\"What shook you up?\""
show nik neutral flaccid hoff with dis3
wi "\"What do you mean?\""
$ investigorder = "first"
show nik talking with dis
ni "\"There is more strain in your voice than there was before.\""
show nik neutral flaccid hoff with dis
wi "\"Well I handled the talk with Hattie less than perfectly.\""
show nik sidelook with dis3
ni "\"She is your wife, yes?\""
wi "\"Ex-wife.\""
ni "\"So you are concerned for her?\""
show nik neutral flaccid hoff with dis3
wi "\"More concerned than she is for herself I fear.\""
show nik disappointed with dis3
"He hums."
ni "\"It sounds like you still want input on her decisions.\""
ni "\"You do not get to do that anymore.\""
show nik neutral flaccid hoff with dis3
wi "\"I know.\""
wi "\"But I don’t want to just stand by and do nothing either.\""
wi "\"I know she’s in some kind of trouble.\""
show nik sidelook with dis3
ni "\"Do you really think she's in more trouble now than where she was?\""
show nik neutral flaccid hoff with dis3
wi "\"Some creeps found her apartment, but she could have relocated instead of coming to me.\""
wi "\"We have a better chance of not getting tailed if we keep away from each other.\""
show nik eyestalking with dis
ni "\"Have you considered that she could be completely safe, and the only reason she was brought here was to bother you?\""
show nik neutral flaccid hoff with dis
wi "\"Well, I know at least part of it was meant to bother me.\""
show nik talking with dis
ni "\"So is it not working?\""
show nik neutral flaccid hoff with dis
wi "\"Is this supposed to be helping, Nik?\""
show nik eyestalking with dis
ni "\"Yes.\""
show nik neutral flaccid hoff with dis1
show nik talking with dis
ni "\"You have to figure out how to keep it from bothering you.\""
show nik sidelook with dis3
ni "\"That is the only thing you can do when somebody has power over you.\""
show nik neutral flaccid hoff with dis3
wi "\"I’d feel a hell of a lot better if justice in this country carried out its function.\""
show nik neutral flaccid hoff with dis1
show nik talking with dis
ni "\"We both know it often doesn’t.\""
show nik neutral flaccid hoff with dis1
show nik talking with dis
ni "\"You alone can’t be the arbiter of that.\""
show nik neutral flaccid hoff with dis
wi "\"Okay then.\""
wi "\"So what can we do right now?\""
show nik eyestalking with dis
ni "\"First you want to find out if she’s actually in danger, yes?\""
show nik neutral flaccid hoff with dis
wi "\"...Yes.\""
show nik sidelook with dis3
ni "\"Just check his office.\""
wi "\"James’ office?\""
ni "\"Yes.\""
ni "\"It is the first door to the right at the top of the stairs.\""
wi "\"And how do you know that?\""
ni "\"He told me earlier.\""
"That sounds like a bad lie to me, but I don’t think I need to press him on it."
show nik neutral flaccid hoff with dis3
wi "\"Won’t we need to get a key if we want to look?\""
show nik eyestalking with dis
ni "\"Let’s just turn the knob first and see.\""
show nik eyes with dis1
show nik eyestalking with dis
ni "\"I do not think James is careful enough with evidence to lock his office.\""
show nik neutral flaccid hoff with dis
wi "\"And why do you figure that?\""
show nik disappointed with dis3
ni "\"He’s not one to think he’s doing anything wrong.\""
show nik neutral flaccid hoff with dis3
wi "\"Still, you’d think he has to know tons of people don’t like him.\""
show nik talking with dis
ni "\"I don’t actually know if he does.\""
show nik neutral flaccid hoff with dis
"I shake my head."
wi "\"Let’s go ahead and try it then.\""
scene bg mansioncorridor with fade
show nik neutral flaccid hoff at right with dis3
"We climb up the right side of the stairs and reach the second floor hallway."
show nik eyes with dis
"At the first door we see I give Nik a look and he nods."
show nik neutral flaccid hoff with dis
stop music fadeout 3.5
"So I decide to turn it."
play sound ("sfx/dooropen.ogg")
"And it actually does open."
show nik smile with dis
stop sound
wi "\"You kiddin’ me?\""
show nik eyessmile with dis
ni "\"I told you.\""
show nik smile with dis
"I shake my head again and press though."
scene bg mansionoffice with fade
play music ("music/contemplation.ogg") fadein 3.0
show nik neutral flaccid hoff at center,dark3 with dis3
"There are files and letters spread everywhere."
"There looks to be some measure of order to them by the ways that they are spread."
"And the bins are full of paper."
"I can’t believe he doesn’t burn these."

menu willinvestigation3:
    "What should I sort through [investigorder]?"
    "The file cabinets." if willjamesfile == False:
        "I don’t suppose he leaves his file cabinets unlocked either."
        "I try to open it but the door is stuck."
        wi "\"Well at least he has some sense.\""
        show nik eyestalking with dis
        ni "\"The keys are on top of the cabinet.\""
        show nik neutral flaccid hoff with dis
        wi "\"...So they are.\""
        play sound ("sfx/keyopen.ogg")
        "I feel a bit of secondhand embarrassment when the keys do in fact work and let me in."
        stop sound
        "There’s various files about taxes, company protocol, and deeds."
        "But there’s a particularly flashy folder with dark paper and gold paper stamped into it."
        "At first I expect it to be something important, like the deed to the house."
        "But what I see is... more of an illustration."
        "That’s James’ face in highly rendered, loving detail."
        "Company scrip: 10 cents."
        $ update_unlocked_pages(1, 26)
        $ renpy.notify("Notebook updated.")
        show nik eyes with dis
        wi "\"...Oh for the love of God.\""
        show nik neutral flaccid hoff with dis
        "I can’t make up my mind on this being hilarious or devastating."
        show nik disappointed with dis3
        ni "\"I wanted to see it for my own eyes.\""
        wi "\"Are you saying that people know about this?\""
        ni "\"...Yes.\""
        wi "\"But how did you know?\""
        show nik sidelook with dis3
        ni "\"The secretary at CSCG tells us everything.\""
        ni "\"James showed this off at his party last Thursday.\""
        show nik neutral flaccid hoff with dis3
        wi "\"Well no wonder people are pissed.\""
        wi "\"I thought it was just a mix of his general cluelessness and his grandfather’s reputation.\""
        wi "\"If he gets the approval to do this it will destroy the economy.\""
        "That means trouble for the Hip."
        "Trouble for all of the merchants too."
        "This little piece of paper puts a target on his back for the whole goddamn town."
        "At least it gives me more information into what’s going on, but Jesus fuckin’ Christ this sonuvabitch."
        "Have to muffle myself before I choke to death laughing."
        wi "\"Nik I’m about balls-to-the-walls hysterical.\""
        show nik disappointed with dis3
        ni "\"Good.\""
        ni "\"The world needs to know that this man is crazy.\""
        show nik neutral flaccid hoff with dis3
        wi "\"I’m terrified about what we’re gonna find next.\""
        $ investigorder = "next"
        $ willjamesfile = True
        if willjamesfolder == False or willjamestrash == False:
            jump willinvestigation3
        else:
            jump postwillinvestigation3

    "The folders." if willjamesfolder == False:
        "These just look like pictures and profiles of various CSCG workers."
        wi "\"Look Nik, there’s you.\""
        "I spread open the file and give him a good look at the photo of himself stapled to the documentation."
        show nik talking with dis
        ni "\"{i}Hardworking but obstinate.{/i}\""
        show nik sidelook with dis3
        ni "\"{i}A threat when communicating with union organizers.{/i}\""
        show nik talking with dis
        ni "\"{i}Harmless and passive on his own.{/i}\""
        show nik -talking with dis1
        show nik talking with dis
        ni "\"{i}Keep his budget tight, and wanting for more work.{/i}\""
        show nik eyes with dis
        wi "\"He thinks you’re passive, Nik.\""
        show nik neutral flaccid hoff with dis
        "He walks away and shuffles through more file cabinets."
        show nik disappointed with dis3
        ni "\"Good.\""
        "Nothing here we didn’t already know, I presume."
        show nik neutral flaccid hoff with dis3
        "I have to wonder who’s taking all these photographs."
        "The Byrneses are the only developers in town I know of accessible to the public, but knowing the money James has, it shouldn’t be hard to find a private developer."
        $ investigorder = "next"
        $ willjamesfolder = True
        if willjamesfile == False or willjamestrash == False:
            jump willinvestigation3
        else:
            jump postwillinvestigation3

    "The trashbin." if willjamestrash == False:
        wi "\"There better not be any gum in this basket.\""
        show nik eyes with dis
        wi "\"...There is.\""
        show nik eyestalking with dis
        ni "\"Just think of it like holding one of his kisses in your hand.\""
        show nik smile with dis
        wi "\"Disgusting.\""
        show nik neutral flaccid hoff with dis
        "The top of the pile includes letters from relatives."
        "It’s not clear to me why he’d toss handwritten letters from his family, but there doesn’t look to be anything special about them."
        "There are quite a few letters from Briggs."
        "All of them seem to be just one or two sentences, formal, and strictly business, mostly about costs and replacement equipment."
        "And then I see parchment that looks a little more fine."
        "I suspect it’s just going to be another letter from their extended family on the east coast."
        show willnote1 at center,dark3 with dis3
        "But it’s not."
        "I stare at what’s between my fingers."
        show nik sidelook with dis3
        ni "\"You went quiet.\""
        show nik neutral flaccid hoff with dis3
        wi "\"Mostly because I found what I was looking for.\""
        "He looks over my shoulder."
        show nik eyestalking with dis
        ni "\"So what are you going to do about it?\""
        show nik neutral flaccid hoff with dis
        hide willnote1 with dis3
        wi "\"I don’t suspect showing her this would be enough to convince her to leave.\""
        play sound ("sfx/paperrip.ogg")
        "I rip a piece of it off and leave the rest of it in the trash."
        wi "\"But want to keep just a piece of it.\""
        stop sound
        $ investigorder = "next"
        $ willjamestrash = True
        if willjamesfolder == False or willjamesfile == False:
            jump willinvestigation3
        else:
            jump postwillinvestigation3


label postwillinvestigation3:

show nik talking with dis
ni "\"I bet we can find more.\""
show nik neutral flaccid hoff with dis
wi "\"I do too but I don’t want to be caught in his office with my trousers down, so to speak.\""
show nik eyes with dis
wi "\"Let’s go on and git.\""
show nik neutral flaccid hoff with dis
"Nik opens the door, looking left, then right, then waves me forward."
scene bg black with dissolve
scene bg mansionfoyer with dissolve
show nik neutral flaccid hoff at right with dis3
"The downstairs is still empty."
stop music fadeout 3.0
play sound "sfx/smallbell.ogg"
"But we hear the dinner bell ring."
stop sound
show mrs at left with dis3:
    xzoom-1
"Mrs. Hendricks walks out into the foyer and sees us walking down the stairs."
show mrs talking with dis
mrs "\"Would the two of you like to stay for dinner?\""
show mrs eyes with dis1
show mrs giggle with dis
show nik sidelook with dis3
mrs "\"We always have more than plenty of food to spare.\""
show mrs with dis
wi "\"That’s mighty thoughtful Mrs. Hendricks but I have to be on my way.\""
show nik disappointed with dis3
ni "\"A friend of mine is expecting me as well.\""
show nik neutral flaccid hoff with dis3
show mrs shocked with dis3
mrs "\"Now that’s a downright shame.\""
show mrs eyes with dis1
show mrs giggle with dis
mrs "\"I’d appreciate it if you thought about coming back.\""
show mrs with dis
"As kind as she is, I don’t want to."
"But that doesn’t change the truth."
wi "\"I figure that I will be.\""
show mrs giggle with dis
"She smiles sweetly at that."
show mrs with dis1
show mrs talking with dis
mrs "\"Then I won’t keep you.\""
show mrs eyes with dis1
show mrs giggle with dis
mrs "\"Please have a perfectly delightful evening, the both of you.\""
show mrs with dis
show nik eyes with dis
"We nod our heads and take our clothes from the coat rack and make our way back outside."
stop music fadeout 3.0
scene bg black with dissolve
play background ("music/cicadas.ogg") fadein 4.5
scene bg mansionexterior with dissolve

show nik neutral flaccid hoff at right with dis3
"I can feel the eyes of the butler on the back of our necks as we depart from the porch and reach the front gate."
"A mechanical whirring in front of us goes off as we go through the opening bars."
"Strangely, I don’t see the gunman."
"But that doesn’t mean he’s not still here somewhere."
show nik eyestalking with dis
ni "\"We had a productive evening.\""
show nik neutral flaccid hoff with dis
"I don’t answer."
scene deserttrail
show nik neutral flaccid hoff at right
with dissolve
"My skin won’t stop crawling until we’re both about two hundred paces from the gate."
show nik sidelook with dis3
ni "\"Why are you silent?\""
show nik neutral flaccid hoff with dis3
wi "\"I never liked going downhill.\""
show nik talking with dis
ni "\"Why’s that?\""
show nik neutral flaccid hoff with dis
wi "\"It’s easier for--\""
play sound ("sfx/distantgunshot.ogg")
show nik shocked with vpunch
"I hear the shot go off before I see it."
queue sound ("sfx/ricochet.ogg")
play music ("music/tension.ogg")
"The rusted metal can on the rock beside my leg sparks and I don’t even need to think about what I’m going to do next."
play sound ("sfx/thud5.ogg")
hide nik with vpunch
stop sound
"I tackle Nik to the ground and I make us roll."
"He screams from the shove but it’s better than either of us getting shot."
"I drag him behind the biggest rock I see and I make him crouch with me."
hide nik with vpunch
wi "\"Who the hell is out there?!\""
"I hear laughter."
"One old, one new, both familiar."
show andy eyes smile with dis3
"I peek past the stone to see Noah and Andy almost keeling over in laughter."
show andy smile with dis
wi "\"What in the HELL are you doin’ boy?\""
show andy talking with dis3
an "\"Aw, come one, we were only funnin’ ya.\""
show andy smile with dis
"Nik is still on the floor, blinking rapidly."
wi "\"Ain’t not a goddamn thing that’s funny about assaulting an officer!\""
show andy angry talking with dis
an "\"Oh quit yer bitchin’.\""
show andy eyes smile with dis1
show andy eyes talking with dis
an "\"We were aimin’ for the can, not you.\""
show andy shock with dis
wi "\"Were y’all funnin’ me when you told your new friend over there to steal my gun?\""
show andy angry talking with dis
an "\"Oh what the hell Noah, you blabbed?\""
show andy angry with dis
noa "\"He bullied it out of me!\""
show andy angry talking with dis
an "\"Oh come on, he ain’t that scary.\""
show andy angry with dis
noa "\"Maybe not to you!\""
wi "\"Your mama’s gonna get an ear full of this the next time I see her, son.\""
show andy angry talking with dis
an "\"Don’t you damn call me son.\""
show andy angry with dis1
show andy angry talking with dis
an "\"I’m a grown man.\""
show andy angry with dis
wi "\"Grown men don’t fire stray bullets near walkin’ civilians.\""
show andy talking with dis
an "\"Ones wearing the colors of the USC military do.\""
show andy eyes with dis1
show andy eyes talking with dis
an "\"I’ve gotta stay sharp with my shootin’ and it’s not my fault you weren’t paying attention where you were walkin’.\""
show andy angry with dis
wi "\"If you keep actin’ like that the only uniform you’re gonna be wearing is black and white stripes!\""
show andy angry talking with dis
an "\"I told you not to bother us.\""
show andy angry with dis1
show andy angry talking with dis
an "\"You should stay damn well away from the both of us.\""
show andy angry with dis
wi "\"Ordinarily that would be peaches but I had to talk with your mother today.\""
show andy angry talking with dis
an "\"Mom might see things differently right now but she don’t really need you.\""
show andy angry with dis1
show andy angry talking with dis
an "\"None of us do.\""
show andy angry with dis1
show andy angry talking with dis
an "\"Ya think I need to make that more clear?\""
show andy angry with dis
wi "\"Your point is crystal but you’re not gonna get anywhere by threatening me.\""
play sound ("sfx/gravelwalk.ogg")
jam "\"Threaten you?\""
show jam at right behind andy with dis3
show andy with dis3
"I see James show up behind Andy and Noah."
stop sound
show jam talking with dis
jam "\"Who’s really threatening anybody?\""
show jam with dis
"I point at my ex-wife’s child."
wi "\"He fired on us, Hendricks.\""
show jam eyes with dis
"James crosses his arms and hums."
jam "\"Fired on you?\""
show jam talking with dis
jam "\"Andy, didn’t you say you were aiming for the can?\""
show jam with dis
show andy talking with dis
an "\"Sir yes sir.\""
show andy smile with dis
show jam happy with dis
jam "\"Then I’m glad we could clear that up.\""
jam "\"So no harm done.\""
show jam with dis
"Piece of shit."
show jam talking with dis
jam "\"Now if I’m not mistaken, that’s the third time I’ve heard the dinner bell go off.\""
show jam happy with dis
jam "\"Let’s go eat before the food goes cold.\""
show jam with dis
noa "\"Hooray!\""
show andy eyes talking with dis
an "\"Sounds good to me.\""
show andy smile with dis1
hide jam
hide andy
with dissolve
stop music fadeout 4.0
"James guides them towards the inside of their porch while touching their shoulders."
"If he thinks that will make me jealous then he has a surprise coming his way."
"I don’t know if he plans to raise his son that way, but he’s leading both of those boys down a dangerous road if nobody nips it in the bud."
"I’ve never seen Andy act this out of line."
"Nobody, and I mean nobody, is going to threaten me from talking to Hattie when I need to talk to her."
"Don’t matter a damn if my blood is runnin’ through his veins or not."
show nik surprised at right with dis3
wi "\"You alright Nik?\""
ni "\"I do not know.\""
show nik disappointed with dis3
ni "\"We are not dead, yes.\""
wi "\"We will indeed see another sunrise.\""
show nik sidelook with dis3
ni "\"Please help me get on my feet William.\""
wi "\"...Right.\""
hide nik with dis3
play sound ("sfx/gravelwalk.ogg")
"We get our distance as far away from that house as we can before we talk again."
stop sound
show nik sidelook at right with dis3
ni "\"Your son is dangerous, Will.\""
show nik neutral with dis3
wi "\"He was fucking with us.\""
show nik eyes with dis
"Nik {nw}"
show nik -eyes with dis
extend "blinks."
show nik talking with dis
ni "\"Does that change what I said?\""
show nik -talking with dis
wi "\"...I think if he really wanted to hit us we wouldn’t be walking right now.\""
wi "\"He’s his own man now, Nik.\""
wi "\"You sayin’ I should talk to him?\""
show nik disappointed with dis3
ni "\"I would say so if he didn’t have a gun.\""
ni "\"...Does his mother have any sway?\""
show nik neutral with dis3
wi "\"Some.\""
wi "\"After all, she’s why he has a roof over his head.\""
wi "\"He says he plans to go, but the fact that he hasn’t already lends some credence to the idea that she can convince him to behave.\""
show nik talking with dis
ni "\"Have her do that.\""
show nik eyes with dis1
show nik eyestalking with dis
ni "\"Preferably in a room with closed walls and no windows.\""
show nik smile with dis
"I force a toothy grin to let him know how much of a hilarious, comic genius he is."
"But he lets the insult roll off his back."
show nik talking with dis
ni "\"Would you like me to walk you back to the brothel?\""
show nik -talking with dis
wi "\"Who says I’m going back to the brothel?\""
show nik eyestalking with dis
ni "\"Because that’s where you always go.\""
show nik neutral with dis
wi "\"Well, no thank you.\""
wi "\"I have to compare some notes with Sam anyway.\""
show nik sidelook with dis3
ni "\"No matter.\""
ni "\"I need shower anyway.\""
show nik talking with dis3
ni "\"I’ll show up at Saguaro’s Hip in several hours.\""
show nik -talking with dis
"I tell him that this is fine, wanting to focus on my leads."
hide nik with dis3
"The more people I talk to, the more I’m convinced that the murder has something to do with the party that was held at the Hendricks’ manor on Thursday."
"And that’s enough of a breakthrough to make me feel like I’m getting somewhere."
stop background fadeout 3.5

scene bg black with slow_dissolve
$ quick_menu = True
$ quick_menu_will = False
$ willnote = False
pause 0.8

scene bg hipwashroom with dissolve
"William’s been gone more than a few hours."
"I know he’s fine on his own, but I can’t help but wonder if he’s pushing himself too hard."
"I know he’s not old, but he {i}ain’t{/i} that young, neither."
"I’m down in the washroom, stripping off my shirt."
"I can’t help but shudder."
"Being in that awful house makes my skin crawl."
"It’s like somethin’ in the air there was {i}sticky{/i}, and I want to scrub it off my clothes and my body."
"I swirl my dirty clothes with the wooden paddle and hear them simmer in the boiling water."
"Cynthia shows up in the middle of this with a bundle of her own."
show cyn serious a at centerleft with dis3
cy"\"I know you like to keep yourself immaculate, Sam, but weren’t you down here just yesterday?\""
m "\"Marcy’s house is {i}disgusting{/i}.\""
m "\"I don’t want to drag anything back into my room.\""
show cyn surprised a with dis
cy "\"Well, that’s not much like her.\""
cy "\"She’s the biggest homebody I know.\""
show cyn annoyed a with dis
m "\"Well maybe some{i}body{/i} needs to get her out of that {i}home{/i} because it’s covered in mold and dust and all these unfinished crafts.\""
show cyn annoyedcrossed a with dis3
cy "\"She’s not {i}dirty{/i}, Sam.\""
show cyn seriouscrossed a with dis
m "\"If she wasn’t, she is now.\""
m "\"You wouldn’t believe the state of that place.\""
"Out of the corner of my eye, somebody big walks by the frame of the door."
show wil at right with dis3
"I feel a little relieved seeing that it’s Will, who for some reason looks even dustier than before we went into Marcy’s place."
show wil smile with dis
"He looks at me and he breaks into a legitimate smile."
wi "\"Oh, Sam, you wouldn’t believe it.\""
show wil with dis
"He stops talking when he sees Cynthia still scrubbing the grime out of our clothes, glaring at him."
show wil talking with dis
wi "\"Would you mind if I borrowed Sam for a moment to talk?\""
show wil with dis
m "\"Will--\""
show cyn angrycrossed a with dis
show wil surprised with dis
play music ("music/contemplation.ogg") fadein 3.0
cy "\"Well, now that you ask, as a matter of fact, I would.\""
show cyn seriouscrossed a with dis
"He blinks."
wi "\"I’m sorry?\""
show cyn angrycrossed a with dis
cy "\"This is our washing room.\""
cy "\"This is our home.\""
show wil with dis
cy "\"It’s not yours?\""
cy "\"Why are you tromping around like you own it?\""
show cyn seriouscrossed a with dis
show wil talking with dis
wi "\"I can assure you that the owner’s given me permission to conduct my business here.\""
show wil with dis
show cyn angrycrossed a with dis
cy "\"As if she can deny you permission?\""
cy "\"You’re the sheriff!\""
cy "\"Quite certain you haven’t forgotten this!\""
show cyn seriouscrossed a with dis
"I don’t know what this is about, but I don’t want to get in the middle of it."
show wil surprised with dis
m "\"...it looks like the two of you should talk.\""
m "\"I’ll be in my room when either of you have finished.\""
m "\"Goodbye.\""


scene bg black with slow_dissolve
$ quick_menu = False
$ quick_menu_will = True
$ willnote = True
scene bg hipwashroom
show cyn seriouscrossed a at centerleft
show sam annoyed -talking at right:
    xzoom-1
with slow_dissolve

"Sam walks around me with a skittish look about him, {nw}"
hide sam with dis3
extend "sulking in the quickest way a puma can while trotting through a narrow corridor."
wi "\"It appears as if we may have got off on the wrong foot, Miss Tsosie.\""
show cyn angrycrossed a with dis
cy "\"He goes off with you and comes home stressed out and covered in grime, Mr. Adler.\""
cy "\"Need I remind you what happened to him the last time he came home looking like that?\""
show cyn seriouscrossed a with dis
wi "\"I can’t really say I can talk about that.\""
"She cackles with the ferocity that only a short yappy woman beset with equal amounts of rage and determination can muster."
show cyn angrycrossed a with dis
cy "\"Yeah, I’ll bet you can’t!\""
show cyn seriouscrossed a with dis
wi "\"I don’t know why you’re goin’ on about Sam.\""
wi "\"Sam’s fine.\""
show cyn angrycrossed a with dis
cy "\"Maybe he doesn’t have any cuts or bruises this time, but he sure does look like he’s aged ten years.\""
show cyn seriouscrossed a with dis
wi "\"Sam’s a grown man.\""
wi "\"You ain’t his momma.\""
show cyn angrycrossed a with dis
cy "\"Didn’t say I was!\""
cy "\"I knew you weren’t as smart as people think you are, but do you really think I’m just mad about Sam?\""
cy "\"Did you even care about what Marcy must be going through?\""
show cyn seriouscrossed a with dis
wi "\"I’m not a mind reader.\""
show cyn angrycrossed a with dis
cy "\"But surely you had to know something!\""
cy "\"That man gloated day and night about controlling Marcy’s entire life and I don’t see you getting involved until things are far worse than they should be.\""
show cyn seriouscrossed a with dis
wi "\"If I had to bring every married man in town just for being too unbecoming with his wife in public, City Hall would dismiss me on the spot.\""
wi "\"I can’t just break into anybody’s home and dig around when I suspect any sort of foul play.\""
wi "\"That’s the kind of stuff that gets you a dagger against your neck in the middle of the night.\""
show cyn angrycrossed a with dis
cy "\"Then how about you spying on all of us and using our private lives for who-knows-what seedy purpose?\""
show cyn seriouscrossed a with dis
"I nod my head, feeling the anger start to well up."
wi "\"So you’re the one who messed with my desk.\""
show cyn angrycrossed a with dis
cy "\"Prove it.\""
show cyn seriouscrossed a with dis
wi "\"You practically confessed. I don’t gotta prove a damn thing.\""
show cyn serious a with dis3
"She looks me up and down and snorts."
show cyn angry a with dis
cy "\"You gonna arrest me, big man?\""
show cyn serious a with dis
wi "\"I’m well within my rights to.\""
show cyn yellingcrossed a with dis3
cy "\"Then are you gonna do something about it then, or is that just another bluff?!\""
show cyn angrycrossed a with dis
"This is escalating out of control."

"I need to work with her, not against her."

"Why can’t she see that’s all that I’m trying to do here?"

if  ETHINT_Points == 1 :
    show cyn surprisedcrossed a with dis
    wi "\"You’re already being spied on!\""
    show cyn seriouscrossed a with dis
    cy "\"Now what the hell is that supposed to mean?\""
    show cyn surprisedcrossed a with dis
    wi "\"The salamander!\""
    wi "\"She’s leaking all of your private information to the wealthiest man in town!\""
    show cyn surprised a with dis3
    cy "\"Ethel?\""
    show cyn fear a with dis
    cy "\"Well, she’s always been mean, but...\""
    "She looks troubled."
    "Like she doesn’t want to believe it but she knows it’s true."
    wi "\"I thought there was a spy for James, and I found her.\""
    wi "\"I haven’t shared or used the brothel’s information in any other way.\""
    wi "\"I’m not interested in cracking down on petty crimes or ruining lives.\""
    if  SW_Points > 1:
        wi "\"I want to keep Sam and the rest of us safe.\""
        show cyn serious a with dis
        "She gives me an odd look."
        cy "\"Huh.\""
        show cyn sad a with dis3
        cy "\"That’s the sincerest you’ve ever sounded to me.\""
        show cyn serious a with dis3
    else:
        wi "\"I want to keep this town safe.\""
        show cyn serious a with dis
        cy "\"I see...\""
        show cyn sad a with dis3
        cy "\"You know, I don’t know if I trust you still...\""
        cy "\"But I think I can trust you more than Ethel now.\""
        show cyn serious a with dis3
        cy "\"I guess I’ll have to figure out what that means.\""
        $ BG_Light =0

    wi "\"If there’s anything you can share with me about her or James Hendricks, then it can help me.\""
    wi "\"It can help all of us.\""
    show cyn sadcrossed a with dis3
    "She crosses her hands and looks away."
    show cyn seriouscrossed a with dis3
    "Then she looks back at me, as if sizing me up again."
    cy "\"I can find out what she’s up to tonight.\""
    wi "\"That might come in handy.\""
    cy "\"If I help do whatever it is you’re doing, are you really gonna help me out?\""
    show cyn serious a with dis3
    cy "\"I don’t do so well when people let me down, you know.\""
    wi "\"I’m not so good with people, Ms. Tsosie, but I think I’m good at this.\""
    "She purses her lips."
    show cyn sadcrossed a with dis3
    cy "\"Wait right there.\""
    hide cyn with dis3
    "She’s gone for about five minutes before she comes back with a small slip of paper{nw}"
    show cyn serious a at centerleft with dis3
    extend "."
    show willnote3 with dis3
    cy "\"Here’s her instructions for the night.\""
    show cyn sad a with dis3
    cy "\"It might not be much but it’s all I’ve got for now.\""
    hide willnote3 with dis3

elif HARINT_Points == 1:
    show cyn seriouscrossed a with dis
    wi "\"You should worry about the goddamn bartender more than me.\""
    show cyn surprisedcrossed a with dis
    cy "\"The bartender?\""
    "She sounds confused, but I can hear the doubt creeping into her voice."
    show cyn surprised a with dis
    cy "\"Why exactly do I need to be worried about Harlan?\""
    wi "\"He has all the access to Dora’s logs as he could want, doesn’t he?\""
    wi "\"A much more comprehensive chunk of information than I ever had.\""
    wi "\"He could easily contact anybody he wants, whenever he wants, just as easily as Dora.\""
    wi "\"I found out that he hates James.\""
    wi "\"But I also found the reason why James brings in more foreigners than Briggs.\""
    wi "\"It’s a bit of an odd position to have for somebody who helps run a brothel that hosts and attracts all sorts of international attention, ain’t it?\""
    show cyn fear a with dis
    "She stands there, breathing."
    cy "\"Do you want to know a secret?\""
    wi "\"Right now, more than anything.\""
    show cyn sad a with dis3
    cy "\"For the last few days I’ve lived in fear of that man.\""
    cy "\"He had a piece of my mother’s fur.\""
    cy "\"In a box.\""
    cy "\"In a hidden crawlspace.\""
    cy "\"I almost left the brothel right then and there, that night.\""
    cy "\"I run the idea through my head every night going forward.\""
    cy "\"But then I think about how I don’t have anywhere to go back to other than Camp Rosa or the reservation.\""
    show cyn fear a with dis3
    "She shakes her head."
    cy "\"Did you know your mother, Adler?\""
    wi "\"Not really.\""
    wi "\"My father didn’t let me see her much.\""
    show cyn sad a with dis3
    cy "\"I knew mine.\""
    cy "\"And I miss her every waking day that I’m alive.\""
    cy "\"And I will never know peace knowing her remains were stolen and sold at the village of my birth, in pieces, to collectors like that man.\""
    cy "\"If there is anything at all, whatsoever, that could fuck up that old man’s life, then I want to help you do it.\""
    "She pulls something out of her pocket."
    show willnote2 with dis3
    show cyn fear a with dis3
    cy "\"He keeps slipping creepy messages like these near Dora’s office, as if we didn’t keep seeing him do it.\""
    show cyn sad a with dis3
    cy "\"I still don’t really trust you, Adler, but if you don’t trust Harlan then that’s at least something we’ve got in common.\""
    hide willnote2 with dis3
    cy "\"For now, he’s my biggest problem.\""
else:
    wi "\"That’s enough.\""
    wi "\"This is a ridiculous conversation.\""
    wi "\"From now on, stay out of my way and I’ll stay out of yours.\""
    cy "\"Gladly.\""
    cy "\"But if you’re going to keep stealing information from us then I’m not going to make it easy for you.\""
    wi "\"It’s a good thing I love a challenge.\""

show cyn surprised a with dis3
clunk "\"Excuse me?\""
stop music fadeout 5.0
"We both jump when we look at the doorway."
show cli happy at right with dis3
"That Batavian stoat is just standing there, smiling."
show cyn serious a with dis
cy "\"How long have you been there?\""
wi "\"I’d like to know as well.\""
show cli eyes talking with dis3
cl "\"Well, I would have interrupted sooner, but you both seemed to be in the midst of a quarrel.\""
show cli with dis1

label williamroute3c:
play music ("music/quiet.ogg") fadein 3.0
wi "\"Mr. Houwelinck...\""
show cli eyes with dis
"He clears his voice."
show cli eyes talking with dis
cl "\"Mr. Tibbits, if you please.\""
show cli at centerright with dis3
wi "\"Mr. Tibbits...\""
show cli doubt with dis
wi "\"I’m working as quickly as I can to apprehend the instigator behind your assault.\""
cl "\"If this is your quick work then I certainly don’t want to see your slow work.\""

if ETHINT_Points == 1:
    "I look down and rub my temples."
    "But then I notice a very yellow, very gauzy piece of fabric sticking out of the stoat’s pocket."
    wi "\"One of the girls give you that?\""
    show cli happy with dis3
    cl "\"Oh, yes.\""
    cl "\"Miss Ethel?\""
    show cli eyes talking with dis
    cl "\"She’s very kind.\""
    show cli with dis
    "No she isn’t."
    wi "\"Did you book her?\""
    show cli blush eyes right with dis
    cl "\"Oh, I feel so indulgent letting you know.\""
    show cli happy with dis3
    cl "\"But yes!\""
    cl "\"And it won’t be my first time either.\""
    show cli blush eyes left with dis3
    cl "\"I wanted to make sure it was well before our night adventure, just in case I’ll be having a go more than once today.\""
    show cli with dis
    wi "\"Could you find out one thing for me?\""
    show cli happy with dis3
    cl "\"Is it something naughty Mr. Adler?\""
    "The beginning of that migraine is creepin' closer."
    show cli with dis3
    wi "\"Ok, I’m just going to tell you what I need now.\""
    "I show him the note."
    show cli doubt with dis
    wi "\"I just want you to confirm who she delivered wine to yesterday.\""
    wi "\"I want to know who wrote this note.\""
    cl "\"Well, I doubt that would make for the best pillow talk, but I’ll see what I can do.\""
    "I sigh."
    wi "\"{i}All{/i} I want to know about is the wine delivery.\""

else:
    wi "\"I’ll let you know if I think of anything, Mr. Tibbits.\""
    show cli eyes talking with dis
    "He waves his paw dismissively."
    cl "\"Well, don’t let me distract you.\""
    show cli doubt with dis
    wi "\"Easier said than done.\""

play sound ("sfx/doorcreakopen.ogg")
"He opens his mouth again, but gets interrupted by the door opening."
stop sound
show cli with dis3
show sam neutral -talking with dis3:
    xpos 0.60
"It’s just Sam again."
show sam neutral talking with dis
m "\"I couldn’t hear any shouting from the hall, so I took that as a good sign.\""
show sam surprised -talking with dis
"When Sam sees Mr. Tibbits, he has the look like he walked in on a picture show of himself plastered on the wall."
show cli happy with dis3
cl "\"Oh, why if it isn’t Samuel!\""
show sam surprised talking with dis
m "\"Oh.\""
show sam surprised -talking with dis1
show sam surprised talking with dis
m "\"Well if it isn’t...\""
show sam sad -talking with dis1
show sam sad talking with dis
show cli doubt with dis3
m "\"Mr., ah...\""
show sam sad -talking with dis
"The room is so quiet I can hear the piano in the saloon playing through the walls."
show cli down with dis3
cl "\"Tibbits.\""
show sam sad talking with dis
m "\"Right.\""
show sam annoyed -talking with dis1
show sam annoyed talking with dis
m "\"Sorry.\""
show sam annoyed -talking with dis1
show sam annoyed talking with dis
m "\"It’s been a long day for me.\""
show sam neutral -talking with dis3
if ETHINT_Points == 1 or HARINT_Points == 1:
    show cyn sadcrossed a with dis3
else:
    show cyn annoyedcrossed a with dis3
cy "\"It’s been a long day for all of us.\""
show cli doubt with dis3
wi "\"Still ain’t over.\""
"The wave of fatigue rolling its way through my body is starting to give me the jitters."
"I could really use a smoke right now."
"Sam looks from my face to hers."
"Looks like he’s putting together that we ain’t done talking."
show cyn seriouscrossed a with dis3
show sam neutral talking with dis3
m "\"Good news, Tibbits.\""
show sam neutral -talking with dis
cl "\"Huh?\""
show sam eyes talking with dis
m "\"Tonight’s your lucky day.\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"Why don’t we get to know each other a little more down at the bar?\""
show cli shocked with dis3
show sam smile with dis3
cl "\"The bar?!\""
show cli sad with dis3
cl "\"That didn’t go so hotly the first time.\""
show sam neutral talking with dis
m "\"Just relax and don’t do anything to stand out.\""
show sam smile with dis3
show cli with dis3
"He opens the door and beckons the weasel outside."
show sam eyes talking with dis
m "\"I’ll even buy you a drink.\""
show sam smile with dis
show cli blush eyes left with dis
cl "\"A drink?!\""
show sam annoyed talking with dis
m "\"A {i}cheap{/i} one.\""
show sam smile with dis
show cli blush eyes right with dis
cl "\"Well, if money’s the issue, then {i}I’ll{/i} buy the drink.\""
show cli happy with dis3
"He wags his index finger."
cl "\"There’s no need to be frugal if the alternative is swill.\""
show cli with dis3
show sam annoyed -talking with dis3
"Sam gives me a look like I owe him more than a few favors as he{nw}"
hide cli
hide sam
with dis3
extend " steps out of the door."
show cyn serious a with dis3

wi "\"Listen, Miss Tsosie.\""
wi "\"I know that you don't trust me.\""
wi "\"Frankly, I understand why.\""
wi "\"But if there's anybody you're willing to talk about, just to let me know about anything wrong or suspicious here at Saguaro's Hip that seems like it's out of your hands...\""
wi "\"Whoever or whatever that might be, just know you can pass the burden of it onto me.\""
cy "\"Well, let me think.\""
"She bends down to brush a piece of dust off her skirt and crosses her legs."
cy "\"You and I both know you know more than enough about the girls.\""
"I lean against the wall, balancing on the back of my foot."
"I try not to let my blood pressure rise."
wi "\"Was that you messing with my papers?\""
show cyn annoyed a with dis
cy "\"Gonna lock me up?\""
wi "\"I could.\""
show cyn seriouscrossed a with dis3
"She crosses her arms."
cy "\"So do it then.\""
"If I arrest her, the other girls would know."
"That would spread to the Madam, and I wouldn't be welcome here anymore."
"We both know this."
"She's seeing how far she can push the envelope..."
wi "\"But we both know I'm not gonna do that.\""
wi "\"Just help me out here.\""
show cyn sadcrossed a with dis3
"She looks away and squints."
show cyn seriouscrossed a with dis3
"Then she looks back to me."
cy "\"Maybe there's one way we can help each other out.\""
wi "\"Oh yeah?\""
if HARINT_Points == 0:
    show cyn worriedcrossed a with dis3
    cy "\"I think there's something wrong with the barkeep.\""
    cy "\"Harlan Perkins.\""
    cy "\"He works just fine with most of the other staff, so nobody else really has a problem with the guy.\""
    show cyn seriouscrossed a with dis3
    cy "\"But I just know there is.\""
    "I nod and cross my arms."
    wi "\"And how do you know?\""
    cy "\"Well there's a few things.\""
    cy "\"But mostly there's these little mannerisms he has.\""
    cy "\"I work a lot of shifts with him so I get to see how he interacts plenty.\""
    show cyn worriedcrossed a with dis3
    cy "\"And let me tell you, there's a lot of rage there.\""
    cy "\"A lot of malice.\""
    show cyn sadcrossed a with dis3
    cy "\"He hides it well, but not so well enough from me.\""
    show cyn seriouscrossed a with dis3
    cy "\"I can read it on his face.\""
    wi "\"So why are you suddenly so willing to talk about him specifically?\""
    cy "\"Well he’s not exactly family.\""
    wi "\"So certain people at the brothel are family to you?\""
    cy "\"Well, all of the workers really.\""
    cy "\"Even the ones who are rough around the edges.\""
    show cyn annoyedcrossed a with dis3
    wi "\"Like Sam?\""
    show cyn seriouscrossed a with dis
    cy "\"Well of course Sam.\""
    show cyn serious a with dis3
    cy "\"But also the ones who won’t approach first timers.\""
    show cyn sad a with dis3
    cy "\"And the ones who don’t want to be here but really have nowhere else to go.\""
    wi "\"It’s a tough life.\""
    show cyn serious a with dis3
    cy "\"Being married sounds tougher.\""
    cy "\"Didn’t work out so well for you, did it?\""
    "I crack a smile."
    wi "\"No.\""
    wi "\"No, it sure didn’t.\""
    show cyn a with dis
    "She laughs too."
    "Quietly."
    show cyn serious a with dis
    cy "\"Plenty of the girls who come here think they’ve hit rock bottom.\""
    cy "\"Enough of them think they’re disgraced because Christian men want virgins.\""
    show cyn annoyed a with dis
    cy "\"Or rather, the virgins they didn’t dally with yet.\""
    show cyn serious a with dis
    wi "\"Those men’s loss.\""
    wi "\"Virgins aren’t so good in bed.\""
    cy "\"More importantly, these girls have got to learn what rock bottom is.\""
    "I hum."
    wi "\"And what do you think that looks like?\""
    "She bites her lip, nodding."
    show cyn seriouscrossed a with dis3
    cy "\"Well, you saw what happened to Mrs. Greene.\""
    show cyn sadcrossed a with dis3
    cy "\"Tied to a broke husband at the hip, {i}til’ death do you part{/i}, with no spending power.\""
    "She crosses her arms and sighs."
    show cyn seriouscrossed a with dis3
    cy "\"Now that’s rock bottom.\""
    cy "\"The girls aren’t so mean to themselves for working the profession after they get used to having money.\""
    cy "\"As well as how to manage it.\""
    wi "\"So I take it a bartending jack, who seems to be the Madam’s biggest fan, wouldn’t exactly have as much in common with the rest of her employees.\""
    show cyn annoyedcrossed a with dis
    cy "\"Back to Harlan again?\""
    wi "\"He’s been on my mind lately.\""
    wi "\"Can you tell me what you know about him?\""
    show cyn sadcrossed a with dis3
    cy "\"I don’t like how he looks at me the past few days.\""
else:
    show cyn sadcrossed a with dis3
    cy "\"I don’t like how Harlan looks at me the past few days.\""
cy "\"Normally he’s curt and rude and minds his own business.\""
cy "\"But with me?\""
"She bites her lip again."
show cyn worriedcrossed a with dis3
cy "\"He stares.\""
wi "\"What do you suspect?\""

if ETHINT_Points == 1 or HARINT_Points == 1:
    if ETHINT_Points == 1:
        cy "\"There was an incident a few days ago where we found some of his belongings hidden in a secret space in the wall.\""
        wi "\"These walls have secret spaces?\""
        show cyn annoyedcrossed a with dis
        "She rolls her eyes."
        cy "\"You think I knew?\""
        cy "\"As of two nights ago they do, yes.\""
        show cyn seriouscrossed a with dis
    "She sighs again."
    if ETHINT_Points == 1:
        cy "\"I think he knows what I saw in his trunk.\""
    else:
        cy "\"I think Harlan knows what I saw in his trunk.\""
    cy "\"He had a piece of jewelry that belonged to my mother.\""
    wi "\"I remember that you used to sell jewelry a few years ago.\""
    show cyn annoyedcrossed a with dis
    "She tilts her head and gives me a look."
    cy "\"Jewelry that belonged to my {i}dead{/i} mother.\""
    if ETHINT_Points == 1:
        cy "\"And pieces of her hair.\""
    "That leaves a bad taste in my mouth."
    wi "\"So then we have a mystic on our hands.\""
    show cyn sadcrossed a with dis3
    "She looks to the side and folds back her tongue."
    cy "\"You know... I remember Dora mentioning that he wanted to be a stage magician.\""
    wi "\"Back when they used to tour together?\""
    "Cynthia shakes her head."
    show cyn annoyedcrossed a with dis3
    cy "\"No, there was no {i}touring together{/i}.\""
    cy "\"She toured, and he went with her.\""
    show cyn seriouscrossed a with dis
    cy "\"They had a big music and drama group and he was one of the stage helpers.\""
    cy "\"She said he’d bring ideas to her here and there.\""
    cy "\"But she refused because he was convinced her stage presence alone would bring enough to the act.\""
    cy "\"If he really did say that he’s right.\""
    cy "\"Dora demands attention just with a look.\""
    cy "\"I don’t think Harlan could carry the same weight, even if his tricks were as good as he said they were.\""
    wi "\"But where did they tour?\""
    "She shrugs."
    cy "\"I’m sure every major city in the United States of Columbia.\""
    show cyn a with dis3
    cy "\"Dora was really big.\""
    show cyn eyes a with dis
    "She sighs again, but this time, it’s a dreamy one."
    cy "\"Dora’s Delight, the Soul of the Magnolias.\""
    show cyn talking a with dis
    cy "\"Would pay more than a pretty penny to see that swan song if I was able to be there fifteen to twenty years ago.\""
    show cyn a with dis1
    show cyn talking a with dis
    cy "\"Surprised you don’t remember seeing posters for her yourself, being the big city man that you are and all.\""
    show cyn a with dis
    wi "\"I probably did see the posters.\""
    wi "\"But I think I would have been sixteen, maybe seventeen.\""
    wi "\"Had a lot on my mind back then.\""
    show cyn serious a with dis
    "She arches an eyebrow and gives me a doubtful expression."
    cy "\"What?\""
    cy "\"Like baseball?\""
    wi "\"Yeah.\""
    "Her eyes glaze over just a bit."
    cy "\"Surely you had dates on the mind too.\""
    wi "\"In a sense.\""
    wi "\"Sports were encouraged.\""
    wi "\"Dalliances with young native women my age were not.\""
    "And especially not the boys."
    wi "\"Doing what my father wanted always came first.\""
    wi "\"He had his ways of making sure that happened.\""
    show cyn annoyed a with dis
    "She scowls."
    cy "\"A real papa’s boy, huh?\""
    "I shrug and pocket my hands."
    wi "\"I dared not refuse.\""
    wi "\"Either way, we didn’t have the best relationship, at the end.\""
    cy "\"I hear you don’t have the best relationship with your son, either.\""
    "I shrug at her."
    wi "\"I suppose neither of us want one.\""
    show cyn annoyedcrossed a with dis
    "She folds her hands."
    cy "\"You sure about that?\""
    wi "\"I asked him.\""
    wi "\"If that boy says he has a warrior’s heart, then I believe him.\""
    wi "\"When you become a warrior, your family becomes your unit.\""
    show cyn seriouscrossed a with dis
    wi "\"I know him well enough to know that he wants that more than me or Hattie doting on him for the rest of his life.\""
    wi "\"If there’s one thing I’ll always give that boy, it’s his right to have choices.\""
    "After all, {i}he{/i} never gave me one."
    "Never."
    show cyn surprisedcrossed a with dis
    "She raises her eyebrows."
    cy "\"So what’s the deal?\""
    show cyn seriouscrossed a with dis
    cy "\"Suddenly I’ve talked enough about myself to get a peek past those steel barricades of yours?\""
    "I shrug."
    wi "\"That's generally how conversations go with me.\""
    wi "\"Keeps things simple.\""
    cy "\"You really think it’s fair though?\""
    "I shake my head."
    wi "\"I’m not so interested in fair.\""
    wi "\"I just don’t want to see more people get hurt if Harlan Perkins is involved in something bigger than himself.\""
    wi "\"Help me or don’t.\""
    play sound ("sfx/creak1.ogg")
    show cyn sad a with dis3
    "She sits on a chair next to a washing basin."
    stop sound
    cy "\"If there’s anything damning on him, I’ll bet it’s in his office.\""
    "She frowns."
    cy "\"But it’s locked up tight.\""
    cy "\"Nobody ever goes in there.\""
    wi "\"Hrm.\""
    show cyn fear a with dis3
    cy "\"What are you thinking?\""
    wi "\"Mystics believe in shit because they want to.\""
    wi "\"Maybe if you give him one of your worst pieces of jewelry and tell him what he wants to hear, he’d let us in...\""
    show cyn serious a with dis
    cy "\"I don’t think he’d let either of us into his office.\""
    wi "\"Maybe not us.\""
    wi "\"But what about Sam?\""
    show cyn seriouscrossed a with dis3
    "She folds her arms again."
    cy "\"Well I never see him stare at Sam the way he stares at me.\""
    cy "\"He owes me a favor anyway.\""
    wi "\"You sure you want to waste it on helping me?\""
    show cyn sadcrossed a with dis3
    cy "\"It’s not entirely for you.\""
    cy "\"I just want to know what other nasty surprises he might have hiding.\""
    show cyn seriouscrossed a with dis3
    cy "\"Let’s go talk to Sam once he’s finished with Mr. Tibbits.\""

else:
    show cyn sadcrossed a with dis3
    cy "\"To be honest, I just don’t want to think about Mr. Perkins right now.\""
    cy "\"If he is doing something wrong, I suspect he’s going to slip up sooner or later.\""
    show cyn annoyedcrossed a with dis
    cy "\"It’s your job to notice when he does or not.\""
    "I hold my hands to my back and look to the ceiling, grunting as my spine stretches."
    wi "\"I only have two eyes, Cynthia.\""
    cy "\"Give me some results and maybe you’ll get more.\""
    cy "\"Are we done here?\""
    "My breath escapes me."
    show cyn seriouscrossed a with dis
    wi "\"Yeah.\""
    wi "\"We’re done.\""
    show cyn serious a with dis3
    play sound ("sfx/clothrustle.ogg")
    "She unfolds her arm and stands up."
    stop sound
    hide cyn with dis3
    "Her bony elbow bumps into me on her way out."
## cut5
play music ("music/saloonpiano.ogg") fadeout 3.0 fadein 3.0
scene bg black with dissolve
scene bg saloon2 with dissolve

"When I open the door, I see a few girls run around the corner, whispering and giggling before they disappear."
"The bar is packed."
"That’s typical for a mid-afternoon on a Sunday."
"But I don’t have to see him to know where Sam is sitting."
"He’ll be at his usual spot in the corner."

"As I approach it, I can hear that I was right."
show sam neutral -talking at center,saloon:
    xzoom-1
show cli doubt at right,saloon
with dissolve
cl "\"Does it shine?\""
show sam neutral talking with dis
m "\"Yeah.\""
show sam neutral -talking with dis
cl "\"Can I find it at the bottom of a river?\""
show sam eyes talking with dis
m "\"Yep.\""
show sam eyes -talking with dis
cl "\"Is it a mineral?\""
show sam eyes talking with dis
m "\"Nope.\""
show sam neutral -talking with dis3
show cli sad with dis3
"The weasel leans into the table, crossing his hands."
show sam smile with dis

cl "\"How many questions am I at?\""
show sam neutral talking with dis
m "\"Seventeen.\""
show sam eyessmile -talking with dis1
show sam eyes talking with dis
m "\"That was one of your questions by the way.\""
show sam smile with dis3
show cli shocked with dis3
cl "\"That doesn’t count!\""
show cli doubt with dis3
m "\"Yeah-huh.\""
"The weasel starts chittering manically in a different language."
cl "\"Does it glow?\""
show sam neutral talking with dis
m "\"None that I ever seen.\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"Last question.\""
show sam smile with dis3
show cli down with dis3
cl "\"Okay.\""
show sam surprised -talking with dis3
show cli serious with dis3
cl "\"Is it bigger or smaller than half a meter?\""
show sam surprised talking with dis
show cli doubt with dis
m "\"What’s a meter?\""
show sam annoyed -talking with dis
cl "\"What do you mean {i}what’s a meter{/i}?\""
show sam annoyed talking with dis
m "\"I mean {i}what{/i}.\""
show sam annoyed -talking with dis1
show sam annoyed talking with dis
m "\"{i}Is{/i}.\""
show sam annoyed -talking with dis1
show sam annoyed talking with dis
m "\"{i}A meter{/i}.\""
show sam annoyed -talking with dis3
show cli down with dis3
cl "\"Ah, right.\""
cl "\"It’s ah.\""
show sam neutral -talking with dis
cl "\"The size of three feet.\""
show sam neutral talking with dis3
show cli doubt with dis3
m "\"My feet or your feet?\""
show sam neutral -talking with dis
cl "\"Okay, now you’re just trying to vex me Samuel.\""
show sam surprised -talking with dis
cl "\"A foot is twelve inches I think?\""
show sam surprised talking with dis
m "\"Oh.\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"Then in that case I suppose it depends.\""
show sam eyes -talking with dis
cl "\"What do you {i}mean{/i} it depends?\""
show sam eyes talking with dis
m "\"Time to take another guess Mr Tibbits.\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"What am I thinking of?\""
show sam smile with dis3
show cli frustrated with dis3
"The weasel rubs his temples with his hands and makes a groaning sound."
show cli with dis3
"Then he stops, and smiles."
show cli eyes talking with dis
cl "\"An anchor.\""
"He perks up and puffs out his chest."
show cli doubt with dis
show sam eyes talking with dis
m "\"Nope.\""
show sam smile with dis3
show cli frustrated with dis3
cl "\"The bollocks do you mean, {i}nope{/i}?!\""
show sam neutral talking with dis3
show cli doubt with dis3
m "\"Now calm down Mr. Tibbits.\""
show sam neutral -talking with dis1
show sam neutral talking with dis
show cli serious with dis
m "\"I’ve got your answer.\""
show sam smile with dis
"The weasel leans in closer."
cl "\"Yes?\""
cl "\"Go on?\""
show sam neutral talking with dis
m "\"You ready?\""
show sam neutral -talking with dis
show cli talking with dis
cl "\"Goodness yes!\""
show sam eyes talking with dis
show cli with dis
m "\"Alright.\""
show sam eyes -talking with dis
"Sam holds up a finger and then balls his fist and coughs into it, clearing his throat."
show sam eyes talking with dis
m "\"The answer is...\""
show sam eyes -talking with dis1
show sam eyes talking with dis
show cli doubt with dis
m "\"A freshly caught catfish.\""
show sam smile with dis
cl "\"...A what!?\""
show cli angry with dis3
cl "\"That’s absurd!\""
show sam eyes talking with dis3
show cli doubt with dis3
m "\"I shit you not Mr. Tibbits, the animal is real, and quite absurd.\""
show sam neutral -talking with dis3
show cli frustrated with dis3
cl "\"I asked you if the thing was living and you told me it wasn’t!\""
show sam neutral talking with dis
m "\"A freshly gutted catfish.\""
show sam neutral -talking with dis
cl "\"You cheated!\""
show sam annoyed talking with dis
m "\"No I didn’t.\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"You just weren’t thinkin' broadly enough.\""
show sam smile with dis
cl "\"{i}Broadly{/i} my foot, I ought to shake you!\""
show sam surprised -talking with dis
show cli doubt with dis3
wi "\"Sorry to interrupt you boys.\""
show cli frustrated with dis3
cl "\"You’re not interrupting a thing!\""
show sam neutral -talking with dis
cl "\"This game is over.\""
show cli serious with dis3
cl "\"I need a drink.\""
hide cli with dis3
"We watch him pout as he makes his way back to the bar, waving his hand for the barkeep’s attention."
wi "\"He’s right you know.\""
show sam annoyed -talking with dis
wi "\"You did cheat.\""
show sam annoyed talking with dis
m "\"I don’t agree.\""
show sam eyes -talking with dis1
show sam eyes talking with dis
m "\"Y’all just can’t be too stubborn about something’s state of being.\""
show sam smile with dis
wi "\"You’re just teasing him aren’t you?\""
show sam happy -talking with dis
m "\"Maybe just a little bit.\""
show sam smile with dis
"I feel myself grin."
wi "\"Piece of shit.\""
show sam neutral talking with dis
m "\"Hey hey hey.\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"It’s not like neither of us got to have any fun.\""
show sam eyessmile -talking with dis
m "\"Besides, he wouldn’t let me pick the game.\""
show sam smile with dis
wi "\"Very sportsmanlike of you.\""
show sam eyes talking with dis
m "\"The sportiest.\""
show sam neutral -talking with dis
"He watches Cliff still waiting at the bar and lowers his voice."
show sam neutral talking with dis
m "\"So what did you and Cynthia end up talking about?\""
show sam surprised -talking with dis
wi "\"We’re both suspicious of the bartender.\""
show sam annoyed -talking with dis
"Sam squints and looks back at me."
show sam annoyed talking with dis
m "\"Our bartender?\""
show sam neutral -talking with dis
wi "\"We ain’t drinkin’ anywhere else, are we?\""
show sam neutral talking with dis
m "\"I just mean...\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"Well, look at him.\""
show sam annoyed -talking with dis
wi "\"Don’t make eye contact.\""
show sam annoyed talking with dis
m "\"I meant figuratively.\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"He’s old, William.\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"And he’s got a lot to lose if he screws anything up.\""
show sam neutral -talking with dis
wi "\"He sure does, doesn’t he?\""
show sam surprised -talking with dis
"A look of understanding crosses his face."
show sam sad -talking with dis
"Then he looks guilty."
"Ashamed."
show sam sad talking with dis
m "\"So you think he might be backed into a corner?\""
show sam sad -talking with dis
wi "\"Maybe.\""
wi "\"For all we know, he could think he’s already lost too much.\""
show sam sad talking with dis
m "\"People do some desperate things when there’s nothing else to lose.\""
show sam sad -talking with dis
"I feel angry."
show sam surprised -talking with dis
wi "\"Stop blaming yourself.\""
"It comes across harsher than I mean it to."
"He flinches,{nw} "
show sam annoyed -talking with dis
extend "then scowls."
show sam annoyed talking with dis
m "\"Sorry, I can’t exactly turn my feelings off like you can.\""
show sam annoyed -talking with dis
wi "\"I meant that there’s a difference between what you need and what you want, when it comes to being backed into corners.\""
wi "\"He’s doing fine enough for himself compared to you.\""
show sam sad -talking with dis
wi "\"Or Nik.\""
wi "\"Cozy job, bartending in the most popular place in town.\""
show sam annoyed talking with dis
m "\"You really know how to make a man feel special.\""
show sam surprised -talking with dis
if ETHINT_Points == 1 or HARINT_Points == 1:
    wi "\"...We want to get into his office, Sam.\""
else:
    wi "\"...I want to get into his office, Sam.\""
show sam neutral talking with dis
m "\"His office?\""
show sam annoyed -talking with dis1
show sam annoyed talking with dis
m "\"That’s funny.\""
show sam annoyed -talking with dis
wi "\"Am I laughing?\""
show sam annoyed talking with dis
m "\"No, but I ought to be if you think you’re gettin’ in there.\""
show sam eyes -talking with dis1
show sam eyes talking with dis
m "\"He keeps his space locked tighter than the chastity cage Dora put on him.\""

if ETHINT_Points == 1 or HARINT_Points == 1:
    show sam neutral -talking with dis
    wi "\"Cynthia thinks she can get us in.\""
    "He shifts his shoulders and leans in."
    show sam annoyed -talking with dis
    wi "\"With your help.\""
    show sam annoyed talking with dis
    m "\"Really?\""
    show sam surprised -talking with dis
    "I hand him a bracelet with bits of bone and turquoise beads."
    wi "\"We’re going to use this bracelet to try to get him to open the window in his room.\""
    wi "\"We need you to convince him that bad things will happen if he doesn’t.\""
    show sam annoyed -talking with dis
    "His eyelids narrow."
    show sam annoyed talking with dis
    m "\"The man’s not stupid, William.\""
    show sam annoyed -talking with dis
    wi "\"But we think he might be deeply paranoid.\""
    show sam surprised talking with dis
    m "\"If that’s the case, you don’t think he’d come after me the first suspicion he has that somebody broke into his office?\""
    show sam surprised -talking with dis1
    show sam surprised talking with dis
    m "\"Christ’s sake, I {i}live{/i} here, William.\""
    show sam surprised -talking with dis
    wi "\"I could always just lock the place down and bust down the door.\""
    show sam neutral -talking with dis
    wi "\"Don’t think that would be very good for business though, or my relationship with the Madam.\""
    show sam annoyed -talking with dis
    "Sam runs off a slurry of curses under his breath."
    show sam eyes talking with dis
    m "\"You really think it’ll work?\""
    show sam neutral -talking with dis
    wi "\"If you’re a good enough actor, yeah.\""
    wi "\"All I want is five minutes.\""
    show sam neutral talking with dis
    m "\"I can try and get you that.\""
    show sam neutral -talking with dis
    wi "\"Let’s go, then.\""
    play sound ("sfx/clothrustle.ogg")
    "I pass the cold bracelet into his hot paw and he pockets it precariously."
    stop sound
    wi "\"I’ll climb my way inside once we’re ready.\""
    scene bg black with medium_dissolve
    $ quick_menu = True
    $ quick_menu_will = False
    $ willnote = False
    scene bg saloon2 with medium_dissolve
    "I can’t believe he just asked me to help him break into Harlan’s study."
    "But then again, it’s William."
    m "\"Jesus fuck.\""
    cl "\"Well, there are scholarly inquiries into his relationship with Mary Magdalene.\""
    show cli at center,saloon with dis3
    "I blink."
    "I can’t believe I forgot about Mr. Tibbits."
    show cli down with dis3
    m "\"It’s just an expression Mr. Tibbits.\""
    cl "\"I know!\""
    show cli serious with dis3
    cl "\"I was just trying to make you laugh.\""
    m "\"Well, ah, I’m sorry to kill the joy and all but I have to deal with some unpleasant work business.\""
    show cli eyes talking with dis
    cl "\"Oh don’t worry yourself!\""
    show cli blush eyes closed with dis1
    show cli blush eyes closed talking with dis
    cl "\"As it happens, I have somebody else to see very soon.\""
    show cli blush eyes closed with dis
    "Huh."
    show cli with dis
    m "\"Really?\""
    show cli talking with dis
    cl "\"Quite sure.\""
    show cli down with dis3
    cl "\"Once again pulled apart by timing, eh?\""
    show cli eyes talking with dis3
    cl "\"No matter! There’s tonight, after all.\""
    show cli with dis
    m "\"Tonight?\""
    m "\"What’s tonight?\""
    show cli talking with dis
    cl "\"Mr. Byrnes called it the Stag, did he not?\""
    show cli with dis
    m "\"Oh. Right.\""
    m "\"The Stag.\""
    hide cli with dis3
    "I had completely forgot about it after what happened today."
    "William probably has too."
    "Not that I think he’ll want to go, after getting caught up in the events today."
    "I really think he could use another break, though, after that all that."
    "Hell, {i}I{/i} could use a break."
    "...time to get this Harlan business over with."
    "I’m lucky enough that the crowd dies down just in time to take a seat at the bar."
    "A couple is chattering loudly next to me, and their table of friends is participating behind them."
    show har at halfright,saloon with dis3
    "Still, Harlan eventually finds time to make his way to me."
    show har eyes talking with dis
    ha "\"Drinks aren’t discounted today Mr. Ayers.\""
    show har with dis
    m "\"That’s alright.\""
    "I’m trying to think quick of what to say."
    m "\"I’ll still have one.\""
    m "\"I’m in a bad way.\""
    show har annoyed with dis
    "His glance flicks towards me."
    show har annoyed talking with dis
    ha "\"You’re not usually one for bellyaching, Mr. Ayers.\""
    show har with dis
    m "\"It’s a very unusual kind of night.\""
    show har eyes talking with dis
    ha "\"Sorry to hear.\""
    show har eyes with dis
    "He doesn’t look at me as he grabs the whiskey."
    show har eyes talking with dis
    ha "\"Pinch a nerve?\""
    show har with dis1
    show har talking with dis
    ha "\"This tends to help you manage.\""
    show har annoyed with dis
    m "\"I appreciate it, Mr. Perkins, but it’s not that kind of way.\""
    show har annoyed talking with dis
    ha "\"Then I can’t say I’m one for emotions, Mr. Ayers.\""
    show har annoyed with dis
    m "\"Emotions ain’t the problem neither.\""
    show har eyebrows with dis
    m "\"It’s spiritual.\""
    "His ears quirk."
    "Damn."
    "William might be right about this."
    show har talking with dis
    ha "\"Is something unusual ailing you?\""
    show har with dis
    m "\"Yeah.\""
    show har eyebrows with dis
    m "\"I’ve been hearing something scratching in the walls.\""
    "I don’t know why I say it."
    "Because I mean to be telling lies tonight, not the partial truth."
    "He stops pouring."
    show har eyes talking with dis
    ha "\"You too, then?\""
    show har with dis
    "He looks relieved."
    "But I suddenly feel a lot less so."
    m "\"I found a Meseta spirit woman who said those clawing sounds are the spirits of the unbaptized.\""
    m "\"She sold me a bracelet that might help drive them out.\""
    show har unamused with dis
    "Harlan snorts dismissively."
    show har unamused talking with dis
    ha "\"Most likely nonsense.\""
    show har unamused with dis1
    show har unamused talking with dis
    ha "\"Any fraud with a chisel and bones in their pocket can fake genuine Meseta talismans.\""
    show har unamused with dis
    m "\"Well I have one right here.\""
    show har unamused talking with dis
    ha "\"Let’s see it, then.\""
    show har unamused with dis
    "I take it out of my pocket and flash it at him."
    show har eyebrows with dis
    "His eyes go wide."
    show har talking with dis
    ha "\"That’s genuine.\""
    show har with dis1
    show har talking with dis
    ha "\"There’s real turquoise...\""
    show har eyes with dis1
    show har eyes talking with dis
    ha "\"And I recognize that engraving!\""
    show har with dis1
    show har talking with dis
    ha "\"Boy...\""
    show har with dis1
    show har angry talking with dis
    ha "\"You must tell me what this shaman told you.\""
    show har with dis
    "I pretend to be concerned."
    m "\"Maybe it should wait until you’re off the job?\""
    show har angry talking with dis
    ha "\"JULIA!\""
    show har angrier with dis
    "An alarmed looking squirrel holding four mugs of beer in her hand looks his way."
    show har with dis1
    show har angry talking with dis
    ha "\"Ten minutes.\""
    show har with dis1
    show har angry talking with dis
    ha "\"Cover me.\""
    show har with dis
    "She nods quickly, and before I can speak he's lifting the latch on the bar."
    show har eyes talking with dis
    ha "\"Let’s go to the hallway...\""
    show har eyes with dis1
    hide har with dis3
    "He doesn't wait for me to agree, but I follow."
    stop music fadeout 5.0
    scene bg saloonhallway
    show har at center,saloon
    with dissolve
    "Once I'm there, he looks at my pocket again."
    show har angry talking with dis
    ha "\"Take it out.\""
    show har with dis
    "I don’t hesitate."
    "It jangles pleasantly when I hold it in my hand."
    "Will said this was one of her worst ones, supposedly."
    "Cynthia does a really good job with these."
    show har angry talking with dis
    play music ("music/contemplation.ogg") fadein 3.0
    ha "\"Now I want you to tell me exactly what this shaman said.\""
    show har with dis
    m "\"Right...\""
    m "\"Let me try and remember.\""
    "It’s time to engineer an incredible lie."
    m "\"The first thing she told me was that souls of the lost get real sore about not bein’ in buildings.\""
    m "\"Home is something they used to know and miss.\""
    m "\"And more importantly, our structures are full of living people.\""
    show har talking with dis
    ha "\"So what?\""
    show har with dis
    m "\"So...\""
    m "\"They want to be near those people...\""
    m "\"Especially ones they can hurt, or...\""
    show har eyebrows with dis
    m "\"Or ones they think are close to death.\""
    "He’s taken aback by that."
    show har annoyed talking with dis
    ha "\"And how would they know who is or isn’t close to death?\""
    show har with dis
    m "\"Can’t say.\""
    m "\"And didn’t ask.\""
    "I keep thinking he’s going to scoff and walk away at any minute."
    "But he’s still listening."

    m "\"Spirits are part of this world, but also part of another.\""
    m "\"Which is why they can move through some things but get stuck in other things.\""
    show har angry talking with dis
    ha "\"How so?\""
    show har with dis
    m "\"She said sometimes they can move through floorboards and bodies like they’re made of water.\""
    "Bullshit."

    m "\"Sometimes it’s like the walls are like hard rock.\""
    "Bullshit!"

    m "\"And then there’s in-betweens where sometimes that hard rock gets more like spring puddin'.\""

    m "\"At any time, these mediums can go back to rock again and they get trapped.\""
    "Pure bullshit!"
    show har talking with dis
    ha "\"So how would one get rid of them if they’re stuck in something as hard as rock?\""
    show har with dis
    m "\"Well, according to her, it’s easiest for them to enter your body while you’re dreaming.\""

    m "\"That’s when they can do the most harm, and try to hitch a ride quicker by shortening your life.\""


    m "\"So a lot of them get drawn to where you sleep the most.\""
    show har talking with dis
    ha "\"Well I sleep in my study.\""
    show har with dis
    m "\"I see.\""

    m "\"That should work.\""

    m "\"The first thing we have to do is to go on in there and open your window.\""

    "The hare doesn’t wait to ask for an explanation why."
    play sound ("sfx/keytake.ogg")
    show har eyes with dis
    "He’s already fumbling with the keys on his belt loop, searching for the right one to his study."
    stop sound
    show har with dis
    "I follow him through the hall to the big door."
    play sound ("sfx/keyopen.ogg")
    queue sound ("sfx/dooropen.ogg")
    "He opens it wide, about to close it again from the inside."

    m "\"You should always leave it open a crack.\""
    "I lick my lips, nervously."

    m "\"For the spirits that are stuck to slip on through.\""
    show har angry with dis
    "The hares lips tighten, but he nods."
    hide har with dis3
    "As I look into the room from the outside, and his body is turned away from me, two shadows in front of me slip inside."
    "All of the hairs on the back of my neck stand up, because I’m starting to believe my own bullshit."
    "...But then I can see that it’s just Will and Cynthia."
    "Cynthia being that quiet is one thing, but considering how big Will is, it’s a little unnerving."
    show har at center,saloon with dis3
    "They’re crouching behind some furniture in the dark as Harlan turns around, walking towards me."
    scene bg black with medium_dissolve

    $ quick_menu = False
    $ quick_menu_will = True
    $ willnote = True
    scene bg black with medium_dissolve
    scene harlanoffice with medium_dissolve
    "He’s walking away from me now."

    "I can hear him chastise Sam, as close as he is."

    ha "\"You don’t need to look in there.\""

    "I pull out a pair of leather gloves and put them on as quickly and quietly as I know how."
    "Harlan seems like the type to check for smudges."

    m "\"Sorry.\""

    m "\"I just wanted to make sure you were doing it right.\""

    ha "\"...Opening a window?\""

    m "\"Well, the medium said the panes need to be perpendickalur to make sure they don’t snag the spirits.\""

    show cyn surprised a at right,dark3a with dis3
    cy "\"Oh.\""
    show cyn fear a with dis
    cy "\"He’s still going.\""

    show cyn serious a with dis
    wi "\"Ignore Sam.\""


    wi "\"Help me look.\""


    wi "\"Just five minutes and we have to jump out of the window.\""
    show cyn annoyed a with dis
    cy "\"I’m pretty sure I’ll have no problem making myself scarce when he gets too close.\""
    show cyn serious a with dis
    "His desk seems like the most obvious place to check."
    "There’s an in and out box for mundane business papers."
    "But the drawer is where things starts to get interesting."
    $ hledgertext = "Names. Addresses. Companions. I could probably track down half the city with all of this information."
    "There’s a little black binder that looks freshly purchased in one of his drawers."
    $ update_unlocked_pages(1, 27)
    $ renpy.notify("Notebook updated.")
    "When I open it up it just has names and dates for various people, and identifying information."

    wi "\"Come take a look at this.\""

    "She tiptoes over and glances down at the pages."
    show cyn surprised a with dis
    cy "\"Oh.\""

    cy "\"That’s a copy of Dora’s book.\""
    show cyn serious a with dis
    cy "\"Sort of like the one you had.\""

    wi "\"So you looked through everything on my desk.\""
    show cyn annoyed a with dis
    "Her lips thin."

    wi "\"Right. Of course you’d all know about that.\""

    cy "\"Hip workers really aren't the best at keeping secrets.\""

    cy "\"Especially the ones people can use against us.\""

    "I can’t waste any time by talking about that now."
    show cyn serious a with dis
    wi "\"Why does he have this?\""

    wi "\"I thought he could look at Dora’s book any time.\""
    show cyn fear a with dis
    "She shakes her head."
    cy "\"See, he’s not supposed to, actually.\""
    show cyn serious a with dis
    cy "\"Dora doesn’t ever let anybody look at the whole book, for obvious reasons I’m sure you can imagine.\""
    show cyn angry a with dis
    cy "\"She’d fire him for this alone.\""
    show cyn serious a with dis
    "Sam’s voice echoes from the hall behind us."

    m "\"...Holding the bracelet puts you on a spiritual level that makes your whole body seem like a soul rather than a vessel.\""

    wi "\"You can’t take that book.\""

    wi "\"He’d know somebody was here.\""
    show cyn fear a with dis
    cy "\"And you’re afraid he’d go after Sam?\""
    show cyn sad a with dis3
    wi "\"Yes.\""

    m "\"If we take big, slow paces, the arms stuck in the walls will have to force themselves towards us.\""
    show cyn serious a with dis3
    "She pats the book with the bottom of her palm covered by her sleeve."

    cy "\"I wish you cared about the rest of us as much as you seem to care about him.\""

    cy "\"But at least you do seem to care about somebody else.\""

    "Sam’s voice is getting closer."

    m "\"The flow of the movement will sweep them out of the house and into the heavens.\""

    wi "\"Hey.\""

    wi "\"If you want to take the book and blow our cover, be my guest.\""
    hide cyn with dis3
    "She walks away."

    "I put the book back in its drawer."
    #sfx
    "But as I put it back in its place, the wooden panel beneath it bounces."

    "I don’t hesitate for long."

    "I take the book out again, then the wood."

    "There’s papers here."

    "The top looks most recent."
    "I sketch as many details as I can."

    "A Huaxian name sticks out."

    "Chang Fulin."
    $ hlettertext = "The mafia uses these pictures as intimidating messeages. Nobody wants to wake up to these in their mail. I imagine Chang Fulin didn't, whoever he is."
    "But most importantly, I copy down the drawings."
    $ update_unlocked_pages(1, 28)
    $ renpy.notify("Notebook updated.")
    "I know these drawings."

    "Why are these drawings here?"

    "My body gets cold from the sudden sweat it's making."
    show cyn surprised a at right,dark3a with dis3
    wi "\"Cynthia...\""
    wi "\"What do these pictures look like to you?\""
    show cyn serious a with dis
    "She hems."
    show cyn annoyed a with dis
    cy "\"Looks kind of like a doodle of a knife stabbing a hand.\""
    show cyn serious a with dis
    wi "\"Yeah, that’s what I thought.\""
    "She shrugs."
    cy "\"Not the best drawing though.\""
    show cyn fear a with dis
    "She must notice my expression, because she looks at my face rather suddenly."
    cy "\"Something the matter?\""

    "Sam’s voice lingers near the doorway."

    m "\"Almost there.\""
    hide cyn with dis3
    wi "\"...I don’t think we have much time left.\""

    "She doesn’t bother responding considering she’s already halfway out of the window."
    wi "\"Shit.\""

    "I manage to put everything back in its place within a few seconds."

    "By the time I reach the wall, Cynthia’s clear of the window exit."
    play sound ("sfx/doorcreakopen.ogg")
    "I swing one leg over the other, twisting my tail and body through the opening, and lower myself to a crouch as the door creaks open."
    "We walk quickly and quietly by, out of sight."
    stop music fadeout 3.0
    scene bg black with dis3
    "Then the two of us walk side-by-side into the entrance of the Hip, not looking at one another, as if nothing had ever happened."
    play music ("music/saloonpiano.ogg") fadein 3.0
    scene bg saloon2 with dissolve

else:
    show sam annoyed -talking with dis
    wi "\"Do you think Harlan has secrets?\""
    show sam annoyed talking with dis
    m "\"Everybody does.\""
    show sam neutral -talking with dis
    wi "\"Relevant to the case I mean.\""
    show sam neutral talking with dis
    m "\"I don’t really know.\""
    show sam neutral -talking with dis1
    show sam neutral talking with dis
    m "\"He ain’t ever been the nicest fella, but he’s fair enough if you don’t give him any trouble.\""
    show sam eyes -talking with dis1
    show sam eyes talking with dis
    m "\"Keeps to himself.\""
    show sam annoyed -talking with dis
    wi "\"So you trust him?\""
    "He taps the table."
    show sam annoyed talking with dis
    m "\"I didn’t say that.\""
    show sam neutral -talking with dis
    wi "\"Enough for you to think he’s not suspicious, I mean.\""
    show sam eyes talking with dis
    m "\"Cynthia doesn’t trust him.\""
    show sam neutral -talking with dis
    wi "\"And what about you?\""
    show sam neutral talking with dis
    m "\"I consider most of Cynthia’s judgments good enough to be considered what I believe, more likely than not.\""
    show sam neutral -talking with dis
    wi "\"Any exceptions?\""
    show sam eyes -talking with dis
    "He shrugs."
    show sam eyes talking with dis
    m "\"There’s you I suppose.\""
    show sam smile with dis
    "He grins."
    wi "\"I don’t need everybody to like me.\""
    show sam neutral talking with dis
    m "\"So long as I like you, Sheriff.\""
    show sam smile with dis
    wi "\"Don’t get me hot in public, Sam.\""
    show sam neutral talking with dis
    m "\"It’s the desert, William.\""
    show sam neutral -talking with dis1
    show sam neutral talking with dis
    m "\"Everybody’s hot.\""
    show sam smile with dis
    "He knows what I mean, so he doesn’t get the dignity of a response."


play background ("sfx/crowd.ogg") fadein 6.0
"Rather than calming down, the energy in the bar keeps ramping up."
"The overcrowding there spills into the stage area and I can hear some performers start to speak up."

if ETHINT_Points == 1 or HARINT_Points == 1:
    show sam neutral -talking at center,saloon with dis3
    "Sam’s gone back to his usual spot and thankfully saved my seat."
    show sam surprised -talking with dis
    "He gives me a look like he wants to know how everything went."
    show sam neutral -talking with dis
    "I give him a look letting him know we can’t talk about it here or now."
else:
    show sam neutral -talking with dis
    "I kick back in the chair and fold my arms behind my head."
show sam neutral talking with dis
m "\"There’s your deputy.\""
show sam neutral -talking with dis
"A very confused looking otter is talking with Cynthia."
wi "\"Todd!\""
$ renpy.music.set_volume(0.4, delay=3.0, channel='background')
show sam neutral -talking at center with dis3:
    xzoom-1
show tod annoyed at right,saloon with dis3
"The voices in the bar quiet down a bit after I shout."
"But the noise recovers quickly and the otter comes rushing towards us."

show tod talking with dis
to "\"There ya are, sir.\""
show tod with dis1
show tod talking with dis
to "\"I did a thorough check on the Greene house and logged the necessary evidence.\""
$ renpy.music.set_volume(1.0, delay=25.0, channel='background')
show tod annoyed with dis
wi "\"Did Marcy make it home?\""
show tod sigh with dis3
to "\"For now.\""
wi "\"Good.\""
show tod surprised with dis3
wi "\"If she comes off her sickness, she’ll probably have more to tell us.\""
wi "\"We'll need to pay her a follow-up visit tomorrow.\""
show tod sad with dis3
"The otter droops."
to "\"I don’t want to step on any toes or nothin’, sir, but don’t you think she’s done enough?\""
"I shake my head."
wi "\"She's given us the lead we need to follow.\""
show tod surprised with dis3
show sam annoyed -talking with dis
to "\"I just don’t think you should press her too hard if you get the chance to speak to her again.\""
show sam neutral -talking with dis
wi "\"I understand your feelings considering you grew up around her.\""
wi "\"But if there’s more she wants to share, the more we know the better.\""
#adjust
"He’s shifting a bit in his seat."
to "\"I, uh...\""
show tod sad with dis3
"He lowers his voice."
to "\"I just wanted to say sorry again for what we...\""
show sam annoyed -talking with dis
"Sam scowls at him."
show tod surprised with dis3
to "\"For what I did today.\""
show tod sad with dis3
to "\"It really, really won't happen--\""
show tod surprised with dis3
wi "\"Save your breath.\""
wi "\"There's no need to worry about that now.\""
show tod sigh with dis3
to "\"Well, I just mean...\""
to "\"I was in a pretty good mood, because I thought things were going to be better for her from now on.\""
to "\"I don't think I gave it as much attention as I maybe should have.\""
show tod surprised with dis3
to "\"I just got carried away since...\""
show tod sigh with dis3
to "\"I mean I had never...\""
to "\"For now.\""
show tod surprised with dis3
"He looks at Sam."
to "\"And the two of you, well.\""
wi "\"Well, what?\""
"He looks between me and Sam again."
to "\"Well, you know...\""
show tod sad with dis3
"He clears his throat and slicks down the fur on his forehead, as if searching for a way to change the subject."
show tod surprised with dis3
to "\"Either way.\""
show tod sad with dis3
to "\"I just hope there’s better things in store for poor old Marcy.\""
show tod sigh with dis
to "\"I reckon Mr. Green’s soul is hopping on charcoal by now.\""
to "\"She’ll do better going forward.\""
show tod surprised with dis3
show sam annoyed talking with dis3
m "\"Sounds like there’s something you don’t want her to say.\""
show sam annoyed -talking with dis
to "\"Huh?\""
show sam neutral talking with dis
m "\"About Mr. Greene, I mean.\""
show sam neutral -talking with dis
"He scratches the back of his neck."
to "\"Not sure where you got that idea from.\""
show sam eyes talking with dis
m "\"You just keep discouraging us from the notion of talking to her again, is all.\""
show sam neutral -talking with dis
"He shifts again."
show tod sigh with dis3
to "\"Naw.\""
show tod surprised with dis3
to "\"I’m just real concerned about her, is all!\""
show sam annoyed -talking with dis
to "\"She’s the bees knees, really.\""
"Todd looks nervous."
"Sam looks doubtful."
"Maybe Sam is on to something about Todd."
"Maybe there was something else going on between him, Marcy, and Mr. Greene."
"Can't say I have any guesses yet, though."
show tod annoyed with dis
wi "\"You really didn’t like Mr. Greene, did you Todd?\""
to "\"Well ma and pa tell me that it’s important to like everybody, no matter how hard it can be.\""
show tod sigh with dis3
to "\"But sometimes it’s {i}real{/i} hard.\""
show tod with dis3
"He whistles and laughs."
show sam annoyed talking with dis
m "\"There's no chance you knew she was taking that medicine, did you?\""
show sam annoyed -talking with dis
"His tone gets harsher."
show tod sigh with dis3
to "\"No, not really.\""
show tod annoyed with dis3
"The cougar shrugs and drops it."
"I can tell Sam isn’t going to push it any further."
"Now I’m {i}definitely{/i} going to want to talk to her when she’s able to speak again."
show tod surprised behind sam with dis3
show sam surprised -talking with dis3
show nik smile at left,saloon behind sam with dis3:
    xzoom-1
ni "\"Good afternoon boys.\""
show sam surprised
show nik surprised
show sam shocked at centerright:
    xzoom 1
with vpunch
"Sam flinches and lets out a genuine shout which makes us all look at him."
show nik sidelook with dis3
show sam sad -talking with dis3
"His ears lower."
show tod annoyed with dis
show sam sad talking with dis
m "\"Sorry.\""
show sam surprised -talking with dis1
show nik neutral flaccid hoff with dis3
show sam surprised talking with dis3
m "\"Just surprised.\""
show sam surprised -talking with dis3
show nik eyestalking with dis3
ni "\"I am known to be very scary.\""
show sam neutral -talking with dis
show nik neutral flaccid hoff with dis
wi "\"This is the first time you got the jump on me too.\""
wi "\"Somebody as big as you shouldn’t be able to do that.\""
show nik eyes with dis
"Nik shrugs."
show nik talking with dis
ni "\"I am very familiar with this bar.\""
show nik neutral flaccid hoff with dis
show sam neutral talking with dis
m "\"Ain’t you usually at the mine still?\""
show sam neutral -talking with dis
show nik talking with dis
ni "\"Not today.\""
show nik eyes with dis1
show nik eyestalking with dis
ni "\"It is a strike, Samuel.\""
show nik neutral flaccid hoff with dis
show sam neutral talking with dis
m "\"So you don’t have to go into work, I take it?\""
show sam surprised -talking with dis
wi "\"He also don’t get paid, Sam.\""
show sam sad talking with dis
m "\"Well, shit.\""
show sam neutral -talking with dis
show nik smile with dis
ni "\"But there is good news.\""
show tod sigh with dis3
to "\"We could use some of that.\""
show tod annoyed with dis3
show sam neutral talking with dis3
m "\"Yes.\""
show sam neutral -talking with dis
"I sigh."
wi "\"Agreed.\""
ni "\"Negotiations are going somewhere.\""
ni "\"A twenty cent hourly raise will be added for everybody in the company.\""
show tod eyes happy with dis
"Todd whistles."
show tod with dis
wi "\"Now that’s what I like to hear.\""
"I raise my glass and Todd meets it."
wi "\"Good on y’all.\""
show sam annoyed talking with dis
m "\"Should still be higher.\""
show sam neutral -talking with dis
show nik eyestalking with dis
ni "\"I agree, but we expected nothing.\""
show nik neutral flaccid hoff with dis
show tod talking with dis
to "\"Something is always better than nothing.\""
show tod surprised with dis
show sam eyes talking with dis
m "\"Not the case with diseases.\""
show sam neutral -talking with dis3
show nik sidelook with dis3
show tod annoyed with dis3
ni "\"Oh, lighten up, Sam.\""
ni "\"Victories, however small, should be noticed.\""
show nik neutral flaccid hoff with dis3
wi "\"Yeah, lighten up.\""
show sam neutral talking with dis
m "\"I’ll just be glad they’re not robbing you as much.\""
show sam neutral -talking with dis
wi "\"Anyway, why don’t you grab a drink with us to celebrate?\""
wi "\"You can tell us why you showed up here.\""
show nik sidelook with dis3
ni "\"Well, I usually come here first to get Sam.\""
show nik disappointed with dis3
ni "\"Then I walk him over to your office.\""
show nik smile with dis3
ni "\"Thankfully, since you’re already here, I won’t have to make the extra effort.\""
show nik neutral flaccid hoff with dis
wi "\"I meant what for.\""
wi "\"You know... the occasion?\""
show nik sidelook with dis3
"He hums."
show nik talking with dis3
show sam surprised -talking with dis3
show tod surprised with dis3
ni "\"...For our nightly plans.\""
show nik neutral flaccid hoff with dis
"I try to focus for a moment."
wi "\"What do you mean, {i}‘nightly plans’{/i}?\""
show nik talking with dis
ni "\"For the Stag tonight.\""
show nik neutral flaccid hoff with dis
"Oh fuck."
"I completely forgot."
"By the looks on Sam and Todd’s face, they're a little overwhelmed."
show tod sigh with dis3
to "\"Ain’t that place a bit rough and tumble?\""
show tod surprised with dis
show sam eyes talking with dis
m "\"Things tend to get rough when you take a tumble.\""
show sam neutral -talking with dis3
show tod annoyed with dis3
wi "\"I don’t know if I have the energy to go to another dance hall tonight, Nik.\""
show nik sidelook with dis3
ni "\"Hrm.\""
ni "\"But it would be a shame to see you miss another opportunity to see it at night with all of us together.\""
show nik neutral flaccid hoff with dis3
wi "\"Well, we’ve had a long day.\""
wi "\"And there’s a lot of things I need to think about regarding Mr. Tibbits’ case.\""
show nik disappointed with dis3
ni "\"Okay, okay.\""
show nik eyestalking with dis3
ni "\"No pressure.\""
show nik neutral flaccid hoff with dis

if ETHINT_Points == 1 or HARINT_Points == 1:
    show sam eyes -talking with dis
    wi "\"Maybe you can help me with something.\""
    show nik talking with dis
    ni "\"Oh?\""
    show nik neutral flaccid hoff with dis
    wi "\"This question applies to you too Todd, so listen up.\""
    show tod annoyed with dis
    to "\"Yessir.\""
    show sam neutral -talking with dis
    wi "\"And you, Sam.\""
    "He’s on what looks like his second drink and he perks up."
    m "\"Mmm.\""
    wi "\"I ran across a peculiar name recently.\""
    wi "\"Not sure if I’m pronouncing it correctly, but I'll say it how it was spelled: Chang Fulin.\""
    show sam eyes talking with dis
    m "\"Nope.\""
    show sam neutral -talking with dis3
    show tod sigh with dis
    to "\"Sorry, boss.\""
    show tod annoyed with dis3
    show nik smile with dis3
    "Nik is smirking a nasty little smirk."
    ni "\"I know him.\""
    "I feel a shot of energy run through my body."
    wi "\"You do?\""
    ni "\"He is a friend of a friend, so to speak.\""
    ni "\"And he will be at the Stag most nights.\""
    "I groan."
    show nik eyessmile with dis
    ni "\"Looks like you’ll be coming with us tonight, after all?\""
    show nik smile with dis
    wi "\"Looking more and more likely...\""
else:
    "My cup has been empty for too long."

show sam surprised -talking with dis
"I take a sip of the beer next to mine on the table."
show sam annoyed talking with dis
m "\"That’s mine.\""
show sam annoyed -talking with dis
wi "\"I need it more than you right now.\""
"I take a big swig of his drink."
show tod surprised with dis3
show nik sidelook with dis3
show sam eyes talking with dis3
m "\"Hope you like the taste of my spit, then.\""
show sam neutral -talking with dis
"Todd gulps and Nikolai avoids eye contact with everybody."
wi "\"Good thing alcohol tends to clean even the dirtiest of mouths.\""
show sam neutral talking with dis
m "\"You and I know the proof on that beer is less than four percent.\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"You’re not tasting just my spit with a proof that low.\""
show sam smile with dis
"He leans over and whispers into my ear."
show sam eyes talking with dis
m "\"I’m talking about the {i}balls{/i} I’ve licked, William.\""
show sam smile with dis
wi "\"I know you dream about me lickin’ balls.\""
show sam neutral talking with dis
m "\"So why keep me waitin’?\""
show sam smile with dis
"I sigh."
"I wish I could answer that right now."
"But I don’t want to spoil the mood."
"So I just decide to act cheeky."
wi "\"Because I never need to make you finish.\""
show nik talking with dis3
ni "\"What are you both whispering about?\""
show nik neutral flaccid hoff with dis
wi "\"Nothing for the ears of God, or civilized company.\""
show sam neutral -talking with dis3
show tod sigh with dis3
to "\"I’m sure he wouldn’t be mad at us forever just for a little bit of indecency here and there.\""
show tod with dis3
show sam annoyed talking with dis
m "\"That’s a bold presumption to make.\""
show sam annoyed -talking with dis
show tod talking with dis
to "\"Well, I just thought about it for a spell.\""
show tod with dis
show sam eyes talking with dis
m "\"He just thought about it for a spell.\""
show sam annoyed -talking with dis
"Sam clearly isn’t impressed."
show tod talking with dis
to "\"And I came up with this.\""
show tod sigh with dis
to "\"I can get mad about somethin’ that happened yesterday.\""
show tod talking with dis3
to "\"But when I think about something rude somebody said to me six to seven months ago, I’m barely sore about it.\""
show tod with dis1
show tod talking with dis
to "\"If God exists for forever, and has forever to sit and think on things, there must be way too many things to stay mad about forever.\""
show tod with dis
show sam annoyed talking with dis
m "\"So you’re sayin’ that instead of Jesus nailing his wrists to a cross to die for our sins, he should have just waited it out.\""
show sam annoyed -talking with dis
show tod talking with dis
to "\"More or less, maybe!\""
show tod with dis
show sam annoyed talking with dis
m "\"And people say I’m morbid when I talk.\""
show sam eyes -talking with dis1
show sam eyes talking with dis
m "\"What does Nikolai think about it?\""
show sam neutral -talking with dis
show tod eyes happy with dis
to "\"Yeah, I’d love to hear another perspective.\""
show tod with dis
wi "\"Yeah Nik.\""
wi "\"Enlighten them.\""
show nik talking with dis
ni "\"Who, me?\""
show nik neutral flaccid hoff with dis
wi "\"Didn’t know there was another Nik at the table.\""
show nik disappointed with dis3
ni "\"Hurm.\""
show nik sidelook with dis3
ni "\"I do not know God.\""
ni "\"And he does not know me.\""
show tod surprised with dis3
show nik eyestalking with dis3
ni "\"But if he ever shows up to see me, I will say hello.\""
show nik neutral flaccid hoff with dis
wi "\"Well then...\""
wi "\"The alcohol has passed on to somebody else, there’s Bible talk, and I’m sweating plenty, so this might as well be church.\""
show tod annoyed with dis
wi "\"I think I’m going to step outside for a bit of air.\""
wi "\"Want to join me, Nik?\""
show nik eyestalking with dis
ni "\"No.\""
show nik smile with dis
ni "\"I am invested in the conclusion of the discussion.\""
wi "\"Alright then.\""
wi "\"I’ll be back after a smoke or two.\""
stop music fadeout 2.5
stop background fadeout 2.5
scene bg saloonoutside with medium_dissolve
"The plants and the fancy seats on the front porch of the Hip make for a cozy space to sit."
"But it might be a fruitless endeavor, considering all the alcohol and the pussy is inside of the building, which makes it where everybody really wants to be."
"People give me looks as they pass me by, but I just ignore them, rustling through my pockets."
"There’s a thick cigar I’ve been saving for a stressful situation."
"I don’t take it out just yet."
"I’ve had far worse days than this one."
play sound ("sfx/match.ogg")
"So I fish around for a slim stick in a pack instead, pluck it out, and go ahead and light it."
stop sound
"A rush of relief flows through me as I inhale."
"And then blow."
"Not the kind of blowing Sam was talking about though."
play music ("music/a-moment-of-solace.ogg") fadein 3.0
"But if I ever did want to try that again, I think I might want it to be with him."
"Or at least have him near me when I did."
"He’s anxious about a lot of things, but never the act."
"And that confidence is contagious."
"There’s something about how he moves, and how he smells, and all the noises he makes that helps my body wake up."
"But if I indulge too much in those pleasures we're bound to get caught."
"I don't want anything to happen to him because I couldn't keep it in my pants enough."
show mur smile with dissolve
show mur talking with dis
mu "\"Hello, Sheriff.\""
show mur smile with dis
"Oh."
"The Byrnes boy."
"I forgot he was going to show up too."
wi "\"Spotted me quick.\""
show mur mischief with dis
mu "\"Just figures you’d be all by yourself in the most popular place in the city.\""
show mur smile with dis
wi "\"That so?\""
"I puff my cigarette again."
"And I start thinking about men sucking cock again."
"Word of mouth tells me the Byrnes boy’s certainly sucked a lot."
"Maybe even more than Samuel."
"And as ashamed as I am to admit it, that excites me."
"He has a good looking muzzle for it."
"And he’s a canine, like me."
"Canines know what canines like."
"He could probably do things for me even Sam couldn’t."
"But he’s a forbidden fruit, so to speak."
"A healthy working relationship with his father is neccessary to make my job possible."
"And I don’t even want to think about getting entangled with whatever his mother gets up to."
show mur sideeye with dis3
mu "\"You just going to stare, or are you going to fill me in on what that business at the store was about?\""
"Probably nothing good about your family if the evidence keeps stacking up."
show mur concerned d with dis
wi "\"You don’t have to worry about it.\""
"That's probably not true, but worrying never helps nobody anyhow."
mu "\"I don’t think I’d have to if you were straight with me.\""
wi "\"Sorry buddy.\""
wi "\"I don’t have a full picture.\""
wi "\"I know pieces.\""
wi "\"There anything specific you want to know?\""
show mur fear d with dis
mu "\"Is my mother under arrest?\""
show mur concerned d with dis
"I roll my eyes."
wi "\"I don’t think I have the power to do so unless she starts walking around with severed heads.\""
wi "\"And it would have to be the severed heads of people who would be missed.\""
wi "\"That make you feel any better?\""
show mur sideeye with dis
mu "\"Strangely?\""
mu "\"Yes.\""
play sound ("sfx/clothrustle.ogg")
show mur concerned d at right with dis3
"He takes a seat next to me."
stop sound
"There’s an odd smell to him."
"On the surface it's like lemons and a crisply washed clothing."
"But beneath it’s a sickly, sweaty smell."
"The kind of sweaty you get from having a fever, not from a brisk jog."
wi "\"You seem off.\""
show mur sideeye with dis
mu "\"Oh.\""
show mur fear d with dis
mu "\"Do I look bad?\""
show mur concerned d with dis
wi "\"You look great, actually.\""
wi "\"But the smell gives you away.\""
show mur eyes with dis
mu "\"I picked a pretty lousy time to get sick, didn’t I?\""
show mur concerned d with dis
wi "\"Getting shot in the arm will do that to you.\""
show mur sideeye with dis
mu "\"Well, it’ll have to be ignored.\""
mu "\"My sister’s wedding is in a few days and they won’t be able to prepare without me.\""
show mur concerned d with dis
wi "\"I’d think a family like yours could hire some labor.\""
play sound ("sfx/clothrustle.ogg")
show mur concerned d at center with dis3
#adjust
"He finds a wicker chair across from me and takes a seat."
stop sound
show mur eyes talking with dis
mu "\"Laborers are great for moving things, but not so good at helping with logistical problems.\""
show mur sideeye with dis
mu "\"Or aesthetic ones, for the photographs.\""
"I nod at him."
wi "\"So you’re still going to play as hard as you work tonight?\""
show mur eyes with dis
mu "\"If I’m doing one I might as well do the other.\""
show mur mischief with dis3
mu "\"And seeing how you act when we get you smashed at the Stag is too good of an opportunity to pass up.\""
show mur smile with dis
wi "\"And you think you can handle that?\""
show mur talking with dis
mu "\"I guess I’ll see.\""
show mur smile with dis
"I chuckle."
"Then I frown again and lower my voice."
wi "\"Mind if I ask you some personal questions?\""
show mur talking with dis
mu "\"I'm surprised. But not at all.\""
show mur sideeye with dis3
mu "\"Frankly I wish you did more often.\""
wi "\"You seem like somebody who loves who you want, as much as you want.\""
wi "\"And I think you know what I really mean when I say ‘love.’\""
wi "\"What do you get out of that exactly?\""
"We wait for a group of six to pass through the door before he answers."
show mur eyes talking with dis
mu "\"All I know is I feel whole when I do it.\""
show mur eyes with dis1
show mur eyes talking with dis
mu "\"Like I’m where I’m meant to be, and it’s just that simple.\""
show mur sideeye with dis
wi "\"But what about after when somebody sees you like a thing instead of a person?\""
"He shrugs."
mu "\"It helps being picky, you know.\""
mu "\"And God knows I get enough interest that I can be.\""
show mur eyes with dis
mu "\"I finish, then move onto somebody else.\""
wi "\"Keep the details near and dear to your heart, if you don’t mind.\""
show mur mischief with dis3
mu "\"It’s too bad you don’t want to know.\""
show mur smile with dis
"Mr. Byrnes, it’s not that I don’t want to know."
"It’s that I probably shouldn’t know."
show mur mischief with dis
mu "\"Somebody as vicious as you would probably split me open, but I think I’d enjoy it while it lasts.\""
show mur sideeye with dis3
wi "\"There will be no deaths in any more bedrooms while I’m around.\""
mu "\"You were almost fun for just a second.\""
mu "\"I can swear that a flicker of it was there.\""
wi "\"Go splash some water on yourself in the bathroom.\""
show mur eyes talking with dis
mu "\"Anyways, where’s Sam and Cliff?\""
show mur sideeye with dis
wi "\"I think Mr. Tibbits is busy with one of the women upstairs.\""
show mur fear d with dis
mu "\"But we were at it three times yesterday.\""
show mur sideeye with dis
wi "\"I’m very happy for you, Mr. Byrnes.\""
mu "\"Yeah yeah yeah.\""
wi "\"Sam should be in his usual spot.\""
mu "\"I don’t know Sam’s usual spot.\""
wi "\"It’s the corner of the bar in the alcove with the round table.\""
show mur with dis
mu "\"You must pay attention to him a lot if you know that.\""
show mur smile with dis3
wi "\"I pay attention to a lot of things.\""
show mur mischief with dis
mu "\"I’m just saying...\""
mu "\"You should probably ask Sam what you were asking me.\""
show mur smile with dis
"I take another puff of my cigarette."
"Hard this time."
"Then I blow."
wi "\"Well, I also don’t want to die of embarrassment before the conspirators come for me.\""
show mur sideeye with dis3
mu "\"And you weren’t with me?\""
wi "\"You’re professional.\""
wi "\"It’s different.\""
mu "\"Sam is by definition a professional.\""
mu "\"And his profession is particularly applicable to these sorts of things, more than mine.\""
"I shake my head."
wi "\"It’s complicated.\""
show mur concerned d with dis
mu "\"Then want to unpack that a bit?\""
wi "\"No.\""
show mur eyes talking with dis
"He sighs."
show mur sideeye with dis
mu "\"First thing I’m doing is sending Sam out.\""
wi "\"You don’t--.\""
show mur concerned d with dis
mu "\"Second thing I’m doing is finding which room Mr. Tibbits is in, so nobody's going to strangle him with a makeshift noose made of stockings.\""
wi "\"Jesus, Murdoch.\""
play sound ("sfx/saloonbackdoor.ogg")
hide mur with dis3
"He’s already gone by the time I’m down to the butt with this cigarette."
"If I talk about this then I know Sam will get ideas."
stop sound
"Which means that I’m going to really have to talk about it."
show sam neutral -talking with dis3
"Sooner rather than later, he comes along."
show sam neutral talking with dis
m "\"The fox sent me out here.\""
show sam neutral -talking with dis
wi "\"I know.\""
wi "\"He seemed very insistent on doing so.\""
show sam neutral talking with dis
m "\"We don’t have to talk about anything if you don’t want to.\""
show sam eyes -talking with dis1
show sam eyes talking with dis
m "\"Sometimes silence is good.\""
show sam eyes -talking with dis
wi "\"I like the silence with you.\""
show sam smile with dis
"He smiles at me."
"We watch the clouds roll by as the sky turns from blue to pink and the people pass us by."
wi "\"A man's been flirtin' with me.\""
show sam neutral talking with dis
m "\"That happens to me all the time.\""
show sam neutral -talking with dis
wi "\"Well, not to me.\""
show sam eyes talking with dis
m "\"Not shocking.\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"Most people don’t know.\""
show sam annoyed -talking with dis1
show sam annoyed talking with dis
m "\"Can’t know.\""
show sam neutral -talking with dis
wi "\"And yet still, he flirted...\""
show sam neutral talking with dis
m "\"Who?\""
show sam neutral -talking with dis
wi "\"Big Sonoran wolf.\""
wi "\"Easy on the eyes.\""
wi "\"Ears too.\""
show sam eyes talking with dis
m "\"Kind of sounds a little like you.\""
show sam neutral -talking with dis
wi "\"Well, he certainly looks durable.\""
wi "\"I’m no good with delicate things.\""
wi "\"I don’t want to break nobody.\""
"Sam crosses his arms and leans against the rails."
show sam neutral talking with dis
m "\"Is that why you like being so rough with me?\""
show sam smile with dis
wi "\"...yeah.\""
wi "\"I know that you can take a lot.\""
show sam neutral -talking with dis
wi "\"I mean, you already have.\""
show sam annoyed -talking with dis
"He scowls a bit, then he nods."
show sam neutral talking with dis
m "\"So why not flirt back?\""
show sam eyes -talking with dis1
show sam eyes talking with dis
m "\"See where it goes?\""
show sam neutral -talking with dis
wi "\"Because I don’t get the impression he’d kneel for me.\""
show sam smile with dis
"Sam smiles."
show sam happy with dis
"Then he breaks into a chuckle."
show sam smile with dis
wi "\"...What?\""
show sam neutral talking with dis
m "\"So kneel for him.\""


if SW_Points>=2:
    show sam surprised -talking with dis
    wi "\"The last time I did that my dad caught me.\""
    show sam surprised talking with dis
    m "\"And you’re still alive?\""
    show sam neutral -talking with dis
    wi "\"Most of my twenties felt more like walking through a haze than living, but I feel plenty alive these days.\""
    show sam surprised -talking with dis
    wi "\"He arranged the marriage between me and my ex-wife within a week.\""
    show sam surprised talking with dis
    m "\"Married in just a week’s notice?\""
    show sam surprised -talking with dis
    wi "\"...yeah.\""
    show sam eyes talking with dis
    m "\"I’d hate to see the bill on that kind of quick arrangement.\""
    show sam neutral -talking with dis
    wi "\"Mostly it was more of a courtroom proceeding than a ceremony.\""
    wi "\"Then I was out of my childhood bedroom and living in the house my father bought for a while.\""
    "I take another puff of that cigarette."
    "Then I blow."
    "The smoke looks ghostly."
    show sam surprised with dis
    wi "\"He wanted a child before the year was up or he’d sent me to the sanitarium.\""
    "Sam cringes, but nods."
    show sam neutral with dis
    wi "\"So I gave him a child.\""
    wi "\"And I gave her a child.\""
    wi "\"And he has a name, and it’s Andy.\""
    wi "\"I figured somebody getting to be born was better than catching genital diseases in an institution bathroom or having strangers take pieces of my brain away.\""
    show sam annoyed -talking with dis
    "Sam crosses his arms."
    show sam annoyed talking with dis
    m "\"Well, after hearing you went through all that, I think swallowing sounds a whole lot more fun than having a kid.\""
    show sam annoyed -talking with dis
    wi "\"I don’t hate it.\""
    "In fact, you love it."
    show sam neutral -talking with dis
    wi "\"It just reminds me of that impossible choice.\""
    wi "\"The life I could have had if I ran away.\""
    wi "\"Or the life I could have had if they caught me and locked me up with all the people who have brain damage.\""
    wi "\"...some men just aren’t going to kneel.\""
    wi "\"It doesn’t need to be explained or defended.\""
    wi "\"It’s just the truth.\""
    show sam eyes with dis
    "He leans in closer."
    show sam eyes talking with dis
    m "\"I just wouldn’t want you to miss out on something I think you’d enjoy.\""
    show sam neutral -talking with dis
    wi "\"What makes you think I’d enjoy it?\""
    show sam neutral talking with dis
    m "\"Because it’s dirty.\""
    show sam neutral -talking with dis1
    show sam neutral talking with dis
    m "\"You like dirty.\""
    show sam neutral -talking with dis
    wi "\"Well...\""
    wi "\"I like dignity too.\""
    show sam neutral talking with dis
    m "\"Just try it, just once with me.\""
    show sam neutral -talking with dis
    wi "\"...maybe next time, then.\""
    show sam smile with dis
    "He smiles."
    show sam neutral talking with dis
    m "\"You sure?\""
    show sam smile with dis
    wi "\"You know I don’t like repeating myself.\""
else:
    show sam neutral -talking with dis
    wi "\"...some men just aren’t going to kneel.\""
    wi "\"It doesn’t need to be explained or defended.\""
    wi "\"It just the truth.\""
    show sam eyes talking with dis
    m "\"I just wouldn’t want you to miss out on something I think you’d enjoy.\""
    show sam neutral -talking with dis
    wi "\"What makes you think I’d enjoy it?\""
    show sam smile with dis
    "Sam smiles."
    show sam neutral talking with dis
    m "\"Because it’s dirty.\""
    show sam neutral -talking with dis1
    show sam neutral talking with dis
    m "\"You like dirty.\""
    show sam neutral -talking with dis
    wi "\"Well...\""
    wi "\"I like dignity too.\""
    show sam neutral talking with dis
    m "\"Try it just once with me.\""
    show sam neutral -talking with dis
    wi "\"...let’s play it by ear next time.\""


stop music fadeout 3.0
play background ("sfx/crickets.ogg") fadein 3.0
scene saloonoutsidedusk
with slow_dissolve
"The sun is getting even lower in the sky."
show sam eyes -talking at center,dusk with dis3
"Sam and I stopped talking a while ago."
"But it’s a cozy kind of quiet considering all of the noise still coming from the inside of the bar."

"It’s seven seventeen here, which means it’s nine seventeen there."
show sam eyes talking with dis
m "\"What are you thinkin’ about?\""
show sam eyes -talking with dis
wi "\"Names. Traces. Motives. Intersecting interests.\""
"I think about lighting another smoke, then I put it back in my pocket."
show sam neutral -talking with dis
wi "\"At least... that’s what I want to say.\""
wi "\"If I don’t put it all down on paper in my office it’s hard to keep track.\""
show sam neutral talking with dis
m "\"So if you’re gonna waste time then why don’t we do it somewhere more lively.\""
show sam smile with dis
wi "\"You mean the Stag?\""
show sam neutral talking with dis
m "\"Might do.\""
show sam smile with dis
wi "\"Look at you becoming the social butterfly.\""
wi "\"Why do you really want to go?\""
"He crosses his arms."
show sam neutral talking with dis
m "\"I’ve never scoped it out for clients.\""
show sam eyes -talking with dis1
show sam eyes talking with dis
m "\"Might be good for business.\""
show sam annoyed -talking with dis
wi "\"Didn't you already do plenty of scoping today with my deputy?\""

"Sam bites his lip."
show sam annoyed talking with dis
m "\"I wish you hadn't made such a fuss about that.\""
show sam annoyed -talking with dis
wi "\"And I wish you took my job more seriously.\""
show sam annoyed talking with dis
m "\"I could say the same, you know.\""
show sam eyes -talking with dis1
show sam eyes talking with dis
m "\"That one's so pent up that anybody could have made a move.\""
show sam neutral -talking with dis
wi "\"So why'd it have to be you?\""
show sam neutral talking with dis
m "\"'Cause early bird gets the worm.\""
show sam smile -talking with dis
wi "\"Fuck's sake.\""
wi "\"Don't say worm.\""
show sam eyessmile with dis
m "\"Is pecker preferable?\""
show sam smile with dis
wi "\"Fuck off, Sam.\""
"He smirks."
show sam neutral talking with dis
m "\"Ain't it a good thing he's like us, Will?\""
show sam neutral -talking with dis
wi "\"Anybody's like us when they don't have the opportunity to get familiar with women out here in the stinkin' desert, Sam.\""
wi "\"You should know that better than anybody.\""
show sam eyes talking with dis
m "\"He knew about us, Will.\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"Now he's way less likely to squeal about it to anybody else.\""
show sam annoyed -talking with dis
wi "\"All otters do is squeal.\""
show sam annoyed talking with dis
m "\"You know what I mean.\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"Plus, he feels a lot different when he's confident.\""
show sam neutral -talking with dis
wi "\"You don't say...\""
show sam eyes talking with dis
m "\"Let's just say he didn't need much help to start taking control.\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"I'd feel weirder about it, if it weren't such an improvement.\""
show sam smile with dis
m "\"Maybe you ought to see what that's like for yourself.\""
show sam neutral -talking with dis
wi "\"You tellin’ me you never sniffed out the place despite all the years you’ve been here?\""
wi "\"Sounds fishy to me.\""
show sam neutral talking with dis
m "\"Well, maybe it’s nice to see you out of your element for a change.\""
show sam neutral -talking with dis
wi "\"What do you think my element is exactly?\""
show sam neutral talking with dis
m "\"Just think it’s funny that you can be shot at, or be up to your arms in blood, but you don’t wrinkle your nose until you have to make a social obligation.\""
show sam neutral -talking with dis
wi "\"A crowded bar with a bunch of pent up drunks ain’t exactly a tea party, Samuel.\""
show sam eyes talking with dis
m "\"I’m sure we can arrange one of those with Mr. Tibbits instead.\""
show sam smile with dis
"I pinch my snout again."
wi "\"Stop.\""
show sam neutral talking with dis
m "\"If we take turns bending him over the table he’ll probably pop faster than the kettle lid.\""
show sam smile with dis
"I feel nothing in my body now but pain."
wi "\"Just shut the hell up?\""
wi "\"Let’s get everybody together if we’re going.\""
hide sam with dis3
"Sam and I stretch before going back inside to corral everybody."
scene saloon2
stop background fadeout 2.0
play music ("music/saloonpiano.ogg") fadein 3.0
show sam neutral at saloon:
    xzoom-1
    xpos -0.12
    yalign 1.0
with dissolve
show nik neutral flaccid hoff at centerright,saloon
show tod at right,saloon
with dis3
"Nik and Todd are where we left them."

show tod surprised with dis
wi "\"If we're headin' out, then let's head out already.\""
show nik talking with dis
ni "\"So you are deciding to go?\""
show nik -talking with dis
wi "\"I am deciding to go.\""
show nik smile with dis
#adjust
play sound ("sfx/thud5.ogg")
"Nik smiles and steps forward, clapping me on the back with his big arms."
stop sound
show nik happy with dis3
ni "\"I thought you might come around!\""
show nik smile with dis3
play sound ("sfx/creak2.ogg")
"Todd stands up stiffly, making his chair wobble."
stop sound
show nik -smile with dis
to "\"Are y'all going now?!\""
wi "\"I don't want to have to say it again.\""
to "\"So where am I supposed to go?\""
wi "\"Wherever you want.\""
wi "\"I already called it a day for you.\""
show nik talking with dis
ni "\"Maybe he would like to come?\""
show nik -talking with dis
show sam eyes with dis
"Sam shakes his head."
show sam annoyed talking with dis
m "\"That might not be such a good idea.\""
show sam -talking with dis
show tod annoyed with dis
"Todd emphatically frowns."
to "\"Now why wouldn't it be?\""
show nik sidelook with dis3
show sam neutral with dis3
"Nik gives Sam a sideways glance."

ni "\"I don't know.\""
show nik eyestalking with dis3
ni "\"Strength in numbers, I say.\""
show nik -eyestalking with dis3
show tod surprised with dis
show sam eyes talking with dis
m "\"It's a very physical place, Mr. Bronson.\""
show sam -eyes -talking with dis
to "\"...Oh.\""
"He blushes a bit."
to "\"Well if that's the case...\""
show tod sigh with dis3
to "\"I don't think I'd mind?\""
show tod surprised with dis3
to "\"Unless William does, of course.\""
show tod with dis
wi "\"Frankly I'd rather you got it out of your system at a place like that, than acting out in places you shouldn't.\""
show tod sigh with dis3
to "\"Well, ah.\""
show nik smile with dis
show tod talking with dis3
to "\"Alrighty.\""


show tod arms happy with dis3
"Todd takes this as an invitation to go, too."
"The damn Stag really doesn’t seem like his kind of place, but it’s too awkward to tell him no, now."


if ETHINT_Points == 1:
    scene bg saloon2 with dissolve


    "We can’t find Cliff or Murdoch much of anywhere, but I remember that the stoat said he’d pay Ethel a visit."
    show sam neutral -talking at center,saloon with dis3
    wi "\"Hey Sam?\""
    show sam neutral talking with dis
    m  "\"What?\""
    show sam surprised -talking with dis
    wi "\"Do you know where Ethel’s bedroom is?\""
    show sam surprised talking with dis
    m "\"Now that’s the last thing I thought you’d ask me.\""
    show sam surprised -talking with dis
    wi "\"I think that’s where our Batavian friend might be.\""
    show sam annoyed talking with dis
    m "\"Wouldn’t be my first, second, or third pick, but then again, I’m just a cocksucker.\""
    show sam annoyed -talking with dis1
    show sam annoyed talking with dis
    m "\"Uh, follow me up the stairs.\""
    show sam annoyed -talking with dis1
    stop music fadeout 5.5
    scene bg saloonhallway with dissolve
    show sam neutral -talking at center,saloon with dis3
    "We follow the stairs up to the mezzanine, past a path near another set of stairs, and in front of a few doors and what looks like a small lobby with cozy chairs."
    show mur sideeye at right,saloon with dis3
    "Murdoch looks very, very bored, flipping through a fashion catalogue."
    "From behind the door we hear yelling."
    wi "\"What the hell was--\""
    show sam annoyed -talking with dis3
    show mur angry with dis3
    "Sam puts his finger to my lips to shut me up while Murdoch does a similar gesture."
    show mur sideeye with dis3
    cl "\"Hyah!\""
    et "\"Ohhh.\""
    et "\"You’re as hot blooded as any yank, Mr. Tibbits!\""
    cl "\"A little ways more!\""
    cl "\"A LITTLE ways more!\""
    et "\"Ohhh I wouldn’t say little!\""
    et "\"I’d say juuuuust right!\""
    et "\"Ohhhh.\""
    cl "\"Hyah!\""
    et "\"Ohhhhhh.\""
    "This is a hell."
    et "\"...wait, you’re done?\""
    cl "\"Afraid so.\""
    cl "\"Are you?\""
    et "\"...yeah, we’re done.\""
    play sound ("sfx/dooropen.ogg")
    hide sam
    hide mur
    with dissolve
    "As the door starts to open Sam and I split to the opposite sides of with our backs against the wall."
    stop sound
    show cli pants blush eyes closed at center,saloon with dis3
    "I only see the salamander's hand as she pushes a very glossy Mr. Tibbits out of the room and closes the door."
    show cli pants blush eyes talking with dis
    play music ("music/quiet.ogg") fadein 3.0
    "He stretches and starts a merry little whistle with a bounce in his step."
    show cli pants doubt with dis3
    show mur sideeye at saloon with dis3:
        xpos 0.55
    show sam neutral -talking at saloon with dis3:
        xpos -0.1
        xzoom-1
    "Until he sees all of us and stops."
    cl "\"Mr. Byrnes I thought--\""
    show sam annoyed -talking with dis3
    show mur angry with dis3
    show cli pants shocked with dis3
    "We all make a shushing gesture."
    show sam neutral -talking with dis3
    show cli down pants with dis3
    show mur sideeye with dis3
    "He lowers his voice."
    cl "\"I thought I told you to redirect anybody down the stairs.\""
    cl "\"I said that it would be quick.\""
    show mur eyes talking with dis
    mu "\"They just got here. I didn’t have time to.\""
    show mur sideeye with dis
    "He wipes his brow and flicks a bit of his sweat to the floor."
    show cli serious pants with dis3
    cl "\"I’ll need a moment in the bathroom to freshen up.\""
    mu "\"Cliff, you really don’t have to worry too much about that for where we’re going.\""
    show cli down pants with dis3
    cl "\"I don’t need to be fresh for others.\""
    cl "\"I need to be fresh for myself.\""
    show cli serious pants with dis3
    wi "\"Just one thing before you go Mr. Tibbits.\""
    show cli doubt pants with dis
    "His tone is snappy."
    cl "\"What?\""
    wi "\"The wine.\""
    wi "\"Did you find out who ordered Ethel to fetch it?\""
    show cli serious pants with dis
    cl "\"Oh that?\""
    show cli talking pants with dis
    cl "\"Well, that was nothing.\""
    show cli eyes pants with dis1
    show cli eyes talking pants with dis
    cl "\"It was exactly who you’d expect to order the wine.\""
    show cli pants with dis1
    show cli talking pants with dis
    cl "\"Harlan. The barkeep.\""
    show cli pants with dis
    $ ethelclifftext = "We could hear him down the hallway. But at least I know now that Harlan asked for the wine delivery."
    $ update_unlocked_pages(1, 29)
    $ renpy.notify("Notebook updated.")
    wi "\"...right.\""
    "I thought as much, but I needed to confirm it."
    show cli happy pants with dis3
    cl "\"Well then!\""
    cl "\"How about you all scoot along and I’ll join you outside downstairs in less than ten minutes.\""
    show mur talking with dis3
    mu "\"Sounds good to me, unless the sheriff needs something else?\""
    show mur smile with dis
    wi "\"No, that’s all I needed.\""
    wi "\"Let’s go meet up with Todd and Nik.\""
    stop music fadeout 3.0




else:
    stop music fadeout 5.0
    scene bg black with dissolve
    "Finding Murdoch and Mr. Tibbits is a bit more of a struggle."
    scene bg saloonstageviewnight with dissolve
    "We check the bar and the stage."
    scene powderroom with dis3
    "Then the powder room."
    scene bg black with dissolve
    scene powderroom with dissolve
    "After circling the whole Hip two or three more times, Sam finds them in the powder room, which confuses us all because we think we checked there."
    show mur sideeye at right
    show cli eyes at center
    with dis3
    "Murdoch looks annoyed."
    "Mr. Tibbits looks incredibly relaxed."
    "Though I can’t help but notice he’s walking a bit oddly."
    scene bg black with dissolve

play background ("sfx/crickets.ogg") fadein 3.5
scene bg echoroadnight
show nik neutral flaccid hoff at right,nightbrown
with dissolve
"Once everybody is together outside, Nik waits for us a little further down the dirt road."
show nik eyes with dis
"When we catch up to him, he clears his throat."
show nik disappointed with dis3
"He puts his hands on his hips and nods solemnly, as if he’s going to make a speech."
#play music ("music/long-nights.ogg") fadein 3.0
ni "\"Good evening gentlemen.\""
"And boy is he startin’ one."
show nik talking with dis3
ni "\"The first thing I want to express is my gratitude to each one of you for making this evening possible.\""
show nik neutral flaccid hoff with dis1
show nik talking with dis
ni "\"This is a historic occasion for myself and Sam.\""
show nik eyes with dis1
show nik eyestalking with dis
ni "\"We have never been able to get William to come and drink with us at the Stag.\""
show nik neutral flaccid hoff with dis
wi "\"It’s not a big deal, Nik.\""
show nik sidelook with dis3
ni "\"Oh, moon.\""
ni "\"Oh, stars.\""
show nik eyestalking with dis3
ni "\"What wheels do you turn to make our Sheriff Adler attend this dance?\""
show nik smile with dis3
"I roll my eyes."
wi "\"If you keep this up I’m just going back home.\""
wi "\"My office is right there you know.\""
"I point at the building as we pass it."
show cli at centerright,nightbrown with dissolve
show cli talking with dis
cl "\"Pardon me.\""
show cli doubt with dis
cl "\"I don’t mean to interrupt anything scripted, but what’s the purpose of going from one dance hall to another?\""
show cli serious with dis3
show mur talking at nightbrown with dis3:
    xzoom-1
    xpos -0.1
mu "\"The Hip is still a brothel, Mr. Tibbits, but it’s world famous for its entertainment and its organizational policies.\""
show mur mischief with dis
mu "\"Where we’re going is more of a free-for-all.\""
show mur smile with dis
show nik talking with dis
ni "\"And it is a gentleman’s club.\""
show nik eyes with dis1
show nik eyestalking with dis
ni "\"So there will be no women.\""
show nik neutral flaccid hoff with dis
show mur talking with dis
mu "\"Aside from the scant drag king or two who sneak in on occasion.\""
show mur smile with dis1
show mur talking with dis
mu "\"But they’re not exactly turned away.\""
show mur sideeye d with dis
mu "\"Can’t say the same for the Mr. and Mrs. couples.\""
show nik eyestalking with dis
ni "\"Oh absolutely not.\""
show nik neutral flaccid hoff with dis
show cli doubt with dis
cl "\"Why might that be so bad?\""
show cli serious with dis3
show mur sideeye with dis3
mu "\"Because then it would just become the Hip but without the class.\""
show nik disappointed with dis3
ni "\"Mr. Byrnes...\""
ni "\"I’m hurt that you would say such a thing.\""
show nik talking with dis3
ni "\"There is plenty of ‘class’ at the Stag.\""
show nik eyes with dis1
show nik eyestalking with dis
ni "\"It is called the proletarian class.\""
show nik smile with dis3
"He smiles slowly."
show mur concerned d with dis3
"Murdoch cringes."
mu "\"Good one, Mr. Krol...\""
show nik eyestalking with dis
show cli with dis
ni "\"Either way, it is cozy and that is what matters most.\""
show nik neutral flaccid hoff with dis
wi "\"Last time I checked it was just a barn.\""
show nik disappointed with dis3
"He holds his paws on his hips and shakes his head."
ni "\"On off hours.\""
show nik talking with dis3
ni "\"At the right time on the right day, it is not just a barn.\""
show nik eyes with dis1
show nik eyestalking with dis
ni "\"It comes to life.\""
show nik neutral flaccid hoff with dis
"I nod to him."
wi "\"So a crowded barn.\""
show tod eyes happy at halfleft,nightbrown behind cli with dis3:
    xzoom-1
to "\"Well I know my way around a barn.\""
to "\"Pa’s been herding cattle since before I was born, and I help him and my brothers out when I’m not at the station or patrolling.\""
show tod surprised with dis
wi "\"It ain’t that kind of barn, Todd.\""
show tod talking with dis
to "\"Well what’s the difference?\""
show tod annoyed with dis
wi "\"The animals filling up this one is people.\""
show tod surprised with dis
show mur eyes with dis
mu "\"And they’ll give you mean looks if you don’t know how to dance.\""
show mur with dis
to "\"We have to dance?\""
show nik eyestalking with dis
ni "\"Yes.\""
show nik neutral flaccid hoff with dis
show mur sideeye with dis
mu "\"Of course, it’s not a rule that you have to dance.\""
show nik talking with dis
ni "\"No.\""
show nik -talking with dis1
show nik talking with dis
ni "\"Tonight it is a rule.\""
show nik eyes with dis1
show nik eyestalking with dis
show tod annoyed with dis
ni "\"One dance at least.\""
show nik neutral flaccid hoff with dis
show tod talking with dis
to "\"Well one dance shouldn’t be so bad.\""
show tod with dis
show cli talking with dis
cl "\"What kind of dances do you know, Mr. Bronson?\""
show tod eyes happy with dis
show cli doubt with dis
to "\"Square.\""
show tod with dis
cl "\"Pardon?\""
to "\"Oh, you know.\""
show tod eyes happy with dis
"He holds his arm out to the weasel as if to hook it."
show cli shocked with dis3
"The weasel looks at it like somebody’s waving a dinner fork in his face."
show cli serious with dis3
show mur eyes with dis3
"The fox butts in to take it and twirls with him."
show mur with dis
mu "\"It’s like this, Cliff.\""
show tod with dis
cl "\"Oh.\""
show cli talking with dis
cl "\"He meant a quadrille.\""
show cli doubt with dis
cl "\"Albeit a very Columbianized one.\""
show cli with dis3
show mur talking with dis3
mu "\"That’s the style most people will use.\""
show mur smile with dis1
show mur talking with dis
mu "\"At the Hip you’ll see more ragtime steps like the grizzly bear and the bunny hop.\""
show mur smile with dis1
show mur talking with dis
mu "\"I thought it fitting that I learn the foxtrot.\""
show mur mischief with dis
show cli doubt with dis
show tod annoyed with dis
show nik eyes with dis
"He grins and a small groan hovers about the crowd."
show nik neutral flaccid hoff with dis3
show mur eyes with dis3
hide tod
show sam annoyed -talking at halfleft,nightbrown
with dis3
m "\"Boo.\""
show sam surprised -talking with dis3
show mur smile with dis3
"Instead of skulking away in shame, he wraps his hand around Sam and leads him backwards."
"The cat keeps stumbling backward until Mr. Byrnes grasps his hand and twirls him before letting go."
show cli blush eyes right with dis
"Cliff’s jaw opens a little and Todd lets out a wolf whistle."
"Nik is glaring."
show cli with dis
show sam neutral -talking with dis
show mur talking with dis
mu "\"What’s fun about it is that it’s a persistent advance...\""
show mur eyes with dis3
mu "\"Fits me well I should say, sappy pun aside.\""
show mur with dis
cl "\"So how exactly do you know which dances they’ll be using in the barn club?\""
show nik sidelook with dis3
ni "\"He performs there.\""
show nik talking with dis3
ni "\"Though he performs better when he is not trying so hard to show off.\""
show nik neutral flaccid hoff with dis3
show mur mischief with dis3
mu "\"Well I have to show off when somebody boos me.\""
mu "\"It’s at least twice as insulting as the initial boo.\""
show mur sideeye d with dis
show nik talking with dis
ni "\"Perhaps you can impress with your hands on an instrument rather than Sam’s waist.\""
show nik neutral flaccid hoff with dis
show mur smile with dis
show sam eyes talking with dis
m "\"You can both touch my waist if you like.\""
show sam neutral -talking with dis
show nik sidelook with dis3
"Murdoch gives him a thumbs up."
"Nik looks slightly embarrassed and pushes ahead of us to keep walking."
ni "\"We should be there in less than five minutes if we pick up the pace...\""
scene bg black with dissolve
scene stagtrailnight with dissolve
show sam neutral -talking at left,night with dis:
    xzoom-1
"Sam slows his pace as he walks, coming close to me."
show sam sad talking with dis
m "\"He’s still upset with me, isn’t he?\""
show sam sad -talking with dis
"I grunt."
wi "\"Now what gave you that idea?\""
show sam eyes talking with dis
m "\"Nevermind.\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"We don’t need to talk about this right now.\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"Tonight’s supposed to be fun.\""
show sam neutral -talking with dis
wi "\"Fun for those three maybe.\""
"Murdoch is practicing more dances with Todd until Cliff cuts in."
"It’s a bit too complex for Todd, but he’s tryin’."
show sam neutral talking with dis
m "\"I’m not that much of a dancer.\""
show sam neutral -talking with dis
wi "\"That’s too bad.\""
show sam annoyed -talking with dis
wi "\"Because I’m a phenomenal dancer.\""
show sam annoyed talking with dis
m "\"You don’t dance, Will.\""
show sam neutral -talking with dis
"His tone is doubtful."
wi "\"You didn’t know me four years ago, Sam.\""
show sam smile with dis
"He smirks."
show sam neutral talking with dis
m "\"And you don’t think you might be a bit rusty?\""
show sam smile with dis
wi "\"Nope.\""
wi "\"Hard to forget once you learn.\""
show sam eyes talking with dis
m "\"I don’t know.\""
show sam eyes -talking with dis1
show sam eyes talking with dis
m "\"You look a little past your prime to me.\""
show sam smile with dis
wi "\"Seems to me like I moved just fine the other night.\""
show sam neutral talking with dis
m "\"But you think you’ll be able to keep up with that wolf you told me about if you see ‘em?\""
show sam smile with dis
wi "\"There ain’t gonna be no wolf.\""
show sam eyes talking with dis
m "\"You’re dodgin’ the question.\""
show sam smile with dis
wi "\"Just because I can dance doesn’t mean I’m going to.\""
"He nods smugly."
show sam neutral talking with dis
m "\"Nik won’t allow that.\""
show sam smile with dis
"I feel my scowl getting a little bit longer."
wi "\"If I dance with anybody then it’s gonna be you.\""
show sam neutral talking with dis
m "\"You think that’ll work?\""
show sam neutral -talking with dis
wi "\"Why wouldn’t it?\""
show sam neutral talking with dis
m "\"All eyes are gonna be on you tonight.\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"Which means less eyes on me.\""
show sam annoyed -talking with dis
"He grabs my arm and his tone goes stern."
show sam annoyed talking with dis
m "\"And I will do everything in my power to preserve this natural order.\""
show sam surprised -talking with dis
"I shrug him off and he stumbles."
show sam -surprised
show cli at center,night
with dissolve
show cli talking with dis
cl "\"I couldn’t help but overhear your dancing claims Mr. Adler.\""
show cli eyes with dis1
show cli eyes talking with dis
cl "\"I would very much like to see your skills, if you’ll allow it.\""
show cli with dis1
show cli talking with dis
cl "\"Perhaps as a gesture that we don’t need to be at one another’s throats for the duration of my stay.\""
show cli doubt with dis
wi "\"I don’t need any gestures Mr. Tibbits.\""
wi "\"Just your cooperation.\""
"He rolls up his sleeves and stands in front of me, chest puffed up against mine and blue eyes looking up at me."
cl "\"Oh, what’s the matter?\""
show cli eyes talking with dis
cl "\"Afraid you can’t keep up, Mr. Adler?\""
show cli with dis
wi "\"I’m more afraid I can’t keep up with him.\""
"I point to the fox who only smiles back at me."
show cli eyes talking with dis
cl "\"I just want to show Columbians a new thing or two about dancing.\""
show cli happy with dis3
cl "\"I promise it’ll be worth it.\""
show cli with dis3
show nik sidelook at right,night behind cli with dis3
ni "\"If there’s anybody showing the Columbians how to dance, it will be me.\""
show nik neutral flaccid hoff with dis3
wi "\"Ain’t the two of us a bit too big together on the dance floor Nik?\""
show nik eyestalking with dis
ni "\"It is a big enough barn.\""
show nik neutral flaccid hoff with dis3
wi "\"Look, I’m not promising to dance with all of you.\""
wi "\"Let’s just say that whatever happens, happens.\""
show nik disappointed with dis3
"Nik nods solemnly."
ni "\"I accept your terms.\""
show nik smile with dis3
"I feel my frown getting tighter."
scene bg stagexteriornight with dissolve
"After walking past a few more walks and tumbleweeds, I can see the barn in the distance."
"In all honesty, there was some truth to what Nik was saying."
"The barn has a bit of a glimmer to it when there are more lanterns and candles lit."
"But what I didn’t notice before was what was behind the barn."
"There are a lot more barns behind it that I hadn’t noticed before."
"Their shadows are silhouetted against the moon, and the longer shadows of the pale figures disappearing into them blur into the obscurity of the greater shade."
show nik neutral flaccid hoff at night with dis3:
    xpos 0.55
wi "\"What are all those other barns back there?\""
show nik talking with dis
ni "\"Those are shared spaces, owned by the property handlers.\""
show nik neutral flaccid hoff with dis
wi "\"For what purposes?\""
show nik sidelook with dis3
ni "\"Recreation...\""
"I think I get the gist of what he’s implying, but I don’t like being left to make my own assumptions because of a vague answer."
show sam neutral -talking at center,night with dis3
"Sam teases me with a lilting tone."
show sam neutral talking with dis
m "\"Fingers crossed you find him when we go inside.\""

if ETHINT_Points == 1 or HARINT_Points == 1:
    show sam neutral -talking with dis3
    show nik talking with dis3
    ni "\"If Chang is in the building we’ll know.\""
    show nik eyes with dis1
    show nik eyestalking with dis
    ni "\"He’s always in the same place.\""
    show sam smile with dis
else:
    show sam smile with dis3
    show nik talking with dis3
    ni "\"{i}’Him?’{/i}\""

show nik neutral flaccid hoff with dis
wi "\"Actually, there’s a man I keep runnin’ into.\""
wi "\"And, well...\""
wi "\"He’s a bit forward.\""
show sam neutral talking with dis
m "\"He wants to sleep with him.\""
show sam smile with dis
show nik surprised with dis
ni "\"William!\""
show nik talking with dis
ni "\"...Are you?\""
show sam surprised -talking with dis3
show nik sidelook with dis3
wi "\"Nobody said nothin’ about no fornication, alright?\""
wi "\"All y’all better get off my back.\""
"I can hear Todd's voice a good deal away."
to "\"Do you hear what he said?\""
to "\"Why’s he yellin’ about fornication?\""
"The other two are lagging behind even further."
show sam surprised talking with dis
m "\"Jesus, William, I was just joking.\""
show sam surprised -talking with dis
wi "\"I’d just like if I could tell you one personal thing without makin’ it everybody else’s business.\""
ni "\"Oh...\""
show nik talking with dis3
show sam neutral -talking with dis3
ni "\"So it’s true?\""
show nik neutral flaccid hoff with dis
wi "\"All I did was think about it, okay?\""
"I feel my heart beating faster and I lower my voice."
wi "\"But Jesus Christ, y’all, we’re still in public.\""
show sam neutral talking with dis
m "\"Nobody heard us, Will.\""
show sam neutral -talking with dis
show nik talking with dis
ni "\"You are still too used to the city, Will.\""
show nik neutral flaccid hoff with dis1
show nik talking with dis
ni "\"Things can happen here.\""
show nik eyes with dis1
show nik eyestalking with dis
ni "\"Nobody cares.\""
show nik neutral flaccid hoff with dis
"The frustration is rising in me again."
wi "\"You’d be surprised when you’re a public official.\""
show nik sidelook with dis3
ni "\"You above anybody here has an alibi.\""
ni "\"You are still on the job.\""
show nik neutral flaccid hoff with dis3
wi "\"Even still...\""
show nik talking with dis
ni "\"What?\""
show nik neutral flaccid hoff with dis
wi "\"I don’t want to lose control of myself so easily.\""
wi "\"People are counting on me.\""

if SW_Points>=2:
    show sam eyes talking with dis
    m "\"So are we, Will.\""
    show sam neutral -talking with dis
    wi "\"What are you talking about?\""
    show sam neutral talking with dis
    m "\"Remember what happened back at the mines in the tunnel?\""
    show sam neutral -talking with dis1
    show sam neutral talking with dis
    m "\"That just wasn’t normal.\""
    show sam neutral -talking with dis
    wi "\"I know it wasn’t normal, y’all, but nothing’s happened to me since.\""
    show nik talking with dis
    ni "\"You have to take care of yourself before you can take care of anybody else.\""
    show nik neutral flaccid hoff with dis
    show sam eyes talking with dis
    m "\"Listen to Nik.\""
    show sam neutral -talking with dis1
    show sam neutral talking with dis
    m "\"And if you aren’t goin’ to listen to him, then please just listen to me.\""
    show sam neutral -talking with dis1
    show sam neutral talking with dis
    m "\"Pull the stick out of your ass and enjoy yourself.\""
    show sam neutral -talking with dis1
    show sam neutral talking with dis
    m "\"For your own sake.\""
else:
    show sam neutral talking with dis
    m "\"We aren’t babies Will.\""
    show sam neutral -talking with dis1
    show sam neutral talking with dis
    m "\"If you worked 24/7 and never slept, driving yourself crazy, there’d still be assholes out and about ruining other people’s lives.\""
    show sam neutral -talking with dis1
    show sam neutral talking with dis
    m "\"The world ain’t in need of some good old fashioned justice right now...\""
    show sam eyes -talking with dis1
    show sam eyes talking with dis
    m "\"It needs some joy.\""

show sam neutral -talking with dis
"Where the hell do these two get off on lecturing me?"
show mur at left,night with dis:
    xzoom-1
mu "\"So.\""
"All three of us turn to Murdoch, Cliff and Todd, finally catching up to us."
show mur mischief with dis
mu "\"Y’all ready to go inside or what?\""
mu "\"Will?\""
show mur smile with dis
wi "\"Yeah I’m ready.\""
stop background fadeout 2.0
scene bg black with dissolve

play music ("music/stag1.ogg") fadein 4.0
scene stagnight with dissolve
"Oddly enough, the smell inside is better than it was the last time I was here."
"They’ve completely opened the doors to the outside, and they’re burning oils and and candles that smell like pine tree sap."


if ETHINT_Points == 1 or HARINT_Points == 1:
    show nik sidelook at right,light1 with dis3
    ni "\"Oh.\""
    wi "\"What?\""
    show nik talking with dis3
    ni "\"Chang is definitely here.\""
    show nik neutral flaccid hoff with dis
    wi "\"Do you see him?\""
    show nik talking with dis
    ni "\"No, but I see my friend Yao up on the loft.\""
    show nik neutral flaccid hoff with dis
    wi "\"He’s that Huaxian tiger you’ve told me about before, right?\""
    show nik eyestalking with dis
    ni "\"Aye.\""
    show nik neutral flaccid hoff with dis1
    show nik talking with dis
    ni "\"If he is here, that means Chang will be here too.\""
    show nik neutral flaccid hoff with dis1
    show nik talking with dis
    ni "\"Come with me.\""
    show nik neutral flaccid hoff with dis1
    scene stagloftnight with dis3
    "He guides me to the ladder that leads into the loft."
    "I’ve been here before recently."
    $ renpy.music.set_volume(0.5, delay=4.0, channel='music')
    scene stagloftbacknight
    show yao casual crossed at center,stagback
    show cha eyes at left,stagback
    with dis3
    "We walk on over to the edge of the loft to the table where the tiger is seated."
    show nik neutral flaccid hoff at stagback behind yao with dis3:
        xpos 0.55
    show cha with dis3
    "Along with a sable I’ve certainly seen before."
    wi "\"Ji Ba?\""
    show yao casual angry
    show cha surprised
    show nik surprised
    with vpunch
    "The tiger stands abruptly, nearly knocking his chair over."
    show cha with dis
    show yao casual teeth with dis
    ya "\"What did you call him?!\""
    show yao casual angry with dis
    wi "\"Whoa now!\""
    #sfx
    play sound ("sfx/thud6.ogg")
    show nik shocked
    show yao casual teeth
    with hpunch


    "He takes a swipe at me but I side-step it."
    stop sound
    show cha smile with dis

    "Nikolai is shouting for him to stop, and the marten is laughing."
    show nik surprised with dis3
    wi "\"Next time warn me when your friends are gonna try to maul me, Nik!\""
    show yao casual surprised with dis
    "The tiger blinks when he sees and hears Nik yelling."
    show yao casual angry crossed with dis
    "Then he sees the sable laughing."
    "He speaks rapidly in a Huaxian language,{nw}"
    play sound ("sfx/tablepunch.ogg")
    show yao casual angry with dis
    show cha eyes with dis
    extend " then slaps his fists on the table as the sable sits up, folding his hands apologetically."
    stop sound
    show cha smile with dis3
    show yao casual sidelook crossed with dis3
    show nik sidelook with dis3
    "The tiger turns back to us and quickly takes a short bow."
    ya "\"My sincerest apologies.\""
    ya "\"Just now, I have acted using my emotions rather than my rationality.\""
    show yao casual angry crossed with dis3
    show cha eyes with dis3
    show nik neutral flaccid hoff with dis3
    ya "\"My associate at the other side of the table has acted with neither.\""
    show cha eyes talking with dis
    unkch "\"As if you haven’t made your bosses look foolish before.\""
    show yao casual crossed with dis
    show cha with dis
    wi "\"I take it your real name is Chang Fulin, then?\""
    "The sable looks at me and holds up his hands, turning his paws skyward."
    show cha talking with dis
    ch "\"So it is.\""
    show cha with dis1
    show cha talking with dis
    ch "\"What are you looking for, Sheriff Adler?\""
    show cha with dis
    "I take out my note book and flip to the right page with the symbol of the black hand."
    wi "\"It'll be quick.\""
    wi "\"All I want to know is: What do you make of this?\""
    "He looks at the book."
    show cha surprised with dis
    "And his eyes go wide, and he flinches."
    show yao casual surprised crossed with dis
    "He starts shaking his head, quickly."
    show cha surprised talking with dis
    ch "\"I’m sorry, but I don’t know what that is.\""
    show cha surprised with dis
    "He’s definitely lying."
    "There’s panic in his voice."
    show yao casual eyebrows crossed with dis3
    show nik sidelook with dis3
    "The tiger speaks to him in Huaxian with a curious tone, but he doesn’t respond."
    "The black hand is used as a symbol of extortion."
    "That means this man is being extorted, doing the extortion, both, or is afraid he’s been caught by me."
    "I think I know which one is most likely, considering Huaxians generally aren’t welcomed into the fold."
    wi "\"Do you know where my office is?\""
    "He nods slowly."
    wi "\"Good.\""
    wi "\"Because I just wanted to say that if you have anything you want to tell me in private, stop by tomorrow during the day.\""
    wi "\"If not, then that’s okay too.\""
    "He nods again, slowly."
    wi "\"I’m going to leave you be for tonight, alright?\""
    "He looks paralyzed."
    "But after a time, he nods."
    $ renpy.music.set_volume(1.0, delay=4.0, channel='music')
    scene stagloftnight with dis3
    "As I turn to go I hear the tiger speak urgently with the sable, his voice getting slightly louder as he refuses to respond."
    "I hear Nik’s footsteps close behind me."
    show nik disappointed at right,light1 with dis3
    ni "\"What did you just do?\""
    "I tuck my notebook back into my pocket."
    wi "\"I just showed him a drawing I found in some documents recently.\""
    wi "\"A drawing with his name next to it.\""
    show nik sidelook with dis3
    ni "\"But what does that mean?\""
    wi "\"Certainly nothing good for him.\""
    wi "\"I’m going to give him some time to think on it.\""
    ni "\"Well if he is in danger, it is good that he has Yao to protect him.\""
    ni "\"I would not want to be on Yao’s bad side.\""
    show nik neutral flaccid hoff with dis3
    wi "\"No kidding.\""
    wi "\"I was up close and personal with the size of his claws.\""
    wi "\"If I was any slower I would have lost the rest of my ear.\""
    show nik talking with dis3
    ni "\"I think it’s time we did what we came here to do.\""
    show nik eyes with dis1
    show nik eyestalking with dis3
    ni "\"No more work.\""
    show nik neutral flaccid hoff with dis
    "A sigh escapes my breath."
    wi "\"Fine.\""
    wi "\"I got what I needed.\""
    scene stagnight with dis3





"The inside is so crowded with people that we can’t even get to the center bar right now."

show tre eyes br w at center,light1 with dis3
"The barkeep looks more tired than I am."
hide tre with dis3
"No sign of the bounty hunter yet, though."
"I should be thankful he’s not here to tempt me to do anything stupid."
"But it also feels a little like I missed out on something that I’ll never take a stab at again."
"Oh well."
"So it goes."

"Sam is sitting on one of the rafters, sitting still while Todd and Mr. Tibbits chatter about what sounds like beeswax in candles, or God knows what else."
show sam neutral -talking at center,light1 with dissolve
show sam neutral talking with dis
m "\"Why do you look so disappointed?\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"We just got here.\""
show sam neutral -talking with dis
wi "\"Too much of today is on my mind.\""
wi "\"That’s all.\""
show sam annoyed -talking with dis
"He looks me over."
show sam annoyed talking with dis
m "\"Oh.\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"That man you’re looking for ain’t here, is he?\""
show sam neutral -talking with dis
wi "\"No?\""
wi "\"I don’t know.\""
wi "\"That ain’t the only thing, Sam.\""
show sam neutral talking with dis
m "\"What else then?\""
show sam neutral -talking with dis
"I look over at the crowded bar."
wi "\"I was really hoping for a strong drink when we got here.\""
show sam eyes talking with dis
m "\"Well if we bum rush the bar together, we can clear a path.\""
show sam smile with dis1
show sam neutral talking with dis
m "\"Might break some limbs, but some of the people here are so scrawny they obviously ain’t using ‘em anyway.\""
show sam smile with dis
"I snort."
wi "\"You’re atrocious, Sam.\""
show sam neutral talking with dis
m "\"So are you if it made you laugh.\""
show sam smile with dis

"Another song starts up and there’s a next round of dance partners."
"This one’s quicker, but there’s still a whole lot of touches on the waist and chests sliding against one another as they make their twirls."
play sound ("sfx/thud3.ogg")
show tod at right,light1 with dis3
"I hear a small thump as I notice Todd sitting next to us."
stop sound
show tod talking with dis
to "\"They make it look easy don’t they?\""
show tod surprised with dis
wi "\"It is easy if you do it for so long.\""
to "\"I meant all the touching.\""
show sam talking with dis
m "\"That’s even easier.\""
show sam -talking with dis3
show tod sigh with dis3
"Todd sighs."

to "\"I wouldn’t know how to keep doing it feeling guilty.\""
show tod annoyed with dis3
show sam talking with dis
m "\"Feeling guilty’s just a part of it.\""
show sam eyes -talking with dis1
show sam eyes talking with dis
m "\"Same goes for all aspects of life.\""
show sam neutral -talking with dis
wi "\"It gets a lot easier when you learn to make it feel good.\""
"They look at me with blank expressions."
wi "\"The shame I mean.\""
"Legs and groins slide past one another and my eyes are on a few fairly sizable tents."
wi "\"You shouldn’t stay here if you’re uncomfortable, Todd.\""
show tod surprised with dis
"My deputy follows the line of my gaze and gulps."
show tod sigh with dis3
"Then he puts both paws on his lap."
"Shyly."
show tod annoyed with dis3
show sam smile with dis3
to "\"No.\""
"His tongue lolls a bit as he speaks."
to "\"I think I’ll be staying.\""
"His voice is firm."
"The unmistakable scent of excitement is coming off of him."
"A one-note laugh escapes me as I nod."
hide tod
hide sam
with dis3
"Sam is right about Todd."
"Whenever he commits to something with confidence, he can feel like a very different person."
"Most people don’t get to see that person, but it’s the reason he’s survived this long in this kind of work."
"He’s someone who can stop thinking too hard, and commit."
"Learning to be less awkward about his natural urges will be good for him."
"I think that’s an unspoken understanding we’ve all come to."
"Voicing it is another matter entirely."
"I'm the worst man to offer him that kind of advice."

show sam smile at center,light1 with dis3
stop music fadeout 3.0
"The music stops."
show sam neutral -talking with dis
"We see Mr. Byrnes walk over to the fiddlers who greet him with open arms and pat him on the arms."
show sam neutral talking with dis
m "\"What’s he doing over there?\""
show sam neutral -talking with dis
wi "\"Looks like he’s grabbing a guitar.\""
show nik sidelook at light1 behind sam with dis3:
    xpos 0.55
ni "\"I told you both he performs here.\""
show nik talking with dis3
ni "\"Were either of you listening?\""
show nik neutral flaccid hoff with dis
show sam annoyed talking with dis
m "\"I don’t know if I can trust that man.\""
show sam annoyed -talking with dis1
show sam annoyed talking with dis
m "\"He knows how to do too much.\""
show sam neutral -talking with dis
wi "\"That’s often what happens when your parents make you do too much.\""
hide sam
hide nik
with dissolve
show mur smile at center,light1 with dissolve
"The fox clears his throat and addresses the crowd."
show mur talking with dis
mu "\"Well howdy folks.\""
show mur smile with dis
"The barn cheers for him just a little too loud for a building this small."
show mur talking with dis
mu "\"Y'all want to know what I think?\""
show mur smile with dis
"They respond to him with a raucous shout."
show mur talking with dis
mu "\"I think it's a beautiful night for a beautiful crowd.\""
show mur smile with dis1
show mur talking with dis
mu "\"You see, I have some associates with me tonight who must not be named.\""
show mur mischief with dis
mu "\"But they’re Stag virgins so to speak, so if you can figure out who they are, please make sure to be gentle with 'em.\""
show mur smile with dis
"Todd isn't the only person this place has an effect on."
"It startles me to see what a different person that fox is in front of a crowd as opposed to when he's in an auditorium or an office, quietly setting up a camera."
"Once again I’m flooded with thoughts about the energy in his step and the flow of his body."
"They’re the kind of thoughts that make me forget about his family as I watch his tail move, bathed in the moonlight from the rafters above."
"He puts out an odd kind of energy that’s somehow contagious."
"The energy you only tend to find in those up and coming hot spots in the big city, the ones that all the undiscovered celebrities go to."
show mur talking with dis
mu "\"Let’s set the tone for them tonight with a little song and dance.\""
show mur smile with dis1

window hide
scene black with slow_dissolve
$ renpy.movie_cutscene("movies/willanimatic.webm", delay=211, loops=0, stop_music=True)
window show
play background ("sfx/crickets.ogg") fadein 5.0
scene bg barnsnight with slow_dissolve
"There’s little campfires all around us."
"The shades of people crawl around us, grasping blindly for their own little pleasures in the dark as Sam and I cling together, his chest close behind me."
"I feel the lump in his pants against my leg."
"Then I turn around to find his tongue with mine again."
"It’s good."
"And he’s good."
"But even after all of this, my mind is frantic."
show sam eyes -talking at center,night with dissolve
show sam eyes talking with dis
m "\"What did you kiss me again for Will?\""
show sam eyessmile -talking with dis
"I hold him closer."
"Tight."
show sam smile with dis
wi "\"Because it feels good.\""
wi "\"What kind of question is that?\""
show sam eyessmile with dis
"He chuckles."
show sam neutral talking with dis
m "\"I meant that the man you were looking for finally showed up.\""
show sam smile with dis
wi "\"I guess.\""
show sam neutral talking with dis
m "\"You got him to dance with you.\""
show sam neutral -talking with dis
wi "\"Well, who didn’t I dance with tonight?\""
"He stares at me."
show sam neutral talking with dis
m "\"You want him, don’t you?\""
show sam neutral -talking with dis
"I don’t know what to say to that."
wi "\"I don’t know if it's good for me to get everything that I want.\""
wi "\"But I do know I want to be with you right now.\""
show sam neutral talking with dis
m "\"Then just close your eyes, Will.\""
show sam eyes -talking with dis1
show sam eyes talking with dis
m "\"So why do you want him, Will?\""
show sam neutral -talking with dis1
show sam neutral talking with dis
m "\"You ain’t the risk-taking type.\""
show sam neutral -talking with dis1

menu samwill4:
    "I think I know, but I'm not sure how to say it."

    "He reminds me of you.":
        show sam annoyed talking with dis
        m "\"You’ve gotta be kiddin' me.\""
        show sam annoyed -talking with dis
        wi "\"What?\""
        wi "\"The comparison ain’t that crazy.\""
        show sam eyes talking with dis
        m "\"You’re right.\""
        show sam annoyed -talking with dis1
        show sam annoyed talking with dis
        m "\"It's completely crazy.\""
        show sam annoyed -talking with dis
        wi "\"What can I say?\""
        wi "\"You both know how to push my buttons.\""
        show sam annoyed talking with dis
        m "\"...I think you might be mixin' up the bad kinds and the good kinds.\""
        show sam annoyed -talking with dis
        wi "\"Well.\""
        show sam neutral -talking with dis
        wi "\"Sometimes the wires get crossed.\""

    "It's about doing something more than sayin' it.":
        $ SW_Points +=1
        wi "\"It's like I've said before.\""
        wi "\"Sometimes your body knows what you want a little better than your head does.\""
        wi "\"And you don't have to make sense out of it with words.\""
        wi "\"I think you lose something when you stop listening to your instincts.\""
        show sam eyes talking with dis
        m "\"I think I understand.\""
        show sam neutral -talking with dis
        wi "\"I think you do too.\""
        m "\"...\""
        wi "\"...\""
        wi "\"Sometimes people just get afraid of losing a part of themselves that they can't get back.\""
        wi "\"I want to see if that's the case for me.\""



    "He's not that risky.":
        wi "\"If he pulls something, that's probably just going to end in mutual harm.\""
        wi "\"I don't think he's brainless.\""
        show sam neutral talking with dis
        m "\"I asked you why you wanted him.\""
        show sam neutral -talking with dis1
        show sam neutral talking with dis
        m "\"Risk has little to do with that.\""
        show sam neutral -talking with dis
        wi "\"It's always on my mind, Sam.\""
        show sam eyes talking with dis
        m "\"Yeah, I get it.\""
        show sam neutral -talking with dis1
        show sam neutral talking with dis
        m "\"It just wasn't really what I was asking.\""
        show sam annoyed -talking with dis
        wi "\"I'm sorry I don't know how to answer you, then.\""
        show sam annoyed talking with dis
        m "\"...nevermind.\""
        show sam annoyed -talking with dis
        "He sounds mad at me."
        show sam eyes talking with dis
        m "\"Go for it or don't, I suppose.\""
        show sam annoyed -talking with dis
        "Yeah, he's mad at me."
        wi "\"We have more important things on our minds than me getting my dick wet, anyway.\""
        show sam eyes talking with dis
        m "\"Let's just go to sleep.\""
        show sam eyes -talking with dis
        wi "\"...Yeah.\""



    "He reminds me of something still wild in me.":
        $ SW_Points +=1
        show sam neutral talking with dis
        m "\"...what do you mean?\""
        show sam neutral -talking with dis
        "A chuckle escapes my throat."
        wi "\"S'pose it's familiar to the notion I had when I first met you.\""
        show sam neutral talking with dis
        m "\"...such as?\""
        show sam neutral -talking with dis
        wi "\"I was taken aback by your recklessness with the way you came onto me.\""
        wi "\"Badge newly donned and everything.\""
        show sam eyes talking with dis
        m "\"I wouldn't have done it if I saw the damn thing.\""
        show sam neutral -talking with dis
        wi "\"Doesn't change how real the exchange was.\""
        wi "\"Sure you needed money.\""
        wi "\"But you didn't need my money in particular that night.\""
        show sam neutral talking with dis
        m "\"The place was packed.\""
        show sam neutral -talking with dis
        wi "\"Could smell how bad you wanted it.\""
        wi "\"Saw it in the shape of your pants.\""
        wi "\"There's an unspoken language to these things.\""
        wi "\"And that man can tell my body's giving him signals, despite how careful I need to be.\""
        wi "\"I just didn't think I could give signals like that anymore.\""
        wi "\"The kinds you give off so easily.\""
        wi "\"I'm happy that ain't gone, Sam.\""
        wi "\"I thought it was.\""
        show sam eyes -talking with dis
        "Sam grunts."
        show sam neutral talking with dis
        m "\"It's not like you get many chances to be vulnerable.\""
        show sam neutral -talking with dis1
        show sam neutral talking with dis
        m "\"I might just be more numb to it because I feel vulnerable all the time.\""
        show sam neutral -talking with dis
        wi "\"I don't want either of us to feel vulnerable, Sam.\""
        wi "\"I want us to feel natural.\""
        show sam eyes talking with dis
        m "\"Is there really anything natural at all about the things we do, Will?\""
        show sam eyes -talking with dis
        wi "\"Ain't anything more natural, Sam.\""
        show sam neutral -talking with dis
        wi "\"What's unnatural is how people try to take pieces of ourselves away.\""
        wi "\"They either try and make us forget what the world made us, or downright steal it from us.\""
        show sam neutral talking with dis
        m "\"You think going to bed with this guy is gonna do all that?\""
        show sam neutral -talking with dis
        wi "\"No.\""
        wi "\"I've gotta do all the work to get that back.\""
        wi "\"This just feels like a step in the right direction.\""


show sam smile with dis
"He puts his hands inside my shirt."
"Sifts his fingers through my fur."
"Finds my chest and squeezes."
"Pulling my back to his chest."
if SW_Points<=2:
    "And we just sit there for a while."
    "Enjoying the sound of the desert wind, under the stars and the moon and the heavens that look down upon us."
    "But once we've had our fill of nature, and each other, we get back on our feet and amble back toward the barn."
    scene bg black with dissolve
    play music ("music/stag1.ogg") fadein 4.0
    scene stagnight with dis3
    "We place our glass mugs on the counter, one after the other, first hearing the clink, then the little pop of air as they settle."
    jump skipkane



if SW_Points>=3:
    show sam neutral talking with dis
    m "\"Do you really want to do something that would make me happy tonight, Will?\""
    show sam smile with dis
    wi "\"Tonight?\""
    wi "\"Yeah.\""
    wi "\"Anything.\""
    show sam neutral talking with dis
    m "\"Okay then.\""
    show sam neutral -talking with dis1
    show sam neutral talking with dis
    m "\"I’ve been thinking about some of the things you’ve said.\""
    show sam neutral -talking with dis1
    show sam neutral talking with dis
    m "\"That there are things that, if you pass them up, you won’t have a chance to do again.\""
    show sam neutral -talking with dis1
    show sam neutral talking with dis
    m "\"And you know what?\""
    show sam neutral -talking with dis1
    show sam neutral talking with dis
    m "\"I think you’ve been through that too many times.\""
    show sam neutral -talking with dis
    "I think about where he’s going with this."
    show sam smile with dis
    wi "\"So you want me to do something stupid?\""
    show sam neutral talking with dis
    m "\"Yeah.\""
    show sam smile with dis1
    show sam neutral talking with dis
    m "\"And I want to do something stupid with you.\""
    show sam eyessmile -talking with dis1
    show sam eyes talking with dis
    m "\"Something a messy, stupid, young and dumb William Adler would want to do.\""
    show sam smile with dis1
    show sam neutral talking with dis
    m "\"Not the thirty-five year old man who thinks too much and who’s a stranger in his own body sometimes.\""
    show sam smile with dis
    "We stare at the stars together for a moment."
    show sam eyes talking with dis
    m "\"You sure you want to do this alone?\""
    show sam neutral -talking with dis
    wi "\"Why, you wanna come with me?\""
    show sam smile with dis
    "He smirks."
    show sam eyessmile with dis
    m "\"Kinda.\""
    show sam smile with dis
    wi "\"Won't that be boring for you?\""
    show sam neutral talking with dis
    m "\"Not if he has you doing some of the things for him you have me do on the regular.\""
    show sam smile with dis
    "I smirk."
    wi "\"So you think this is payback, huh?\""
    wi "\"You might be disappointed if you think I'm as easy to bend over as you are.\""
    show sam eyes talking with dis
    m "\"I didn't say it was going to be easy.\""
    show sam neutral -talking with dis1
    show sam neutral talking with dis
    m "\"But I have faith the show will be satisfying when you're butting heads with somebody just as stubborn as you.\""
    show sam neutral -talking with dis1
    show sam neutral talking with dis
    m "\"Are you really willing to loosen up?\""
    show sam smile with dis

    menu samwill5:
        "Funny you should mention that..."

        "Fat chance if you think I'd lift my tail.":
            show sam neutral talking with dis
            m "\"That sounds more like you.\""
            show sam neutral -talking with dis
            wi "\"I know what I like, Sam.\""
            show sam eyes talking with dis
            m "\"If you say so.\""
            show sam neutral -talking with dis1
            $ KaneChoice = False


        "I'll be calling all the shots if anything happens.":
            show sam eyes talking with dis
            m "\"I don't really get the impression that the wolf over there has a whole lot of respect for authority.\""
            show sam neutral -talking with dis
            wi "\"If he really wants a piece of me then maybe he's going to have to learn.\""
            show sam neutral talking with dis
            m "\"Not a whole lot of people like to learn things in the bedroom, Will.\""
            show sam neutral -talking with dis1
            show sam neutral talking with dis
            m "\"Sometimes you have to take what you get.\""
            show sam annoyed -talking with dis
            wi "\"I'm aroused, Sam, not desperate.\""
            show sam annoyed talking with dis
            m "\"That's not what I meant.\""
            show sam neutral -talking with dis1
            show sam neutral talking with dis
            m "\"Opportunities can break when you're too brittle is all.\""
            show sam neutral -talking with dis
            "I shrug."
            wi "\"And sometimes things just aren't meant to be.\""
            $ KaneChoice = False


        "Maybe.":
            $ SW_Points +=1
            show sam eyes talking with dis
            m "\"You don't sound too sure.\""
            show sam neutral -talking with dis
            wi "\"Guess I ain’t.\""
            show sam neutral talking with dis
            m "\"I think this is the kinda thing you need to be sure about.\""
            show sam neutral -talking with dis1
            show sam neutral talking with dis
            m "\"Otherwise things can get messy quick.\""
            show sam neutral -talking with dis
            wi "\"Not so much the fun kind, huh?\""
            show sam neutral talking with dis
            m "\"You tend to have fun from one side of it at least.\""
            show sam neutral -talking with dis1
            show sam neutral talking with dis
            m "\"Can't say for sure about the other.\""
            show sam neutral -talking with dis1
            $ KaneChoice = True



        "If you can allow for things to go where they need to, then so can I.":
            $ SW_Points +=1
            m "\"As if you can handle doin' what I do on the regular.\""
            wi "\"I'm sure I could manage.\""
            show sam neutral talking with dis
            m "\"Well you sound sure.\""
            show sam neutral -talking with dis1
            show sam neutral talking with dis
            m "\"But that's big talk.\""
            show sam neutral -talking with dis1
            show sam neutral talking with dis
            m "\"Good thing you have a big mouth.\""
            show sam eyessmile -talking with dis
            m "\"You're probably gonna need it.\""
            show sam smile with dis
            wi "\"I'm not gonna think about that right now.\""
            show sam neutral talking with dis
            m "\"I'm sure you'll have plenty of time to mull it over if things come to that.\""
            show sam smile with dis1
            $ KaneChoice = True


    wi "\"You know Sam...\""
    wi "\"I read once upon a time ago that the lights we see in the sky, right now, are from stars that died so far away, a long time ago.\""
    wi "\"And it makes me think that I don’t think I want to be a walking reminder to people of what I used to be.\""
    wi "\"I want to feel alive right now, and live more with the time I've got left.\""
    wi "\"After all this shit with the hit and the killings I mean.\""
    show sam smile with dis
    "Sam just laughs."
    m "\"Good.\""
    show sam neutral talking with dis
    m "\"Then let’s go back to that bar.\""
    show sam smile with dis1
    show sam neutral talking with dis
    m "\"Let’s find that wolf.\""
    show sam smile with dis1
    show sam neutral talking with dis
    m "\"And we can do something stupid together.\""
    show sam smile with dis
    play sound ("sfx/clothrustle.ogg")
    "We help each other to our feet."
    stop sound
    "And walk back inside."
    stop background fadeout 2.5
    scene bg black with dissolve
    play music ("music/stag1.ogg") fadein 4.0
    scene stagnight with dissolve
    "There’s people asleep on the floor and on the rafters, but the music’s still going, and there’s still plenty of people who haven’t had their fill of dancing the night away."
    show kan at light1 with dis3:
        xpos 0.6
        yalign 1.0
    "Kane is still at the bar."
    "Somehow he has a way of still looking good even after sweating."
    "I can smell the alcohol and the sharp canine signifier on him well before I’m near, then take a seat next to him."
    show kan smile with dis
    "He glances over at me and smirks."
    show kan sneer with dis
    ka "\"Well, hello again.\""
    show kan eyes smug with dis
    ka "\"It’s good to see mixing with common thugs and vagabonds didn’t give you a heart attack, Sheriff.\""
    show kan sneer with dis
    ka "\"And that your bedtime isn’t eight o’clock.\""
    show kan smile with dis
    #sfx
    "He slides his drink towards me."
    show sam neutral -talking at halfleft,light1 with dis3:
        xpos 0.2
        yalign 1.0
        xzoom-1
    wi "\"You really think I’m no fun, don’t you?\""
    "I put my hand on his drink."
    "It’s cool to the touch and warm to the lips."
    show kan sneer with dis
    ka "\"Can’t believe it ‘til I see it.\""
    show kan wink with dis1
    show kan smile with dis1
    show sam neutral -talking light1 with dis1
    show sam neutral talking with dis
    m "\"Where do you propose he shows you then?\""
    show sam neutral -talking with dis
    wi "\"I’ve got this, Sam.\""
    "I take another sip of Kane’s drink, then put it down, and slide it back over."
    show sam eyes talking with dis
    m "\"Do you?\""
    show sam neutral -talking with dis
    show kan eyes smug with dis
    "Kane chuckles."
    show kan smug with dis
    ka "\"Yeah, do you?\""
    show kan smile with dis
    wi "\"I solemnly swear it, bounty hunter.\""
    show kan with dis
    "A few heads turn to the end of the bar and scoot away."
    "The wolf makes a disgusted noise and starts mumbling."
    show kan talking with dis
    ka "\"Not so loud...\""
    show kan with dis3
    show tod annoyed at light1 behind sam with dis3:
        xpos -0.1
        yalign 1.0
        xzoom-1
    to "\"What exactly are you fellas talking about that’s gettin’ folks so jumpy?\""
    show tod surprised with dis
    show sam eyes talking with dis
    m "\"Sex, Mr. Bronson.\""
    show sam neutral -talking with dis
    show tod sad with dis3
    "The otter clams up."
    to "\"You don’t...\""
    show tod sigh with dis
    to "\"You don’t have to be so blunt, Mr. Ayers.\""
    show sam neutral talking with dis
    m "\"With you I gotta be.\""
    show sam neutral -talking with dis3
    show kan smug with dis3
    show tod surprised with dis3
    ka "\"What, is he looking to join us, too?\""
    show kan smile with dis
    wi "\"No.\""
    wi "\"He isn’t.\""
    show kan eyes sneer with dis
    ka "\’Cept his ears are goin’ beet red.\""
    show kan smile with dis
    show sam neutral talking with dis
    m "\"Why don’t I handle ‘im.\""
    show sam smile with dis
    wi "\"Sam.\""
    show sam eyessmile with dis
    m "\"I have unfinished business with this one, Sheriff.\""
    show sam neutral -talking with dis
    wi "\"Illegal business, no doubt.\""
    show sam eyes talking with dis
    m "\"A bit hypocritical to say that, ain’t it?\""
    show sam smile with dis
    wi "\"Yeah.\""
    wi "\"The truth’s the truth, though.\""
    show sam neutral -talking with dis
    show kan eyes smug with dis
    ka "\"Now I’m invested in the entertainment.\""
    show kan smile with dis
    "He points at the otter."
    show kan talking with dis
    ka "\"Two lawmen for the price of one is too good to pass up.\""
    show kan sneer with dis
    ka "\"Y’all come together, so to speak, or I don’t go.\""
    show kan smile with dis
    "There’s a knot forming in my chest."
    wi "\"You’re a real bastard, you know that?\""
    show kan eyes smug with dis
    ka "\"Oh, you don’t know the half of it.\""
    show kan smile with dis
    "This little indulgence just turned into a logistical challenge."
    wi "\"Too risky.\""
    "He leans his chest against the table and rests his head against his paws."
    show kan smug with dis
    ka "\"You tellin’ me you’re scared of a little risk?\""
    show kan smile with dis
    "A one-note laugh escapes my throat."
    wi "\"Acting like a kid ain’t gonna make me agree to something {i}this stupid{/i}.\""
    "Sleeping together with a man is one thing, but group of us?"
    "In the open?"
    "I don't care what Nik says can happen there."
    "That's just too plain risky."
    show kan sneer with dis
    ka "\"So how about actin’ like an adult?\""
    show kan talking with dis
    ka "\"Let’s get a drink or two in you and see how you feel.\""
    show kan smile with dis
    "Sam nudges me with his elbow."
    show sam neutral talking with dis
    m "\"Come on, Sheriff.\""
    show sam neutral -talking with dis1
    show sam neutral talking with dis
    m "\"Besides, if he tries anything fishy, we outnumber him.\""
    show sam neutral -talking with dis
    show kan eyes smile with dis
    show tre br w at light1 behind kan with dis3:
        xpos 0.4
        yalign 1.0
    "Kane barks out a shout to the barkeeper."
    show kan eyes talking with dis
    ka "\"Get me a glass of spirits over here, and put it on my tab.\""
    show tre eyes with dis
    show kan with dis
    "A full, gold glass of rye smellin’ whiskey gets placed in front {nw}"
    show tre -eyes with dis
    extend "of me."
    hide tre with dis3
    wi "\"Mr. Kane.\""
    show kan talking with dis
    ka "\"Not a word until you get a glass down.\""
    show kan with dis
    "I open my mouth and he tilts his head,{nw}"
    show kan sneer with dis
    extend" eyes shining, like he’s about to laugh, fangs showing."
    show kan eyes smile with dis
    "So I down the whole damn glass."
    "It burns as it goes down but I keep on gulping."
    show kan smug with dis
    ka "\"There we go.\""
    show kan talking with dis
    ka "\"Goes down smooth, don’t it?\""
    show kan smile with dis
    "For a moment I hear the familiar voice of a young german shepherd, not a wolf."
    "I check my watch."
    "It’s eight fifty-five here, so it’s ten fifty-five, there."
    show kan smug with dis
    ka "\"So what will it be, sheriff?\""
    show kan eyes smug with dis
    ka "\"Want to do something different for a change?\""
    show kan smile with dis
    "I know this is a mistake."
    "But I also know I still want to make it."
    "There’s something important here."

    menu willkanechoice:

        "Should I make a mistake?"
        "Yes." if KaneChoice == True:
            show kan sneer with dis
            wi "\"Get me another drink.\""
            show kan eyes sneer with dis
            ka "\"You sure you can stomach it?\""
            show kan smile with dis
            wi "\"It takes a lot for me to feel it.\""
            #Treyhere
            wi "\"I want to get plastered.\""
            show kan talking with dis
            ka "\"You heard the man, barkeep.\""
            show kan sneer with dis
            ka "\"Let’s wet his whistle.\""
            show kan smile with dis
            "The golden liquid fills my cup again."
            "I down this one too."
            #sfx
            "Then I get out of my seat."
            wi "\"Let’s go.\""
            show kan talking with dis
            ka "\"I’m surprised you can stand.\""
            show kan smile with dis
            show sam neutral talking with dis
            m "\"I’m not.\""
            show sam smile with dis1
            show sam neutral talking with dis
            m "\"Ain’t surprising considerin’ the amount he can put away.\""
            show sam smile with dis
            wi "\"Let’s just do this before I change my mind.\""
            show sam neutral -talking with dis
            "Sam juts out his chin."
            show sam neutral talking with dis
            show tod annoyed with dis
            m "\"I’m letting Nik know.\""
            show sam neutral -talking with dis
            wi "\"Let’s not make this a crowd, Sam.\""
            show sam annoyed -talking with dis
            "He scratches the back of his head, pausing."
            show sam neutral talking with dis
            m "\"I just meant it might be a good idea to let him know where we’re going?\""
            show sam surprised -talking with dis
            wi "\"You know he’d want to come.\""
            show sam neutral -talking with dis
            "He pauses, and then nods."
            show sam neutral talking with dis
            m "\"Mr. Byrnes, then?\""
            show sam neutral -talking with dis
            "I shake my head."
            wi "\"Too reckless.\""
            wi "\"I’m not risking any pictures.\""
            show sam surprised -talking with dis
            show tod talking with dis
            to "\"How about we tell that Mr. Tibbits fella?\""
            show sam eyes talking with dis
            show tod surprised with dis
            "Me and Sam both say {i}no{/i} at the same time."
            show sam neutral -talking with dis
            "It leaves Todd looking a little shellshocked."
            show kan talking with dis
            ka "\"Don’t keep me waiting, fellas.\""
            show kan eyes with dis1
            show kan eyes talking with dis
            ka "\"Third barn out back.\""
            show kan with dis1
            stop music fadeout 2.5
            play background ("sfx/crickets.ogg") fadein 2.5
            scene bg barnsnight with dissolve
            "It’s dark outside, but still warm."
            "I figure that these places are vacant when the Stag closes late at night, but I can still see lanterns, and bodies moving, making shadows when they pass by the wooden slats."
            "One of the barns doesn’t have any lights on at all, but I can still see a good number of bodies shuffling around in the dark."
            "The noises and the bleachy smells are unmistakable."
            show kan at halfright,night with dissolve
            show kan talking with dis
            ka "\"Why the sour look, sheriff?\""
            show kan eyes with dis1
            show kan eyes talking with dis
            ka "\"You too good to mingle with the masses?\""
            show kan sneer with dis
            "He gives me a nasty grin."
            ka "\"Not everybody’s pretty, you know.\""
            show kan smile with dis
            "They could honestly be doing God knows what in there and nobody would know until sunlight."
            wi "\"Sounds like they're getting their groins into anything they can in there.\""
            show kan eyes talking with dis
            ka "\"Probably.\""
            show kan smile with dis
            "He puts on a tone of mock concern."
            show kan smug with dis
            ka "\"You gonna go arrest them for the indecency of it all?\""
            show kan smile with dis
            wi "\"No.\""
            show kan talking with dis
            ka "\"Didn’t think so.\""
            show kan smile with dis1
            scene bg gymbarnnight with dissolve
            "The barn he leads us to has a loft, and a lot of hay."
            "There’s figures moving in the corners, but the lights are out."
            "He puts a finger to his face and then points to a ladder."
            play sound ("sfx/creak1.ogg")
            queue sound ("sfx/creak2.ogg")
            queue sound ("sfx/creak3.ogg")
            "Then he starts climbing."
            "We follow."
            stop sound
            "Climbing underneath him, I can smell him getting more excited."
            "I try not to let it affect me too much."
            "Yet."
            play sound ("sfx/match.ogg")
            scene bg black with dissolve
            scene bg gymbarnupnight with dissolve
            "Once we’re all at the top of the loft, Kane takes out a lighter and makes one of the lanterns glow."
            stop sound
            show kan eyes smug at right,light2 with dis3
            ka "\"Very good everybody.\""
            #sfx
            show kan smile with dis
            "He brushes the hay off his knees, and his head pans left to right."
            show kan smug with dis
            ka "\"To get this rodeo started...\""
            show kan sneer with dis
            ka "\"...why don’t we have the sheriff get on his knees.\""
            show kan with dis
            "I figured he was gonna try to pull this."
            wi "\"I don’t get on my knees.\""
            "The wolf sucks his teeth."
            show kan talking with dis
            ka "\"You do tonight.\""
            show kan smile with dis3
            show tod surprised at centerleft,light2 with dis3:
                xzoom-1
            to "\"Why does he need to get on his knees?\""
            show kan talking with dis
            ka "\"Why else?\""
            show kan sneer with dis
            ka "\"Because he’s going to suck me off, and get my seed all over his sharp nose.\""
            show kan smile with dis
            #sfx
            "We hear more movements in the corner."
            "It sounds like somebody else is finishing."
            show tod sigh with dis3
            to "\"Well...\""
            to "\"I could always do it instead?\""
            "The wolf starts laughing."
            show kan eyes smug with dis
            ka "\"Now there’s a public servant who understands the meaning of service.\""
            show tod surprised with dis3
            show kan smile at centerright,light2 with dis3
            "He walks toward Todd and musses the fur on his head a bit."
            show kan talking with dis
            ka "\"But he’s not gonna cut it doin' it all by himself, Adler.\""
            show kan smug with dis
            ka "\"It’s gotta be you.\""
            show kan with dis
            wi "\"Nothing’s ever {i}gotta{/i} be me.\""
            show kan eyes at right,light2 with dis3
            "The wolf shakes his head."
            show sam annoyed -talking s at light2 behind tod with dis3:
                xzoom-1
                xpos -0.1
            "Sam rolls his eyes."
            show tod surprised at centerleft,light2 with dis3:
                xzoom 1
            show sam annoyed talking s with dis
            m "\"Now come on, Will.\""
            show sam eyes -talking s with dis1
            show sam eyes talking s with dis
            show kan smile with dis
            m "\"Just how many times have I done it for you?\""
            show sam smile s with dis
            "I just now notice Sam’s shirt is gone."
            play sound ("sfx/clothrustle.ogg")
            show sam smile n with dis3
            "He’s stripping his pants off too."
            stop sound
            "God he looks good."
            show sam n with dis3
            wi "\"Because before today, you never asked why I wouldn’t.\""
            show sam eyes talking n with dis3
            m "\"Cause before today, you’d just say you’re not a cock sucker.\""
            show sam smile n with dis3
            "I chuckle."
            wi "\"Guess you know me well enough.\""
            show kan eyes talking with dis
            ka "\"Now now.\""
            show kan smug with dis
            ka "\"I hold the belief that anybody can learn.\""
            show kan smile with dis
            "I’m starting to get the urge to put this cocky sunovabitch in his place."
            show kan eyes smile with dis
            "But then I feel something enter my mouth."
            "It’s warm and wet and flexible."
            "It’s Kane's tongue."
            "He’s kissing me."
            "He's testing my mouth with powerful scoops and delicate flicks."
            "And he’s damn good."
            "Despite all the alcohol I drank, I feel myself swelling."
            show kan eyes smug with dis
            ka "\"If you like to kiss that much, then I know you like to suck.\""
            show kan smile with dis
            "He pats my cheek with his palm."
            show kan talking with dis
            ka "\"Now on your knees, or else we’re in for a very awkward and uneventful night, because I’m not gonna...\""
            show kan smile with dis
            #sfx
            "He puts his paws on my shoulders and guides me lower."
            show kan sneer with dis
            ka "\"Budge.\""
            "I mean to stand again, to stand my ground still, but I’m just plain dizzy."
            "The alcohol’s finally kicking in."
            "Just what the hell am I doing down here if not to do exactly what he's expecting?"
            scene wilcg7a at light2 with dissolve:
                subpixel True
                ease 30.0 zoom 1.2
            to "\"Sucking it is supposed to feel really good, right?\""
            "I feel a little bit like I’m in a fever dream, watching Todd lean in to Sam’s crotch."
            m "\"Better than good.\""
            ka "\"Especially once you get used to the taste.\""
            m "\"You might even come to crave it.\""
            "Todd’s just staring at Sam's pecker for a good while."
            "I almost think he’s going to stand up and leave for a moment."
            "God knows that’s the smarter choice."
            "Because I know that the both of us would be run out of town if the wrong people saw us in this position."
            wi "\"Todd...\""
            scene wilcg7b at light2 with dis3:
                subpixel True
                zoom 1.2
            "But right as I say his name he leans in to lick."
            "He makes a whiny little squeak, and Sam pulls back just far enough to see the shine of spit on his cock."
            "I see the shine of slime on his lips."
            m "\"Not too bad for a Mormon boy, huh?\""
            "Sam's pre starts to drip in front of Todd."
            "And then he dips in to lick again, cleaning it off of Sam."
            "That squeaky whine is just a bit louder now."
            scene wilcg7c at light2 with dis3:
                subpixel True
                zoom 1.2
            ka "\"Gonna let your deputy show you that he has the bigger pair of balls?\""
            "Kane walks toward me."
            "Cock out."
            "His smell’s much stronger now that he’s out of his pants."
            "And he’s already half stiff."
            ka "\"Showtime.\""
            stop background fadeout 5.0
            scene bg black with dissolve

            "I remember the last time I sucked."
            "I can smell the wet dirt, the grass and the young sweat."
            wl "\"William.\""
            "I know from how hard he’s hitting the back of my throat that he’s eager."
            wl "\"{i}Ohh, William.{/i}\""
            "And I can taste him finish."
            wl "\"{i}Ahhh!...Ahhh!{/i}\""
            play sound ("sfx/doorburst.ogg")
            "But the door’s slamming open."
            stop sound
            wf "\"{i}WILLIAM!{/i}\""
            wf "\"{i}YOU GODDAMN COCK SUCKER!{/i}\""
            play background ("sfx/crickets.ogg") fadein 1.5
            scene wilcg7c at light2 with dis3:
                subpixel True
                zoom 1.2
                pause 0.6
                ease 23 zoom 1.1
            "Then I can smell the hay and the desert air again."
            "And wolf."
            "Eager, impatient wolf."
            ka "\"C’mon.\""
            "He bounces his prick with his muscles in front of me."
            m "\"He’s had more than two shots.\""
            m "\"Give him some patience.\""
            m "\"We’re not exactly in a hurry over here\""
            "Todd just mumbles and sputters with the occasional squeak, considering his mouth keeps full."
            "Samuel gasps when the otter starts to bob, and he thrusts in sync with the soft suckles."
            "Kane sighs, bringing his prick closer."
            ka "\"You just gonna stare at me with those puppy dog eyes, or are you going to get to work already?\""
            scene wilcg7d at light2 with dis3:
                subpixel True
                zoom 1.1
                pause 0.6
                ease 20 zoom 1.0
            "Fine then."
            "I lean forward a bit, parting my lips."
            "I know this time isn’t going to be like the last."
            "It’s been years."
            "And Sam is here with me."
            "So I sniff."
            "That masculine stink is driving me up the walls."
            ka "\"That’s it.\""
            "It’s like my whole body is coming awake."
            "And this smug bastard knows it."
            scene wilcg7e at light2 with dis3
            "I feel his hand tug my ear as he pulls me closer."
            "My tongue is lolling."
            "I want to lick it."
            "Carefully."
            "And I know that he knows it."
            "Just to make sure that it’s not too thick."
            scene wilcg7f at light2 with dis3
            wi "\"Mmph!\""
            ka "\"What is this, a dinner party?\""
            wi "\"Mngh...\""
            scene bg black with dissolve
            scene wilcg8c at light2 with dis3
            "The wolf lets me off to breathe."
            "I gasp for air, and my mouth feels slimy and salty already."
            "I can hear Sam laughing."
            m "\"You’re here to suck some stiff cock Will, not go romancing it.\""
            "Todd doesn’t give any input, but considering the sounds he’s making, he can’t."
            scene wilcg8a at light2 with dis3
            ka "\"Decent first attempt.\""
            ka "\"You have one of these, Sheriff.\""
            ka "\"You know what feels good.\""
            scene wilcg8b at light2 with dis3
            ka "\"Balls to the base.\""
            scene wilcg8c at light2 with dis3
            ka "\"Lick.\""
            "He points it at me, commanding."
            scene bg black with dissolve
            scene wilcg7e at light2 with dis3
            "So I give him what we both want."
            "I let my tongue drag against him, starting where his balls droop lowest, all the way up the shaft."
            "There’s a dew drop of more salty slime that sticks to me even as I pull away."
            ka "\"There we go.\""
            ka "\"That feels nice.\""
            ka "\"Feeling more like a cocksucker now?\""
            wi "\"...\""
            ka "\"I can tell this isn’t your first time.\""
            m "\"Really?\""
            ka "\"Mhm.\""
            ka "\"He knows the right spots.\""
            "I lick him again to make him shut up."
            ka "\"Ohh...\""
            ka "\"Now that feels nice.\""
            ka "\"Awfully domestic for such a dignified mouth.\""
            wi "\"Mrph...\""
            "He spits on his own dick, letting the drool drip down slow."
            ka "\"Clean it.\""
            scene wilcg7f at light2 with dis3
            "He pushes me down, forcing more spit into my mouth, more drool out of my cheeks."
            ka "\"Damn.\""
            ka "\"Even I wouldn’t have followed those orders without a little resistance.\""
            "At the end of the day, I’m plenty experienced with following orders, right?"
            "Even when they taste bad."
            "But I can’t pretend any of this tastes bad."
            scene wilcg8c at light2 with dis3
            wi "\"...I need this.\""
            scene wilcg8b at light2 with dis3
            ka "\"What’s that, Sheriff?\""
            ka "\"What did you say?\""
            scene wilcg8c at light2 with dis3
            "I’m not going to repeat myself."
            m "\"I believe he said he needs this, Mr. Kane.\""
            ka "\"Oh, I can tell.\""
            scene wilcg8b at light2 with dis3
            ka "\"He reeks like a whore just from startin' to suck just one cock.\""
            scene wilcg8c at light2 with dis3
            m "\"Oh yeah.\""
            m "\"He smells a little strong when he’s excited, but you get used to it.\""
            ka "\"Maybe it’s time he smelled a little like somebody else.\""
            wi "\"Wait--\""
            "I push him away, trying to get a breather, wiping all of the spit and pre from my face while sweat beats down on my brow."
            scene wilcg8b at light2 with dis3
            ka "\"Hold his arms?\""
            scene wilcg8c at light2 with dis3
            "I feel Sam reach behind me while Todd coughs wildly."
            m "\"Like this?\""
            wi "\"Sam!\""
            ka "\"Yeah, just like that.\""
            scene wilcg8a at light2 with dis3
            ka "\"Any last words before things get messy, Sheriff?\""
            scene wilcg8c at light2 with dis3
            "I swallow my own spit, watching the shadow of his prick loom over my face."
            wi "\"Yeah.\""
            wi "\"Just do it in my mouth.\""
            "The wolf grins big, and then squeezes the base of his cock. Hard."
            ka "\"No.\""
            "He points the tip of his dick at my face."
            scene wilcg8d at light2 with dis3
            "Then he starts throbbing."
            "Rope after rope of his seed spills out of him."
            "Directed at me."
            "The splash is warm."
            "And disgusting."
            "But my cock feels so hard that I feel it could practically tear my own pants off."
            scene wilcg8e at light2 with dis3
            ka "\"Now there’s a pretty sight.\""
            scene wilcg8f at light2 with dis3
            ka "\"I should humiliate lawmen more often.\""
            "I sputter, some of his seed landing in my throat and making me gag."
            "Slime drips from my mouth to the floor."
            "I sputter as I try to speak clearly."
            wi "\"You’re really pushing your goddamn luck.\""
            "He places his paw on the erection inside my clothes and squeezes."
            ka "\"And you’re really pushing your way through your work pants.\""
            ka "\"Help me strip him.\""
            "They take my shirt first."
            "Then my suspenders."
            "Then my pants, my socks, my garters."
            "He sniffs the air belligerently."

            ka "\"Phew.\""
            scene wilcg8e at light2 with dis3
            ka "\"He really is a happy boy, ain’t he?\""
            scene wilcg8f at light2 with dis3
            wi "\"Tell Sam to let go of my arms and I’ll show you how happy I really am with your tone.\""
            "He shakes his head."
            ka "\"We ain’t done yet.\""
            "He spreads my legs and whistles."
            ka "\"Want to know why I insisted on coming on your face?\""
            "I think, feeling more of his seed spill down the side of my face."
            wi "\"Blatant disrespect.\""
            "He laughs."
            ka "\"Well, that too.\""
            ka "\"But mostly I just want you to remember the smell of me when I make you cum, lawman.\""
            scene bg black with dis3
            "As the warm moisture sinks into my snout, so too do his lips on my tip."
            "My whole body shivers from how sensitive my tip is, and I let out a whine."
            "He pulls off for just a moment to speak again."
            ka "\"I bet you’ll think about it for the rest of your life.\""
            "He dips down."
            "And again."
            "And again."
            "And he slurps and smacks his mouth when he licks."
            "First his tongue bathes my shaft and my balls."
            "But then it slips beneath my tail."
            "My gut instinct is to shout, but the yell is silenced by Sam’s tongue in my mouth."
            "And I can’t do anything."
            "Not a goddamn thing."
            "Not until my balls pull back."
            "Until my seed comes spewing out of me."
            "Thick, and hot, and stinking."
            "And the wolf eats it up greedily."
            "My head is so foggy and my eyelids are so heavy that I can’t focus anymore."
            "I remember just one thing before darkness overtakes me."
            "Samuel wrapping his body around me, cleaning all of the filth off me with his tongue."
            stop background fadeout 2.0
            pause 3.0
            play ambient ("sfx/birds.ogg") fadein 3.5
            #kanecont
            "Fuck."
            window hide
            scene bg wilcg9 with medium_dissolve:
                subpixel True
                truecenter
                zoom 1.45
                ease 50.0 zoom 1.0
            pause 3.5
            window show
            "I’d never slept on a bale full of hay this well."
            "Sam has his arms around me and we’re both soft, if a bit sticky."
            m "\"Finally awake over there, Sheriff?\""
            "I open my eyes and rub my face."
            wi "\"Yeah.\""
            wi "\"I’m up.\""
            m "\"Good.\""
            m "\"Was it everything you had wanted?\""
            wi "\"Well...\""
            wi "\"It was a little bit crazy.\""
            wi "\"But yeah.\""
            wi "\"I think it was.\""
            "He gives me a soft kiss on my whiskers, slipping me a sliver of tongue."
            m "\"Good.\""
            m "\"I was worried we were taking things a bit far.\""
            wi "\"Honestly?\""
            wi "\"You could have pushed me harder.\""
            "I give him a stony glare and he stares back at me."
            "Then his unserious ass goes cross-eyed, and we both break out into laughter."
            "Until a sunbeam strikes me across the face and I feel a stab of pain behind my eyes."
            scene bg gymbarnupday
            show sam surprised n at center,dark3
            with dis3
            wi "\"Shit...\""
            "I wince and he touches my arm."
            show sam talking with dis
            m "\"You okay?\""
            show sam -talking with dis
            wi "\"Yeah...\""
            show sam neutral -talking with dis
            wi "\"I’m fine.\""
            wi "\"If anything, I would've expected to have a headache after a night like that, but everything’s clear.\""
            show sam eyes talking with dis
            m "\"That’s good then.\""
            show sam -eyes -talking with dis
            wi "\"Why... should I not be?\""
            wi "\"It’s nice here with you.\""
            show sam surprised talking with dis
            m "\"Well...\""
            show sam surprised -talking with dis1
            show sam surprised talking with dis
            m "\"You sound like you're in a better condition than the deputy.\""
            show sam surprised -talking with dis
            "We hear loud snores coming from a barrel."
            "The big ass cheeks and the tail of a river otter are sticking out of it, top-side up."
            wi "\"Well, shit...\""
            show sam neutral talking with dis
            m "\"Also it’s an hour ‘til noon.\""
            show sam -talking with dis
            "I rub my snout a little deeper, trying to massage some of the pressure away."
            wi "\"Not good but could be worse.\""
            "I check my wrist to get a more precise time."
            "And that’s when I notice that my watch is gone."
            play music ("music/quiet.ogg") fadein 5.5
            wi "\"...The hell?\""
            "I look around me and under me and see if I can get some idea of what’s going on."
            "I feel my heart pump quick, but then relax, realizing Sam knew the time."
            show sam surprised with dis
            wi "\"Can I have my watch back Sam.\""
            show sam sad with dis
            "He averts his gaze."
            m @talking "\"I don’t have it.\""
            show sam surprised -talking with dis
            wi "\"The hell you mean you don’t have it?!\""
            show sam surprised talking with dis
            m "\"All our clothes are gone...\""
            show sam sad -talking with dis
            "He breaks eye contact again."
            m @talking "\"...including your badge.\""
            wi "\"The fuck?!\""
            show sam surprised with dis
            "I roll out of the hay, searching under it for the watch with the leather strap, just in case the exact thing that I know has happened hasn’t happened."
            wi "\"The motherfucker!\""
            wi "\"I’ll throttle him for this!\""
            hide sam with dis3
            "I stand up and walk over to the window of the loft."
            "There’s people walking around outside."
            "Shit."
            show sam surprised n at center,dark3 with dissolve
            show sam surprised talking with dis
            m "\"The good news is he didn’t get your guns or your keys.\""
            show sam surprised -talking with dis1
            show sam surprised talking with dis
            m "\"I sort of guessed that this might happen so I hid them.\""
            show sam sad -talking with dis1
            show sam sad talking with dis1
            m "\"Didn’t think he’d want the badge but I guess I was wrong.\""
            show sam neutral -talking with dis
            wi "\"Well thank you, Sam, but I can’t exactly stroll into town just wearing a holster.\""
            show sam neutral talking with dis
            m "\"There’s a burlap sack in the corner.\""
            show sam neutral -talking with dis
            wi "\"You gotta be shitting me, Sam.\""
            show sam eyes talking with dis
            m "\"It’s better than nothin’, ain’t it?\""
            show sam neutral -talking with dis1
            show sam neutral talking with dis
            m "\"Not like I’m the respectable looking one in the first place.\""
            show sam neutral -talking with dis
            wi "\"I ain’t gonna cut holes into a sack and walk around like I’m in a nightie for the most doped up man alive.\""
            show sam neutral talking with dis
            m "\"Well there’s three of us so there’s probably enough just to cover our peckers.\""
            show sam neutral -talking with dis1
            show sam neutral talking with dis
            m "\"Not unless you want to go looking for a swimming hole and swipe somebody else’s clothes.\""
            show sam neutral -talking with dis
            "Son of a bitch."
            "Just the thought of myself tucking my tail under my legs to hide my ass crack in broad daylight in the middle of town makes my skin crawl."
            "That bastard Kane didn’t want to just make me his bitch, he wanted to publicly humiliate me."
            "This is what I get for allowing myself to have something?"
            show sam surprised with dis
            ni "\"...Sam?\""
            "The two of us flinch."
            ni "\"Sam is that you?\""
            "We see a very unkempt-looking Nikolai walking into the barn."
            show sam surprised talking with dis
            m "\"Up here!\""
            show sam surprised -talking with dis1
            scene bg gymbarn
            show nik neutral at center
            with dis3
            "He turns around and spots us."
            "Thank Christ."
            show nik surprised with dis3
            ni "\"Um.\""
            wi "\"Hi there.\""
            show nik sidelook with dis3
            ni "\"...you both tried the firebarrel bourbon didn’t you?\""
            wi "\"What?\""
            wi "\"No.\""
            show nik surprised with dis3
            ni "\"Then why are you both naked?\""
            ni "\"It’s half-past eleven.\""
            m "\"Somebody nicked our clothes, Nik.\""
            m "\"We can’t come down...\""
            ni "\"Oh!\""
            show nik sidelook with dis3
            ni "\"Well this is too bad.\""
            show nik disappointed with dis3
            "He puts his hands on his hips like he’s thinking, albeit in a casual manner."
            wi "\"You’re understating things a bit there, Nik.\""
            show nik talking with dis3
            ni "\"Why don’t I go get you both some clothes?\""
            show nik -talking with dis
            wi "\"...That would be appreciated, Nik.\""
            hide nik with dis3
            "Sam tells Nik that he hid our guns and keys underneath a barrel."
            "I sigh and feel my heart thump just a little bit slower when I see that they’re still there."
            show nik neutral at center with dis3
            wi "\"There’s spare clothes in my bedroom.\""
            wi "\"Use the iron key for the office and the brass one for the apartment.\""
            show nik talking with dis
            ni "\"Two shirts, two pants, and some undergarments?\""
            show nik -talking with dis
            "I hear Todd making groaning noises in the barrel."
            show nik surprised with dis
            wi "\"...three, actually.\""
            "Nik looks shocked."
            ni "\"Who else is up there?\""
            wi "\"Just the deputy.\""
            ni "\"The deputy?!\""
            ni "\"Why?\""
            wi "\"Does it matter?\""
            wi "\"Now you gonna help us out here Nik, or nah?\""
            show nik disappointed with dis3
            ni "\"Considering you need all the help you can get right now, yes.\""
            ni "\"It is just a little shocking to see you like this.\""
            wi "\"You don’t have to tell me that.\""
            show nik sad with dis3
            ni "\"I can’t help but feel like this is my fault to some degree.\""
            ni "\"I will be back as quickly as possible.\""
            hide nik with dis3
            "Nik hurries out of the barn and I see him stride across the glade as fast as his stride can take him."
            scene bg gymbarnupday with dis3
            "Todd squeals as Sam tries to tug him out of the barrel,holding onto his stubby hips, but his fur is so oily he keeps slipping on back in like cranberry sauce stuck in a can."
            "It doesn’t take long for me to get tired of watching this so I help Sam tip the barrel sideways so gravity can do most of the work."
            #adjust
            show tod arms sigh n at left,dark3:
                xzoom-1
            show sam neutral n at right,dark3
            with dis3
            to "\"Oof, that smarts!\""
            show tod sigh n with dis3
            show sam talking n with dis3
            m "\"You alright, Deputy Bronson?\""
            show sam -talking n with dis3
            show tod surprised n with dis3
            to "\"Well, I reckon so.\""
            wi "\"How’d you get in there?\""
            to "\"Truth be told I don’t exactly remember.\""
            show tod sigh n with dis3
            to "\"Feels like most of the blood is still rushin’ out of my head.\""
            show tod surprised n with dis3
            to "\"All I know is that I definitely didn’t hurt.\""
            show tod annoyed n with dis
            show sam eyes talking n with dis
            m "\"Yeah, you’re definitely not the type to gag.\""
            show sam -eyes -talking with dis
            "Todd nods, but after a moment {nw}"
            show tod surprised n with dis
            extend "does a double take."
            to "\"Oh God we really...\""
            show sam smile with dis
            "Sam smirks."
            m "\"Sure did.\""
            m "\"And so did Will.\""
            "He’s flustered now."
            "Then he lowers his voice."
            show sam -smile with dis
            to "\"Is that why all my clothes are gone?\""
            wi "\"No Todd.\""
            wi "\"That’s because somebody stole them.\""
            to "\"Stole ‘em?!\""
            to "\"Well people can’t go doin’ that. I need my clothes to walk around in!\""
            wi "\"It’s okay. Nik is already getting some of my clothes.\""
            to "\"Now how am I supposed to wear your clothes William?\""
            to "\"They’ll fall right offa me!\""
            wi "\"There’s a burlap sack in the corner if you prefer that.\""
            show tod sad n with dis3
            "He looks over."
            "I’m starting to think he might actually consider it."
            show tod surprised n with dis3
            wi "\"Just wear my damn clothes until you can get home and swap them with your own.\""
            to "\"But I want my other clothes back!\""
            show sam annoyed talking with dis
            m "\"He can keep mine.\""
            show sam annoyed -talking with dis1
            show sam annoyed talking with dis
            m "\"They’re practically rags at this point.\""
            show sam annoyed -talking with dis
            to "\"But my vest was special!\""
            show sam neutral with dis
            wi "\"Listen, Todd.\""
            wi "\"If I see him again I’ll chase him down like the dog he is and make him regret taking our stuff.\""
            wi "\"I hope I’ve made myself clear?\""
            show tod sigh n with dis
            to "\"...yes, Sheriff.\""
            wi "\"We’ve wasted enough time on this stupid detour.\""
            wi "\"Questioning Mrs. Greene one last time is far more important than settling any of these personal vendettas.\""
            to "\"...okay.\""
            show tod sad n with dis
            "I sit down in the corner and cross my legs while Sam leans against a window."
            #adjust
            show tod annoyed n with dis
            show sam eyes talking with dis
            m "\"In spite of the thief, I hope y’all both had a good time last night.\""
            show sam -eyes -talking with dis
            wi "\"Now’s not the time, Sam.\""
            show tod annoyed n at halfleft,transparent with dis3
            "Todd gets a little bit closer to Sam and leans against the other side of the window."
            show tod sigh n with dis3
            to "\"I thought it was a great time, Mr. Ayers.\""
            show tod n with dis3
            m "\"Glad to hear it.\""
            show tod surprised n with dis3
            show sam eyes talking with dis3

            m "\"Because you still both owe me money.\""
            show sam -eyes -talking with dis
            play sound ("sfx/creak3.ogg")
            "I stand up, mostly because I feel like shaking Sam, but outside the window I see Nik is already on his way back with bundles under his arm."
            wi "\"Nik is damn speedy when he wants to be, huh?\""
            show sam talking with dis
            m "\"It’s the long stride.\""
            show sam -talking with dis1
            stop ambient fadeout 4.0
            scene gymbarn with dis3
            "I can feel the collective relief wash over us as Nik gets into the building and hands us our clothes, shying away from looking too close."
            "Sam fits into my clothes just fine since we’re nearly the same size."
            "Todd definitely looks like he’s wearing some sort of baptism outfit in my shirt."
            scene barns with dis3
            "I thank Nik now that we’re finally properly ready to get on with what we need."
            "Todd dashes off homeward to get a proper change of clothes."
            "Nik parts ways with us, assuring us that he’ll see us again soon."
            "Sam comes with me back to my office to freshen up."

            jump marcymerge


        "No.":
            $ KaneChoice = False
            show kan with dis
            wi "\"I’m afraid that’s going to be a no, Mr. Kane.\""
            show kan eyes with dis
            "He shrugs and then takes a swig of his beer."
            show kan eyes talking with dis
            ka "\"Suit yourself, lawman.\""
            show kan with dis
            play sound ("sfx/glass.ogg")
            "He sets the glass down on the table with a tink."
            stop sound
            show kan smile with dis
            ka "\"Just try not to hit the whiskey too hard.\""
            show kan sneer with dis
            "The slight grin on his face spreads a little wider."
            ka "\"You seem like the type who keeps a bedtime.\""
            label willsplitB2:
            #sfx
            "Kane whistles as he walks away, turning his glass over, and placing it in front of me, {nw}"
            hide kan with dis3
            extend "before disappearing into the crowd and out the barn door."

            if SW_Points>=4:
                show sam eyes talking with dis
                m "\"You sure that’s what you really wanted?\""
                show tod annoyed with dis
                show sam neutral -talking with dis
                "I scowl a bit."
                wi "\"Well.\""

                wi "\"Not particularly.\""
                wi "\"But it’s really not the time for me to get sloppy.\""
                show sam talking with dis
                m "\"Funny thing about time.\""
                show sam -talking with dis1
                show sam talking with dis
                m "\"It often runs out.\""
                show sam -talking with dis
                "He leans forward on his stool and looks at me."
                show sam talking with dis
                m "\"How many chances like this do you think you’re gonna get?\""
                show sam -talking with dis
                "I close my eyes and rub my eyelids."
                "He whispers in my ear."
                show sam eyes talking with dis
                m "\"I know how much you wanted this.\""
                show sam neutral -talking with dis
                "I lower my voice to a whisper too, but it comes across more as a growl."
                wi "\"Going through life isn’t always about doing what you want.\""

            else:
                show sam eyes talking with dis
                m "\"Welp.\""
                show sam neutral -talking with dis1
                show sam talking with dis
                show tod annoyed with dis
                m "\"Easy come, easy go.\""
                show sam annoyed -talking with dis1
                show sam annoyed talking with dis
                m "\"He seemed a bit pushy for your taste, anyhow.\""
                show sam neutral -talking with dis1
                hide sam
                hide tod
                with dis3
                #sfx
                "I look out into the crowd again, wondering if he’s still lurking somewhere."
                $ renpy.music.set_volume(0.5, delay=5.0, channel='music')
                "Then I see the back of a German shepherd’s head."
                "He’s wearing a black tan cardigan and a crisp white shirt."
                wi "\"Aiden?\""
                "The figure doesn’t turn around and keeps shuffling through the crowd."
                "I knew he wouldn’t be turning his head."
                "Because that wasn’t his name, and he isn’t really here."
                "But there was a sudden pang of hope that made me want to call out anyway."
                $ renpy.music.set_volume(1.0, delay=5.0, channel='music')
                show tod surprised at left,light1:
                    xzoom-1
                show sam surprised at centerleft,light1:
                    xzoom-1
                with dissolve
                show sam surprised talking with dis
                m "\"Who’s Aiden?\""
                show sam surprised -talking with dis
                "I shake my head."
                wi "\"Somebody from my old home who I used to know.\""
                show sam annoyed -talking with dis
                "Sam’s brow furrows."
                show sam annoyed talking with dis
                m "\"From the city?\""
                show sam surprised -talking with dis
                wi "\"Yeah.\""
                show sam surprised talking with dis
                m "\"Why would somebody like that be here?\""
                show sam surprised -talking with dis
                wi "\"He wouldn’t be.\""
                wi "\"I just wanted to see if there was a coincidence.\""
                "Sam rightfully strums his paw on the table as if I had just started speaking in tongues."
                show sam annoyed talking with dis
                m "\"Okay then.\""
                show sam annoyed -talking with dis1


            hide tod
            hide sam
            with dis3
            label skipkane:
            "The barkeep, a tawny fox, approaches and sets down a mug to get our attention."
            bartre "\"More pints?\""
            show sam annoyed talking at left,light1 with dis3:
                xzoom-1
            m "\"I think we’re probably done.\""
            show sam annoyed -talking with dis
            wi "\"Yeah, give me another.\""
            "The fox nods and takes my mug to a barrel."
            show sam annoyed talking with dis
            m "\"Weren’t you just making a fuss about not getting sloppy?\""
            show sam annoyed -talking with dis
            wi "\"I have a much higher tolerance than you.\""
            wi "\"Frankly, I’d probably get more lip from anybody here if I {i}weren’t{/i} drinking.\""
            ni "\"There you both are.\""
            show nik at right,light1 with dis3
            "I hear Nik’s voice behind me before I turn around to see him."
            show nik sidelook with dis3
            wi "\"Hello Nik.\""
            show sam annoyed talking with dis
            m "\"...Hello.\""
            show sam annoyed -talking with dis3
            show nik disappointed with dis3
            ni "\"So...\""
            ni "\"The reason why I wanted you to come tonight was so we could spend the night {i}together{/i}.\""
            show nik neutral with dis3
            wi "\"I thought that’s what we’re doing.\""
            show sam annoyed talking with dis
            m "\"...Yes.\""
            show sam annoyed -talking with dis3
            show nik disappointed with dis3
            ni "\"Well, no.\""
            ni "\"That is not exactly the truth.\""
            ni "\"You both keep going off together.\""
            show nik sidelook with dis3
            ni "\"Without me.\""
            show nik neutral with dis3
            "Oh."
            "Oh boy."
            "I didn’t think he’d want to go into this tonight."
            wi "\"We’re glad to have you here now.\""
            wi "\"Aren’t we, Sam?\""
            show sam eyes talking with dis
            m "\"Hold on, I could use another drink.\""
            show sam neutral -talking with dis1
            show sam talking with dis
            #Treyhere
            m "\"Barkeep!\""
            show sam -talking with dis1
            show sam talking with dis
            m "\"Over here! Another pint, please!\""
            show sam annoyed -talking with dis
            wi "\"You see?\""
            wi "\"Everybody’s having a great time.\""
            show nik eyestalking with dis
            ni "\"You are right.\""
            show nik neutral with dis1
            ni @talking "\"I do see.\""
            #sfx
            "He sits on the opposite side of Sam with a thud."
            ni @talking "\"However, it would be good to hear that from Sam himself.\""
            "Sam is not looking at him."
            "In fact, he’s staring straight forward."
            "Scowling."
            show sam annoyed talking with dis
            m "\"Okay.\""
            show sam annoyed -talking with dis1
            show sam annoyed talking with dis
            m "\"Let’s talk about anything.\""
            show sam annoyed -talking with dis1
            show sam annoyed talking with dis
            m "\"It’s good that William’s here, too, considering he’d hear about anything we talked about anyhow.\""
            show sam annoyed -talking with dis1
            show sam annoyed talking with dis
            m "\"Saves us some time.\""
            show sam annoyed -talking with dis3
            show nik disappointed with dis3
            ni "\"You would have done the same to me if something was obviously wrong and you withheld it!\""
            show sam annoyed talking with dis
            m "\"Wrong.\""
            show sam annoyed -talking with dis3
            show nik angry with dis3
            ni "\"Not wrong!\""
            play sound ("sfx/tablepunch.ogg")
            show sam surprised
            "Nikolai’s fist pounds the table." with vpunch
            show sam annoyed with dis
            "Some of the other bar patrons are looking our way."
            stop sound
            "The barkeep delivers Sam’s beer."
            "Slowly."
            ni "\"I thought somebody was after you!\""
            ni "\"I thought you were in danger, that your client wanted to hush you up, or that you were borrowing money...\""
            ni "\"I was scared for you and you cut me out!\""
            show nik neutral with dis3
            show sam annoyed talking with dis3
            m "\"By ratting on me to William?!\""
            show sam annoyed -talking with dis
            "I understand where he’s coming from, but it’s awkward being talked about like that when I’m right here."
            show sam eyes talking with dis
            m "\"Fuck!\""
            show sam annoyed -talking with dis3
            show nik sidelook with dis3
            ni "\"I want a beer also, barkeep.\""
            show nik neutral with dis3
            "This poor man exhales."
            bartre "\"I'll go do that then...\""
            show sam eyes with dis
            "Sam sips his drink while Nik becomes the one to taps his claws."
            wi "\"Do y’all feel better now?\""
            show sam eyes talking with dis
            m "\"Yes.\""
            show sam annoyed -talking with dis
            ni @talking "\"No.\""
            "I rub my temples."
            wi "\"Well, I’m sorry you think I’m that much of a bastard, Sam, but Nik came looking for me and told me what happened based on concern for you.\""
            show sam annoyed talking with dis
            m "\"Because it was a stupid thing to do.\""
            show sam annoyed -talking with dis3
            show nik angry with dis3
            ni "\"Stupid?!\""
            show sam annoyed talking with dis
            m "\"You can be that much of a bastard, Will.\""
            show sam annoyed -talking with dis1
            show sam annoyed talking with dis
            m "\"When you want the truth, you get ruthless.\""
            show sam annoyed -talking with dis
            "I feel grateful that the music in the barn is too loud for much of anybody to hear what they’re saying."
            wi "\"Fair.\""
            wi "\"Be that as is it may...\""
            show nik sidelook with dis3
            wi "\"Nik told me what he did out of concern for you.\""
            wi "\"So why don’t you turn around, look him in the eye, shake his hand, and tell him {i}‘thank you’{/i}.\""
            show sam eyes talking with dis
            m "\"Can’t.\""
            show sam eyes -talking with dis1
            show sam eyes talking with dis
            m "\"His eyes go dopey when he’s mad.\""
            show sam eyes -talking with dis3
            show nik disappointed with dis3
            ni "\"No they do not!\""
            "I’m not gonna remark on the validity of that claim."
            show nik neutral with dis3
            show sam annoyed -talking with dis3
            wi "\"Sam.\""
            show sam annoyed talking with dis
            m "\"Will.\""
            show sam annoyed -talking with dis
            "I take a deep chug of my mug and then set it down."
            wi "\"Stop being such a pussy.\""
            "Sam’s claws retract around his mug and he scrapes the glass."
            show sam annoyed talking with dis
            m "\"Fine.\""
            show sam annoyed -talking with dis
            wi "\"Tell him thank you for caring about you.\""
            show sam eyes talking with dis
            m "\"Thank you for caring about me, Nik.\""
            show sam neutral -talking with dis
            "Nik is still staring."
            show sam surprised with dis
            show nik sad with dis3
            "Then his chest heaves with a sniff."
            "He makes a low, loud sound as tears well up around his eyes."
            show sam surprised talking with dis
            m "\"Don’t cry, Nik...\""
            show sam surprised -talking blush with dis
            "He looks around, cheeks flushed."
            show sam sad talking -blush with dis
            m "\"At least not here... not where people can...\""
            show sam sad -talking with dis
            "Tears well up in his eyes too."
            show nik sad at center with dis3
            "Nik wraps his big arms around Sam and holds him tight, both shuddering, making one another damp."
            show nik surprised with dis
            show sam surprised with dis
            "A group of drunks around us start to clap."
            show nik sidelook at centerright with dis3
            "They flinch, letting go of each other immediately and going back to their drinks."
            "The music picks up again and the drunk people begin to dance once more."
            #nikcont
            show nik sidelook with dis3
            "Nik wipes his eyes."
            ni "\"Perhaps it would be best to discuss this somewhere more private.\""
            show sam eyes with dis3
            "Sam wipes his eyes and {nw}"
            show sam annoyed with dis3
            extend "scowls as his ears go flat."
            m @talking "\You don’t say...\""
            show sam neutral with dis3
            show nik neutral with dis3
            wi "\"You know this place better than us, Nik.\""
            wi "\"Lead the way.\""
            #sfx
            show nik eyes with dis
            "Me and Nik stand while {nw}"
            show nik neutral with dis3
            show sam neutral at left,light1 with dis3:
                xzoom 1
            extend "Sam looks off into the corner."
            m @talking "\Think it’s wise to leave the deputy by himself?\""
            "I follow his gaze."
            "The deputy is holding a spoon with his mouth and an egg in it, twirling while a group of people, including Mr. Byrnes and Mr. Tibbits, clap for him."
            wi "\Let’s worry about one thing at a time.\""
            stop music fadeout 2.5
            play background ("sfx/crickets.ogg") fadein 2.5
            scene bg stagexteriornight with dis3
            "Nik walks us out of the barn and into the field with the small patches of fire."
            "We see shadows shuffling about, most going in and out of barns."
            scene bg stagtrailnight with dis3
            "But Nik takes us into a little copse of trees."
            scene bg stagforest with dis3
            play sound ("sfx/gravelwalk.ogg")
            "We walk about ten minutes through brush and come along to a big tree with splitting branches that covers the sandy floor with its canopy."
            show nik smile at right,night with dis3
            show sam neutral at left,night with dis3:
                xzoom-1
            ni "\"Good.\""
            stop sound
            ni "\"Thankfully nobody’s here tonight...\""
            "I cock my eyebrow."
            show nik neutral with dis
            wi "\"People frequent this tree?\""
            show nik eyestalking with dis
            ni "\It’s a useful shape.\""
            show nik neutral with dis
            play sound ("sfx/foreststep.ogg")
            "Sam steps between the v-shape in the trunks and feels up the bark."
            stop sound
            show sam smile with dis
            m "\"Good for bending over.\""
            "Nik ignores this."
            show nik talking with dis
            show sam neutral with dis
            ni "\"I meant as a landmark for leaving and picking up things.\""
            show nik -talking with dis1
            show nik talking with dis
            ni "\"Sometimes it draws a crowd during the day, but I have seen no one come here after dark.\""
            show nik -talking with dis
            wi "\"Right...\""
            wi "\"So do the both of you feel better now that you’ve spoken your piece?\""
            show sam eyes talking with dis
            m "\"I guess.\""
            show sam neutral -talking with dis
            show nik sad with dis3
            ni "\"I just want things to feel right between me and Sam again.\""
            #music
            show sam surprised with dis
            ni "\"At least before I move to Payton.\""
            "Me and Sam snap our attention to Nik."
            show nik sidelook with dis3
            show sam surprised talking with dis3
            m "\"You never told us that.\""
            show sam surprised -talking with dis
            wi "\"How soon?\""
            show nik disappointed with dis3
            "He holds his hips and sighs."
            ni "\"Less than a week.\""
            "This is sudden."
            show nik neutral with dis3
            wi "\"Really now?\""
            show sam annoyed talking with dis
            m "\"And to think you got mad at {i}me{/i} for withholding things.\""
            show sam surprised -talking with dis
            show nik surprised with dis3
            ni "\"I am not withholding it!\""
            show nik disappointed with dis3
            ni "\"My decision is recent.\""
            ni "\"A much better opportunity showed up for me and I will be taking it.\""
            #sfx
            show nik neutral with dis3
            "I think I hear the train for a moment but it’s just wind rustling through the leaves."
            show sam annoyed -talking with dis
            "Samuel tsks."
            show sam talking with dis
            m "\"{i}Payton{/i} though?\""
            show sam -talking with dis1
            show sam talking with dis
            #adjust
            m "\"Why the hell Payton of all places?\""
            show sam -talking with dis1
            show sam talking with dis
            m "\"If you’re just gonna go, then consider going farther.\""
            show sam neutral -talking with dis
            show nik talking with dis
            ni "\"Because it makes me easier to follow.\""
            show nik disappointed with dis3
            ni "\"I thought there might be a chance some of you might follow me there.\""
            show sam annoyed talking with dis
            m "\"Nik, that place is even more of a hellhole than here.\""
            show sam -talking with dis1
            show sam talking with dis
            m "\"They don’t even got electricity on the streets yet.\""
            show sam -talking with dis3
            show nik sidelook with dis3
            ni "\"I have faith that not only will they catch up to Echo’s amenities, but exceed them.\""
            show sam neutral -talking with dis
            ni "\"There is a steel mill and welder’s cooperative I have been asked to partake in.\""

            show nik neutral with dis3
            wi "\"Since when do you weld?\""
            show nik talking with dis
            ni "\"Since the moment they teach me to.\""
            show nik -talking with dis1
            show nik talking with dis
            ni "\"Skills can be learned.\""
            show nik -talking with dis1
            show nik talking with dis
            ni "\"My connections are more important than what I know.\""
            show nik sidelook with dis3
            ni "\"The working conditions and the low pay here are no longer feasible.\""
            #adjust
            "It’s hard for me to think of a time within the last two years where the three of us weren’t together."
            show nik neutral with dis3
            "Going on without Nik here is gonna be hard."
            show nik talking with dis
            ni "\"You both aren’t saying anything.\""
            show nik -talking with dis
            wi "\"What is there to say?\""
            wi "\"I respect the decision.\""
            wi "\"Sam doesn’t like it here either.\""
            show sam eyes talking with dis
            m "\"I like the both of you though.\""
            show sam neutral -talking with dis
            "I put my hands in my pockets and listen to the crickets chirp."
            wi "\"Ain’t that just the way of things, though?\""
            wi "\"Life is just a series of people coming and going.\""
            wi "\"People you hate just as much as the people you...\""
            "They both watch me carefully."

            if SW_Points>=4:
                wi "\"You know, we’re about as close as three men can be with one another, ain’t we?\""
                show nik blush with dis3
                "Nikolai blushes."
                "Sam looks like he’s thinking."
                show sam neutral talking with dis3
                show nik sidelook with dis3
                m "\"I want you to talk that out, William.\""
                show sam -talking with dis
                wi "\"Now, hold on a minute.\""
                show sam eyes talking with dis
                m "\"The crickets are still chirping.\""
                show sam neutral -talking with dis1
                show sam neutral talking with dis
                m "\"Nobody’s snuck up on us.\""
                show sam neutral -talking with dis
                "I grit my teeth a little to prevent an impromptu snarl."
                wi "\"You know what I meant.\""
                show sam eyes talking with dis
                m "\"But say it.\""
                show sam neutral -talking with dis
                wi "\"We’re connected through you Sam.\""
                wi "\"Through what we pay you for.\""
                wi "\"And how you take care of us when we need it.\""
                wi "\"I doubt we could function if we hadn’t’ve met you Sam.\""
                wi "\"There’s probably more honor in the work you do than me and Nik combined and I should have said it sooner.\""
                show sam smile with dis
                m "\"Heh.\""
                wi "\"Oh, fuck off with that expression.\""
                m "\"You’re just funny when you’re sentimental is all.\""
                "Now I feel like a fool."
                show sam eyes talking with dis
                m "\"I needed to hear you say this, though.\""
                show sam neutral -talking with dis1
                show sam neutral talking with dis
                m "\"Truth be told...\""
                show sam neutral -talking with dis1
                show sam neutral talking with dis
                m "\"I don’t much like that whoring is the only job I have enjoyed.\""
                show sam annoyed -talking with dis1
                show sam annoyed talking with dis
                m "\"Don’t much like that I’m a faggot, neither.\""
                show sam annoyed -talking with dis
                "He spits on the ground."
                show sam annoyed talking with dis
                m "\"Makes me feel like it’s the only thing I’m good for.\""
                show sam eyes -talking with dis1
                show sam eyes talking with dis
                m "\"But I accepted that a long time ago.\""
                show sam neutral -talking with dis1
                show sam neutral talking with dis3
                show nik blush with dis3
                m "\"And you’re the only two who give me purpose outside of the work.\""
                show sam neutral -talking with dis1
                show sam neutral talking with dis
                m "\"So I don’t really want to lose that either.\""
                show sam neutral -talking with dis
                "He puts his hands in his pockets and looks at me."
                show nik sidelook with dis3
                show sam neutral talking with dis3
                m "\"So if I keep helping you wrap up this big investigation that you’re working on, Will, can the three of us get out of here together once it’s finished?\""
                show sam neutral -talking with dis
                "I stare at him."
                show nik neutral with dis3
                wi "\"What, to Payton?\""
                show sam neutral talking with dis
                m "\"Yeah, to Payton.\""
                show sam annoyed -talking with dis1
                show sam annoyed talking with dis
                m "\"I guess.\""
                show sam neutral -talking with dis1
                show sam neutral talking with dis
                m "\"If that’s what Nik really thinks would be best.\""
                show sam neutral -talking with dis1
                "We look to him and wait for him to speak."
                show nik disappointed with dis3
                ni "\"Yes.\""
                ni "\"It is the only way forward.\""
                show nik neutral with dis3
                show sam annoyed -talking with dis3
                "Sam spits again."
                show sam annoyed talking with dis
                m "\"Then I’ll go to fuckin’ Payton.\""
                show sam eyes -talking with dis1
                show sam eyes talking with dis
                m "\"Will you resign and come with us, Will?\""
                show sam neutral -talking with dis
                "This is one of the craziest things I’ve ever heard."
                "And what’s crazier now is how much I’m considering it after everything that’s happened."
                wi "\"It’ll be a lot harder for me to protect you anywhere else, Sam.\""
                wi "\"Is that what you really want?\""
                show sam eyes -talking with dis
                "He shrugs."
                show sam neutral talking with dis
                m "\"If there really is something bad in store for me, it might be because it’s meant to happen.\""
                show sam annoyed -talking with dis1
                show sam annoyed talking with dis
                m "\"But why should we waste any of the time we might have on people who couldn’t care less if we were all dead?\""
                show sam annoyed -talking with dis1
                show sam annoyed talking with dis
                m "\"Echo will still go on without us.\""
                show sam eyes -talking with dis1
                show sam eyes talking with dis
                m "\"And if it doesn’t, then, well...\""
                show sam annoyed -talking with dis1
                show sam annoyed talking with dis
                m "\"Maybe it don’t have any right to exist.\""
                show sam neutral -talking with dis
                "I sigh."
                wi "\"Alright.\""
                wi "\"If I can blow the lid off the connection between the CGSC’s operations and the murders in town, and make it public, then that’s the best that I can do for these people.\""
                wi "\"I’ll resign and go with you both.\""
                wi "\"Does that sit right with you, Nik?\""
                show nik smile with dis
                ni "\"Honestly?\""
                show nik eyessmile with dis
                ni "\"It’s the best thing I could have hoped for.\""
                #adjust
                show nik sad with dis3
                ni "\"I know that I could start a life again without the two of you, only with the help from my connections at CGCS who are leaving too.\""
                ni "\"But I still don’t want to.\""
                show nik talking with dis3
                ni "\"I do not think the connection that we share could be found again, even in many, many lifetimes.\""
                show nik neutral with dis
                wi "\"So that’s that, then.\""
                wi "\"You have our word, Sam.\""
                show sam annoyed with dis
                "The puma frowns."
                show sam annoyed talking with dis
                m "\"People give me their word all the time.\""
                show sam neutral -talking with dis1
                show sam neutral talking with dis
                m "\"Actions speak louder than words, Will.\""
                show sam neutral -talking with dis
                wi "\"Then what will convince you?\""
                show sam neutral talking with dis
                m "\"Well...\""
                show sam eyes -talking with dis
                pause 1.0
                show sam annoyed talking with dis
                m "\"Actually, forget it.\""
                show sam neutral -talking with dis
                show nik surprised with dis
                "Nik and I tense up a bit."
                show nik sidelook with dis3
                ni "\"No, Sam, we want you to speak up.\""
                show sam eyes talking with dis
                m "\"It’s stupid.\""
                show sam annoyed -talking with dis
                wi "\"Since when has that ever stopped you from sharing?\""
                play sound ("sfx/thud.ogg")
                show nik neutral
                "Nik elbows me and I feel a little bit of wind knocked out of me." with hpunch
                stop sound
                show sam annoyed talking with dis
                m "\"Fine.\""
                show sam eyes -talking with dis1
                show sam eyes talking with dis
                m "\"Don’t say I didn’t warn you...\""
                show sam neutral -talking with dis1
                show sam neutral talking with dis
                m "\"If y’all promise that we’re going to share everything, then I mean I want y’all to share {i}everything{/i}.\""
                show sam neutral -talking with dis1
                show sam neutral talking with dis
                show nik surprised with dis
                m "\"I’m never going to feel equal to the both of you if we don’t sleep together regularly without any money being exchanged.\""
                show sam neutral -talking with dis
                "Nik and I share an incredulous look."
                ni"\"Do you mean...\""
                ni "\"At the same time?\""
                show sam neutral talking with dis
                m "\"The three of us. Yeah.\""
                show sam neutral -talking with dis1
                show sam neutral talking with dis
                m "\"And I want you both to put a dick in your mouth.\""
                show sam eyes -talking with dis1
                show sam eyes talking with dis
                m "\"I don’t particularly care who.\""
                show sam neutral -talking with dis
                wi "\"Christ almighty, Sam...\""
                show sam annoyed -talking with dis
                m "\"Will.\""
                show sam neutral -talking with dis1
                show sam neutral talking with dis
                m "\"You told me you still think about it.\""
                show sam neutral -talking with dis3
                show nik disappointed with dis3
                ni "\"Sam...\""
                ni "\"If William told you this in confidence, then you shouldn’t be telling me.\""
                show nik sidelook with dis3
                ni "\"But I must confess...\""
                ni "\"It feels less lonely knowing that even somebody like William has these thoughts.\""
                ni "\"It makes me wonder how many of us there are who do but never really say it.\""
                show nik talking with dis3
                ni "\"Is it the truth, William?\""
                show nik neutral with dis3
                "I can feel the sweat on the back of my neck."
                "I can’t say much."
                "But I have to say somethin’."

                menu swn:
                    "Tell Nikolai the truth?"
                    "Yes." if SW_Points>=5:
                        $ SWNChoice=True
                        wi "\"Yeah.\""
                        #adjust
                        "Nik is still just as tense as I am."
                        show sam neutral talking with dis
                        m "\"I’m sorry I spilled the beans, William.\""
                        show sam sad -talking with dis1
                        show sam sad talking with dis
                        m "\"But I don’t want to feel like Sam the whore tonight.\""
                        show sam eyes -talking with dis1
                        show sam eyes talking with dis
                        m "\"I want to feel like Sam, your friend.\""
                        show sam neutral -talking with dis1
                        show sam neutral talking with dis
                        m "\"I want y’all to do for me what I’ve done hundreds of times for y’all.\""
                        show sam neutral -talking with dis
                        wi "\"So just, suck a cock.\""
                        show sam neutral talking with dis
                        m "\"Yeah.\""
                        show sam neutral -talking with dis
                        wi "\"Anybody’s cock?\""
                        show sam eyes talking with dis
                        m "\"Mine or Nik’s.\""
                        show sam neutral -talking with dis
                        show nik surprised with dis
                        "Nik looks a little more skittish."
                        ni "\"And you’d like me to do it too, yes?\""
                        show sam annoyed talking with dis
                        m "\"None of you {i}have{/i} to do shit.\""
                        show sam eyes -talking with dis1
                        show sam eyes talking with dis
                        m "\"By all means don’t if you don’t want to.\""
                        show sam annoyed talking with dis3
                        show nik blush with dis3
                        m "\"I told y’all that it was stupid.\""
                        play sound ("sfx/foreststep.ogg")
                        show sam surprised -talking with dis3
                        show nik blush with dis3:
                            ypos 1.23
                        "Nik suddenly kneels."
                        show sam surprised -talking blush with dis3
                        ni "\"Ok.\""
                        ni "\"I’ll try you both, then.\""
                        "My heart jolts."
                        wi "\"Nik he said we didn’t {i}have{/i} to.\""
                        show nik flustered with dis3
                        ni "\"And who says I didn’t {i}want{/i} to?\""
                        ni "\"I understand how Sam might feel since he’s the one who always does this.\""
                        show nik blush with dis3
                        ni "\"And like I have said.\""
                        ni "\"I have had the thought to do so before.\""
                        show sam surprised talking with dis
                        m "\"...What?\""
                        show sam surprised -talking with dis3
                        show nik flustered with dis3
                        ni "\"Please do not make me repeat what I said.\""
                        show sam surprised talking with dis
                        m "\"Okay, but...\""
                        show sam surprised -talking with dis1
                        show sam surprised talking with dis
                        m "\"I said the thought was dumb.\""
                        show sam surprised -talking with dis1
                        show sam surprised talking with dis
                        m "\"And you'd never ask before to try--\""
                        show sam surprised blush -talking with dis
                        show nik blush with dis3
                        ni "\"Take off your pants, Sam.\""
                        hide sam
                        hide nik
                        with dis2
                        pause 0.5
                        #adjust
                        play sound ("sfx/belt.ogg")
                        queue sound ("sfx/zipper.ogg")
                        "I hear the snap of his buttons and the tug of his zipper."
                        "He’s fishing himself out, thick and pink as ever as he scoots up to kneeling Nik."
                        stop sound
                        ni "\"How should I start?\""
                        m "\"Just a lick will do.\""
                        "He leans in."
                        "Hesitates."
                        "Then he opens his mouth, and drags his tongue and the top of his fuzzy snout along Sam’s prick."
                        "It’s strange to see Nik do this to Sam, even knowing he always has been Sam's client."
                        "And it’s suddenly very hard to ignore the growing tent in his pants that shows me just how big every part of him really is."
                        "Nik licks again."
                        "Then again."
                        "And a fourth time which makes Sam begin to purr."
                        ni "\"Should I do this until you finish?\""
                        m "\"No.\""
                        m "\"I don’t need to.\""
                        m "\"But if you keep that up, I will anyway.\""
                        ni "\"It is not a bad taste at all...\""
                        ni "\"Very clean.\""
                        "The badger gives me a look as he keeps licking."
                        ni "\"You next then?\""
                        "I feel that twang of panic again."
                        wi "\"Do you {i}really{/i} want to lick my prick, Nikolai?\""
                        ni "\"It would be a good idea.\""
                        ni "\"That is, if you will be trying mine.\""
                        "I look at his pants again."
                        "Just from the outline it’s hard to believe he could fit something like that down there."
                        "I look away, feeling my ears get hot."
                        "I undo the buttons in my pants."
                        "And I slip it out."
                        "I feel his wet nose before the warm tongue."
                        "The lick is strong and firm."
                        "A much wider tongue than Sam’s."
                        "He pauses after the first lick."
                        ni "\"Eugh.\""
                        wi "\"...what?\""
                        ni "\"You’re already sticky...\""
                        ni "\"Samuel took much longer.\""
                        wi "\"Yeah.\""
                        wi "\"That happens pretty quickly for me.\""
                        wi "\"Sorry.\""
                        "The badger pauses."
                        "I expect him to ask to stop, but then he goes down again."
                        "Firmer. Stronger."
                        "Feels... really good."
                        ni "\"You’re much saltier than Sam.\""
                        ni "\"Perhaps that is why your temper is so quick...\""
                        wi "\"...Excuse me?\""
                        "He goes down on me again, slurping this time."
                        wi "\"...Shit.\""
                        "I’m already at full mast."
                        "It’s hard to believe he’s never done this before."
                        "Or maybe he just understands what feels good naturally."
                        "He scoops his tongue against the side of me, tongue rolling, and then pulls away with a smack."
                        ni "\"Do you think this is strange?\""
                        "I nod emphatically."
                        wi "\"Oh yeah.\""
                        ni "\"Hmm.\""
                        "He dips down to my balls, getting them in his mouth, suckling them."
                        "Then he pulls away."
                        ni "\"If Sam is used to being the only one who does this, then I don’t.\""
                        "He pulls back and stands up slowly."
                        "It’s impossible to disregard the thick flag pole in his trousers."
                        play sound ("sfx/belt.ogg")
                        "He undoes the notches of his belt, fumbling with the clip as it comes loose, allowing himself free."
                        stop sound
                        "The strong smell of earth is all I notice as he slips his manhood out of the side of the fabric."
                        ni "\"So...\""
                        ni "\"What is the best way to go about this, then?\""
                        "The cougar steps forward, his shaft bobbing as he approaches me from the other side of Nik."
                        "Sam is longer, but not nearly as thick."
                        m "\"It’ll be more fun for all of us if we take turns.\""
                        m "\"If one of us actually does finish first, the mood flies away.\""
                        "I watch them both, throbbing."
                        "I look to the left."
                        "Then I look to the right."
                        "I expect to see the glare of eyes, but there’s really nobody."
                        "The crickets are still chirping."
                        m "\"Who do you want to try first, Will.\""
                        "I cringe."
                        wi "\"I don’t think that much matters, Sam.\""
                        "Sam pipes up first."
                        m "\"I think you owe me most, but I want to see you try and take Nik.\""
                        "I look at the big badger’s piece skeptically."
                        wi "\"You saying that anybody can?\""
                        "Nikolai is blushing even harder."
                        ni "\"Sam usually uses both hands.\""
                        play sound ("sfx/foreststep.ogg")
                        "Sam puts his hands on my shoulders to get me down on my knees{nw}"
                        scene wilcg10a with dis4
                        extend " and Nik walks up."
                        stop sound
                        "I dip my head in to give him a sniff first."
                        "He’s..."
                        "Sweaty."
                        "Real sweaty."
                        "I close my eyes and stick out my tongue."
                        scene wilcg10b with dis3
                        "Bringing myself in closer to lick."
                        "This is my friend."
                        "Just my good friend."
                        stop background fadeout 5.0
                        scene bg black with dis3
                        "Just like Aiden."
                        "The other cocksucker."
                        "The voice in my head sounds like my father."
                        play sound ("sfx/punch1.ogg") volume 0.1
                        "Then I hear the punches."
                        play sound ("sfx/bottlesmash1.ogg") volume 0.1
                        "The window smash."
                        "Blood."
                        stop sound
                        scene wilcg10b with dis3
                        play background ("sfx/crickets.ogg") fadein 1.0
                        "I dip my head in and focus on my friend again."
                        "He’s damp and warm and I lick him strategically."
                        "Once right, once left, once where the balls connect to the shaft to the tip."
                        "Then I take as much as I can of him in."
                        ni "\"Will?\""
                        "I look up at him."
                        wi "\"Mmm?\""
                        ni "\"You feel very nice.\""
                        "Heat surges through my cheeks as I ignore the praise."
                        "I keep up with my task."
                        ni "\"Oh, um.\""
                        ni "\"Oh wow.\""
                        "Nik moans at first."
                        "Then he starts to growl."
                        scene wilcg10b with dis4
                        "He brings his hands down on my head."
                        "His gentle touch turns into a vice grip."
                        "It actually hurts a bit."
                        "And I don’t want to tell him to stop because it’s making me harder."
                        m "\"Nik, your grip.\""
                        "There’s immediately a release of claws and my scalp tingles."
                        scene bg stagforest with dis3
                        "The badger’s cock pulls out of me, leaving a puddle of spit and pre on the dirt floor."
                        "I grunt a little in relief, but also in disappointment."
                        ni "\"Sorry.\""
                        ni "\"I got carried away.\""
                        wi "\"It was fine.\""
                        wi "\"Wasn’t like I was bleedin’ or nothin’.\""
                        m "\"Not much more power and you could have been.\""
                        m "\"Trust me.\""
                        wi "\"I’m just saying that I wouldn’t much mind that either so long as it’s not killin’ me.\""
                        "I close my eyes and bump my nose against him."
                        "The first thing that I notice is he’s as drippy as I am by the way it clings to my nose."
                        "The second thing I notice is the beer on Nik’s breath."
                        "I skip the lick and just put it all in my mouth at once."
                        m "\"...Goddamn.\""
                        "I swirl my tongue."
                        "I flex my tongue."
                        "I repeat all the little tricks and wishes I’d whisper into Sam’s ear when I was getting close."
                        "My head is dizzy and swimming with the amount of effort I put in."
                        "I start to bob, churning off and on him, determined to make something happen."
                        "He chuckles and pushes me off."
                        m "\"Holy shit, slow down.\""
                        "I heave, catching my breath."
                        m "\"Fuck.\""
                        "I wipe my mouth."
                        "We’re all panting, and dripping, and sticky."
                        wi "\"How do we plan on finishing this then?\""
                        m "\"Well, I’ve only done this once...\""
                        m "\"We’re gonna lie in a circle.\""
                        m "\"Heads between each other’s knees.\""
                        m "\"Will between mine, Nik between Will’s, I between Nik's.\""
                        m "\"Mostly we get each other as close as we can before finishing.\""
                        m "\"Then when we can’t control it anymore, just gently squeeze the shaft, like this.\""
                        "He cups his paw and grasps the air, flexing open and closed."
                        m "\"If it works out we’ll all finish at the same time.\""
                        m "\"Y’all ready?\""
                        "Nik nods."
                        scene wilcg11 with dis4
                        "I just scoot close to Sam who’s lying on a patch of dirt, put my head between his legs, and slip his warm, thick shaft into my mouth."
                        "I feel Nik’s massive maw slide between my legs, and his firm licks wash over me again, getting me to shiver."
                        "The sweat of Sam’s balls still commingles with Nik’s breath."
                        "We all sweat as we move together-- thrusting, bobbing, slurping."
                        "Until I feel the squeeze on my dick from Nik’s massive, clumsy claw."
                        "I feel his whole body shake as he shouts into my groin."
                        "I can hear his splatters, which are shockingly loud, and I suddenly understand that Sam was letting me off easy."
                        "A sudden chemical smell fills the air. And like a chain reaction, Samuel’s legs begin to shake."
                        "The thick shots of his murky spunk on my tongue make me swallow, as if by instinct, and the rest of my body follows suit."
                        "I lift my arms, smelling the sickly sweet arousal on my body as I grasp his spurting dick to let him know that I’m about to lose control."
                        "The tightness in my balls draws tighter and tighter as Nik’s mouth swallows as much of me as he can."
                        "And I feel myself start to cum, shooting inside of my best friend, as the whore we’ve both fucked in a way that neither of us can ever deny again."
                        scene bg black with dis2
                        "I think I love these men."
                        "No, as I hold Sam’s waist and Nik holds mine, I know I love these men."
                        "I decide right here and now that we’ll either die together or survive together."
                        "Nobody’s getting left behind."
                        pause 2.5
                        #ncont
                        "I start to breathe deep, and slow."
                        "Then gasp."
                        scene bg stagforest with dis3
                        "I hadn't realized we had fallen asleep."
                        "It's Sam who has woken me."
                        show sam surprised at left,night with dis3:
                            xzoom-1
                        "He's shaking my arm."
                        show nik disappointed at right,night with dis3
                        "Sam is shaking Nik too, who wakes up with a roar."
                        show nik neutral with dis3
                        show sam surprised talking with dis3
                        m "\"Do you see it?\""
                        show sam surprised -talking with dis
                        "He's asking both of us."
                        show nik sidelook with dis3
                        ni "\"See what?\""
                        "Nik is looking in between the V of the trees."
                        "I look too, and there's nothing there."
                        show sam sad -talking with dis
                        "Sam's wide eyes start to droop."
                        show nik neutral with dis3
                        show sam sad talking with dis3
                        m "\"I meant that the moon is higher than it oughta be.\""
                        show sam sad -talking with dis
                        "Considerin' the moon isn't in the place he was looking, I doubt that's what he meant."
                        "But if he had a night terror I'm not going to press him on it."
                        show sam eyes talking with dis
                        m "\"We shouldn't be sleepin' outside like this.\""
                        show sam sad -talking with dis
                        "That's something he's right about."
                        "If somebody stumbles upon us with our shirts off and our drawers unbuttoned covered in spit and god knows what else..."
                        "Well it would be bad."
                        jump postswn

                    "No.":
                        $ SWNChoice= False
                        wi "\"It’s not exactly like that.\""
                        wi "\"Sam shouldn’t have brought it up.\""
                        show sam neutral talking with dis
                        m "\"Know what?\""
                        show sam eyes -talking with dis1
                        show sam eyes talking with dis
                        m "\"You’re right.\""
                        show sam neutral -talking with dis1
                        show sam neutral talking with dis
                        m "\"I overstepped.\""
                        show sam neutral -talking with dis
                        wi "\"Maybe just a little.\""
                        show sam annoyed with dis
                        "He grimaces and I see a fang."
                        "I’m not in the mood to entertain his attitude tonight."
                        jump swndecline

            else:
                label swndecline:
                wi "\"Well...\""
                wi "\"Like I was saying before: people come and people go.\""
                wi "\"We have much say in a man’s or woman’s life when they make up their minds and feel compelled to do something.\""
                show nik sidelook with dis3
                ni "\"So that’s it then?\""
                ni "\"You’re both fine with me leaving?\""
                show nik neutral with dis3
                show sam annoyed talking with dis3
                m "\"Fine ain’t the right word.\""
                show sam annoyed -talking with dis
                wi "\"Fine’s a plenty good word.\""
                show sam neutral -talking with dis
                wi "\"If things are better for Nik in Payton, then they’re better for Nik in Payton.\""
                wi "\"That’s just how things shake out sometimes.\""
                wi "\"And we’re not that far away if we need to visit.\""
                wi "\"Just half an hour by train, ain’t it Nik?\""
                show nik disappointed with dis3
                ni "\"True.\""
                ni "\"Perhaps you will both join me there soon.\""
                ni "\"I cannot imagine things running very well for much longer here.\""
                ni "\"Too many things are going to break.\""
                show nik neutral with dis3
                "I sigh and shake my head."
                wi "\"That’s true, but I’ve gotta help them clean up their mess.\""
                "I see the muscle in Nik’s lips pull back."
                show nik talking with dis3
                ni "\"But why does it have to be your mess?\""
                show nik -talking with dis1
                show nik talking with dis
                ni "\"You can just resign.\""
                show nik -talking with dis1
                show nik talking with dis
                ni "\"No job is worth that much trouble.\""
                show nik -talking with dis
                wi "\"Not for the guilty, no.\""
                "I stick my paws in my pockets and sigh."
                wi "\"But I owe the Madam a favor or two.\""
                wi "\"I just needed someplace to be for a while.\""
                wi "\"Maybe that time is just about up.\""
                wi "\"But the least I’m gonna do before makin’ myself scarce is solve the connection between the murders in town and the CSCG operations.\""
                show nik sad with dis3
                show sam annoyed -talking with dis3
                "Sam scoffs while Nik rubs his eyes and nods."
                show sam neutral -talking with dis
                ni "\"Then that is the way things have to be.\""
                ni "\"I hope you will remember my offer once things are finished here.\""
                "I shake my head and pull out a cigarette."
                show nik neutral with dis3
                wi "\"No Nik, I won’t forget.\""
                #sfx
                "I flick my lighter and let the flames lick the paper."
                "Then I inhale."
                "Exhale."
                "And feel calm."
                wi "\"It’s been a long night.\""
                wi "\"Sam and I have places to be tomorrow.\""
                show sam neutral talking with dis
                m "\"Marcy’s again?\""
                show sam neutral -talking with dis
                "I nod."
                wi "\"That’s the one.\""
                wi "\"Let’s go wrangle up Todd and call it a night.\""
                show sam neutral talking with dis
                m "\"You think we’ll have to peel him off the floor?\""
                show sam neutral -talking with dis
                wi "\"He doesn’t drink, Sam.\""
                show sam eyes talking with dis
                m "\"Doesn’t mean he won’t be stuck to something.\""
                show sam neutral -talking with dis
                "I cringe a bit."
                show nik talking with dis
                ni "\"I will go off on my own way, then.\""
                show nik -talking with dis1
                show nik talking with dis
                ni "\"I will make sure to see each of you again before I go.\""
                show nik -talking with dis
                "He holds out his huge, warm paw that almost entirely envelops mine as he shakes it."
                show nik eyes at center with dis3
                show sam surprised with dis3
                "Then pulls Sam into a tight hug."
                "The puma flinches at first."
                show sam eyes with dis
                "Then he leans into it."
                hide sam
                hide nik
                with dis3
                "I give them some space, finishing my cigarette and flicking out the ashes."
                label postswn:
                scene bg stagexteriornight with dis3
                "The journey back to the barn goes without incident."
                "We find Todd passed out on the rafters."
                "Sam bats at his cheeks to wake him up, and we walk him back into town."
                scene bg echoroadnight with dis3
                "Todd goes his way and Sam spends the night with me again, but we’re both too sore and tired to do much of anything else."
                stop background fadeout 3.0
                scene bg black with slow_dissolve
                jump marcymerge







#1
label marcymerge:
scene bg black with dissolve
scene bg greenecottage with dissolve
play music ("music/contemplation.ogg") fadein 3.0
#kane diff
if KaneChoice == True:
    "Even without my watch, I can tell we've arrived at the cottage sometime after two PM and before sundown."
else:
    "It's ten past five PM there, so ten past three PM here when we arrive at Marcy's cottage."
"Marcy’s adorable little cottage looks far less adorable each time I see it."
"Gone are those windowsill pies cooling in the sun and the evidence of bustling activity in the yard and on the porch."
"The house feels less like space for somebody to eat and sleep in so much as a replica of a house."
"Dolls line the outside steps."
"Potted plants that used to contain live succulents now have knitted replicas."
"All things on the stoop look untouched, but also unmaintained."
show sam at left:
    xzoom-1
if KaneChoice == True:
    show tod annoyed a at right
else:
    show tod annoyed at right
with dis3
"I can tell she’s home only from the open windows."
wi "\"Marcy?\""
"I don’t get an answer."
wi "\"Marcy, it’s Sheriff Adler.\""
wi "\"Please open up, I need to ask you some questions.\""
"She doesn’t respond."
if KaneChoice == True:
    show tod sigh a at right
else:
    show tod sigh at right
with dis3
to "\"We’re sorry to bother ya, Marcy but this’ll be the last time, swear on my grandpa Emmet’s grave.\""
if KaneChoice == True:
    show tod annoyed a at right
else:
    show tod annoyed at right
with dis3
"It sounds like she isn’t going to respond."
"But then we hear her voice."
if KaneChoice == True:
    show tod surprised a at right
else:
    show tod surprised at right
with dis
mar "\"{cps=20}Just go away.\""
"Todd gives me a worried look."
"I stick my head through the window."
wi "\"You don’t sound well, Marcy.\""
wi "\"We can help you if you need it.\""
show sam surprised with dis
"She makes a high pitched groan and then a screech."
mar "\"{cps=20}I said...\""
mar "\"...go!\"" with vpunch
"Todd gives me a look as if he’s asking me what to do."
"I clear my voice and begin to ask her again."
"But I never get the chance to."
play music ("music/horrorpiano.ogg") fadeout 2.0 fadein 2.0
play sound ("sfx/wsplash.ogg")
"From within, we hear something splash onto the floor."
"We hear Marcy Greene inhale, ragged and slow, until she lets out a shriek that goes well beyond the boundaries of her property, into Lake Emma."
"I can’t tell if she’s screaming at us or from pain."
wi "\"Ayers!\""
wi "\"Bronson!\""
wi "\"Help me bust this door down {i}right now{/i}!\""
show sam neutral with dis
if KaneChoice == True:
    show tod annoyed a at right
else:
    show tod annoyed at right
with dis
"Nobody hesitates."
hide sam
hide tod
with dis3
"I place my body on the door and Todd and Sam flank me."
wi "\"SLAM IT ON THE COUNT OF THREE.\""
wi "\"ONE...\""
wi "\"TWO...\""
"We hear another horrible scream."
wi "\"THREE!\""
play sound ("sfx/thud7.ogg")
"I can feel something knock loose from our combined body weight, but it’s not enough."  with vpunch
"There’s another splash."
wi "\"AGAIN!\""
"Then a gurgle."
wi "\"ONE...\""
#sfx
"The scraping sound of metal on wood."
wi "\"TWO...\""
"A toppling sound."
wi "\"THREE!\""
play sound ("sfx/doorburst.ogg")
"The wooden slot gives this time and the door busts open." with vpunch
scene bg greenecottageinterior dark with dissolve
show mar eyes at center,house1 with dis3
"Marcy is squatting in a pail in front of the fireplace."
"Tears are streaming down her face."
"Blood is running down her legs."
"Marcy crouches, squeezes her eyes shut, looks skyward into the ceiling, and yowls."
"Birds in the trees outside above us caw as they disperse."
show sam surprised at left,house1 with dis3:
    xzoom-1
if KaneChoice == True:
    show tod surprised a at right,house1 with dis3
else:
    show tod surprised at right,house1 with dis3
to "\"M-ma’am...\""
to "\"Are you okay?!\""
"Sam looks at Todd as if he can’t believe he just asked that, and he looks at me in a daze."
play sound ("sfx/thud3.ogg")
hide mar with dis3
"She cries out, sinking to the ground on her knees as a pool of something dark overflows from the pail below her."
show sam surprised talking with dis
m "\"Oh, shit!\"" with vpunch
show sam surprised -talking with dis3
if KaneChoice == True:
    show tod sad a with dis3
else:
    show tod sad with dis3
to "\"That’s...\""
"Sounds like they both just realized right now what’s happening."
show sam surprised talking with dis
m "\"She’s in labor!\""
show sam surprised -talking with dis3
if KaneChoice == True:
    show tod surprised a with dis3
else:
    show tod surprised with dis3
to "\"The heck you mean she’s in labor?!\""
show sam surprised talking with dis
m "\"I don’t think I fuckin' stuttered!\""
show sam surprised -talking with dis
"A slew of curse words fly out of my mouth."
"I should have known from the medicine this might not have happened yet."
wi "\"You ever delivered an infant, Todd?\""
to "\"Not a person’s, no!\""
wi "\"Well, it ain't much different.\""
wi "\"Go to the cupboard and get her a clean sheet.\""
if KaneChoice == True:
    show tod sad a with dis3
else:
    show tod sad with dis3
to "\"I, uh, um... ok!\""
hide tod with dis3
"He runs a little stiffly as his thick tail trots behind him."
play sound ("sfx/rummage1.ogg")
"We hear him slide and run into some cupboards as a few boxes topple."
stop sound
"I hold Mrs. Greene."
"She’s shaking something fierce."
wi "\"Deep breaths, M-ma’am...\""
wi "\"Help me move her, Sam.\""
"She’s leaving thin, splattery trails as we get her out of the kettle."
"I try to get her onto the floor, onto a flat surface, but the coppery smell of blood is cloying."

"Sam elevates her head with a pillow."
show sam surprised talking with dis
m "\"Do you have a midwife?\""
show sam surprised -talking with dis3
"She looks at him, like she’s lost, and shakes her head and starts crying again."
if KaneChoice == True:
    show tod surprised a at right,house1 with dis3
else:
    show tod surprised at right,house1 with dis3
"I hear Todd’s footsteps as he races back into the room with what looks like a tablecloth."
wi "\"We have to get these off of her.\""
if KaneChoice == True:
    show tod sigh a at right,house1 with dis3
else:
    show tod sigh at right,house1 with dis3
to "\"C-can we d-do that, m-ma’am...?\""
"She nods, still shaking."
if KaneChoice == True:
    show tod annoyed a at right,house1 with dis3
else:
    show tod annoyed at right,house1 with dis3
"Todd looks at me like I’m the one who needs to do it."
if KaneChoice == True:
    show tod surprised a at right,house1 with dis
else:
    show tod surprised at right,house1 with dis
show sam annoyed -talking with dis
"Sam shakes his head and jerks it towards her, giving Todd the hardest stare I’ve seen him give in his life."
if KaneChoice == True:
    show tod sad a with dis3
else:
    show tod sad with dis3
to "\"Okay.\""
if KaneChoice == True:
    show tod sigh a with dis
else:
    show tod sigh with dis
to "\"Alright.\""
hide tod with dis3
show sam eyes with dis
"Todd crouches, grimacing from the smell as he puts his paws below."
show sam surprised  with dis
"I hear the undergarments squelch as he pulls them down, sticking slightly to the skin."
"I can tell from the streaks on the side of her leg she has an infection."
wi "\"Don’t try to push too hard.\""
if KaneChoice == True:
    show tod surprised a at right,house1 with dis3
else:
    show tod surprised at right,house1 with dis3
"She shakes her head, tears still welling out of her eyes."
if KaneChoice == True:
    show tod talking a with dis
else:
    show tod talking with dis
to "\"It’s okay Mrs. Greene!\""
if KaneChoice == True:
    show tod eyes happy a with dis
else:
    show tod eyes happy with dis
to "\"You’re gonna be a mommy!\""
if KaneChoice == True:
    show tod surprised a with dis
else:
    show tod surprised with dis
"The rat starts wailing again."
play sound ("sfx/wsplash.ogg")
"More blood splashes to the ground."
if KaneChoice == True:
    show tod eyes happy a with dis
else:
    show tod eyes happy with dis

to "\"I think I see a head!\""
if KaneChoice == True:
    show tod surprised a with dis
else:
    show tod surprised with dis
"Mrs. Greene screams again."
if KaneChoice == True:
    show tod talking a with dis
else:
    show tod talking with dis
to "\"I definitely see a head!\""
if KaneChoice == True:
    show tod a with dis
else:
    show tod with dis
"I hold her paw and she squeezes mine."
"Hattie did the same when she delivered Andy."
"Without any medicine I can’t imagine the pain that Mrs. Greene is going through."
if KaneChoice == True:
    show tod eyes happy a with dis
else:
    show tod eyes happy with dis
to "\"Now there’s a body!\""
if KaneChoice == True:
    show tod surprised a with dis
else:
    show tod surprised with dis
wi "\"Hold it while it comes out.\""
hide tod with dis3
to "\"I am, I am!\""
wi "\"Make sure the cord isn’t wrapped around its neck.\""
to "\"Is that not supposed to happen?\""
wi "\"The baby can get strangled on it if you’re not careful.\""
to "\"It’s sliding out pretty easy now.\""
scene bg black with dis3
"I can see it too."
"It’s bloody and hairless with chunks of pus coating the body, and encased in a thin film of mucus."
"But it’s small."
"Very small."
scene bg greenecottageinterior dark
show sam sad at left,house1:
    xzoom-1
with dis3
to "\"Do we need to cut the cord?\""
show sam eyes with dis3
wi "\"No need.\""

wi "\"It’s good to let the blood flow through the cord and the rest comes out later.\""
show sam eyes talking with dis
m "\"It usually detaches by itself.\""
show sam -eyes -talking with dis
to "\"How do you know that?\""
show sam sad talking with dis
m "\"Because it happens enough at work.\""
show sam sad -talking with dis3
if KaneChoice == True:
    show tod surprised a at right,house1 with dis3
else:
    show tod surprised at right,house1 with dis3
"I know he’s right."
"There aren’t any sounds."
"I feel my expression numb and Todd looks scared."
"Sam just covers his mouth, unable to look away from the scene of Mrs. Greene trembling while the sour-smelling thing attached by a fleshy cord below her legs doesn’t breathe."
"I hang my head, pinch my nose, and then look back to Sam."
if KaneChoice == True:
    show tod sad a with dis3
else:
    show tod sad with dis3
wi "\"We need to keep her awake.\""

wi "\"She’s lost a lot of blood.\""
mar "\"{cps=20}I knew they were dead.\""
mar "\"{cps=20}I knew it, I knew it, I knew it.\""
show sam sad talking with dis
m "\"You don’t have to worry about that now, Mrs. Greene.\""
show sam sad -talking with dis
mar "\"{cps=20}But it’s all my fault.\""
show sam eyes talking with dis
m "\"It’s not.\""
show sam sad -talking with dis1
show sam sad talking with dis
m "\"This thing happens all the time.\""
show sam sad -talking with dis1
show sam sad talking with dis
m "\"Trust me, I see it happen all the time.\""
show sam sad -talking with dis
mar "\"{cps=20}But it is though.\""
mar "\"{cps=20}If it would have lived, he would have taken it.\""
if KaneChoice == True:
    show tod surprised a with dis3
else:
    show tod surprised with dis3
show sam surprised with dis3
wi "\"...What?\""
mar "\"{cps=20}Taken it like he took me.\""
show sam surprised talking with dis
m "\"Mrs. Greene?!\""
show sam surprised -talking with dis
mar "\"{cps=20}If he was dead then I could have had this one.\""
mar "\"{cps=20}But now there won’t be another one.\""
mar "\"{cps=20}Forever again, for never again, for never again.\""
"Her eyelids flutter before they close."
show sam surprised talking with dis
m "\"Stay with me, Mrs. Greene.\""
show sam surprised -talking with dis
wi "\"Todd, go get her something to drink.\""
hide tod with dis3
wi "\"Sit with her and keep talking, Sam.\""
wi "\"I’m going to go boil some water.\""
scene bg greenekitchen with dis3
"I don’t look back at them when I stand up, feeling my tail sway behind me as it prickles."
"I see Sam shake her shoulder to try to wake her up again."
"There’s a big enough pot below her stove."
if KaneChoice == True:
    show tod surprised a at right,sunset with dis3
else:
    show tod surprised at right,sunset with dis3
"Todd knows exactly where the cups are."
if KaneChoice == True:
    show tod sigh a with dis3
else:
    show tod sigh with dis3
"He finds a large jug of water in a pantry and turns the knob to let it flow."
if KaneChoice == True:
    show tod annoyed a with dis3
else:
    show tod annoyed with dis3
play sound "sfx/tea.ogg"
"I turn on her sink and let the water begin to flow."
hide tod with dis3
"Todd runs out with the cup in his hand."
stop sound
"I’m surprised but thankful that she has a gas stove, so I don’t have to light a fire or stoke any coals to get started."
"I have to find a place where Marcy can lie down."
scene bg greenecottageinterior dark with dis3
"Her couch is so covered with these damn dolls that she has no place to sit."
"Upsetting her further will just add stress."
"I remove each and every one of those dolls from the couch and place them on the only surface left, which is the table."
show sam sad -talking at center,house1
if KaneChoice == True:
    show tod sad a at right,house1
else:
    show tod sad at right,house1
show mar eyes at centerright,house1
with dis3
"Sam and Todd bring her in and she’s holding a pink-stained sheet, wrapped up in swaddle."
show sam neutral -talking with dis
wi "\"Here, here!\""
hide sam
hide tod
hide mar
show sam neutral -talking at left,house1:
    xzoom -1
if KaneChoice == True:
    show tod sad a at right,house1
else:
    show tod sad at right,house1
show mar eyes at center,house1
with dis3
"I direct them to the couch."
"Marcy is still dripping from the legs."
show mar eyes talking with dis
mar "\"{cps=20}Bedroom.\""
show mar with dis
wi "\"No Marcy, it’s not clean.\""
"She holds up the sheet."
show mar talking with dis
show sam surprised
if KaneChoice == True:
    show tod surprised a
else:
    show tod surprised
with dis
mar "\"{cps=20}I want to put her with the others.\""
show mar with dis
"With the others?!"
"Oh, God..."
show mar eyes
if KaneChoice == True:
    show tod sigh a
else:
    show tod sigh
with dissolve
hide tod with dis3
"Todd takes it for her and disappears into the bedroom."
show mar eyes talking with dis
mar "\"{cps=20}Thank you.\""
show mar eyes smile with dis3
mar "\"{cps=20}Always such a good boy.\""
show mar eyes with dis
show sam sad -talking with dis
"Sam leans into me, whispering in my ear."
show sam sad talking with dis
m "\"The afterbirth wasn’t whole when it came out.\""
show sam eyes -talking with dis
"I feel the ‘Fuck’ roll out of me like it’s a gasp."
show sam neutral -talking with dis
wi "\"Marcy, who’s your doctor?\""
show mar eyes talking with dis
mar "\"{cps=20}Medicine?\""
show mar dazed eyes with dis
mar "\"{cps=20}I’ve had my fill of medicine.\""
show mar eyes with dis
wi "\"We already know everything so there’s no need to hide anything from us anymore.\""
wi "\"You’re very sick, and you need help.\""
if KaneChoice == True:
    show tod surprised a at right,house1 with dis3
else:
    show tod surprised at right,house1 with dis3
with dis3
show mar with dis3
stop music fadeout 8.0
"Todd comes out of the room looking a little queasy."
to "\"I dragged the couch in there and kept her on it.\""
"Okay, that’s enough."
wi "\"Let’s talk in the kitchen.\""
"They both follow me."
hide sam
hide tod
with dissolve
scene bg greenekitchen at sunset with dissolve:
    zoom 1.03
    truecenter
if KaneChoice == True:
    show tod sad a at right,sunset
else:
    show tod sad at right,sunset
with dis3
show sam sad -talking at left,sunset:
    xzoom -1
with dis3
play music ("music/contemplation.ogg") fadein 5.0
wi "\"Okay, this is really bad.\""
show sam neutral -talking with dis
wi "\"Sam?\""
wi "\"Dora knows doctors, right?\""
show sam neutral talking with dis
m "\"People who are close enough, yeah.\""
show sam neutral -talking with dis
wi "\"Would she help in this case?\""
show sam neutral talking with dis
m "\"She would.\""
show sam neutral -talking with dis
wi "\"She’d respond better to you than she would to me.\""
show sam eyes talking with dis
m "\"...Right.\""
show sam -eyes -talking with dis1
show sam neutral talking with dis
m "\"I could go get help?\""
show sam neutral -talking with dis
wi "\"I think it would be a good idea to go fetch her.\""
wi "\"Be careful about who else you bring.\""
wi "\"If a licensed doctor saw any of this, it wouldn’t be good for her.\""
show sam neutral talking with dis
m "\"Yeah, okay.\""
show sam neutral -talking with dis1
hide sam with dissolve
"Sam gives Marcy another cautious look before disappearing out the front door."
scene bg greenecottageinterior dark
show mar dazed at center,house1
with dissolve
if KaneChoice == True:
    show tod sad a at right,house1
else:
    show tod sad at right,house1
with dis3
"Me and Todd head back to the living room."
"She’s staring up at the ceiling, holding her paw up, feeling one of the yarn streamers tacked to her walls, letting it slip through her digits, coiling them up."
wi "\"Marcy.\""
"She doesn’t respond to my voice."
wi "\"Mrs. Greene?\""
if KaneChoice == True:
    show tod sigh a with dis3
else:
    show tod sigh with dis3
to "\"Is it okay if we give you this?\""
if KaneChoice == True:
    show tod sad a with dis
else:
    show tod sad with dis
show mar smile with dis
"Her eyes widen as her mouth breaks into a smile."
mar "\"{cps=20}Penelope...\""
mar "\"{cps=20}I bet you thought I had forgotten all about you.\""
wi "\"Is Penelope the doll’s name?\""
show mar eyes smile with dis3
mar "\"{cps=20}No.\""
show mar smile with dis3
mar "\"{cps=20}That was my sister.\""
show mar eyes with dis3
mar "\"{cps=20}The doll is hers.\""
show mar with dis3
wi "\"Did she give it to you for safekeeping?\""
wi "\"It doesn’t look cheap.\""
show mar talking with dis3
mar "\"{cps=20}Because it wasn’t.\""
show mar with dis1
show mar talking with dis3
mar "\"{cps=20}I stole it because I was jealous.\""
show mar eyes with dis1
show mar eyes talking with dis3
mar "\"{cps=20}But I was going to give it back.\""
show mar eyes with dis1
show mar eyes talking with dis3
$ marcydolltext = "It used to belong to Marcy's sister."
$ current_journal_page = 21
$ renpy.notify("Notebook updated.")
mar "\"{cps=20}I just never got the chance to.\""
show mar eyes with dis3
"None of us dare ask why."
show mar with dis3
wi "\"Why do you think Mr. Greene had this locked in the cellar?\""
show mar talking with dis3
mar "\"{cps=20}Because he knew I wanted it.\""
show mar eyes with dis1
show mar eyes talking with dis3
mar "\"{cps=20}He’d know if I’d try to mess with the chains.\""
show mar with dis3
wi "\"But why would he put it down there?\""
show mar eyes talking with dis3
mar "\"{cps=20}Same reason he always did.\""
show mar eyes smile with dis3
mar "\"{cps=20}He knew little girls like dollies.\""
show mar smile with dis3
"She takes a look at the porcelain and gives it a kiss on the cheek."
show mar talking with dis3
mar "\"{cps=20}In the dark, and the quiet, it’s safe and warm.\""
show mar with dis1
show mar talking with dis3
mar "\"{cps=20}Sometimes you have to lose yourself in the coziness.\""
show mar with dis1
show mar talking with dis3
mar "\"{cps=20}And the idea of not moving anymore isn’t so bad.\""
show mar eyes with dis1
show mar eyes talking with dis3
mar "\"{cps=20}Because you’re pretty as a picture and not quite so cheap.\""
show mar eyes with dis3
wi "\"Mrs. Greene.\""
show mar with dis3
wi "\"What does this have to do with anything?\""
show mar talking with dis3
mar "\"{cps=20}I’m just repeating what he said, before he took me away from everybody I knew.\""
show mar with dis1
show mar talking with dis3
mar "\"{cps=20}I think I understand now that he just liked to hurt me.\""
show mar eyes with dis1
show mar eyes talking with dis3
mar "\"{cps=20}Not because I think it made him happy...\""
show mar eyes with dis1
show mar eyes talking with dis3
mar "\"{cps=20}But because it made him feel more alive.\""
show mar eyes with dis1
show mar eyes talking with dis3
mar "\"{cps=20}Made him feel more alive than me, all the while saying he was doing me the greatest favor.\""
show mar with dis1
show mar talking with dis3
mar "\"{cps=20}Well, he wasn’t doing that.\""
show mar dazed with dis3
mar "\"{cps=20}I just think...\""
mar "\"{cps=15}I just think--\""
play sound ("sfx/wsplash.ogg")
scene bg black with dis
"We flinch as she goes cross-eyed and retches loudly."
"Red vomit shoots into the dark water we cleaned her with."
scene bg greenecottageinterior dark
show mar eyes at center,house1
if KaneChoice == True:
    show tod surprised a at right,house1
else:
    show tod surprised at right,house1
with dis3
"I don’t know if she’s going to be okay, or if she’s got much time left."
if KaneChoice == True:
    show tod sad a with dis3
else:
    show tod sad with dis3
wi "\"Mrs. Greene, don’t push yourself.\""
show mar dazed with dis3
mar "\"{cps=20}But I... want. To.\""
mar "\"{cps=20}Won’t let him hurt people no more.\""
show mar dazed eyes with dis3
mar "\"{cps=20}Not even... dead...\""
wi "\"Mrs. Greene!\""
mar "\"{cps=20}He had the gun.\""
mar "\"{cps=20}Went in the carriage.\""
mar "\"{cps=20}Doing things for Huxley even she didn’t know.\""
mar "\"{cps=20}Red... fox...\""
wi "\"Red...\""
if KaneChoice == True:
    show tod surprised a with dis3
else:
    show tod surprised with dis3
to "\"Fox?\""
"...That’s what I needed."
hide mar with dis3
"She vomits again, brighter red this time, and her breath quickens."
wi "\"Todd, I want you to stay with her while Sam brings help.\""
if KaneChoice == True:
    show tod sad a with dis3
else:
    show tod sad with dis3
to "\"Y-yes sir.\""
stop music fadeout 2.0
scene bg black with slow_dissolve
$ quick_menu = True
$ quick_menu_will = False
$ willnote = False
pause 0.8
"I’m used to being covered in bodily fluids any day of the week, but I’m still not used to blood."
cy "\"Sam?\""
scene bg powderroom
show ave serious at centerleft
show cyn fear a at left:
    xzoom-1
show dor cig eyes at right
with slow_dissolve
m "\"Hrm?\""
play music ("music/mellowpiano.ogg")
cy "\"Are you with me?\""
"I stop staring at the bucket of water that’s taken on a pink hue."
show cyn sad a with dis3
show dor cig worried with dis3
cy "\"Could you hand me a rag from one of the clean buckets?\""
show cyn fear a with dis3
cy "\"This one’s already warm.\""
show dor cig eyes talking with dis
md "\"It’s because her temperature is increasing.\""
show dor cig eyes with dis1
show dor cig eyes talking with dis
md "\"She’s burning up.\""
show dor cig worried with dis1
show cyn sad a with dis3
cy "\"Is she gonna be alright?\""
show dor cig eyes talking with dis
md "\"I’ve seen women in worse condition pull through, but it’s pretty bad.\""
show dor cig with dis1
show dor cig profile talking with dis3
md "\"What do you think, Avery?\""
show dor cig profile with dis1
show ave thinking scared with dis3
av "\"It’s... bad.\""
show ave thinking with dis
av "\"I think an IV solution is necessary for any chance at a partial recovery.\""
show ave thinking sad with dis
av "\"But there will be permanent damage.\""
show dor cig eyes talking with dis3
show ave serious with dis3
md "\"I’ll pay any expense.\""
show dor cig with dis1
show dor cig talking with dis
md "\"Just do what has to be done.\""
show dor cig worried with dis
show ave serious talking with dis
av "\"Right away.\""
show ave serious with dis1
show ave serious talking with dis
av "\"Could I ask one of the residents to stay for a moment?\""
show ave serious with dis
show dor cig with dis
show cyn fear a with dis
cy "\"I can--\""
show cyn surprised a with dis
show dor cig profile talking with dis
md "\"That will be me.\""
show dor cig profile with dis
show cyn serious a with dis
"Cynthia closes her mouth and nods."
show ave shocked with dis
show cyn surprised a with dis
show dor cig with dis3
grunk "\"Where is she?\""
hide cyn
hide dor
hide ave
with dis3
"A familiar, stern voice echoes through the hallway."
show gre at left with dis3:
    xzoom-1
"An older vixen, who I recognize as Mrs. Byrnes, makes her way into the hall, being trailed by Scarlet."
show gre eyes with dis
sc "\"I told her that she should wait but--\""
show ave shocked at centerleft behind gre
show dor cig at right
with dissolve
show gre with dis
show dor cig eyes talking with dis
md "\"It’s fine, Scarlet.\""
show dor cig with dis
show gre talking with dis
show ave serious with dis
gr "\"Let me see her.\""
show gre with dis1
show dor cig profile with dis3
"The madam makes a quiet gesture with her hand and Mrs. Byrnes stands over the bedside of Marcy Greene."
show gre a down with dis3:
    xzoom 1
"Her stiff face slackens to a look of remorse."
show gre a talking with dis
gr "\"What happened to her?\""
show gre a with dis
show ave serious talking with dis
av "\"From what I can tell, complications in delivery long term may have lead to sepsis.\""
show ave serious with dis
show gre a talking with dis
gr "\"From just one delivery?\""
show gre a down with dis3
show ave thinking sad with dis3
av "\"This looks like several.\""
show dor cig profile talking with dis1
show ave shocked with dis3
md "\"From what the police have told me, more than ten.\""
show dor cig profile with dis1
show ave serious with dis3
show gre with dis3:
    xzoom-1
"Her head snaps to the madam."
show gre talking with dis
gr "\"More than ten?!\""
show gre frown grit eyes with dis
gr "\"Oh, that beast...\""
show gre eyes with dis1
show gre eyes talking with dis
gr "\"She doesn’t have to worry anymore.\""
show gre smi with dis1
show gre smi talking with dis
gr "\"We’ll take good care of her.\""
show ave serious eyes with dis
show dor cig profile talking with dis
show gre smi with dis
md "\"Yes, we will.\""
show ave serious with dis
show dor cig talking with dis3
md "\"What will you provide to the cause, Gretchen?\""
show dor cig with dis
show gre smi talking with dis
gr "\"What do you need?\""
show gre smi with dis1
show gre smi talking with dis
gr "\"Money?\""
show gre with dis
show dor cig profile squint with dis3
md "\"Assurance.\""
show dor cig profile with dis
show gre talking with dis
gr "\"On?\""
show gre with dis
show dor cig profile squint with dis
md "\"That you’ll go through me and the doctor before giving anymore girls in the community dosages.\""
show dor cig profile with dis1
show gre f frown eyes with dis3:
    xzoom 1
"She looks like she’s about to argue, {nw}"
show gre f down with dis
extend "but the madam gives her a look so intense that the vixen recedes."
show gre f eyes calm with dis
"She clasps Marcy’s paw like she’s a daughter, stoops over her and kisses her forehead once before wiping away a tear."
show gre f eyes calm talking with dis
gr "\"Alright.\""
show gre f with dis1
show dor cig talking with dis3
md "\"Good.\""
show dor cig with dis1
show dor cig talking with dis
show ave serious eyes with dis
md "\"Nothing we’ve said leaves this room.\""
show ave serious with dis
show dor cig profile squint with dis3
md "\"That goes for everyone here.\""
show dor cig profile with dis
#sfx
hide dor
hide ave
hide gre
with dis3
"Me, Cynthia, Avery and Scarlet all nod and she draws the curtains over Marcy’s bed, leaving only the outline of her silhouette and the doctor’s."
show cyn surprised a with dissolve
cy "\"Let’s go do some laundry, Sam.\""
show cyn sad a with dis3
cy "\"Your clothes are a bit of a mess.\""
show cyn surprised a with dis3
sc "\"Bit of a mess?\""
show cyn serious a with dis
sc "\"He looks like the ripper.\""
sc "\"What went on at the Greene’s?\""
show cyn sad a with dis3
m "\"A lot.\""
m "\"It’s a bit of a long story.\""
show cyn serious a with dis3
sc "\"And tossin’ your scants around in grey water is such a high intensity activity?\""
sc "\"Tell me the details, love.\""
sc "\"That’s it, I’m comin’ with you.\""
"Both Cynthia and I refuse because we’re so worn out, but she doesn’t really take no for an answer."
scene bg black with dissolve
scene bg hipwashroom with dissolve
show cyn serious a at centerleft with dis
"So the three of us huddle around the laundry room barrel, rolling our soiled clothes over the washboard, as I tell them both what happened."
sc "\"...what in the name of creation was going on in that awful house?\""
show cyn seriouscrossed a with dis3
cy "\"Mrs. Byrnes must have known to some extent, right?\""
sc "\"I doubt to that extent.\""
sc "\"She’s provided plenty of medicine for us and I’ve never seen it go sideways like that.\""
"She shakes her head."
show cyn sadcrossed a with dis3
sc "\"Ten though?\""
sc "\"Just one takes a toll, but ten?\""
cy "\"It’s unbelievable.\""
show cyn angrycrossed a with dis3
cy "\"That man of hers needs more than an earful.\""
m "\"He’s dead.\""
show cyn seriouscrossed a with dis
sc "\"Too true my duckie, I’m ready to march on his property meself and give him the hosing down that his mother ought to have done years ago.\""
show cyn surprised a with dis3
m "\"I mean he’s actually dead.\""
show cyn serious a with dis
"She looks at me and tilts her head."
sc "\"Since when?\""
m "\"Since Thursday.\""
show cyn surprised a with dis
m "\"His head’s been cut off.\""
show cyn fear a with dis
"Both she and Cynthia look shocked."
sc "\"That might be a thing worth knowin’?!\""
sc "\"You’d think the sheriff would go spreading the great news?\""
show cyn seriouscrossed a with dis3
cy "\"Adler’s too busy spying on us and making deals to do his job I wager.\""
sc "\"That’s usually how things go for a sheriff in this part of the country though, innit?\""
sc "\"Next one through the revolving door doesn’t tend to be much different.\""
sc "\"Hopefully this one won’t be sent away in a casket looking like swiss cheese.\""
m "\"But he was doing his job.\""
m "\"He announced it to the widow first.\""
m "\"Soon after she had her emergency.\""
show cyn angrycrossed a with dis
cy "\"Then where is he now?\""
show cyn seriouscrossed a with dis
m "\"I don’t know.\""
m "\"He had to chase a lead, but he made sure Marcy was taken care of.\""
show cyn angrycrossed a with dis
cy "\"And he just zoomed off, leaving you alone?\""
show cyn yellingcrossed a with dis
cy "\"With the otter?\""
show cyn angrycrossed a with dis
"Her tone is sounding more and more incredulous as time passes."
show cyn seriouscrossed a with dis
m "\"Bronson got the job done.\""
show cyn angrycrossed a with dis
cy "\"The man can barely get his holster on, Sam.\""
show cyn seriouscrossed a with dis
m "\"If you have a problem with this then why don’t you just talk to the sheriff?\""
show cyn angrycrossed a with dis
cy "\"I don’t need to talk to him.\""
cy "\"I’m just saying he was probably better equipped to handle a situation like that than--\""
stop music fadeout 5.0
show cyn seriouscrossed a with dis
wi "\"Sam?\""
"We hear William’s voice down the corner."
sc "\"Looks like it’s time for me to pack it up.\""
sc "\"Let’s talk again soon, lovelies.\""
if KaneChoice == True:
    show wil surprised nw at right with dis3
else:
    show wil surprised at right with dis3
"She leaves the doorway and lets out a one-note giggle as she bumps into William in the hall and clamors past him."
"Cynthia marches right up to him."
show cyn angrycrossed a with dis
cy "\"What the hell happened, William?\""
if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
wi "\"I don’t have time to go over it, but you probably heard everything there is to tell.\""
if KaneChoice == True:
    show wil nw with dis1
else:
    show wil with dis1
if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
show cyn annoyedcrossed a with dis
wi "\"I need to talk to Mrs. Byrnes, and now.\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
cy "\"Why now?\""
if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
show cyn surprisedcrossed a with dis
wi "\"Because I know she’s here, and I know she’s involved.\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis

label williamroute3d:

show cyn seriouscrossed a with dis
cy "\"I’ll go and ask the Madam if she’s willing to talk.\""
if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
wi "\"She better.\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
cy "\"I’ll doubt she’ll refuse you, but it’s worth a try.\""
if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
wi "\"Take your time.\""
if KaneChoice == True:
    show wil nw with dis1
else:
    show wil with dis1
window hide
scene bg black with dissolve
$ quick_menu = False
$ quick_menu_will = True
$ willnote = True
play music ("music/contemplation.ogg") fadein 1.5
pause 2.0
window show
"Half past ten."
scene bg powderroom
show sam at right
with dis3
"I’m working later and later each day."
"Like it’s the old days all over again."
wi "\"Could you step out while I’m waiting for Mrs. Byrnes, Sam?\""
show sam talking with dis
m "\"Sure.\""
show sam -talking with dis1
show sam talking with dis
m "\"Any reason why?\""
show sam -talking with dis
wi "\"People say different things when they’re by themselves.\""
wi "\"I think that’s going to matter for this.\""
show sam talking with dis
m "\"If you say so.\""
show sam -talking with dis
wi "\"See you soon.\""
show sam eyes with dis
m "\"Mmm.\""
show sam -eyes with dis1
hide sam with dis3
play sound ("sfx/saloonbackdoor.ogg")
"He slips out the back door, since she’s more likely to enter from the hall side."
if SW_Points>2:
    "He doesn’t give himself enough credit about little things like that."
play sound ("<from 0.1>sfx/dooropen.ogg")
show gre f at center with dissolve
show gre f talking with dis
gr "\"You wanted to see me?\""
stop sound
show gre f with dis
wi "\"Perhaps not under these circumstances.\""
show gre f talking with dis
gr "\"Quite.\""
show gre f eyes with dis1
show gre f eyes talking with dis
gr "\"You consider yourself quite the big shot, don’t you, Mr. Adler?\""
show gre f with dis
wi "\"You don’t need a big bullet to take anybody down.\""
wi "\"Sometimes you don’t need anything that blunt.\""
wi "\"Toxins that aid in birth control for instance...\""
show gre f talking with dis
gr "\"Would be considered an easily accessible remedy, you mean?\""
show gre f eyes with dis1
show gre f eyes talking with dis
gr "\"Girls out here on the prairie all know it.\""
show gre f with dis1
show gre f talking with dis
gr "\"A good man can be hard to find when they’re lonely and outnumber the girls one hundred to one.\""
show gre f with dis
wi "\"Since it’s not such a big deal then, would you admit to giving Marcy Greene access to the plants she would need?\""
show gre f eyes talking with dis
gr "\"I don’t recall.\""
show gre f with dis1
show gre f talking with dis
gr "\"It’s quite possible, but Marcy had the gardening know-how to supply what she needed herself at any time, I imagine.\""
show gre f with dis1
show gre f talking with dis
gr "\"Do you plan on getting to the point, Mr. Adler?\""
show gre f with dis
wi "\"There’s not always a point to these things.\""
show gre f eyes talking with dis
gr "\"How aptly put.\""
show gre f with dis
wi "\"But it’s important to know as much as we can, as soon as we can, when a case is fresh and there are a whole lot of loose ends.\""
show gre f down with dis
wi "\"Was Marcy suicidal?\""
show gre f talking with dis
gr "\"No.\""
show gre f with dis1
show gre f talking with dis
gr "\"Survival is all Marcy knows.\""
show gre f with dis1
show gre f talking with dis
gr "\"She’s become something of an expert in it...\""
show gre f with dis
wi "\"Did she give you any indication that she might be experiencing recent delusions?\""
show gre f talking with dis
gr "\"Not to my knowledge.\""
show gre f eyes with dis1
show gre f eyes talking with dis
gr "\"I believe she pretends to act like a child because the role is forced on her.\""
show gre f frown with dis
wi "\"By whom?\""
show gre f frown talking with dis
gr "\"I believe you know who.\""
show gre f frown with dis
wi "\"By her husband?\""
show gre f frown talking with dis
gr "\"Late husband.\""
show gre f frown with dis
"I look up at her and watch her as I write."
wi "\"What makes you think that he’s dead?\""
show gre f frown talking with dis
gr "\"Because he’d be dead before leaving her alone.\""
show gre f frown with dis1
show gre f frown talking with dis
gr "\"He considered her his prize.\""
show gre f with dis
wi "\"So you don’t actually know that he’s dead?\""
show gre f talking with dis
gr "\"If he isn’t, then he’s somewhere he doesn’t want to be.\""
show gre f eyes with dis1
show gre f eyes talking with dis
gr "\"Unless he’s somebody’s hostage, I’m willing to bet a pretty penny that he is, indeed, dead.\""
show gre f down with dis
wi "\"How much would you bet if we did it now?\""
show gre f frown talking with dis
gr "\"Pardon?\""
show gre f frown with dis
wi "\"If you could entertain the thought, Mrs. Byrnes.\""
show gre a eyes talking with dis3
gr "\"If you want me to gamble with you, Mr. Adler, you should fix me a strong drink.\""
show gre f sq frown with dis3
wi "\"That won’t be necessary.\""
show gre f sq frown talking with dis
gr "\"You’re cheap, like expected.\""
show gre with dissolve
show gre talking with dis
gr "\"Will that be all?\""
show gre with dis
wi "\"Just one more thing.\""
show gre eyes talking with dis
gr "\"Let’s hear it then, darling.\""
show gre eyes with dis1
show gre eyes talking with dis
gr "\"If you keep me any longer, I’ll have to send divorce papers your way too.\""
show gre with dis
wi "\"Right.\""
wi "\"Did you attend a gathering at the Hendricks’ mansion within the last week?\""
show gre talking with dis
gr "\"A few days ago.\""
show gre with dis
wi "\"Which day?\""
show gre talking with dis
#here
gr "\"Monday.\""
show gre with dis
wi "\"Did you walk?\""
show gre talking with dis
gr "\"We have a carriage.\""
show gre with dis
"I slap my pencil down to the desk."
wi "\"Thank you ma’am, that will be all.\""
wi "\"Thanks to your help, I think we’re closer to understanding what happened to both of the Greenes.\""
show gre eyes talking with dis
gr "\"I don’t get a pat on the back when I do my job, Mr. Adler.\""
show gre with dis1
show gre talking with dis
gr "\"Don’t expect you’ll get one either from doing the bare minimum.\""
show gre with dis1
hide gre with dis3
"She walks out the door with her head held high."
wi "\"I’ll savor it when I solve it, ma’am.\""
play sound ("sfx/doorshut.ogg")
"The door closes."
"She’s confident about where she was the night we found Huxley."
"Strange thing to do for a lead suspect."
play sound ("<to 0.5>sfx/saloonbackdoor.ogg")
"Another door cracks behind me."

window hide
scene bg black with dissolve
$ quick_menu = True
$ quick_menu_will = False
$ willnote = False
window show

if KaneChoice == True:
    scene bg powderroom
    show wil nw at center
    with dis3
else:
    scene bg powderroom
    show wil at center
    with dis3
stop sound
m "\"I thought I heard her leave.\""
if KaneChoice == True:
    show wil eyes talking nw with dis
else:
    show wil eyes talking with dis
wi "\"She did, Sam.\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
m "\"So did it go anywhere?\""
if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
wi "\"Just some statements she might regret if I can prove any of them were false later.\""
if KaneChoice == True:
    show wil sideeyes nw with dis3
else:
    show wil sideeyes with dis3

"Will rubs his temples and thinks."

if KaneChoice == True:
    show wil eyes talking nw with dis3
else:
    show wil eyes talking with dis3
wi "\"Alright.\""
if KaneChoice == True:
    show wil nw with dis1
    show wil talking nw with dis
else:
    show wil with dis1
    show wil talking with dis
wi "\"I think I’ve talked enough the last few days.\""
if KaneChoice == True:
    show wil nw with dis1
    show wil talking nw with dis
else:
    show wil with dis1
    show wil talking with dis
wi "\"It’s time to make moves.\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
m "\"...What exactly can you do?\""
if KaneChoice == True:
    show wil sideeyes nw with dis3
else:
    show wil sideeyes with dis3
wi "\"Let’s get back to my office.\""
if KaneChoice == True:
    show wil talking nw with dis3
else:
    show wil talking with dis3
wi "\"Too many shadows linger against doorways here.\""
if KaneChoice == True:
    show wil nw with dis1
else:
    show wil with dis1
hide wil with dis3
"I nod, following William out the door."
scene bg black with dissolve
scene bg echoroadnight with dis3
"When we’re outside the Hip, we pick up our gait."

"It’s all too quiet for a night like this."

"Usually there’s more fuss."

"More drinking and gambling."

"But nobody’s around."

"It’s the same kind of feeling when you’re out in the wild by your lonesome and you don’t hear any bugs."

"But you feel no greater certainty that something is out there."

"The fur on William’s tail is bristling too."

"I can tell he feels it, but he’s not reacting to it."

"Not besides picking up his pace to a light sprint."
scene bg black with dissolve
scene bg officenight with dis3
play sound ("sfx/keytake.ogg")
queue sound ("sfx/keyopen.ogg")
"When we get back to the office, Will fumbles for his keys and wastes no time locking the door."
if KaneChoice == True:
    show wil sideeyes nw at center,prisonnight with dis3
else:
    show wil sideeyes at center,prisonnight with dis3
m "\"...Why’d you do that?\""

"His paw pauses."
stop sound
wi "\"I don’t know.\""

wi "\"It’s an instinct I picked up a long time ago...\""
if KaneChoice == True:
    show wil nw with dis3
else:
    show wil with dis3
m "\"Was somebody following us?\""
if KaneChoice == True:
    show wil eyes talking nw with dis
else:
    show wil eyes talking with dis
wi "\"I think so.\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
m "\"...Who?\""
if KaneChoice == True:
    show wil sideeyes nw with dis3
else:
    show wil sideeyes with dis3
wi "\"Can’t say.\""

wi "\"Doesn’t matter now though, unless they plan on breaking down the door.\""

wi "\"The feeling’s gone.\""

"He’s right about that."

"I don’t know why, but being here in the jailhouse feels more safe."

"Even though the window’s fixed, I still remember the sound of the glass breaking."
"It’s easy to forget things like that can happen any time, even when you think you feel safe."

if KaneChoice == True:
    show wil nw with dis3
else:
    show wil with dis3
m "\"So what are you going to do now?\""
if KaneChoice == True:
    show wil eyes nw with dis
else:
    show wil eyes with dis
"William walks{nw}"
hide wil with dis3
play sound ("sfx/bottles1.ogg") volume 0.5
extend " over to the bar in his office, and I hear him unscrew a glass stopper."
queue sound ("<from 1.8 to 3.5>sfx/tea.ogg")
"I hear pouring."
if KaneChoice == True:
    show wil nw at center,prisonnight with dis3
else:
    show wil at center,prisonnight with dis3
"He returns with a glass and offers it to me without asking."
stop sound
"I take it because I need it."

"I tip it to my lips, tasting just a bit."

"There’s no burn to this whiskey."

"It’s nicer than his ordinary stuff."

"Will drinks too, but his eye is on me rather than the glass."
if KaneChoice == True:
    show wil eyes nw with dis
else:
    show wil eyes with dis
queue sound ("<to 0.4>sfx/glass.ogg") volume 0.5
"He tips his head back, downing a shot, and then places the glass on an end table with a clock."
if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
stop sound
wi "\"Hendricks is having a party in two days.\""
if KaneChoice == True:
    show wil eyes nw with dis1
    show wil eyes talking nw with dis
else:
    show wil eyes with dis1
    show wil eyes talking with dis
wi "\"He’ll be more distracted than usual, and he can’t resist showing off.\""
if KaneChoice == True:
    show wil nw with dis1
    show wil talking nw with dis
else:
    show wil with dis1
    show wil talking with dis
wi "\"If there’s any day to learn what we need to learn about that house, that will be the day.\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
m "\"I thought you didn’t find a lot there the last time.\""
if KaneChoice == True:
    show wil eyes nw with dis
else:
    show wil eyes with dis
"William shakes his head."
if KaneChoice == True:
    show wil eyes talking nw with dis
else:
    show wil eyes talking with dis
wi "\"Not true.\""
if KaneChoice == True:
    show wil nw with dis1
    show wil talking nw with dis
else:
    show wil with dis1
    show wil talking with dis
wi "\"Often, you find most of what you need quite early.\""
if KaneChoice == True:
    show wil nw with dis1
    show wil talking nw with dis
else:
    show wil with dis1
    show wil talking with dis
wi "\"Just ain’t always gonna know what you’re looking for right away.\""
if KaneChoice == True:
    show wil eyes nw with dis1
    show wil eyes talking nw with dis
else:
    show wil eyes with dis1
    show wil eyes talking with dis
wi "\"No.\""
if KaneChoice == True:
    show wil nw with dis1
    show wil talking nw with dis
else:
    show wil with dis1
    show wil talking with dis
wi "\"I’m quite certain James Hendricks aided and concealed the deaths of several dozen different people, though he certainly wasn’t alone, and he wasn’t the outright murderer in many of these cases.\""
if KaneChoice == True:
    show wil sideeyes nw with dis3
else:
    show wil sideeyes with dis
wi "\"But you have to be able to prove these things beyond a reasonable doubt.\""

wi "\"And even then, a good lawyer can get you out of things.\""

wi "\"He needs to be exposed, and in front of a crowd.\""

wi "\"I can tell that there’s more than one thing in that mansion that would hang him.\""
if KaneChoice == True:
    show wil nw with dis3
else:
    show wil with dis3
m "\"...But what if nobody listens?\""
if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
wi "\"Then they’ll have to live with it when I shoot him.\""
if KaneChoice == True:
    show wil eyes nw with dis1
    show wil eyes talking nw with dis
else:
    show wil eyes with dis1
    show wil eyes talking with dis
wi "\"I don’t think it will come to that...\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
m "\"...I don’t suspect it should.\""

m "\"It’s an awful thing to make a man bleed.\""
if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
wi "\"Not if they’re soaked in everybody else’s blood.\""
if KaneChoice == True:
    show wil eyes nw with dis1
    show wil eyes talking nw with dis
else:
    show wil eyes with dis1
    show wil eyes talking with dis
wi "\"But you’re right.\""
if KaneChoice == True:
    show wil nw with dis1
    show wil talking nw with dis
else:
    show wil with dis1
    show wil talking with dis
wi "\"It shouldn’t come to that.\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
m "\"...So what are you going to do with one day?\""
if KaneChoice == True:
    show wil eyes talking nw with dis
else:
    show wil eyes talking with dis
wi "\"Find out as much about that house as possible before stepping in.\""
if KaneChoice == True:
    show wil nw with dis1
    show wil talking nw with dis
else:
    show wil with dis1
    show wil talking with dis
wi "\"Everyone who works there.\""
if KaneChoice == True:
    show wil nw with dis1
    show wil talking nw with dis
else:
    show wil with dis1
    show wil talking with dis
wi "\"All the ways you could come and go.\""
if KaneChoice == True:
    show wil nw with dis1
    show wil talking nw with dis
else:
    show wil with dis1
    show wil talking with dis
wi "\"People who regularly attend the parties there.\""


if KaneChoice == True:
    show wil nw with dis
    m "\"You have been making friends in unlikely places.\""
    show wil surprised nw with dis
    m "\"Why not use what you’ve got?\""
    wi "\"...Huh?\""
    m "\"I mean that wolf we fucked from the bar.\""
    show wil frustrated nw with dis3
    wi "\"You mean the sunuvabitch who stole our clothes?\""
    m "\"Yeah.\""
    wi "\"Are you stupid?\""
    m "\"Well...\""
    m "\"People who spend the energy to fuck with you tend to like you in some manner.\""
    wi "\"...By stealing our clothes?\""
    wi "\"I get the feeling he just wanted to get the booze money out of pawning our things.\""
    show wil nw with dis3
    m "\"If he just wants money, it would make it even easier to get what you want out of him.\""
    show wil surprised nw with dis
    m "\"That ain’t the feeling I got though.\""
    show wil nw with dis
    wi "\"Uh huh?\""
    m "\"Some people are junkies for excitement.\""
    m "\"I’d know better about that than anybody.\""
    show wil sideeyes nw with dis3
    m "\"I get the feeling he was posing a challenge for you.\""
    m "\"He got a kind of look in his eye when he mentioned you were the sheriff.\""
    m "\"Knowing you’d be trouble was {i}exciting{/i} to him, William.\""
    show wil nw with dis3
    m "\"I just figured you could use that.\""
    show wil eyes nw with dis
    "William’s lip curls into a scowl."
    show wil eyes talking nw with dis
    wi "\"It’s something.\""
    show wil nw with dis
    m "\"Only trouble I suspect is finding him again.\""
    show wil sideeyes nw with dis3
    wi "\"That won’t be a problem if he’s not already out of town.\""
    show wil talking nw with dis3
    wi "\"Ghosts tend to haunt the same graveyards.\""
    show wil eyes nw with dis1
    show wil eyes talking nw with dis
    wi "\"He’ll be at the Stag, or close to it.\""
    show wil nw with dis

else:
    show wil surprised with dis
    m "\"What about Nik?\""
    show wil talking with dis
    wi "\"What {i}about{/i} Nik?\""
    show wil with dis
    m "\"He’d help us find something if we ask...\""
    show wil talking with dis
    wi "\"Well, yeah.\""
    show wil with dis1
    show wil talking with dis
    wi "\"Of course he would.\""
    show wil sideeyes with dis3
    wi "\"But askin’ a man to bite the hand that feeds him more than once is an unreasonable ask.\""
    show wil eyes talking with dis3
    wi "\"I don’t like puttin’ him in that position.\""
    show wil with dis1
    show wil talking with dis
    wi "\"But maybe he can point us in another direction.\""
    show wil with dis1
    show wil talking with dis
    wi "\"Spread the heat off of him a bit.\""
    show wil with dis3
    m "\"That club he goes to would probably be the least suspicious place to get in contact.\""
    show wil talking with dis
    wi "\"The Stag?\""
    show wil sideeyes with dis3
    wi "\"Mmm.\""
    wi "\"I had the same thought as well.\""
    show wil talking with dis3
    wi "\"But let’s keep it strictly business this time, not pleasure, yeah?\""
    if SW_Points >2:
        show wil smile with dis
    else:
        show wil with dis
    m "\"Ironic thing to say to me, but sure.\""
    show wil with dis
#
"I stare down at the crystal glass in my paw, swirling around the golden liquid."

m "\"Should I be going then?\""
if KaneChoice == True:
    show wil sideeyes nw with dis3
else:
    show wil sideeyes with dis3
"William taps his paws on his glass, glancing at the repairs in the window."
if KaneChoice == True:
    show wil talking nw with dis3
else:
    show wil talking with dis3
wi "\"In ordinary cases I’d say it’s a bad idea for you to spend too much time with me.\""
if KaneChoice == True:
    show wil nw with dis1
    show wil talking nw with dis
else:
    show wil with dis1
    show wil talking with dis
wi "\"But as things are, probably would be the best if you spent your nights with me until things get back to normal.\""
if KaneChoice == True:
    show wil nw with dis3
else:
    show wil with dis3
m "\"...Will they ever?\""
if KaneChoice == True:
    show wil sideeyes nw with dis3
else:
    show wil sideeyes with dis3
"Willim breaks eye contact and clears his throat."

wi "\"Yes.\""

wi "\"They have to.\""

wi "\"Pressure like this can’t just keep building up forever.\""

wi "\"Eventually things explode.\""

wi "\"Then they go back to as normal as they can.\""

wi "\"It’s an endless cycle, and it happens everywhere.\""

wi "\"It’s just hard to know what it’s going to look like before it happens.\""

m "\"Hm.\""
if KaneChoice == True:
    show wil nw with dis3
else:
    show wil with dis3
m "\"So what does that mean for the two of us then?\""

"Will cocks his head and places his glass on the end table."
if KaneChoice == True:
    show wil talking nw with dis3
else:
    show wil talking with dis3
wi "\"Say what you mean.\""
if KaneChoice == True:
    show wil sideeyes nw with dis3
else:
    show wil sideeyes with dis3
m "\"I mean, what am I doing here if things are just going to go back to how they were?\""
if KaneChoice == True:
    show wil talking nw with dis3
else:
    show wil talking with dis3
wi "\"That’s what you’re hoping for after this, right?\""
if KaneChoice == True:
    show wil eyes nw with dis1
    show wil eyes talking nw with dis
else:
    show wil eyes with dis1
    show wil eyes talking with dis
wi "\"You really want to know?\""
if KaneChoice == True:
    show wil nw with dis3
else:
    show wil with dis3
m "\"Yeah.\""

if SW_Points >2:
    "Will taps the outside of his glass with his paws before he sets it down on the table."
    if KaneChoice == True:
        show wil eyes nw with dis3
    else:
        show wil eyes with dis3
    "He hunches over, adjusting his shoulders and rolling his neck before he inhales."
    if KaneChoice == True:
        show wil eyes talking nw with dis3
    else:
        show wil eyes talking with dis3
    wi "\"Let’s start with the question you just asked.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"Why do {i}you{/i} think I want you here?\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    "I feel myself begin to scowl."

    m "\"To be honest, I really don’t know.\""

    m "\"There are smarter people than me in town who could help you out better than I could.\""
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    wi "\"You really think so?\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    m "\"Yeah, I do.\""
    if KaneChoice == True:
        show wil eyes talking nw with dis
    else:
        show wil eyes talking with dis
    wi "\"Then here’s what I think.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"I think you’re a lot smarter than you give yourself credit for.\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    m "\"Oh fuck off.\""
    play sound ("<from 0.2>sfx/tablepunch.ogg")
    if KaneChoice == True:
        show wil angry nw with hpunch
    else:
        show wil angry with hpunch
    wi "\"{i}Listen!{/i}\""
    if KaneChoice == True:
        show wil nw with dis3
    else:
        show wil with dis3
    "The table shakes and my mouth shuts."
    stop sound
    if KaneChoice == True:
        show wil eyes talking nw with dis
    else:
        show wil eyes talking with dis
    wi "\"The moment I saw you, I knew life had done you dirty.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"It’s in the way you hunch your shoulders.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"The way you avoid eye contact.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"The way you slink over yourself.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"How you try and make make yourself small, even when you’re the broadest-shouldered man in the room and your pelt shines as bright as the hot sand in the summer light.\""
    if KaneChoice == True:
        show wil eyes nw with dis1
        show wil eyes talking nw with dis
    else:
        show wil eyes with dis1
        show wil eyes talking with dis
    wi "\"You don’t have to tell me door after door was closed to you when you came a-knocking.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"It’s carved into your face like a whittler’s razors on balsa wood.\""
    if KaneChoice == True:
        show wil sideeyes nw with dis3
    else:
        show wil sideeyes with dis3
    wi "\"Terrible things happened to you, like how they happened to me.\""

    wi "\"I can’t stand five minutes alone with men who laugh too easy, knowing that they’ll never understand what it’s like to hurt.\""
    if KaneChoice == True:
        show wil talking nw with dis3
    else:
        show wil talking with dis3
    wi "\"Not even necessarily because I don’t think they want to.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"I more question their capacity to.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"If you can’t understand how people hurt, how can I begin to think you’d be able to recognize what people are capable of to make others hurt?\""
    if KaneChoice == True:
        show wil eyes nw with dis1
        show wil eyes talking nw with dis
    else:
        show wil eyes with dis1
        show wil eyes talking with dis
    wi "\"I simply think you can’t.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"Maybe it’s a terrible thing to say, but tough shit.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"It’s what I think.\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    "I feel the impulse to argue with him, but I don’t find the right words."
    if KaneChoice == True:
        show wil eyes talking nw with dis
    else:
        show wil eyes talking with dis
    wi "\"Now don’t get me wrong, Sam.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"I’m not saying people who feel deeply necessarily think deeply.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"Often enough, it’s the opposite.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"But you have to feel deeply to think deeply.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"People who don’t understand that never go far in my line of work.\""
    if KaneChoice == True:
        show wil eyes nw with dis1
        show wil eyes talking nw with dis
    else:
        show wil eyes with dis1
        show wil eyes talking with dis
    wi "\"You don’t just {i}have{/i} emotions.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"You think about them in a way that isn’t overly attached.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"Anything you missed out on in schooling, I can teach you.\""
    if KaneChoice == True:
        show wil eyes nw with dis1
        show wil eyes talking nw with dis
    else:
        show wil eyes with dis1
        show wil eyes talking with dis
    wi "\"But I can’t teach somebody that.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"I need somebody else on my level to give me a second opinion.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"And if I didn’t think that was you, then we wouldn’t be speaking right now.\""
    if KaneChoice == True:
        show wil eyes nw with dis1
    else:
        show wil eyes with dis1

#[if will is below the trust threshold]
else:
    if KaneChoice == True:
        show wil eyes talking nw with dis
    else:
        show wil eyes talking with dis
    wi "\"I think you talk too much when you’re worried.\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    m "\"...Fuck you.\""
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    wi "\"Still that tongue.\""
    if KaneChoice == True:
        show wil eyes nw with dis1
        show wil eyes talking nw with dis
    else:
        show wil eyes with dis1
        show wil eyes talking with dis
    wi "\"We should be grateful we both aren’t dead yet.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"Stay close to me and I’ll make sure you won’t be.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"Is that clear enough for you?\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    m "\"...Yeah.\""

if KaneChoice == True:
    show wil eyes talking nw with dis
else:
    show wil eyes talking with dis
wi "\"You should get some sleep.\""
if KaneChoice == True:
    show wil eyes nw with dis1
    show wil eyes talking nw with dis
else:
    show wil eyes with dis1
    show wil eyes talking with dis
wi  "\"We have a lot to do tomorrow.\""
if KaneChoice == True:
    show wil eyes nw with dis1
else:
    show wil eyes with dis1
hide wil with dis3
"Will doesn’t wait for me as he walks to the doors annexing the jail to his apartment."
stop music fadeout 3.5
"Whatever my feelings, I can’t disagree that this feels like the safest place for me to be right now."
scene bg black with dissolve
pause 1.5
"I lie in William’s bed, staring up at the ceiling."
scene bg willbedroomnight with dis3
"I had hoped to get a good night’s rest for once, but too many small noises at once keep me sitting up with my eyes wide open."

"Like the ironwood branch at William’s window that taps against the glass."

"Or the sounds of breathing that feel like they’re coming from William only sometimes."

"The longer I stare into the dark ceiling, the longer it feels like it’s staring back."

"The longer you’re used to being chased, the easier it is to believe something’s there, even if it might not be."

"But if there is something there..."

"Is it really me being haunted, or is it this place?"
scene bg black with dis4
"Sometimes I wonder."
pause 2.5
scene bg willbedroom with dis3
"...At some point I must have fallen asleep, because I can see daylight now."

"William’s not in bed either."
play music ("music/quiet.ogg") fadein 2.0
"I use his washroom to freshen up before heading down the stairs."
scene bg black with dissolve
if ETHINT_Points == 1 or HARINT_Points == 1:
    scene bg officeday with dis3
    "I see a thin-looking man heading quickly out the door of the jail."
    "I think he might be a weasel, but I’m not entirely sure."
    if KaneChoice == True:
        show wil nw at centerright,prisonday with dis3
    else:
        show wil at centerright,prisonday with dis3
    "But I forget about it when William’s gaze meets mine as he steps out of his office."
else:
    if KaneChoice == True:
        scene bg officeday
        show wil nw at centerright,prisonday
        with dissolve
    else:
        scene bg officeday
        show wil at centerright,prisonday
        with dissolve

if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
wi "\"You’re up.\""
if KaneChoice == True:
    show wil eyes nw with dis1
    show wil eyes talking nw with dis
else:
    show wil eyes with dis1
    show wil eyes talking with dis
wi "\"Good.\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
m "\"I don’t tend to sleep in late.\""
if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
wi "\"We have a real busy day ahead of us.\""
if KaneChoice == True:
    show wil nw with dis1
    show wil talking nw with dis
else:
    show wil with dis1
    show wil talking with dis
wi "\"Todd will be over any minute to receive his instructions.\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
m "\"Is he not coming with us?\""
if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
wi "\"We’ll need to establish some warrants with a judge from City Hall.\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
m "\"I haven’t seen you do that before.\""
if KaneChoice == True:
    show wil eyes talking nw with dis
else:
    show wil eyes talking with dis
wi "\"Sometimes I don’t really bother.\""
if KaneChoice == True:
    show wil nw with dis1
    show wil talking nw with dis
else:
    show wil with dis1
    show wil talking with dis
wi "\"This won’t be a situation like that.\""
play sound ("sfx/knock.ogg")
if KaneChoice == True:
    show wil surprised nw with dis3
else:
    show wil surprised with dis3
"There’s a few loud bangs on the front door."
queue sound ("sfx/knock.ogg")
if KaneChoice == True:
    show wil frustrated nw with dis3
else:
    show wil frustrated with dis
"I can tell from the weight of them and the fact that they pick up again before we get to the door that Todd’s the one making them."
stop sound
wi "\"You know the door isn’t locked, Todd.\""
if KaneChoice == True:
    show wil nw
    show tod sigh a at left,prisonday behind wil:
        xzoom-1
    with dis3
else:
    show wil
    show tod sigh at left,prisonday behind wil:
        xzoom-1
    with dis3
to "\"M’sorry!\""

to "\"I just wanted to forewarn you to my presence.\""
if KaneChoice == True:
    show wil eyes talking nw
    show tod surprised a
    with dis3
else:
    show wil eyes talking
    show tod surprised
    with dis3
wi "\"You’re always here at ten AM sharp.\""
if KaneChoice == True:
    show wil nw with dis1
    show wil talking nw with dis
else:
    show wil with dis1
    show wil talking with dis
wi "\"I could never mistake you for anybody else.\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
to "\"Right...\""
if KaneChoice == True:
    show tod arms sigh a with dis3
else:
    show tod arms sigh with dis3
to "\"It’s just been an eventful last few days, huh?\""
if KaneChoice == True:
    show tod arms surprised a with dis3
else:
    show tod arms surprised with dis3
"He’s blushing a bit as he looks my way."

"I realize now that I’m not wearing a shirt."
play sound ("sfx/paper1.ogg") volume 0.7
if KaneChoice == True:
    show tod surprised a with dis3
    show wil eyes nw with dis3
else:
    show tod surprised with dis3
    show wil eyes with dis3
"William pulls out an envelope from his pocket and taps it against Todd’s chest, issuing an order without skipping a beat."
stop sound
if KaneChoice == True:
    show wil talking nw with dis
    show tod a with dis
else:
    show wil talking with dis
    show tod with dis
wi "\"You’re going to have to take this to City Hall and give it to Judge Grant.\""
if KaneChoice == True:
    show wil nw with dis1
    show wil talking nw with dis
else:
    show wil with dis1
    show wil talking with dis
wi "\"Make sure he reads the whole thing and make sure you don’t leave without him giving you paperwork.\""
if KaneChoice == True:
    show wil nw with dis
    show tod talking a with dis
else:
    show wil with dis
    show tod talking with dis
to"\"Right.\""
if KaneChoice == True:
    show wil talking nw with dis
    show tod a with dis
else:
    show wil talking with dis
    show tod with dis
wi "\"This one’s probably going to take a while but don’t let him brush you off.\""
if KaneChoice == True:
    show wil nw with dis1
    show wil talking nw with dis
else:
    show wil with dis1
    show wil talking with dis
wi "\"It’s crucial that we get this warrant and that we leave a paper trail for it.\""
if KaneChoice == True:
    show wil nw with dis
    show tod talking a with dis
else:
    show wil with dis
    show tod talking with dis
to "\"Uh huh.\""
if KaneChoice == True:
    show tod a with dis1
    show tod talking a with dis
else:
    show tod with dis1
    show tod talking with dis
to "\"Who’s the warrant for this time?\""
if KaneChoice == True:
    show wil talking nw with dis
    show tod a with dis
else:
    show wil talking with dis
    show tod with dis
wi "\"Don’t worry about it. Just get it done.\""
if KaneChoice == True:
    show wil nw with dis
    show tod talking a with dis
else:
    show wil with dis
    show tod talking with dis
to "\"Yessir!\""
if KaneChoice == True:
    show tod sigh a with dis3
else:
    show tod sigh with dis3
to "\"I guess I shouldn’t waste time then.\""
if KaneChoice == True:
    show tod talking a with dis3
else:
    show tod talking with dis3
to "\"I’ll be off right away.\""
if KaneChoice == True:
    show wil talking nw with dis
    show tod a with dis
else:
    show wil talking with dis
    show tod with dis
wi "\"Good man.\""
if KaneChoice == True:
    show wil nw with dis
    show tod eyes happy a with dis
else:
    show wil with dis
    show tod eyes happy with dis
"The otter smiles a little when he hears that and walks away {nw}"
hide tod with dis3
extend "with a bounce in his step."

"It’s a bit surprising to see a deputy actin’ that bashful on duty."

m "\"You really think it’s going to take all day to get a warrant?\""
if KaneChoice == True:
    show wil eyes talking nw with dis
else:
    show wil eyes talking with dis
wi "\"Not sure, but he doesn’t need to be around for this anyway.\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
m "\"Why’s that?\""
if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
wi "\"I have my reasons.\""
if KaneChoice == True:
    show wil nw with dis1
    show wil talking nw with dis
else:
    show wil with dis1
    show wil talking with dis
wi "\"Go put your shirt on.\""
if KaneChoice == True:
    show wil nw with dis1
    show wil talking nw with dis
else:
    show wil with dis1
    show wil talking with dis
wi "\"I want to give that bar a closer look in the sunlight.\""
if KaneChoice == True:
    show wil nw with dis1
else:
    show wil with dis1
scene bg black with dissolve
scene bg echobackalley with dis3
"Outside, I get the same strange sense of loneliness I got the other night."

"Empty porches."

"Shuttered businesses."

"Perhaps I’m exaggerating a bit, but it’s like the whole town decided today isn’t going to happen."

"That’s unusual enough to unnerve me."

"But it doesn’t dissuade me from following William to that barn."
scene bg black with dissolve
scene bg stagexteriorday with dissolve
#sfx
if KaneChoice == True:
    show wil nw at center with dis3
else:
    show wil at center with dis3
play sound ("sfx/clothrustle.ogg") volume 0.7
"When we get there, William takes a cigarette and a lighter out of his pocket."
if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
wi "\"It loses some of its appeal when you can see all the cracks in the woodwork while the sun beats down on it.\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
m "\"Everybody looks better in the dark.\""
queue sound ("sfx/lighteron.ogg") volume 0.7
if KaneChoice == True:
    show wil eyes nw with dis
else:
    show wil eyes with dis
"He lights it."
if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
stop sound
wi "\"Those windows look a hell of a lot more welcoming when you can see ‘em lit up from the bottom of the hill.\""
if KaneChoice == True:
    show wil nw with dis1
    show wil talking nw with dis
else:
    show wil with dis1
    show wil talking with dis
wi "\"You’d think they’d still need light in a dark barn during the day if they’re preparing.\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
m "\"I guess.\""
if KaneChoice == True:
    show wil eyes nw with dis
else:
    show wil eyes with dis
"William takes a puff."

"Inhales."
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
"Exhales."
if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
wi "\"It just makes me ask questions is all.\""
play sound ("sfx/knock.ogg")
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
"William steps up and knocks at the door."
if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
wi "\"Anybody in there?\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
"A surly sounding voice answers."
stop sound
treunk "\"Uh.\""

treunk "\"We’re closed.\""
if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
wi "\"That’s okay.\""
if KaneChoice == True:
    show wil nw with dis1
    show wil talking nw with dis
else:
    show wil with dis1
    show wil talking with dis
wi "\"I’m here to ask questions, not to have a good time.\""
#sfx
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
"He flicks his badge at the front door."

"There’s not-so-subtle swearing on the other side of the door."

treunk "\"A minute.\""
if KaneChoice == True:
    show wil eyes talking nw with dis
else:
    show wil eyes talking with dis
wi "\"Take your time.\""
if KaneChoice == True:
    show wil nw with dis1
else:
    show wil with dis1
play sound ("sfx/gravelwalk.ogg")
hide wil with dis3
"I watch William stride over to the window while he waits."

"It looks like he can see pretty much everything whoever’s inside is doing, but he doesn’t seem impressed."
stop sound
treunk "\"Okay.\""

treunk "\"I’m unlocking the door now.\""
play sound ("sfx/doorcreakopen.ogg") volume 0.7
scene bg stag
show tre surprised br at center,stagday
with dis3
"We’re greeted by a tawny fox."

"I recognize him as the bartender from the other night."
stop sound
show tre talking with dis
bartre "\"Come in?\""
show tre -talking with dis1
if KaneChoice == True:
    show wil nw at stagday with dissolve:
        xzoom-1
        xpos -0.1
        yalign 1.0
    show wil talking nw with dis
else:
    show wil at stagday with dissolve:
        xzoom-1
        xpos -0.1
        yalign 1.0
    show wil talking with dis
wi "\"No need to be on edge.\""
if KaneChoice == True:
    show wil nw with dis1
    show wil talking nw
    show tre -surprised with dis
    with dis
else:
    show wil with dis1
    show wil talking
    show tre -surprised with dis
    with dis
wi "\"I’m just here to take a look around the site during the day.\""
if KaneChoice == True:
    show wil nw with dis1
    show wil talking nw  with dis
else:
    show wil with dis1
    show wil talking with dis
wi "\"You obviously know a lot of miners from CGCS like to drink here after hours.\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
show tre talking with dis
bartre "\"Well, yeah.\""
if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
show tre -talking surprised with dis
wi "\"And surely you have all the proper paperwork to sell what you make here.\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
show tre talking with dis
bartre "\"...Yes.\""
if KaneChoice == True:
    show wil eyes nw with dis
else:
    show wil eyes with dis
show tre -talking with dis
wi "\"Mmm.\""
if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
wi "\"I’m not here to bust anybody.\""
if KaneChoice == True:
    show wil nw with dis1
    show wil talking nw with dis
else:
    show wil with dis1
    show wil talking with dis
wi "\"But if you’re cooperative with me, it could be a great deal of help for those men who work the mines.\""
if KaneChoice == True:
    show wil eyes nw with dis1
    show wil eyes talking nw with dis
else:
    show wil eyes with dis1
    show wil eyes talking with dis
wi "\"Considering they’re the bread and butter of this business, I feel you’d be interested in their welfare.\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
show tre talking with dis
bartre "\"...Makes sense.\""
show tre -talking -surprised with dis1
show tre talking with dis
bartre "\"You know, now that you mention it, I think I might know something.\""
if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
show tre -talking with dis
wi "\"Maybe it has something to do with your cellar?\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
show tre talking with dis
bartre "\"We don’t have a cellar.\""
if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
show tre -talking surprised with dis
wi "\"Then what were you covering up with with the blue rug behind the bar?\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
bartre "\"Oh?\""
if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
show tre -surprised with dis
wi "\"It looked like a trapdoor.\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
show tre talking with dis
bartre "\"That just goes to the distillery.\""
if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
show tre -talking with dis
wi "\"So you realize admitting it’s a trapdoor means you have a cellar.\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
show tre eyes talking with dis
bartre "\"Sorry, my language isn’t so good.\""
if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
show tre -eyes -talking with dis
wi "\"It seems fine to me.\""
if KaneChoice == True:
    show wil nw with dis
else:
    show wil with dis
show tre talking with dis
bartre "\"No, sorry, it’s just very hard to understand you.\""
show tre -talking with dis
wi "\"Mhm.\""

if KaneChoice == True or SW_Points<3:
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    wi "\"So, I’m going to want to see what’s in your cellar now.\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    show tre eyes with dis
    "The fox says something under his breath that’s definitely at least three curses."
    show tre -eyes with dis1
    show tre talking with dis
    bartre "\"Yeah, okay, but not for very long?\""
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    show tre -talking with dis
    wi "\"That depends on what I find.\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    show tre talking with dis
    bartre "\"It’s nothing bad.\""
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    show tre -talking surprised with dis
    wi "\"Why would you think saying that would make me thing anything other than you’re doing something bad?\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    show tre eyes talking with dis
    bartre "\"But I said it’s nothing bad...\""
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    show tre surprised -talking with dis
    wi "\"Okay, please lift the rug.\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    "The bartender freezes for a moment, looks back at the rug with some reluctance, then looks like he’s about to say something."
    show tre eyes talking with dis
    bartre "\"Okay I’ll do it.\""
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    show tre surprised -talking with dis
    wi "\"As if that were in question?\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"Please get on with it, sir.\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    show tre eyes talking with dis
    bartre "\"Okay, okay.\""
    show tre -talking with dis
    "The fox moves in that awkward way that somebody does when they get caught with their pants down."
    play sound ("sfx/scrape4.ogg")
    show tre -eyes with dis
    "He sweeps away the blue rug with his foot paw and it reveals, to nobody’s surprise, a door."
    show tre talking with dis
    bartre "\"It’s kind of a dangerous place if you don’t let me go first?\""
    stop sound
    if KaneChoice == True:
        show wil eyes nw with dis
    else:
        show wil eyes with dis
    show tre -talking with dis
    "Will’s eyes are glazing over."
    if KaneChoice == True:
        show wil eyes talking nw with dis
    else:
        show wil eyes talking with dis
    wi "\"Be my guest.\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    "The fox picks up the trapdoor{nw}"
    play sound ("sfx/creak4.ogg")
    hide tre with dis3
    extend " and hops down a foot, the bottom half of his body disappearing as he sinks tail first into the hole."
    bartre "\"Uh, more people can come now.\""
    if KaneChoice == True:
        show wil eyes nw with dis
    else:
        show wil eyes with dis
    "Will beckons for me to go."
    stop sound
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    "I shake my head and he rolls his eyes."
    hide wil with dis3
    play sound ("sfx/creak2.ogg")
    stop music fadeout 10.0
    "Then I see him step into the hole, descending quick enough to make me feel the ladder has to be sturdy."
    "I follow his lead."
    "My paws touch cold metal."
    "It’s a steel ladder, bolted to the frame of the floor and an iron bar embedded in the ground."
    wi "\"Good God.\""
    if KaneChoice == True:
        scene bg stagcellar
        show wil surprised nw at left,dark2:
            xzoom-1
        show tre eyes smile br at dark2:
            xpos 0.65
            yalign 1.0
        with dis3
    else:
        scene bg stagcellar
        show wil surprised at left,dark2:
            xzoom-1
        show tre eyes smile br at dark2:
            xpos 0.65
            yalign 1.0
        with dis3
    "When I hit the floor I see what William is gawkin’ at."
    "Cases and cases of bottled spirits, some stacking to the top of the ceiling, litter the room."
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    show tre talking with dis
    bartre "\"Yeah it’s impressive, right?\""
    if KaneChoice == True:
        show wil eyes talking nw with dis
    else:
        show wil eyes talking with dis
    show tre -eyes -talking -smile with dis
    wi "\"It’s a whole lot more than an establishment like this would ever need.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"...Why’s there bed rolls?\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    show tre talking with dis
    bartre "\"Sometimes when I work with alcohol, I get sleepy just from touching it.\""
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    show tre surprised -talking with dis
    wi "\"You’re really not a good liar.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"And what’s this?\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    show tre talking with dis
    bartre "\"What’s what?\""
    show tre -talking with dis1

    if KaneChoice == True:
        hide wil
        show wil nw at left,dark2
        with dis3
    else:
        hide wil
        show wil at left,dark2
        with dis3
    "William looks at one of the larger stacks of crates in the corner."
    if KaneChoice == True:
        show wil eyes nw with dis
    else:
        show wil eyes with dis
    "He runs his paws against it."
    if KaneChoice == True:
        show wil eyes talking nw with dis
    else:
        show wil eyes talking with dis
    wi "\"I can feel wind.\""
    if KaneChoice == True:
        show wil eyes nw with dis1
        show wil eyes talking nw with dis
    else:
        show wil eyes with dis1
        show wil eyes talking with dis
    wi "\"This leads to the mines, doesn’t it?\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    show tre -surprised eyes with dis
    "I see the fox hinge his knees, lowering himself to the ground to grab something."
    show tre -eyes talking with dis
    bartre "\"Well how about you let me just show you...\""
    show tre -talking angry with dis
    play music ("music/tension.ogg")
    "It’s a baseball bat that’s in his hand."
    "He raises it behind William’s back {nw}"
    play sound ("<from 0.15>sfx/thud6.ogg")
    hide wil
    hide tre
    with hpunch

    extend "but I’m already on him."
    play sound ("sfx/thud2.ogg")
    show deepmine with dis
    "I grab the bat in his hand before his elbow slides back." with hpunch
    hide deepmine with dis4
    "The wind rushes out of my lungs as I feel myself keel over."
    play sound ("sfx/punch1.ogg") volume 0.7
    "William undercuts him in the belly and I hear him make the same sound that I just did." with hpunch
    if KaneChoice == True:
        show wil nw at halfleft,dark2 with dissolve:
            xzoom-1
    else:
        show wil at halfleft,dark2 with dissolve:
            xzoom-1
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    stop sound
    wi "\"That’s another tunnel to the mine, isn’t it?\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"How about you tell me what you use it for, hrm?\""
    if KaneChoice == True:
        show wil nw with dis1
    else:
        show wil with dis1
    hide wil with dis3
    if KaneChoice == True:
        show wil nw at halfright,dark2 with dissolve:
            xzoom-1
    else:
        show wil at halfright,dark2 with dissolve:
            xzoom-1
    stop music fadeout 5.0
    play music2 ("music/bedhorror.ogg") fadein 10.0
    "William crouches down over the man and he looks away."
    bartre "\"Nobody built it.\""
    bartre "\"It’s always been there.\""
    bartre "\"People just use it to transport stuff.\""
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    wi "\"Stuff like people?\""
    if KaneChoice == True:
        show wil eyes nw with dis1
        show wil eyes talking nw with dis
    else:
        show wil eyes with dis1
        show wil eyes talking with dis
    wi "\"Why the cots?\""
    if KaneChoice == True:
        show wil nw with dis1
    else:
        show wil with dis1
    hide wil with dissolve
    if KaneChoice == True:
        show wil nw at halfleft,dark2 with dissolve:
            xzoom-1
    else:
        show wil at halfleft,dark2 with dissolve:
            xzoom-1
    play sound ("sfx/clothrustle.ogg")
    show tre eyes br at right,dark2 with dissolve
    "The bartender rubs the bridge of his nose with his sleeve."
    show tre -eyes talking with dis
    bartre "\"People will put up with a lot to enter your country if it means they don’t have to face the boot.\""
    if KaneChoice == True:
        show wil nw with dis1
    else:
        show wil talking with dis
    show tre -talking surprised with dis
    wi "\"Like aid in murder?\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    show tre -surprised angry with dis
    wi "\"Maybe a little bit of trafficking people on the side?\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    "The fox spits on the ground."
    bartre "\"I didn’t do shit.\""
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    wi "\"You punched my friend and then tried to assault me with a baseball bat.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"If you have nothing to hide, then why go through all that?\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    bartre "\"Because you’re causing too many problems.\""
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    wi "\"This bar connects to the tunnels because you perform services for Mr. Hendricks.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"Tell me I’m wrong.\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    show tre -angry with dis
    "The fox’s ears twitch a little bit and he shuts his mouth."
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    wi "\"Surely it’s not crazy that you would?\""
    if KaneChoice == True:
        show wil eyes nw with dis1
        show wil eyes talking nw with dis
    else:
        show wil eyes with dis1
        show wil eyes talking with dis
    wi "\"A great deal of your clientele works for him after all.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"Why the secrecy if there nothing wrong?\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    "He still doesn’t talk."
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    show tre surprised with dis
    wi "\"If you’re not going to give me anything, then I’m sending you to the county jail.\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    show tre -surprised eyes talking with dis
    bartre "\"I have to work.\""
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    show tre -eyes surprised -talking with dis
    wi "\"I suppose you should have thought of that before grabbing a bat then.\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    show tre angry with dis
    bartre "\"You’re the one creating problems for everybody.\""
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    wi "\"Ignoring problems isn’t going to fix them.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"It’s just going to make things worse.\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    show tre eyes -angry with dis
    "He still doesn’t say anything."
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    show tre -eyes surprised with dis
    wi "\"You know, I think I recognize one of those toys on one of the cots.\""
    if KaneChoice == True:
        show wil eyes nw with dis1
        show wil eyes talking nw with dis
    else:
        show wil eyes with dis1
        show wil eyes talking with dis
    wi "\"They call them Lupita dolls, don’t they?\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    "A flash of concern crosses the man’s eyes."
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    wi "\"Yeah, I can tell.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"You have a daughter, don’t you?\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis

    wi "\"A young one by the look of it, if this belongs to her...\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    show tre -surprised talking with dis
    bartre "\"So what?\""
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    show tre -talking with dis
    wi "\"So why isn’t she here if her things are?\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    show tre talking with dis
    bartre "\"She’s only allowed to visit me certain times of the year.\""
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    show tre -talking with dis
    wi "\"And I’m assuming if you do what you’re told, you get to see her more often?\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    show tre eyes talking with dis
    bartre "\"...Yes.\""
    show tre -talking with dis1
    show tre talking with dis
    bartre "\"Her mother too.\""
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    show tre -eyes -talking with dis
    wi "\"I see.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"And when’s the last time you’ve seen either of them?\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    show tre talking with dis
    bartre "\"Almost nine months.\""
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    show tre -talking with dis
    wi "\"Any letters?\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    show tre talking with dis
    bartre "\"No.\""
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    show tre -talking with dis
    wi "\"And that’s not strange to you?\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    show tre eyes talking with dis
    bartre "\"Could mean anything.\""
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    show tre -eyes -talking surprised with dis
    wi "\"Doesn’t look good though does it?\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    "Pain flashes across the man’s face."
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    wi "\"What’s your name?\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    show tre talking with dis
    tr "\"People call me Trey.\""
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    show tre -talking with dis
    wi "\"Looks to me like you have a bad deal.\""
    if KaneChoice == True:
        show wil eyes nw with dis1
        show wil eyes talking nw with dis
    else:
        show wil eyes with dis1
        show wil eyes talking with dis
    show tre -surprised with dis
    wi "\"How about if you help me instead of helping Mr. Hendricks, not only will I forget about this incident with the baseball bat...\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"But I’ll help you look into what’s going on with your wife and kid too.\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    show tre talking with dis
    tr "\"Sounds too good to be true.\""
    if KaneChoice == True:
        show wil eyes talking nw with dis
    else:
        show wil eyes talking with dis
    show tre -talking with dis
    wi "\"Let’s just call it blow for blow.\""
    if KaneChoice == True:
        show wil nw with dis1
        show wil talking nw with dis
    else:
        show wil with dis1
        show wil talking with dis
    wi "\"Can you show me how this tunnel connects to the Hendricks manor?\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    show tre eyes talking with dis
    tr "\"There’s several ways.\""
    if KaneChoice == True:
        show wil surprised nw with dis
    else:
        show wil surprised with dis
    show tre -eyes -talking with dis
    wi "\"Several ways?\""
    show tre talking with dis
    tr "\"Yeah, but only one that we use.\""
    if KaneChoice == True:
        show tre -talking
        show wil nw
        with dis1
    else:
        show tre -talking
        show wil
        with dis1
    show tre talking with dis
    tr "\"One way’s been out of order for a long time.\""
    show tre eyes -talking with dis1
    show tre talking with dis
    tr "\"Parts of it are broken.\""
    show tre -eyes -talking with dis1
    show tre talking with dis
    tr "\"Not too practical for hauling consumptives.\""
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    show tre -talking with dis
    wi "\"I presume you don’t just mean alcohol.\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    show tre eyes talking with dis
    tr "\"There’s some of that.\""
    show tre -talking with dis1
    show tre talking with dis
    tr "\"But also stronger things for sure.\""
    show tre -eyes -talking with dis1
    show tre talking with dis
    tr "\"Usually people with badges like yours aren’t immune to that sort of thing...\""
    if KaneChoice == True:
        show wil eyes talking nw with dis
    else:
        show wil eyes talking with dis
    show tre -talking with dis
    wi "\"Not interested.\""
    if KaneChoice == True:
        show wil surprised nw with dis
    else:
        show wil surprised with dis
    show tre talking with dis
    tr "\"Somewhat surprising if you’re willing to walk off into the night with Kane.\""
    show tre -talking with dis
    wi "\"You know Kane?\""
    if KaneChoice == True:
        show wil eyes talking nw with dis
    else:
        show wil eyes talking with dis
    wi "\"I suppose you would if he’s a regular.\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    show tre talking with dis
    tr "\"Kane’s not his real name, but yeah...\""
    show tre eyes -talking with dis1
    show tre talking with dis
    tr "\"We go way back.\""
    show tre -eyes -talking with dis1
    if KaneChoice == True:
        show wil frustrated nw with dis3
        wi "\"I’m more concerned with the size of the bruise I leave on his ass the next time I see him than his name.\""
        wi "\"Motherfucker stole our clothes.\""
        show wil surprised nw with dis3
        show tre talking with dis3
        tr "\"...That all?\""
        show tre -talking surprised with dis
        show wil nw with dis
        "William gives him a severe look."
        show wil talking nw with dis
        wi "\"Gonna pretend I didn’t hear that.\""
        show tre -surprised with dis
        show wil nw with dis
    show tre talking with dis
    tr "\"Dunbar likes to take risks.\""
    show tre eyes -talking with dis1
    show tre talking with dis
    tr "\"I keep waiting for him to lose big, but it doesn’t seem to happen.\""
    show tre -eyes -talking with dis1
    show tre talking with dis
    tr "\"I wouldn’t be alive if I took risks like that.\""
    show tre -talking with dis1
    show tre talking with dis
    tr "\"Says something about him that he does.\""
    if KaneChoice == True:
        show wil talking nw with dis
    else:
        show wil talking with dis
    show tre -talking with dis
    wi "\"Does he work for Hendricks too?\""
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    show tre talking with dis
    tr "\"The only one he works for is himself.\""
    show tre eyes -talking with dis1
    show tre talking with dis
    tr "\"But if he knows it gets under your skin, he would.\""
    show tre -eyes -talking with dis1
    if KaneChoice == True:
        show wil frustrated nw with dis3
    else:
        show wil frustrated with dis3
    wi "\"Great.\""
    if KaneChoice == True:
        show wil nw with dis3
    else:
        show wil with dis3
    show tre talking with dis3
    stop music fadeout 6.0
    tr "\"Why don’t we start today over?\""
    show tre -talking with dis1
    show tre talking with dis
    tr "\"I’ll make you and your man a drink.\""
    if KaneChoice == True:
        show wil surprised nw with dis
    show tre -talking with dis
    "Me and William look at one another."
    if KaneChoice == True:
        show wil nw with dis
    else:
        show wil with dis
    "Silently we agree it’s best not to ask what he means there."
    "Considering the nature of his business, I figure he’s seen plenty how men act around one another in the middle of the desert without many women around."
    "I think we’re just not used to somebody being so casual about it, if he’s saying what he’s sayin’."
    "Then again, what should we expect from a man who knows Kane Dunbar well?"



else:
    show wil surprised with dis
    ni "\"William?\""
    hide wil
    hide tre
    with dissolve
    show nik at right,stagday with dissolve
    show wil surprised at left,stagday with dis3:
        xzoom-1
    wi "\"Nik?\""
    show wil talking with dis
    wi "\"You’re here early, aren’t you?\""
    show wil with dis
    show nik talking with dis
    ni "\"You were looking to wait for me here?\""
    show nik -talking with dis
    show wil eyes talking with dis
    wi "\"Well, yes.\""
    show wil with dis1
    show wil talking with dis
    wi "\"But shouldn’t you be working right now?\""
    show wil with dis1
    show nik disappointed with dis3
    ni "\"Things at the company are not going so well.\""
    ni "\"It is not worth talking about, but it also means more time away from the site.\""
    show nik -disappoineted with dis3
    "I frown."
    m "\"You’re struggling then?\""
    show nik surprised with dis3
    "His gaze moves over to me and his eyes widen."
    ni "\"You are here too, Sam?!\""
    m "\"Feels like I’ve sort of become William’s shadow in the last few days.\""
    show nik sidelook with dis3
    ni "\"I have noticed.\""
    show nik disappointed with dis3
    "Nikolai sighs."
    ni "\"Please do not worry about me, Samuel.\""
    ni "\"Finding work has never been difficult for me...\""
    ni "\"This job always had an expiration date.\""
    ni "\"I fear it just happening sooner than I had expected it to.\""
    show nik -disappointed with dis3
    show wil talking with dis3
    wi "\"How would you feel about doing as much damage as you can before they force you out?\""
    show wil with dis
    show nik eyes with dis
    "Nikolai {nw}"
    show nik -eyes with dis
    extend "blinks."
    show nik talking with dis
    ni "\"It depends upon what you mean by that.\""
    show nik sidelook with dis3
    ni "\"There are people I’m fond of who still work there.\""
    show nik -sidelook with dis3
    show wil talking with dis3
    wi "\"It shouldn’t do much to the company itself.\""
    show wil eyes with dis1
    show wil eyes talking with dis3
    wi "\"Just the management.\""
    show wil with dis
    show nik talking with dis
    ni "\"When problems happen to management, it usually affects us anyway.\""
    show wil talking with dis
    show nik surprised with dis
    wi "\"I think they’re murderers, Nik.\""
    show wil with dis
    ni "\"That is a serious accusation William...\""
    show nik sidelook with dis3
    ni "\"...But if you believe it, you probably have some proof.\""
    show wil eyes talking with dis
    wi "\"I do.\""
    show wil with dis1
    show wil talking with dis
    wi "\"I need somebody who knows how the tunnels underground connect to the Hendricks manor.\""
    show wil with dis
    ni "\"You think that they do?\""
    show wil talking with dis
    wi "\"That pretty much has to be the case.\""
    show wil with dis1
    show nik disappointed with dis3
    "Nik looks like he’s thinking hard."
    ni "\"I know somebody who would know.\""
    show nik talking with dis3
    ni "\"You are in luck too. They’re here right now.\""
    show nik -talking with dis
    show wil talking with dis
    wi "\"I’d appreciate if you could introduce us.\""
    show wil with dis1
    show nik sidelook with dis3
    ni "\"Follow.\""
    "The badger trots off to the wooden stairs that lead to the loft up above and{nw}"
    play sound ("sfx/creak1.ogg")
    hide nik with dis3
    extend " starts to climb."
    hide wil with dis3
    play sound ("sfx/creak2.ogg")
    "Will takes a brisk pace when he climbs up behind him."
    "I’m the last to ascend."
    stop sound
    scene bg stagloftback with dis3
    "The loft looks a lot less cozy when there isn’t gentle lighting to soften the hard wood."
    show yao casual sidelook crossed at left,stagday with dis3:
        xzoom-1
    "A tiger sits on a crate, sitting beside a burlap sack he has his paw over."
    show nik at halfright,stagday with dissolve
    show wil at stagday with dissolve:
        xpos 0.6
        yalign 1.0
    show wil talking with dis
    wi "\"He the guy?\""
    show wil with dis
    show yao -sidelook angry -crossed with dis3
    "The tiger uncrosses his arms and his eyes turn to slits."
    if ETHINT_Points == 0 and HARINT_Points == 0:
        show yao teeth with dis3
        show nik surprised with dis3
    ya "\"Nik, what is this?\""
    if ETHINT_Points == 1 or HARINT_Points == 1:
        show nik talking with dis
        ni "\"I believe I introduced you before briefly, but this is Sheriff Adler and Sam Ayers--\""
        show nik -talking with dis
    else:
        show nik disappointed with dis3
        ni "\"This is Sheriff Adler and Sam Ayers--\""
        show nik surprised with dis3
    show yao angry crossed with dis3
    "He crosses his arms again."
    ya "\"I know who he is.\""
    ya "\"Why would you bring this to me today?\""
    if ETHINT_Points == 0 and HARINT_Points == 0:
        show nik -surprised with dis3
    show wil sideeyes with dis3
    wi "\"I don’t mean any trouble.\""
    show yao -angry with dis
    wi "\"We need some help.\""
    show wil with dis3
    "The tiger’s shoulders are still stiff."
    show yao talking with dis
    ya "\"Help regarding what?\""
    show yao -talking with dis
    show nik talking with dis
    ni "\"He needs help with the tunnels.\""
    show nik -talking with dis
    show wil talking with dis
    wi "\"If you could show me where the subterranean systems lead to the Hendricks manor, it would be a lot of help.\""
    show wil with dis
    ya "\"Hmmph.\""
    show yao talking with dis
    ya "\"If that is all you want, that would be easy.\""
    show yao eyebrows with dis
    ya "\"But why would you need to know such things?\""
    ya "\"You have free access to the road.\""
    show yao -talking with dis
    show wil talking with dis
    wi "\"I just need to know all of the places a person could feasibly enter and exit the manor.\""
    show yao -eyebrows with dis
    show wil with dis
    "He shrugs, then clasps his paws."
    show yao talking with dis
    ya "\"Very well.\""
    show yao -talking with dis1
    show yao talking with dis
    ya "\"I have a map I could draw for you.\""
    show yao -talking with dis1
    show yao talking with dis
    show wil surprised with dis
    ya "\"And there is an entrance point here that leads to the house easily enough.\""
    show yao -talking with dis
    wi "\"...Here?\""
    show yao talking with dis
    ya "\"There is a trapdoor to a cellar beneath the bar...\""
    show yao -talking with dis1
    show wil sideeyes with dis3
    wi "\"I spotted that before I came in.\""
    show wil talking with dis3
    wi "\"It’s beneath the blue rug, isn’t it?\""
    show wil with dis
    "The tiger nods."
    show yao talking with dis
    ya "\"Yes.\""
    show yao -talking with dis
    show wil talking with dis
    wi "\"Will the bartender give me trouble if I ask to use it?\""
    show wil with dis1
    show yao sidelook with dis3
    ya "\"He is compromised, but he is not above mutual assistance.\""
    show yao talking with dis3
    ya "\"Getting to know him better would be helpful if you wish to use this location as an access point without informing your enemies.\""
    show yao -talking with dis
    show wil eyes talking with dis
    wi "\"Thank you, Mr. Yao...\""
    show wil with dis
    show yao talking with dis
    ya "\"Thank him.\""
    show yao -talking with dis
    "The tiger jerks his head to Nik."
    show yao talking with dis
    ya "\"I only trust who he trusts, and I owe him favors.\""
    show yao sidelook with dis3
    ya "\"He has saved my life many times.\""
    show nik disappointed with dis3
    ni "\"As have you.\""
    ya "\"Well...\""
    show yao talking with dis3
    show nik -disappointed with dis3
    ya "\"A map is a small thing comparatively.\""
    show yao -talking with dis1
    show yao talking with dis
    ya "\"Lucky for you I have something on me.\""
    show yao -talking with dis1
    show yao talking with dis
    ya "\"But I could make it easier to read for you.\""
    show yao -talking with dis
    show nik eyestalking with dis
    ni "\"You should go warm up to the bartender while he writes this down for you.\""
    show nik -eyestalking with dis
    show wil eyes talking with dis
    wi "\"I don’t exactly warm up to people too quickly.\""
    show wil with dis
    show nik smile with dis
    ni "\"Sam should help.\""
    show yao eyebrows with dis
    m "\"We need to get friendly with him, not fuck him.\""
    show wil talking with dis
    wi "\"S’pose it’s time to put on.\""
    show wil smile with dis
    wi "\"Get ready to work that charm, sunshine.\""
    "I roll my eyes, following William toward the ladder, waiting for him to descend first."
    scene stag
    show tre br at right,stagday
    with dissolve
    show wil at left,stagday with dis3:
        xzoom-1
    "When we get back to the bar, it seems like he’s been waiting for us."


if KaneChoice == True:
    show wil talking nw with dis
else:
    show wil talking with dis
wi "\"Alright barkeep.\""
if KaneChoice == True:
    show wil eyes nw with dis1
    show wil eyes talking nw with dis
else:
    show wil eyes with dis1
    show wil eyes talking with dis
wi "\"How about you give us a shot of whiskey each?\""
if KaneChoice == True:
    show wil nw with dis1
else:
    show wil with dis1


scene black with slow_dissolve
"To be continued..."
window hide
scene credits with slow_dissolve
pause
scene credits2 with slow_dissolve
pause
scene black with slow_dissolve
