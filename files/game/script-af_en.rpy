label af_main:
    stop music fadeout 2.0
    scene bg train with dissolve_scene_full
    play music subway
    show crowd1 with dissolve

    "Wind's howling. With its last parade riding its horse throughout the carriage, my body abruptly leaning forward."
    "I am surrounded by countless backpacks, suitcases, beanies and shoes."
    "Interrupting those glowing screens awkwardly, I step out the subway door."
    scene black with dissolve
    "Walking towards the exit, I take a look at the grim sky, imprisoned by cold steels."

    stop music fadeout 0.5
    play music subwaypeople

    "I bury my face into my collar, and walk up the necessary steps, one by one, in order to get up there."
    scene bg subwaystation2 with Dissolve(1.0)
    stop music fadeout 1.0
    play music rain volume 0.72
    play sound umbrella
    "Vehicles rushing by, write the moisture onto my face.{w=0.3} There are few passengers around, my eyes mostly fix on the shining leaves."
    show white at easein_to_alpha(0, 1.0, 0.9)
    "\"…why do you wear such thin clothes…\""
    "\"What? …\""
    scene bg street1_day_rain with Dissolve(1.0)
    "I turn to the other side of the alley, beneath that well-worn telegraph pole, something was looming, as if someone was there……"
    "However, there are no signs of walking nor wet footprints, I close my eyes, then gently open them…"
    "To notice nothing but my heart being tightly grabbed by something I can't quite describe."
    "I walk the path with a rather anxious pace, firmly holding my rain avoiding tool."
    scene bg residential_day_rain with dissolve
    pause(0.5)
    scene bg house1_day_rain with dissolve
    "Pale courtyard rails just drag my eyes there unceasingly, my increasing speed could barely fight back its strength."
    show vignette_white at vignetteflicker
    "Memories flood in, every step prints a dialogue.{w=0.3} Water flows into the sewer, wave by wave."
    "It's clearer for me than anyone that if I stop by, even only for a second, I will slip."
    "It was totally wrong not to follow the GPS, there must be a much shorter route……"
    "However, my body subconsciously walks on this path ever since I got out of the subway station…"
    "Who am I going to blame though? This is where I used to live after all."
    hide vignette_white with dissolve
    "Luckily, I've got somewhere else to visit."
    "Right?"
    stop music fadeout 3.0
    scene white with Dissolve(1.0)
    pause(1.0)
    scene bg office2 with dissolve
    play music interlude
    "Finally, I start tramping past foreign buildings, pass those LED light boxes and plastic counters, then present my well-edited lines to those vaccinated faces."
    "We take out our documents, exchange smiles, show off our teeth, and our tongues stir up the saliva, weaving polite words into the behaved air."
    "I pick up my wet umbrella by the door and stare at the outside streets from where I stand still."
    scene bg loudstreet1_night_rain with dissolve
    "Suddenly some shadows approach my back, dodging its engagement, I stagger to the corner."
    show crowd2 at t33
    "Turns out to be couple of high school students walking outside, chatting and laughing."
    "I notice something…"
    "It's their collar…… their collar…"
    hide crowd2 with Dissolve(2.0)
    "I just toss my eyes there, until the shades of red vanish behind the expanding angle between us."
    "My fluorescent phone screen tends to become a main role on the stage of the dim sky. I cope with my social apps nonchalantly using one hand."
    "Eventually, I turn off the GPS, simply just walk back to where I came."
    scene bg house1_night2_rain with dissolve
    "Orange glitter draws my silhouette cautiously onto the window across the street, I dig forward, eyes on the ground."
    "But a sense of warmth stopped me in the middle of this road, in front of the peaceful courtyard."
    "An unfamiliar car parked on the side of the house, although it's still a few meters from where I stand, the heat under the hood is hard to ignore—as is the light behind the window."
    "Gentle melody paints every inch of the room with its welcoming color, I could hardly recognize anything through the vague windows, but I'm sure that there are many people, sitting around a big table."
    stop music fadeout 2.0
    play sound cheers
    show white with Dissolve(2.0)
    "Must be quite a meal. Among their cheerful laughter and clangs of cutlery, two children are looming."
    "\"You can cook? Really? Maybe you should change the word with {i}eat{i}!\""
    "\"You don't believe? Don't beg me for a taste then!!\""
    play sound shower
    "Leaked relaxation from the shower head slips down my eyelids, lingering with my skin towards the last corner where lights could ever reach."
    "Highlights hop from one drop to another, blur everything around me into the soothing steam."
    "My nerves seem to ease a little.{w=0.3} Nothing's better than a proper hot shower after a busy yet cold, wet day."
    stop sound fadeout 0.5
    "\"Have you brought your pillow today?\"{w=0.3} I dry myself up, open the door."
    stop music
    hide white
    pause(0.1)
    play sound fall
    queue sound rain volume 0.36
    show white with vpunch
    pause(0.1)
    hide white
    "My forehead banging against the chilly concrete wall seriously, nerves resume onto the cello, freezing air stabs into my bones with no mercy."
    "When hard steel wires pierce through my eyelids to pull them up, an aged stoop appears in my sight."
    show oldman at t11
    play music abyss
    randomperson "Hello?"
    "The old man saw me react a little, so he give it another pat on my shoulder."
    "\"I saw you standing here for a while now…are you looking for someone?\""
    "\"Ah! Umm…no, nothing much,…sorry, I'm just spacing out…\""
    show layer master:
        blur 0
        easein 1.0 blur 15
    "A foul taste of vertigo strikes over me, street lamps…get so gloomy, pavement starts to curve, to fold, to intertwine, expelling my ugly figure out of this silent street."
    scene black with Dissolve(1.0)
    show layer master:
        blur 0
    pause(1.0)
    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene bg bedroom_night with dissolve
    play music int_night volume 0.5
    "I sit in front of my desk, fiddling with my boring pen."
    "My brain just won't stop replaying it all, images get tossed onto the desk, and crash to pieces before I could examine them correctly."
    "I look up at my bookshelf at the least appealing corner, it still lies there."
    "Pulling it out, dust begins to wake."
    "I gently turn the pages over, along with the inferior lines, then I pick up the creased paper, unfold it, and hold it on my palms."
    "I sigh to myself."
    "With the air leaving my mouth, the once floated dusts now start to become more visible under my table lamp."
    play sound page_turn
    "The most familiar handwriting in my life lies there faintly, unable to breathe even once. I try to fold it back, yet my body remains limp."
    "Before long, I stand up and walk to the living room."
    show black with dissolve
    "It's probably midnight now, but I still want to take a walk, it's not like I will be able to know who or what awaits me in my dreams……{w=0.3} Or another night without any dreams."
    scene bg doorway_night
    hide black with dissolve
    "I manage to reach the doorknob in darkness."
    "\"What a day.\""
    "I gently open the door."
    show sayori laugh3 uu at hf11
    "{cps=30}\"Boooooooo!!!!\"{/cps}{nw}"
    hide sayori
    "I'm caught off guard, stagger back against the door frame, barely maintain my balance."
    "I catch my breath, then stand up to look at the doorway."
    "What's happening? I swear I've heard something."
    scene cg fog with dissolve
    $ persistent.cg1 = True
    play music flatline volume 0.6
    "Some cyan fog enters my door from the distant darkness outside, forming the tenderest figure in my memory at the last defense line of mine."
    "She slowly steps out of the glim far beyond my reach, descend from the celestial, like a helpless star."
    "I feel a salty taste filling my throat."
    "The outline starts to take form, then she waves her hand before my eyes."
    "Seems like she made a mistake to measure the distance, her hand runs through my face, the thin fog gets disturbed, and then reluctantly gather together again."
    scene bg doorway_night with dissolve
    "When she finally releases my eyesight, an undeniably familiar face reveals."
    show sayori sadsmile1 dd at t11 with Dissolve(1.0)
    show sayori worried1 du
    s "{size=-5}Hey……[player]……{/size}"
    "I try my best to stay calm, but billions of strings all get intertwined inside my head as walls begin falling apart, leaving their solemn height behind."
    play sound hb loop
    show vignette at vignetteflicker(-2.030)
    show black at easein_to_alpha(0, 20, 0.8)
    show layer master:
        blur 0
        easein 5 blur 10
    "Overwhelming tides take down every fortress in the blink of an eye."
    "My body trembles under the heavy air hammer, bashing and smashing."
    "I take a glance at her neck, behind her half visible cyan, there's nothing but the silent doorway, facing the freezing breeze of November."
    "I try to remember more, but my efforts become useless behind my blurry eyes."
    show sayori worried2 du
    s "{size=-5}[player],… what's wrong? ……{/size}"
    "Seeing me wordless, she seems to be a bit worried."
    "I close my eyes, forcing them to rotate a little.{w=0.25} Tears drip down to my shirt.{w=0.25} I dare not to open them, I dare not to confirm."
    show black at easein_to_alpha(0.8, 1.0, 1.0)
    "My feet sink down the quicksand, I give in to the surging memory, let them drag me down, down to the bottom…{w=0.25} Only the cold air reminds me of my delicate presence."
    scene bg doorway_night
    show sayori surprised1 uu at i11
    hide vignette
    hide black with Dissolve(0.0)
    stop sound
    show layer master:
        blur 0
    with Dissolve(0.1)
    s "{cps=*3}{size=+10}Heyyyy!!!{/size}{/cps}"
    "Hearing her call, I open my eyes without any hesitation."
    show sayori sadsmile1 dd
    "The cyan figure's still there……{w=0.25} Fog constantly fades at the edge of the outline, as if she were to disappear into the vast world any second with a blow of a storm."
    "…"
    "{cps=*0.35}Luckily, there's no storm tonight, nor the vast world.{/cps}"
    "…"
    "…"
    mc "{cps=*0.25}…………Sayori?{/cps}"
    s "{size=-5}Hi [player]! Where are we right now?{/size}"
    show sayori curious4 dd
    "Her voice is very hoarse, but her tone remains heart-lifting, as if nothing has ever changed."
    "I chose my words, edited them, considered them."
    "I scrutinize my thousands of phrases in thousand lines of poems thousands of times, trying to find the most proper way to reply to her."
    "Finally, I let out a long sigh."
    mc "You really gave me a heart attack back there."
    "I reach out to pat on her shoulder, but my hand just goes through her body, leaving only the darkness around the door."
    show sayori sadsmile2 ud
    s "{size=-5}Ehehe… it's always so interesting to see you get flustered.{/size}"
    mc "Umm…I didn't know… I was just about to take a walk outside, and you suddenly……"
    show sayori laugh1 uu at laugh_cg
    s "{size=-5}Hahahah!!{/size}"
    "She lets out a giggle, seems still replaying my earlier reaction."
    s "{size=-5}{cps=*2}Hahaha…{/cps}{/size}"
    show sayori reluc1 dd
    "Our eyes meet as her laughter begins to dim."
    show sayori weep1 dd
    "Even though we are standing at a close distance, my gaze seems to be carried a thousand miles away, traveling to the end of time."
    "Here where even lights could not reach, I've finally found my sky-blue eyes."
    "Although they are unable to escape the siege of stiff cyan, I remember their original color."
    "I see limpid tears emerge from there, soaking her pillow, her Mr. Cow, her paper beneath her pen."
    mc "What ha……{cps=*0.25}{size=-5}How're you doing? …{/size}{/cps}"
    show sayori weep2 dd
    pause(0.6)
    show sayori weep3 dd
    pause(0.8)
    show sayori weep4 uu
    pause(0.3)
    show sayori weep6 uu
    "She lowers her head, tears leaking through her fingers unstoppably. Her shoulders begin to tremble, in the end, she can no longer hold it, collapses to me."
    hide sayori with dissolve
    "I reach out to embrace her, there's nothing I can come up with at this moment."
    "I think a hug is the best thing I can do now."
    play sound fall
    "She goes through my body as she crashes to the ground, endless sorrow kicks in, drowning, slaughtering."
    scene cg fell with dissolve
    "A lighting tears my heart in half, I crouch down to lift her up, to hug her tightly."
    "But no matter what I do, there's only the stone cold air to respond to me."
    "Her crying is the only thing that echoes in my room, her figure gets stirred to a mess thanks to my movement, the mist is becoming less and less visible."
    "Panic strikes, sending a chill down my spine. I hastily close the front door, and then try to rearrange the fog into her body, or rather, her shape."
    scene bg doorway_night with dissolve
    show sayori weep7 uu at t11 with Dissolve(0.8)
    "I put my hand on her back to comfort her."
    "I know Physics doesn't quite work the way it usually does right now, that I'm just using my own strength to hold my hand in the air to match the pose of comforting."
    show sayori weep8 uu
    "I hope this will somehow make her feel better, even though I don't believe in the slightest that the warmth can reach her side."
    "But I know she's by {b}my{/b} side, and that's ……that's…"
    "{cps=*0.25}That's good{/cps}"
    $ renpy.music.set_volume(0.2, 20, 'music')
    show sayori weep8 uu at focus
    "I kneel by her side, I couldn't make out a single word from her sobbing."
    "She buries her face in her hands, her coral hair tumbles down to cover them as her bow shakes in unspeakable fear."
    "Suddenly I let out a bitter chuckle, sadness and sorrow could no longer be suppressed under my throat."
    scene black with dissolve
    "I memorize that Monday… the chair lying on her floor, and the weight when she fell to my arms………"
    "The rough rope still tied her neck like a wolf choking its prey, with the dried blood rusting the air."
    "Morning lights gently penetrated her window, but they could never warm her cold body again."
    stop music fadeout 1.0
    $ renpy.music.set_volume(1.0, 0, 'music')
    scene bg doorway_night with dissolve
    show sayori sadsmile3 uu at t11
    mc "{cps=*0.25}Sor… I'm sorry……{/cps}"
    "Once again I try to reach her, but the result is all the same."
    show sayori sadsmile3 ud
    s "{size=-5}It's fine.{/size}"
    "She wipes her tears away, trying her best to hold the sobbing back, then looks up at me."
    show sayori care1 dd
    s "{size=-5}It wasn't your fault…{/size}"
    s "{size=-5}I just…{/size}"
    "…"
    "Her gravelly voice is barely recognizable, I can see her throat struggling under that awful bruise on her neck, as if the rope's still there."
    mc "Does it hurt?"
    show sayori peace1 dd at dip_slightly
    "She nods."
    mc "Don't talk OK? I'll get you some water."
    hide sayori with dissolve
    " "
    "I freeze the moment I stand up"
    "Stupid."
    "I can only turn around to face her in awkwardness as I find her clutching the end of my jacket."
    show sayori weep9 ud at t11
    "I reach out to take her hand in mine with disbelief. Out of the blue, hers gets lifted up by me successfully."
    "Sadly, there are too many details in my reality, soon I find out that she's just cooperating."
    "However, a small sense of warmth flows out from her fingertips."
    "Yet it disappears before I can pay more attention to it."
    mc "{size=-5}{cps=*0.25}What ha……{/cps}{/size}"
    mc "…How're you doing"
    show sayori reluc2 dd
    s "{size=-5}I……emmm…{/size}"
    show sayori sadsmile4 du
    s "{size=-5}I'm fine.{/size}"
    "She forces a smile."
    mc "{cps=*0.25}Why…{/cps}"
    "Now's not the time for that."
    mc "Are you hungry?"
    "The sentence pops out my mouth without me noticing as I trying to change the subject."
    show sayori reluc3 dd
    pause(0.5)
    show sayori weep1 dd
    s "{size=-5}I………{/size}"
    show sayori reluc4 dd
    "She look at the ground, helplessly."
    "This is enough!!!"
    "Her expression is like tons of rocks covering my chest, making it impossible for me to breathe."
    "I have to do something!"
    scene bg kitchen1_night
    play sound fridge volume 0.71
    "I storm in the kitchen, cluelessly searching in the fridge."
    "Finally I manage to find something that can be called ‘food' before I put them into the microwave, and sit at the table."
    "She follows me into the kitchen, I turn on the light."
    play sound switch
    scene bg kitchen1_day
    show sayori curious1 dd at t11
    "that's when I noticed that she's not standing firmly on the ground, but rather a floating state."
    show sayori curious2 ud
    s "{size=-5}You moved?{/size}"
    mc "Yeah…"
    mc "I transferred to another school. I couldn't stay around there anymore."
    "I look at her in guilt."
    show sayori curious2 ud at t33
    s "{size=-5}What's this?{/size}"
    "She points to my PS5 in the corner."
    mc "Ahh… ummm……That's my gaming console."
    show sayori angry1 dd
    s "{size=-5}Humph! So you began to play games again?{/size}"
    show sayori angry2 du
    s "{size=-5}I bet that you're not attending any clubs either!{/size}"
    mc "Well… actually…"
    mc "There are a lot of activities going around in college, so…"
    show sayori curious3 uu at h33
    s "{size=-5}What?!{/size}"
    s "{size=-5}You are in college now???{/size}"
    mc "Yeah, after all……"
    mc "It's been four years…"
    show sayori reluc5 dd
    "…"
    show sayori curious4 dd
    s "{size=-5}Already…four years?{/size}"
    " "
    show sayori sadsmile3 ud at f33
    s "{size=-5}Look at you.{/size}"
    show sayori sadsmile5 du at f11
    s "{size=-5}Didn't comb, didn't shave…{/size}"
    "She walks towards me, mildly touching my face."
    show sayori mock1 du at focus(640, 0.85)
    s "{size=-5}Jesus, you are worse than me sometimes.{/size}"
    "She giggles, running her hand through my long-forgotten hair. However, it feels like nothing but the plain air."
    "I'm speechless, thinking of it, when was the last time I looked in a mirror?"
    s "{size=-5}So, what does co…{/size}{nw}"
    play sound microwavefinish
    show sayori curious2 uu at t11
    pause(0.5)
    show sayori curious2 uu at h11
    mc "Wait here."
    hide sayori with dissolve
    "Warm smell spreads out all over the kitchen as soon as I open the microwave, bringing at least some ease to this cold night."
    "I put the pasta onto the table, its red sauce seems especially intriguing under the orange light. I have to say, even this makes me hungry."
    show sayori laugh3 uu at t11
    "Her eyes are just about to beam, but it doesn't ease me a bit. I put a fork before her."
    show sayori laugh3 uu at h11
    s "{size=-5}Wow! This looks reeeeaaally nice!!!{/size}"
    "Her familiar gasp rings by my ears."
    show sayori smile1 ud
    "The Sayori I know fully comes back as she reaches the fork and prepares a pasta massacre when suddenly…"
    show sayori reluc5 dd
    "Her fingers pass through the motionless metal."
    "I clench my fists."
    "{size=+10}God damn it!!!{/size}"
    "I curse the fuckin' pasta in my mind, I want to burn the table, I want to crash the useless microwave!!!"
    show sayori sadsmile1 dd
    play music Around
    s "{size=-5}You can have it.{/size}"
    show sayori sadsmile4 dd
    s "{size=-5}You didn't eat on time, right?{/size}"
    s "{size=-5}I can tell.{/size}"
    "…"
    "I smile."
    mc "No one knows me better than you."
    show sayori mock2 dd
    s "{size=-5}Otherwise why would you bring yourself an extra fork?{/size}"
    "I take up my fork, yet I can hardly move them."
    "Their weight is beyond all measuring, sealing all my senses. I can't move them an inch, even if I have the power to rewind day and night."
    show sayori care2 du
    s "{size=-5}Hurry, it's getting cold.{/size}"
    mc "Well, it's still a bit too hot right now since I heated it too long……and…um……"
    "I want to slap myself in the face, what kind of bad excuse is that?"
    "Anyway, I start eating."
    hide sayori with dissolve
    "The food."
    "It is a bit hot, to say the least. But it's not my problem to worry about."
    "I just mix up the sauce with random-intertwined curves, and stuff whatever it turns out to be into my mouth."
    "Their density decreases in my plate, when the last minced meat vanishes behind my teeth, a tear drops to the warmth that lingers above the whiteness. "
    "I reach out to take some napkins with my mouth full of pasta."
    show sayori smile1 uu at t11
    "Sayori sits across the table, holding her chin. "
    "She seems……better?"
    s "{size=-5}Your cooking is not so bad after all…{/size}"
    show sayori smile1 du
    "She taps her finger on the table as her legs dangle below it."
    show sayori smile2 du
    "Her smile looks so beautiful under the only light that illuminates this empty room."
    mc "How do you know?"
    "I gulp down some water, wiping my face with the napkin."
    show sayori curious1 du
    s "{size=-5}Emmmm, I don't know.{/size}"
    show sayori smile3 dd
    s "{size=-5}It's just that… watching you eat, makes me feel better.{/size}"
    s "{size=-5}Reminds me what pasta tastes like…{/size}"
    show sayori sadsmile1 dd
    s "{size=-5}I guess?{/size}"
    show sayori smile2 dd
    s "{size=-5}And the look on your face, tells me everything.{/size}"
    mc "Ahaha…"
    "She'll kill me if she knew this was just some random microwave food I picked up from some random convenient store."
    show sayori surprise1 ud at dip_short
    s "{size=-5}*ahem!*{w=1.0} Err….{/size}"
    "Suddenly she coughs severely, I see her try to touch her throat."
    mc "I'll drink some more."
    "I think I'm crazy, but I guess grasping the straw is all I can do now."
    "So I take down three glasses of water in one go."
    show sayori smile1 dd
    "I notice that she's gulping, too. Her facial expression seems a lot easier now."
    "I recall everything she has done after we meet, how do I know that this is actually working, or she's just pretending to not worry me?"
    show sayori smile2 dd
    "I look at the slowly appearing smile on her face."
    "I believe her."
    mc "Any better?"
    "I smile in bittersweet. "
    mc "Just don't touch it, OK? It hasn't healed yet. "
    show sayori reluc2 dd
    s "{size=-5}emmm…{/size}"
    mc "Let me take a look."
    "I walk over to examine her neck."
    show black with dissolve
    "Ghost cyan mist cannot hide her pain. I know what their color are supposed to be."
    "The texture of woven rope has been imprinted into her soft skin in cold blood, turning her inner flesh out."
    "The valley that orbits her neck is not even scabbed yet, and the blood is still seeping out from it, drip by drip."
    "The grain shivers with her every breath, and the fiber that hasn't left her neck yet, is like millions of sharp blades, stabbing into the bottom of my heart without remorse."
    hide black with dissolve
    mc "I'm sorry……"
    show sayori sadsmile4 dd
    s "It's okay, I said it…"
    s "It wasn't your fault."
    show sayori reluc6 dd
    s "{cps=*0.35}{size=-5}It wasn't anyone's fault…{/size}{/cps}"
    "She murmurs to herself. "
    "I take her hands, watching them."
    show sayori weep9 uu at f11
    "Her fingertips are stained with blood, the nail of the index finger from her right hand has been ripped over."
    "Some fiber that still sticks on her thumb, dried to a grilled brown along with the blood. "
    show layer master:
        blur 0
        easeout 1 blur 10
    "Other fingers' condition are probably worse, but I fail to remember more as my eyes water up again."
    show layer master:
        blur 10
        easein 0.3 blur 0
    mc "Are you tired?"
    show sayori reluc3 dd at t11
    s "No."
    "She shakes her head."
    show sayori smile1 du
    s "Let's take a walk outside, I want to take a look at where you live."
    "That's when I realized that she's still wearing her thin pajamas with her bare feet."
    stop music fadeout 1.0
    mc "{cps=*3}That's out of the question!{/cps}"
    mc "At least…"
    "But she just chuckles."
    show sayori smile2 du at laugh_cg_twice
    pause(0.5)
    show sayori laugh2 uu
    s "What are you thinking? It's not like I can get any colder since I'm a spooky ghost!"
    mc "Alright…"
    mc "Just wait a bit."
    mc "I'll go get a coat."
    scene bg bedroom_night with dissolve
    "I rush to the bedroom, open the wardrobe to take out my warmest jacket."
    "Then, just as I was about to close it, I stopped."
    play music shemeditates
    "I grab a beanie"
    mc "Just in case…"
    show sayori smile1 dd at face
    mc "Ahh!!!!"
    show sayori smile2 dd at t11
    s "Hahahahah!!"
    show sayori laugh1 uu
    s "That's {i}two{/i} scores for Sayori!!"
    mc "Really Sayori?"
    show sayori smile2 dd
    s "Aw……you have to learn to watch your back~"
    mc "You'll pay for this."
    show sayori mock3 dd at t22
    s "Well, how about seeing how will you pay for this mess first?"
    show sayori mock3 dd at t33
    pause(0.5)
    show sayori mock3 dd at s33
    "She then begins to check my room, hands behind her back."
    show sayori mock3 dd at t33
    pause(0.5)
    show sayori mock3 dd at t21
    s "Would you look at this?"
    show sayori mock3 dd at t11
    pause(0.5)
    show sayori mock3 dd at s11
    pause(0.5)
    show sayori curious2 ud
    s "Gosh……"
    show sayori surprise1 dd
    s "What even is this?! …"
    show sayori curious1 dd at t11
    mc "You know what you look like?"
    mc "Guess next you're going to put my name on that list of yours, right?"
    mc "{i}President Sayori?{/i}"
    show sayori mock3 dd
    s "You bet!"
    stop music fadeout 2.0
    "I follow her out of the room with the beanie in my hands."
    scene bg doorway_night with dissolve
    "Then I push the doorknob, once again, embrace the cold night."
    "With Sayori behind my back."
    stop music fadeout 1.0
    play sound doorclose
    scene bg street2_night with dissolve
    play music disturbance
    show sayori smile1 dd at t11
    s "So…"
    show sayori curious1 du
    s "Have we been here before?"
    s "It doesn't seem so unfamiliar."
    mc "Yep, I didn't move that far."
    mc "Remember that forest we used to hang out? It's not far from here since it's the suburb."
    show sayori serious1 uu
    s "Err, let me think…"
    show sayori curious3 uu at h11
    s "Ah!"
    s "Is there a lake? Where we buried our time capsule by it?"
    "I smile."
    show sayori curious1 dd
    mc "Yeah, beneath that biggest tree."

    scene black with dissolve
    "We walk past a lonely street lamp as my shadow gets stretched into the darkness behind my back."
    mc "Can others see you?"
    s "I'm not so sure… since I just woke up like hours ago, and haven't seen anyone else besides you."
    mc "You just woke up?"
    "I look at her in confusion. "
    s "Yeah… everything starts to dim, even my eyes were opened, I couldn't see or feel anything."
    s "When I regain my eyesight, well, you're there, sitting in your bedroom, reading something, but I don't think you noticed me, so…"
    mc "So that's how you get your first score."
    s "Ehehe~"
    scene bg street2_night with dissolve
    "We continue to walk under the artificial light."
    "…"
    show sayori curious1 du at t11
    s "What about the festival? What happened after… umm…"
    show sayori reluc3 dd
    pause(0.75)
    show sayori curious1 dd
    s "How's Natsuki and Yuri doing?"
    mc "From what Monika had told me, the atmosphere was utterly down due to the lack of presence, and the visitors were also not that enthusiastic about the sharing, so their activities ended in a rush."
    "I guess I'll just tell her the truth."
    show sayori reluc5 dd at s11
    s "Monika………"
    play music flatline volume 0.2
    mc "What's wrong?"
    show sayori smile4 dd
    s "Em? Oh, it's nothing."
    show sayori curious5 dd
    s "Don't worry about it. What happened to our club after the festival?"
    show sayori weep1 dd
    mc "Well, we disbanded because there weren't enough members, but I don't remember anything specific during that time, I just…"
    mc "don't remember…"
    show black at easein_to_alpha(0, 0.5, 0.15)
    "I gulp."
    "Now that I think of it, that period was like a glass covered with steam, only ambiguous pictures come into my eyes, the rest is nothing but a blur."
    show sayori weep9 dd
    mc "I only attended a few days of school after…… you left."
    show black at easein_to_alpha(0.15, 0.5, 0.3)
    mc "So many things to fix, so many people to inform. I didn't receive any {i}actual{/i} help since I literally got no friends."
    show black at easein_to_alpha(0.3, 0.5, 0.45)
    mc "Hell, even reading those guidelines and filling endless forms were enough to make me a walking dead."
    show black at easein_to_alpha(0.45, 0.5, 0.6)
    pause(1.0)
    show black:
        alpha 0.6
        easeout 0.5 alpha 0.15
    "I stop to catch a breath."
    play music chamberofreflection volume 1.0
    mc "Your seat, your books……{w} your photo on the class wall…{w} too many… too many things to face.{w} I couldn't stay there anymore, so I transferred as fast as I could, just to get away…"
    "……………"
    "Sayori pauses."
    show sayori weep2 dd
    s "What about Natsuki? And Yuri? …………Monika?"
    "A string of familiar names pierces my body, overpowering all my fights and resists.{w} I can't dodge, I can't hide, I can only let the rain of memory soaks me, from inside out."
    mc "I'm sorry…"
    show sayori weep8 dd
    mc "I don't quite remember, I didn't see Natsuki and Yuri after the funeral… I suppose, I don't even remember their expression that day."
    mc "Guess sometimes it's better to just leave a person alone."
    show sayori weep9 dd
    mc "As for Monika…"
    "…"
    "A pair of emerald eyes suddenly emerges in my mind, an empty classroom…."

    "What was that?"
    mc "She was…"

    mc "She's…"
    mc "Gosh, why is it so hard to remember?"
    "I frown, as if some worms slide into my clothes, the discrepancy in the memory questions my brain unstoppably."
    mc "I think… I've had met Monika after that… we talked, like a lot."
    show black at easein_to_alpha(0.15, 0.5, 0.3)
    mc "But it feels like I wasn't there, that I wasn't a part of it."
    show black at easein_to_alpha(0.3, 0.5, 0.45)
    mc "And when I try to remember more of it, the memory just abruptly jumps to my new school part."
    show black at easein_to_alpha(0.45, 0.5, 0.6)
    "It doesn't match, it doesn't make sense."
    stop music fadeout 3.0
    hide black with Dissolve(3.0)
    s "[player]? Are you alright?"
    "She reaches out to my hand."
    show sayori sadsmile6 ud
    s "It must be a tough time for you, but it's OK to forget, maybe it is even a bliss to not remember all of it, right? ……"
    play music Around fadein 2.0
    show sayori smile5 uu
    s "Let's talk about your college!"
    "Her tone is returning to herself."
    mc "…Sure, where do you want me to begin with?"
    show sayori smile2 uu
    s "Start with your new club president!!"
    show white:
        alpha 0
        easein 2.0 alpha 1.0
    mc "Huh?! …That's ……"
    "We walk and talk, from my roommates to our new library, from that twisted statue in the campus to the dust deserting their steel eaves."
    "I mention to her that I am keeping a sunflower in my room, and that big fat cat can't even roll herself over thanks to the students' treat… and some weird fellow sitting behind the bushes, drawing the flow of life. "
    "……And of course, my new club president. "
    "There's still a literature club in my college, which is a good thing. "
    "Although everyone seems to prefer talking about novels and movies, I still keep the habit of writing poetry."
    "I tell Sayori about the notebook I was reading earlier, I keep every one of her poems there, along with my mindless sentences and phrases,"
    "from moist to dry, from dry to moist, all the way down until the end of the last page, until what's behind the back cover."
    "Dozens? Hundreds? Maybe thousands? I can't quite remember, just as I can't remember how many hours in four years one month plus one day, nor how many seconds in thirty thousand seven hundred and eighty-four hours."
    "Time never gives you a break, I was lingering in my comfort zone a minute ago, then I got thrown away into a place where two parallel lines meet a minute after, chasing the glassy butterfly at the edge of my reality. "

    s "[player]?"
    stop music fadeout 2.0
    "She waves her hand before me."
    scene bg schoolgate_day with dissolve
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
    "I cry out loud subconsciously, I feel gazes nailing onto me."
    show sayori curious1 dd:
        alpha 0.3
        easein 0.1 alpha 1.0
    mc "Sayori!!!!!"
    s "Huh?"
    mc "I'm… I'm losing you!!"
    show sayori sadsmile1 ud
    s "What're you talking about? I'm here, dummy…"
    "The curve of her lip is looming in the thin air."
    show sayori sadsmile2 ud
    s "You won't be able to leave me hanging this time, I'll stick to you, wherever you go~"
    "A fortunate cold sweat slips down my forehead."
    mc "I could look for my old uniform, if……"
    show sayori curious2 uu
    s "What about mine?"
    mc "It's okay, I have……"
    "…"
    mc "That's a bad joke…"
    show sayori reluc7 dd
    s "Sorry… I didn't mean to say that."
    show sayori curious6 dd
    s "But don't you have courses to attend?"
    mc "It's nothing, none of them matters."
    show sayori curious1 ud
    s "OooK..."
    s "So, what's next, we head back?"
    mc "No, we have breakfast."
    scene bg loudstreet2_day
    play music shemeditates
    "I stand up and walk forward the moment I finish my sentence."
    show sayori angry1 dd at t11
    s "Hey, wait me!"
    s "What's with the speed?"
    mc "It's a surprise."
    show sayori curious3 uu
    s "Whhaaaaaat??"
    show sayori curious3 dd
    "She trots to the front of me, walking backwards."
    show sayori curious3 dd:
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
    show sayori curious6 dd
    s "What is it??"
    mc "It won't be a surprise if I tell you."
    show sayori surprise1 ud
    s "Pleeease?"
    "She runs around me in pure curiosity."
    mc "Do you feel anything when others run through you?"
    show sayori angry4 dd
    s "“Don't change the subject!”"
    show sayori curious2 dd
    mc "Here we are."
    scene bg bakery_blur with dissolve
    "We walk on the sidewalk for a while before we reach the bakery."
    "A lady is tidying up the mess of the rushing hour."
    mc "Morning, Miss."
    mc "{i}I would like four cinnamon buns.{/i}"
    show sayori happy1 uu at t11
    s "Woooooow!!!"
    "Sayori jumps all around the counters, eventually ending up staring at those decent pastries."
    scene white with Dissolve(3.0)
    "I make my way to the checkout as her typical exaggerating voice echoes in the background."
    "I can hear her wolfing down the food anxiously and those rusty wheels of the school gate grinding against the concrete."
    "We are fired off like an arrow leaving its bow, pointing straight into the school building, with our plastic bags flying behind us."
    scene bg bakery_blur with dissolve
    show sayori smile5 dd at h11
    s "Hurry! Just eat it!"
    "Sayori is radiating her excitement from all over her body, her happiness passes across the end of her hair to reach my palms, then drips all the way down onto those steaming buns."
    "Little nervous, I pay the cashier."
    "When the cashier walks away, I ask Sayori in a low voice."
    show sayori smile1 dd
    mc "She really couldn't hear you."
    show sayori curious1 du
    s "I wonder if Natsuki and Yuri can."
    mc "I'm not so sure about Yuri, but Natsuki…"
    mc "She's probably gonna pass out."
    show sayori curious6 dd
    s "Nah, Nat is not that timid."
    "I wolf down the four of them in one go."
    show sayori smile4 dd
    "Sayori looks at me, satisfied. "
    mc "How was it?"
    show sayori smile5 ud
    s "You bet!"
    "I laugh."
    mc "Fancy anything else?"
    show sayori smile1 ud
    s "Can you handle?"
    mc "It won't hurt to just bring them back."
    show sayori mock3 dd
    s "In that case…"
    show sayori at lhide
    hide sayori
    s "I want this!"
    s "And this!!"
    s "Emmmm…… This one seems good…"
    s "Oh! I almost forget, the cookies!!!"
    "I've just made myself another bad decision…… "
    mc "OK, OK…, that's enough, my fridge's not gonna hold it."
    show sayori mock3 dd at t11
    show sayori at laugh_cg_twice
    s "Ehehe, I just don't see you like this very often~"
    show sayori smile1 dd
    "She looks at me, or rather, the two big shopping bags in my hands."
    scene bg loudstreet2_day with dissolve
    "I can only make up some compromising face."
    "But these pastries are steaming heartily, I guess I will trade anything with the world as long as she's happy."
    scene bg loudstreet3_day with dissolve
    mc "…hu…hu…"
    mc "I can't… hold it… let's take the bus."
    "I lean against the wall to catch my breath."
    show sayori angry1 du at t11
    s "No! You should take more exercise!"
    mc "That's easy for you to say! Don't forget who am I buying this for!"
    show sayori angry5 dd
    s "Alright alright, it won't be that far since we have already walked this long, right?"
    "I take out my phone to check the map."
    "It shows 13.3KM on the GPS."
    show sayori curious3 uu
    s "We walked that far?!"
    "Given this, I refuse to walk a single step."
    show sayori curious2 du at lhide
    pause(0.5)
    hide sayori
    "I drag Sayori to the nearest bus stop."
    " "
    "Unbelievably, again I try to look at the sign, line to line, up and down, but still fail to find my answer."
    "Looks like we have to……"
    "Walk…"
    "I lift up the two bags, stepping forward reluctantly."
    stop music fadeout 2.0
    scene black with dissolve
    pause(1.0)
    scene bg bedroom_day with dissolve
    "…"
    play sound closet
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
    play sound torn
    mc "Oops."
    "I made a mistake by tearing the note to half, the other part sticks to my inner pocket."
    show sayori curious2 dd at t11
    s "What is it?"
    mc "Dunno, it's something I didn't take out while washing."
    "I take off my blazer, turn my pocket over cautiously, and peel the note from it bit by bit."
    "From the thickness of it I could tell that someone folded this a couple of times carefully."
    "There are some words on it…"
    "But they are divided by the crevice."
    "I slowly put the two pieces together, despite soaking up by the water, and staying in my pocket for god knows how long, they are still recognizable."
    "I speak them out subconsciously while reading them."
    "To [player]"
    show sayori curious4 ud
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
    call showpoem (get_poem("poem_y1"))
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
    "I mean, I thought it would be her email address since Natsuki is writing her own, but this isn't an email's format… there are some words there… with strange blanks to split them."
    "Is this some sort of {i}mailing address{/i}? She does prefer this physical edition though…"
    "Maybe it is, but these words are too vague to tell, I can't get exact information from them."
    "I push the chair backwards, then stand up to check Sayori."
    "I sit next to her, her right hand is gently placing on the balcony, seemingly faint under the sunlight."

    "I put mine in hers, matching the outline."

    "Thin fog crawls to the back of my hand like a shadow, gently licking my surging veins."
    play music weresorry
    "A weird pulse starts to spread to my palm, making the blood in my flesh synchronize with something."
    "I stare into her temporary peaceful eyebrows."
    "Storm was wiping the field over along with all the existing orders."
    "Before the overwhelming leaves and grass returned to the ground, there was somebody, sneaking in the rye."
    "Dark machine arms dig into the moist earth from beyond the sky, turning all the straws over, and carve the noise of gasoline into them."
    "Metal wheels rapidly spin, the accuracy of math denies all the compromising and flinching."
    "Seeds, they are forced to stare at their mother's roots, and to watch them get shredded apart by the blades."
    scene black with dissolve
    "Grab, pry, and tear. Cramp, swell, and sting, along with sorrow. Some reflection, then soaking, warmth."
    "Numb smell, covered in weariness, open up to see the night outside, and the black face on the ceiling, the emerald eyes spinning within."

    show bg monika1
    pause(0.15)
    hide bg monika1
    pause(0.5)
    scene bg bedroom_day with dissolve
    show sayori angry6 dd at t11
    s "{size=-5}Uwmmmmm…………{/size}"
    show sayori reluc8 dd
    pause(0.5)
    show sayori angry6 dd
    "I stare at her in silence."
    show sayori reluc8 ud
    s "Awhhhh………"
    s "You finished? "
    s "How long…"
    s "{size=-10}How long have I been sleeping……{/size}"
    "Her voice is extremely hoarse, like sandpaper grinding concrete. The only surviving moisture is struggling inside gravel's siege."
    mc "Not too long, like half an hour."
    "I take the mug by my hand, adjusting its angle until the curve of the ceram completely blocks my view as the chilly liquid streams down my throat."
    "Seeing my throat going up and down, there's an odd understanding tying us together."
    show sayori curious7 ud
    "The brush wipes the dust of chalk off the blackboard, and her voice gets back to limpid, temporarily."
    show sayori reluc3 ud
    s "Did you…"
    show sayori worried3 ud
    s "Did you get in touch with them?"
    mc "I was just about to ask you about that. The letter is not so easy to read. But………"
    "I pause, touching the edge of the mug with my fingers."
    show sayori reluc3 ud
    mc "Can you tell me what happened?"
    show sayori worried3 ud
    pause(0.5)
    show sayori weep9 ud
    "I look at her right into the eyes, light blue turns deep cyan in the darkness, among the surging river in the steep valley and fire in the woods, my thought is finally confirmed."
    show sayori reluc9 ud
    "She looks to the floor, we are all preparing for the upcoming conversation in this dreadful silence."
    "In the end, she responds with a sound that is tiny enough to be a fiber detached from the noose, yet it expands to Leviathan in my ears within a split second, just like the mountains rising and falling behind her back."
    show sayori weep2 ud
    stop music
    s "{cps=*0.3}It's……………Monika…………{/cps}"
    show sayori weep8 ud
    show white:
        alpha 0.2
    with dissolve
    show layer master:
        blur 0
        easein 0.5 blur 10
    "Dialogues from the past suddenly release, emerging in my brain."
    "\"Monika was right…\""
    "\"I should just…\""
    hide white
    show layer master:
        blur 0
    with dissolve
    mc "What"
    mc "did"
    show sayori weep9 ud
    mc "Monika"
    mc "do?"
    "I nail these words out letter by letter, the rest of the sentence gets loaded into my magazine one by one."
    " "
    show sayori weep2 ud at s11
    "She stops for a bit, then all of her emotions burst out uncontrollably."
    show sayori weep5 uu at t11
    play music run
    s "I DON'T KNOW!"
    "Her tears strike my sight along with these three words."
    s "I DON'T KNOW! I DON'T KNOW! I DON'T KNOW!"
    s "IDONTKNOWIDONTKNOWIDONTKNOWIDONTKNOW!!!!!!!!!-----------"

    show sayori at alphaflicker(-2.030)
    "She repeats these words like sleep-talking as the mist from all over her body starts to fade, millions of lines and curves shake along with it, sending her figure out of the window, into the abyss."
    mc "Sayori! Calm… calm down!"
    "I reach out, trying to comfort her."
    show sayori at easein_to_alpha(0.4, 0.15, 0.15)
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
    "{cps=*0.5}A pair of emerald eyes.{/cps}"
    show sayori weep10 dd:
        i11
        easein_to_alpha(0, 0.25, 0.6)
    "She calms a little, no longer shaking as the details in her shadow become clear again."
    show sayori weep6 dd
    s "She was there, she was always there…"
    show sayori weep4 dd
    s "Ever since you joined the club…… she was on the ceiling of every sleepless night, she was at the corner of the empty classroom where I picked up the materials for drawing posters!"
    show sayori weep5 dd
    s "At the doorway! On the kitchen table! Inside my blanket!! ……"
    show sayori weep4 dd
    s "I couldn't figure out who was in the darkness at first, but it gets clearer and clearer…"
    s "The voice said a lot of mean things to me, I was…"
    "I continuously replay the tip of the iceberg she described to me in her bedroom that day."
    show sayori weep10 dd
    s "I don't know. I think I'm crazy, I'm seeing things, that it wasn't Monika speaking…"
    show sayori weep10 ud at sink(a=0.6)
    s "I tried. I tried denying it."
    show sayori weep3 ud
    s "But there was something else, a third voice inside my head."
    s "It welcomed Monika's visit, agreed with everything she said without hesitation."
    s "It took over my body, drove me away. I could do nothing but watching it discussing me with Monika, to comment me, to reconstruct me…"
    s "It had actually always been like this, I'm learning to live with it."
    s "Although it was mean, it won't listen, always thought about taking control over everything…"
    show sayori weep11 ud at sink_more(a=0.6)
    s "But I promised myself to get along with it and we were making progress {size=-2}un{size=-1}til{size=-1}… {size=-1}until{size=-1}…{size=-1}…{size=-1}…{/size}"
    "Her voice becomes more and more unrecognizable as endless sorrow and tears fill her throat, making her unable to talk clearly."
    "I remember that Friday, that was my first time discovering her unusual behavior, then I told…"
    show white at easein_to_alpha(0.27, 0.5, 1.0)
    "I'll try to talk to her, so try not to think about it for now"
    hide white with dissolve
    pause(0.3)
    show sayori weep10 dd
    "I really, really want to know what did Monika say to her."
    "But her streaming tears and hoarse sobbing is the best explanation. "
    mc "It's okay, it's okay… I'm here."
    show sayori at walk_in(a=0.6)
    "I squeeze her hands, trying to warm them."
    "Then I go get another mug of water, drinking as I sit along with her."
    hide sayori with dissolve
    "Still crying, she collapses to me, unsurprisingly goes through my body and lays on the bed."
    "I slowly move away from her as I carry the weight of my heart, avoiding making too much disturbance to her shape."
    "I crouch down to check on her. After confirming her sleep, I sneak out my bedroom, gently close the door."
    stop music fadeout 5.0
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
    scene black with Dissolve(3.0)

    "I zip it up, let out a long sigh of relief before I collapse to the chair."
    "I keep my fingers crossed, stare out the window quietly."
    play music crush fadein 1.0
    "The sky is fascinatingly blue, the remaining clouds all get pushed aside except only one soft jet cloud flying across the whole sky, pointing to the far side of future beyond predictions."
    "Layers of leaves fade from deep to light, onto the top, melting into the moss within the walls."
    "I hear the breath of tranquility."
    "One…"
    "two…"
    "three…"
    "I sit there all the afternoon, watching the shadow of the telegraph pole stretches as the remaining sunset illuminates the horizon to gold."
    "Until the sparkling stars reappear on the night's veil, gentle breeze runs through struggling grass."
    "We camped in the wild, our tent was covered by the wet air of midnight, moths wandered around our camp light as some rustle came out near the lake."
    "We heard animals telling their night tales as wings rushing through the woods."
    "Our body laid back at the entrance of the tent, feeling the uneven ground from under the camping mat."
    "Dirt and shovel composed a symphony, fluffy earth blocks rolled over to the strong roots aside."
    "The diameter of the pit increased, I leaned the warm steel handle against the trunk, erasing my breathless sweat."
    "Beside me, there was Sayori, holding the aged aluminum box with her everlasting smile, which was wrapped with tapes over and over irregularly."
    "I want to take another look~~"
    "No! They said that it can't be opened once it is sealed!"
    "Then tell me what you wrote."
    "Nope."
    "Meanie! Just a little bit."
    "Please?"
    "You can see for yourself after ten years."
    "Tennnnn Yeeeears??? That's so long! Can I check it tomorrow?"
    "Next week?"
    "Next month!"
    "……………………"
    stop music fadeout 2.0
    play music2 int_night volume 0.6
    "Clanging sounds appeared in the pit, then turned soft and blunt(unsure), until this short symphony ended beneath the texture of the shoes."

    scene bg bedroom_night2
    "*ding*"
    "My laptop screen illuminates as there's a message showing at the corner which says I've got a new email."
    "Are you [player]? What are you talking about?"
    "It's Natsuki."
    "I finally decided to send a riddle-like letter to every possible address, telling them that I want to join the literature club and wonder if they know a short coral hair girl, I've heard that she is the vice president."
    "Looks like luck is on my side."
    "I reply to Natsuki to brief the situation, and ask her to contact me on social media to make further conversation. "
    "Striking down the enter, I hold my chin while watching the words on the screen that have already been sent to the other side of the server."
    "I wonder when she will recei…{nw}"


    "Her reply letter comes in almost immediately, looks like she's right in front of her computer."
    "I go to check the profile link she gives me on social media."






    "I turned off my cellphone, taking a deep breath, I turned to Sayori."
    "She really is a heavy sleeper, even without her snoring."
    "I don't feel like waking her up at the moment. So I just take out my phone again to check the time."
    "4:44 am, is it this late already? I didn't know we had such a long chat… and she's not talking about sleeping either."
    "Huh, guess we all are night owls."
    "Just then I feel the hunger inside my stomach. Thinking of it, I haven't eaten anything since noon."
    "I didn't turn my lights on as well, there are only some gloomy street lights from outside."
    scene bg kitchen1_day with dissolve
    play sound fridge
    "I make my way to the kitchen, take out some bread we bought this morning."
    "What should I eat?"
    "I decide to have some of the cookies and animal-shaped buns instead of the cakes, they seem more durable."
    "Holding a glass of hot milk, I return to the bedroom with the steaming food in my hand."
    show black with dissolve
    "I gently open the half-closed door with my feet."
    scene bg bedroom_night with dissolve
    play music Around fadein 1.0
    show sayori sleepy1 dd at t33
    pause(0.5)
    show sayori sleepy2 dd
    pause(0.75)
    show sayori sleepy1 dd
    "Morning, sleepyhead."
    "I place the food on the desk."
    show sayori sleepy4 ud
    pause(0.5)
    show sayori sleepy3 ud
    pause(0.5)
    show sayori sleepy2 ud
    pause(0.5)
    show sayori sleepy1 dd
    s "Awmmmm…… "
    "Noticing she's not completely awake, I turn to take a bite on the cookie."
    "The taste though, is not that good after the freezing."
    "I should have more back at the shop."
    mc "There's good news."
    show sayori sleepy1 ud
    s "Huh………"
    show sayori sleepy5 dd
    s "What is it? ……"
    mc "I've found Nat."
    show sayori curious3 uu at h33
    s "Really??!!!"
    "Suddenly her drowsiness vanishes from her face, and the cheerful smile returns to her eyebrows, as if none of the previous breakdown had anything to do with her."
    "I wish I could keep that smile forever."
    mc "Yeah, I chatted with her a little bit."
    mc "She's attending college in the north now."
    show sayori at t31
    s "Let me talk to her!!!"
    mc "Woow, not so fast. "
    mc "It's ten in the morning, she's got courses to attend."
    show sayori angry1 dd
    s "Then why didn't you wake me?"
    mc "Well, maybe it's because you were sleeping like a dea…"
    mc "Like a heavy sleeper."
    mc "You'll probably still be doing it if I hadn't had breakfast."
    show sayori angry4 dd
    s "Meanie!"
    show sayori serious1 dd
    mc "Alright, alright, my bad. But there's something else that you'll definitely be interested in."
    "I keep saying along with her curious look."
    mc "Yuri is in the exact same college as Natsuki."
    show sayori laugh3 uu
    s "Wow!!! That's so nice! How's their relationship?"
    mc "Welp, you know Natsuki…"
    mc "But I think it isn't as bad as she put it."
    show sayori smile5 du
    s "Thought so, hahah."
    mc "I told her about your…… situation. She will contact Yuri this weekend, and we’ll meet up sometime once we figure out where Monika is."
    show sayori reluc2 dd at s31
    s "…"
    s "Monika………"
    show sayori reluc7 dd
    mc "Yeah, we’re going to confront her. Don’t you want to know what the truth is?"
    "I glance at my backpack."
    show sayori worried3 dd at t31
    s "Alright……"
    show sayori reluc10 dd
    s "But where do we start? It’s been so long."
    show sayori worried3 dd
    mc "We can start with our high school. In fact, weren’t we just about to visit there?"
    "I stand up to tidy my uniform."
    show sayori worried2 dd at s31
    s "Sure, but…"
    mc "What is it?"
    show sayori reluc11 dd at sink_more(240)
    s "I don’t know………"
    stop music fadeout 1.5
    mc "Just don’t think about it too much for now……"
    mc "It won’t hurt to just take a walk around the school."
    show sayori reluc10 dd
    s "I guess…"
    scene street2_day with dissolve
    "We stand in the cold early morning breeze."

    show crowd3 with dissolve

    "A bus slowly stops before the board. I could see crowded people through the bleary window."
    "The decompression valve lets out a rough breath before the hydraulic mechanism brings the door open with a loud clang."
    "People waiting at the bus stop all crowd to the entrance, making the commute even more dense."
    "I hesitate."
    hide crowd3 with dissolve
    show sayori curious1 dd at t11
    mc "How about we take the taxi."
    show sayori curious6 dd
    s "Why though?"
    mc "Errrr… because it’s faster? I don’t want to see the school gate shut when we arrive."
    show sayori serious1 du
    s "Huh……"
    "Without her further question, I pull out my phone to call the cab."
    scene black with dissolve

    "Before long, a white car approaches, driving us to the direction of old days."
    play sound cab loop
    "All the street lights are cut off synchronously, buildings at our sides are also disappearing as they rapidly get pushed backwards, into the grayish blue sky."
    "We are entering the urban area, our pace slows, and the surroundings are becoming more and more familiar."
    "At last, the driver leaves us at the school gate that I will never forget."
    stop sound fadeout 0.5
    scene bg schoolgate_day with dissolve

    show crowd4 with dissolve
    "We’re not late, the first bell hasn't rung yet, students are crowding across the gate, which is very convenient for us."
    show sayori mock3 du at t11
    s "Don’t you get caught~~"
    mc "That’s impossible. "
    mc "Not if you report to the guard."
    show sayori mock4 du
    s "Huh! That depends!"
    "I then take out my student’s ID from back in high school, waving it before her."
    show sayori smile2 dd at focus
    show sayori at focus(640, 0.85)
    s "Ehehe, you look so stupid in this image."
    mc "Who are you to judge me?"
    show sayori angry4 dd at t11
    s "Meanie!"
    "Then we walk through the gate, seemingly not drawing any attention. "
    hide crowd4 with dissolve
    pause(0.1)
    hide sayori with dissolve
    scene bg campus_day with dissolve
    pause(0.2)
    show sayori curious2 ud with dissolve
    s "I can’t believe we’re actually inside!"
    show sayori at t21
    pause(0.5)
    show sayori at t33
    "She runs around under the school building."
    show sayori at t11
    mc "It’s also my first time."

    scene stair1_day with dissolve
    "I step to the entrance of the stairs, looking at those students who are walking in a hurry."
    show sayori curious1 dd at t11
    s "What now? Are you going to attend the classes?"
    mc "I don’t think that’s realistic, given this is not college."
    mc "Let’s just go straight to the club office."
    show sayori sadsmile1 du
    s "Awwww… it’s Mr. Dan, right?"
    s "But what if he doesn’t work here anymore?"
    show sayori curious1 du
    mc "Keep your fingers crossed."

    scene corridor_day with dissolve
    "Standing before the familiar office door, unceasing nervous crawls over me."
    "I take a deep breath, then knock on the door."
    play sound doornock
    show sayori sadsmile1 dd at t11
    s "A bit nervous?"
    mc "Of course."
    show sayori curious5 du
    s "Monika must be feeling the same way when she came here to apply for setting up the club."
    show sayori reluc2 dd
    mc "Don’t mention her."
    hide sayori with dissolve
    "I squeeze my thumb and index finger on my right hand."
    play sound dooropen
    show dan dcurious1 at t11
    "Who are…"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
