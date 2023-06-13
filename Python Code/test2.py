# Anfang des Python-Programms

# Definieren von Variablen
n1 = 0
n2 = 0
nt = 0
estado = 0

while True:  # Die Hauptschleife des Programms, die immer läuft, bis wir sie explizit beenden
    print("----------------------------")
    print("|                          |")
    print("|                          |")
    print("|                          |")
    print("----------------------------")
    
    n1 = float(input("Bitte geben Sie die erste Zahl ein: "))  # Eingabe der ersten Zahl
    if n1 == 0:
        continue  # Wenn die Eingabe 0 ist, springen wir zum Anfang der Schleife zurück

    menu_input = input("Wählen Sie eine Option (+: Addieren, -: Subtrahieren, /: Teilen, *: Multiplizieren, C: Löschen, S: Beenden): ")
    if menu_input.lower() == "s":  # Wenn die Eingabe "s" oder "S" ist, beenden wir das Programm
        break
    elif menu_input.lower() == "c":  # Wenn die Eingabe "c" oder "C" ist, springen wir zum Anfang der Schleife zurück (und löschen damit die Eingaben)
        continue

    n2 = float(input("Bitte geben Sie die zweite Zahl ein: "))  # Eingabe der zweiten Zahl
    if n2 == 0:
        continue  # Wenn die Eingabe 0 ist, springen wir zum Anfang der Schleife zurück

    # Berechnungen basierend auf der gewählten Option durchführen
    if menu_input == "+":
        nt = n1 + n2
    elif menu_input == "-":
        nt = n1 - n2
    elif menu_input == "*":
        nt = n1 * n2
    elif menu_input == "/":
        if n2 != 0:  # Um Division durch 0 zu vermeiden
            nt = n1 / n2
        else:
            print("Fehler: Division durch 0 ist nicht erlaubt.")
            continue

    print("Das Ergebnis ist: ", nt)  # Das Ergebnis anzeigen
