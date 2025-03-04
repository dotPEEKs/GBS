import os
import barcode
from barcode.writer import ImageWriter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import cm

from backend.containers import BRCodeContainer
from backend.util import remove_dir
class PDFGenerator:
    def __init__(self,barcode_container: BRCodeContainer):
        self.pdf_fname = "output.pdf"
        self.barcode_container = barcode_container
    def generate_pdf_file(self,text_x_pos = 10,text_y_pos = 10):
        if os.path.exists("pdf_workarea"):
            remove_dir("pdf_workarea")
        os.makedirs("pdf_workarea")
        barcode_files = []
        for i, data in enumerate(self.barcode_container):
            filename = f"pdf_workarea\\barcode_{i}"
            barcode_class = barcode.get_barcode_class(data[1].replace("-",""))
            barcode_instance = barcode_class(data[2], writer=ImageWriter())
            barcode_instance.save(filename)
            barcode_files.append(filename)

        # PDF oluşturma
        pdf_path = self.pdf_fname
        pdf = canvas.Canvas(pdf_path)

        # PDF sayfa ayarları
        page_width, page_height = 595, 842
        x_start, y_start = 50, 700
        barcode_width, barcode_height = 150, 50
        spacing_x, spacing_y = 30, 20

        # Barkodları 3'erli gruplar halinde PDF'e ekleme
        for i, barcode_file in enumerate(barcode_files):
            row = i // 3  # Satır numarası
            col = i % 3  # Sütun numarası

            x_position = x_start + col * (barcode_width + spacing_x)
            y_position = y_start - row * (barcode_height + spacing_y + 10)

            barcode_image = ImageReader(barcode_file + ".png")
            pdf.drawImage(barcode_image, x_position, y_position + 3, width=4 * cm, height=2 * cm)
            pdf.setFont("Helvetica", 10)
            key,value = self.barcode_container[i]
            position_x = x_position + text_x_pos
            position_y = y_position + text_y_pos + 2
            print(value["barcode_type"])
            if value["barcode_type"] == "EAN-8":
                position_x -= 10
            elif value["barcode_type"] == "ISBN-10":
                position_x -= 11
            elif value["barcode_type"] == "EAN-13":
                position_x -= 13
            elif value["barcode_type"] == "EAN-14":
                position_x -= 14
            pdf.rect(x_position, y_position + 10 , barcode_width, barcode_height + 20)
            pdf.drawString(text=key, x = position_x , y = position_y)
        pdf.save()
        print(f"PDF Created : {pdf_path}")
if __name__ == "__main__":
    container = BRCodeContainer()
    container.push_back("Kapak","ITF","123456")

    pdfgen = PDFGenerator(container)
    pdfgen.generate_pdf_file()
