import json

class Record:
    def __init__(self, name, value, flag):
        self.name = name
        self.value = value
        self.flag = flag

def main():
    record = Record("Test Name", "Test Value", "true")

    # Erzeugung des JSON-Objekts
    try:
        ws_json_output = json.dumps(record.__dict__)
        print("JSON document successfully generated.")
    except Exception as e:
        print(f"Error generating JSON: {e}")
        return

    ws_json_char_count = len(ws_json_output)

    print("Generated JSON for record: ", record.__dict__)
    print("----------------------------")
    print(ws_json_output)
    print("----------------------------")
    print("JSON output character count: ", ws_json_char_count)
    print("Done.")

if __name__ == "__main__":
    main()
