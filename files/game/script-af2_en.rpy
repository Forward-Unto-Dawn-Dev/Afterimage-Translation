label af2_main:
    scene white with MultipleTransition([
        False, Dissolve(3.0),
        act2, Pause(4.0),
        act2, Dissolve(3.0),
        True])

    play ambient ext_day volume 0.9
    s "[player]?"
    stop music fadeout 3.0
    "She waves her hand before me."
    scene bg schoolgate_day with Dissolve(2.0)
    "I'm pulled back to reality, the sun is revealing itself behind the cyan sky."
    "We sit on the bench along the street, watching the bustling students crowding towards the school gate."
    "Looks like we somehow wandered to our high school."
    show sayori worried2 du at t11
    s "Is everything okay? You are spacing out again…"
    mc "Err… I'm fine."
    show sayori serious1 dd
    s "I want to take a look inside…"
    show sayori smile3 dd at s11
    "She leans back against the bench."
    show sayori smile3 dd:
        alpha 1.0
        easeout 6.0 alpha 0.3
    "Under the bright morning lights, her smiling cheek seems so ……"
    "So insignificant…… "
    "Sunlight penetrates her ghost outline, making it more and more invisible, I can't almost figure out those details inside the mist, like the dew retreating to the blue sky, her body is disappearing in the noisy lights."
    show sayori curious1 dd:
        alpha 0.3
        easein 0.1 alpha 1.0
    mc "Sayori!!!!!"
    "I cry out loud subconsciously, I feel gazes nailing onto me."
    s "Huh?"
    mc "I'm… I'm losing you!!"
    show sayori sadsmile1 ud at f11
    s "What're you talking about? I'm here, dummy…"
    "The curve of her lip is looming in the thin air."
    show sayori sadsmile2 ud
    s "You won't be able to leave me hanging this time, I'll stick to you, wherever you go~"
    "A fortunate cold sweat slips down my forehead."
    show sayori sadsmile2 ud at t11
    mc "I could look for my old uniform, if……"
    show sayori curious2 uu at f11
    s "What about mine?"
    mc "It's okay, I have……"
    "…"
    pause(1.5)
    mc "That's a bad joke…"
    show sayori reluc7 dd at t11
    s "Sorry… I didn't mean to say that."
    show sayori curious6 dd at f11
    s "But don't you have courses to attend?"
    show sayori curious6 dd at t11
    mc "It's nothing, none of them matters."
    show sayori curious1 ud at f11
    s "OooK..."
    s "So, what's next, we head back?"
    mc "No,"
    mc "we have breakfast."
    scene bg loudstreet2_day with dissolve
    play music shemeditates fadein 1.0
    "I stand up and walk forward the moment I finish my sentence."
    show sayori angry1 dd at t11
    s "Hey, wait for me!"
    show sayori angry1 dd at f11
    s "What's with the speed?"
    show sayori angry1 dd at t11
    mc "It's a surprise."
    show sayori curious3 uu at h11
    s "Whhaaaaaat??"
    show sayori curious3 dd
    "She trots to the front of me, walking backwards."
    show sayori curious3 dd at hpunch:
        i11
        alpha 1.0
        easeout 0.3 alpha 0.1
    pause(0.5)
    show sayori curious3 dd:
        alpha 0.1
        easein 0.3 alpha 1.0
    "Suddenly a stranger passes through her, disturbing her figure to a mess."
    mc "Hey!"
    "The fog reforms after the stranger leaves."
    mc "Watch yourself…"
    show sayori curious6 dd at f11
    s "What is it??"
    mc "It won't be a surprise if I tell you."
    show sayori surprise1 ud
    s "Pleeease?"
    "She runs around me in pure curiosity."
    mc "Do you feel anything when others run through you?"
    show sayori angry4 dd
    s "Don't change the subject!"
    show sayori curious2 dd at t11
    mc "Oh and here we are."
    stop ambient fadeout 1.0
    scene bg bakery_blur with dissolve
    "We walk on the sidewalk for a while before we reach the bakery."
    "A lady is tidying up the mess of the rushing hour."
    mc "Morning, Miss."
    mc "{i}I would like four cinnamon buns.{/i}"
    show sayori happy1 uu at r11
    show sayori happy1 uu at h11
    s "Woooooow!!!"
    "Sayori jumps all around the counters, eventually ending up staring at those decent pastries."
    scene white with Dissolve(3.0)
    "I make my way to the checkout as her typical exaggerating voice echoes in the background."
    "I can hear her wolfing down the food anxiously and those rusty wheels of the school gate grinding against the concrete."
    "We are fired off like an arrow leaving its bow, pointing straight into the school building, with our plastic bags flying behind us."
    scene bg bakery_blur with Dissolve(3.0)
    show sayori smile5 dd at h11
    s "Hurry! Just eat it!"
    "Sayori is radiating her excitement from all over her body, her happiness passes across the end of her hair to reach my palms, then drips all the way down onto those steaming buns."
    "Little nervous, I pay the cashier."
    "When the cashier walks away, I ask Sayori in a low voice."
    show sayori smile1 dd
    mc "She really couldn't hear you."
    show sayori curious1 du at f11
    s "I wonder if Natsuki and Yuri can."
    show sayori curious1 du at t11
    mc "I'm not so sure about Yuri, but Natsuki…"
    mc "She's probably gonna pass out."
    show sayori curious6 dd at f11
    s "Nah, Nat is not that timid."
    show sayori curious6 dd at t11
    pause 2.0
    "I wolf down the four of them in one go."
    show sayori smile4 dd
    "Sayori looks at me, satisfied. "
    mc "Good?"
    show sayori smile5 ud at f11
    s "You bet!"
    show sayori smile5 ud at t11
    "I laugh."
    mc "Fancy anything else?"
    show sayori smile1 ud at f11
    s "Can you handle?"
    mc "It won't hurt to just bring them back."
    show sayori mock7 dd at t11
    s "In that case…"
    show sayori at lhide
    hide sayori
    s "I want this!"
    s "And this!!"
    pause(1.0)
    s "Emmmm…… This one seems good…"
    pause(1.0)
    s "Oh! I almost forget, the cookies!!!"
    "I've just made myself another bad decision…… "
    mc "OK, OK…, that's enough, my fridge's not gonna hold it."
    show sayori mock3 dd at t11
    show sayori at laugh_cg_twice
    s "Ehehe, I just don't see you like this very often~"
    show sayori smile1 dd
    "She looks at me, or rather, the two big shopping bags in my hands."
    play ambient ext_day volume 0.9 fadein 1.0
    scene bg loudstreet2_day with dissolve
    "I can only make up some compromising face."
    "But these pastries are steaming heartily, I guess I will trade anything with the world as long as she's happy."
    scene bg loudstreet3_day with dissolve
    pause 2.0
    mc "…hu…hu…"
    mc "I can't… hold it… let's take the bus."
    "I lean against the wall to catch my breath."
    show sayori angry1 du at t11
    show sayori angry1 du at f11
    s "No! You should take more exercise!"
    show sayori angry1 du at t11
    mc "That's easy for you to say! Don't forget who am I buying this for!"
    show sayori angry5 dd at f11
    s "Alright alright, it won't be that far since we have already walked this long, right?"
    show sayori angry5 dd at t11
    "I take out my phone to check the map."
    "It shows 13.3KM on the GPS."
    show sayori curious3 uu at f11
    s "We walked that far?!"
    show sayori curious3 uu at t11
    "Given this, I refuse to walk a single step."
    show sayori curious2 du at lhide
    pause(0.5)
    hide sayori
    "I drag Sayori to the nearest bus stop."
    pause 3.0
    "Unbelievably, again I try to look at the sign, line to line, up and down, but still fail to find my answer."
    "Looks like we have to……"
    "Walk…"
    "I lift up the two bags, stepping forward reluctantly."
    stop music fadeout 2.0
    stop ambient fadeout 2.0
    scene black with Dissolve(1.0)
    pause(1.0)
    play ambient int_day volume 0.9 fadein 1.0
    scene bg bedroom_day with dissolve
    "…"
    play sound closet volume 2.5
    "I dig in my closet, all the down until I finally find my outfit from the past."
    mc "How do I look?"
    "I slightly adjust my tie, then turn to Sayori."
    show sayori smile2 ud at t11
    s "You look like someone who's about to be late for his club~"
    mc "Really?"
    hide sayori with dissolve
    "I look at myself in the mirror."
    "My collar is rather wrinkled, leaning against my neck."
    "The edge of my sleeves have been worn out to its inner fabric, and those threads coming out from my sweater, are seemingly telling the story of my lost time by my washed-out tie and the tightened seam."
    mc "Not so bad, at least they aren't falling apart. "
    "Once again I neaten my collar a little, and button my blazer up."
    "Em?"
    "There's something in my pocket."
    "I fumble inside it, and take out something utterly soft."
    "It's a worn-out note that I didn't take it out before washing it, apparently."
    play sound torn volume 3.0
    pause(0.5)
    mc "Oops."
    "I made a mistake by tearing the note to half, the other part sticks to my inner pocket."
    show sayori curious2 dd at t11
    s "What is it?"
    mc "Dunno, it's something I didn't take out while washing."
    "I take off my blazer, turn my pocket over cautiously, and peel the note from it bit by bit."
    "From the thickness of it I could tell that someone folded this a couple of times carefully."
    "There are some words on it…"
    "But they are divided by the crevice."
    "I slowly put the two pieces together, despite soaking up by the water, and staying in my pocket for god knows how long, they are still somehow recognizable."
    "I speak them out subconsciously while reading them."
    "\"To [player]\""
    pause 2.0
    show sayori curious4 ud s11
    s "It's Natsuki's writing…"
    "Sayori preempts me before I say it."
    "Indeed, those blunt angles and specific strokes, are all indicating Natsuki's style."
    "I open both parts of the not up synchronously to avoid mismatch the lines."
    "I could at least come up with three possible time points."
    show layer master:
        blur 0
        easein 1.5 blur 50
    "I see Natsuki walk inside my classroom quietly, approaching my seat, take one last look at this very paper…"
    "Then slide it into my pocket."
    call showpoem (get_poem("poem_m1"))
    hide sayori with Dissolve(1.0)
    show layer master:
        blur 0
    "The paper has been soaked and rubbed to a mess, I make my best effort to read those words, deciphering the original meanings from their fleeting figures."
    "Even so, most of them just lost what they guard for within the lines and paragraphs permanently."
    "I turn to the back of it, indeed there are four sets of numbers. I'm guessing it's their phone numbers and email addresses."
    "Why there isn't Monika's though?"
    "I've noticed that Sayori's not here, I look up to find her sitting by the window, with her eyes slightly closed."
    "Is she sleeping?"
    "Yeah, we stayed up all night after all, not to mention the long walk home."
    "Leaving her to it, I boot up my laptop, trying to insert one of the addresses into it."
    "I look at the profile picture of this email—this isn't Natsuki's style at all…"
    "I remember her chatting with me online, it's impossible for a person like her to use this kind of image."
    "Did I type the wrong number?"
    "I grab the note and take a second look at those ambiguous ones."
    "A few more new accounts pop out after I changed those uncertain numbers, but none of them feels like Natsuki."
    "This is confusing, there won't be as much trouble if it's gets confirmed at the beginning, but now I really can't decide which is which thanks to the choices."
    "What if she changes? It's been four years…"
    "What if I send something sincere to a complete stranger? That would be extremely awkward…"
    "Didn't she give me her number before she visits my house? That's right! How could I forget something like that?"
    "So I open up my contact list, searching for her name."
    "Recalling something backwards as I lift my thumb off the screen, leaving the list sliding down on its own."
    "I didn't just throw my old cellphone away. I've also deleted all my past acquaintances."
    "What a great job, [player]."
    "I just have to move on to Yuri's."
    "What is this besides her phone number?"
    "I mean, I thought it would be her email address since Natsuki is writing her own, but this isn't an email's format… there are some words there… with strange blanks in between."
    "Is this some sort of {i}mailing address{/i}? She does prefer this physical type of writing though…"
    "Maybe it is, but these words are too vague to tell, I can't get exact information from them."
    "I push the chair backwards, then stand up to check Sayori."
    scene cg window with Dissolve(1.0)
    $ persistent.cg5 = True
    "I sit next to her, her right hand is gently placing on the balcony, seemingly faint under the sunlight."
    scene cg window2 with dissolve
    $ persistent.cg6 = True
    "I put mine in hers, matching the outline."
    "Thin fog crawls to the back of my hand like a shadow, gently licking my surging veins."
    play music weresorry fadein 2.0
    "A weird pulse starts to spread to my palm, making the blood in my flesh synchronize with something."
    "I stare into her temporarily peaceful eyebrows."
    "Storm was wiping the field over along with all the existing orders."
    "Before the overwhelming leaves and grass returned to the ground, there was somebody, sneaking in the rye."
    "Dark machine arms dig into the moist earth from beyond the sky, turning all the straws over, and carve the noise of gasoline into them."
    "Metal wheels rapidly spin, the accuracy of math denies all the compromising and flinching."
    "Seeds, they are forced to stare at their mother's roots, and to watch them get shredded apart by the blades."
    "Grab, pry, and tear. Cramp, swell, and sting, along with sorrow. Some reflection, then soaking, warmth."
    "Numb smell, covered in weariness,"
    "open up to see the night outside,"
    "and the black face on the ceiling,"
    "the emerald eyes spinning within."
    show noise
    play sound noise volume 0.5
    pause(0.2)
    hide noise
    stop sound
    stop music fadeout 3.0
    scene bg bedroom_day with Dissolve(1.0)
    show sayori angry6 dd at t11
    s "{size=-5}Uwmmmmm…………{/size}"
    show sayori reluc8 dd
    pause(0.15)
    show sayori angry6 dd
    "I stare at her in silence."
    show sayori reluc8 ud at s11
    s "{size=-5}Awhhhh………{/size}"
    show sayori reluc8 ud at t11
    s "{size=-5}You finished?{/size}"
    s "{size=-5}How long…{/size}"
    show sayori reluc8 ud at f11
    s "{size=-10}How long have I been sleeping……{/size}"
    show sayori reluc8 ud at t11
    "Her voice is extremely hoarse, like sandpaper grinding concrete. The only surviving moisture is struggling inside gravel's siege."
    mc "Not too long, like half an hour."
    "I take the mug by my hand, adjusting its angle until the curve of the ceram completely blocks my view as the chilly liquid streams down my throat."
    "Seeing my throat going up and down, there's an odd understanding tying us together."
    show sayori curious7 ud
    "The brush wipes the dust of chalk off the blackboard, and her voice gets back to limpid, temporarily."
    show sayori reluc3 ud at f11
    s "Did you…"
    show sayori worried3 ud
    s "Did you get in touch with them?"
    show sayori worried3 ud at t11
    mc "I was just about to talk with you about that. The letter is not so easy to read. But………"
    pause 1.5
    "I pause, touching the edge of the mug with my fingers."
    show sayori reluc3 ud at s11
    stop ambient fadeout 1.0
    mc "Could you tell me what happened?..."
    pause 3.0
    show sayori worried3 ud
    pause(2.0)
    show sayori weep9 ud
    "I look at her right into the eyes."
    "Light blue turns deep cyan in the darkness, among the surging river in the steep valley and howling fire in the forgotten woods, my thought is finally confirmed."
    show sayori reluc9 ud
    pause 1.0
    "She looks to the floor, we are all preparing for the upcoming conversation in this dreadful silence."
    "In the end, she responds with a sound that is tiny enough to be a fiber detached from the noose,"
    "yet it expands to Gargantua in my ears within a split second, just like the mountains rising and falling behind her back."
    show sayori weep2 ud at t11
    s "{cps=*0.1}It's……………Monika…………{/cps}"
    show sayori weep8 ud
    show vignette_white:
        alpha 0.2
    with dissolve
    show layer master:
        blur 0
        easein 0.5 blur 10
    "Dialogues from the past suddenly release, emerging in my brain."
    "\"Monika was right…\""
    "\"I should just…\""
    hide vignette_white
    show layer master:
        blur 0
    with Dissolve(1.0)
    pause 2.0
    mc "What"
    mc "did"
    show sayori weep9 ud at t11
    mc "Monika"
    mc "do?"
    "I nail these words out letter by letter, the rest of the sentence gets loaded into my magazine one by one."
    pause 2.0
    show sayori weep2 ud
    "{cps=*0.2}She stops for a bit, then all of her emotions burst out uncontrollably.{/cps}"
    show sayori weep5 uu:
        linear 6.0 blur 100
        linear 6.0 alpha 0.2
    play music run volume 0.6
    s "I don't know!"
    "Her tears strike my sight along with these three words."
    s "I DON'T KNOW! I DON'T KNOW! I DON'T KNOW!"
    s "IDONTKNOWIDONTKNOWIDONTKNOWIDONTKNOW!!!!!!!!!-----------"
    show noise
    play sound noise volume 0.5
    pause 0.2
    stop sound
    hide noise
    "She repeats these words like sleep-talking as the mist from all over her body starts to fade, millions of lines and curves shake along with it, sending her figure out of the window, into the abyss."
    mc "Sayori! Calm… calm down!"
    "I reach out, trying to comfort her."
    show sayori weep5 uu:
        blur 100
        linear 1.0 blur 70
        alpha 0.2
    "Unlike the previous one, I feel a thorn-like touch on her back this time."
    show white:
        alpha 0.27
    with Dissolve(0.3)
    show layer master:
        blur 13
    with dissolve
    "\"It felt like a bunch of thorns……\""
    "\"Like a spear going through my heart………\""
    "I look up along the hands that are holding the spear to find…"
    scene bg bedroom_day with dissolve
    show layer master:
        blur 0
    "{cps=*0.1}A pair of emerald eyes.{/cps}{nw}"
    show noise
    play sound noise volume 0.5
    pause 0.2
    hide noise
    stop sound
    show sayori weep10 dd at i11:
        alpha 0.2
        linear 1.5 alpha 0.6
    "She calms a little, no longer shaking as the details in her shadow become clear again."
    pause 0.5
    show sayori weep10 dd at t11:
        alpha 0.6
    pause 1.0
    show sayori weep6 dd at t11:
        alpha 0.6
    pause 0.5
    show sayori weep6 dd at t11:
        alpha 0.6
    s "She was there, she was always there…"
    show sayori weep4 dd at t11:
        alpha 0.6
    s "Ever since you joined the club…… she was on the ceiling of every sleepless night, she was at the corner of the empty classroom where I picked up the materials for drawing posters!"
    show sayori weep5 dd at hf11:
        alpha 0.6
    s "At the doorway!{w} On the kitchen table!{w} Inside my blanket!! ……"
    show sayori weep4 dd at t11:
        alpha 0.6
    s "I couldn't figure out who was in the darkness at first, but it gets clearer and clearer…"
    show sayori weep4 dd at s11:
        alpha 0.6
    s "The voice said a lot of mean things to me, I was…"
    "I continuously replay the tip of the iceberg she described to me in her bedroom that day."
    show sayori weep10 dd at t11:
        alpha 0.6
    s "I don't know. I think I'm crazy, I'm seeing things, that it wasn't Monika speaking…"
    show sayori weep10 ud at sink(a=0.6)
    s "I tried. I tried denying it."
    show sayori weep3 ud:
        alpha 0.6
    s "But there was something else, a third voice inside my head."
    s "It welcomed Monika's visit, agreed with everything she said without hesitation."
    s "It took over my body, drove me away. I could do nothing but watching it discussing me with Monika, to comment me, to reconstruct me…"
    s "It had actually always been like this, I'm learning to live with it."
    s "Although it was mean, it won't listen, always thought about taking control over everything…"
    show sayori weep11 ud at sink_more(a=0.6)
    s "But I promised myself to get along with it and we were making progress {size=-2}un{size=-4}til{size=-6}… {size=-8}until{size=-10}......{size=-12}.........{size=-14}.............{/size}"
    "Her voice becomes more and more unrecognizable as endless sorrow and tears fill her throat, making her unable to talk clearly."
    "I remember that Friday, that was my first time discovering her unusual behavior, then I told…"
    show vignette_white at easein_to_alpha(0.27, 0.5, 1.0)
    "\"I'll try to talk to her, so try not to think about it for now\""
    hide vignette_white with dissolve
    pause(2.0)
    show sayori weep10 dd
    stop music fadeout 4.0
    "I really, really want to know what did Monika say to her."
    "But her streaming tears and hoarse sobbing is the best explanation. "
    pause 2.0
    mc "It's okay, it's okay… I'm here."
    mc "I'm here."
    mc "You are safe now."
    mc "Nobody's going to take control of you anymore."
    mc "You are safe."
    show sayori at walk_in(a=0.6)
    "I squeeze her hands, trying to warm them."
    "I..."
    "I reach out to hug her, even though her body feels more meaningless than the air."
    hide sayori with dissolve
    "Still crying, she collapses to me, unsurprisingly goes through my body and lays onto the bed."
    scene black with Dissolve(2.0)
    mc "Sayori?..."
    s "{cps=*0.2}{size=-8}sor...........{/size}{/cps}"
    s "{cps=*0.2}{size=-8}s..........................{/size}{/cps}"
    pause 2.0
    "She's not responding, or maybe it's because I can't make anything out from her sobbing."
    "I can see her body trembling, her back shaking."
    "She clutches her head with her hands, disturbing her hair to a mess."
    "After a little while, when the crying has finally drained her last drop of energy, her sobbing sound becomes lower and lower,"
    "her arms fall to the side, and her fingers strech from the grip."
    "I look at her destroyed figure, at what's remaining of her soul."
    "I want to say something."
    "Yet I can't."
    "My throat hurts, hurts a lot."
    "All of the air gets wiped out from my lungs."
    "I can sense the blood being pumped in my head."
    "Millions and millions of thoughts come across my mind."
    "But I can't make out a single one of them."
    "The only thing I see is her crying sound."
    "Echoing in my head."
    "In my blood."
    "Echoing,"
    "echoing,"
    "echoing"
    pause 3.0
    "We stay like this for a while."
    "Then I slowly move away from her as I carry the weight of my heart, avoiding making too much disturbance to her shape."
    "I crouch down to check on her. After confirming her sleep, I sneak out my bedroom, gently close the door."
    "Then, I tighten up every last one of my muscles before I fire off from my house. I run to the nearest hardware shop in the neighborhood at my maximum speed before buying a ten meter long climbing rope."
    scene bg street2_day with dissolve
    pause(0.5)
    scene bg loudstreet2_day with dissolve
    "It comforts my heart as the tip of the rope gets grilled to black by the fire."
    show black with dissolve
    "Lines and lines of plans are carved into solid concrete, then sink down to the bottom of the lake."
    "I seize the rope in my hand, make my way home as fast as possible."
    hide black with dissolve
    pause(0.5)
    scene bg street2_day with dissolve
    pause(0.5)
    scene bg doorway_day with dissolve
    pause(0.5)
    scene bg bedroom_day with dissolve
    "Luckily, Sayori is still sleeping. I quickly pull my backpack over, clear my book out and stuff the rope into it."
    stop music fadeout 3.0
    play sound zip fadeout 1.0 volume 0.7
    play ambient int_day volume 1.5
    "I zip it up, let out a long sigh of relief before I collapse to the chair."
    "I keep my fingers crossed, stare out the window quietly."
    "The sky is fascinatingly blue, the remaining clouds all get pushed aside except only one soft jet cloud flying across the whole sky, pointing to the far side of future beyond predictions."
    "Layers of leaves fade from deep to light, onto the top, melting into the moss within the walls."
    "I hear the breath of tranquility."
    "One…"
    "two…"
    "three…"
    show bg bedroom_dusk with Dissolve(4.0)
    "I sit there all the afternoon, watching the shadow of the telegraph pole stretches as the remaining sunset illuminates the horizon to gold."
    "Until the sparkling stars reappear on the night's veil, gentle breeze runs through struggling grass."
    scene black with Dissolve(5.0)

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
