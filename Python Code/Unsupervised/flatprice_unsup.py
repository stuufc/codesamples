class VariablesExamples:
    def __init__(self):
        self.human_name = ''
        self.human_address = ''
        self.square_meters = 0
        self.square_price = 0.0
        self.tax_percent = 0
        self.negative_value = 0.0
        self.flat_price = 0.0
        self.tax_summ = 0.0

    def input_process(self):
        self.human_name = input("Please enter Name: ")
        self.human_address = input("Please enter Address: ")
        self.square_meters = int(input("Please enter square meters of flat: "))
        self.square_price = float(input("Please enter square meter's price: "))
        self.tax_percent = int(input("Please enter percent of tax: "))
        self.negative_value = float(input("Enter any really big NEGATIVE value: "))

    def calculations_and_display(self):
        print("---------------------------------------")
        print()
        print(self.human_name)
        print(self.human_address)
        print("SQUARE-METERS: ", self.square_meters)
        print("SQUARE-METERS-OUT: ", self.square_meters)
        print("SQUARE-PRICE: ", self.square_price)
        print("SQUARE-PRICE-OUT: ", self.square_price)
        self.flat_price = self.square_meters * self.square_price
        print("FLAT-PRICE: ", self.flat_price)
        print("FLAT-PRICE-OUT-1: ", self.flat_price)
        print("FLAT-PRICE-OUT-2: ", self.flat_price)
        print("TAX-PERCENT: ", self.tax_percent)
        print("TAX-PERCENT-OUT: ", self.tax_percent)

if __name__ == "__main__":
    variables_examples = VariablesExamples()
    variables_examples.input_process()
    variables_examples.calculations_and_display()
