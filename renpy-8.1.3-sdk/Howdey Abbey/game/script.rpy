# Sie können das Skript Ihres Spiels in dieser Datei platzieren.

# Bestimmen Sie Grafiken unterhalb dieser Zeile, indem Sie die "Image-Statements" verwenden.
# z. B. image eileen happy = "eileen_happy.png"
image s1 p1 = "/FINAL SZENE 1/S1 P1.png"
image s1 p2 = "/FINAL SZENE 1/S1 P2.png"
image s1 p3 = "/FINAL SZENE 1/S1 P3.png"
image s1 p4 = "/FINAL SZENE 1/S1 P4.png"
image s1 p5 = "/FINAL SZENE 1/S1 P5.png"
image s1 p6 = "/FINAL SZENE 1/S1 P6.png"
image s1 p7 = "/FINAL SZENE 1/S1 P7.png"
image s1 p8 = "/FINAL SZENE 1/S1 P8.png"
image s1 p9 = "/FINAL SZENE 1/S1 P9.png"
image s1 p10 = "/FINAL SZENE 1/S1 P10.png"
image s1 p11 = "/FINAL SZENE 1/S1 P11.png"
image s1 p12 = "/FINAL SZENE 1/S1 P12.png"
image s1 p14 = "/FINAL SZENE 1/S1 P14.png"
image s1 p15 = "/FINAL SZENE 1/S1 P15.png"
image s1 p16 = "/FINAL SZENE 1/S1 P16.png"
image s1 p17 = "/FINAL SZENE 1/S1 P17.png"
image s1 p18 = "/FINAL SZENE 1/S1 P18.png"
image s1_2 p1 = "/FINAL SZENE 1/S1_2 P1.png"

image s2 p1 = "/FINAL SZENE 2/S2 P1.png"
image s2 p2 = "/FINAL SZENE 2/S2 P2.png"
image s2 p3 = "/FINAL SZENE 2/S2 P3.png"
image s2 p4 = "/FINAL SZENE 2/S2 P4.png"
image s2 p5 = "/FINAL SZENE 2/S2 P5.png"
image s2 p6 = "/FINAL SZENE 2/S2 P6.png"
image s2 p7 = "/FINAL SZENE 2/S2 P7.png"
image s2 p8 = "/FINAL SZENE 2/S2 P8.png"
image s2 p9 = "/FINAL SZENE 2/S2 P9.png"
# Bestimmen Sie Charaktere, die in diesem Spiel verwendet werden.
define a = Character('ABBEY', color="#f5440e")
define b = Character('BILLY', color="#4965a1")
define e = Character('EDUARDO', color="#31611e")
define n = Character('NACHBARIN', color="#61dfff")
define k = Character('NACHBARSKIND', color="#9aff6b")
define s = Character('SALONBESITZER', color="#811414")
define d = Character('DORFBEWOHNER', color="#9b9b9b")
#Du, Deine, Dich groß schreiben!
# Hier beginnt das Spiel.
label start:
#Szene 1
    python:
        renpy.music.set_volume(0.4, 1, channel='music')
    #stop music fadeout 3.0
    show s1 p1
    play sound "/sounds/cutleryClinking.mp3" fadein 0.4 volume 1
    ""
    python:
        renpy.music.set_volume(0.4, 0.3, channel='sound')
    show s1 p2
    a "Uhm.. Papi?"
    a "Ich hab überlegt-"
    show s1 p3
    stop sound fadeout 1.0
    a "weil, also-"
    show s1 p4
    a "... ich bin ja jetzt schon sieben und wollte daher fragen, ob ich-" #text evtl nacheinander erschienen lassen
    stop music fadeout 0.3
    play music "/sounds/hardJustice.mp3" fadein 1 volume 0.5  
    show s1 p5
    b "Und da geht das wieder los."
    show s1 p6
    b "Wann blickst Du, dass Du zu jung bist?"
    show s1 p7
    a "Du bist nicht Papi!"
    b "Muss ich auch nicht, um zu wissen, dass Du viel zu-"
    python:
        renpy.music.set_volume(0.1, 0, channel='music')
        renpy.music.set_volume(1, 0.3, channel='sound')
    play sound "/sounds/woodTableHit.mp3" volume 2
    show s1 p8
    "*Bumm*"
    python:
        renpy.music.set_volume(0.1, 1, channel='music')
    show s1 p9
    e "Hört auf!"
    play sound "/sounds/tablespoon1.mp3"
    show s1 p10
    b "hmpf"
    show s1 p11
    e "Kleines hör zu. Du kriegst Deine Chance."
    e "Pass morgen auf die Tiere auf. Dann darfst Du mit ausreiten."

    menu: 
        " "

        "Bedanken":
            show s1 p12
            a "Danke Papi!!!"

        "Billy die Zunge rausstrecken":
            show s1_2 p1
            a "pfft!" #streckt die Zunge raus
            hide s1_2
    
    show s1 p14
    b "Dad, bist Du-"
    show s1 p15
    e "Billy." #E steht auf
    show s1 p16
    e "Genug jetzt."
    show s1 p17
    e "Morgen."
    e "Morgen. Sonnenaufgang."
    e "Morgen. Sonnenaufgang. Hier."
    e "Morgen. Sonnenaufgang. Hier. Ja?"
    show s1 p18
    "" #a nickt schnell
    stop music fadeout 0.5
    

