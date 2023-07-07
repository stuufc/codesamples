import random

# Definieren Sie die Länge des Arrays und die Mindest-/Maximalwerte
len_arr = 10
min_num = 1
max_num = 99

# Generieren Sie ein Array von zufälligen Zahlen
arr = [random.randint(min_num, max_num) for _ in range(len_arr)]

# Drucken Sie das unsortierte Array
print("Unsorted:", arr)

# Führen Sie das Bubble-Sort durch
for j in range(len_arr):
    for k in range(len_arr - j - 1):
        # Wenn das aktuelle Element größer als das nächste ist, tauschen Sie sie
        if arr[k] > arr[k + 1]:
            arr[k], arr[k + 1] = arr[k + 1], arr[k]

# Drucken Sie das sortierte Array
print("Sorted:", arr)
