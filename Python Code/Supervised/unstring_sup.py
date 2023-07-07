# Initialize the source string
ws_source_str = "Hello World"

print("EX 1 : SIMPLE UNSTRING")
print("SOURCE STRING: " + ws_source_str)

# Split the string into two parts
ws_part_1, ws_part_2 = ws_source_str.split()

print("PART1: " + ws_part_1)
print("PART2: " + ws_part_2)

print("=================================================")
print("EX 2 : UNSTRING MULTIPLE TIMES INTO SAME DEST.")

# Split the string into two parts, but use a pointer to remember where we left off
ws_pointer = 1

for _ in range(2):
    try:
        ws_part_1, ws_source_str = ws_source_str.split(maxsplit=1)
    except ValueError:  # Too many values to unpack (string was not split)
        print("ERROR: OVERFLOW")
    else:
        print("Successfully unstrung.")

    print("PART VALUE: " + ws_part_1)
    print("POINTER: " + str(ws_pointer))

    ws_pointer += len(ws_part_1) + 1  # Update the pointer

# Hier endet meine Übersetzung. Die weitere Umsetzung erfordert eine genauere Betrachtung der Funktionalitäten im COBOL-Code, 
# um sicherzustellen, dass die Übersetzung korrekt ist.