#Szene 2
    python:
        renpy.music.set_volume(1, 1, channel='music')
    play music "/sounds/theJourney.mp3" fadein 1.0 volume 0.5
    
    show s2 p1 with fade
    b "Tze."
    show s2 p2 
    "" #e auf pferd
    show s2 p3 with dissolve
    "" #a schaut an e vorbei
    show s2 p4
    "*bling*" #fokus auf E's stern
    show s2 p5
    "..." #fokus auf a's stern #punkt für punkt erscheinen
    play sound "/sounds/horseTrotting.mp3" volume 0.5
    show s2 p6
    n "Toll siehst du aus! Wie ein echter kleiner Sheriff!"
    show s2 p8
    k "Ha- Hallo! *woahhh*"
    show s2 p7
    a "Ich pass heute ganz alleine auf die Herde auf!"
    show s2 p9
    s "Guten Morgen Sheriff!"
    stop sound fadeout 0.5

#Szene 3
    play sound "/sounds/horseTrotting.mp3" volume 0.3 fadein 0.5
    show s3 p1 with fade
    "" #Weide
    stop sound fadeout 0.5
    show s3 p2 with dissolve
    ""
    show s3 p3 with dissolve
    ""
    show s3 p4 with dissolve
    ""
    python:
        renpy.music.set_volume(0.1, 2, channel='music')
    show s3 p5
    e "So, Kleines."
    show s3 p6
    e "..."
    show s3 p7
    e "Mach mich stolz."
    show s3 p8
    a "Du kannst auf mich zählen!" #e steigt auf
    python:
        renpy.music.set_volume(0.5, 1, channel='music')
    play sound "/sounds/horseTrotting.mp3" volume 0.3 fadein 0.5
    show s3 p9 with dissolve
    "" #beide tippen ihren hut
    stop sound fadeout 0.5
    stop music fadeout 0.5

