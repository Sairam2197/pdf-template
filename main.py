from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

csv_file = pd.read_csv("topics.csv")

for index, row in csv_file.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="BI", size=24)
    pdf.set_text_color(200, 50, 75)
    pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align="L")
    pdf.line(10, 21, 200, 21)
"""adding co-ordinates for underline - line under the text, since we have given the unit as mm
we are giving the co-ordinates in mm pdf.line(x1, y1, x2,y2)"""


pdf.output("output.pdf")