label af3_main:
    stop ambient fadeout 1.0
    play music crush fadein 1.0
    scene black with MultipleTransition([
        False, Dissolve(3.0),
        act3, Pause(4.0),
        act3, Dissolve(3.0),
        True])

    "We camped in the wild, our tent was covered by the wet air of midnight, moths wandered around our camp light as some rustle came out near the lake."
    "We heard animals telling their night tales as wings rushing through the woods."
    "Our body laid back at the entrance of the tent, feeling the uneven ground from under the camping mat."
    "Dirt and shovel composed a symphony, fluffy earth blocks rolled over to the strong roots aside."
    "The diameter of the pit increased, I leaned the warm steel handle against the trunk, erasing my breathless sweat."
    "Besides me, there was Sayori, holding the aged aluminum box with her everlasting smile, which was wrapped with tapes over and over irregularly."
    "\"I want to take another look~~\""
    "\"No! They said that it can't be opened once it is sealed!\""
    "\"Then tell me what you wrote.\""
    "\"Nope.\""
    "\"Meanie! Just a little bit.\""
    "\"Please?\""
    "\"You can see for yourself after ten years.\""
    "\"Tennnnn Yeeeears??? That's so long! Can I check it tomorrow?"
    "\"Next week?\""
    "\"Next month!\""
    "……………………"
    stop music fadeout 2.0
    play ambient int_night fadein(1.0) volume 1.6
    "Clanging sounds appeared in the pit, then turned soft and dull, until this short symphony ended beneath the texture of the shoes."
    scene bg bedroom_night2
    play sound ding1
    "My laptop screen illuminates as there's a message showing at the corner which says I've got a new email."
    "Are you [player]? What are you talking about?"
    "It's Natsuki."
    "I finally decided to send a riddle-like letter to every possible address, telling them that a girl with short coral hair invites me to join the literature club, she's the vice president."
    "Looks like luck is on my side."
    "I reply to Natsuki to brief the situation, and ask her to contact me on social media to make further conversation. "
    "Striking down the enter, I hold my chin while watching the words on the screen that have already been sent to the other side of the server."
    "{cps=*0.2}I wonder when she will recei…{/cps}{nw}"
    play sound ding1
    "Her reply letter comes in almost immediately, looks like she's right in front of her computer."
    "I go to check the profile link she gives me on social media."
    call phone ("Natsuki", natsuki_messages, 2, 10, hide_phone=False) from _call_phone_3

    "..."
    show white onlayer front:
        alpha 0.0
        0.5
        linear 20.0 alpha 1.00
    call phone ("Natsuki", natsuki_messages, 12, 9) from _call_phone_4

    "..."
    hide white onlayer front with Dissolve(5.0)
    "We chat from nothing to everything."
    "From our seven-days friendship in the subtropics to her college up above the 800-millimeter precipitation boundary."
    "From her same kept literary habit to her new cupcake flavors."
    "Even though the time we spent together will never outweigh the time we didn't, those days have been increased to a incomparable length inside our own memories. "
    queue ambient int_night volume 1.0

    call phone ("Natsuki", natsuki_messages, 300, 5, hide_phone=False) from _call_phone_5

    "I swallow."

    call phone ("Natsuki", natsuki_messages, 305, 23, hide_phone=False) from _call_phone_6

    "..."
    play music abyss fadein(2.0)

    call phone ("Natsuki", natsuki_messages, 328, 36, hide_phone=False) from _call_phone_7

    "..."

    call phone ("Natsuki", natsuki_messages, 364, 11, hide_phone=False) from _call_phone_8

    pause 1.0

    call phone ("Natsuki", natsuki_messages, 376, 31, hide_phone=False) from _call_phone_9

    "......"
    "..."

    call phone ("Natsuki", natsuki_messages, 407, 8, hide_phone=False) from _call_phone_10

    "I then turn to Sayori, and take a picture instantly. "
    play sound camera

    call phone ("Natsuki", natsuki_messages, 415, 16, hide_phone=False) from _call_phone_11
    pause 2.0

    call phone ("Natsuki", natsuki_messages, 431, 1, hide_phone=False) from _call_phone_12

    stop music fadeout(4.0)
    pause 1.0

    call phone ("Natsuki", natsuki_messages, 432, 83, hide_phone=False) from _call_phone_13

    "..."

    call phone ("Natsuki", natsuki_messages, 515, 3) from _call_phone_14

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
    stop ambient fadeout 2.0
    show sayori sleepy1 dd at t33
    pause(0.5)
    show sayori sleepy2 dd
    pause(0.75)
    show sayori sleepy1 dd
    mc "Morning, sleepyhead."
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
    mc "I told her about your…… situation. She will contact Yuri this weekend, and we'll meet up sometime once we figure out where Monika is."
    show sayori reluc2 dd at s31
    s "…"
    s "Monika………"
    show sayori reluc7 dd
    mc "Yeah, we're going to confront her. Don't you want to know what the truth is?"
    "I glance at my backpack."
    show sayori worried3 dd at t31
    s "Alright……"
    show sayori reluc10 dd
    s "But where do we start? It's been so long."
    show sayori worried3 dd
    mc "We can start with our high school. In fact, weren't we just about to visit there?"
    "I stand up to tidy my uniform."
    show sayori worried2 dd at s31
    s "Sure, but…"
    mc "What is it?"
    show sayori reluc11 dd at sink_more(240)
    s "I don't know………"
    stop music fadeout 4.0
    mc "Just don't think about it too much for now……"
    mc "It won't hurt to just take a walk around the school."
    show sayori reluc10 dd
    s "I guess…"
    play ambient schoolcrowd2 fadein 2.0 volume 0.3
    scene bg street2_day with dissolve
    "We stand in the cold early morning breeze."
    show crowd3 with dissolve
    "A bus slowly stops before the board. I could see crowded people through the bleary window."
    play sound bus_brake fadeout 1.0 volume 2.0
    "The decompression valve lets out a rough breath before the hydraulic mechanism brings the door open with a loud clang."
    "People waiting at the bus stop all crowd to the entrance, making the commute even more dense."
    "I hesitate."
    show sayori curious1 dd at t11
    mc "How about we take the taxi."
    show sayori curious6 dd
    s "Why though?"
    mc "Errrr… because it's faster? I don't want to see the school gate shut when we arrive."
    show sayori serious1 du
    s "Huh……"
    "Without her further question, I pull out my phone to call the cab."
    hide crowd3 with dissolve
    scene black with dissolve
    "Before long, a white car approaches, driving us to the direction of old days."
    play sound cab loop fadein 1.0
    stop ambient fadeout 1.0
    "All the street lights are cut off synchronously, buildings at our sides are also disappearing as they rapidly get pushed backwards, into the grayish blue sky."
    "We are entering the urban area, our pace slows, and the surroundings are becoming more and more familiar."
    "At last, the driver leaves us at the school gate that I will never forget."
    stop sound fadeout 2.0
    scene bg schoolgate_day with dissolve
    play ambient schoolcrowd1 fadein 1.0 volume 0.3
    show crowd4 with dissolve
    "We're not late, the first bell hasn't rung yet, students are crowding across the gate, which is very convenient for us."
    show sayori mock3 du at t11
    s "Don't you get caught~~"
    mc "That's impossible. "
    mc "Not if you report to the guard."
    show sayori mock4 du
    s "Huh! That depends!"
    "I then take out my student's ID from back in high school, waving it before her."
    show sayori smile2 dd at focus
    show sayori at focus(640, 0.85, 50)
    s "Ehehe, you look so stupid in this image."
    mc "Who are you to judge me?"
    show sayori angry4 dd at t11
    s "Meanie!"
    "Then we walk through the gate, seemingly not drawing any attention. "
    hide crowd4 with dissolve
    pause(0.1)
    hide sayori with dissolve
    play ambient ext_day volume 1.2
    scene bg campus_day with dissolve
    pause(0.2)
    show sayori curious2 ud at t11 with dissolve
    s "I can't believe we're actually inside!"
    show sayori at t21
    pause(0.5)
    show sayori at t33
    "She runs around under the school building."
    s "Everything don't seem to have changed that much."
    show sayori at t11
    mc "It's also my first time."
    scene bg stair1_day with dissolve
    play ambient int_day volume 1.2 fadein 1.0
    "I step to the entrance of the stairs, looking at those students who are walking in a hurry."
    show sayori curious1 dd at t11
    s "What now? Are you going to attend the classes?"
    mc "I don't think that's realistic, given this is not college."
    mc "Let's just go straight to the club office."
    show sayori sadsmile1 du
    s "Awwww… it's Mr. Dan, right?"
    s "But what if he doesn't work here anymore?"
    show sayori curious1 du
    mc "Keep your fingers crossed."
    scene bg corridor_day with dissolve
    "Standing before the familiar office door, unceasing nervous crawls over me."
    "I take a deep breath, then knock on the door."
    play sound doornock volume 0.7
    show sayori sadsmile1 dd at t11
    s "A bit nervous?"
    mc "Of course."
    show sayori curious5 du
    s "Monika must be feeling the same way when she came here to apply for setting up the club."
    show sayori reluc2 dd
    mc "Don't mention her."
    hide sayori with dissolve
    "I squeeze my thumb and index finger on my right hand."
    play sound closet_open
    show dan dcurious1 at t11
    d "Who are…"
    play music t3
    show sayori laugh2 uu t43
    show dan dcurious2
    show sayori laugh2 uu at h33
    s "Mr. Dan!!!"
    mc "Good afternoon, Mr. Dan."
    show sayori laugh2 at easein_to_alpha(1.0, 3.0, 0.4)
    "I look at his mustache, it seems like compared to us, the {i}real{/i} adult doesn't change that much."
    show dan dsmile1
    d "Oh hello! It's you, welcome! Haven't seen you guys for a long time! What brings you here?"
    show dan dsmile2
    show sayori smile5:
        alpha 0.4
    mc "Yep, Sa… I happened to have a spare day, so I thought I could come and pay a visit."
    d "Come in and have a seat."
    hide dan
    show sayori at lhide(.50)
    hide sayori
    pause 1.0
    scene bg office1_dusk with dissolve
    "There are photos of all kinds of club activities hanging on the wall, the atmosphere is very lively."
    "Some well decorated frames are placed on his desk, and some elegant handwritten posters are sticking on the wall across it, along with various plushies and models."
    "I sit next to his desk, I've noticed that there is a rather less decorated frame out there. It seems to have less people in it compared to other lively photos."
    show sayori curious3 dd at r41:
        alpha 0.4
    pause(0.5)
    show sayori smile5 uu at h41:
        alpha 0.4
    s "These must be photos taken from clubs! …"
    mc "Hey……"
    "I try to stop her as she goes straight through Mr. Dan's body."
    show dan dsmile2 at t11
    "Well, he doesn't seem to notice."
    "I'll just leave her to it."
    show sayori tongue1 at t42:
        alpha 0.4
    s "Ehehe~ Seems like you can't talk with me right now, you have to work hard on it~ "
    "She starts to make faces before me."
    "Sayori oh Sayori…"
    show sayori smile3 dd at t44:
        alpha 0.4
    pause(0.5)
    show sayori smile3 dd at s44:
        alpha 0.4
    show dan dsmile1
    d "Hahahah, I can see that you didn't change that much."
    show dan dcurious3
    show sayori smile3 dd at t44:
        alpha 0.4
    d "And… It's always nice to have you back, no matter under what kinds of premises."
    show sayori serious3 ud at t44:
        alpha 0.4
    pause 0.5
    show sayori at lhide(t=.85)
    hide sayori
    pause 1.0
    mc "Yeah… life in college is kinda busy, it's a shame that I didn't come back to visit the school in the past few years."

    show dan dsmile2
    d "Yes, you need to remember that life comes first. It is hard and cruel, but don't forget that we'll always be here to support you."
    show dan dcurious3
    d "Well, maybe in an insignificant way, but we'll try our best."
    show dan dsmile2
    d "Anyway… How's your life going?"
    mc "I'll say it's getting better."
    d "Emmm………"
    d "Good, I was right about you not being held back."
    d "Have you made some new friends?"
    mc "Of… of course!"
    show dan dserious1
    d "…"
    d "While sitting and talking with me…"
    d "Do you regret to have come this far?"
    "…?"
    show dan dsmile1 at laugh_cg_twice
    d "Hahah."
    show dan dsmile2
    d "Don't push yourself too hard. If the story's end denies all your anticipation, I wish you could have the courage to start it over."
    mc "Huh…"
    "I have no idea…"
    show dan dserious1
    d "Do you think that too much persistence puts you in the dead end?"
    mc "Err…?"
    "I'm a little confused."
    d "All of this is prepared for you. I believe you will have your own understandings."
    d "Once it's all settled,"
    d "I wish you can learn more than what others have expected you to learn, don't let your reality shatter in vain."
    "..."
    show dan dsmile1 at h11
    d "Hahahah, don't rush it though, I'm sure you've still got half of the time to figure it out."
    "He spins his pen in his hand, there was a piece of paper on his desk…"
    "I can't tell what's on it though…"
    mc "{size=-5}Puff.....................{/size}"
    "Sayori has finally broken my defense, every nerve of mine is trying to bring my muscle to laugh."
    "I'm trying my best to not laugh in front of Mr. Dan, because it seems like he is having a serious conversation with me right now."
    show dan dserious1 at f11
    d "You should know, we hardly see the real sadness among most of the tragedies. "
    "…"
    show dan dsmile2 at t11
    d "Okay, That's all I got to say to you."
    d "And [player], I don't think you guys come to visit the school just for one reason, right?"
    mc "…! Y…Yeah!"
    mc "I'm here for Monika"
    show dan dcurious3
    d "If I remember it correctly, she was your club president? "
    mc "Yep."
    show dan dsmile3
    d "Ahh… I could never forget her, she's smart, athletic, always willing to help others, like a bundle of sunshine, the literature club would be missing half of its soul without her."
    d "Are you looking for her?"
    mc "Yeah, I've got some questions to ask her."
    d "Emmm......"
    d "I think she did mention to me about which college she was admitted to."
    d "Because she had an excellent score on her graduation exam."
    d "...It's been a long time though."
    d "Let me think..."
    "He opens up the computer, searching for the information. "
    pause 1.0
    show dan dsmile2 at t43
    d "I remember it. I'll send the college's name to you email."
    mc "I appreciate it."
    d "Other than that, I don't quite know."
    d "You could ask around the college."
    d "Just say hello to her for me will you?"
    mc "No problem."
    show sayori reluc2 dd at leftin(300, 0.80, .70):
        alpha 0.4
    "Sayori is looking at something on the table without making a sound."
    show dan dsmile1
    show sayori smile1 dd
    d "You can sit here as long as you like, make yourself at home."
    show dan dcurious3
    d "The clubs are about to start though, I must go check on them."
    "He picks up the paper on the desk."
    mc "Okay! See you around Mr. Dan!"
    show dan at rhide
    hide dan
    "I watch him exit the office with a file in his hands while receiving the email he has just sent to me."
    show sayori laugh2 ud at f20:
        alpha 0.4
    s "See you Mr. Dan!!!"
    scene cg leave with dissolve
    $ persistent.cg7 = True
    hide sayori
    "He turns around and smiles."
    d "Take care of {i}yourself{/i}."
    play sound closet_close
    scene bg office1_dusk
    pause(0.1)
    show sayori smile1 ud at f11
    s "[player], look at this, this is our club…"
    "She whispers by my ear"
    "I sit on Mr. Dan's seat, and check that picture."
    hide sayori with dissolve
    "Four familiar people come into my view."
    "Sayori is waving at the camera, "
    "Monika is clutching a paper and a pen against her chest while Yuri's holding a giant book, looking timidly towards the camera."
    "As for Natsuki, well, she's holding her arms like a tough guy."
    s "We took this picture not long after we set up the whole club, you were probably still sitting in your house watching anime back then, hehe."
    mc "That's good, how about I take a picture of it as a souvenir. "
    s "Sure!"
    "So I pull out my phone, and record a moment that had been already recorded."
    play sound camera
    pause(1.0)
    "Then, we wander around Mr. Dan's office for another while, looking through the pictures of the clubs these years."
    stop music fadeout(5.0)
    "Debate club, anime club, robot club……"
    pause(2.0)
    show sayori smile1 dd at t11
    mc "Let's go."
    show sayori curious1 du at f11
    s "Where to?"
    show sayori curious1 du at t11
    "I open up the archive Mr. Dan just sent to me, it should point out where did Monika go after the graduation. "
    "My heart shakes."
    show sayori reluc3 dd at s11
    mc "{cps=*0.3}She's still in our city.{/cps}"
    show sayori sadsmile1 dd at t11
    s "That's kinda…… convenient?"
    mc "Yep, how about we go visit her right now?"
    show sayori curious6 ud at f11
    s "What about Yuri and Natsuki? Aren't you supposed to wait for them?"
    mc "Err…… you have a point."
    "I scratch my head"
    show sayori smile2 dd
    s "Anyway, how about we go grab a meal, it's close to dinner time."
    mc "Anything on your mind?"
    show sayori serious1 uu
    s "I don't—————————————"
    show sayori laugh3 uu
    s "think you have any better ideas than mine!!"
    show sayori smile2 dd
    "She gives me a warm smile."
    show sayori laugh4 at laugh_cg
    "Hahahahah…"
    "We both laugh."
    hide sayori
    scene bg corridor_day with dissolve
    play sound closet_close
    play music daisuke fadein(4.0)
    "Stepping out of the office, the freezing air of early morning embraces me, that's when I noticed that the air conditioner has been opened up back inside."
    "Which is reasonable, given that it is late winter now."
    show sayori smile3 dd at t11
    s "It must be snowing in Natsuki's place…"
    show sayori curious3 uu at f11
    pause(0.9)
    show sayori smile5 uu
    s "How I wish I could have a snow fight with her! There must be a loooot of snow in the north."
    "Considering it is still class time, and the club meetings haven't begun yet, Sayori and I can't revisit our old club room."
    "And it would be suspicious for a student like me to wander around the campus during class time."
    scene bg stair1_day with dissolve
    "So we decided to leave the school first."
    mc "How about we just head back and finish what we bought yesterday? "
    show sayori angry3 dd at t11
    s "Awwww… come on…"
    pause(0.5)
    show sayori angry4 dd
    pause(0.7)
    show sayori angry5 dd
    pause(0.9)
    show sayori angry4 dd
    pause(0.2)
    mc "You are killing my wallet! I'm not someone who can edit the number on the credit card at will!"
    show sayori worried3 ud at t45
    pause(0.2)
    show sayori worried3 ud at focus(500, 0.85)
    s "Come on [player]… I happen to know a decent restaurant just near your district…"
    "Here comes her classic scheme, which is hard for me to resist."
    scene bg campus_night with dissolve
    "But I won't give in to it!"
    show sayori surprise1 dd at t45
    mc "Out of the question! You're not going to go to any ‘decent restaurant' of yours until you finish the ones {i}you{/i} picked up from that bakery!"
    show sayori angry5 dd at s45
    s "Humph! It's not like {i}I am the one who's going to eat them! {/i}"
    mc "You almost sound like Natsuki."
    scene bg schoolgate_day with dissolve
    "I giggle."
    show sayori curious6 dd at t45
    mc "How about this."
    stop music fadeout(5.0)
    mc "We head back for lunch first, and I'll take you there for dinner."
    show sayori angry12 at sink_more(500)
    s "Uwwww.."
    scene white with Dissolve(2.0)
    "The taxi reaches us as we talk, without her making further complaints, I open up the door and let myself in."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
