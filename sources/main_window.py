import os
import subprocess
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
# from backend.printer import Printer disabled :/
from ui.ui_main_window import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from backend.database import Database
from backend.containers import BRCodeContainer
from backend.pdf_gen import PDFGenerator
from backend import check_font_file
from backend.msgbox import *
from backend.vars import Vars
from backend.enum import Index
from backend.enum import Defaults
from backend import is_program_running_exe
class GBSMain(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.db = Database(database_path = Vars.json_path)
        self.barcode_container = BRCodeContainer()
        self.setWindowTitle("GENEL BARKOD SİSTEMİ")
        self.setWindowIcon(QIcon(u":/main/db.png"))
        self.setupUi(self)

        # Widget yapılandırmaları
        self.tableWidget.setHorizontalHeaderLabels(["URUN ADI","BARKOD","ADET","BARKOD TIPI","SEÇ"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.centralwidget.setStyleSheet("QTableWidget::item { color: \"black\";}")
        self.tableWidget.horizontalHeader().setStyleSheet("::section { background-color: 'transparent'; \ncolor: 'black';}")
        self.tableWidget.setStyleSheet("""QTableCornerButton::section { background-color: 'transparent'}""")
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Fixed) # dikey sekmeyi fare ile resizing yapmayı bloklamak için
        self.tableWidget.verticalHeader().setStyleSheet("::section { background-color: 'transparent';\n color: 'black'; }")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers) # bu hücrelerdeki yazıları düzenlenmesini bloklamak için
        self.tableWidget.setRowCount(self.db.size())

        self.save_btn.clicked.connect(self.print_all_barcode)
        self.pushButton_2.clicked.connect(self.clear_all_selected_barcodes)
        self.set_all_brcode()
    def set_all_brcode(self):
        for index,barcode_data in enumerate(self.db.read().items()): # NOT:get_db methodu yeniden adlandırlacak ayrıca direkt barkodları getirecek
            item_name_widget = QTableWidgetItem(barcode_data[0])
            barcode_type_widget = QTableWidgetItem(barcode_data[1]["barcode_type"])
            barcode_type_widget.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item_barcode_widget = QTableWidgetItem(barcode_data[1]["item_barcode"])
            item_barcode_widget.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.tableWidget.setItem(index,Index.INDEX_ITEM_NAME,item_name_widget)
            self.tableWidget.setItem(index,Index.INDEX_ITEM_BARCODE,item_barcode_widget)
            self.tableWidget.setCellWidget(index,Index.INDEX_QLINE_EDIT,self.create_qline_edit_widget())
            self.tableWidget.setItem(index,Index.INDEX_BARCODE_TYPE,barcode_type_widget)
            self.tableWidget.setCellWidget(index,Index.INDEX_ITEM_CHECKBOX_STATUS,self.create_checkbox_widget())
    def create_horizontal_layout(self):
        horizontal_layout = QHBoxLayout()
        horizontal_layout.setContentsMargins(15,0,15,0) # left top right bottom
        return horizontal_layout

    def create_horizontal_layout_for_line_edit(self):
        horizontal_layout = QHBoxLayout()
        horizontal_layout.setContentsMargins(15,0,15,0)  # Daha küçük kenar boşluğu
        return horizontal_layout

    def create_qline_edit_widget(self):
        widget = QWidget()
        layout = self.create_horizontal_layout_for_line_edit()

        qline_edit = QLineEdit()
        qline_edit.setPlaceholderText("bir değer girin")
        ##7a8069
        qline_edit.setStyleSheet("""
            QLineEdit {
                background-color: 'gray';
                border-radius: 15px;
                padding: 5px;
            }
        """)

        qline_edit.setFixedHeight(30)  # ÇOK ÖNEMLİ EĞER Kİ LİNE EDİT İÇİN BORDER-RADİUS EKLEMEK İSTİYORSAK MUTLAKA BUNU GÖZDEN GEÇİRMELİYİZ !!!
        qline_edit.setText(str(
            Defaults.DEFAULT_QLINE_EDIT_VALUE
            )
        )
        layout.addWidget(qline_edit)
        widget.setLayout(layout)
        return widget
    def create_checkbox_widget(self):
        widget = QWidget()
        layout = self.create_horizontal_layout()
        checkbox = QCheckBox()
        checkbox.setStyleSheet(
            """
            QCheckBox::indicator:unchecked {
                background-color: 'gray';
                border-radius: 5px;
            }
            """
        )
        layout.addWidget(checkbox)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        widget.setLayout(layout)
        return widget
    def print_all_barcode(self):
        for row in range(self.tableWidget.rowCount()):
            checkbox = self.tableWidget.cellWidget(row,Index.INDEX_ITEM_CHECKBOX_STATUS)
            checkbox_status = checkbox.findChild(QCheckBox)
            if checkbox_status.isChecked(): # is selected ?
                item_name =  self.tableWidget.item(row,Index.INDEX_ITEM_NAME).text()
                item_barcode = self.tableWidget.item(row,Index.INDEX_ITEM_BARCODE).text()
                qline_edit_data = self.tableWidget.cellWidget(row,Index.INDEX_QLINE_EDIT).findChild(QLineEdit)
                item_barcode_type = self.tableWidget.item(row,Index.INDEX_BARCODE_TYPE).text()
                self.barcode_container.push_back(
                    item_name = item_name,
                    item_brcode_type = item_barcode_type,
                    item_brcode = item_barcode,
                    brcode_count = qline_edit_data.text()
                )
        if self.barcode_container.size() >= 1:
            pdfgen = PDFGenerator(self.barcode_container)
            pdfgen.create_pdf_doc(show_pdf_file = True)
    def save_pdf(self):
        out = self.print_all_barcode()
        if out is None:
            MessageBox(
                title = "UYARI",
                text = "En az 1 barkod seçmelisiniz !",
                box = Dialogs.DIA_OK | Icon.ICO_EXCLAMATION
            )
        else:
            out.create_pdf_doc(show_pdf_file = True)


    def clear_all_selected_barcodes(self):
        for row in range(self.tableWidget.rowCount()):
            checkbox = self.tableWidget.cellWidget(row,4).findChild(QCheckBox)
            qlineedit = self.tableWidget.cellWidget(row,2).findChild(QLineEdit)
            qlineedit.setText(str(Defaults.DEFAULT_QLINE_EDIT_VALUE))
            if checkbox.isChecked():
                checkbox.setChecked(False)
if __name__ == "__main__":
    check_font_file(__file__)
    app = QApplication([])
    window = GBSMain()
    if window.db.size() < 1:
        MessageBox(
            title = "UYARI",
            text = "Herhangi bir veri eklenmemiş !!",
            box = Dialogs.DIA_OK | Icon.ICO_EXCLAMATION
        )
        cmd_command = sys.executable + " " + Vars.db_main_raw_source_path
        if is_program_running_exe():
            cmd_command = Vars.db_main_executable_path
        subprocess.call(cmd_command)
        sys.exit(1)
    else:
        window.show()
        app.exec()
