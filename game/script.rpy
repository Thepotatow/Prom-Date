default lang = "svenska"
define config.has_autosave = True
# use : $ renpy.force_autosave()

#for inventory
init python:
    class Item:
        def __init__(self, name, icon, detail, description="No description available."):
            self.name = name
            self.icon = icon
            self.detail = detail
            self.description = description

default inventory = []
# When adding an item:
# $ inventory.append(Item("name", "icon.png", "detail.png", "description"))           


transform right_char:
    xpos 0.60 
    ypos 0.1

transform left_char:
    xpos 0.10
    ypos 0.1
    
#renpy websete, timed menues
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

#put this before a menue:
#$ time = 5
#$ timer_range = 5
#$ timer_jump = 'give_up'
#show screen countdown

init:
    default time = 0
    default timer_range = 0
    default timer_jump = "give_up"    
    $ timer_range = 0
    $ timer_jump = 0


# The game starts here.
label start:

    # maybie video cutscean
    en "intro" 
    sv "intro"
    

    scene bg courtyard
    show screen side_menu

    sv "Tyler bad mig träffa honom vid rinken, men jag har inte råd att komma sent till ännu en lektion, pappa hade dödat mig."
    
    $ renpy.force_autosave()


    menu:
        "Tyler bad mig träffa honom vid rinken, men jag har inte råd att komma sent till ännu en lektion, pappa hade dödat mig."

            "Gå till hockeyrinken":
                $ affection_bear += 1
                $ affection_dad -= 1
                jump tyler_intro

            "Kom i tid till lektionen":
                $ affection_bear -= 1
                $ affection_dad += 1
                jump exam1


label give_up:
    # game over screen
    scene black
    with fade
    sv "Jag kan inte göra deta längre. Det käns inte rätt. Sorry, Tyler"

    return
       
label exam1:
    #1A
    #on time for class
    scene bg classroom
    with fade

    sv "Precis i tid..."

    show bella neutral at right_char

    sv "Och där är hon. Jag ångrar inte ens att jag lämnade Tyler."

    hide bella neutral
    show bella happy at right_char


    $ renpy.force_autosave()
    menu:
        "*Bellanie går förbi och ler mot honom. *"

        "Le tillbaka”":
            #2A
            $ affection_bella += 1
            jump exam_game

        "Ignorera":
            #2B
            $ affection_dad -= 1
            jump exam_game

label tyler_intro:
    #1B
    scene bg ice_rink
    with fade

    show tyler happy
   
    t "Cass! Du är sen!"

    c "Du pressar mitt schema."

    t "Jag lär faktiskt Alvin hur man är kapten så han kan ta över sen när jag är borta. Du kan väl hjälpa till?"

    c "Du får en kvart. Jag har prov i filosofi."

    hide tyler happy
    show tyler happy at right_char
    show alvin happy at left_char

    a "Ska du lära mig att bli kapten på femton minuter?"

    c "Om du är tillräckligt bra så är det allt du behöver"

    jump exam_late


label exam_late:
    #1B

    #school bell sound

    jump exam_game


label exam_game:
    scene bg classroom 
    with fade

    $ renpy.force_autosave()

    #icon????????? into game
    #mini game
    #fail = game over => auto save

    jump script_1_cont

label script_1_cont:
    scene bg hallway
    show tyler neutral
    with fade

    t "Cass, jag behöver prata med dig. Jag behöver en tjänst"

    c "Okej, vad behöver du?"

    hide tyler neutral
    show tyler angry

    t "Igår kväll pratade jag med min syster om balen. Hon sa att hon inte har någon dejt eftersom alla som frågat henne är sketchy främlingar."
    t "Jag vill inte att hon går med en främling men jag kan inte själv gå med henne eftersom jag lovat Emily, såklart."

    hide tyler angry
    show tyler neutral

    c "Såklart. Vill du att jag hittar någon åt henne?"

    t "Jag vill att du går med henne. Jag litar på dig, du är min bästa vän. Men du måste fråga henne själv."
    t "Valet är hennes i slutändan så se till att det blir ett ja, okej?"

    $ renpy.force_autosave()
    menu:
        "Can du göra det?"
        "Såklart jag går med henne":
            jump script_3a

        "Jag tror inte det är en bra idé":
            #3b
            jump give_up
            

