

init python:
    class PhoneCharacter(object):
        def __init__(self, name, cps, color, is_mc=False):
            super(PhoneCharacter, self).__init__()
            self.name = name
            self.cps = float(cps)
            self.color = Color(color)
            self.is_mc = is_mc
        
        def get_typing_delay(self, message):
            return (len(message) / self.cps) * (1.0 + renpy.random.random())
        
        def __call__(self, message, typing_delay=None, delay=None):
            if typing_delay is None:
                typing_delay =  self.get_typing_delay(message)
            
            if delay is None:
                delay = 0.0
            
            return PhoneMessage(self.name, typing_delay, delay, message, self.color, self.is_mc)

init python:
    class PhoneMessage(object):
        def __init__(self, name, typing_delay, delay, message, color, is_mc):
            self.name = name
            self.typing_delay = typing_delay
            self.delay = delay
            self.message = message
            self.color = Color(color)
            self.is_mc = is_mc
        
        def calculate_cps(self):
            return len(self.message) / self.typing_delay
        
        def __str__(self):
            return self.message
        
        def __unicode__(self):
            return self.message

    class DateSep(object):
        def __init__(self, day, month, year=2021):
            self.day = day
            self.month = month
            self.year = year
        
        def __str__(self):
            from datetime import date
            return date(self.year, self.month, self.day).strftime("%d %b")
        
        def __unicode__(self):
            return str(self)

define mc_msg = PhoneCharacter("[player]", 35.0, "#f7de74", True)
define y_msg = PhoneCharacter("Yuri", 35.0, "#be91f9")
define s_msg = PhoneCharacter("Sayori", 21.0, "#a00")
define n_msg = PhoneCharacter("Natsuki", 35.0, "#ffbdd6")

init python in phone_framework:
    from store import (
        Frame,
        Borders,
        TintMatrix,
        Transform,
        ui,
        Text
    )

    currently_typing = None

    entries = [ ]
    messages_yadj = ui.adjustment()

    def clear():
        global entries
        entries = [ ]

    class typing(object):
        def __init__(self, entry):
            self.entry = entry
        
        def __enter__(self):
            global currently_typing
            currently_typing = self.entry
            return self
        
        def __exit__(self, *args):
            global currently_typing
            currently_typing = None

    def colored_frame(color):
        child = Transform("phone/message_frame.png", zoom=0.5, matrixcolor=TintMatrix(color))
        return Frame(child, Borders(20, 20, 20, 20))


    def add_text(message, cps, **kwargs):
        return renpy.display.layout.AdjustTimes(
            Text(message, style="chat_textbox_message_text", slow_cps=cps, **kwargs),
            None,
            None
        )

transform show_phone(d):
    subpixel True
    zoom 0.75
    on show:
        alpha 0.0 yoffset 500
        ease_quad d alpha 1.0 yoffset 0
    on hide:
        alpha 1.0 yoffset 0
        ease_quad d alpha 0.0 yoffset 500

screen phone2(name):
    style_prefix "phone2"
    window
style phone2_window is empty:
    background "images/effects/white.jpg"
    size (1280,720)

screen phone(name):
    python:
        phone_framework.messages_yadj.value = float('inf')

    style_prefix "phone"

    window at show_phone(1.25):
        has frame style_suffix "display_window"
        side "t b c":
            use chat_header(name)
            use chat_textbox()
            use messages(phone_framework.entries)

define gui.phone_frame_borders = Borders(14, 36, 14, 53)

style phone_window is empty:
    background Frame(
        Transform("images/phone/phone_background.png", xalign=0.5, yalign=0.5),
        gui.phone_frame_borders
    )
    padding gui.phone_frame_borders.padding
    xalign 0.5 yalign 0.1
    ysize 802 xsize 390

style phone_display_window is empty:
    background "#FFE1ED"
    yfill True xfill True

screen chat_header(name):
    style_prefix "chat_header"

    frame:
        has fixed
        yalign 0.5
        xfill True
        yfit True


        add "images/phone/back.png"
        label _(name) style_suffix "name":
            yoffset 5
        add "images/phone/menu.png":
            xoffset 306
            yoffset 5


style chat_header_frame:
    ysize 53
    background "#474747"
    xfill True
    padding (10, 10)

style chat_header_label_text:
    outlines [ ]

style chat_header_back_button is empty:
    xalign 0.0 yalign 0.5

style chat_header_back_button_text is chat_header_label_text:
    color "#0094FF"
    size 18

style chat_header_name is empty:
    xalign 0.5 yalign 0.5

style chat_header_name_text is chat_header_label_text:
    font "mod_assets/font/fzht.ttf"
    color "#aaa"
    size 22

style chat_header_active is empty:
    xalign 1.0 yalign 0.5
style chat_header_active_text is chat_header_label_text:
    font "mod_assets/font/fzht.ttf"
    color "#0a0"
    size 16

screen message_entry(entry):
    style_prefix "message_entry"

    frame:
        if entry.is_mc:
            xalign 1.0

        background phone_framework.colored_frame(entry.color)
        text entry.message

style message_entry_frame:
    xmaximum 250
    padding (10, 10)

style message_entry_text:
    font "mod_assets/font/fzht.ttf"
    outlines [ ]
    size 18

screen typing_indicator(is_mc):
    style_prefix "message_entry"

    if not is_mc:
        frame:
            background phone_framework.colored_frame(Color("#f2f2f2"))

            has hbox
            yoffset 2
            spacing 3

            text "⚫" at typing_blink(0.0) color "#000" font "DejaVuSans.ttf"
            text "⚫" at typing_blink(0.2) color "#000" font "DejaVuSans.ttf"
            text "⚫" at typing_blink(0.4) color "#000" font "DejaVuSans.ttf"
    else:
        null

transform typing_blink(delay):
    alpha .25
    pause delay

    block:
        ease .2 alpha 0.75
        pause .2
        ease .2 alpha 0.25
        pause (1.2 - 0.6)
        repeat

transform typing_blink2(delay):
    alpha .25
    pause delay

    block:
        ease .2 alpha 1.0
        pause .2
        ease .2 alpha 0.0
        pause (1.1 - 0.6)
        repeat

screen messages(entries):
    style_prefix "messages"

    fixed:
        yfill True


        viewport:
            yadjustment phone_framework.messages_yadj
            draggable True
            mousewheel True
            yinitial 1.0
            yalign 1.0
            yfill False

            has frame
            vbox:
                xfill True spacing 5

                for entry in entries:
                    if isinstance(entry, PhoneMessage):
                        use message_entry(entry)
                    if isinstance(entry, DateSep):
                        label "[entry]" style_suffix "date_sep"



                if phone_framework.currently_typing is not None:
                    use typing_indicator(phone_framework.currently_typing.is_mc)

style messages_frame:
    background None
    padding (10, 10)

style messages_date_sep:
    xalign 0.5
    padding (10, 10)

style messages_date_sep_text:
    font "mod_assets/font/fzht.ttf"
    color "#000"
    size 16
    outlines [ ]

label phone(name, phone_entry, start, n=0, hide_phone=True):
    show screen phone(name)

    python hide:
        _window_hide(None)
        phone_framework.clear()

        phone_framework.entries += phone_entry[:start]

        if phone_framework.entries:
            _last_phone_who = phone_framework.entries[-1].name
        elif phone_entry.messages:
            _last_phone_who = phone_entry[start].name
        else:
            _last_phone_who = None

        end = start + n

        for entry in phone_entry[start:end]:
            if _last_phone_who != entry.name:
                pause(renpy.random.uniform(1.0, 3.0))
            else:
                pause(0.5)
            
            if entry.delay > 0.0:
                pause(entry.delay)
            
            with phone_framework.typing(entry):
                pause(entry.typing_delay + 0.5)
            
            phone_framework.entries.append(entry)
            
            _last_phone_who = entry.name

        pause()

    if hide_phone:
        call hide_phone from _call_hide_phone


    return

label phone2(name, phone_entry, start, n=0, hide_phone=True):
    show screen phone(name)

    python hide:
        _window_hide(None)
        phone_framework.clear()

        phone_framework.entries += phone_entry[:start]

        if phone_framework.entries:
            _last_phone_who = phone_framework.entries[-1].name
        elif phone_entry.messages:
            _last_phone_who = phone_entry[start].name
        else:
            _last_phone_who = None

        end = start + n

        for entry in phone_entry[start:end]:
            if _last_phone_who != entry.name:
                pause(renpy.random.uniform(1.0, 3.0))
            else:
                pause(0.5)
            
            if entry.delay > 0.0:
                pause(entry.delay)
            
            with phone_framework.typing(entry):
                pause(entry.typing_delay + 0.5)
            
            phone_framework.entries.append(entry)
            
            _last_phone_who = entry.name

        pause()

    if hide_phone:

        call hide_phone2 from _call_hide_phone2

    return




label hide_phone():
    hide screen phone
    return

