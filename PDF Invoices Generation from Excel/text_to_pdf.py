

# this program converts texy files into multipage pdf document

from fpdf import FPDF
import glob
from pathlib import Path

pdf = FPDF(orientation="P", unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

filepaths = glob.glob("TextFiles/*.txt")

for filepath in filepaths:
    header = Path(filepath).stem
    data = ""
    with open(filepath, 'r') as f:
        data = f.readline()

    # now we have header and data
    # we can write it on pdf document
    pdf.add_page()
    pdf.set_font(family="Times", style='B', size=24)
    pdf.cell(w=0, h=12, align='L', ln=1, txt=f"{header.capitalize()}")
    pdf.line(12, 21, 200, 21)
    # writing data after the header
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=f"{data}")


pdf.output("check.pdf")
