import pandas as pd

def create_test_data():
    print("Creating test data files...")
    
    # Hier erstellen wir die Testdaten. Sie können diese Daten durch die tatsächlichen Daten ersetzen.
    data_1 = pd.DataFrame({
        'customer_id': [1, 5, 10, 50, 25, 75],
        'customer_last_name': ['last-1', 'last-5', 'last-10', 'last-50', 'last-25', 'last-75'],
        'customer_first_name': ['first-1', 'first-5', 'first-10', 'first-50', 'first-25', 'first-75'],
        'customer_contract_id': [5423, 12323, 653, 5050, 7725, 1175],
        'customer_comment': ['comment-1', 'comment-5', 'comment-10', 'comment-50', 'comment-25', 'comment-75']
    })
    
    data_2 = pd.DataFrame({
        'customer_id': [999, 101, 102, 1000, 103, 105],
        'customer_last_name': ['last-999', 'last-101', 'last-102', 'last-1000', 'last-103', 'last-105'],
        'customer_first_name': ['first-999', 'first-101', 'first-102', 'first-1000', 'first-103', 'first-105'],
        'customer_contract_id': [10000, 202, 300, 4000, 500, 600],
        'customer_comment': ['comment-999', 'comment-101', 'comment-102', 'comment-1000', 'comment-103', 'comment-105']
    })
    
    # Schreiben der Daten in eine Textdatei
    data_1.to_csv('test-file-1.txt', index=False)
    data_2.to_csv('test-file-2.txt', index=False)

def merge_and_display_files():
    try:
        # Dateien einlesen
        test_file_1 = pd.read_csv('test-file-1.txt')
        test_file_2 = pd.read_csv('test-file-2.txt')

        # Dateien zusammenführen
        merged_file = pd.concat([test_file_1, test_file_2])

        # Dateien sortieren und abspeichern
        merged_file = merged_file.sort_values(by=['customer_id'])
        merged_file.to_csv('merge-output.txt', index=False)

        print("Merged and sorted files...")
        print(merged_file)
    except Exception as e:
        print(f"Error merging and sorting files: {e}")

def sort_and_display_file():
    try:
        # Datei einlesen
        merged_file = pd.read_csv('merge-output.txt')

        # Datei sortieren und abspeichern
        sorted_file = merged_file.sort_values(by=['customer_contract_id'], ascending=False)
        sorted_file.to_csv('sorted-contract-id.txt', index=False)

        print("Sorted merged file on descending contract id....")
        print(sorted_file)
    except Exception as e:
        print(f"Error sorting file: {e}")

def main_procedure():
    create_test_data()
    merge_and_display_files()
    sort_and_display_file()
    print("Done.")

main_procedure()