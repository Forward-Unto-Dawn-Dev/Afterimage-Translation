label af5_main:
    play music interlude fadein 3.0
    scene white with MultipleTransition([
        False, Dissolve(1.0),
        act5, Pause(4.0),
        act5, Dissolve(3.0),
        True])
    scene white with dissolve
    play ambient ext_night volume 1.5 fadein 2.0
    "The projector lights from high above penetrate through the taxi's window, into my delicate eyesight. The burning luminance makes it hard to stare at them."
    "On the runway, there's a plane adjusting its pose with signals shining all over the body."
    stop ambient fadeout 3.0
    play ambient airport fadein 1.0 volume 0.15
    scene bg airport_day with Dissolve(1.5)
    "I take out our luggage, after going through various instructions, we sit down in the waiting hall."
    "A giant screen is hanging down from the ceiling, showing all kinds of numbers in red and green."
    "Compared to the darkness outside, the hall is a lot brighter."
    "And warmer, too."
    "There are few people to be seen at this minute,"
    "there is one that is sleeping on the bench with his coat covered up his body, and some are staring at their cellphones while the rest just lay out their rushing breakfast on their laps, wolfing it down."
    "Anxious yet wordless footsteps run past me, dragging their suitcases behind, among the emotionless female voice that echoes in the hall."
    stop music fadeout 2.0
    show sayori curious1 dd at t11
    s "When's our flight?"
    show sayori curious1 dd at t22
    pause(0.5)
    show sayori curious1 dd at s22
    pause(0.3)
    "Sayori sits next to me, dangling her feet back and forth."
    mc "Let's see……"
    mc "about forty-four… forty-five minutes."
    "I quickly calculate it."
    show sayori sleepy4 ud
    pause(1.0)
    show sayori sleepy3 ud
    pause(0.8)
    show sayori sleepy2 ud
    pause(1.0)
    show sayori sleepy1 dd
    pause(0.8)
    s "Ahhh--------------"
    play music Around fadein 4.0
    show sayori sleepy1 dd at sink_more(x=880)
    "She lets out a long yawn, falling to my body."
    show sayori sadsmile1 dd
    s "I'm so happy, [player]."
    mc "Emhmm?"
    show sayori sadsmile2 du
    s "We can all be together again…… ahaha………"
    show sayori sadsmile8 dd at sink_more2(x=880)
    s "It almost…"
    s "{i}{cps=*0.2}Almost feels like a dream.{/cps}{/i}"
    s "Eh, I'm gonna take a nap, remember to wake me~~"
    mc "I will."
    show sayori peace2 dd at sink_hide(x=880)
    "I mildly nod."
    scene cg arm with dissolve
    $ persistent.cg12 = True
    "I hold her tiny hands as I watch her weakly closing her tired eyelids. Her sleepy bow dozes off to the side, and her body faints along with it."
    "I gently stroke her hair, winding them behind her ears."
    "The second hand of the clock clicks and clicks. We stay like this for nobody knows how long, until I eventually hear that emotionless voice calling our number."
    scene bg airport_day with Dissolve(2.0)
    mc "Wakey wakey……"
    "I shake her body, she slowly opens her eyes."
    show sayori nsleepy1 dd at t11
    pause(1.0)
    show sayori nsleepy2 dd
    pause(1.5)
    show sayori nsleepy1 dd
    pause(0.5)
    mc "It's our turn."
    show sayori nsleepy4 uu at focus(x=640, z=0.85, t=1.0)
    s "Ah-------------"
    show sayori nsleepy4 uu at t11
    "She leaves my laps, stretching in relaxation."
    show sayori nsmile10 dd at f11
    s "What a comfortable sleep."
    "Her eyes are still weary, I could still feel her limp body."
    show sayori npeace3 dd at t11
    pause(0.8)
    show sayori nsmile10
    pause(1.0)
    show sayori nsmile4 dd at f11
    s "I've had a dream."
    show sayori nsmile4 dd at t11
    mc "Tell me about it."
    show sayori nsmile8 ud at f11
    s "We went to dig that time capsule, plants were thriving there, and the trees…"
    show sayori ncurious3 uu
    s "they were so tall!"
    show sayori nsmile3 ud at t11
    s "Took me a while to find that very spot, various flowers were growing under that giant tree, with all kinds of colors. Well, I still prefer the blue ones…"
    show sayori ncurious3 du at h11
    s "And you brought that shovel over, preparing to strike the earth with full force."
    show sayori nsadsmile9 dd at s11
    s "I have to say, I was hesitating for a moment."
    mc "Hesitating for what?"
    show sayori nsadsmile7 dd
    s "Because I hate to destroy those lovely flowers…"
    show sayori nsadsmile7 dd at sink_more(640)
    "She's gazing into another world."
    show sayori nawkward2 dd at tcommon2(640)
    s "But I also reeeaally wanted to see what we wrote, so I just left you to it."
    show sayori nsmile1 ud at t11
    s "Then it was dug out, but it looks so new, even newer than when we buried it, without any dust on it."
    show sayori nsmile8 uu at f11
    s "It was black, shiny, with a keyhole on it."
    show sayori nsmile8 uu at t11
    mc "A keyhole?"
    show sayori nsmile1 dd at f11
    s "Yeah, and we went to pick the key up in that lake."
    show sayori ncurious9 uu
    s "And um… I suddenly heard you screaming with an ‘OUCH!', then I looked at you, there was a bruise on your face."
    show sayori nserious1 uu
    s "And then… then was that lake."
    s "The lake… umm………"
    s "{cps=*0.3}uwwwwwwwwwwwwwwwwwwwwwwww………{/cps}"
    show sayori nserious5 du
    s "There was something…… or someone… on the lake, I don't quite remember…… "
    show sayori nserious4 dd
    s "Nonetheless, we opened that box."
    "We walk to the entrance, I take out my prepared two tickets and hand them over to the ticket collector."
    play ambient plane1 fadein 1.0 volume 0.2
    scene bg plane with dissolve
    "Sayori keeps describing that dream of hers as we walk through the hallway."
    show sayori nsmile5 uu at t11
    s "There was a lot of food besides our two letters!"
    show sayori nsmile2 uu at f11
    s "And Nasuki, Yuri, Monika they all came over, we hugged and laughed. Everybody was having a cheerful chat! And we decided to picnic there."
    show sayori nsmile1 dd at t11
    mc "Then?"
    show sayori nserious1 ud at f11
    s "Then we headed to the…"
    show sayori nserious5 ud at t11
    pause(0.7)
    show sayori nangry15 ud
    pause(1.0)
    show sayori nserious5 ud
    pause(0.5)
    s "To the…… Err…"
    pause(1.0)
    show sayori nserious5 uu at h11
    s "There! The...! Eh, it's there…!"
    show sayori nsurprise1 uu at f11
    s "Gosh why is this so hard to remember!"
    mc "Hahahah, dreams are all like that. They start and they end, out of the blue."
    scene black with dissolve
    "She's still working hard on remembering that dream, which brings me to think as well."
    "Monika…… How should I face her when we meet……"
    scene cg plane with Dissolve(2.0)
    $ persistent.cg13 = True
    "I look at the side of her face, she's sitting by the window, we have already reached the stratosphere as the clouds under the wings are all painted orange by the morning sunshine."
    "The bright light of the rising sun spills onto her cheek, drawing a magnificent golden line on her smile within her fleeting feelings."
    scene cg plane2 with dissolve
    $ persistent.cg14 = True
    s "Oh! I remember it!"
    s "We headed fifteen meters west, into the mid-lake's {cps=*0.2}..................{/cps}{nw}"
    scene black with dissolve
    play ambient plane2 volume 0.3 noloop
    "The roaring of the engine streams in endlessly. Beyond that hovering skyline, our long-lost reunion is waiting for us."
    "Plane leaves unpredictable trails in the sky, carrying us to the other side of paradise."
    "The steam on my ears gets wiped out as the ground outside the window clarifies."
    stop music fadeout 5.0
    "Regular rooftops are divided by thin and straight roads, the different districts becoming easy to tell. We fly by above the city, smoothly landing on the runway."
    play ambient airport2 fadein 1.5 volume 0.5 loop
    "Stepping out the plane door, the engine's humming declines behind our back."
    "We flood into the hall with crowded people----looks like it's the rush hour."
    mc "Sayori!"
    s "Huh?!"
    mc "Stay close to me!"
    s "OK!!"
    stop ambient fadeout 3.0
    "We grab our luggage and walk out of the giant glass wall of the airport."
    scene bg airport2 with dissolve
    play ambient wind volume 1.2 fadein 2.0
    mc "We're here."
    "I turn around to take a picture of the name that stands high above the rooftop before sending it to the groupchat."
    "They don't reply immediately though."
    "Still on the plane, I guess."
    play music keepcalm fadein 3.0
    show vignette_white with dissolve
    mc "Huuuuuu!~~~"
    hide vignette_white with Dissolve(2.5)
    "Just then I feel the freezing air around me."
    "This is the north…"
    "Micro ice shards float down from the sky piece by piece, laying the white onto all the cars going in and out."
    "People are standing by the curb with solid clothes covering them, and their severely lowered brims."
    show sayori nsmile7 dd at t11 with Dissolve(2.0)
    "I look at Sayori, a chill suddenly gets sent down my spine."
    show sayori ncurious1 dd
    mc "Aren't you cold?"
    show sayori ncurious6 ud at f11
    s "I'm not, what's the matter?"
    show sayori nserious1 ud at t42
    "She's reaching out to get those snowflakes, like a kid walking into a candy shop."
    show sayori nlaugh3 uu at h42
    s "I could finally make a snowman!!!!"
    show sayori nsmile1 dd
    mc "Let's go to the hotel and settle down first, then you can go wherever you want."
    stop ambient fadeout 2.0
    scene bg cab with dissolve
    play ambient cab
    "We're like two real tourists, spacing out on the touring guide map."
    show sayori nsmile1 dd at t50
    mc "I suppose this is your first time taking a plane."
    show sayori nsmile1 dd at t22
    "I lean back against the backseat of the cab comfortably."
    show sayori nsmile3 du
    s "Yeah."
    "Her eyes are fixed on the silver city outside."
    show sayori nreluc15 du
    s "When was the last time we traveled together?"
    mc "I don't think there is any…"
    "I would love to find such a circumstance in my memory, but unfortunately…"
    "It just doesn't exist."
    show sayori nreluc2 dd at s22
    s "Is that so……"
    show sayori nserious2 dd at t22
    mc "Nah, it's nothing, we can enjoy this one at least."
    mc "I browse through the pamphlet in my hand."
    mc "{cps=*0.5}Where do you want to go first? {/cps}{nw}"
    play sound ding2
    pause(2.0)
    show sayori ncurious1 ud at f22
    s "Nat?"
    show sayori ncurious1 ud at t22
    mc "Let me see…"
    "I take out my phone."
    pause(2.0)
    show sayori nserious4 ud
    mc "Nope, it's just a garbage mail."
    "Natsuki and Yuri stay silent."
    play sound airbrakes
    hide sayori with dissolve
    stop ambient fadeout 1.0
    "Tires scratches the ground, pushing my body forward."
    stop music fadeout 4.0
    scene bg hotel with dissolve
    "We stop in front of the hotel."
    "I take out my suitcase from the trunk, and make my way inside the hotel with Sayori."
    scene bg bedroom2 with dissolve
    play ambient int_day fadein 1.0 volume 1.2
    show sayori ncurious6 ud at t11
    s "Why did you order a twin room."
    mc "There are two of us, anything wrong?"
    show sayori nreluc11 dd at s11
    s "But I……"
    "Her eyes are sweeping on the ground back and forth."
    show sayori nworried3 du
    s "You don't have to bother…… didn't you say you……"
    show sayori nreluc10 dd at sink_more(640)
    s "This is unnecessary money."
    show sayori nworried3 dd
    mc "That's fine, we don't get the chance all the time."
    "I throw my backpack away and lay down on the bed."
    hide sayori with dissolve
    show layer master:
        blur 0
        easein .25 blur 30
    "Soft mattress bounces me up before cuddling me in."
    pause 2.0
    mc "Ahhh-----------"
    "I stretch."
    pause 2.0
    show layer master:
        blur 30
        easein .25 blur 0
    mc "Sayori."
    show sayori nserious4 ud at t11
    s "Emmhmm?"
    mc "I wanna ask you something. "
    show sayori ncurious1 ud at f11
    s "Say it then."
    show sayori ncurious1 ud at t11
    mc "Let's say we do find Monika."
    show sayori nworried3 ud
    mc "Wha……{w}What should we say to her?"
    show sayori nworried3 dd
    pause(1.0)
    show sayori nreluc16 dd
    pause(0.8)
    show sayori nworried3 dd at f11
    s "Do I have to answer that question?"
    show sayori nworried3 dd at t11
    mc "Err… you don't have to if you…"
    show sayori nreluc16 dd at s11
    mc "Nah, I'm just asking myself, really."
    show sayori nsadsmile1 dd at t11
    pause(0.7)
    show sayori nsmile2 uu at f11
    s "We could just chat. We can talk about high school, about their lives, and we go somewhere to play!"
    show sayori nsmile1 dd
    s "Like it's always been."
    show sayori nsmile1 dd at t11
    mc "Sayori……"
    "I smile at the bush viper twining around her body bittersweetly."
    mc "I wish I were you, but you have to……{nw}"
    play sound ding2
    hide sayori with dissolve
    "I take out my phone, suppressing the anger within."
    "Don't tell me it's another garbage mail."

    call phone ("Natsuki, Yuri, Sayori(3)", group_messages, 561, 17, hide_phone=False) from _call_phone_18

    show sayori nlaugh3 uu at t22
    s "They're here!"
    show sayori nsmile8 dd at f22
    s "Hurry!"
    show sayori nsmile8 dd at t22
    mc "OK,OK…"
    call hide_phone
    pause(0.5)
    hide sayori with dissolve
    "I lift my backpack and walk towards the door."
    show sayori nsurprise1 uu at h11
    s "I didn't mean that!"
    mc "Huh?"
    show sayori nmock7 ud at f11
    s "You tell them to send a selfie!"
    show sayori nmock7 ud at t11
    "She said as she giggled."
    show sayori nmock7 ud at t21
    mc "Oh you…"

    call phone ("Natsuki, Yuri, Sayori(3)", group_messages, 578, 3, hide_phone=False) from _call_phone_19

    "Natsuki's questioning me with her emojis, but after a while, she sends a photo over."

    call phone ("Natsuki, Yuri, Sayori(3)", group_messages, 582, 1) from _call_phone_20

    scene cg selfie with dissolve
    $ persistent.cg15 = True
    s "Ehehe~~ Hurry and save it."
    mc "Sayori oh Sayori… I didn't know you were this kind of person."
    "It's a bit funny to save others' selfie."
    "Almost make me feel like a weirdo."
    "But……"
    "No point thinking into it too much, I did it as she says."
    scene black with dissolve
    stop music fadeout 5.0
    "After the short interlude, we head off towards Monika's college."
    pause 3.0
    play ambient schoolcrowd fadein 1.0 volume 0.3
    scene bg schoolgate2 with dissolve
    "And here I thought every one of her colleges had to be that weird."
    "Guess not."
    "The one that stands before me, is totally different from the previous one."
    "People come and go, along with their chatting and laughter."
    play music ghost fadein 1.0
    show sayori nlaugh2 uu at t11
    s "I can't wait to say hello to her roommates~"
    show sayori nsmile1 uu
    mc "What're you talking about? We are not going to go to her dorm."
    show sayori ncurious6 du at f11
    s "Where then?"
    show sayori ncurious6 du at t11
    mc "The lab of course! It's class time. And that report mentioned about her tutor as well, so it's convenient for us."
    hide sayori with dissolve
    "I find out the picture that I took earlier, matching it with the map."
    "I have to say, although the goal is clear, this college is incredibly huge."
    "It takes us a long walk before we finally reach the very science building."
    play ambient int_day volume 1.2 fadein 2.0
    scene bg stair1_day with dissolve
    "Spotless stairs reveal themselves before us, our destination of this trip lies beyond the sixth corner."
    "Splitting our legs, we step on them steadily."
    play sound ring1 volume 0.3 loop
    "Suddenly, my phone starts to ring."
    "It's Natsuki calling."
    $ n_name = "Natsuki"
    play sound ring2 volume 0.3 noloop
    n "Hello?? … Is this [player] speaking?"
    "She sounds breathless."
    n "Where you at? We're inside the college now."
    mc "NO. 5 science building, AI laboratory on the third floor."
    "My heart's beating fast, I almost throw the words out."
    n "You found her?"
    mc "She should be inside the lab."
    n "That's great! …Yuri! Take a look at where we are! ……"
    n "…"
    n "It's close! Hold there, we're coming!!"
    play sound ring2 volume 0.3
    pause 0.7
    play sound ring2 volume 0.3
    pause 0.7
    play sound ring2 volume 0.3
    pause 0.7
    show sayori nsmile5 dd at t11
    s "{size=-5}Hehe....................{/size}"
    mc "What's so funny?"
    show sayori nmock7 ud at f11
    s "When we get up there, I'll go hide. You can talk with them once they arrive, and I'll jump out to give them a heart-attack!!!"
    show sayori nmock9 uu
    s "I'll give you a code, when you feel like it's the right time, just say ‘Sayori! Use splash!', and that's when I'll strike!"
    show sayori nmock9 dd at t11
    mc "Is this fine with Natsuki? You'll scare her."
    show sayori nsmile2 ud at f11
    s "Like I said before, she's not that timid."
    mc "Huhuh… Alright then."
    scene bg stair2_day with dissolve
    pause(0.5)
    scene bg corridor2_day with dissolve
    "We reached the third floor just when we finished our talk."
    "A few more steps in, we find ourselves a door, labeled as ‘AI Laboratory'."
    scene cg lab1 with dissolve
    $ persistent.cg16 = True
    "I compare it with the photo on my phone."
    scene bg corridor2_day with dissolve
    show sayori nsmile3 dd at t11
    mc "Seems like we've hit the jackpot."
    show sayori nsadsmile2 ud at f11
    s "Ehehe~ Then I'll see you later~~!"
    s "Don't forget what we told you~"
    show sayori nsadsmile2 dd at t11
    stop music fadeout 4.0
    hide sayori with Dissolve(4.0)
    "She smiles at me for the last time, then disappears behind the corner of the hallway."
    pause(2.0)
    play sound doorknock
    pause(2.0)
    mc "Hu----------"
    "Staring at that metal label on the door. I take a deep breath to ease the sound of my heartbeat."
    "I look down to tidy up my clothes as well."
    "Monika……………"
    pause(3.0)
    play sound closet_open
    "The door is open."
    show dr at t11
    "An old man step out the door with his glasses on, clutching some files against his chest."
    randomperson "Who are…"
    mc "Hello! You must be Dr. Marx right? I'm looking for Monika."
    dr "Monika…?"
    "He blinks, I can see that the confusion still stays there."
    mc "Yes. Isn't she your assistant at the AI lab?"
    dr "Huh…?"
    "He seems quite surprised, he adjusts the files in the arms to assure their stay."
    dr "I think you've mistaken it, my dear. This is the office of the Psychology Major, and as far as I know, we don't have an AI major in this university…"
    pause(2.0)
    "What? ……"
    "I startle, I take a second look at the metal label."
    scene cg lab2 with dissolve
    $ persistent.cg17 = True
    "'Office of Psychology Major'"
    mc "But……"
    scene bg corridor2_day with dissolve
    "I anxiously take out my cellphone, trying to confirm that picture."
    "But it is nowhere to be found."
    "Am I getting a virus?"
    "Oh, right! Didn't I send this to the group chat earlier? I'll just check the chat record."
    "So I switch to the chat app."
    pause(2.5)
    "The record is not even there…"
    "I directly search for her name in the list as my heart was beating faster and faster."
    "I didn't add her, she's not in my list."
    "Nor did Yuri, and that group chat… they're vaporized like the dew under the mid-noon, as if they have never existed."
    pause(2.0)
    "Oh!"
    "The call records!"
    "Didn't we just talked on the phone."
    "Hah, stupid me."
    "I'll just call her again."
    "......"
    "Listening to the background music while waiting for her to pick up makes me calm down a little."
    "Did they get lost?"
    "Nah, they should be here any seconds now."
    pause(1.0)
    "\"You have reached the wrong number.\""
    "\"Please hang up and try again. •beep• •beep•\""
    show dr at t11
    dr "It's getting late, my dear, I'm going to head home, what if you……"
    stop ambient
    play music richard
    scene bg corridor2_night
    "I look outside, the sky is tainted by deep purple as the lights around the building and the campus all start to turn off."
    "I'll ask Sayori, this is probably one of her pranks I suppose."
    mc "Sayori!!!"
    pause(2.0)
    mc "SAYORI!!!!!!!!!"
    "No response."
    "Suddenly some footsteps come out from the stairs."
    mc "Wait, my friends are here, let me ask them."
    scene bg stair2_night with dissolve
    "I run there, full speed."
    "A student with his glasses on has made his way up to me, who's also looking at me in confusion."
    show student at t11
    randomperson "Dr. Liu!!!"
    randomperson "Still here at this hour?"
    show dr at t22
    dr2 "Oh, I was just about to leave… "
    dr2 "by the way…… Do you know a Monika?"
    randomperson "What's the matter? Who's Monika?"
    dr2 "Emm…… that student is looking for her I guess… But I think he has come to the wrong place."
    scene bg corridor2_night with dissolve
    "I speed up, dash to the corner of the hallway, Sayori should've hide here."
    "But it's nothing there. The corner turns, expands, and turns again, disappearing into the darkness of the cold winter."
    show student at t22
    randomperson "I don't think I know her. Who's him? And Who's Monika?"
    show dr at t33
    dr2 "I don't………"
    mc "Sayori! Use splash!!!!!!"
    pause(2.5)
    "But nothing happened."
    stop music fadeout 5
    "That old man starts to take out his phone."
    show layer master:
        blur 0
        easein 2.0 blur 0.4
    "I see that student fades like tides retreating from the beach, leaving the wet sand behind."
    "My thigh shakes, one step, two step, I'm going backwards."
    "I step on a delicate petal. Suddenly, an arching root trips me over, I fall down to the moist soil."
    scene cg lake1 with dissolve
    $ persistent.cg18 = True
    "Fog crawls in, blur everything into the ear-ripping silence. Mountains quake, skies shatter. Storm is tearing my body apart."
    "I see leaves swallowing insults on their branches, I see trees cracking, sky flashing, I see the lightning and the thunder, but without a single sound, as if I was watching a pantomime."
    "Heavy snow rolls into the forest after piercing through the fog, yet gets picked up by the wind within seconds, battering between the shadows of trees, despising all the rules and orders."
    "Ice slices my face open like sharp blades, my ears are frozen, my consciousness grows numb."
    "A narrow path is divided out among this chaos, showing the hard-frozen ice cap on the lake."
    scene cg lake2 with dissolve
    $ persistent.cg19 = True
    "The biggest tree can no longer bear the storm's torture. With the cracking of its head, it falls to the lake. Smashing the ice cap open, sinks into the freezing water."
    scene cg lake3 with Dissolve(2.0)
    $ persistent.cg20 = True
    "Surrounded by frost, a piece of circle black takes the view of middle lake."
    scene cg lake4
    $ persistent.cg21 = True
    "Lightnings that descends from the celestial, they assemble by the edge of the black, flows into its depth."
    "Blocks and blocks of ice float up from the water. "
    "I stare at it, at the clarified black. It is invisible, but nothing can be seen behind it. My eyes are severely grabbed, downwards, forwards, into the abyss of that circle."
    "I mindlessly stand there, that's when a string of warm wind escapes from the troop, whispering gently by my ears."
    "Drowsiness strikes, I try to take a step forward."
    "I step onto the water. Chill ripple holds me."
    "Up and down, my eyes are gradually warmed by mysterious words."
    "Then I take another firm step."
    "{cps=*0.3}I head fifteen meters west, into the mid-lake's blackness.{/cps}"

    if ((persistent.playername == "MaKa") or (persistent.playername == "Kidney")):
        play music latespring noloop
        scene white with Dissolve(2.0)
        show circle onlayer front at hole2
        show title "Written By : \n{size=55}Batebri{/size}\n\nCoded By :\n{size=55}RoyAH_M\nBatebri{/size}\n\nCoding Support :\n{size=55}Elckarow\nWretchedTeam\nRoyAH_M{/size}\n\nArtist :\n{size=55}Batebri{/size}\n\nProofreaders :\n{size=55}Horderlocke\nAndrewA01\nTheMagicalGuardian\nPiculra\nLeonnnn{/size}\n\nMusicians :\n{size=55}Chromacle  -  \"Interlude\"\nEl Huervo  -  \"Crush\", \"Daisuke\", \"Ghost\"\nEndless  -  \"Disturbance\", \"Keep Calm\"\niamthekidyouknowwhatimean  -  \"Run\"\nLife Companions  -  \"Richard\", \"We're Sorry\"\nLipPi Sound  -  \"Abyss Intro\"\nMagic Sword  -  \"The Way Home\"\nModulogeek  -  \"Around\"\nNounverber  -  \"Black Tar\"\nOld Future Fox Gang  -  \"Guided Meditation\"\nScattle  -  \"Flatline\"\nSjellos  -  \"Chamber of Reflection\"\nThe Green Kingdom  -  \"Untitled\"\nLudoWic  -  \"Panoramic Feelings\"\n{font=mod_assets/font/汉仪长宋简.ttf}腰  - “晚春”{/font}{/size}\n\nBackground Support :\n{size=55}Kimugure After\nUncle Mugen\n{font=mod_assets/font/汉仪长宋简.ttf}(c)安野让{/font}\nYukito\nAyaemo Creative Institute\nMorbi ||/WoD\\Dev\nuezere{/size}\n\nPlaytesters :\n{size=55}Oliver Norton\nHorderlocke\nLilBigJP\nNuru\nBoeJiden\njfgibson73\nmemespirit\nsilver\nshpeedz\nKID-X-ec\nHacker_NSS\nStardewValliant\nYaagii\nDetermined_Spirit\nShadowSlayer051\nHappySpiderFan\nDecepticon\nEXE||\nIsaLation{/size}\n\nChinese Translation Support :\n{size=55}Carta\n{font=mod_assets/font/汉仪长宋简.ttf}诺帕提{/font}{/size}\n\nSpecial Thanks : \n{size=55}Drechenaux\nTeam Salvato\n{font=mod_assets/font/汉仪长宋简.ttf}腰\n\n寸铁{/font}{/size}" at credit
        pause 391
        scene black
        $ persistent.cg0 = True
        $ persistent.cg1 = True
        $ persistent.cg22 = True
        $ persistent.cg23 = True
        $ persistent.cg24 = True
        $ persistent.cg25 = True
        hide circle onlayer front
        call showpoem (get_poem("poem_m2"))
    else:
        play music untitled noloop
        scene white with Dissolve(2.0)
        show circle onlayer front at hole
        show title "Written By : \n{size=55}Batebri{/size}\n\nCoded By :\n{size=55}RoyAH_M\nBatebri{/size}\n\nCoding Support :\n{size=55}Elckarow\nWretchedTeam\nRoyAH_M{/size}\n\nArtist :\n{size=55}Batebri{/size}\n\nProofreaders :\n{size=55}Horderlocke\nAndrewA01\nTheMagicalGuardian\nPiculra\nLeonnnn{/size}\n\nMusicians :\n{size=55}Chromacle  -  \"Interlude\"\nEl Huervo  -  \"Crush\", \"Daisuke\", \"Ghost\"\nEndless  -  \"Disturbance\", \"Keep Calm\"\niamthekidyouknowwhatimean  -  \"Run\"\nLife Companions  -  \"Richard\", \"We're Sorry\"\nLipPi Sound  -  \"Abyss Intro\"\nMagic Sword  -  \"The Way Home\"\nModulogeek  -  \"Around\"\nNounverber  -  \"Black Tar\"\nOld Future Fox Gang  -  \"Guided Meditation\"\nScattle  -  \"Flatline\"\nSjellos  -  \"Chamber of Reflection\"\nThe Green Kingdom  -  \"Untitled\"\nLudoWic  -  \"Panoramic Feelings\"\n{font=mod_assets/font/汉仪长宋简.ttf}腰  - “晚春”{/font}{/size}\n\nBackground Support :\n{size=55}Kimugure After\nUncle Mugen\n{font=mod_assets/font/汉仪长宋简.ttf}(c)安野让{/font}\nYukito\nAyaemo Creative Institute\nMorbi ||/WoD\\Dev\nuezere{/size}\n\nPlaytesters :\n{size=55}Oliver Norton\nHorderlocke\nLilBigJP\nNuru\nBoeJiden\njfgibson73\nmemespirit\nsilver\nshpeedz\nKID-X-ec\nHacker_NSS\nStardewValliant\nYaagii\nDetermined_Spirit\nShadowSlayer051\nHappySpiderFan\nDecepticon\nEXE||\nIsaLation{/size}\n\nChinese Translation Support :\n{size=55}Carta\n{font=mod_assets/font/汉仪长宋简.ttf}诺帕提{/font}{/size}\n\nSpecial Thanks : \n{size=55}Drechenaux\nTeam Salvato\n{font=mod_assets/font/汉仪长宋简.ttf}腰\n\n寸铁{/font}{/size}" at credit
        pause 345
        scene black
        $ persistent.cg0 = True
        $ persistent.cg1 = True
        $ persistent.cg22 = True
        $ persistent.cg23 = True
        $ persistent.cg24 = True
        $ persistent.cg25 = True
        hide circle onlayer front
        call showpoem (get_poem("poem_m2"))
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
