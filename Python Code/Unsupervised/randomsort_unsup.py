import random

def main():
    w_len_arr = 20
    w_arr = [0] * w_len_arr

    # Generiere Zufallszahlen und fülle das Array
    for i in range(w_len_arr):
        w_ran_num = random.randint(1, 99)
        w_arr[i] = w_ran_num
        print("POS: ", i+1, " RANDOM NUMBER: ", w_arr[i])

    # Sortiere das Array (Einfüge-Sortierung)
    for i in range(1, w_len_arr):
        key = w_arr[i]
        j = i - 1

        while j >=0 and key < w_arr[j] :
                w_arr[j+1] = w_arr[j]
                j -= 1

        w_arr[j+1] = key

    # Ausgabe des sortierten Arrays
    for i in range(w_len_arr):
        print("POS: ", i+1, " SORTED: ", w_arr[i])

main()
