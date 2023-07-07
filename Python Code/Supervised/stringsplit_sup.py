# Die Variable w_string ist der zu verarbeitende String
w_string = "HOHOHOHOHO"

# Die Anweisung 'for' in Python ist äquivalent zur Anweisung 'PERFORM VARYING' in COBOL
for w_count in range(1, len(w_string) + 1):  # Python range endet bei 'stop - 1'
    # Python indiziert von 0 anstelle von 1 in COBOL, daher 'w_count - 1'
    print(w_string[w_count - 1])