label script_3a:
    show tyler neutral

    c "Såklart jag går med henne"

    hide tyler neutral
    show tyler happy

    t "Tack."

    hide tyler happy
    show tyler neutral

    #bb (bear comes into frame)

    if affection_bear >=0:
        # något mer???
        bb "Bra jobbat i morse, grabbar! Alvin blir en bra kapten för laget!" # något mer???
    else:
        bb "Cassidy! Jag såg inte dig vid rinken i morse. Alvin behöver hjälp om han ska bli bäst. Det är bäst att du är där imorgon!"

    c "Du fuskar, Tyler. Din pappa är tränare, det är inte lagligt."

    hide tyler neutral
    show tyler happy

    t "Jo, det kan du ge dig fan på att det är. Förresten, fredag kväll, Emily’s födelsedag. Kommer du?"

    hide tyler happy
    show tyler neutral

    c "Jag önskar att jag kunde. Jag måste plugga annars får jag stryk. Du vet hur pappa är..."

    t "Ja, juste... Familj, eller hur?"

    c "Det kan man säg. Hälsa Emily från mig."

    t "Det ska jag."

    scene black
    with fade

    scene bg Hallway
    with fade

    sv "Jag måste se till att Bellanie säger ja innan jag frågar henne om balen."
    sv "Så jag borde hålla mig på hennes goda sida och med tanke på att jag typ aldrig har pratat med henne så är väl det en bra början. Och på tal om… Här är min chans."

    #en "*Bellanie is spotted futher down the hallway.*"
    #sv "*Både Bell och valen dyker upp samtidigt.*" #??? valen

    show bella neutral

    $ renpy.force_autosave()

    menu:
        "Hur gick provet?":
            $ affection_bella += 1
            jump script_4b

        "Jag vill lära känna dig bättre":
            $ affection_bella -= 1
            jump script_4a

        "Ge upp":
            jump give_up


label script_4a:

    c "Hej, Bellanie! Jag är vän med Tyler. Vi har filosofi tillsammans."
    
    b "Ja, det har vi! Jag känner igen dig. Du heter Cassidy, va?"

    c "Exakt. Och om det går bra så vill jag gärna lära känna dig lite bättre?"

    b "Uum, visst. Jag måste skynda mig lite nu men jag kan ge dig mitt nummer så kan vi väl höras lite senare?"


    # inventory/ her phone nr added to catelog
    sv "*Hon skriver ner sitt nummer på en lapp och ger det till honom.*"
    
    $ inventory.append(Item("Bellanies mobilnummer", "egg1_icon.png", "egg1_detail.png", "Bellas mobilnummer, snabbt nedskrivet på en lapp."))

    #change images ect sound afect ect

    sv "Hennes nummer?... Okej, det är väl en början."

    jump script_4

label script_4b:
    c "Hej, Bellanie! Jag är vän med Tyler. Vi har filosofi tillsammans." 

    b "Ja, det har vi! Jag känner igen dig. Du heter Cassidy, va?"

    c "Exakt. Hur gick provet för dig?"

    b "Skit. Jag är sämst på filosofi. Det spelar ingen roll hur mycket jag anstränger mig och pluggar, jag klarar inte det ändå..."

    c "Jag kan hjälpa dig om du vill? Jag är skitbra på det."

    b "Vilket självförtroende. Det hade faktiskt varit jättebra. Tack så mycket, Cass. Jag skriver ner mitt nummer till dig så kan vi väl höras av lite senare?"

    sv "*Hon skriver ner sitt nummer på en lapp och ger det till honom.*"

    sv "Hennes nummer… Fuck yeah."

    jump script_4

label script_4:
    if affection_burt <= 0:
        jump script_4_1b
    else:
        jump script_4_1a

label script_4_1b:
    scene bg cass_bedroom
    with fade

    #burt cassyidys dad comes in

    bs "Pojk! Jag såg att du var sen till din första lektion idag. Vad fan handlar det om?"

    c "Förlåt, pappa. Jag behövde träna med Tyler."

    bs "Du hade prov. Tro inte att jag inte har koll på ditt schema. Det är bäst att det inte händer igen."

    sv "*Burt går ut*"

    sv "Det ska det inte. Jag vet att jag kom undan enkelt nu. En varning bara."

    jump script_4_1a

