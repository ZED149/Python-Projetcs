


# This is the main file for FLAT MATES APP program

from bill import Bill
from flatmate import Flatmate
from pdf_report import PdfReport

# flatmates objects
salman = Flatmate(name="Salman", days_in_house=20)
awais = Flatmate(name="Awais", days_in_house=30)

# bill object
bill = Bill(amount=120, period="November 2023")

print(salman.pays(bill, awais))
p = PdfReport("files\\house.png")
p.generate(salman, awais, bill)

