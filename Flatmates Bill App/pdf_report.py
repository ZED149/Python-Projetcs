
from fpdf import FPDF
import webbrowser
# PdfReport class
class PdfReport:
    """
    This class generates a PDF file containing 2 Flatmates name and amount as their information.
    """

    # Constructor
    def __init__(self, filename):
        self.filename = filename

    # generate()
    def generate(self, flatmate1, flatmate2, bill):
        """
        This function produces a PDF document that contains both flatmates information and
        how much each has to pay. In addition, it also contains the period for them for their stay.
        :param flatmate1:
        :param flatmate2:
        :param bill:
        :return:
        """

        # creating an empty pdf document
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        # adding page to empty pdf document
        pdf.add_page()

        # putting image to the pdf
        pdf.image(self.filename, w=0, h=50)

        # setting font for the title
        pdf.set_font(family="Times", style='BU', size=20)
        # adding cell for the title
        pdf.cell(w=0, h=100, border=1, ln=1, align='C', txt="FLATMATE(s) BILL")

        # putting an empty cell
        pdf.cell(w=0, h=50, border=0, ln=1)

        # changing font style to none
        pdf.set_font(family='Times', style='')

        # now, we need to put details
        pdf.cell(w=100, h=50, border=0, txt="Period: ", align='C')
        # changing font style to italic
        pdf.set_font(family='Times', style='I')
        pdf.cell(w=200, h=50, border=0, txt=bill.period, ln=1, align='C')
        # changing font style to none
        pdf.set_font(family='Times', style='')
        pdf.cell(w=100, h=50, border=0, txt="Amount: ", align='C')
        # changing font style to italic
        pdf.set_font(family='Times', style='I')
        pdf.cell(w=200, h=50, border=0, txt=str(bill.amount), align='C', ln=1)

        # putting an empty cell
        pdf.cell(w=0, h=50, border=0, ln=1)

        # now printing details of flatmates
        # changing font style to none
        pdf.set_font(family='Times', style='')
        pdf.cell(w=100, h=50, border=0, txt=flatmate1.name, align='C')
        # changing font style to italic
        pdf.set_font(family='Times', style='I')
        pdf.cell(w=100, h=50, border=0, txt=str(round(flatmate1.pays(bill, flatmate2))), ln=1, align='C')
        # changing font style to none
        pdf.set_font(family='Times', style='')
        pdf.cell(w=100, h=50, border=0, txt=flatmate2.name, align='C')
        # changing font style to italic
        pdf.set_font(family='Times', style='I')
        pdf.cell(w=100, h=50, border=0, txt=str(round(flatmate2.pays(bill, flatmate1))), ln=1, align='C')

        # putting an empty cell
        pdf.cell(w=0, h=50, border=0, ln=1)

        # printing end line
        pdf.cell(w=0, h=1, border=1, ln=1)

        # outputting it
        pdf.output("files\\bill.pdf")

        # opening it automatically
        webbrowser.open("files\\bill.pdf")