label script_4_1a:

    # bg Desk zoom-in

    sv "Jag borde lägga in Bellanies nummer i min telefon så jag kan skriva till henne. Eller borde jag skriva till henne nu? Det kanske är skumt…"

    sv "Men nu när jag har pratat med henne så kan jag inte släppa det och det är irriterande. Jag måste få skriva av mig på något sätt."
    sv "Om hon får något anonymt så vet hon inte att det är jag och Tyler skulle inte få veta att det är från mig om han får reda på det. Det låter som ett säkert val."

    # as parents argue outside
        
    $ renpy.force_autosave()

    #empty letter infront

    menu:
        "Skriv ett subtilt brev”":
            $ subtle_letter = True
            jump subtle

        "Skriv ett känslomässigt brev":
            $ subtle_letter = False
            jump romantic

        "Ge upp":
            jump give_up

label subtle:
    #parents fighting
    #writing sounds
    #show subtle letter

    sv "..."

    jump script_4_5

label romantic:
    #parents fighting
    #writing sounds
    #show romantic letter


    sv "..."

    jump script_4_5

label script_4_5:   

    sv "Pappa är förbannad igen. Säkert på grund av mig. Det är bäst att jag låser dörren, jag vill inte bli inblandad mer nu."

    sv "*På skrivbordet bredvid står hennes nummer inristat i bordet.*"

    $ name_to_remove = "Bellanie's phone number"
    $ inventory = [item for item in inventory if item.name != name_to_remove]

    $ renpy.force_autosave()

    menu:
        "555-0159":
            jump phone_call

        "Sov":
            jump next_morning

label phone_call:
    sv "Hon sa ju faktiskt att vi skulle höras av senare. Senare är väl ändå samma dag?"
    # insert phone call

    jump choice_2

label choice_2:
    menu:
        "Sov":
            jump next_morning

label next_morning:
    scene bg hallway # lockers
    with fade

    sv "*Nästa morgon. Alvin kommer gåendes mot honom.*"

    c "Om jag skickar in lappen direkt i hennes skåp skulle hon aldrig kunna veta vem det är ifrån. Men hon kanske också inte hittar det alls. Jag skulle kunna be Alvin ge det till henne."
    c "Han är smart nog att inte fråga vad det handlar om och han ska bli kapten så han är skyldig mig för att jag hjälper honom träna."


    menu:
        "Skicka lappen med Alvin":
            $ alvin_good = True
            jump script_6a

        "Skicka in det i hennes skåp":
            $ alvin_good = False
            jump script_6b

        "Ge upp":
            jump give_up


label script_6a:

    c "Alvin! Jag behöver en tjänst!"

    a "Absolut, Cass. Vad behöver du?"

    c "Ge det här till Bellanie. Tyler’s tvillingsyster. Säg inte vem det är från. Säg ingenting alls, bara ge det till henne."

    a "Yes, boss. Jag säger inte ett ord."

    sv "*Alvin skickar in lappen i hennes skåp.*"

    #sound afect

    scene black
    with fade

    sv "*Alvin springer iväg.*"

    jump script_6a_5

label script_6a_5:
    scene bg hallway # lockers
    with fade

    sv "*Cassidy ser Bellanie prata med en av sina vänner i korridoren.*"

    b "Jag fick ett brev från Alvin idag. Han sa inte att det var från honom men jag tror det var det."


    sv "Såklart tror hon att det var från Alvin..."

    s "Det där låter bara läskigt, Bell"

    jump script_5

label script_6b:

    sv "*Cassidy ser Bellanie prata med en av sina vänner i korridoren.*"

    b "Jag fick ett hemligt brev från någon idag. Det låg i mitt skåp."

    s "Vad obehagligt."

    jump script_5

label script_5:
    if subtle_letter:
        jump script_5a
    else:
        jump script_5b
    
label script_5a:
    #subtle letter result
    b "Han är gullig och snäll. Jag gillar honom."

    scene black
    with fade

    jump script_7

label script_5b:
    #romantic letter result
    b "Nej, det är gulligt."

    scene black
    with fade

    jump script_7