#Szene 4
    python:
        renpy.music.set_volume(1, 0, channel='music')
    play music "/sounds/blueOn.mp3" volume 0.5
    show s4 p1 with fade
    pause
    show s4 p2 with dissolve
    pause
    show s4 p3 with dissolve
    a "Alles ruhig."
    show s4 p4 with dissolve
    pause
    python:
        spielen1 = False
        spielen2 = False
        füttern = False

    menu:
        a "*seufz* Aber auch ganz schön laaaaangweilig..."

        "Mit Puppe spielen":
            jump spielen1

        "Tiere füttern":
            jump tiereFüttern1
            
        "Nichts tun":
            jump warten

    #Szene 4.1
    label spielen1:
        show s4_1 p1 with dissolve
        a "...und so wurde Stella zum größten Sheriff im ganzen Westen!"
        a "*seufz* Und nun?"
        python:
            spielen1 = True  
        menu:
            " "

            "Flöte spielen":
                #hide s4_1
                jump spielen2          
            "Tiere füttern" if füttern == False:
                #hide s4_1
                jump tiereFüttern1
            "Möhre verfüttern" if füttern == True:
                #hide s4_1
                jump tiereFüttern2
            "Nichts tun.":
                #hide s4_1
                jump warten   
    
    #Szene 4.4
    label spielen2:
        python:
            renpy.music.set_volume(0, 0.5, channel='music')
        play sound "<from 12>/sounds/recorder.mp3" fadein 0.5
        show s4_4 p1 with dissolve 
        "{font=freeSans.ttf}♩ ♪{/font}" #a spielt mit flöte, läuft zaun entlang
        show s4_4 p2 with dissolve
        "{font=freeSans.ttf}♪♪ ♩{/font}"
        stop sound fadeout 0.5
        python:
            spielen2 = True
            renpy.music.set_volume(1, 0.5, channel='music')
        menu:
            " "
            
            "Tiere füttern" if füttern == False:
                #hide s4_4
                jump tiereFüttern1
            "Möhre verfüttern" if füttern == True:
                #hide s4_4
                jump tiereFüttern2
            "Nichts tun.":
                #hide s4_4
                jump warten
    #Szene 4.6
    label spielen3:
        python:
            renpy.music.set_volume(0, 0.5, channel='music')
        play sound "<from 1 to 12>/sounds/recorder.mp3" fadein 0.5
        show s4_6 p1 with dissolve
        "{font=freeSans.ttf}♩ ♪♩{/font}"  #a spielt mit flöte, läuft zaun entlang
        show s4_6 p2 with dissolve
        "{font=freeSans.ttf}♪ ♪♪ ♩{/font}" #s folgt ihr
        stop sound fadeout 0.5
        python:
            renpy.music.set_volume(1, 0.5, channel='music')
        jump pony
    #Szene 4.2
    label tiereFüttern1:
        show s4_2 p1 with dissolve
        "" #hält gras hin
        show s4_2 p2 with dissolve
        ""
        show s4_2 p3
        a "Komm schon. Ist frisch!" #kein tier reagiert
        show s4_2 p4
        "..."
        a "Dann halt nicht..."
        python:
            füttern = True
        
        menu:
            " "

            "Mit Puppe spielen" if spielen1 == False:
                #hide s4_2
                jump spielen1
            "Flöte spielen" if spielen1 == True and spielen2 == False:
                #hide s4_2
                jump spielen2
            
            "Möhre verfüttern":
                #hide s4_2
                jump tiereFüttern2

            "Nichts tun.":
                #hide s4_2
                jump warten   
    #Szene 4.5
    label tiereFüttern2:
        show s4_5 p1
        a "Ja endlich!"
        show s4_5 p2
        "*mampf*"
        menu:
                " "

                "Für das Pony Flöte spielen":
                    #hide s4_5
                    jump spielen3
                "Nichts tun.":
                    #hide s4_5
                    jump pony   

    #Szene 4.3
    label warten:
        show s4_3 p1
        stop music fadeout 1.0
        "" #a liegt vor Zaun, Hut tief im Gesicht, Grashalm im Mund
    #Szene 5
        play music "/sounds/flower.mp3" fadein 2.0
        show s5 p2 with fade
        "" 
        show s5 p3
        e "Sheriffs schlafen nie, Kleines."
        show s5 p4
        a "Aber..!"
        a "Aber.. ich...!"
        a "Aber.. ich... nein das-!"
        show s5 p5
        e "Komm mit Kleines."
        e "Ist meine Schuld."
        e "Deine Füße passen nicht in die Stiefel eines Sheriffs."
        show s5 p6 with dissolve
        ""
        return
        #SLEEPY ENDING
    #Szene 4.7
    label pony:
        show s4_7 p1 with fade
        "*stups*" #a liegt vor Zaun, Hut tief im Gesicht, Grashalm im Mund
        show s4_7 p2 with dissolve
        a "hmm?" #s stupst a an
        a "Willst du spielen?"
        stop music fadeout 0.5
        jump szene6
     
    

