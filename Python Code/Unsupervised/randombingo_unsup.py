import random

def main():
    w_len_arr = 100
    w_arr = [0] * w_len_arr

    print("-------------------------------------------------")
    print("- Welcome in the game tip lottery !             -")
    print("- You choose one number from 1 to 100!          -")
    print("-------------------------------------------------")

    print("-------------------------------------------------")
    print("- Generating numbers .......                    -")
    print("-------------------------------------------------")

    for i in range(w_len_arr):
        w_arr[i] = random.randint(1, 100)

    w_random_tip = random.randint(1, 200)
    w_j = 0
    for _ in range(w_random_tip):
        w_j += 1

    w_tip = w_arr[w_j]

    print("-------------------------------------------------")
    print("- Winning number is : ", w_tip)
    print("-------------------------------------------------")

main()
