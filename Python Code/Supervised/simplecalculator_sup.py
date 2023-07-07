def clear_screen():
    print("\033c", end="")  # clear screen command for UNIX systems

def compute(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    else:
        return None

def main():
    while True:
        clear_screen()
        try:
            n1 = float(input("Enter the first number (or 0 to quit): "))
            if n1 == 0:
                break
        except ValueError:
            print("Invalid input.")
            continue

        while True:
            print("\nSelect operator:")
            print("+ ---> ADD")
            print("- ---> SUBTRACT")
            print("/ ---> DIVIDE")
            print("* ---> MULTIPLY")
            print("C ---> CLEAR")
            print("S ---> QUIT")

            op = input("\nYour choice: ")

            if op.upper() == 'S':
                return
            elif op.upper() == 'C':
                break
            elif op in {'+', '-', '*', '/'}:
                try:
                    n2 = float(input("\nEnter the second number (or 0 to quit): "))
                    if n2 == 0:
                        break
                except ValueError:
                    print("Invalid input.")
                    continue

                result = compute(n1, n2, op)
                print("\nThe result is: ", result)
                input("\nPress enter to continue.")
                break
            else:
                print("Invalid operator.")
                input("\nPress enter to continue.")

if __name__ == "__main__":
    main()
