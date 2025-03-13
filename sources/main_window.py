import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from ui.ui_main_window import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from backend.backend import *
from backend.containers import BRCodeContainer
from backend.pdf_gen import PDFGenerator
class GBSMain(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("GENEL BARKOD SİSTEMİ")
        self.setupUi(self)
        self.tableWidget.setHorizontalHeaderLabels(["URUN ADI","BARKOD","ADET","BARKOD TIPI","ONAY"])
        self.db = Database(Vars.json_path)
        self.set_all_printers()
        self.barcode_container = BRCodeContainer()
        self.tableWidget.setRowCount(len(self.db.get_db()["barcodes"]))
        self.pushButton.clicked.connect(self.print_all_barcode)
        self.pushButton_2.clicked.connect(self.clear_all_selected_barcodes)
        self.set_all_brcode()
    def set_all_printers(self):
        for printer in list_physical_printers()[0][1:]:
            if printer != "" and isinstance(printer,str):
                self.comboBox.addItem(printer)
    def set_all_brcode(self):
        for index,barcode_data in enumerate(self.db.get_db()["barcodes"].items()):
            item_name_widget = QTableWidgetItem(barcode_data[0])
            barcode_type_widget = QTableWidgetItem(barcode_data[1]["barcode_type"])
            item_barcode = QTableWidgetItem(barcode_data[1]["item_barcode"])
            self.tableWidget.setItem(index,0,item_name_widget)
            self.tableWidget.setItem(index,1,item_barcode)
            self.tableWidget.setCellWidget(index,2,self.create_qline_edit_widget())
            self.tableWidget.setItem(index,3,barcode_type_widget)
            self.tableWidget.setCellWidget(index,4,self.create_checkbox_widget())
    def create_horizontal_layout(self):
        horizontal_layout = QHBoxLayout()
        horizontal_layout.setContentsMargins(15,0,15,0) # left top right bottom
        return horizontal_layout
    def create_qline_edit_widget(self):
        widget = QWidget()
        layout = self.create_horizontal_layout() # ekledik çünkü QWidget kendisinden diretk addwidget methodu bulundurmuyor bu yüzden bir layout gerekiyor
        qline_edit = QLineEdit()
        qline_edit.setPlaceholderText("çıkartılacak olan barkod adedi giriniz ...")
        qline_edit.setText("1")
        layout.addWidget(qline_edit)
        widget.setLayout(layout)
        return widget
    def create_checkbox_widget(self):
        widget = QWidget()
        layout = self.create_horizontal_layout()
        checkbox = QCheckBox()
        layout.addWidget(checkbox)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        widget.setLayout(layout)
        return widget
    def print_all_barcode(self):
        for row in range(self.tableWidget.rowCount()):
            checkbox = self.tableWidget.cellWidget(row,4)
            checkbox_status = checkbox.findChild(QCheckBox)
            if checkbox_status.isChecked(): # is selected ?
                item_name = self.tableWidget.item(row,0).text()
                item_barcode = self.tableWidget.item(row,1).text()
                qline_edit_data = self.tableWidget.cellWidget(row,2).findChild(QLineEdit)
                item_barcode_type = self.tableWidget.item(row,3).text()
                self.barcode_container.push_back(
                    item_name = item_name,
                    item_brcode_type = item_barcode_type,
                    item_brcode = item_barcode,
                    brcode_count = qline_edit_data.text()
                )
                pdfgen = PDFGenerator(self.barcode_container)
                pdfgen.generate_pdf_file(text_x_pos=15,text_y_pos=60)
    def clear_all_selected_barcodes(self):
        for row in range(self.tableWidget.rowCount()):
            checkbox = self.tableWidget.cellWidget(row,4).findChild(QCheckBox)
            if checkbox.isChecked():
                checkbox.setChecked(False)
if __name__ == "__main__":
    app = QApplication([])
    window = GBSMain()
    window.show()
    app.exec()