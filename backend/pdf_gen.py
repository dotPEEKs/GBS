import os
import barcode
import tempfile
from barcode.writer import ImageWriter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import cm

from backend.containers import *
from backend.util import remove_dir
class PDFGenerator:
    def __init__(self,barcode_container: BRCodeContainer):
        self.pdf_fname = "output.pdf"
        self.barcode_container = barcode_container
    def generate_pdf_file(self,text_x_pos = 10,text_y_pos = 10,launch = False):
        temp_dir = tempfile.TemporaryDirectory()
        barcode_files = []
        for i, data in enumerate(self.barcode_container):
            item_name, barcode_data = data
            for brcode_count in range(int(barcode_data["item_count"])):
                filename = os.path.join(temp_dir.name,f"{brcode_count}_{i}")
                barcode_class = barcode.get_barcode_class(barcode_data["barcode_type"].replace("-",""))
                barcode_instance = barcode_class(barcode_data["item_barcode"], writer=ImageWriter())
                barcode_instance.save(filename)
                barcode_files.append(
                    (
                        filename,
                        item_name,
                        barcode_data["barcode_type"],
                        barcode_data["item_barcode"], # Not ilerde bunu bir class yap tuple'dan değiştir
                    )
                )
        # PDF oluşturma
        pdf_path = self.pdf_fname
        pdf = canvas.Canvas(pdf_path)

        # PDF sayfa ayarları
        page_width, page_height = 595, 842
        x_start, y_start = 50, 700
        barcode_width, barcode_height = 150, 50
        spacing_x, spacing_y = 30, 20

        # Barkodları 3'erli gruplar halinde PDF'e ekleme
        for i, barcode_data in enumerate(barcode_files):
            row = i // 3  # Satır numarası
            col = i % 3  # Sütun numarası

            x_position = x_start + col * (barcode_width + spacing_x)
            y_position = y_start - row * (barcode_height + spacing_y + 10)
            barcode_fname = barcode_data[0]
            item_name = barcode_data[1]
            barcode_type = barcode_data[2]
            item_barcode = barcode_data[3]
            barcode_image = ImageReader(barcode_fname + ".png")
            pdf.drawImage(barcode_image, x_position, y_position + 3, width=4 * cm, height=2 * cm)
            pdf.setFont("Helvetica", 10)
            position_x = x_position + text_x_pos
            position_y = y_position + text_y_pos + 2
            if barcode_type == "EAN-8" and len(item_barcode) > 8:
                position_x -= 10
            elif barcode_type == "ISBN-10":
                position_x -= 11
            elif barcode_type == "EAN-13":
                position_x -= 13
            elif barcode_type == "EAN-14":
                position_x -= 14
            pdf.rect(x_position, y_position + 10 , barcode_width, barcode_height + 20)
            pdf.drawString(text=item_barcode, x = position_x , y = position_y)
        pdf.save()
        print(f"PDF Created : {pdf_path}")
        temp_dir.cleanup()
        if launch:
            os.system(f"start {filename}")
if __name__ == "__main__":
    container = BRCodeContainer()
    container.push_back("Kapak","ITF","123456")

    pdfgen = PDFGenerator(container)
    pdfgen.generate_pdf_file()
