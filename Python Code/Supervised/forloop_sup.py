# Definieren Sie die Variablen, die für die Schleifen benötigt werden
w_i = 0
w_j = 0
w_k = 0

# Führen Sie die erste Schleife aus
while w_i <= 20:
    w_j = w_i
    w_i += 1

    while w_j <= 20:
        w_k = w_j * w_i
        print(f"UNTIL: {w_i} W-K: {w_k} = {w_j} * {w_i}")
        w_j += 1

# Setzen Sie die Werte der Variablen auf 0 zurück
w_i = 0
w_j = 0
w_k = 0

# Führen Sie die zweite Schleife aus
for w_i in range(1, 21):
    w_j = w_i
    w_i += 1

    for w_j in range(1, 21):
        w_k = w_j * w_i
        print(f"VARYING: {w_i} W-K: {w_k} = {w_j} * {w_i}")
        w_j += 1