init python:
    natsuki_messages = [
        DateSep(21, 11),
        n_msg("[player]?"),
        n_msg("Поверить не могу… это и вправду ты."),
        mc_msg("привет"),
        n_msg("Как ты?"),
        mc_msg("Концы с концами сводил."),
        n_msg("М-да…"),
        n_msg("Сколько ж времени прошло?"),
        n_msg("Года 4?"),
        mc_msg("Ага"),
        mc_msg("Четыре года."),
        n_msg("Где учишься теперь?"),
        mc_msg("Всё ещё здесь."),
        mc_msg("В нашем городе."),
        mc_msg("Забавно наблюдать, когда ты думаешь об этом."),
        mc_msg("Я перевёлся, забросил литературный клуб,"),
        mc_msg("и всё таки как-то остался в этом проклятом городке. Не осмелился двигаться дальше."),
        n_msg("А колледж изменил вообще что-то?"),
        n_msg("Ну в плане"),
        mc_msg("Я понял."),
        mc_msg("По сравнению со старшей школой -- да, учитывая, что моя старшая школа была тем ещё кошмаром."),
        mc_msg("но…"),
        mc_msg("Всё то более не будет прежним."),
        n_msg("Прости."),
        mc_msg("Не извиняйся."),
        mc_msg("Я пришёл в себя после стольких лет."),
        mc_msg("В этом на деле нет ничьей вины."),
        mc_msg("Ха."),
        mc_msg("Да и ты, я вижу, знатно изменилась."),
        mc_msg("Не знаю такую Нацуки, которая бы так легко извинялась."),
        n_msg("{image=images/phone/emoji1.png}"),
        mc_msg("хаха, ну ладно, а у тебя как в колледже?"),
        n_msg("Да нормально, наверное."),
        n_msg("Соседи по комнате порой хрень творят."),
        n_msg("Но для меня также хорошо было уйти от…"),
        n_msg("ты понял."),
        mc_msg("{image=images/phone/emoji2.png}"),
        mc_msg("Приятно слышать."),
        mc_msg("Надеюсь ты их слишком сильно не хреначила."),
        n_msg("Ха ха ха."),
        mc_msg("А в целом как оно?"),
        mc_msg("Ну и это"),
        mc_msg("где вообще колледж твой?"),
        n_msg("На севере далеко, в Риверсауте."),
        mc_msg("Блиин…"),
        mc_msg("И вправду далековато."),
        mc_msg("Вроде на северо-востоке холодновато."),
        n_msg("Это ты так думаешь."),
        n_msg("Снег тоже найс"),
        n_msg("Белизна эта сердце умиротворяет."),
        mc_msg("Своего рода поэтическая пауза, да?"),
        n_msg("Я, если ты ещё не в курсе, член литературного клуба."),
        mc_msg("{image=images/phone/emoji2.png}"),
        mc_msg("Снег идёт щас?"),
        n_msg("да"),
        n_msg("Весь день в общаге сижу."),
        n_msg("Ветер продолжает в окно колотить, издавая звук, жутко завывающий."),
        n_msg("Я вообще думала этим вечером за продуктами сходить, но смотря на погоду…"),
        n_msg("Думаю придется подождать, пока не уляжется всё."),
        n_msg("К слову"),
        n_msg("У тебя как с общежитием?"),
        mc_msg("Ну-у."),
        mc_msg("Чел есть, что днями напролёт в игры рубится."),
        mc_msg("Он полюбас решит начать новый раунд, как только у него такая появится возможность."),
        mc_msg("Был один раз, когда он не ложился спать до 4 утра"),
        mc_msg("И всё ещё говорит со своей командой на обычной громкости."),
        mc_msg("Прикинь?"),
        n_msg("Ты говоришь об этом так, будто вообще не играешь в видеоигры."),
        mc_msg("Ну, я и не играю."),
        n_msg("Невозможно."),
        mc_msg("По-честному, это не потому, что я не хочу играть в игры, просто за последние несколько лет не появилось ни одной реально хорошей игры."),
        mc_msg("Компании продолжают выпускать мусор и разочаровывать этим мусором игроков."),
        n_msg("Я не куплюсь на это."),
        n_msg("Если ты в игры не играешь, то что тогда?"),
        n_msg("Ты у нас, [player], любимчик преподов?"),
        n_msg("{image=images/phone/emoji2.png} {image=images/phone/emoji2.png} {image=images/phone/emoji2.png}"),
        mc_msg("{image=images/phone/emoji2.png}"),
        mc_msg("Сейчас я в основном играю в старые игры, да и в том числе у меня не так много времени, чтобы играть в них."),
        n_msg("А чего так?"),
        mc_msg("У меня ещё другие дела есть, вот чего."),
        mc_msg("Дедлайны, которые закрывать надо, оценки, которые надо исправлять, и много-много других таких вещей, которые ждут своей очереди."),
        n_msg("Реально преподский любимчик."),
        mc_msg("{image=images/phone/emoji2.png}"),
        mc_msg("Оч смешно."),
        mc_msg("У меня не вышло хороших оценок на выпускном экзамене в школе, поэтому лучше бы мне постараться получить степень магистра, чтобы шансы повысить."),
        mc_msg("Так что… н-да, много всего сделать надо."),
        n_msg("…поняла, мы ничем и не отличаемся."),
        n_msg("Но всё таки я считаю иногда стоит брать перерыв, ты слишком себя нагружаешь."),
        mc_msg("Пасиб, буду иметь ввиду."),
        n_msg("Ты действительно ничем не занимаешься в свободное время?"),
        mc_msg("Ну не, не совсем. Преувеличил слегка."),
        mc_msg("На самом-то деле,"),
        mc_msg("интересный факт…"),
        mc_msg("Я снова вступил в литературный клуб."),
        n_msg("Хаха!"),
        n_msg("Ну же."),
        n_msg("Расскажи."),
        mc_msg("Я просто искал клубы, чтоб время убить, потому что моё отношение к играм ты уже услышала."),
        mc_msg("Я не был уверен, какой выбрать, пока не увидел литературный клуб."),
        mc_msg("Это сразу стало единственным вариком, даже думать не пришлось."),
        n_msg("Ты разве не был ярым фанатом аниме?"),
        mc_msg("Не."),
        mc_msg("Давно к аниме интерес пропал, да и к манге тоже."),
        mc_msg("Мне просто не хочется... вообще больше смотреть их."),
        mc_msg("Не могу точно описать это."),
        n_msg("Ну раз так… {image=images/phone/emoji2.png}"),
        mc_msg("А ты? Всё ещё Ванильных Девочек коллекционируешь?"),
        n_msg("Есстестна!"),
        n_msg("Они уже часть моей жизни."),
        n_msg("Доставка томов в общагу много времени отнимает, хаха"),
        n_msg("Но оно того стоит."),
        mc_msg("Делишься ими со своими соседями по комнате?"),
        n_msg("Да ни за что на свете!"),
        n_msg("Как у тебя вообще такая мысль появилась?"),
        mc_msg("Оу, ладно, просто предположил."),
        n_msg("Но я и вправду пыталась ими поделиться с другими."),
        n_msg("И тут кое-какая вещь всплывает."),
        n_msg("Я ведь тоже в литературном клубе состою."),
        mc_msg("{image=images/phone/emoji2.png}"),
        mc_msg("Начинает походить на новеллу или что-то типа в этом роде, хех."),
        mc_msg("Мы друг от друга в тысячах миль"),
        mc_msg("Но оба по-прежнему в литературном клубе."),
        n_msg("Вижу явного члена литературного клуба, хаха."),
        n_msg("Чем у себя занимаетесь?"),
        mc_msg("В основном, дискуссии устраиваем."),
        mc_msg("Нам нравится обсуждать фильмы, текста песен, ибо они в отличие от книг легче перевариваются."),
        mc_msg("Иногда мы вместе фильмы смотрим, довольно приятное времяпрепровождение, от некоторых фильмов реально дух захватывает."),
        mc_msg("Больше никаких стихов, это в прошлом."),
        n_msg("Что-ж, я писать ещё не бросила."),
        n_msg("По факту, мы пытаемся помогать друг другу в написании совместной истории."),
        mc_msg("Звучит классно, и о чём сама история?"),
        n_msg("О современной жизни."),
        n_msg("Несмотря на то, что нас всего пятеро, мы все согласны с тем, что истинное счастье можно найти только в реальной жизни, и история, которая несёт в себе самый сильный посыл, тоже будет основана на реальной жизни."),
        n_msg("Вот, за что я так сильно и полюбила Ванильных Девочек."),
        mc_msg("Да... даже с тем фактом что я и читал-то совсем немного, да и было это давно, теперь, когда ты об этом сказала, я вдруг понял, что они пытались донести."),
        n_msg("Тебе бы стоило следить за выпусками."),
        n_msg("Это ведь первоклассное повествование."),
        mc_msg("Хаха, а ты это тоже рекомендовала членам своего клуба?"),
        n_msg("Нуу… было такое."),
        n_msg("Они согласились взглянуть. Ну знаешь, как обычно."),
        n_msg("Я думала они нормальные, но блин…"),
        n_msg("Просто они, видимо, не проявляют особого энтузиазма к этому."),
        n_msg("Не то, что ты…"),
        n_msg("Чёрт, так тяжело порекомендовать людям то, что ты {i}по-настоящему любишь{/i}."),
        mc_msg("Знаешь, я ещё пишу стихи."),
        n_msg("Ты разве сейчас не писал, что в твоём клубе нет поэтических занятий?"),
        mc_msg("Ага, их нет."),
        mc_msg("Я имею ввиду лично себя, не клуб."),
        mc_msg("Всё ещё пишу."),
        n_msg("Ну…"),
        mc_msg("У меня есть блокнот для них, и, думаю, она очень скоро кончится."),
        n_msg("\"Не ярый фанат литературы\", нда?"),
        mc_msg("Я стал заниматься этим, как только Сайори…"),
        mc_msg("покинула нас."),
        mc_msg("Написал там много слов и фраз."),
        mc_msg("на самом деле в основном просто бессвязная болтовня"),
        mc_msg("Но потом,"),
        mc_msg("Типа, где-то в октябре 2019?"),
        mc_msg("Может ноябре?"),
        mc_msg("Честно не особо помню"),
        mc_msg("Тогда-то я наконец и поступил в свой колледж."),
        mc_msg("короче, начал в этом разбираться и обнаружил, что мне это даже интересно."),
        mc_msg("А потому начал писать более приемлемые работы."),
        mc_msg("Выстраивая структуру, подбирая слова…"),
        mc_msg("Играя с ритмом."),
        mc_msg("В последние месяца я малость сбавил темп."),
        mc_msg("Но все равно очень приятно, когда время от времени посвящаешь себя написанию чего-то себе же,"),
        mc_msg("находясь в нужном настроении."),
        mc_msg("Думаю, то, что Сайори затащила меня в литературный кружок, в конце концов было неплохой идеей, хаха"),
        mc_msg("ага"),
        n_msg("Воу…"),
        n_msg("Не ожидала такого от… тебя."),
        n_msg("Ты звучишь прям как Юри."),
        mc_msg("Да ну?"),
        n_msg("Да."),
        n_msg("Кста, мог бы показать парочку работ? Я бы с удовольствием взглянула."),
        mc_msg("Хаха, конечно"),
        mc_msg("но не за просто так"),
        mc_msg("те надо и свои показать тоже {image=images/phone/emoji2.png}"),
        n_msg("…"),
        mc_msg("что? у тебя нет такой?"),
        mc_msg("ой да ну, а я то думал что тебе \"писать не надоест\""),
        n_msg("Да подожди ты!{image=images/phone/emoji1.png}"),
        n_msg("{image=images/phone/pic1.png}"),
        mc_msg("что то типа такого"),
        mc_msg("{image=images/phone/pic1.png}"),
        DateSep(22, 11),
        mc_msg("Ну, похоже на твой стиль… ноо"),
        mc_msg("Должен сказать, стало лучше."),
        n_msg("Эй, я не из тех, кто вечно торчит в прошлом."),
        mc_msg("Приятно это слышать."),
        n_msg("А ты, походу, наконец научился писать полноценные предложения, а не просто набор рандомных слов."),
        n_msg("мои поздравления"),
        mc_msg("Эй, это мое любимое, ты в курсе?"), #?????
        mc_msg("Это прозвучало из песни."), #?????
        n_msg("Океей…{image=images/phone/emoji2.png}"),
        n_msg("Я просто пошутила."),
        n_msg("Могу понять, что ты пытался донести этим стихом…"),
        n_msg("Это приятный штрих."),
        n_msg("Наш город сильно изменился, верно?"),
        mc_msg("Да, магазины всё приходят, всё уходят, а здания всё так возвышаются и так сияют…"),
        mc_msg("Только меня это по-настоящему не колышит, по крайней мере пора."),
        mc_msg("Вот что меня колышит, так это парк."),
        mc_msg("Блин, эти корпорации собираются построить там торговый центр или тип того, поэтому они просто сносят всё."),
        mc_msg("Я тусовался там"),
        mc_msg("с Сайори."),
        mc_msg("Та капсула времени…"),
        mc_msg("Хранит все самые лучшие воспоминания…"),
        mc_msg("Просто понять не могу."),
        n_msg("Имеешь в виду парк возле того ручья?"),
        n_msg("Там была желтая горка?"),
        mc_msg("Да. Он самый."),
        mc_msg("И его больше нет."),
        n_msg("Бля."),
        n_msg("Может я тебя тогда и не знала, но тоже жила в том районе."),
        n_msg("Помню, как мы устраивали там пикник, и именно тогда я впервые попробовала мамины кексы…"),
        n_msg("Ну нахер."),
        mc_msg("Хотелось бы мне вновь откусить кусочек твоего."),
        n_msg("Чего?"),
        mc_msg("Ну, кекса."),
        mc_msg("Ты же их ещё печёшь?"),
        n_msg("Типа того."),
        n_msg("Готовила набор для одной из встреч клуба."),
        n_msg("А поскольку один парень не хочет ни клубничных, ни шоколадных, появилась возможность попробовать приготовить что-то новое."),
        mc_msg("Как такое может быть, что кто-то не любит клубнику и шоколад?"),
        mc_msg("И ты ничего на это не сказала?"),
        n_msg("Не, у него аллергия на них."),
        n_msg("Кроме того, я собиралась попробовать что-то новое в готовке."),
        n_msg("Некоторые кухонные приспособления вообще довольно полезные."),
        n_msg("Так что почему и нет."),
        mc_msg("Погоди, у тебя в общаге кухня есть?"),
        n_msg("Не-а, просто одолжила школьную."),
        mc_msg("У них можно одолжить кухню?"),
        n_msg("Ага, там ещё клуб готовки есть, прикинь?"),
        mc_msg("Ха…"),
        mc_msg("А чего не вступила в него?"),
        mc_msg("Там, должно быть, очень даже весело."),
        n_msg("Готовка это, безусловно, классно…"),
        n_msg("Но литература - это другое."),
        n_msg("Литературный клуб - это в целом другое."),
        mc_msg("Понял."),
        mc_msg("ну так"),
        mc_msg("что ты теперь тогда делаешь?"),
        n_msg("Стараюсь теперь готовить что-то более натуральное."),
        n_msg("Натуральный вкус, без каких-либо приправ."),
        n_msg("Лишь масло, яйца, молоко, сыр..."),
        n_msg("Глянь."),
        n_msg("{image=images/phone/pic2.png}"),
        n_msg("Круассаны — мои любимые. Остальное не так уж и идеально."),
        n_msg("пока что."),
        n_msg("Ещё работаю над ними, детали улучшаются."),
        n_msg("Тебе точно стоит как-нибудь их попробовать."),
        mc_msg("Это точно."),
        mc_msg("Вернёшься на Рождество?"),
        n_msg("Блин…"),
        n_msg("Чуть не забыла."),
        n_msg("Зависит от обстоятельств."),
        n_msg("ХЗ."),
        n_msg("Ничего обещать не могу, потому у меня, ровно как и у тебя, есть дедлайны."),
        n_msg("И для меня это тоже важно."),
        n_msg("И у меня на уме есть одна мысль"),
        n_msg("Что я больше не хочу оставаться в нашем городе."),
        n_msg("Я мог бы просто остаться здесь после окончания университета, найти работу и..."),
        n_msg("Жить."),
        mc_msg("Такая она -- жизнь?"),
        n_msg("Жизнь."),
        mc_msg("Интересно, чем сейчас Юри занимается?"),
        mc_msg("Как у неё там дела обстоят."),
        n_msg("Стала автором журнала."),
        n_msg("И время от времени публикует в своем блоге все свои сочинения."),
        mc_msg("Откуда ты знаешь?"),
        n_msg("Ну, мы в одном колледже учимся."),
        mc_msg("Чего…"),
        mc_msg("Да быть не может…"),
        mc_msg("Ты прикалываешься надо мной."),
        n_msg("нет"),
        n_msg("Я серьёзно."),
        mc_msg("Как?{image=images/phone/emoji2.png}"),
        n_msg("Совпадение наверное."),
        n_msg("Тут есть обе специальности, которые мы хотели выбрать."),
        n_msg("На самом деле, мы впервые приехали сюда одним и тем же путем."), # ?????
        n_msg("Потому что со мной никого нет, а путешествовать одной опасно."),
        mc_msg("Понял…"),
        mc_msg("И как ваши отношения?"),
        n_msg("Мы не так часто видимся, ибо на совершенно разных специальностях учимся."),
        n_msg("Она реально странная, знаешь?"),
        n_msg("Не ответила на мое сообщение."),
        n_msg("А потом вдруг в полночь позвонила и спросила меня о проблемах с ее ноутом…"),
        n_msg("У нее, как всегда, сложный почерк."),
        n_msg("Я вообще не в курсе, что она мне скинуть хотела, и я вообще не хочу проверять ее работы!!!"),
        mc_msg("Но ты все равно это сделала"),
        mc_msg("так?"),
        mc_msg("Ты же упомянула, что она официальный автор."),
        n_msg("Я не хочу читать их или тип того!"),
        n_msg("Просто она, похоже, отчаянно нуждается в совете…"),
        mc_msg("хаха, окей, ладно{image=images/phone/emoji2.png} {image=images/phone/emoji2.png}"),
        n_msg("По крайней мере, она больше не пытается ссориться со мной."),
        n_msg("При условии, что она будет уважать мой стиль и идеи в литературе."),
        n_msg("И это радует."),
        mc_msg("Ага, помню такое, было классно наконец увидеть, что вы с Юри поладили."),
        n_msg("Слушай, [player]."),
        n_msg("Приятно снова общаться с тобой."),
        n_msg("Но я знаю, что ты не мог меня искать просто для того, чтобы поиграться с ностальгией. Тем более после стольких лет."),
        n_msg("Если тебе есть что сказать,"),
        n_msg("скажи."),
        mc_msg("Да."),
        mc_msg("Нет смысла ходить вокруг да около, поэтому сразу к делу."),
        n_msg("Я вся во внимании."),
        mc_msg("Я встретил Сайори."),
        mc_msg("Полагаю, её призрака."),
        n_msg("[player], я знаю, что ты потерял её."),
        mc_msg("Нет, послушай."),
        mc_msg("Это не то."),
        mc_msg("Я собирался отправиться в старый район, разобраться со всеми делами."),
        mc_msg("И я случайно прошёл мимо ее дома."),
        mc_msg("Конечно, все изменилось, теперь там, думаю, живет другая семья, но"),
        mc_msg("в тот вечер я собирался прогуляться."),
        mc_msg("И тут она просто вдруг появилась в дверях, когда я собирался уходить!"),
        mc_msg("Из ниоткуда."),
        mc_msg("Я думаю, это связано с визитом к ней домой."),
        mc_msg("Какие-то связи явно были!"),
        n_msg("…"),
        n_msg("Это шутка?"),
        n_msg("Если да, то, честно говоря, плохая."),
        mc_msg("Зачем мне шутить о ней?!"),
        mc_msg("Я, наверное, могу шутить над каждым в этом чертовом мире, кроме Сайори!"),
        mc_msg("ЭТО ОНА!"),
        mc_msg("Сто процентов!"),
        mc_msg("Извини, отвлёкся."),
        n_msg("Окей… значит, вы оба можете коммуницировать друг с другом?"),
        mc_msg("Да! С языка сняла."),
        mc_msg("Она рассказала мне обо всем!"),
        mc_msg("Обо всём, что осталось тайной."),
        n_msg("Да быть не может…"),
        n_msg("Ты имеешь ввиду… причину?"),
        mc_msg("Убийца!"),
        mc_msg("Это была Моника! Она стояла за всем этим!"),
        mc_msg("ХЗ, помнишь ли ту пятницу перед фестивалем, когда Сайори ушла раньше?"),
        mc_msg("Она была немного не в себе да?"),
        mc_msg("Она улыбалась неискренне и даже не хотела со мной об этом говорить."),
        mc_msg("Поэтому я спросил Монику, заметила ли она что-нибудь неладное."),
        mc_msg("Затем она пошла поговорить с ней."),
        mc_msg("Ты же еще помнишь это, да? Ты и Юри тоже там были."),
        mc_msg("Можешь Юри спросить, уверен, у нее память хорошая."),
        mc_msg("Моника рассказала ей много тревожных вещей, и не только в тот день, похоже и в те выходные, когда они вместе работали над созданием этих брошюр."),
        mc_msg("О, и выходные, когда мы..."),
        mc_msg("кексы готовили."),
        mc_msg("Я навестил ее до того, как ты пришла."),
        mc_msg("Тогда она и призналась мне в своей депрессии."),
        mc_msg("Черт возьми…"),
        mc_msg("Я не должен был оставлять ее в таком состоянии…"),
        mc_msg("не думал, что всё настолько серьёзно."),
        mc_msg("Ты же помнишь, да?"),
        mc_msg("Когда ты собиралась идти домой."),
        mc_msg("Перед моим двором."),
        mc_msg("блин"),
        mc_msg("она пришла…"),
        mc_msg("чёрт…"),
        mc_msg("Я правда не знаю."),
        mc_msg("Что мне делать?"),
        mc_msg("Что я должен был делать?"),
        mc_msg("Я лишь просто смертный!"),
        n_msg("О Боже, успокойся, [player]."),
        n_msg("Ты явно не в себе."),
        mc_msg("Вот почему я и изучаю психологию в колледже."),
        mc_msg("Я хочу стать терапевтом."),
        mc_msg("Я людям хоч помогать."),
        mc_msg("Я хочу знать, что делать, когда происходят такие вещи."),
        mc_msg("Конечно, я порой шутил с тобой, но это другое."),
        mc_msg("и ты права"),
        mc_msg("Я пришел не поболтать, а поностальгировать."),
        mc_msg("И я не имею в виду, что с тобой плохо общаться."),
        mc_msg("но Сайори…"),
        mc_msg("да."),
        mc_msg("Всё о ней."),
        n_msg("Ладно, [player], если ты сейчас серьезно, то и я тоже буду серьёзна."),
        n_msg("Ты уверен, что это не что-то типа послеобраза?"),
        n_msg("Я как-то слышала, что люди могут видеть вещи, посещая места, которые связаны с их травмирующими воспоминаниями."),
        n_msg("Ты изучаешь психологию, так что определенно что-то знаешь об этом."),
        n_msg("Тебе нужно сходить к врачу, это плохо для здоровья."),
        n_msg("Правда."),
        mc_msg("нет"),
        mc_msg("Я не могу."),
        mc_msg("Ты не понимаешь?"),
        mc_msg("Это мой шанс!"),
        mc_msg("Я наконец смогу ей помочь!"),
        mc_msg("Я схожу к врачу"),
        mc_msg("Обещаю."),
        mc_msg("Но не могу сейчас тратить время на терапию."),
        mc_msg("Ибо она здесь."),
        mc_msg("Я не знаю, почему она появилась, и не знаю, когда она исчезнет."),
        mc_msg("Мне страшно, Нац."),
        mc_msg("Мы гуляли этим утром."),
        mc_msg("Она так выглядела…"),
        mc_msg("так трудно было узнать ее под солнцем."),
        mc_msg("И она рассказала мне о Монике, когда мы узнали..."),
        mc_msg("Вернусь к этому позже."),
        mc_msg("У нее случился нервный срыв, она плакала..."),
        mc_msg("ее фигура мерцала, как в аду."),
        mc_msg("Весь этот туман, мгла…"),
        mc_msg("Она может исчезнуть в любую секунду!"),
        mc_msg("Мне нужно поторопиться."),
        mc_msg("Я не могу позволить себе потерять этот шанс…"),
        mc_msg("Я правда напуган"),
        mc_msg("я боюсь потерять её снова"),
        mc_msg("ну то есть не потерять"),
        mc_msg("скорее... подвести"),
        mc_msg("Слушай, Нацуки,"),
        mc_msg("Я говорю об этом очень серьезно, я не шучу."),
        mc_msg("Поверь, возможно, за все эти годы мы и вправду изменились."),
        mc_msg("Но что осталось неизменным — так это моя забота о Сайори."),
        mc_msg("Я бы никогда не стал над ней шутить, даже если я был бы сумасшедшим."),
        mc_msg("И я далеко не сумасшедший."),
        mc_msg("Да я могу даже доказать ее существование."),
        mc_msg("Она сейчас спит на моей кровати, могу фотку сделать."),
        mc_msg("{image=images/phone/pic3.png}"),
        n_msg("Почему ты ее так сотавил придурок?!"),
        n_msg("У нас сейчас середина, блять, ноября! Накинь на неё что-нибудь теплое!"),
        n_msg("И переодень! Это вот такая твоя «забота»?"),
        mc_msg("Я не могу, окей?"),
        mc_msg("Я не могу добраться до…"), # ?????
        mc_msg("ее реальности."), # ?????
        mc_msg("Она же призрак, бога ради!"),
        mc_msg("Я пытался дать ей попить"),
        mc_msg("Хотел приготовить ей поесть"),
        mc_msg("но она не может"),
        mc_msg("даже блядскую вилку взять!!!"),
        mc_msg("и эти чертовы шрамы…"),
        mc_msg("пиздец"),
        mc_msg("Просто увидеть ее такой уже разбило мне сердце."),
        mc_msg("Так что не поднимай эту тему."),
        n_msg("Прости… я же не знала."),
        n_msg("И что собираешься делать теперь?"),
        n_msg("Точнее"),
        n_msg("Что вообще ты МОЖЕШЬ сделать? Учитывая сея обстоятельства."),
        mc_msg("Я не знаю"),
        mc_msg("вообще ни о чем."),
        mc_msg("мы просто гуляем, общаемся."),
        mc_msg("Она сказала, что хочет увидеть нашу школу."),
        mc_msg("Ну и мне удалось достать свою старую форму."),
        mc_msg("И я нашла письмо, которое ты мне писала..."),
        mc_msg("ты и Юри."),
        n_msg("Ох…."),
        mc_msg("Я даже не знал о ней."),
        mc_msg("Прошло уже куча лет с тех пор, как я в последний раз надевал форму."),
        mc_msg("Со школьных пор."),
        mc_msg("Блин, прости меня, Нац."),
        mc_msg("Не то чтобы я не хотел тебе отвечать."),
        mc_msg("Вам обеим."),
        mc_msg("Просто в то время мне приходилось очень тяжело."), # ?????
        mc_msg("и у меня действительно не было возможности увидеть записку.."),
        mc_msg("Если бы я узнал раньше, что вы мне передали его, я бы обязательно ответил…"),
        mc_msg("Как же обидно, он изношен, промок и разорван…"),
        mc_msg("не могу понять, что вы с Юри пытались сказать."),
        mc_msg("Прости меня."),
        n_msg("Тебе незачем извиняться."),
        n_msg("Как ты и сказал, это была ни чья вина."),
        n_msg("С этим нам всем было нелегко справиться."),
        n_msg("Так что всё нормально..."),
        n_msg("Я думаю..."),
        n_msg("Вот как тебе удалось меня найти, не так ли?"),
        n_msg("Я же оставила там свои контакты."),
        mc_msg("Да, реально прикольно"),
        mc_msg("Знаешь, почему я отправил тебе на почту вопрос-загадку?"),
        mc_msg("Я нашёл несколько адресов типа твоего. Не один, а прям несколько."),
        mc_msg("Поэтому не понимал, какой именно твой."),
        mc_msg("А вот у Юри…"),
        mc_msg("Тяжело сказать."),
        n_msg("Ха, я ж уже говорила, она странная."),
        n_msg("Я думаю, это ее почтовый адрес или вроде того, а не е-мэйл, если не ошибаюсь."),
        mc_msg("Агась..."),
        mc_msg("Но это нормально, поскольку вы учитесь в одном колледже, связаться с ней будет легко."),
        n_msg("Ну так…"),
        mc_msg("Ну да. Мне нужно найти Монику."),
        mc_msg("Я собираюсь ей противостоять."),
        mc_msg("И затем"),
        mc_msg("Она за всё заплатит."),
        mc_msg("о да"),
        mc_msg("это я и собираюсь сделать."),
        mc_msg("Ты случаем не в курсе, куда поступила Моника после школы?"),
        mc_msg("Ты как-то поддерживала связь с ней?"),
        n_msg("Я нет… на самом деле."),
        mc_msg("А Юри?"),
        n_msg("Нет..."),
        n_msg("Насколько мне известно, она тоже с ней не контачит."),
        n_msg("Прости, знаешь... как литературный клуб распался, мы стали практически чужими друг для друга."),
        n_msg("Может в школе поспрашиваешь?"),
        n_msg("Преподов?"),
        mc_msg("Ну да... должно сработать."),
        mc_msg("Да и мы как раз собирались пойти туда."),
        mc_msg("Это определённо должно сработать."),
        mc_msg("Я просто спрошу записи у учителя, который клубами заведует."),
        mc_msg("Уверен, в этом списке есть Моника."),
        mc_msg("Я скажу, как только мы чего-нибудь добьемся."),
        n_msg("ОК."),
        n_msg("Поняла."),
        n_msg("Я тоже помогу в поисках Моники."),
        n_msg("Завтра спрошу Юри, не знает ли она что-нибудь."),
        n_msg("И спроси кого-нибудь из моих бывших одноклассников, хотя сомневаюсь, что они реально ответят."),
        n_msg("Но так или иначе."),
        n_msg("Главное - ее найти."),
        n_msg("Тогда и посмотрим, когда мы сможем встретиться."),
        n_msg("Я бы не говорила, что она 'за все заплатит', но, по крайней мере, мы должны знать правду."),
        mc_msg("Разве ты не говорила, что в последнее время занята дедлайнами? Отвлекать не очень бы хотелось."),
        n_msg("Ты и не отвлекаешь."),
        n_msg("Черт возьми, да на самом деле дело не в Монике."),
        n_msg("Я так хочу увидеть Сайори тоже…"),
        n_msg("Поговорить с ней…"),
        n_msg("Она тоже ведь была важным другом для меня, понимаешь?"),
        n_msg("Так помогла мне…"),
        n_msg("Так что печатать не торопись."),
        n_msg("Я приду, чего бы то ни стоило."),
        n_msg("Если не в этом месяце, так в следующем."),
        n_msg("Мне нужно кое-что сказать ей…"),
        n_msg("Я тоже хочу, чтобы она покоилась с миром."),
        mc_msg("Я даже не знаю, как тебя отблагодарить, Нацуки… правда, огромное спасибо. "),
        n_msg("Я все сказала, прекрати печатать, и приступай к делу, пока не поздно."),
        mc_msg("Хорошо."),

    ]

