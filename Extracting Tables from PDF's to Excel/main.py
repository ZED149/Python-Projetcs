

# this is the main for this script
# it extracts table from a pdf file and store it in an Excel file

# importing libraries
import tabula       # extract table from pdf


# extracting table from pdf
pdf_file = "Table+and+Text.pdf"
table = tabula.read_pdf(pdf_file, pages=1)

# now, we need to convert it into an Excel file
table[0].to_excel("Table and Test.xlsx")

