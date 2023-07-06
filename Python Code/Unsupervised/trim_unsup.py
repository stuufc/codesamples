def main():
    ws_test_string_1 = "    hello world       "
    ws_test_string_2 = ""

    print("--" + ws_test_string_1 + "--")
    print("--" + ws_test_string_1.strip() + "--")
    print("--" + ws_test_string_1.lstrip() + "--")
    print("--" + ws_test_string_1.rstrip() + "--")

    ws_test_string_2 = "******************************"
    print(ws_test_string_2)
    ws_test_string_2 = ws_test_string_1
    print(ws_test_string_2)

    ws_test_string_2 = "******************************"
    print(ws_test_string_2)
    ws_test_string_2 = ws_test_string_1.strip()
    print(ws_test_string_2)

    ws_test_string_2 = "******************************"
    print(ws_test_string_2)
    ws_test_string_2 = ws_test_string_1.lstrip()
    print(ws_test_string_2)

    ws_test_string_2 = "******************************"
    print(ws_test_string_2)
    ws_test_string_2 = ws_test_string_1.rstrip()
    print(ws_test_string_2)

    print("--" + "    String literal    " + "--")
    print("--" + "    String literal    ".strip() + "--")
    print("--" + "    String literal    ".lstrip() + "--")
    print("--" + "    String literal    ".rstrip() + "--")

if __name__ == "__main__":
    main()
