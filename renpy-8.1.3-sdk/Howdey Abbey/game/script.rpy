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
define b = Character('BILLY', color="#173064")
define e = Character('EDUARDO', color="#31611e")
define n = Character('NACHBARIN', color="#61dfff")
define k = Character('NACHBARSKIND', color="#9aff6b")
define s = Character('SALONBESITZER', color="#811414")

#Du, Deine, Dich groß schreiben!
# Hier beginnt das Spiel.
label start:
#Szene 1
    show s1 p1
    ""
    show s1 p2
    a "Uhm.. Papi?"
    a "Ich hab überlegt"
    show s1 p3
    a "weil, also,"
    show s1 p4
    a "... ich bin ja jetzt schon sieben und wollte daher fragen ob ich-" #text evtl nacheinander erschienen lassen
    show s1 p5
    b "Und da geht das wieder los."
    show s1 p6
    b "Wann blickst Du, dass Du zu jung bist?"
    show s1 p7
    a "Du bist nicht Papi."
    b "Muss ich auch nicht um zu wissen, dass Du viel zu-"
    show s1 p8
    "*bumm*"
    show s1 p9
    e "Hört auf."
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

        "Billy die Zunge raus strecken":
            show s1_2 p1
            a "pfft" #streckt die Zunge raus
            hide s1_2
    
    show s1 p14
    b "Dad, bist Du-"
    show s1 p15
    "" #E steht auf
    show s1 p16
    e "Genug, Billy."
    show s1 p17
    e "Morgen Sonnenaufgang, hier. Ja?"
    show s1 p18
    "" #a nickt schnell
    hide s1 p18 with fade
    

#Szene 2
    show s2 p1 with fade
    ""
    show s2 p2
    "" #e auf pferd
    show s2 p3
    "" #a schaut an e vorbei
    show s2 p4
    "*bling*" #fokus auf E's stern
    show s2 p5
    "..." #fokus auf a's stern #punkt für punkt erscheinen
    show s2 p6
    e "Morgen."
    show s2 p8
    k "Hallo!"
    show s2 p7
    a "Guten Morgen!"
    show s2 p9
    s "Guten Morgen Sheriff"

#Szene 3
    show s3 p1 with fade
    "" #Weide
    show s3 p2
    pause
    show s3 p3
    pause
    show s3 p4
    pause
    show s3 p5
    e "So, Kleines."
    show s3 p6
    e "..."
    show s3 p7
    e "Mach mich stolz."
    show s3 p8
    "" #e steigt auf
    show s3 p9
    "" #beide tippen ihren hut

#Szene 4
    show s4 p1 with fade
    pause
    show s4 p2
    pause
    show s4 p3
    pause
    show s4 p4
    pause
    python:
        spielen1 = False
        füttern = False

    menu:
        " "

        "Mit Puppe spielen":
            jump spielen1

        "Tiere füttern":
            jump tiereFüttern1
            
        "Nichts tun":
            jump warten

    #Szene 4.1
    label spielen1:
        show s4_1 p1
        a "seufz" 
        python:
            spielen1 = True  
        menu:
            " "

            "Flöte spielen":
                hide s4_1
                jump spielen2          
            "Tiere füttern" if füttern == False:
                hide s4_1
                jump tiereFüttern1
            "Möhre verfüttern" if füttern == True:
                hide s4_1
                jump tiereFüttern2
            "Nichts tun.":
                hide s4_1
                jump warten   
    
    #Szene 4.4
    label spielen2:
        show s4_4 p1
        "*musik*" #a spielt mit flöte, läuft zaun entlang
        show s4_4 p2
        "*musik*"
        python:
            spielen2 = True
        menu:
            " "
            
            "Tiere füttern" if füttern == False:
                hide s4_4
                jump tiereFüttern1
            "Möhre verfüttern" if füttern == True:
                hide s4_4
                jump tiereFüttern2
            "Nichts tun.":
                hide s4_4
                jump warten
    #Szene 4.6
    label spielen3:
        show s4_6 p1
        "𝅘𝅥 𝅘𝅥𝅯𝅘𝅥𝅯" #a spielt mit flöte, läuft zaun entlang
        show s4_6 p2
        "𝅘𝅥𝅯𝅘𝅥𝅮 𝅘𝅥𝅯" #s folgt ihr
        jump pony
    #Szene 4.2
    label tiereFüttern1:
        show s4_2 p1
        "" #hält gras hin
        show s4_2 p2
        ""
        show s4_2 p3
        "Komm schon. Ist frisch!" #kein tier reagiert
        show s4_2 p4
        "..."
        python:
            füttern = True
        
        menu:
            " "

            "Mit Puppe spielen" if spielen1 == False:
                hide s4_2
                jump spielen1
            "Flöte spielen" if spielen1 == True:
                hide s4_2
                jump spielen2
            
            "Möhre verfüttern":
                hide s4_2
                jump tiereFüttern2

            "Nichts tun.":
                hide s4_2
                jump warten   
    #Szene 4.5
    label tiereFüttern2:
        show s4_5 p1
        a "Ja endlich!"
        menu:
                " "

                "Spielen":
                    hide s4_5
                    jump spielen3
                "Nichts tun.":
                    hide s4_5
                    jump pony   

    #Szene 4.3
    label warten:
        show s4_3 p1
        "" #a liegt vor Zaun, Hut tief im Gesicht, Grashalm im Mund
    #Szene 5
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
        show s5 p6
        ""
        return
        #SLEEPY ENDING
    #Szene 4.7
    label pony:
        show s4_7 p1 with fade
        "" #a liegt vor Zaun, Hut tief im Gesicht, Grashalm im Mund
        show s4_7 p2
        a "hm?" #s stupst a an
        jump szene6
     
    

