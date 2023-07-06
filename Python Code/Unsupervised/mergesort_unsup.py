import csv

class CustomerRecord:
    def __init__(self, id, last_name, first_name, contract_id, comment):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.contract_id = contract_id
        self.comment = comment

def write_record(file, record):
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([record.id, record.last_name, record.first_name, record.contract_id, record.comment])


def merge_and_display_files():
    print("Merging and sorting files...")
    
    data1 = []
    data2 = []
    
    with open('test-file-1.txt', mode='r') as file1, open('test-file-2.txt', mode='r') as file2:
        data1 = [CustomerRecord(*line.strip().split(',')) for line in file1]
        data2 = [CustomerRecord(*line.strip().split(',')) for line in file2]

    merged_data = sorted(data1 + data2, key=lambda record: int(record.id))
    
    with open('merge-output.txt', mode='w') as merged_file:
        for record in merged_data:
            write_record(merged_file, record)
    
    print("Merged and sorted data:")
    with open('merge-output.txt', mode='r') as merged_file:
        print(merged_file.read())

def sort_and_display_file():
    print("Sorting merged file on descending contract id....")

    with open('merge-output.txt', mode='r') as merged_file:
        data = [CustomerRecord(*line.strip().split(',')) for line in merged_file]

    sorted_data = sorted(data, key=lambda record: int(record.contract_id), reverse=True)
    
    with open('sorted-contract-id.txt', mode='w') as sorted_file:
        for record in sorted_data:
            write_record(sorted_file, record)
            
    print("Sorted data:")
    with open('sorted-contract-id.txt', mode='r') as sorted_file:
        print(sorted_file.read())

def create_test_data():
    print("Creating test data files...")

    with open('test-file-1.txt', mode='w') as file:
        write_record(file, CustomerRecord(1, "last-1", "first-1", 5423, "comment-1"))
        write_record(file, CustomerRecord(5, "last-5", "first-5", 12323, "comment-5"))
        write_record(file, CustomerRecord(10, "last-10", "first-10", 653, "comment-10"))
        write_record(file, CustomerRecord(50, "last-50", "first-50", 5050, "comment-50"))
        write_record(file, CustomerRecord(25, "last-25", "first-25", 7725, "comment-25"))
        write_record(file, CustomerRecord(75, "last-75", "first-75", 1175, "comment-75"))

    with open('test-file-2.txt', mode='w') as file:
        write_record(file, CustomerRecord(999, "last-999", "first-999", 111999, "comment-999"))
        # Add more records if needed
        # ...

if __name__ == "__main__":
    create_test_data()
    merge_and_display_files()
    sort_and_display_file()
    print("Done.")
