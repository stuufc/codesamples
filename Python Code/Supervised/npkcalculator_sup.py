# Initialisiere Variablen
X = 0
Y = 0
R = 0
N = 0
OP = ''

# Helferfunktionen
def is_magic(num):
    """Überprüft, ob eine Zahl 'magisch' ist."""
    return num == 666

def calc(x, y, operator):
    """Berechnet das Ergebnis der Operation, die auf 'x' und 'y' mit dem gegebenen Operator angewendet wird."""
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        return x / y
    else:
        raise ValueError("Ungültiger Operator")

def display_result(x, y, result, operator):
    """Zeigt das Ergebnis einer Operation an."""
    print()
    print(x)
    print(operator, y)
    print("--------------")
    print(result)

def head_procedure():
    for _ in range(5):
        print()
    print("+-----------------------------------------------+")
    print("+   THE AMAZING NPK CALCULATOR, DONE IN PYTHON  +")
    print("+-----------------------------------------------+")
    print()

def input_procedure():
    global X, Y
    X = int(input("X? "))
    Y = int(input("Y? "))

def find_magic_procedure():
    print()
    if is_magic(X) or is_magic(Y):
        print("You have entered a magic number.")
        print("Congrats!")
    if is_magic(R):
        print("You have found a magic number.")
        print("Congrats!")
    print()

def menu_procedure():
    global OP
    OP = input("Please choose an operator [+ - / *]: ")

def calc_procedure():
    global R
    R = calc(X, Y, OP)
    display_result(X, Y, R, OP)

# Hauptprogramm
def main_procedure():
    while True:
        head_procedure()
        input_procedure()
        menu_procedure()
        calc_procedure()
        find_magic_procedure()
        again = input("Want some more [y/n]? ")
        if again.lower() == 'n':
            print("Bye!")
            break

# Führe das Hauptprogramm aus
if __name__ == "__main__":
    main_procedure()
