import random

def main():
    # Initialisieren der Variablen
    w_len_arr = 20
    w_arr = [0] * w_len_arr

    # Generieren von zufälligen Zahlen
    for w_r in range(w_len_arr):
        w_ran_num = random.randint(1, 99)  # Erzeugen einer Zufallszahl zwischen 1 und 99
        w_arr[w_r] = w_ran_num
        print("POS: ", w_r + 1, " RANDOM NUMBER: ", w_arr[w_r])

    # Sortieren des Arrays mit dem Insertion-Sort-Algorithmus
    for w_i in range(1, w_len_arr):
        w_key = w_arr[w_i]
        w_j = w_i - 1

        while w_j >= 0 and w_arr[w_j] > w_key:
            w_arr[w_j + 1] = w_arr[w_j]
            w_j -= 1

        w_arr[w_j + 1] = w_key

    # Anzeigen der sortierten Elemente
    for w_h in range(w_len_arr):
        print("POS: ", w_h + 1, " SORTED: ", w_arr[w_h])

if __name__ == "__main__":
    main()
