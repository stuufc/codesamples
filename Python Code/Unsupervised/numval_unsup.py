def main_procedure():
    ws_x_val = input("Enter first number: ")
    ws_9_val = input("Enter second number: ")

    # In Python wird `float()` benutzt, um einen String in eine Gleitkommazahl zu konvertieren
    ws_total = float(ws_x_val) + int(ws_9_val)

    print("Total: ", ws_total)

main_procedure()