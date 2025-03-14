import os
import warnings
from tempfile import TemporaryDirectory

import barcode
import tempfile
from barcode.writer import ImageWriter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import cm

from backend.containers import *
from backend.util import convert_turkish_char_to_eng
class PDFGenerator:
    def __init__(self,barcode_container: BRCodeContainer):
        self.pdf_fname = "output.pdf"
        self.barcode_container = barcode_container
        self.barcode_files = []
        self.tempdir = TemporaryDirectory()
        self.pdf_page_layout = PDFGenPageSizesContainer()

    def generate_barcode_images(self):
        for i, data in enumerate(self.barcode_container):
            item_name, barcode_data = data
            for brcode_count in range(int(barcode_data["item_count"])):
                filename = os.path.join(self.tempdir.name,f"{brcode_count}_{i}")
                barcode_class = barcode.get_barcode_class(barcode_data["barcode_type"].replace("-",""))
                barcode_instance = barcode_class(barcode_data["item_barcode"], writer=ImageWriter())
                barcode_instance.save(filename)
                print("Creating image: " + os.path.basename(filename))
                self.barcode_files.append(
                    PDFGenContainer(
                        filename,
                        item_name,
                        barcode_data["barcode_type"],
                        barcode_data["item_barcode"]
                    )
                )
    @classmethod
    def align_item_name_text(cls,item_name,barcode_type):
        item_name_len = len(item_name)
        size_tables = {
            "ITF":[
                37, # xpos tab
                6 # barcode_len
            ],
            "EAN8":[
                6,
                8
            ],
            "ISBN10":[
                55,
                6
            ],
            "EAN13":[
                5,
                -6
            ],
            "EAN14":[
                5
                -4
            ]
        }
        if not size_tables.get(barcode_type) is None:
            padsize = size_tables[barcode_type][0]
            minlen = size_tables[barcode_type][1]
            if item_name_len < minlen:
                return padsize
            return padsize + item_name_len
        return -1
    def get_image_padsize(self,barcode_type):
        if barcode_type == "ITF":
            return 13.5
        else:
            return -4

    def calculate_text_alignment(self,pdf, text, font_name="Helvetica", font_size=10, container_width=150):
        pdf.setFont(font_name, font_size)
        text_width = pdf.stringWidth(text, font_name, font_size)
        return (container_width - text_width) / 2
    """
    def create_pdf_doc(self,show_pdf_file = False,text_x_pos = 130,text_y_pos = 60):
        self.generate_barcode_images()
        pdf = canvas.Canvas(self.pdf_fname)
        for i, barcode_data in enumerate(self.barcode_files):
            row = i // 3  # Satır numarası
            col = i % 3  # Sütun numarası
            x_position = self.pdf_page_layout.xpos + col * (self.pdf_page_layout.barcode_width + self.pdf_page_layout.spacing_xpos)
            y_position = self.pdf_page_layout.ypos - row * (self.pdf_page_layout.barcode_height + self.pdf_page_layout.spacing_ypos + 10)
            barcode_image = ImageReader(barcode_data.fname + ".png")
            pdf.drawImage(barcode_image, x_position + self.get_image_padsize(barcode_data.item_barcode_type), y_position + 3, width=4 * cm, height=2 * cm)
            pdf.setFont("Helvetica", 10)
            position_y = y_position + text_y_pos + 2

            aligned_x = x_position + self.calculate_text_alignment(pdf, "Kapak123", "Helvetica", 10, 150)
            pdf.rect(x_position, y_position + 10 , self.pdf_page_layout.barcode_width, self.pdf_page_layout.barcode_height + 20)
            pdf.drawString(text=barcode_data.item_name, x = aligned_x, y = position_y)
        pdf.save()
        print(f"PDF Created : {self.pdf_fname}")
        if show_pdf_file:
            os.system(f"start {self.pdf_fname}")
    """

    def create_pdf_doc(self, show_pdf_file=False, text_x_pos=130, text_y_pos=60):
        self.generate_barcode_images()
        pdf = canvas.Canvas(self.pdf_fname)
        for i, barcode_data in enumerate(self.barcode_files):
            row = i // 3  # Satır numarası
            col = i % 3  # Sütun numarası
            x_position = self.pdf_page_layout.xpos + col * (
                        self.pdf_page_layout.barcode_width + self.pdf_page_layout.spacing_xpos)
            y_position = self.pdf_page_layout.ypos - row * (
                        self.pdf_page_layout.barcode_height + self.pdf_page_layout.spacing_ypos + 10)
            barcode_image = ImageReader(barcode_data.fname + ".png")
            pdf.drawImage(barcode_image, x_position + 15,
                          y_position + 3, width=4 * cm, height=2 * cm)
            pdf.setFont("Helvetica", 10)
            position_y = y_position + text_y_pos + 2
            pdf.rect(x_position, y_position + 10, self.pdf_page_layout.barcode_width,
                     self.pdf_page_layout.barcode_height + 20)

            # Metni hizalama
            aligned_x = x_position + self.calculate_text_alignment(pdf, barcode_data.item_name, "Helvetica", 10,
                                                              self.pdf_page_layout.barcode_width)
            pdf.drawString(aligned_x, position_y, barcode_data.item_name)
        pdf.save()
        print(f"PDF Created : {self.pdf_fname}")
        if show_pdf_file:
            os.system(f"start {self.pdf_fname}")
if __name__ == "__main__":
    container = BRCodeContainer()
    container.push_back("Kapak","ITF","123456")

    pdfgen = PDFGenerator(container)
    pdfgen.generate_pdf_file()
