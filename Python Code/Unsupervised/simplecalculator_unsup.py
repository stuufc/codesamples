def main():
    n1 = 0
    n2 = 0
    nt = 0
    estado = 0

    while True:
        n1 = float(input("Enter first number: "))
        if n1 == 0:
            continue

        print_menu()

        menu_input = input()

        if menu_input.lower() == "s":
            break

        if menu_input.lower() == "c":
            clear_screen()
            continue

        print("Operator: ", menu_input)

        n2 = float(input("Enter second number: "))
        if n2 == 0:
            continue

        if menu_input == "+":
            nt = n1 + n2
        elif menu_input == "-":
            nt = n1 - n2
        elif menu_input == "/":
            nt = n1 / n2
        elif menu_input == "*":
            nt = n1 * n2

        print("Result: ", nt)
        n1 = nt

    print("Bye!")

def print_menu():
    print("Select operator:")
    print("+ ---> ADD")
    print("- ---> SUBTRACT")
    print("/ ---> DIVIDE")
    print("* ---> MULTIPLY")
    print("C ---> CLEAR")
    print("S ---> EXIT")

def clear_screen():
    print("\033c", end="")

if __name__ == "__main__":
    main()
