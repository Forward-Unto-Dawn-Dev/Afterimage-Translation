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
    "Я смотрю на свою книжную полку в неприглядном углу. Она всё ещё лежит там."
    "Когда я вытащил её, с неё посыпалась пыль."
    play sound page_turn
    "Я медленно переворачивал страницы, затем взял смятую бумажку, развернул её и держал на ладонях."
    "Я вздохнул про себя."
    "И когда воздух вышел изо рта, некогда летающие пылинки стали более заметными под настольной лампой."
    "Самый знакомый почерк в моей жизни лежит там еле различимо, неспособный и вздохнуть. Я попытался сложить его обратно, но моё тело было слишком вялым."
    "Вскоре я встал и пошёл в гостиную."
    scene black with dissolve
    "Сейчас, полагаю, полночь, но я всё ещё хочу прогуляться. Не думаю, что я узнал бы, кто или что ожидает меня в моих снах…{w=0.3} Или же это очередная ночь без всяких снов."
    scene bg doorway_night with dissolve
    "В темноте мне удается дотянуться до дверной ручки."
    mc "Что-ж за день."
    "Я медленно открываю дверь."
    show sayori laugh3 uu at i11:
        zoom 1.5
    hide sayori
    randomperson "{cps=30}БУ-У-У-У-У!{/cps}{nw}"
    "Я был застигнут врасплох. Я отшатнулся назад, к дверному косяку, и с трудом сохранил равновесие."
    "Перевёл дыхание, встал и смотрел на дверной проём."
    "Что происходит? Клянусь, я что-то слышал."
    play music flatline volume 0.5
    scene cg fog with Dissolve(2.0)
    $ persistent.cg2 = True
    queue ambient int_night volume 0.7
    "Некий голубой туман проникает в мою дверь из далёкой темноты снаружи, образуя на последней линии обороны моей памяти самую нежную фигуру."
    "Она медленно вышла из мерцания за пределами моей досягаемости, спустилась с небес, как беспомощная звезда."
    "Я почувствовал солоноватый привкус в горле."
    "Контур начал обретать форму, а затем она помахала рукой пред моими глазами."
    "Кажись, она ошиблась, измерив наше расстояние. Её рука прошла по моему лицу, тонкий туман рассеялся, а затем неохотно собрался воедино."
    scene bg doorway_night with Dissolve(1.0)
    "И когда она наконец отпустила мой взгляд, я увидел несомненно знакомое лицо."
    show sayori sadsmile1 dd at t11 with Dissolve(3.0)
    show sayori worried1 du
    s "{size=-5}Хей… [player]…{/size}"
    "Я изо всех сил старался сохранять спокойствие, но в моей голове переплелись миллиарды струн, стены начали рушиться, оставляя позади свою торжественную высоту."
    play sound hb loop volume 1.0
    show vignette_black at vignetteflicker(-2.030)
    show black at easein_to_alpha(0, 20, 0.8)
    show layer master:
        blur 0
        easein 5 blur 10
    "Мощные приливы в мгновение ока сносят любую крепость."
    "Мое тело дрожало под мощными ударами воздуха, бьющими и крушащими."
    "Я бросаю взгляд на её шею: за полузаметной голубизной нет ничего, кроме безмолвного дверного проема, за которым гуляет морозный ноябрьский ветер."
    "Я пытаюсь вспомнить ещё что-либо, но мои усилия оказываются бесполезными из-за затуманенного взора."
    show sayori worried2 du at f11
    s "{size=-5}[player]… что-то не так?……{/size}"
    "Видя, что я не мог вымолвить ни слова, она, кажется, была малость обеспокоена."
    "Я закрываю глаза, понемногу закатывая их.{w=0.25} Слезы капают на рубашку.{w=0.25} Я не смею их открыть, я не смею это принять."
    show black at easein_to_alpha(0.8, 1.0, 1.0)
    "Мои ноги тонут в зыбучих песках, я поддаюсь нахлынувшим воспоминаниям, позволяю им тянуть меня вниз, прямиком на дно…{w=0.25} И только холодный воздух напоминает мне о моем присутствии."
    scene bg doorway_night with dissolve
    show sayori surprised1 uu at i11
    hide vignette
    hide black with Dissolve(0.0)
    stop sound
    show layer master:
        blur 0
    with Dissolve(0.1)
    s "{cps=*3}Хе-е-ей!{/cps}"
    "Услышав зов её, я без колебаний открываю глаза."
    show sayori sadsmile1 dd
    "Голубая фигура все ещё там…{w=0.25} Туман рассеивается по краям контура, будто она может в любую секунду исчезнуть в бескрайнем мире из-за порыва бури."
    "…"
    "{cps=*0.35}К счастью, сегодня ночью нет ни бури, ни бескрайнего мира.{/cps}"
    "…"
    "…"
    mc "{cps=*0.25}… Сайори?{/cps}"
    show sayori sadsmile1 dd at f11
    s "{size=-5}Здравствуй, [player]! А где это мы?{/size}"
    show sayori curious4 dd at t11
    "Её голос хриплый, но тональность осталась всё той же проникновенной, будто ничего и не изменилось."
    "Я выбирал слова, менял их, обдумывал."
    "Я разглядываю свои тысячи фраз в тысячах строк стихов тысячу раз, пытаясь найти наиболее подходящий способ ей ответить."
    pause(3.0)
    "Наконец, я выпустил длинный вздох."
    mc "{cps=*0.2}Ты и впрямь довела меня до сердечного приступа.{/cps}"
    pause(1.0)
    "Я протянул руку, дабы похлопать её по плечу, но моя рука просто проходит сквозь ее тело, оставив лишь темноту вокруг двери."
    show sayori sadsmile2 ud at f11
    s "{size=-5}Хе-хе… всегда интересно наблюдать, как ты волнуешься.{/size}"
    show sayori sadsmile2 ud at t11
    mc "Эм-м… Я не знаю… Я как раз собирался прогуляться, а ты вдруг…"
    show sayori laugh1 uu at laugh_cg
    s "{size=-5}Ха-ха-ха-хаа!{/size}"
    "Она хихикает, кажется, всё ещё прокручивая в голове ту мою реакцию."
    s "{size=-5}{cps=*2}Ха-ха-ха...{/cps}{/size}"
    pause(1.0)
    show sayori sadsmile1 uu at t11
    s "{size=-5}{cps=*2}Ха-ха....{/cps}{/size}"
    pause(1.0)
    show sayori reluc1 dd at s11
    pause(2.0)
    "Наши взгляды встретились. Её смех начал стихать."
    pause(1.0)
    show sayori weep1 dd
    "Несмотря на то, что мы стояли близко друг к другу, мой взгляд словно перенёсся на тысячу миль, путешествуя прямо к концу времени."
    "Здесь, куда даже свет не мог проникнуть, я наконец нашел небесно-голубые глаза."
    "Хоть они не могли избежать нового оттенка тумана, я помнил их первоначальный цвет."
    "Я видел, как на её глазах накатывались слезы, они впитывались в её подушку, её Мистера Корову, её бумагу под ручкой."
    pause(1.0)
    mc "Что проис...{cps=*0.25}{size=-5}Как дела?..{/size}{/cps}"
    pause(1.5)
    show sayori weep2 dd
    pause(1.0)
    show sayori weep3 dd
    pause(1.0)
    show sayori weep4 uu
    pause(0.7)
    show sayori weep6 uu
    pause(0.5)
    "Она опустила голову, слёзы неудержимо текли сквозь пальцы. Её плечи начали дрожать. В конце концов, она не выдержала и упала на меня."
    hide sayori with dissolve
    "Я потянулся, чтобы обнять её, но в этот момент ничего не мог придумать."
    "Думаю, объятия — это лучшее, что я мог бы сейчас предпринять."
    play sound fall
    "Но она прошла сквозь мое тело, падая на землю,"
    "и вечная печаль накатывает, топит, убивает."
    scene cg fell with dissolve
    $ persistent.cg3 = True
    "Словно молния разрывала моё сердце. Я наклонился, чтобы поднять её и крепко обнять."
    "Но что бы я ни делал, я чувствовал в руках лишь холодный как камень воздух."
    "Её плач — единственное, что раздавалось в моей комнате, её фигура пришла в беспорядок от моих движений, туман становился всё менее и менее заметным."
    "Накатывала паника, и холодок пробегал по моей спине. Я торопливо закрыл входную дверь, затем попытался перестроить туман в её тело, или, скорее, в её форму."
    scene bg doorway_night with dissolve
    show sayori weep7 uu at t11 with Dissolve(1.5)
    "Я положил руку ей на спину, пытаясь успокоить."
    "Я знаю, что физика работает с ней не совсем так, как обычно, и я просто использовал собственную силу, чтобы держать руку в воздухе, дабы соответствовать позе утешения."
    show sayori weep8 uu
    "Я надеялся, что это хоть как-то заставит её почувствовать себя лучше, хотя нисколько не верил, что это тепло до неё дойдет."
    "Но я знал, что она рядом со {b}мной{/b}, и это… это…"
    "{cps=*0.5}Это хорошо.{/cps}"
    $ renpy.music.set_volume(0.2, 20, 'music')
    show sayori weep8 uu at focus
    "Я опустился на колени рядом с ней, но не мог разобрать ни слова из её рыданий."
    "Она закрыла лицо руками, её коралловые волосы упали вниз, закрывая их, а её бантик трясся от невыразимого страха."
    "Внезапно я горько усмехнулся, печаль и скорбь больше не могли сдерживаться в моем горле."
    scene black with dissolve
    "Я помню тот понедельник… стул, лежащий на полу, и тяжесть, когда она упала мне на руки…"
    "Грубая верёвка всё ещё обвивала её шею, словно волк, душащий свою добычу, а в воздухе витал запах высохшей крови."
    "Утренний свет нежно проникал в её окно, но он уже никогда не сможет согреть её замерзшее тело."
    stop music fadeout 5.0
    queue ambient int_night volume 0.8
    scene bg doorway_night with dissolve
    show sayori sadsmile3 uu at t11
    mc "{cps=*0.25}Прос… {/cps}"
    mc "{cps=*0.25}Прости меня…{/cps}"
    "Я снова пытаюсь убедить её в своей вине, но результат тот же."
    show sayori sadsmile3 ud
    s "{size=-5}Всё в порядке.{/size}"
    pause(0.5)
    "Она вытерла слёзы, изо всех сил стараясь сдержать рыдания, а затем подняла на меня взгляд."
    show sayori care1 dd
    s "{size=-5}Это была не твоя вина…{/size}"
    s "{size=-5}Я просто…{/size}"
    "…"
    "......"
    "Её хриплый голос едва можно было узнать, я видел, как её горло сводило судорогой под этим ужасным синяком на шее, как будто верёвка всё ещё была на ней."
    pause(0.5)
    mc "Болит?"
    show sayori peace1 dd at dip_slightly
    "Она кивнула."
    mc "Не говори, ладно? Я принесу воды."
    hide sayori with dissolve
    pause(1.0)
    "Я встал и задумался."
    "Тупица."
    "Я мог лишь неловко повернуться к ней, заметив, что она сжимала край моей куртки."
    show sayori weep9 ud at t11
    "Без особой надежды я потянулся, чтобы взять её руку. Ни с того ни с сего, я успешно поднял её."
    "К сожалению, вскоре я узнал, что она просто подыграла мне."
    "Однако я почувствовал лёгкое ощущение тепла кончиков её пальцев."
    "Но оно исчезло раньше, чем я успел обратить на него внимание."
    mc "{size=-5}{cps=*0.25}Что проис…{/cps}{/size}"
    mc "…как дела?"
    pause(1.0)
    show sayori reluc2 dd
    s "{size=-5}Я… эм-м…{/size}"
    pause(1.0)
    show sayori sadsmile4 du
    s "{size=-5}В порядке.{/size}"
    "Она выдавила улыбку."
    mc "{cps=*0.25}Зачем же ты…{/cps}"
    pause(0.5)
    "Нет, сейчас не время для этого."
    mc "Ты голодна?"
    "Незаметно для себя сказал я в попытке сменить тему разговора."
    show sayori reluc3 dd
    pause(1.0)
    show sayori weep1 dd at s11
    s "{size=-5}Я…{/size}"
    show sayori reluc4 dd
    "Она беспомощно посмотрела в землю."
    "С меня довольно!"
    "Выражение её лица было похоже на тонну камней, навалившихся на мою грудь, мешающих мне дышать."
    "Мне нужно сделать что-нибудь!"
    scene bg kitchen1_night with dissolve
    play sound fridge volume 0.9
    "Я ворвался на кухню, беспомощно роясь в холодильнике."
    "Наконец мне удалось найти что-то, что можно было назвать «едой», прежде чем я положил это в микроволновку и сел за стол."
    "Она прошла за мной на кухню, я включил свет."
    play sound switch
    scene bg kitchen1_day
    show sayori curious1 dd at t11
    "Вот тогда-то я и заметил, что она не стоит на земле, а скорее парит в воздухе."
    show sayori curious2 ud at f11
    s "{size=-5}Ты переехал?{/size}"
    show sayori curious2 ud at t11
    mc "Ага…"
    mc "Я перевелся в другую школу. Я не мог больше оставаться в той."
    "Я смотрю на нее с чувством вины."
    show sayori curious2 ud at t33
    pause(0.5)
    show sayori curious2 ud at f33
    s "{size=-5}А это что?{/size}"
    show sayori curious2 ud at t33
    "Она указывает на мою PS5 в углу."
    mc "А-а… эм-м… Моя игровая консоль."
    show sayori angry1 dd at f33
    s "{size=-5}Хмф! Так ты снова начал в игры играть?{/size}"
    show sayori angry2 du
    s "{size=-5}Держу пари, что ты и в клубы никаких не состоишь!{/size}"
    show sayori angry2 du at t33
    mc "Ну… типа…"
    mc "В колледже проводят много мероприятий, так что…"
    show sayori curious3 uu at h33
    s "{size=-5}Что?!{/size}"
    s "{size=-5}Ты уже в колледже?{/size}"
    mc "Да, после всего…"
    mc "Прошло много времени…"
    show sayori curious2 uu at t33
    s "{size=-5}Как много?{/size}"
    mc "…четыре года…"
    show sayori reluc5 dd at s33
    "…"
    show sayori curious4 dd at t33
    s "{size=-5}Целых… четыре года?{/size}"
    "…"
    show sayori sadsmile3 ud
    s "{size=-5}Взгляни на себя.{/size}"
    show sayori sadsmile3 ud at t11
    show sayori sadsmile5 du at f11
    s "{size=-5}Не причёсанный, не побритый…{/size}"
    "Она подошла ко мне и слегка коснулась моего лица."
    show sayori mock1 du at focus(640, 0.85, 50)
    s "{size=-5}Блин, ты порой ничуть не лучше меня.{/size}"
    "Она, хихикая, провела рукой по моим давно забытым для себя волосам. Но по ощущениям это всего лишь воздух."
    "Я не мог подобрать слов, пока думал об этом. Когда я в последний раз вообще смотрелся в зеркало?"
    s "{size=-5}И как оно в колл…{/size}{nw}"
    play sound microwavefinish
    show sayori curious2 uu at t11
    pause(0.5)
    show sayori curious2 uu at h11
    mc "Дай минутку."
    hide sayori with dissolve
    pause(2.0)
    "Тёплый запах разнёсся по кухне, как только я открыл микроволновку, внося хоть какое-то облегчение в этот холодный вечер."
    "Я подал лапшу на стол, её красный соус кажется особенно интригующим под блекло-оранжевым светом. Должен сказать, от вида этого блюда я даже проголодался."
    show sayori laugh3 uu at t11
    "Казалось бы, её глаза вот-вот засияют, но мне от этого было ничуть не легче. Я положил перед ней вилку."
    show sayori laugh3 uu at h11
    s "{size=-5}Вау! Выглядит о-о-о-о-очень классно!{/size}"
    "Её знакомый вздох звенит у меня в ушах."
    show sayori smile1 ud
    "Знакомая мне Сайори совсем уж вернулась, когда её рука потянулась к вилке и готовилась к резне макарон, как вдруг--"
    show sayori reluc5 dd at s11
    "--неподвижный металл оставался на месте, как верёвка, затянутая в узел."
    "Я сжал кулаки."
    "{i}Да чёрт!{i}"
    "Я мысленно проклинаю эти ебучие макароны, я хочу поджечь стол, я хочу разбить эту бесполезную микроволновку!"
    show sayori sadsmile1 dd at t11
    queue ambient int_night volume 0.6
    play music Around fadein 1.0
    s "{size=-5}Возьми.{/size}"
    show sayori sadsmile4 dd
    s "{size=-5}Ты ведь не поел вовремя, так?{/size}"
    s "{size=-5}Я в этом уверена.{/size}"
    "…"
    "Я улыбнулся."
    mc "Никто меня не знает лучше, чем знаешь ты."
    show sayori mock2 dd
    s "{size=-5}А иначе зачем ты ещё одну вилку с собой взял?{/size}"
    "Я беру вилку, но с трудом могу ею двигать."
    "Вес не поддается никаким измерениям, она завладела моими чувствами. Я не мог сдвинуть ни на дюйм, даже если бы у меня была возможность перемотать день назад."
    show sayori care2 du
    s "{size=-5}Быстрее, остынет.{/size}"
    mc "Ну, сейчас она ещё горячая, ибо я слишком долго её разогревал… и… эм…"
    "Мне хочется влепить себе пощёчину, что за хреновая отговорка?"
    "Так или иначе, я стал есть."
    hide sayori with dissolve
    pause(2.0)
    "Еда."
    pause(1.0)
    "Она была горячевата, но это не та проблема, о которой стоило беспокоиться."
    "Я просто перемешал соус в произвольном порядке и положил в рот всё, что получилось."
    "Количество еды уменьшается, когда последний кусочек фарша исчезает у меня на зубах, слеза упала на тепло, которое осталось на белизне тарелки."
    "Я тянусь за салфетками, а мой рот набит пастой."
    show sayori smile1 uu at t11
    "Сайори сидит за столом, держась за подбородок."
    "Она выглядит… лучше?"
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