#Szene 6
label szene6:
    play music "sounds/theHardWay.mp3" volume 0.5 fadein 1.0
    show s6 p1 with fade
    "" #bulle schläft
    show s6 p2 with dissolve
    a "So sieht man sich wieder, Bulle Bill!"
    show s6 p3
    a "Du hast die Milch von Paula Kuh geklaut!"
    a "Du hast die Milch von Paula Kuh geklaut! Dafür wirst Du jetzt-"
    
    show s6 p4
    "" #bulle geht weg
    show s6 p7
    a "He-Hey! Bleib-!"
    show s6 p6
    ""
    show s6 p5
    a "Du bist festgenommen!"
    show s6 p8
    ""
    show s6 p9 with dissolve
    stop music fadeout 1.0
    play sound "/sounds/flute.mp3" fadein 0.4 volume 0.3
    "*fiiiiiieeeeeep*" #s bäumt sich auf
    stop sound
    play music "/sounds/wokLikeACowboy.mp3" fadein 0.3 volume 0.4
    show s6 p10
    a "WAAAA-" #bulle rennt
    play sound "/sounds/stampede.mp3" loop
    show s6 p11
    a "AAAH!" #chaos
    show s6 p12
    play audio "/sounds/woodShatter.mp3" volume 2.0
    "KRACH!" #bulle zerstört tor
    show s6 p13
    "" #a sitzt und fängt an zu weinen
    stop sound fadeout 3.0
    python:
        renpy.music.set_volume(0.2, 0.5, channel='music')
    show s6 p14 with dissolve
    a "NEEIN!" #s stupst a an
    show s6 p15
    a "aber..."
    show s6 p16 with dissolve
    "*stups*"
    menu:
        " "

        "Hier bleiben":
            jump szene7
        "Den Tieren hinterher":
            jump szene8
#Szene 7
    label szene7:
        python:
            renpy.music.set_volume(1, 0.5, channel='music')
        play music "/sounds/houseOnARock.mp3" volume 0.6 fadein 1.0
        show s7 p2 with fade
        "*schluchz*"
        show s7 p3 with dissolve
        "*schluchz*"
        show s7 p4
        e "Sheriffs stehen zu ihren Fehlern, Kleines."
        show s7 p5 with dissolve
        a "Papi..."
        a "Papi... ich.."
        a "Papi... ich.. der Stier!"
        a "Papi... ich.. der Stier! und-"
        show s7 p6
        e "Beruhig dich."
        e "Beruhig dich. Ist meine Schuld -"
        e "Billy hatte Recht."
        e "Deine Füße passen nicht in die Stiefel eines Sheriffs."
        show s7 p7 with dissolve
        ""
        return