#Szene 6
label szene6:
    show s6 p1 with fade
    "" #bulle schläft
    show s6 p2 with dissolve
    a "So sieht man sich wieder, Bulle Bill"
    show s6 p3
    a "Du hast die Milch von Paula Kuh geklaut. Dafür wirst Du jetzt-"
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
    show s6 p9
    "*fiiiiiieeeeeep*" #s bäumt sich auf
    show s6 p10
    "" #bulle rennt
    show s6 p11
    "" #chaos
    show s6 p12
    "KRACH!" #bulle zerstört tor
    show s6 p13
    "" #a sitzt und fängt an zu weinen
    show s6 p14
    "" #s stupst a an
    show s6 p15
    ""
    show s6 p16
    ""
    menu:
        " "

        "Hier bleiben":
            jump szene7
        "Den Tieren hinter her":
            jump szene8
#Szene 7
    label szene7:
        show s7 p2 with fade
        ""
        show s7 p3 with dissolve
        ""
        show s7 p4
        e "Sheriffs stehen zu ihren Fehlern, Kleines"
        show s7 p5
        a "Papi..."
        a "Papi... ich.."
        a "Papi... ich.. der Stier! und-!"
        show s7 p6
        e "Beruhig dich. Ist meine Schuld -"
        e "Billy hatte recht."
        e "Deine Stiefel passen nicht in die Stiefel eines Sheriffs."
        show s7 p7
        ""
        return
#Szene 8    
    label szene8:
        b "da da dam daaa da dam" 

        "AAAAHHH! Hilfe!" #geschrei vom dorfeingang

        "..." #tiere rennen durch dorf

        "..." #bewohner rennen in ihre häuser

        "..." #bulle rennt stände um

        "..." #a reitet auf s tieren hinterher

        a "Geht alle nach Hause!"

        "..." #a wirft lasso neben kuh

        "..." #bulle verfolgt kind

        "..." #kind rennt zu tür

        "..." #kind hämmert an tür

        "..." #bulle nimmt anlauf
        
        "..." #a reitet zu ihm

        b "Was zum-? Bist du- Abbey! Warte!"

        "..." #b rennt zu veranda

        b "Abbey! - komm da weg! Warte auf Dad!" #b schaut runter

        "..." #b sieht skorpion

        "..." #a kommt zum halt

        "..." #kind schaut a an

        "..." #bulle scharrt
        menu:
            " "

            "Bulle-Bill anschreien":
                jump szene8_2
            "In Flöte pusten":
                jump szene8_3
    label szene8_2:
        show s8_2 p1
        a "BULLE-BILL!!! ZUERST DIE MILCH VON PAULA-KUH UND NUN DA-!!"
        show s8_2 p2
        "" #a greift zur flöte
        show s8_2 p3
        ""
        show s8_2 p4 with fade
        a "WAHHHHH!!!!"
        show s8_2 p5 with fade
        ""
        return
    label szene8_3:
        



        "*fiiiiiieeeeeep" #a blässt in flöte

        "*fiiiiiieeeeeep*" #kind hält sich ohren zu

        "*fiiiiiieeeeeep*" #b hält sich ohren zu

        a "EEEH!" #s bäumt sich auf, a fällt

        "..." #bulle bockt, rennt weg

        b "..." #bulle rennt an b vorbei

        "..." #bulle zerquetscht skorpion

        "*BANG*" #e schießt

        "..." #e reitet an b vorbei

        "..." #e reitet an a vorbei

        b "..." #b schaut auf skorpion

        e "Abigail, Kleines."

        e "Deine Füße passen nicht in die Stiefel eines Sheriffs."

        a "Nein- aber- Papi- ich- das Pony-"

        e "Is' meine Schuld Kleines. Billy! Wir fangen die Tiere."

        a "..." #weint

        b "..." #b wirft skorpion weg

        b "Nein, Dad."

        "..." #a und e schauen zu b

        b "Abbey hat sich hier voll reingesteigert."
        b "Sie ist den Tieren einfach hinter her. Verdammt, sie hat den Stier lieber auf sich gezogen als auf die"
        
        b "ganzen erwachsenen Weicheier hier!" #e schaut zu a, a nickt

        "..." #a umarmt b

        b "Wenn du mich fragst, macht genau das einen guten Sheriff aus."
        b "Ich habs nichtmal über die Straße geschafft."

        "..." #Bewohner schauen aus den türen raus

        "..." #auch schmied

        e "..." #e schaut zu b&a

        e "Gut, Abbey. Fang das Pony. Billy, sattel dein Pferd."

        e "Lasst uns ein paar Tiere fangen" #black stripes auf seine Augen

#Szene 9
    show s9 p1
    "" #e schlägt weidentor zu
    show s9 p2
    "" #e setzt sich auf pferd
    show s9 p3
    "" #alle reiten in Sonnenuntergang
    show s9 p4
    ""
    return