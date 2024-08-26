label af1_main:
    play music interlude fadein 1.0
    scene bg office2 with MultipleTransition([
        False, Dissolve(3.0),
        act1, Pause(4.0),
        act1, Dissolve(3.0),
        True])

    "Наконец, я начал проходить мимо иностранных зданий, фонарей и прилавков, а затем начал произносить свои хорошо отрепетированные реплики этим лживым лицам."
    "Мы достали наши документы, обменялись улыбками, продемонстрировав друг другу зубы, в то время как наши языки разжигали слюну, вплетая вежливые слова в нагнетённую атмосферу."
    "Я взял свой мокрый зонт, лежащий у двери, и, стоя на месте, смотрел на улицу."
    scene bg loudstreet1_night_rain with dissolve
    "Внезапно некая тень приближается к моей спине, я уклоняюсь от ее удара и, пошатываясь, забиваюсь в угол."
    show crowd2 at t33
    "Это оказалась пара старшеклассников, которая прогуливалась по улице, болтая и смеясь."
    "Я кое-что заметил…"
    "Их галстучки…"
    hide crowd2 with Dissolve(3.0)
    "Я смотрел на них, пока эти оттенки красного не стали совсем неразличимыми в дали."
    "Свет моего телефона зачастую играет главную роль на фоне тусклого неба. Я небрежно управлял приложениями одной рукой."
    "В конце концов я выключил GPS и просто вернулся туда, откуда пришёл."
    scene bg house1_night2_rain with dissolve
    "Оранжевый блеск вырисовывал мой силуэт на витринах напротив, а я всё шёл вперёд, опустив глаза в землю."
    "Но ощущение тепла остановило меня прямо посреди дороги, перед тихим двориком."
    "Незнакомая машина была припаркована у дома. Хотя я и стоял в нескольких метрах от неё, жар капота было трудно игнорировать, как и свет за окном."
    "Переливы света окрашивали каждый сантиметр комнаты в свой нежный цвет, и я с трудом мог что-либо разглядеть сквозь мутные окна, но был уверен, что там много людей, которые сидят за большим столом."
    stop music fadeout 2.0
    play sound cheers
    show white with Dissolve(2.0)
    "Должно быть, они ужинали. Средь весёлого смеха и звона столовых приборов вырисовывались двое детей."
    "\"Умеешь готовить? Да ну? Может тебе стоит сказать {i}'жрать'{i}?\""
    "\"Не веришь? Тогда не проси меня даже пробовать!\""
    play sound shower
    "Струя расслабления, исходящая от насадки для душа, стекает по моим векам, задерживаясь на коже."
    "Блики перескакивают с одной капли на другую, создавая покой."
    "Мои нервы, кажется, понемногу успокаивались.{w=0.3} Нет ничего лучше, чем принять воистину горячий душ после напряженного, холодного и дождливого дня."
    stop sound fadeout 1.5
    "\"Ты принесла сегодня свою подушку?\"{w=0.3} Я вытираюсь и открываю дверь."
    stop music
    scene bg house1_night2_rain with vpunch
    queue sound rain volume 0.36
    play sound fall
    pause(0.3)
    play music abyss
    "Я сильно ударился лбом о бетонную стену. Нервы вновь будто играли на виолончели, ледяной воздух безжалостно пронизывал меня до костей."
    "Пытаясь поднять свои веки, я увидел сутулого старика."
    show oldman at t11
    randomperson "Э-эй?"
    "Старик заметил мою реакцию и ещё раз похлопал меня по плечу."
    randomperson "Я вижу ты тут долго стоишь…"
    randomperson "Ждёшь кого-то?"
    mc "Ах! Э-эм…"
    mc "Нет, не совсем… извините, просто ворон считал…"
    show layer master:
        blur 0
        easein 1.0 blur 15
    "У меня начала кружиться голова, уличные фонари... стали такими мрачными, тротуар начал изгибаться, скручиваться, переплетаться, прогоняя мою уродливую фигуру с тихой улицы."
    stop music fadeout 4.0
    stop sound fadeout 4.0
    scene black with Dissolve(3.0)
    show layer master:
        blur 0
    scene bg bedroom_night with Dissolve(1.0)
    play ambient int_night volume 0.8 fadein 3.0
    "Я скучал за столом, поигрывая ручкой."
    "Мой мозг просто не перестаёт прокручивать всё это, картинки падают на стол и разбиваются вдребезги, прежде чем я успеваю их как следует рассмотреть."
    "Я смотрю на свою книжную полку в неприглядном углу, она всё ещё лежит там."
    "Pulling it out, dust begins to wake."
    play sound page_turn
    "I gently turn the pages over, along with the inferior lines, then I pick up the creased paper, unfold it, and hold it on my palms."
    "I sigh to myself."
    "With the air leaving my mouth, the once floated dusts now start to become more visible under my table lamp."
    "The most familiar handwriting in my life lies there faintly, unable to breathe even once. I try to fold it back, yet my body remains limp."
    "Before long, I stand up and walk to the living room."
    scene black with dissolve
    "It's probably midnight now, but I still want to take a walk, it's not like I will be able to know who or what awaits me in my dreams……{w=0.3} Or another night without any dreams."
    scene bg doorway_night with dissolve
    "I manage to reach the doorknob in darkness."
    mc "What a day."
    "I gently open the door."
    show sayori laugh3 uu at i11:
        zoom 1.5
    hide sayori
    randomperson "{cps=30}BOOOOOOOOOOOOO!!!!{/cps}{nw}"
    "I'm caught off guard, stagger back against the door frame, barely maintain my balance."
    "I catch my breath, then stand up to look at the doorway."
    "What's happening? I swear I've heard something."
    play music flatline volume 0.5
    scene cg fog with Dissolve(2.0)
    $ persistent.cg2 = True
    queue ambient int_night volume 0.7
    "Some cyan fog enters my door from the distant darkness outside, forming the tenderest figure in my memory at the last defense line of mine."
    "She slowly steps out of the glim far beyond my reach, descend from the celestial, like a helpless star."
    "I feel a salty taste filling my throat."
    "The outline starts to take form, then she waves her hand before my eyes."
    "Seems like she made a mistake to measure the distance, her hand runs through my face, the thin fog gets disturbed, and then reluctantly gather together again."
    scene bg doorway_night with Dissolve(1.0)
    "When she finally releases my eyesight, an undeniably familiar face reveals."
    show sayori sadsmile1 dd at t11 with Dissolve(3.0)
    show sayori worried1 du
    s "{size=-5}Hey……[player]……{/size}"
    "I try my best to stay calm, but billions of strings all get intertwined inside my head as walls begin falling apart, leaving their solemn height behind."
    play sound hb loop volume 1.0
    show vignette_black at vignetteflicker(-2.030)
    show black at easein_to_alpha(0, 20, 0.8)
    show layer master:
        blur 0
        easein 5 blur 10
    "Overwhelming tides take down every fortress in the blink of an eye."
    "My body trembles under the heavy air hammer, bashing and smashing."
    "I take a glance at her neck, behind her half visible cyan, there's nothing but the silent doorway, facing the freezing breeze of November."
    "I try to remember more, but my efforts become useless behind my blurry eyes."
    show sayori worried2 du at f11
    s "{size=-5}[player],… what's wrong? ……{/size}"
    "Seeing me wordless, she seems to be a bit worried."
    "I close my eyes, forcing them to rotate a little.{w=0.25} Tears drip down to my shirt.{w=0.25} I dare not to open them, I dare not to confirm."
    show black at easein_to_alpha(0.8, 1.0, 1.0)
    "My feet sink down the quicksand, I give in to the surging memory, let them drag me down, down to the bottom…{w=0.25} Only the cold air reminds me of my delicate presence."
    scene bg doorway_night with dissolve
    show sayori surprised1 uu at i11
    hide vignette
    hide black with Dissolve(0.0)
    stop sound
    show layer master:
        blur 0
    with Dissolve(0.1)
    s "{cps=*3}Heyyyy!!!{/cps}"
    "Hearing her call, I open my eyes without any hesitation."
    show sayori sadsmile1 dd
    "The cyan figure's still there……{w=0.25} Fog constantly fades at the edge of the outline, as if she were to disappear into the vast world any second with a blow of a storm."
    "…"
    "{cps=*0.35}Luckily, there's no storm tonight, nor the vast world.{/cps}"
    "…"
    "…"
    mc "{cps=*0.25}…………Sayori?{/cps}"
    show sayori sadsmile1 dd at f11
    s "{size=-5}Hi [player]! Where are we right now?{/size}"
    show sayori curious4 dd at t11
    "Her voice is very hoarse, but her tone remains heart-lifting, as if nothing has ever changed."
    "I chose my words, edited them, considered them."
    "I scrutinize my thousands of phrases in thousand lines of poems thousands of times, trying to find the most proper way to reply to her."
    pause(3.0)
    "Finally, I let out a long sigh."
    mc "{cps=*0.2}You really gave me a heart attack back there.{/cps}"
    pause(1.0)
    "I reach out to pat on her shoulder, but my hand just goes through her body, leaving only the darkness around the door."
    show sayori sadsmile2 ud at f11
    s "{size=-5}Ehehe… it's always so interesting to see you get flustered.{/size}"
    show sayori sadsmile2 ud at t11
    mc "Umm…I didn't know… I was just about to take a walk outside, and you suddenly……"
    show sayori laugh1 uu at laugh_cg
    s "{size=-5}Hahahahahhhh!!{/size}"
    "She lets out a giggle, seems still replaying my earlier reaction."
    s "{size=-5}{cps=*2}Hahahah...{/cps}{/size}"
    pause(1.0)
    show sayori sadsmile1 uu at t11
    s "{size=-5}{cps=*2}Haha........{/cps}{/size}"
    pause(1.0)
    show sayori reluc1 dd at s11
    pause(2.0)
    "Our eyes meet as her laughter begins to dim."
    pause(1.0)
    show sayori weep1 dd
    "Even though we are standing at a close distance, my gaze seems to be carried a thousand miles away, traveling to the end of time."
    "Here where even lights could not reach, I've finally found my sky-blue eyes."
    "Although they are unable to escape the siege of stiff cyan, I remember their original color."
    "I see limpid tears emerge from there, soaking her pillow, her Mr. Cow, her paper beneath her pen."
    pause(1.0)
    mc "What ha...{cps=*0.25}{size=-5}How're you doing? .........{/size}{/cps}"
    pause(1.5)
    show sayori weep2 dd
    pause(1.0)
    show sayori weep3 dd
    pause(1.0)
    show sayori weep4 uu
    pause(0.7)
    show sayori weep6 uu
    pause(0.5)
    "She lowers her head, tears leaking through her fingers unstoppably. Her shoulders begin to tremble, in the end, she can no longer hold it, collapses to me."
    hide sayori with dissolve
    "I reach out to embrace her, there's nothing I can come up with at this moment."
    "I think a hug is the best thing I can do now."
    play sound fall
    "But she goes right through my body as she crashes to the ground,"
    "endless sorrow kicks in, drowning, slaughtering."
    scene cg fell with dissolve
    $ persistent.cg3 = True
    "A lighting tears my heart in half, I crouch down to lift her up, to hug her tightly."
    "But no matter what I do, there's only the stone cold air to respond to me."
    "Her crying is the only thing that echoes in my room, her figure gets stirred to a mess thanks to my movement, the mist is becoming less and less visible."
    "Panic strikes, sending a chill down my spine. I hastily close the front door, and then try to rearrange the fog into her body, or rather, her shape."
    scene bg doorway_night with dissolve
    show sayori weep7 uu at t11 with Dissolve(1.5)
    "I put my hand on her back to comfort her."
    "I know Physics doesn't quite work the way it usually does right now, that I'm just using my own strength to hold my hand in the air to match the pose of comforting."
    show sayori weep8 uu
    "I hope this will somehow make her feel better, even though I don't believe in the slightest that the warmth can reach her side."
    "But I know she's by {b}my{/b} side, and that's ……that's…"
    "{cps=*0.5}That's good.{/cps}"
    $ renpy.music.set_volume(0.2, 20, 'music')
    show sayori weep8 uu at focus
    "I kneel by her side, I couldn't make out a single word from her sobbing."
    "She buries her face in her hands, her coral hair tumbles down to cover them as her bow shakes in unspeakable fear."
    "Suddenly I let out a bitter chuckle, sadness and sorrow could no longer be suppressed under my throat."
    scene black with dissolve
    "I memorize that Monday… the chair lying on her floor, and the weight when she fell to my arms………"
    "The rough rope still tied her neck like a wolf choking its prey, with the dried blood rusting the air."
    "Morning lights gently penetrated her window, but they could never warm her cold body again."
    stop music fadeout 5.0
    queue ambient int_night volume 0.8
    scene bg doorway_night with dissolve
    show sayori sadsmile3 uu at t11
    mc "{cps=*0.25}Sor… {/cps}"
    mc "{cps=*0.25}I'm sorry……{/cps}"
    "Once again I try to reach her, but the result is all the same."
    show sayori sadsmile3 ud
    s "{size=-5}It's fine.{/size}"
    pause(0.5)
    "She wipes her tears away, trying her best to hold the sobbing back, then looks up at me."
    show sayori care1 dd
    s "{size=-5}It wasn't your fault…{/size}"
    s "{size=-5}I just…{/size}"
    "…"
    "......"
    "Her gravelly voice is barely recognizable, I can see her throat struggling under that awful bruise on her neck, as if the rope's still there."
    pause(0.5)
    mc "Does it hurt?"
    show sayori peace1 dd at dip_slightly
    "She nods."
    mc "Don't talk OK? I'll get you some water."
    hide sayori with dissolve
    pause(1.0)
    "I freeze the moment I stand up."
    "Stupid."
    "I can only turn around to face her in awkwardness as I find her clutching the end of my jacket."
    show sayori weep9 ud at t11
    "I reach out to take her hand in mine with disbelief. Out of the blue, hers gets lifted up by me successfully."
    "Sadly, there are too many details in my reality, soon I find out that she's just cooperating."
    "However, a small sense of warmth flows out from her fingertips."
    "Yet it disappears before I can pay more attention to it."
    mc "{size=-5}{cps=*0.25}What ha……{/cps}{/size}"
    mc "…How're you doing?"
    pause(1.0)
    show sayori reluc2 dd
    s "{size=-5}I……emmm…{/size}"
    pause(1.0)
    show sayori sadsmile4 du
    s "{size=-5}I'm fine.{/size}"
    "She forces a smile."
    mc "{cps=*0.25}Why…{/cps}"
    pause(0.5)
    "Now's not the time for that."
    mc "Are you hungry?"
    "The sentence pops out my mouth without me noticing as I trying to change the subject."
    show sayori reluc3 dd
    pause(1.0)
    show sayori weep1 dd at s11
    s "{size=-5}I………{/size}"
    show sayori reluc4 dd
    "She look at the ground, helplessly."
    "This is enough!!!"
    "Her expression is like tons of rocks covering my chest, making it impossible for me to breathe."
    "I have to do something!"
    scene bg kitchen1_night with dissolve
    play sound fridge volume 0.9
    "I storm in the kitchen, cluelessly searching in the fridge."
    "Finally I manage to find something that can be called ‘food' before I put them into the microwave, and sit at the table."
    "She follows me into the kitchen, I turn on the light."
    play sound switch
    scene bg kitchen1_day
    show sayori curious1 dd at t11
    "that's when I noticed that she's not standing firmly on the ground, but rather a floating state."
    show sayori curious2 ud at f11
    s "{size=-5}You moved?{/size}"
    show sayori curious2 ud at t11
    mc "Yeah…"
    mc "I transferred to another school. I couldn't stay around there anymore."
    "I look at her in guilt."
    show sayori curious2 ud at t33
    pause(0.5)
    show sayori curious2 ud at f33
    s "{size=-5}What's this?{/size}"
    show sayori curious2 ud at t33
    "She points to my PS5 in the corner."
    mc "Ahh… ummm……That's my gaming console."
    show sayori angry1 dd at f33
    s "{size=-5}Humph! So you began to play games again?{/size}"
    show sayori angry2 du
    s "{size=-5}I bet that you're not attending any clubs either!{/size}"
    show sayori angry2 du at t33
    mc "Well… actually…"
    mc "There are a lot of activities going around in college, so…"
    show sayori curious3 uu at h33
    s "{size=-5}What?!{/size}"
    s "{size=-5}You are in college now???{/size}"
    mc "Yeah, after all……"
    mc "It's been a while…"
    show sayori curious2 uu at t33
    s "{size=-5}How long?{/size}"
    mc "...Four years..."
    show sayori reluc5 dd at s33
    "…"
    show sayori curious4 dd at t33
    s "{size=-5}Already…four years?{/size}"
    "..."
    show sayori sadsmile3 ud
    s "{size=-5}Look at you.{/size}"
    show sayori sadsmile3 ud at t11
    show sayori sadsmile5 du at f11
    s "{size=-5}Didn't comb, didn't shave…{/size}"
    "She walks towards me, mildly touching my face."
    show sayori mock1 du at focus(640, 0.85, 50)
    s "{size=-5}Jeez, you are worse than me sometimes.{/size}"
    "She giggles, running her hand through my long-forgotten hair. However, it feels like nothing but the plain air."
    "I'm speechless, thinking of it, when was the last time I looked in a mirror?"
    s "{size=-5}So, what does co…{/size}{nw}"
    play sound microwavefinish
    show sayori curious2 uu at t11
    pause(0.5)
    show sayori curious2 uu at h11
    mc "Wait here."
    hide sayori with dissolve
    pause(2.0)
    "Warm smell spreads out all over the kitchen as soon as I open the microwave, bringing at least some ease to this cold night."
    "I put the pasta onto the table, its red sauce seems especially intriguing under the orange light. I have to say, this even makes me hungry."
    show sayori laugh3 uu at t11
    "Her eyes are just about to beam, but it doesn't ease me a bit. I put a fork before her."
    show sayori laugh3 uu at h11
    s "{size=-5}Wow! This looks reeeeaaally nice!!!{/size}"
    "Her familiar gasp rings by my ears."
    show sayori smile1 ud
    "The Sayori I know fully comes back as her hand reaches the fork and prepares a pasta massacre when suddenly--"
    show sayori reluc5 dd at s11
    "--the motionless metal stayed where it was like a rope tightening its knot."
    "I clench my fists."
    "{i}God damn it!!!{i}"
    "I curse the fuckin' pasta in my mind, I want to burn the table, I want to crash the useless microwave!!!"
    show sayori sadsmile1 dd at t11
    queue ambient int_night volume 0.6
    play music Around fadein 1.0
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
    pause(2.0)
    "The food."
    pause(1.0)
    "It is a bit hot, to say the least. But it's not my problem to worry about."
    "I just mix up the sauce with random-intertwined curves, and stuff whatever it turns out to be into my mouth."
    "Their density decreases in my plate, when the last minced meat vanishes behind my teeth, a tear drops to the warmth that lingers above the whiteness. "
    "I reach out to take some napkins with my mouth full of pasta."
    show sayori smile1 uu at t11
    "Sayori sits across the table, holding her chin. "
    "She seems……better?"
    show sayori smile1 uu at f11
    s "{size=-5}Your cooking is not so bad after all…{/size}"
    show sayori smile1 uu at t11
    show sayori smile1 du
    "She taps her finger on the table as her legs dangle below it."
    show sayori smile2 du
    "Her smile looks so beautiful under the only light that illuminates this empty room."
    mc "How do you know?"
    "I gulp down some water, wiping my face with the napkin."
    show sayori curious1 du at f11
    s "{size=-5}Emmmm, I don't know.{/size}"
    show sayori smile3 dd
    s "{size=-5}It's just that… watching you eat, makes me feel better.{/size}"
    s "{size=-5}Reminds me what pasta tastes like…{/size}"
    show sayori sadsmile1 dd
    s "{size=-5}I guess?{/size}"
    show sayori smile2 dd
    s "{size=-5}And the look on your face, tells me everything.{/size}"
    show sayori smile2 dd at t11
    mc "Ahaha…"
    "She'll kill me if she knew this was just some random microwave food I picked up from some random convenient store."
    show sayori surprise1 ud at dip_short
    s "{size=-5}*ahem!*{w=1.0} Err….{/size}"
    "Suddenly she coughs severely, I see her try to touch her throat."
    mc "I'll drink some more."
    "I think I'm crazy, but I guess grasping the straw is all I can do now."
    "So I take down three glasses of water in one go."
    pause(1.5)
    show sayori smile1 dd at dip
    "I notice that she's gulping, too. Her facial expression seems a lot easier now."
    "I recall everything she has done after we meet, how do I know that this is actually working, or she's just pretending to not worry me?"
    show sayori smile2 dd
    "I look at the slowly appearing smile on her face."
    pause(2.0)
    "I believe her."
    mc "Any better?"
    "I smile in bittersweet. "
    mc "Just don't touch it, OK? It hasn't healed yet. "
    show sayori reluc2 dd at s11
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
    show sayori sadsmile4 dd at t11
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
    mc "I wipe away my tears."
    show sayori reluc3 dd at t11
    s "No."
    "She shakes her head."
    show sayori smile1 du
    s "Let's take a walk outside, I want to take a look at where you live."
    "That's when I realized that she's still wearing her thin pajamas and her feet are still bare."
    queue ambient int_night volume 0.8
    stop music fadeout 6.0
    mc "{cps=*3}That's out of the question!{/cps}"
    mc "At least…"
    "But she just chuckles."
    show sayori smile2 du at laugh_cg_twice
    pause(0.5)
    show sayori laugh2 uu
    s "What are you thinking? It's not like I can get any colder since I'm a spooky ghost!"
    mc "Alright…"
    mc "Just wait a bit."
    mc "I'll go grab a coat."
    scene bg bedroom_night with dissolve
    play sound closet volume 2.5
    "I rush to the bedroom, open the wardrobe to take out my warmest jacket."
    "Then, just as I was about to close it, I stopped."
    stop sound fadeout 0.5
    play music shemeditates
    "I grab a beanie."
    mc "Just in case…"
    mc "Now back to{nw}"
    show sayori smile1 dd at face
    mc "Ahh!!!!"
    show sayori smile2 dd at t11
    s "Hahahahah!!"
    show sayori laugh1 uu at f11
    s "That's {i}two{/i} scores for Sayori!!"
    show sayori laugh1 uu at t11
    mc "Really Sayori?"
    show sayori smile2 dd at f11
    s "Aw……you have to learn to watch your back~"
    show sayori smile2 dd at t11
    mc "You'll pay for this."
    show sayori mock7 dd at f22
    s "Well, how about seeing how will you pay for this mess first?"
    show sayori mock7 dd at t22
    show sayori mock7 dd at t33
    pause(0.5)
    show sayori mock7 dd at s33
    "She then begins to check my room, hands behind her back."
    show sayori mock7 dd at t33
    pause(0.5)
    show sayori mock7 dd at t21
    pause(0.5)
    s "Would you look at this?"
    show sayori mock7 dd at t11
    pause(0.5)
    show sayori mock7 dd at s11
    pause(0.5)
    show sayori curious2 ud
    s "Gosh……"
    show sayori surprise1 dd
    s "What even is this?! …"
    show sayori curious1 dd at t11
    mc "You know what you look like?"
    mc "Guess next you're going to put my name on that list of yours, right?"
    mc "{i}President Sayori?{/i}"
    show sayori mock9 dd at f11
    s "You bet!"
    stop music fadeout 2.0
    "I follow her out of the room with the beanie in my hands."
    scene bg doorway_night with dissolve
    "Then I push the doorknob, once again, embrace the cold night."
    "With Sayori behind my back."
    stop ambient fadeout 1.0
    play sound closet_close
    scene bg street2_night with dissolve
    play ambient ext_night volume 0.8
    play music disturbance fadein 2.0 volume 1.2
    show sayori smile1 dd at t11
    s "So…"
    show sayori curious1 du at f11
    s "Have we been here before?"
    s "It doesn't seem so unfamiliar."
    show sayori curious1 du at t11
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
    scene cg shadow with dissolve
    $ persistent.cg4 = True
    "We walk past a lonely street lamp as my shadow gets stretched into the darkness beyond me."
    mc "Can others see you?"
    s "I'm not so sure… since I just woke up like hours ago, and haven't seen anyone else besides you."
    mc "You just woke up?"
    "I look at her in confusion. "
    s "Yeah… "
    s "I've had a long, long dream,"
    s "like really long."
    s "Dreamed about lots of stuff."
    s "I remember hearing you talking with someone..."
    s "and then..."
    s "When I regain my eyesight, well, you were there, sitting in your bedroom, reading something, but I don't think you noticed me, so…"
    mc "So that's how you get your first score."
    s "Ehehe~"
    scene bg street2_night with dissolve
    "We continue to walk under the artificial light."
    "…"
    show sayori curious1 du at t11
    show sayori curious1 du at f11
    s "What about the festival? What happened after… umm…"
    show sayori reluc3 dd
    pause(0.7)
    show sayori curious1 dd
    s "How's Natsuki and Yuri doing?"
    show sayori curious1 dd at t11
    "I guess I'll just tell her the truth."
    mc "From what Monika told me, the atmosphere was a little...dim."
    mc "The festival fell apart due to a lack of visitors. Didn't help that the ones were there, didn't really care for it."
    mc "And then, of course...well, you know what happened."
    show sayori reluc5 dd at s11
    s "Monika………"
    mc "What's wrong?"
    show sayori smile4 dd at t11
    s "Em? Oh, it's nothing."
    show sayori curious5 dd at f11
    s "Don't worry about it. What happened to our club after the festival?"
    show sayori weep1 dd at t11
    mc "Well, we disbanded because there weren't enough members, but I don't remember anything specific during that time, I just…"
    stop music fadeout 3.0
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
    play music chamberofreflection volume 0.6
    mc "Your seat, your books……{w} your photo on the class wall…{w} too many… too many things to face.{w} I couldn't stay there anymore, so I transferred as fast as I could, just to get away…"
    "……………"
    "Sayori pauses."
    show sayori weep2 dd
    s "What about Natsuki? And Yuri?"
    s "…………Monika?"
    "A string of familiar names pierces my body, overpowering all my fights and resists.{w} I can't dodge, I can't hide, I can only let the rain of memory soaks me, from inside out."
    mc "I'm sorry…"
    show sayori weep8 dd
    mc "I don't quite remember, I didn't see Natsuki and Yuri after the funeral… I suppose, I don't even remember their expression that day."
    mc "Guess sometimes it's better to just leave a person alone."
    show sayori weep9 dd
    mc "As for Monika…"
    "…"
    "{cps=*0.8}A pair of emerald eyes suddenly emerges in my mind, an empty classroom.......{/cps}{nw}"
    show vignette_black at vignetteflicker
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
    hide vignette_black
    hide black with Dissolve(3.0)
    s "[player]? Are you alright?"
    "She reaches out to my hand."
    show sayori sadsmile6 ud
    s "It must be a tough time for you, but it's OK to forget, maybe it is even a bliss to not remember all of it, right? ……"
    play music Around fadein 2.0
    show sayori smile5 uu at f11
    s "Let's talk about your college!"
    "Her tone is returning to herself."
    show sayori smile5 uu at t11
    mc "…Sure, where do you want me to begin with?"
    show sayori smile2 uu at h11
    s "Start with your new club president!!"
    show white:
        alpha 0
        easein 5.0 alpha 1.0
    mc "Huh?! …That's ……"
    "We walk and talk, from my roommates to our new library, from that twisted statue in the campus to the dust deserting their steel eaves."
    "I mention to her that I am keeping a sunflower in my room, and that big fat cat can't even roll herself over thanks to the students' treat… and some weird fellow sitting behind the bushes, drawing the flow of life. "
    "……And of course, my new club president. "
    "There's still a literature club in my college, which is a good thing. "
    "Although everyone seems to prefer talking about music and movies, I still keep the habit of writing poetry."
    "I tell Sayori about the notebook I was reading earlier, I keep every one of her poems there, along with my mindless sentences and phrases,"
    "from moist to dry, from dry to moist, all the way down until the end of the last page, until what's behind the back cover."
    "Dozens?"
    "Hundreds?"
    "Maybe thousands? I can't quite remember, just as I can't remember how many hours in four years one month plus one day, nor how many seconds in thirty thousand seven hundred and eighty-four hours."
    "Time never gives you a break, I was lingering in my comfort zone just a minute ago, then I got thrown away into a place where two parallel lines meet a minute after, chasing the glassy butterfly at the edge of my reality."
    scene white with Dissolve(3.0)

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