#Szene 8    
    label szene8:
        python:
            renpy.music.set_volume(0.1, 0.5, channel='music')
            renpy.music.set_volume(0.1, 0.5, channel='audio')
        play audio "/sounds/stampede.mp3" loop 
        show s8_1 p1 with fade
        b "*da da dam daaa da dam*" 
        show s8_1 p2 with dissolve
        python:
            renpy.music.set_volume(1, 0.5, channel='audio')
        d "AAAAHHH! Hilfe!" #geschrei vom dorfeingang
        python:
            renpy.music.set_volume(1, 1.5, channel='music')
        
        show s8_1 p3 with dissolve
        "" #tiere rennen durch dorf 
        show s8_1 p4
        ""
        play audio "/sounds/woodShatter.mp3" volume 2.0
        show s8_1 p5
        ""
        show s8_1 p6
        b "Abbey??"
        show s8_1 p7
        a "Geht alle nach Hause!"
        show s8_1 p8
        k "Uhmmm..."
        show s8_1 p9
        k "HILFE!"
        show s8_1 p10
        a "Bulle Bill..."
        show s8_1 p11
        b "Was zum-?"
        b "Was zum-? Bist du-"
        show s8_1 p12
        b "Abbey! Warte!"
        show s8_1 p13
        b "Abbey! - komm da weg! Warte auf Dad!"
        show s8_1 p14
        b "Wuah!?"
        show s8_1 p15
        a "BILL!"
        menu:
            " "
            "Bulle Bill anschreien":
                jump szene8_2
            "In Flöte pusten":
                jump szene8_3
    label szene8_2:
        show s8_2 p1
        a "BULLE BILL!!! ZUERST DIE MILCH VON PAULA KUH UND NUN DA-"
        play sound "/sounds/stampede.mp3" volume 1.5 loop
        show s8_2 p2
        a "oh."
        show s8_2 p3
        ""
        stop music fadeout  0.5
        
        show s8_2 p4 with fade
        a "WAHHHHH!!!!"
        stop sound fadeout 0.5
        play music "/sounds/recorder.mp3"
        show s8_2 p5 with fade
        ""
        return
    label szene8_3:
        show s8_3 p1
        ""
        show s8_3 p2
        python:
            renpy.music.set_volume(0.3, 0.4, channel='music')
        play sound "/sounds/flute.mp3" fadein 0.4 volume 0.7
        "*fiiiiiieeeeeep*" #a blässt in flöte
        show s8_3 p3
        play sound "/sounds/flute.mp3" if_changed volume 0.7
        "*fiiiiiieeeeeep*" #kind hält sich ohren zu
        show s8_3 p4
        play sound "/sounds/flute.mp3" if_changed volume 0.7
        "*fiiiiiieeeeeep*" #b hält sich ohren zu
        show s8_3 p5
        python:
            renpy.music.set_volume(1, 1, channel='music')
        a "EEEH!" #s bäumt sich auf, a fällt
        play audio "/sounds/woodShatter.mp3" volume 0.5
        stop music fadeout 4.0
        show s8_3 p6
        ""
        play sound "/sounds/gunshot.mp3"
        stop audio fadeout 3.0
        play music [ "<silence 1>", "/sounds/hardJustice.mp3" ] volume 0.5 fadein 0.5
        show s8_3 p7
        "*BANG*" 
        #sound bang
        
        show s8_3 p8
        ""
        show s8_3 p9
        ""
        show s8_3 p10
        "" 
        show s8_3 p11
        e "Abigail, Kleines."
        show s8_3 p14
        e "Deine Füße passen nicht in die Stiefel eines Sheriffs."
        show s8_3 p12
        a "Nein-"
        a "Nein- aber-" 
        a "Nein- aber- Papi-"
        a "Nein- aber- Papi- ich-"
        a "Nein- aber- Papi- ich- das Pony-"
        show s8_3 p13
        e "Is' meine Schuld Kleines."
        show s8_3 p15 with dissolve 
        e "Billy! Wir fangen die Tiere."
        show s8_3 p16
        "" #b wirft skorpion weg
        show s8_3 p17
        python:
            renpy.music.set_volume(0.2, 0.5, channel='music')
        play music "<from 15>/sounds/theHardWay.mp3" volume 0.5 fadein 1.0 fadeout 1.0
        b "Nein, Dad."
        show s8_3 p18
        "" 
        show s8_3 p19
        b "Abbey hat sich hier voll reingestürzt."
        show s8_3 p20
        b "Sie ist den Tieren einfach hinter her."
        show s8_3 p21
        b "Verdammt, sie hat den Stier lieber auf sich gezogen als auf die ganzen erwachsenen Weicheier hier!"  
        show s8_3 p22
        "" #a umarmt b
        show s8_3 p23
        ""
        show s8_3 p24
        b "Wenn du mich fragst, macht genau das einen guten Sheriff aus."
        show s8_3 p25
        b "Ich habs nichtmal über die Straße geschafft..."
        
        show s8_3 p26
        "" #Bewohner schauen aus den türen raus
        show s8_3 p27
        "" #auch schmied
        show s8_3 p28
        ""
        show s8_3 p29
        ""
        show s8_3 p30
        e "Gut, Abbey."
        e "Gut, Abbey. Fang das Pony."
        python:
            renpy.music.set_volume(1, 1, channel='music')
        show s8_3 p32
        e "Billy, sattel dein Pferd."
        show s8_3 p33
        e "Lasst uns ein paar Tiere fangen!"
        

#Szene 9
    
    show s9 p1 with fade
    "" #e schlägt weidentor zu
    show s9 p2 with dissolve
    "" #e setzt sich auf pferd
    show s9 p3
    "" #alle reiten in Sonnenuntergang
    show s9 p4 with dissolve
    ""
    return