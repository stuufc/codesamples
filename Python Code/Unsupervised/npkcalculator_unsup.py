def head_procedure():
    for _ in range(5):
        print(" ")
    print("+-----------------------------------------------+")
    print("+   THE AMAZING NPK CALCULATOR, DONE IN COBOL   +")
    print("+-----------------------------------------------+")
    print(" ")

def input_procedure():
    x = int(input("X?"))
    y = int(input("Y?"))
    return x, y

def find_magic_procedure(x, y, r):
    print(" ")
    if x == 666 or y == 666:
        print("You have entered a magic number.")
        print("Congrats!")
    if r == 666:
        print("You have found a magic number.")
        print("Congrats!")
    print(" ")

def menu_procedure():
    op = input("Please choose an operator [+ - / *]:")
    return op

def calc_procedure(x, y, op):
    if op == '+':
        r = x + y
    elif op == '-':
        r = x - y
    elif op == '*':
        r = x * y
    elif op == '/':
        r = x / y
    return r

def main_procedure():
    head_procedure()
    while True:
        x, y = input_procedure()
        op = menu_procedure()
        r = calc_procedure(x, y, op)
        find_magic_procedure(x, y, r)
        print(" ")
        print(" ")
        print(" ", x)
        print(op, y)
        print("--------------")
        print(" ", r)
        op = input("Want some more [y/n]?")
        if op.lower() == 'n':
            print("Bye!")
            break

main_procedure()
