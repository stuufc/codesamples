def is_numeric_test():
    # Funktion, die prüft, ob eine Eingabe nur aus Ziffern besteht
    def is_numeric(input_str):
        return input_str.isdigit()

    # Prozess: Plain
    ws_user_input = input("(plain) Enter a value: ")
    if is_numeric(ws_user_input):
        print(f"{ws_user_input} is numeric!")
    else:
        print(f"{ws_user_input} is not numeric.")

    # Prozess: Zero-Fill
    ws_user_input_justified = input("(right justify, zero fill) Enter another value: ")
    ws_user_input_justified = ws_user_input_justified.replace(" ", "0") # ersetzt Leerzeichen durch Nullen
    if is_numeric(ws_user_input_justified):
        print(f"{ws_user_input_justified} is numeric!")
    else:
        print(f"{ws_user_input_justified} is not numeric.")

    # Prozess: Trim
    ws_user_input = input("(trim) Enter a third value: ")
    ws_user_input = ws_user_input.replace(" ", "") # entfernt Leerzeichen
    if is_numeric(ws_user_input):
        print(f"{ws_user_input} is numeric!")
    else:
        print(f"{ws_user_input} is not numeric.")

# Aufruf der Funktion
is_numeric_test()