label script_7:
    #scene bg outside, road, friday evning
    #with fade

    sv "Den bästa stunden på dagen: När gatan är död och allt är tyst. Jag behöver inte lyssna på mamma och pappa och jag skulle välja tystnad över den skiten vilken dag som helst."
    sv "Och idag verkar det vara extra perfekt för där är hon… Hon väntar på en buss som jag antar ska ta henne till Emily’s hus. Det känns inte konstigt att gå fram och prata med henne längre."
    sv "Det känns naturligt."

    show bella neutral

    c "Bellanie! Ska du ta bussen till Emily? Jag trodde Tyler skulle köra dig?"

    b "Nej. Han ska dricka ikväll så han kör inte. Och dessutom är han redan där och hjälper henne. Vad gör du ute såhär sent?"

    sv "Tar en paus från mina plågsamma föräldrar, försöker fly från mina föräldrar, tekniskt sätt flyr hemifrån för att jag inte orkar lyssna på när min pappa slår skiten ur mamma..."
    sv "Anledningarna är många men det kanske jag inte kan säga till henne. Vad säger man då?"

    menu:
        "Ute och springer":
            $ affection_bella += 1
            jump late_run

        "Vandrar runt och hoppas träffa dig":
            $ affection_bella -= 1
            jump stroll

        "Ge upp":
            jump give_up


label late_run:
    c "Ute och springer bara. Det är för varmt för det när solen fortfarande är uppe"

    b "Det är sant."

    jump the_big_quesition


label stroll:
    c "Vandrar runt och hoppas träffa dig. Och det verkar som att jag hade tur"
    
    b "Jaså? Vad gulligt av dig."

    jump the_big_quesition


label the_big_quesition:
    

    menu:
        "Vill du gå med mig till balen?":
            jump maybe_prom

        "Gå hem":
            jump walk_away

        "Ge upp":
            jump give_up

label maybe_prom:
    c "Förresten nu när jag har dig här. Finns det någon möjlighet att jag kan ta dig till balen i slutet av terminen?"

    if affection_bella >= 1:
        jump lets_go_to_prom
    else:
        jump no_prom

label lets_go_to_prom:
    #the only GOOD ending
    b "Balen? Ja, visst. Jag går hellre med dig än med nån jag knappt känner, det skulle vara mycket säkrare. Tack."

    #scene bg you win
    #prom ending 2 

    return

label no_prom:
    #you get a bad ending
    b "Balen? Jag känner dig knappt och det skulle bli skumt att gå med min brors bästa vän. Ledsen."

    #scene bg you get loose the game

    #prom ending 2 get rejected

    return

label walk_away:
    #7 CONT
    c "Även om jag gärna stannar och väntar tills din buss kommer så borde jag fortsätta. Men det var kul att se dig."

    b "Kul att se dig också."

    sv "Jag skulle kunna stanna här och prata med henne i timmar, men jag tror att jag faktiskt skulle spy om jag fortsätter att titta in i hennes ögon."

    sv "Och det där jävla leendet. Nej, inte en chans, min mage skulle vänt sig. Är det såhär det känns när man är kär? Jag trodde det skulle kännas bra inte som ett jävla slag i pungen."

    if affection_bella <= 1:
        sv "Dessutom verkar hon inte vilja bli störd just nu. Om jag ska vara på hennes goda sida får jag passa mig."
   
    jump script_7b_cont


label script_7b_cont:
    #utanför Emilys hus
    sv "Är det Emily’s hus? Hur långt har jag sprungit? Jag är verkligen förvirrad idag. Men nu när jag ändå är här så skulle det väl inte skada att gå in och hälsa. Emily fyller ju faktiskt år."

    # i hennes hus så hör han bella och alvin pratta

    sv "Två gånger på en dag? Jag har verkligen tur. Jag vet att det är fel men jag kan inte låta bli att lyssna på dem."

    jump script_7b_pre


label script_7b_pre:
    if alvin_good:
        jump script_7b_6a
    else:
        jump script_7b_6b


