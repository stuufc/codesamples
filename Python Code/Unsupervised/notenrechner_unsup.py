import datetime

# Definition der Variablen
name = ""
note1 = 21
note2 = 21
note3 = 21
note4 = 21
fehlstunden = -1
pruefung = 21
durchschnitt = 0
ende_note = 0
m_fehlstunden = 0

# Einige Unterprogramme definiert als Funktionen
def eingabe_verfahren(note_var_name):
    global name
    while True:
        print("Bitte geben Sie die", note_var_name, "ein:")
        note = int(input())
        if 0 <= note <= 20:
            return note

def berechne_durchschnitt():
    global durchschnitt, m_fehlstunden, note1, note2, note3, note4, fehlstunden
    durchschnitt = (note1+note2+note3+note4)/4
    m_fehlstunden = durchschnitt - (fehlstunden/2)
    return durchschnitt, m_fehlstunden

def frueher_bericht_verfahren():
    heute = datetime.datetime.now()
    print(heute.strftime("%d/%m/%y"))
    print("N1:", note1)
    print("N2:", note2)
    print("N3:", note3)
    print("N4:", note4)
    print("Durchschnitt:", durchschnitt)

def schlechter_student_bericht():
    print("NICHT BESTANDEN DURCH FEHLSTUNDEN, MIT NOTE VON", m_fehlstunden)
    print("Anzahl der Fehlstunden:", fehlstunden)
    print("KEINE OPTION FÜR PRÜFUNG.")

def pruefung_bericht_verfahren():
    global ende_note
    ende_note = (durchschnitt + pruefung) / 2
    print("Endnote: ", ende_note)
    if ende_note < 10:
        print("== NICHT BESTANDEN ==")
    else:
        print("== BESTANDEN ==")

# Hauptverfahren
name = input("Bitte geben Sie den Namen ein:")
note1 = eingabe_verfahren("Note 1")
note2 = eingabe_verfahren("Note 2")
note3 = eingabe_verfahren("Note 3")
note4 = eingabe_verfahren("Note 4")
fehlstunden = eingabe_verfahren("Fehlstunden")
berechne_durchschnitt()
frueher_bericht_verfahren()

if durchschnitt < 10:
    print("Durchschnitt unter 10 (NICHT BESTANDEN).")

if fehlstunden > 25 or fehlstunden/2 > durchschnitt:
    schlechter_student_bericht()
else:
    if durchschnitt < 10:
        pruefung = eingabe_verfahren("Prüfung")
        pruefung_bericht_verfahren()
    else:
        print("BESTANDEN.")
