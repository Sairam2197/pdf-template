from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

csv_file = pd.read_csv("topics.csv")

for index, row in csv_file.iterrows():
    pdf.add_page()
    #setting Header
    pdf.set_font(family="Times", style="BI", size=24)
    pdf.set_text_color(200, 50, 75)
    pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align="L")

    # adding lines
    for i in range(20,298, 10):
        pdf.line(10, i, 200, i)
    pdf.line(10, 21, 200, 21)


    """adding co-ordinates for underline - line under the text, since we have given the unit as mm
we are giving the co-ordinates in mm pdf.line(x1, y1, x2,y2)"""

    #footer setting
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(200, 200, 75)
    pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align="R")


    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(276)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(200, 200, 75)
        pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align="R")

        #adding lines
        for i in range(20, 298, 10):
            pdf.line(10, i, 200, i)

pdf.output('output.pdf')