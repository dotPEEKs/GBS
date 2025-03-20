import os
import sys
import json
sys.path.insert(0, os.path.abspath('.'))
from barcode import (
    EAN13,EAN8,
    EAN14,
    ISBN10,ITF
)
from backend.util import *
class Backend:
    """
    - Önceki özellikleri silindi duruma göre ayarlanacak :)
    """
class Database:
    def __init__(self,db_path):
        self.db_path = db_path
        self.init_db()
        self.exceptions = ""
    def get_db(self) -> dict:
        with open(self.db_path,"r") as f:
            return json.load(f)
    def get_last_error(self):
        return self.exceptions
    def insert_db(self,item_name: str,item_barcode: str):
        result = False
        try:
            if self.is_exist(item_name):
                MessageBox(
                    title ="Uyarı !",
                    text = "Aynı üründen veritabanında mevcut ! :)",
                    box = Dialogs.DIA_OK | Icon.ICO_EXCLAMATION
                )
            barcode = self.get_db()
            barcode["barcodes"][item_name] = {
                "item_barcode":item_barcode,
                "barcode_type":str(get_barcode_type(item_barcode)[0])
            }
            with open(self.db_path,"w") as f:
                f.write(json.dumps(barcode,indent = 4))
                result = True
        except Exception as e:
            self.exceptions = str(e)
        return result
    def init_db(self):
        with open(self.db_path,"r") as f:
            if len(f.read()) == 0:
                data = {"barcodes":{}}
                data = json.dumps(data)
                with open(self.db_path,"w") as f:
                    f.write(data)
    def is_exist(self,item_name: str) -> bool:
        return not self.get_db()["barcodes"].get(item_name) is None
    def remove_item(self,item_name: str):
        if self.is_exist(item_name):
            result = self.get_db()
            del result["barcodes"][item_name]
            with open(self.db_path,"w") as f:
                f.write(json.dumps(result,indent = 4))
            print(result)
    def size(self):
        return len(self.get_db()["barcodes"])