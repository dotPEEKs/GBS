import os
import shutil
import time
import barcode
from barcode.writer import ImageWriter
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from backend.containers import *
from backend.util import convert_turkish_char_to_eng, get_user_desktop
from tempfile import TemporaryDirectory
from reportlab.pdfgen import canvas
class PDFGenerator(Repr):
    def __init__(self,barcode_container: BRCodeContainer):
        self.pdf_fname = "output.pdf"
        self.barcode_container = barcode_container
        self.barcode_files = []
        self.tempdir = TemporaryDirectory()
        self.pdf_page_layout = PDFGenPageSizesContainer()
        self.pagesize = A4
    def generate_barcode_images(self):
        try:
            for i, data in enumerate(self.barcode_container):
                item_name, barcode_data = data
                for brcode_count in range(int(barcode_data["item_count"])):
                    filename = os.path.join(self.tempdir.name,f"{brcode_count}_{i}")
                    barcode_class = barcode.get_barcode_class(barcode_data["barcode_type"].replace("-",""))
                    img_writer = ImageWriter()
                    img_writer.font_path = os.path.join(Vars.target_dir,"font.ttf")
                    barcode_instance = barcode_class(barcode_data["item_barcode"], writer = img_writer)
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
        except Exception as e:
            pass

    def calculate_text_alignment(self,pdf, text, font_name="Helvetica", font_size=10, container_width=150):
        pdf.setFont(font_name, font_size)
        text_width = pdf.stringWidth(text, font_name, font_size)
        return (container_width - text_width) / 2

    def create_pdf_doc(self, show_pdf_file=False,save_to_desktop = True):
        text_y_pos = 60
        self.generate_barcode_images()
        pdf = canvas.Canvas(self.pdf_fname)
        pdf.setTitle("GBS - Barkod listesi")
        page_index = 0
        for barcode_data in self.barcode_files:
            if page_index == 24: # burayı düzenle ve bir enum sınıfı oluştur
                page_index = 0
                pdf.showPage()
            row = page_index // 3  # Satır numarası
            col = page_index % 3  # Sütun numarası
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

            if len(barcode_data.item_name) > 15:
                barcode_data.item_name = barcode_data.item_name[:8] + "..." + barcode_data.item_name[-4:]
            aligned_x = x_position + self.calculate_text_alignment(pdf, barcode_data.item_name, "Helvetica", 10,
                                                                   self.pdf_page_layout.barcode_width)
            pdf.drawString(aligned_x, position_y, convert_turkish_char_to_eng(barcode_data.item_name))
            page_index+=1
        pdf.save()
        print(f"PDF Created : {self.pdf_fname}")
        if show_pdf_file:
            os.system(f"start {self.pdf_fname}")
        if save_to_desktop:
            desktop_path = get_user_desktop()
            shutil.copy(self.pdf_fname,os.path.join(desktop_path,"pdf_" + time.strftime("%H_%M_%d_%m_%S") + "-GBS" + os.path.basename(self.pdf_fname)))

if __name__ == "__main__":
    container = BRCodeContainer()
    container.push_back("Kapak","ITF","123456")

    pdfgen = PDFGenerator(container)
    pdfgen.generate_pdf_file()