label script_7b_6a:
    sv "Om Alvin säger att lappen var från mig så..."

    b "Hej, Alvin. Tack för den där lappen."

    a "Ja, absolut. När som."

    sv "Den lilla skiten."

    b "Det var verkligen fint skrivet."

    a "Vad bra! Vad gör du imorgon?"

    sv "Han kan inte mena allvar."

    b "Ingenting. Har du planer?"

    a "Det kanske jag har. Om du är okej med att jag gör lite planer för dig?"

    b "Jag gillar initiativet."

    sv "Jag skulle inte ha skickat det med honom..."

    jump script_8

label script_7b_6b:
    a "Bell! Jag trodde inte att du skulle vara här?"

    b "Varför inte det? Emily är min brors flickvän."

    a "Okej, fair enough. Har du planer imorgon?"

    b "Ummm…"

    sv "Hon ser inte ut att gilla honom så mycket. Han borde se det från en mil bort. Gör inget dumt nu, Alvin."

    a "Förresten så var den där lappen från mig."

    sv "Vafan sa han nu? Dumt, Alvin."

    b "Jaha… Ja, jag är väl ledig imorgon."

    a "Får jag boka upp dig?"

    b "Eeh. Visst. En kväll går bra."

    sv "Säg inte ja då! Alvin, din blinda jävel! Ser du inte att hon uppenbarligen inte gillar dig?! Jag kan inte se på honom. Och jag behöver nåt starkt."

    jump script_8

label script_8:
    # tyler konfronterar cass ang alvin

    t "Cass, jag trodde inte du kunde komma?"

    menu:
        "Jag hade vägarna förbi":
            jump script_8_1

        "Tänkte jag kunde säga hej i alla fall":
            jump script_8_2

label script_8_1:
    c "Jag hade vägarna förbi."

    jump script_8_5

label script_8_2:
    c "Jag tänkte jag kunde säg hej i alla fall."

    jump script_8_5

label script_8_5:
    t "Vad bra. Men tro inte att jag inte har märkt..."

    sv "Märkt vad? Snälla säg inte “hur du ser på min syster” - jag lovar jag ska va’ snäll."

    t "Du har bettet dig som ett as mot Alvin hela kvällen. Varför?"

    menu:
        "Ljug och säg att det är lugnt":
            $ tyler_lie = True
            jump script_8a

        "Utgör Alvin till aset":
            $ tyler_lie = False
            jump script_8b


label script_8a:
    c "Inget. Allt är bra, jag har väl bara inte pratat med honom så mycket ikväll."

    t "Okej, dåså. Men sköt dig, han ser upp till dig."

    c "Jag vet. Lycka till."

    jump script_9a


label script_8b:
    if alvin_good:
        jump script_8b_6a
    else:
        jump script_8b_6b


label script_8b_6a:
    c "Jag hörde honom prata med din syster. Han har tydligen skickat lappar anonymt till henne, antagligen för att han inte vill att du ska veta det."

    c "Han bjöd ut henne nyss och jag gillar inte hans blick så jag håller ett öga på honom. Det är allt."

    t "Det var som fan. Tack för att du är ärlig. Jag ska ha koll på honom."

    jump script_9


label script_8b_6b:
    c "Jag hörde honom prata med din syster. Han bjöd ut henne och hon verkade inte så bekväm med honom. Du borde hålla ett öga på honom."

    t "Åh fan. Tack för att du säger det. Jag ska hålla honom."

    jump script_9


label script_9:
    #arives home, parents arguing
    #entry way

    sv "Som vanligt är han arg på henne för att hon inte gör något anat än att gå runt i huset. Men han vet varför hon bara är hemma hela tiden. Hennes fotboja låter henne inte lämna huset."

    sv "Hon har haft den i snart ett år efter att hon blev påkommen med försök till skattefusk och polisen låste in henne. Tack vare honom slapp hon fängelse men istället blev hon fast här."

    sv "Det låter värre än vanligt. Om han inte redan har slagit henne rejält så kommer han att göra det snart. Jag får ont i magen bara av att tänka på att behöva se henne efteråt."
    
    menu:
        "Rädda mamma":
            jump script_9a

        "Gå till rummet":
            jump script_9b


label script_9b:
    #hide in bedroom
    scene bg cass_bedroom
    with fade

    sv "Å andra sidan vet jag att det förmodligen bara blir värre om jag blir inblandad. Jag borde gå till mitt rum och låsa dörren."

    scene black
    with fade

    jump script_10


