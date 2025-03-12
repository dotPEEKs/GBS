import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from ui.ui_main_window import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from backend.backend import *

class GBSMain(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("GENEL BARKOD SİSTEMİ")
        self.setupUi(self)
        self.tableWidget.setHorizontalHeaderLabels(["URUN ADI","BARKOD","ADET","BARKOD TIPI","ONAY"])
        self.db = Database(Vars.json_path)
        self.set_all_printers()
        self.set_all_brcode()
        self.barcode_container = []
        self.set_all_brcode()
        self.tableWidget.setRowCount(len(self.db.get_db()["barcodes"]))
        self.pushButton_2.clicked.connect(self.walk_on_table_widget)
    def set_all_printers(self):
        for printer in list_physical_printers()[0][1:]:
            if printer != "" and isinstance(printer,str):
                self.comboBox.addItem(printer)
    def set_all_brcode(self):
        for index,barcode_data in enumerate(self.db.get_db()["barcodes"].items()):
            item_name = barcode_data[0]
            item_name_widget = QTableWidgetItem(item_name)
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
    def walk_on_table_widget(self):
        for row in range(self.tableWidget.rowCount()):
            line_edit = self.tableWidget.cellWidget(row,2) # qtablewidget içersindeki kolon ve sütünlardaki verilere ulaşmak için indexleri veriyoruz fakat widget içersine yerleştirildiği için aşağıdaki findchild methodunu kullanıyoruz

            # fakat normal item methodu kullanılamaz çünkü sadece qtablewidgetitem ile çalışabilir :)
            checkbox = self.tableWidget.cellWidget(row,3)
            brcode_count = line_edit.findChild(QLineEdit)
            checkbox_status = checkbox.findChild(QCheckBox)
            if checkbox_status.isChecked():
                print(self.tableWidget.item(row,1).text())
if __name__ == "__main__":
    app = QApplication([])
    window = GBSMain()
    window.show()
    app.exec()