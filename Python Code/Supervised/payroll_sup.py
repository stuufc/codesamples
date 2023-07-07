def main():
    # Zuweisung von Werten zu Variablen
    who = "Captain COBOL"
    where = "San Jose, California"
    why = "Learn to be a COBOL expert"
    hours = 19
    rate = 23

    # Berechnung des Bruttoverdienstes
    gross_pay = hours * rate

    # Ausgabe der Informationen
    print("Name: ", who)
    print("Location: ", where)
    print("Reason: ", why)
    print("Hours Worked: ", hours)
    print("Hourly Rate: ", rate)
    print("Gross Pay: ", gross_pay)
    print(why, " from ", who)

if __name__ == "__main__":
    main()
