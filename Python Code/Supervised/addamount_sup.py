# Anfang des Programms
while True:
    # Erfassen der Kundendaten und Kaufbeträge
    cust_no_in = input('ENTER NAME (15 CHARACTERS): ')
    amt1_in = int(input('Enter amount of first purchase (5 digits): '))
    amt2_in = int(input('Enter amount of second purchase (5 digits): '))
    amt3_in = int(input('Enter amount of third purchase (5 digits): '))

    # Speichern des Kundennamens und der Kaufbeträge
    cust_no_out = cust_no_in
    total_out = amt1_in + amt2_in + amt3_in  # Berechnen der Gesamtsumme der Einkäufe

    # Ausgabe der Gesamtsumme
    print(f'{cust_no_out} Total Amount = {total_out}')

    # Überprüfen, ob es weitere Dateneingaben gibt
    more_data = input('MORE INPUT DATA (YES/NO)?: ').upper()

    # Wenn es keine weiteren Daten gibt, beende die Schleife und das Programm
    if more_data == 'NO':
        break
# Ende des Programms
