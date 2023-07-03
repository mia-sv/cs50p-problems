from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.set_font("helvetica", size=50)
pdf.text(40, 45, txt="CS50 Shirtificate")

pdf.image("shirtificate.png", w=200, x=5, y=70)
pdf.set_font("helvetica", size=28)

name = input("Name: ")

pdf.set_text_color(r=255)
pdf.cell(w=190, h=230, txt=f"{name} took CS50", align="C")

pdf.output("shirtificate.pdf")
