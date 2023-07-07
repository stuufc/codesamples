import datetime

# Variablen-Initialisierung
name = ""
note1 = 21
note2 = 21
note3 = 21
note4 = 21
fehlstunden = -1
durchschnitt = 0
pruefung = 21
eingabe_note = 0
ende_note = 0
m_fehlstunden = 0

def eingabe_verfahren():
    global name, note1, note2, note3, note4, fehlstunden, eingabe_note

    name = input("Bitte geben Sie den Namen ein: ")
    while not name.isalpha():
        name = input("Bitte geben Sie den Namen ein: ")
    
    for i in range(1, 5):
        globals()[f'note{i}'] = int(input(f"Bitte geben Sie die Note {i} ein: "))
        while not (0 <= globals()[f'note{i}'] <= 20):
            globals()[f'note{i}'] = int(input(f"Bitte geben Sie die Note {i} ein: "))

    fehlstunden = int(input("Wie viele Fehlstunden gibt es? "))
    while fehlstunden < 0:
        fehlstunden = int(input("Wie viele Fehlstunden gibt es? "))

def berechne_durchschnitt_verfahren():
    global note1, note2, note3, note4, durchschnitt, fehlstunden, m_fehlstunden

    durchschnitt = (note1 + note2 + note3 + note4) / 4
    m_fehlstunden = durchschnitt - (fehlstunden / 2)

def frueher_bericht_verfahren():
    global name, note1, note2, note3, note4, durchschnitt

    heute = datetime.datetime.now()
    print(heute.strftime("%d/%m/%Y"))
    print(name)
    for i in range(1, 5):
        print(f"N{i}: {globals()[f'note{i}']}")
    print(f"Durchschnitt: {durchschnitt:.2f}")

def schlechter_student_bericht():
    global m_fehlstunden, fehlstunden

    print(f"NICHT BESTANDEN DURCH FEHLSTUNDEN, MIT NOTE VON {m_fehlstunden:.2f}")
    print(f"Anzahl der Fehlstunden: {fehlstunden}")
    print("KEINE OPTION FÜR PRÜFUNG.")

def pruefung_eingabe_verfahren():
    global pruefung, eingabe_note

    pruefung = int(input("Bitte geben Sie die Prüfungsnote ein: "))
    while not (0 <= pruefung <= 20):
        pruefung = int(input("Bitte geben Sie die Prüfungsnote ein: "))

def pruefung_bericht_verfahren():
    global durchschnitt, pruefung, ende_note

    ende_note = (durchschnitt + pruefung) / 2
    print(f"Endnote: {ende_note:.2f}")

    if ende_note < 10:
        print("== NICHT BESTANDEN ==")
    else        print("== BESTANDEN ==")

def haupt_verfahren():
    eingabe_verfahren()
    berechne_durchschnitt_verfahren()
    frueher_bericht_verfahren()
    
    if durchschnitt < 10:
        print("Durchschnitt unter 10 (NICHT BESTANDEN).")

    if fehlstunden > 25 or fehlstunden/2 > durchschnitt:
        schlechter_student_bericht()
    else:
        if durchschnitt < 10:
            pruefung_eingabe_verfahren()
            pruefung_bericht_verfahren()
        else:
            print("BESTANDEN.")

# Hauptprogramm
haupt_verfahren()
