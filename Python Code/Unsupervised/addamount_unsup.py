class AddAmt:
    def __init__(self):
        self.more_data = 'YES'

    def main(self):
        while self.more_data.upper() != 'NO':
            self.cust_no_in = input('ENTER NAME (15 CHARACTERS): ')
            self.amt1_in = int(input('Enter amount of first purchase (5 digits): '))
            self.amt2_in = int(input('Enter amount of second purchase (5 digits): '))
            self.amt3_in = int(input('Enter amount of third purchase (5 digits): '))
            
            self.cust_no_out = self.cust_no_in
            self.total_out = self.amt1_in + self.amt2_in + self.amt3_in

            print(f'{self.cust_no_out} Total Amount = {self.total_out}')

            self.more_data = input('MORE INPUT DATA (YES/NO)? ').upper()

if __name__ == "__main__":
    add_amt = AddAmt()
    add_amt.main()
