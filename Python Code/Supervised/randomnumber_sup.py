import random

def main():
    # Eingabe und Initialisierung der Variablen
    w_result = 0

    # Generieren der Zufallszahlen
    for _ in range(10):  # Wiederhole 10 mal
        w_result = random.randint(1, 100)
        print("Random number: ", w_result)

if __name__ == "__main__":
    main()
