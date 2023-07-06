def process_plain():
    ws_user_input = input("(plain) Enter a value: ")

    if ws_user_input.isnumeric():
        print(f"{ws_user_input} is numeric!")
    else:
        print(f"{ws_user_input} is not numeric.")

def process_zero_fill():
    ws_user_input_justified = input("(right justify, zero fill) Enter another value: ")

    # Entferne führende Leerzeichen und ersetze sie durch Nullen
    ws_user_input_justified = ws_user_input_justified.lstrip().rjust(len(ws_user_input_justified), '0')

    if ws_user_input_justified.isnumeric():
        print(f"{ws_user_input_justified} is numeric!")
    else:
        print(f"{ws_user_input_justified} is not numeric.")

def process_trim():
    ws_user_input = input("(trim) Enter a third value: ")

    # Entferne alle Leerzeichen
    ws_user_input_trimmed = ws_user_input.replace(" ", "")

    if ws_user_input_trimmed.isnumeric():
        print(f"{ws_user_input_trimmed} is numeric!")
    else:
        print(f"{ws_user_input_trimmed} is not numeric.")


def main():
    process_plain()
    process_zero_fill()
    process_trim()

if __name__ == "__main__":
    main()
