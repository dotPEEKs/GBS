


import os
# -*- coding: <encoding name> -*-
import sys
import pprint
from argparse import ArgumentParser

from ui.db_add import *
from backend.util import init
from backend.backend import *
from backend.msgbox import *
from backend.vars import Vars
from PySide6.QtWidgets import QApplication,QMainWindow

class db_main(QMainWindow):
    def __init__(self,database: Database):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.add_button.clicked.connect(self.check_input_value)
        self.db = database
        self.ui.item_name.textChanged.connect(self.check_name)
        self.ui.item_barcode.textChanged.connect(self.check_brcode_type)
        self.setWindowIcon(QIcon(u':/main/db.png'))
        self.setWindowTitle("Genel Barkod Sistemi ")
    def check_input_value(self):
        item_name = str(self.ui.item_name.text())
        item_barcode = str(self.ui.item_barcode.text())
        if len(item_barcode) == 0 and len(item_name) == 0:
            MessageBox(
                title=":)",
                text="Bir çılgınlık yapıp bilgileri girmeye ne dersin ;)",
                box=Dialogs.DIA_OK | Icon.ICO_INFO
            )
            return
        if self.db.insert_db(item_name,item_barcode):
            MessageBox(
                title = "Başarılı :)",
                text = "Ürün veritabanına eklendi :)",
                box = Dialogs.DIA_OK | Icon.ICO_INFO
            )
        else:
            MessageBox(
                title = "İşlem başarısız :/",
                text = self.db.get_last_error(),
                box = Dialogs.DIA_OK | Icon.ICO_EXCLAMATION
            )
    def check_brcode_type(self):
        text_table = {
            6:{
                "text":"Geçerli barkod tipi: ITF"
            },
            8:{
                "text":"Geçerli barkod tipi: EAN-8"
            },
            10:{
                "text":"Geçerli barkod tipi: ISBN-10"
            },
            13:{
                "text":"Geçerli barkod tipi: EAN-13"
            },
            14:{
                "text":"Geçerli barkod tipi: EAN-14"
            }
        }
        if not text_table.get(len(self.ui.item_barcode.text())) is None:
            self.ui.brcode_type.setText(text_table[len(self.ui.item_barcode.text())]["text"])
        else:
            self.ui.brcode_type.setText("Bilinmeyen barkod tipi :/")
    def check_name(self):
        if len(self.ui.item_barcode.text()) < 1:
            self.ui.brcode_type.setText("Lütfen ürün ismi giriniz ")
        else:
            self.ui.item_barcode.setText("")
if __name__ == "__main__":
    init()
    database = Database(Vars.json_path)
    database = Database(db_path = Vars.json_path)
    database.init_db()
    app = QApplication(sys.argv)
    window = db_main(database = database)
    window.show()
    sys.exit(app.exec())