init python:
    group_messages = [
        DateSep(26,10),
        mc_msg("Heyyyyy! Yuri!"),
        y_msg("Please to meet you，[player]。"),
        mc_msg("I'm not [player]!!"),
        mc_msg("I'm Sayori！"),
        y_msg("Hehe, nice joke [player]."),
        mc_msg("{image=images/phone/emoji2.png} {image=images/phone/emoji2.png} {image=images/phone/emoji2.png}"),
        mc_msg("you don't believe? I'm 100% Sayori!"),
        y_msg("Natsuki told me about your situation, are you helping her typing right now?"),
        mc_msg("not exactly."),
        mc_msg("I'm actually {i}controlling{/i} him!"),
        y_msg("Meaning...?"),
        mc_msg("I possessed him"),
        mc_msg("you know what I'm talking about~ every ghost does that"),
        y_msg("Emmm......"),
        y_msg("Is he okay with that?"),
        mc_msg("he's got no say here!"),
        mc_msg("he belongs to me now!"),
        y_msg("Hehe, well okay then."),
        y_msg("I don't think [player] talks like this either."),
        y_msg("So, Sayori, how do you feel?"),
        mc_msg("about what?"),
        y_msg("Returning to the reality."),
        mc_msg("let me think"),
        mc_msg("well its not that cold if I'm being honest "),
        mc_msg("and cinnamon buns are the best~"),
        y_msg("Did [player] take you to the bakery?"),
        mc_msg("yeah, he also cooked some pasta for me"),
        y_msg("Woah, I didn't know he's capable of cooking now."),
        mc_msg("nah its not that delicious honestly speaking, but I want to be nice to him, so don't tell him that."),
        y_msg("Hehe, I'll keep this just between you and me then."),
        mc_msg("where's Nat???"),
        mc_msg("[player] told me a looot about her"),
        n_msg("What did that punk say?"),
        y_msg("Her class should be over soon, but I don't know what she's attending today exactly."),
        mc_msg("Natsuki!!!"),
        n_msg("what is happening here?"),
        mc_msg("it's been soooo long since I talked with you Nat"),
        y_msg(":)"),
        n_msg("Sayori?"),
        n_msg("are you using [player]'s phone rn?"),
        mc_msg("his laptop"),
        n_msg("you sneaked into that machine or something?"),
        mc_msg("I sneaked into him"),
        n_msg("yeesh"),
        mc_msg("ehehe~"),
        n_msg("speak, what did he say about me?"),
        mc_msg("He said Yuri and you have a really nice relationship~"),
        y_msg("That's really sweet of him"),
        n_msg("Did he say that?"),
        mc_msg("what exactly did you say then?"),
        n_msg("Hahah! I told him Yuri is a creep!"),
        y_msg("Natsuki!"),
        n_msg("what do you want me to say then?"),
        n_msg("explain that midnight phone call first!"),
        n_msg("I was about to sleep!"),
        y_msg("My apology."),
        y_msg("My laptop told me to update, so I restarted the system to do so."),
        y_msg("But after that, it just stoped moving, the screen stayed black."),
        mc_msg("ahahah"),
        n_msg("why can't you just google it?"),
        mc_msg("I've never used a laptop before"),
        y_msg("I think you are aware of that, I don't use smartphones."),
        n_msg("Oh come on!"),
        n_msg("It's 2021!"),
        mc_msg("wow"),
        mc_msg("Yuri you don't have a smartphone?"),
        n_msg("how's it possible that there are still people not using smartphones???"),
        y_msg("Yes."),
        y_msg("I always feel that the world of Internet is too shallow and rushing. That's why I decided to not get attached to them as much as possible."),
        mc_msg("Ahhh... but cats and puppies are really cute tho...{image=images/phone/emoji2.png}"),
        n_msg("{image=images/phone/emoji2.png}"),
        n_msg("I won't let her get into that if I were you, she's gonna drive you crazy"),
        y_msg("Even though those lovely animals can really warm our hearts, don't you think that while throwing ourselves into such easy-to-digest contents, the real meaningful contents are although being thrown away by us?"),
        mc_msg("ah..."),
        n_msg("woah woah woah"),
        n_msg("you stop that now"),
        n_msg("did u fix the laptop or not?"),
        n_msg("don't you dare to call me at midnight I'm telling you!"),
        mc_msg("[player] should be good at computers I think"),
        mc_msg("he's the one playing video games all day"),
        y_msg("I brought it to the shop to check for problems later, just got it back to my dormitory today."),
        n_msg("hah, so you don't know about it"),
        y_msg("But the staff there told me that the laptop was actually fine."),
        n_msg("@Yuri maybe it's just you misunderstanding something is all"),
        mc_msg("don't know about what???"),
        n_msg("[player] told me that"),
        n_msg("HE DON'T PLAY GAMES NOW"),
        n_msg("and he learns hard!"),
        n_msg("think you two can have some common language @Yuri "),
        y_msg("What is his major if I may ask?"),
        n_msg("Psychology"),
        n_msg("he's gonna be a therapist one day"),
        mc_msg("wow, he never told me that"),
        mc_msg("why does he want to be a doctor tho?"),
        n_msg("There's a lot he hasn't told you."),
        n_msg("listen to this"),
        n_msg("he said that he thinks his roommates's sound is so loud that he can barely focus on study!"),
        mc_msg("hahahah"),
        mc_msg("oh! speaking of which"),
        mc_msg("he has a gaming console in his kitchen!"),
        mc_msg("he's just bluffing"),
        n_msg("{image=images/phone/emoji1.png}"),
        n_msg("[player], would you mind explaining that?"),
        mc_msg("I only play old games!!!"),
        mc_msg("get back!"),
        y_msg("XD"),
        n_msg("{image=images/phone/emoji2.png}"),
        n_msg("you gonna keep an eye on him"),
        n_msg("see if he really is a hardworking person like he says he is"),
        y_msg("It's quite a surprise to me that [player] would ever want to be a therapist."),
        n_msg("emhmm"),
        n_msg("and he's in a literature club, too"),
        mc_msg("hahaha"),
        mc_msg("really?"),
        n_msg("I'm not gonna lie to you like he does"),
        y_msg("So he hasn't lost his interest in literature?"),
        n_msg("yeah"),
        n_msg("he even writes poems"),
        mc_msg("let me see let me see!"),
        n_msg("{image=images/phone/pic1.png}"),
        y_msg("That's actually not bad."),
        mc_msg("{image=images/phone/emoji2.png}"),
        mc_msg("wow..."),
        mc_msg("so goood"),
        n_msg("Didn't he take you to walk around the neighborhood?"),
        n_msg("How's our hometown now?"),
        mc_msg("Err..."),
        mc_msg("idk"),
        mc_msg("he's moved"),
        mc_msg("we took a walk around the suburb, not our old neighborhood"),
        mc_msg("I think we've been here before"),
        mc_msg("but.. it's not so different, I'd say there are no major changes"),
        y_msg("Where do you used to live?"),
        mc_msg("he said he's gonna take me to dig our time capsule later"),
        n_msg("you buried a time capsule?"),
        n_msg("cool"),
        mc_msg("@Yuri  south-east district"),
        y_msg("Oh, I was a little far from there, I live south."),
        mc_msg("that's gonna be a long walk to school everyday"),
        y_msg("Indeed, I need to get up at six to prepare."),
        y_msg("But I rent a house near our school when preparing for the graduation exam, just for the convenience."),
        n_msg("so you rent a house huh? I didn't attend the exam there"),
        n_msg("I attended it in another province"),
        mc_msg("wow... the graduation exam..."),
        mc_msg("still feels like a far-away thing for me"),
        y_msg("Hehe, indeed it's far away :)"),
        n_msg("yeah, like almost 3 years ago"),
        mc_msg("tell be about it"),
        mc_msg("was it hard?"),
        n_msg("they say that year's exam was pretty hard"),
        n_msg("but I'd say students repeat that line every year"),
        mc_msg("Yuri must have got a nice score!"),
        n_msg("meet the legend herself"),
        n_msg("{image=images/phone/emoji2.png}"),
        y_msg("Ahaha, you are exaggerating, Natsuki."),
        y_msg("But I am proud of myself."),
        y_msg("Didn't make any unnecessary mistakes."),
        n_msg("you always do"),
        mc_msg("do you feel nervous?"),
        n_msg("it was a lot more strict than our usual tests!"),
        n_msg("went through a couple times of security check, and policemen were everywhere"),
        n_msg("just seeing their equipment is already nervous enough for you"),
        y_msg("Natsuki is right."),
        y_msg("Despite it all, I think that by the time you're in there, leaning back in your seat, you'll find your worries won't mean so much anymore. And you'll feel relieved."),
        y_msg("The weather was nicely temperate during our exam days. Neither too hot nor too cold, my palms didn't sweat much."),
        n_msg("yep, even the listening test felt a lot more slower than usual"),
        n_msg("So much better than when they were all buzzing around during the tests at school."),
        mc_msg("is it okay to bring water?"),
        n_msg("yep, but you better put it on the ground, you don't want to accidentally knock the bottle over"),
        n_msg("and it's best if you bring some extra pens"),
        n_msg("ha... what am I talking about exactly..."),
        y_msg("I actually went to the restroom during the math exam."),
        y_msg("There will be a person following you all the way to the restroom door, and when you are done, he will follow you to the classroom."),
        mc_msg("that's creepy"),
        n_msg("humh, there was something creepier!"),
        n_msg("At my place, I heard there was a guy who suddenly stood up and tore the exam paper of another student!"),
        y_msg("Seriously?"),
        mc_msg("that's mean..."),
        mc_msg("why..."),
        n_msg("yeah it's true, even the news reported it"),
        y_msg("How was the problem solved in the end?"),
        n_msg("they gave that student another paper to rewrite his answers"),
        mc_msg("that was horrible..."),
        mc_msg("so how do feel when it's all done?"),
        mc_msg("Must feel quite relief!"),
        n_msg("now that's the strange thing"),
        n_msg("every time someone asks me this question, I always find myself hard to remember how did I exactly feel, or what I exactly did during that time."),
        n_msg("The only thing I remember is how I felt {i}before{/i} the exam, or when I'm preparing for it."),
        n_msg("That summer after that exam was like a blur to me, can't remember anything specific."),
        n_msg("feels like I went for a long sleep, and when I open my eyes again, I'm at my new college!"),
        y_msg("Yes, and this vacation was supposed to be an unforgettable memory that you look forward to for a long time. "),
        y_msg("Am I right?"),
        n_msg("Yes! That's exactly what I want to say!"),
        n_msg("I just can't remember what did I exactly do!"),
        y_msg("Emm... I feel the same way."),
        y_msg("><"),
        y_msg("I think it's a kind of psychological phenomenon."),
        y_msg("Maybe [player] can explain it for us."),
        mc_msg("ehehe, I'll tell him later"),
        mc_msg("speaking of which, how does the north look like exactly?"),
        y_msg("If you mean the cities, they look all the same to me."),
        n_msg("yeah, but the snows are nice"),
        mc_msg("haha... I've always wanted to see snows."),
        mc_msg("we never had one here before"),
        n_msg("you won't be speaking like that when you can barely move your legs in the snow here on our streets"),
        y_msg("Snows here are a little too wild."),
        y_msg("If you want to see the best whiteness, you'd better go to the central area."),
        y_msg("Their beauty there are more gentle yet not too aggressive."),
        n_msg("{image=images/phone/emoji2.png}"),
        n_msg("I see you are a member of the literature club, huh?"),
        n_msg("I told [player] yesterday that I was gonna do some grocery shopping once the snow sets down, but it just keeps blowing and blowing."),
        n_msg("my legs are gonna stuck in the snow again when I go out"),
        mc_msg("it can be that deep?"),
        mc_msg("I want to make a snowman~~"),
        n_msg("oh, one thing's different here"),
        n_msg("we don't have an air conditioner in our dorm"),
        mc_msg("{image=images/phone/emoji2.png}"),
        mc_msg("huh?!"),
        mc_msg("then how do you gonna survive the winter?"),
        mc_msg("it's gonna be dozens of degrees below zero there!"),
        y_msg("We have a central heating system here, I think it is built within the building's structure, it's really warm once you get inside the house. "),
        n_msg("yep it's really warm"),
        y_msg("So you don't have to worry about that."),
        y_msg("Even I have to take off my coat when I'm inside my dormitory."),
        mc_msg("you remind me of that sweater of yours"),
        mc_msg("I always thought you were a person who's afraid of cold"),
        y_msg("You're correct, I still am. ><"),
        y_msg("I'll definitely cover myself up with amounts of clothes if I'm outdoors."),
        n_msg("she's right, she brought this two giant suitcases when we took the train to get here"),
        n_msg("I was wondering if she had brought the books with her, otherwise how's it possible that something will take up so much spaces"),
        n_msg("But she told me they were all her clothes!"),
        n_msg("{image=images/phone/emoji2.png}"),
        mc_msg("you took the train together?"),
        mc_msg("{image=images/phone/emoji2.png}"),
        mc_msg("oh that's right, [player] told me you're in the same collge"),
        mc_msg("I forgot"),
        mc_msg("what a coincidence "),
        y_msg("It is a kind of coincidence."),
        n_msg("emhmm, besides, it was dangerous for me to travel alone, we can look after each other this way"),
        n_msg("although her parents totally took that as a vacation"),
        y_msg("Yes, they even took me shopping. I told them I have to register, and I have many other businesses to deal with, there's just not enough time for that."),
        mc_msg("hahahah"),
        mc_msg("but"),
        mc_msg("Won't you have troubles if you don't use smartphones? "),
        n_msg("that's what u don't understand"),
        n_msg("don't be cheated by her surface"),
        n_msg("she's actually quite impressive!"),
        n_msg("She's a signed author now."),
        n_msg("though I don't know how she convinced the people at registration department to let her go without scanning any QR code"),
        y_msg("I wouldn't call myself a real writer."),
        n_msg("if the magazines don't count, what about the things you posted to your blog?"),
        n_msg("let me show you her pieces"),
        n_msg("{image=images/phone/pic1.png}"),
        n_msg("{image=images/phone/pic1.png}"),
        n_msg("these are just a tip of the iceberg"),
        y_msg("Indeed, they are merely the world build I wrote for my novel."),
        y_msg("I wouldn't call them the main story, they are just some random background stories, and it's not complete yet."),
        mc_msg("awsome..."),
        mc_msg("what kind of novel are you writing?"),
        y_msg("Science fiction."),
        mc_msg("huh"),
        mc_msg("I don't know you're a fan of sci-fi Yuri, I thought you will be writing fantasy or horror."),
        y_msg("I happened to watch a nice movie when I was at third grade in high school, it made me become a fan of science fiction."),
        y_msg("In fact, there is magic elements in my novel, it tells a story about the rivalry between magic and science. "),
        y_msg("But in general, it still is a science fiction. "),
        n_msg("I heard her talking about it with me, I think the structure is too huge, I don't like it"),
        n_msg("it's really hard for normal fellas to feel related to that level of story, you got to focus on the ordinary people."),
        y_msg("Natsuki has a point, I reconsidered my thoughts on that matter after hearing what she said."),
        y_msg("The whole project is at its beginning stage now, so I don't need to rush."),
        y_msg("The details of the story must be abundant whether it's a huge structure or a small one."),
        y_msg("The worst thing about a science fiction is that there are not enough details in the world it builts to take the readers into that story."),
        mc_msg("{image=images/phone/emoji2.png}"),
        mc_msg("wow, you guys are amazing! no wonder you are memebers of the literature club"),
        mc_msg("Natsuki you likes writing complicated things like this now?"),
        n_msg("I'm not!"),
        n_msg("I always perfer the simple style! The most complicated things are the most simple ones you know?!"),
        n_msg("you can try translating things"),
        n_msg("Translating a poem or lyric is a lot more difficult than translating an article "),
        y_msg("I agree with you on that."),
        n_msg("I'm gonna get back to Parfait Girls again"),
        n_msg("it looks like an ordinary manga on the outside, most readers take it as an ordinary one, too"),
        n_msg("but its story can be digged deeper, there's another surface under the surface"),
        n_msg("Parfait Girls can get deep if you want it to be deep, but all kinds of people can enjoy the story no matter it's deep or not."),
        n_msg("That's the \"simple\" I pursue."),
        n_msg("Get it?"),
        n_msg("it's not just simply simple or just simply complicated"),
        y_msg("Hehe, I believe Sayori is going to past out if you keep talking like that."),
        mc_msg("nonono!"),
        mc_msg("I like it, it's intreesting"),
        mc_msg("speaking of which, even [player] joined a literature club, why didn't you two?"),
        n_msg("I did"),
        y_msg("I do know we have a literature club, and I do want to take part in it, but I am really busy this semester, can't arrange the time, so I have to put it down :("),
        n_msg("I was talking with [player] about this the other day"),
        n_msg("@Yuri That's an excuse."),
        n_msg("We won't give you any assignments like your press does."),
        n_msg("it's a place for you to relax, well you can join our discussion if you want, but you also can just sit there if you don't feel like talking"),
        y_msg("How am I going to put this... :("),
        n_msg("you likes to sit alone anyways"),
        mc_msg("are you guys all busy in college?"),
        mc_msg("{image=images/phone/emoji2.png}"),
        mc_msg("I heard you said that [player] is busy"),
        mc_msg("and now Yuri..."),
        n_msg("yeah, it is busy to be honest"),
        mc_msg("uww..."),
        mc_msg("didn't they all say that it would be easier once we went to college"),
        n_msg("it's always easy to give an empty promise"),
        n_msg("Everything you heard that makes you feel comfortable and fills you with excitement and anticipation,"),
        n_msg("are mostly fake."),
        y_msg("I agree with Natsuki."),
        y_msg("I've also learned a lot of things, having come this far from home."),
        y_msg("Life is a lifelong lesson."),
        mc_msg("Are you..."),
        mc_msg("Doing okay?"),
        mc_msg("{image=images/phone/emoji2.png}"),
        n_msg("Don't worry about that, Sayori!"),
        n_msg("maybe I should call you little sister Sayori, considering you are four years younger than us now"),
        n_msg("If life is a lifelong lesson, I will hand in a perfect answer for the final exam."),
        n_msg("I won't let our vice president down."),
        mc_msg("Don't push yourself too hard."),
        mc_msg("You will never let me down."),
        mc_msg("The most happy moment of mine is when we're all together."),
        mc_msg("{image=images/phone/emoji2.png}"),
        mc_msg("So Natsuki."),
        mc_msg("And Yuri, oh and [player] of course, Monika, too."),
        n_msg("Monika......"),
        mc_msg("Though I don't know where Monika exactly is right now"),
        mc_msg("But I believe she can hear."),
        mc_msg("I want you all to loose the weight on your shoulders."),
        mc_msg("Don't push yourself too hard."),
        mc_msg("there aren't so many classes to attend and so many deadlines to catch up"),
        mc_msg("you gotta enjoy your life while you still can"),
        mc_msg("look at those scenaries you described in your poems"),
        mc_msg("how beautiful"),
        y_msg("Thank you, Sayori."),
        y_msg("I won't forget what you said."),
        mc_msg("btw Yuri"),
        mc_msg("{image=images/phone/emoji2.png}"),
        mc_msg("you are so beautiful"),
        mc_msg("did anyone has a crush on you in the college"),
        n_msg("hahahah!!"),
        y_msg("I..."),
        n_msg("Yuri might be good at writing things"),
        n_msg("but when it comes to communicating with people, she has no idea!"),
        y_msg("well"),
        y_msg("this is true"),
        y_msg("actually there's this guy who I believe has interest in me."),
        y_msg("he always wanted to have conversations with me"),
        y_msg("but I always found it hard for me to lay down my guard"),
        y_msg("he also asks me about my novel"),
        y_msg("but I just can't talk with him the way I talk with you"),
        y_msg("uww"),
        n_msg("He asked you out?"),
        y_msg("yeah"),
        y_msg("but I made excuses to avoid it"),
        y_msg("I think I'm going mess it up"),
        mc_msg("jeez"),
        mc_msg("how come"),
        mc_msg("don't think about it too much"),
        mc_msg("just follow your instinct and talk about whatever you feel comfortable with"),
        y_msg("I'll try it next time :)"),
        mc_msg("what about Nat?"),
        mc_msg("{image=images/phone/emoji2.png}"),
        n_msg("me?"),
        n_msg("None."),
        n_msg("I despise those people"),
        mc_msg("ehehe"),
        n_msg("Everything they say is just for fun."),
        n_msg("Wait till I meet someone who's willing to take things seriously."),
        n_msg("I don't like those shallow people."),
        mc_msg("I'm sure you can meet one"),
        mc_msg("and Yuri!"),
        mc_msg("tell me more about that guy!"),
        mc_msg("how you met with him?"),
        y_msg("emm..."),
        y_msg("We take the same course."),
        y_msg("One time, I handed in my homework too late and couldn't get in touch with the teacher. That's when he happened to sit next to me."),
        y_msg("I asked him if he knew any other way to submit it."),
        y_msg("He told me: \"Just use your cellphone, take a picture and send over.\""),
        y_msg("And I told him that I didn't have a smartphone."),
        y_msg("I think that's how I made him interested."),
        y_msg("Then he said: \"Are you that writer everyone talks about?\""),
        y_msg("And I answered: \"Yes, but I'm not that excellent as they described.\""),
        y_msg("We had a little talk about it."),
        y_msg("And then it just became routine for us to find each other after class. We didn't have any other courses scheduled those two weeks, so we ended up talking a lot."),
        y_msg("There's a small pond in our school they rarely maintain, it has a lot of shrubs growing freely."),
        y_msg("That's where we usually wandered to."),
        n_msg("huh, I can't believe you never told me these kinda things"),
        mc_msg("wow"),
        y_msg("But after those weeks went, we were assigned to different schedules. We didn't have the time to meet up as often, so we had less opportunities to talk."),
        y_msg("He asked me for my phone number, I told him I'd prefer if he could send letters instead since I can't talk as well over the phone."),
        y_msg("He didn't write a lot."),
        n_msg("so he ACTUALLY did?"),
        y_msg("Yes, we exchanged letters two times."),
        n_msg("my"),
        n_msg("lucky for you to meet someone like that"),
        n_msg("I won't write a letter if I were him"),
        y_msg("He said he wants to take me to the movies in his recent letter, it's a movie adapted from a science fiction."),
        y_msg("He said he wants to hear my thoughts on that movie."),
        mc_msg("and then?"),
        y_msg("I hesitated..."),
        y_msg("so I refused."),
        y_msg("I've read that novel, actually I was quite interested in seeing an adapted version."),
        n_msg("then why are you rejecting him?"),
        mc_msg("{image=images/phone/emoji2.png}"),
        y_msg("I think it will move our relationship further."),
        y_msg("I am not ready for it yet."),
        y_msg("So I don't want to go out with him so fast."),
        mc_msg("how did he respond?"),
        y_msg("No, he haven't replied yet."),
        n_msg("I have that kinda feeling too"),
        n_msg("If there's a person you can get along with and you have common languages, you will feel relaxed to talk with him when you are not so close."),
        n_msg("But once you started to learn more about each other, you will want to push him away."),
        mc_msg("will you feel guilty"),
        n_msg("yep, it's guilty"),
        n_msg("Guilty for not understanding why you want to push someone you like away."),
        n_msg("But at the same time, you don't want to show him every one of your secrets either."),
        n_msg("so it's complicated"),
        mc_msg("I didn't get it before"),
        mc_msg("now I get it too"),
        mc_msg("sometimes it's best to just keep the balance"),
        mc_msg("it won't end well if you poke a hole in wall"),
        n_msg("btw, how does he look"),
        y_msg("I think he's nice for my liking."),
        mc_msg("{image=images/phone/emoji2.png}"),
        n_msg("do you have a photo"),
        y_msg("no............."),
        n_msg("hahahahahah"),
        n_msg("it's always so fun to tease you!"),
        mc_msg("{image=images/phone/emoji2.png}"),
        mc_msg("come on show us..."),
        y_msg("I really didn't... receive any..."),
        n_msg("hah, which major his in? I'll go get it for u!"),
        y_msg("Natsuki!"),
        mc_msg("hahaha"),
        mc_msg("oh! btw"),
        y_msg("We are not what you think we are right now..."),
        mc_msg("Natsuki"),
        y_msg("So please don't do that."),
        n_msg("what?"),
        n_msg("@Yuri I know, I was just kidding"),
        mc_msg("[player] told me about your cupcakes!"),
        mc_msg("He said you are a lot better than before!"),
        y_msg("I've been lucky enough to taste them a few times before."),
        mc_msg("wow"),
        mc_msg("I want to taste them too!"),
        mc_msg("where are you Natsuki???"),
        y_msg("Possibly got something to deal with at the moment."),
        mc_msg("what did she make for you?"),
        mc_msg("tell me about it"),
        y_msg("Natsuki didn't limit herself by only making cupcakes."),
        y_msg("She has tried making all kinds of pastries."),
        mc_msg("uhm"),
        y_msg("Last time she showed me the Croissant she made."),
        y_msg("Very delicate."),
        mc_msg("delicate?"),
        y_msg("Yes, it's delicate just looking at it."),
        y_msg("{image=images/phone/pic2.png}"),
        y_msg("Of course, the taste is impeccable, too."),
        mc_msg("{image=images/phone/emoji2.png}"),
        mc_msg("aww, I want to have one too"),
        n_msg("I'm back!"),
        n_msg("got a phone call"),
        n_msg("@Yuri what did I tell you, it's good right!"),
        y_msg("Hehe, God's honest truth."),
        mc_msg("When will you come over Nat!"),
        mc_msg("I miss you guys!"),
        y_msg("Did you find where Monika is?"),
        mc_msg("we can go picnic!"),
        mc_msg("remember to bring your famous cupcakes!"),
        mc_msg("it's gonna be interesting, hahah  {image=images/phone/emoji2.png}"),
        n_msg("no, it won't be fresh enough if I make them here"),
        n_msg("{image=images/phone/emoji2.png}"),
        n_msg("I will never call such things \"famous\"!"),
        n_msg("Does [player] still got an oven in his house?"),
        mc_msg("he does, I think I did see one"),
        n_msg("Then I'll come make them there."),
        mc_msg("hooray!"),
        y_msg("What are you going to bake?"),
        n_msg("wait, I'll write you a list, you gonna pick up those materials for me"),
        n_msg("@Yuri I'll make Croissants again, gonna show her my most satisfied dish."),
        n_msg("I've been doing researches on cheese cakes recently, I'll try them out this time too."),
        n_msg("oh and Sayori, aren't you a big fan of cinnamon buns? "),
        mc_msg("Yeah! "),
        n_msg("I haven't tried baking them before, I can do it this time. "),
        mc_msg("Love you the most Nat!!!"),
        mc_msg("{image=images/phone/emoji2.png}"),
        n_msg("{image=images/phone/emoji2.png}"),
        n_msg("Get away from me."),
        n_msg("{image=images/phone/pic1.png}"),
        n_msg("Don't miss anything I'm telling you. "),
        mc_msg("hehe, I won't"),
        y_msg("What's the black tea for?"),
        n_msg("that's a part of the recipe"),
        n_msg("well it's hard to explain, you'll know when you eat it."),
        mc_msg("oh btw"),
        mc_msg("are there any interesting snacks in the north?"),
        mc_msg("almost forgot to ask"),
        mc_msg("you can't bring the cupcakes, at least bring me some of those snacks"),
        y_msg("Have you ever heard of grilled cold noodles?"),
        mc_msg("waht is that"),
        y_msg("It's like grilled egg noodles, but without the egg, and they will mix some other materials like sausages and vegetables in it."),
        mc_msg("sounds like those pancakes they sold at our school gate"),
        n_msg("they are familiar in a way, but grilled cold noodles are spicy, I don't know if they suit your taste"),
        mc_msg("just bring some, it's gonna be [player] eating them anyway, so I wouldn't mind"),
        n_msg("{image=images/phone/emoji2.png}"),
        y_msg("{image=images/phone/emoji2.png}"),
        mc_msg("hahahah"),
        mc_msg("then I'll get something delicious too! let's have a big party!"),
        y_msg("It won't be better if it really happens."),
        n_msg("then I'll go arrange the time with Yuri, we'll send you the time schedule in the group chat, don't forget to pick us up!"),
        y_msg("I have a few drafts to finish too, I'll leave you guys be."),
        n_msg("cool, let's call it a day then, I'm going too"),
        mc_msg("ememm, see you then!"),
        DateSep(28,10),
        mc_msg("I'm [player]!!"),
        mc_msg("Did you book the tickets?"),
        mc_msg("Refund if you did!"),
        mc_msg("listen"),
        mc_msg("I found Monika's college!"),
        mc_msg("but she has already graduated"),
        mc_msg("went to another one"),
        mc_msg("good thing is that she's still in our country"),
        mc_msg("anyway we have to change our destination to there"),
        mc_msg("reply when you receive it"),
        mc_msg("here's a poster that introduces her condition, look"),
        mc_msg("{image=images/phone/pic3.png}"),
        DateSep(27,10),
        n_msg("haven't seen Monika for quite a while."),
        n_msg("I have to say she's getting pretty."),
        n_msg("good thing you told us now, we were just discussing about booking today"),
        n_msg("anyway, I hand over my presentation today, the rest is not so hard to handle"),
        n_msg("Yuri and I could come out on this weekend if anything goes well"),
        n_msg("you should check the airline schedule"),
        n_msg("It would be convenient for us if you can arrange our arriving time closer."),
        n_msg("we'll discuss more once we meet"),
        mc_msg("ok, then I'll go for the booking"),
        mc_msg("{image=images/phone/emoji2.png}"),
        DateSep(28,10),
        mc_msg("good afternoon chat"),
        mc_msg("seeems like it's the off-season recently, so the tickets are quite easy to book"),
        mc_msg("{image=images/phone/pic1.png}"),
        mc_msg("is this time okay with you guys?"),
        y_msg("It couldn't be better."),
        y_msg("We have finished our own businesses as well, just done packing the luggage."),
        y_msg("What is Sayori doing?"),
        mc_msg("she said she's gonna give you a surprise"),
        n_msg("what surprise?"),
        mc_msg("aha, my lips are sealed"),
        n_msg("{image=images/phone/emoji1.png}"),
        y_msg("Hehe, I'll be waiting."),
        mc_msg("Then I'll see you girls on the other side!"),
        n_msg("Good! Call me when you arrive!"),
        y_msg("Okay then. By the way it's getting late, you should get some rest."),
        mc_msg("no prob"),
        DateSep(28,11),
        mc_msg("Sayori and I have arrived!"),
        mc_msg("{image=images/phone/pic3.png}"),
        mc_msg("we are heading to the hotel now"),
        mc_msg("where are you now? {image=images/phone/emoji2.png} {image=images/phone/emoji2.png}"),
        y_msg("Sorry, our flight got delayed, we've just landed."),
        n_msg("I'll never take this company's flights again!"),
        n_msg("bunch of jerks"),
        n_msg("why the sudden nucleic acid testing"),
        n_msg("wasting my time!"),
        n_msg("and this damn whether!"),
        n_msg("it's written on the app that it's supposed to be sunny!"),
        n_msg("Fuck this!"),
        n_msg("{image=images/phone/emoji1.png}"),
        mc_msg("what happened?"),
        mc_msg("aren't you already here? Sayori and I are just outside, we'll wait"),
        y_msg("We have to re-register some documents, the waiting line is long, this is going to take a while."),
        y_msg("Why don't you and Sayori go to the college first, we'll catch up with you once we finish up here."),
        n_msg("ha! we'll end up sleeping in the airport today once we {i}finish up{/i}!"),
        mc_msg("it's okay, we don't have to rush"),
        mc_msg("we can go tomorrow if we can't go today"),
        mc_msg("besides, we can gather together to have a meal first"),
        y_msg("That will do."),
        mc_msg("oh and sayori said she wants to see your selfie~~"),
        mc_msg("{image=images/phone/emoji2.png}"),
        y_msg("{image=images/phone/emoji2.png}"),
        n_msg("{image=images/phone/emoji2.png} {image=images/phone/emoji2.png} {image=images/phone/emoji2.png}"),
        n_msg("{image=images/phone/pic4.png}"),
    ]

