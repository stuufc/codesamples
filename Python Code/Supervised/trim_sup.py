# Der String ws_test_string_1 enthält führende und abschließende Leerzeichen
ws_test_string_1 = "    hello world       "

# Display the original and trimmed versions
print("--" + ws_test_string_1 + "--")
print("--" + ws_test_string_1.strip() + "--")  # Removes leading and trailing spaces
print("--" + ws_test_string_1.lstrip() + "--")  # Removes leading spaces
print("--" + ws_test_string_1.rstrip() + "--")  # Removes trailing spaces

# Erstellen eines weiteren Strings für weitere Operationen
ws_test_string_2 = "******************************"

# Anzeigen und Überschreiben von ws_test_string_2 mit verschiedenen Versionen von ws_test_string_1
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

# Bearbeiten und Anzeigen eines String-Literals
print("--" + "    String literal    " + "--")
print("--" + "    String literal    ".strip() + "--")
print("--" + "    String literal    ".lstrip() + "--")
print("--" + "    String literal    ".rstrip() + "--")
