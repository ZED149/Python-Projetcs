
import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
import datetime

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    # reading Excel file
    df = pd.read_excel(filepath, sheet_name='Sheet 1')

    # creating an empty pdf document
    pdf = FPDF(orientation="P", unit='mm', format='A4')
    pdf.add_page()
    # now we need to add content to the page
    # setting auto page break to false
    pdf.set_auto_page_break(auto=False, margin=0)
    # setting font style
    pdf.set_font(family="Times", size=24, style='B')
    # storing stem of filepath
    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]
    # writing invoice number to cell
    pdf.cell(w=0, h=12, ln=1, align='L', txt=f"Invoice NR. {invoice_nr}")

    # getting today's date in day-month-year format
    date = datetime.date.today().strftime("%d-%m-%Y")
    # writing date to pdf cell
    pdf.cell(w=0, align='L', h=12, ln=1, txt=f"Date {date}")
    # writing some line breaks
    pdf.ln(2)

    # now we need to print table to the pdf document
    # But first we need to print table headers to the pdf document
    # setting font style to normal
    pdf.set_font(family="Times", style="B", size=12)
    columns = df.columns
    # writing column headers
    pdf.cell(w=25, h=12, txt=f"{columns[0].replace("_", " ").title()}", border=1, align='C')
    pdf.cell(w=50, h=12, txt=f"{columns[1].replace("_", " ").title()}", border=1, align='C')
    pdf.cell(w=25, h=12, txt=f"{columns[2].replace("_", " ").title().split(" ")[0]}", border=1, align='C')
    pdf.cell(w=30, h=12, txt=f"{columns[3].replace("_", " ").title()}", border=1, align='C')
    pdf.cell(w=30, h=12, txt=f"{columns[4].replace("_", " ").title()}", border=1, align='C')

    pdf.ln(12)

    # iterating on df object
    for index, row in df.iterrows():
        # setting font style to normal
        pdf.set_font(family="Times", style="", size=12)
        # writing product id to the cell
        pdf.cell(w=25, h=8, txt=f"{row['product_id']}", border=1)
        pdf.cell(w=50, h=8, txt=f"{row['product_name']}", border=1)
        pdf.cell(w=25, h=8, txt=f"{row['amount_purchased']}", border=1)
        pdf.cell(w=30, h=8, txt=f"{row['price_per_unit']}", border=1)
        pdf.cell(w=30, h=8, txt=f"{row['total_price']}", border=1, ln=1)

    # calculating total sum of the products purchased
    total_price_sum = df['total_price'].sum()

    # now we need to print total price sum on the document
    for i in range(0, 1):
        pdf.cell(w=25, h=8, txt="", border=1)
        pdf.cell(w=50, h=8, txt="", border=1)
        pdf.cell(w=25, h=8, txt="", border=1)
        pdf.cell(w=30, h=8, txt="", border=1)
        pdf.cell(w=30, h=8, txt=f"{total_price_sum}", border=1, ln=1)

    # adding total due amount line
    # setting font size
    pdf.set_font(family="Times", style="B", size=18)
    pdf.ln(10)
    pdf.cell(w=0, h=10, txt=f"The total due amount is {total_price_sum} Euros.", ln=1)

    # adding company name and logo
    pdf.cell(w=15, h=10, txt="ZED ")
    pdf.image("pythonhow.png", w=10)

    # saving pdf document
    pdf.output(f"{invoice_nr}.pdf")


