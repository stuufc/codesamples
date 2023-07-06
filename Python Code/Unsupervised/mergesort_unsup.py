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

def create_test_data():
    print("Creating test data files...")

    with open('test-file-1.txt', mode='w') as file:
        write_record(file, CustomerRecord(1, "last-1", "first-1", 5423, "comment-1"))
        write_record(file, CustomerRecord(5, "last-5", "first-5", 12323, "comment-5"))
        write_record(file, CustomerRecord(10, "last-10", "first-10", 653, "comment-10"))
        write_record(file, CustomerRecord(50, "last-50", "first-50", 5050, "comment-50"))
        write_record(file, CustomerRecord(25, "last-25", "first-25", 7725, "comment-25"))
        write_record(file, CustomerRecord(75, "last-75", "first-75", 1175, "comment-75"))

if __name__ == "__main__":
    create_test_data()
    print("Done.")
