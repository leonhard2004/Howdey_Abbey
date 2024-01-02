# Sie können das Skript Ihres Spiels in dieser Datei platzieren.

# Bestimmen Sie Grafiken unterhalb dieser Zeile, indem Sie die "Image-Statements" verwenden.
# z. B. image eileen happy = "eileen_happy.png"
image s1 p1 = im.Scale("S1P1.png", 1920, 1080)
image s1 p2 = im.Scale("S1P2.png", 1920, 1080)
image s1 p3 = im.Scale("S1P3.png", 1920, 1080)
# Bestimmen Sie Charaktere, die in diesem Spiel verwendet werden.
define a = Character('ABBEY', color="#f5910e")
define b = Character('Billy', color="#271b1b")
define e = Character('Eduardo', color = "#5f3719")

# Hier beginnt das Spiel.
label start:
#Szene 1
#Du, Deine, Dich groß schreiben!
    show s1 p1
    "..."
    show s1 p2
    a ""
    a "Uhm.. Papi?"
    show s1 p3
    a "Ich hab überlegt..."
    a "weil, also, ... ich bin ja jetzt schon sieben und wollte daher fragen ob ich-"
    



    return