label script_9a:
    #save mom

    sv "Jag kan inte gömma mig. Jag kan inte lämna henne med det där."

    scene bg cass_livingroom
    with fade

    bs "Fan, det enda du gör är att sitta i soffan! Vem ska uppfostra ungen, va?! Jag har fan inte tid med det!"

    k "Burt, snälla. Han är gammal nog att ta hand om sig själv."

    bs "Jag bryr mig inte om han är gammal nog! Han behöver en mamma, inte nåt jävla spöke som vandrar i vardagsrummet!"

    k "Han behöver en pappa också!"

    bs "Jag försörjer den här familjen!! Jag betalar taket över hans huvud OCH DITT! Det minsta du kan göra är att fråga hur fan han mår!"

    k "Och när gjorde du nånsin det!?"

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'mamma_rätt'
    show screen countdown

    menu:
        "Mamma har rätt":
            jump mamma_rätt

        "Slå henne inte":
            jump mamma_hand

label mamma_rätt:
    c "Våga inte höja handen mot henne!! Hon har rätt!"

    sv "*Burt vänder sig till Cassidy*"

    bs "Vem sa att du fick lägga dig i?"

    c "Vem sa att du fick slå din fru?"

    jump script_9a_cont


label mamma_hand:
    c "Våga inte slå henne framför mig!"

    sv "*Burt vänder sig till Cassidy*"

    bs "Vem sa att du fick lägga dig i?"

    c "Vem sa att du fick bete dig så mot din fru?"

    jump script_9a_cont


label script_9a_cont:
    bs "Du har ju aldrig protesterat förut."

    c "Det räcker!"

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'game_over_12'
    show screen countdown

    menu:
        "SLÅ TILLBAKA":
            #emil i lönebärja
            scene black
            with fade
            jump script_10


label game_over_12:
    #ending 12 bad ending
    sv "*dad gives you a punch*"

    return


label script_10:
    scene bg cass_bedroom
    with fade

    #her phone nr is now on the wall

    menu:
        "555-0159":
            jump phone_call2

        "Sov":
            scene black
            with fade
            jump script_10_cont

label phone_call2:

    # insert phone call nr2 or 1 depending if you had the first phone call


    menu:
        "Sov":
            scene black
            with fade
            jump script_10_cont


label script_10_cont:
    scene bg courtyard
    with fade

    #after a lesson

    sv "*Cassidy går ut på school gården efter sin föreläsning.*"

    sv "Tyler är inte på parkeringen. Han brukar alltid vänta här på Bellanie men nu är hon ensam. Med tanke på hur mycket vi råkar springa in i varandra numera så känns det nästan som ödet."

    sv "Vilket jag inte har något emot. Det ser ut som om hon redan är på väg hem men det skulle ta henne flera timmar att gå hela vägen hem härifrån."

    sv "Det är mörkt innan hon hinner hem. Tyler skulle inte vilja att hon gick hem ensam. Jag borde följa henne hem så att hon är säker."

        menu:
            "Håll avstånd":
                #10a
                $ keep_distance = True
                jump script_10a

            "Håll vakt":
                #10b
                $ keep_distance = False
                jump script_10b


label script_10a:
    sv "Om jag går för nära så kanske hon tror att jag förföljer henne. Det skulle inte se bra ut för någon."

    sv "Okej, nu är hon hemma och säker. Jag borde gå. Å andra sidan så såg hon inte mig bakom henne innan."

    sv "Så hon inte att jag är här. Och som det ser ut nu så verkar det som att hon byter om. Kan jag verkligen lämna ett sånt här tillfälle bara sådär?"

    jump script_11

label script_10b:
    if affection_dad >= 0:
        $ ending_10 = True
    else:
        $ ending_9 = True

    sv "Om jag följer efter henne på avstånd skulle det	Se ut som att jag förföljer henne. Jag borde hålla mig nära så hon kan se mig."

    scene black 
    with fade

    sv "Okej, nu är hon hemma och säker. Jag borde gå. Å andra sidan hade hon inget emot att jag följde henne hem. Och jag har inget emot det som syns genom hennes fönster."

    sv "Det tog ett par timmar att gå hem precis som jag trodde. Och som det ser ut nu så verkar det som att hon byter om. Kan jag verkligen lämna ett sånt här tillfälle bara sådär?"

    jump script_11