screen new_messages():
    style_prefix "new_messages"
    null height 10
    label _("New Messages")
    null height 10

style new_messages_label:
    xalign 0.5

style new_messages_label_text:
    font "mod_assets/font/fzht.ttf"
    outlines [ ]
    size 18
    color "#b00"



screen chat_textbox():
    style_prefix "chat_textbox"

    frame:
        has hbox
        spacing 4
        yalign 0.5
        xsize 256
        frame:
            background phone_framework.colored_frame(Color("#6d6d6d"))
            has hbox
            xsize 236
            yalign 0.5

            if phone_framework.currently_typing is not None and phone_framework.currently_typing.is_mc:
                $ message = phone_framework.currently_typing.message


                add phone_framework.add_text(message, phone_framework.currently_typing.calculate_cps(), xsize=280)

            else:
                text "|" at typing_blink2(0.0):
                    size 18





        add "images/phone/send.png":
            xoffset 5
            xalign 1.0 yalign 0.5


style chat_textbox_frame:
    xfill True yminimum 50
    background "#424242"
    padding (10, 10)


style chat_textbox_text is empty:
    outlines [ ]
    size 16
    color "#999898"

style chat_textbox_message_text is chat_textbox_text:
    font "mod_assets/font/fzht.ttf"
    color "#999898"

style chat_textbox_placeholder_text is chat_textbox_text:
    color "#b0b0b0"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
