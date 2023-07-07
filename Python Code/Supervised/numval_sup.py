def main_procedure():
    # Eingabeaufforderung für den Benutzer
    ws_x_val = input("Enter first number: ")
    ws_9_val = input("Enter second number: ")

    # Konvertierung des ersten Werts in eine Zahl und Berechnung der Summe
    ws_total = float(ws_x_val) + float(ws_9_val)

    # Anzeige der Gesamtsumme
    print("Total: ", ws_total)

if __name__ == "__main__":
    main_procedure()
