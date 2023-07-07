import random

def main():
    # Initialisieren der Liste
    w_arr = [0]*100
    
    # Eingabe und Initialisierung der Variablen
    w_i = 1
    w_j = 1
    w_k = 1

    # Willkommensnachricht
    print("-------------------------------------------------")
    print("- Welcome in the game tip lottery !             -")
    print("- You choose one number from 1 to 100!          -")
    print("-------------------------------------------------")

    print("-------------------------------------------------")
    print("- Generating numbers .......                    -")
    print("-------------------------------------------------")
    
    # Generieren von Zufallszahlen
    for w_i in range(1, 101): # 101, weil die obere Grenze exklusiv ist
        w_num = random.randint(1, 100)
        w_arr[w_i-1] = w_num
    
    # Wählen einer zufälligen "Gewinnzahl"
    while w_k <= 200:
        w_random_tip = random.randint(1, 100)
        w_k += 1
    
    while w_j <= w_random_tip:
        w_j += 1
    
    w_tip = w_arr[w_j-1]

    # Ausgabe der "Gewinnzahl"
    print("-------------------------------------------------")
    print("- Winning number is : ", w_tip)
    print("-------------------------------------------------")

if __name__ == "__main__":
    main()