label script_11:
    menu:
        "Stanna":
            #11a
            scene black
            with fade
            jump script_11_5

        "Gå hem":
            #11b
            scene black
            with fade
            jump script_11_5


label script_11_5:
    scene bg ice_rink
    with fade

    t "Jag pratade med Bellanie igår kväll. Hon har nåt creep som följer efter henne. Jag börjar bli orolig för henne. Han har tydligen försökt ringa henne också."

    c "Har hon inte hans nummer inlagt?"

    t "Nej. Varför skulle hon ha det? Hon vet inte ens vem det är."

    c "Hon la aldrig in mitt nummer i sin telefon. Jag kanske inte borde säg mitt namn alls när jag ringer henne. Tyler verkar inte uppskatta det."

    scene black
    with fade

    jump script_12


label script_12:
    #belalnie i bild
    scene bg courtyard
    with fade

    b "Hej, Cassidy! Grattis till vinsten!"

    c "Tack. Du verkar föra med dig tur."

    b "Nejdå, det var din förtjänst, Cass."

    c "Ska Tyler köra dig hem?"

    b "Ja, jag ska vänta på honom här. Hurså?"

    menu:
        "Ta chansen":
            #12a
            jump script_12a

        "Gå närmre":
            #12b
            jump script_12b


label script_12a:
    c "För att… För att fuck it-"

    scene black
    with fade

    scene bg courtyard
    with fade

    c "Det här kanske är den enda chansen jag får. Tillfället är perfekt. Ingen kan se oss och jag behöver det. Det där jävla leendet… Bellanie blir helt stilla i mina armar och jag vet att det är rätt."

    show bella scarred
    with fade

    b "Jag tror jag ska gå, Tyler sa åt mig att vänta vid bilen. Men vi ses, okej..."

    c "Det gör vi."

    scene black
    with fade

    jump ending_3


label enging_3:
    sv "Om jag hade vetat att hon skulle göra en sån stor grej av det så hade jag aldrig gjort det där och då."

    sv "Hon gick direkt till rektorn och jag är helt säker på att det här är tillräckligt för att få mig relegerad. Jag hoppas bara det jag sa till rektorn var bra nog."

    sv "*Bellanie går förbi honom och in till rektorns kontor. Han lyssnar på vad de säger.*"

    pj "Tack för att du kom hit, Bellanie."

    b "Har du pratat med Cassidy?"

    pj "Det har jag. Han sa att din bror Tyler var där för att köra dig hem, är det så?"

    b "Ja, de hade hockeymatch. Det var därför jag var där."

    pj "Så han sa i alla fall sanningen då. Och enligt Cassidy så hade Tyler sett er två tillsammans. Han var där hela tiden."

    pj "Så jag pratade med Tyler också eftersom han nu är ett vittne och Tyler sa inget om att Cassidy hade gjort några närmanden. Men du säger alltså att Tyler var där och såg det?"

    b "Nej, han såg inte vad som hände. Tyler hade inte kommit ut ur byggnaden än."

    pj "Nu hänger inte din historia ihop här, Bellanie. Du sa nyss att han var där hela tiden."

    b "Ja, han var i byggnaden. Han var där men han var inte precis just där då."

    pj "Du förstår väl att det finns tre olika historier här som gör det väldigt svårt att säga sanningen."

    b "Det finns inte alls tre olika historier. Du tar det ur kontext. Jag hade gått ut först och Cassidy var där och då pratade vi med varandra och sen kysste han mig och sen kom Tyler ut. Han såg det aldrig."

    pj "Jag förstår att du är upprörd, Bellanie. Men försök se det här från mitt perspektiv."

    pj "Jag vet ingenting om din historia med Cassidy och nu har jag en tjej som hävdar att hennes brors bästa vän har antastat henne och att hennes bror inte var där när det hände, efter att hon sagt att han var där."

    pj "Jag har en kille som säger att ingenting hände och att hans bästa vän var där och såg det hela tiden."

    pj "När jag sen pratar med hans bästa vän så säger han att Cassidy aldrig kom i närheten av hans syster och att det låter otroligt att hans vän skulle kyssa henne och ännu värre antasta henne."

    pj "Du förstår väl hur det här låter, eller hur?"

    b "Du tror inte på mig..."

    pj "Som rektor får jag inte ta sidor eller hävda egna åsikter i en sån här sak. Men det finns inget bevis och inga vittnen som säger att du har blivit antastad. Däremot har jag ett vittne som säger att du inte blivit det och det är din egen bror..."

    b "Så vad händer nu? Ska han bara fortsätta gå på samma lektioner som mig och fortsätta antasta mig så länge det inte finns något bevis?"

    pj "Som det ser ut just nu så har du lagt allvarliga anklagelser som har startat rykten på skolan om Cassidy. Med det sagt: så kan jag inte tillåta dig att nämna det igen."

    pj "Och om dina vänner diskriminerar Cassidy eller behandlar honom annorlunda på grund av vad du har sagt så är det på ditt samvete."

    b "Va? Du menar att… han är mitt ansvar nu? Att det är mitt ansvar att folk ska behandla Cassidy med respekt?"

    pj "Han ska behandlas precis som tidigare och ja, det är ditt ansvar. Anklagelserna är dina."

    scene black
    with fade

    sv "Att jag gjorde vadå? Hon sa att jag kysste henne?..."

    sv "Va? Jag- okej, jag vet inte riktigt vad hon vill ha ut av det där men jag har aldrig lagt en enda hand på Bellanie."

    sv "Hennes bror var där hela tiden, han kan intyga vad jag säger. Jag gick ut med honom och jag lämnade inte hans sida en enda gång, så fråga honom..."

    sv "Nej, vi sa hejdå och sen körde han hem med Bellanie, inget mer hände..."

    sv "Ja, jag är säker..."

    sv "Ja, jag kan ringa hit honom nu… Tack… Ja, jag väntar utanför."
    
    #win the game ending 3

    return


