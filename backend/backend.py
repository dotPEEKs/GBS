import os
import sys
import json
#sys.path.insert(0, os.path.abspath('.'))

from backend.util import *
from backend.msgbox import *
from backend.enum import DigitsEnums
class Database:
    def __init__(self,database_path = Vars.json_path):
        self.database_path = database_path
        self.init_db()
        self.exceptions = ""
    def get_db(self) -> dict:
        with open(self.database_path,"r") as f:
            return json.load(f)
    def write(self,content):
        content = json.dumps(content)
        try:
            with open(self.database_path,"w") as file_fd:
                file_fd.write(content)
        except:
            return False
        return True

    def read(self):
        with open(self.database_path,"r") as file_fd:
            json_content = json.load(file_fd)
            return json_content.get("barcodes",DigitsEnums.BAD_JSON_FILE)

    def insert_db(self,item_name: str,item_barcode: str):
        if self.is_exist(item_name):
            MessageBox(
                title ="Uyarı !",
                text = "Aynı üründen veritabanında mevcut ! :)",
                box = Dialogs.DIA_OK | Icon.ICO_EXCLAMATION
            )
            return False
        if get_barcode_type(item_barcode) != DigitsEnums.BAD_BARCODE_TYPE:
            content = self.read()[item_name] = {
                "item_barcode":item_barcode,
                "barcode_type":get_barcode_type(item_barcode)
            }
            return self.write(content = content)
    def init_db(self):
        database_template = {
            "version":"1.0",
            "barcodes":{}
        }
        if self.size() == 0:
            self.write(database_template)
    def get(self,item):
        return self.read().get(item,DigitsEnums.NON_EXISTING_KEY)
    def is_exist(self,item_name: str) -> bool:
        return self.get(item_name) != DigitsEnums.NON_EXISTING_KEY
    def remove_item(self,item_name: str):
        if self.is_exist(item_name):
            result = self.read()
            if result.pop(item_name,False):
                self.write(result)
    def size(self):
        return len(self.read())
    def __getitem__(self, item):
        return self.get(item)