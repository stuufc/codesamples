def main():
    ws_source_str = "Hello World"

    print("=" * 50)
    print("EX 1: SIMPLE UNSTRING")
    print("SOURCE STRING: ", ws_source_str)
    ws_part_1, ws_part_2 = ws_source_str.split()
    print("PART1: ", ws_part_1)
    print("PART2: ", ws_part_2)

    print("\n" + "=" * 50)
    print("EX 2: UNSTRING MULTIPLE TIMES INTO SAME DEST.")
    print("SOURCE STRING: ", ws_source_str)
    ws_parts = ws_source_str.split()
    for i, ws_part in enumerate(ws_parts, start=1):
        print("PART VALUE: ", ws_part)
        print("POINTER: ", i)

    print("\n" + "=" * 50)
    print("EX 3: UNSTRING INTO EXPLICIT FIELDS")
    print("SOURCE STRING: ", ws_source_str)
    ws_part_1, ws_part_2 = ws_source_str.split()
    print("PART1: ", ws_part_1)
    print("PART2: ", ws_part_2)

    print("\n" + "=" * 50)
    print("EX 4: UNSTRING WITH MULTIPLE DELIMITERS")
    ws_source_str = "A<B<CD>E%FG!HIJ|KL!MN>OP#QR!ST"
    print("SOURCE STRING: ", ws_source_str)
    delimiters = "<>!|"
    ws_parts = [part for part in re.split("|".join(map(re.escape, delimiters)), ws_source_str) if part]
    for i, ws_part in enumerate(ws_parts, start=1):
        print("VALUE: ", ws_part)
        print("CURRENT POINTER: ", i)
        print("TOTAL FIELDS FILLED: ", len(ws_parts))

    print("\n" + "=" * 50)
    print("EX 5: UNSTRING WITH MULTIPLE DELIMITERS INTO MULTIPLE DESTINATIONS")
    ws_source_str = "A<B<CD>EFG!HIJ|KLMN>O"
    print("SOURCE STRING: ", ws_source_str)
    ws_parts = [part for part in re.split("|".join(map(re.escape, delimiters)), ws_source_str) if part]
    for i, ws_part in enumerate(ws_parts, start=1):
        print("STRING NUMBER: ", i)
        print("VALUE: ", ws_part)
        print("TOTAL FIELDS FILLED: ", len(ws_parts))

    print("\n" + "=" * 50)
    print("EX 6: UNSTRING FORMATTED NUMBER")
    ws_source_num = "123,456.12"
    print("SOURCE VALUE: ", ws_source_num)
    ws_parts = [part for part in re.split(",|\.", ws_source_num) if part]
    print("PART 1: ", ws_parts[0])
    print("PART 2: ", ws_parts[1])
    print("PART 3: ", ws_parts[2])


if __name__ == "__main__":
    main()