label script_12b:
    if tyler_lie: # ljuger för tyler
        jump script_12b_8a
    else:
        jump script_12b_8b


label script_12b_8a:
    c "Jag ville bara veta hur mycket tid jag har ensam med dig."

    b "Varför vill du va ensam med mig?… du behöver inte stå så nära och kan du snälla ta bort din hand från min rygg."

    c "Litar du inte på mig?"

    b "Det är inte det att jag inte litar på dig men det känns lite konstigt. Du är min brors kompis och jag känner dig knappt så..."

    c "Titta på mig. Oroa dig inte. Jag skulle aldrig skada dig."

    b "Det tror jag inte att du skulle. Men det betyder inte att jag vill att du rör vid mig så snälla, släpp mig."

    #heartbeat sound loop starts

    b "Cassidy… jag säger till Tyler. Jag kommer berätta för honom om du inte släpper mig nu."

    #Cut scene.
    #game over ending 4


label script_12b_8b:

    c "Jag ville bara veta hur mycket tid jag har ensam med dig."

    b "Varför vill du va ensam med mig? … du behöver inte stå så nära."

    c "Litar du inte på mig?"

    b "Det är inte det att jag inte litar på dig men det känns lite konstigt. Du är min brors kompis och jag känner dig knappt så…"

    c "Nej, okej, jag förstår. Det är lugnt."

    sv "Helvete, det sista jag vill är att skrämma henne. Jag vill att hon ska lita på mig. Jag behöver att hon säger ja till balen. Jag måste hålla mitt löfte till Tyler. Det var kanske för tidigt..."

    scene black
    with fade

    jump script_13a

label script_13a:
    #mobilsamtal

    sv "Jag måste vara smartare. Jag kan inte låta mina känslor ta mina beslut. Jag måste vara logisk. Jag måste hålla mitt löfte till Tyler. Det löser sig. Hon är min. Hon vet bara inte om det än, men när hon gör det... så kommer hon att vara tacksam."
    
    menu:
        "555-0159":
            jump phone_call2

        "Dörren":
            scene black
            with fade
            jump script_10_cont

    #insert phone call

    jump script_FB


label script_FB:
    t "Pappa måste renovera hela jävla huset men pengarna finns fan inte till det nu."

    c "Om ni behöver nån som kan hjälpa till billigt så är mamma arkitekt. Hon sitter ju inne just nu så hon gör det säkert billigt"


label script_13b:



    return