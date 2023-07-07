import json

def json_generate_example():
    # Definieren Sie ein Dictionary für den Datensatz
    ws_record = {
        "name": None,
        "value": None,
        "enabled": None,
    }

    # Füllen Sie den Datensatz
    ws_record["name"] = "Test Name"
    ws_record["value"] = "Test Value"
    ws_record["enabled"] = True

    try:
        # Generieren Sie JSON aus dem Datensatz
        ws_json_output = json.dumps(ws_record)
        print("JSON document successfully generated.")
    except Exception as e:
        print(f"Error generating JSON: {e}")
        return

    # Anzeigen der Ergebnisse
    print("Generated JSON for record: ", ws_record)
    print("----------------------------")
    print(ws_json_output)
    print("----------------------------")
    print("JSON output character count: ", len(ws_json_output))
    print("Done.")

# Aufruf der Funktion
json_generate_example()
