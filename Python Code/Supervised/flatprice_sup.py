# Fragen Sie den Benutzer nach den erforderlichen Daten
human_name = input("Please enter Name: ")
human_address = input("Please enter Address: ")
square_meters = int(input("Please enter square meters of flat: "))
square_price = float(input("Please enter square meter's price: "))
tax_percent = int(input("Please enter percent of tax: "))
negative_value = float(input("Enter any really big NEGATIVE value: "))

print("---------------------------------------")
print(" ")

# Ausgabe der erfassten Daten
print(human_name)
print(human_address)

# Ausgabe und Speicherung von Daten in einer Variablen
square_meters_out = square_meters
print(f"SQUARE-METERS: {square_meters}")
print(f"SQUARE-METERS-OUT: {square_meters_out}")

square_price_out = square_price
print(f"SQUARE-PRICE: {square_price}")
print(f"SQUARE-PRICE-OUT: {square_price_out}")

# Berechnen Sie den Preis der Wohnung und geben Sie ihn aus
flat_price = square_meters * square_price
print(f"FLAT-PRICE: {flat_price}")

flat_price_out_1 = flat_price
flat_price_out_2 = flat_price
print(f"FLAT-PRICE-OUT-1: {flat_price_out_1}")
print(f"FLAT-PRICE-OUT-2: {flat_price_out_2}")

# Ausgabe der Steuerprozentsätze
tax_percent_out = tax_percent
print(f"TAX-PERCENT: {tax_percent}")
print(f"TAX-PERCENT-OUT: {tax_percent_out}")
