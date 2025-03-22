import os
import json
from backend.util import get_barcode_type
from backend.enum import DigitsEnums
from backend import create_dbs_dir_if_needed
class Database:
    def __init__(self,database_path):
        create_dbs_dir_if_needed()
        self.database_path = database_path
        self.empty_json_template = {
            "version": "1.0",
            "barcodes": {}
        }
        self.create_new_json_template_if_needed()
    def create_new_json_template_if_needed(self):
        if self.get_fsize() == 0 or not os.path.exists(self.database_path):
            with open(self.database_path,"w") as fd:
                fd.write(self.json_dump(self.empty_json_template))
    def raw_write(self,content: dict):
        try:
            with open(self.database_path,"w") as fd:
                result = self.json_dump(content)
                if result != DigitsEnums.BAD_JSON_FILE:
                    fd.write(result)
        except Exception as e:
            print(e)
            return False
        return True
    def raw_read(self):
        with open(self.database_path,"r") as file_fd:
            content = self.json_load(file_fd.read())
            return content
    def json_dump(self,content: dict):
        try:
            output =  json.dumps(content,indent = 4)
        except:
            return DigitsEnums.BAD_JSON_FILE
        return output
    def json_load(self,content: str):
        try:
            output = json.loads(content)
        except json.JSONDecodeError:
            return DigitsEnums.BAD_JSON_FILE
        return output
    def getfsize(self):
        return os.path.getsize(self.database_path)
    def read(self):
        content = self.raw_read()
        if content == DigitsEnums.BAD_JSON_FILE:
            return False
        return content["barcodes"]
    def exists(self,item):
        return not self.read().get(item,DigitsEnums.NON_EXISTING_KEY) == DigitsEnums.NON_EXISTING_KEY
    def add_item(self,item_name = "Default Item Name",item_barcode = "123456"):
        if self.exists(item_name):
            return False
        database_content = self.raw_read()
        if database_content != DigitsEnums.BAD_JSON_FILE and get_barcode_type(item_barcode) != DigitsEnums.BAD_BARCODE_TYPE:
            database_item_dictionary_template = {
                "item_barcode":item_barcode,
                "barcode_type":get_barcode_type(item_barcode)
            }
            database_content["barcodes"][item_name] = database_item_dictionary_template
            return self.raw_write(database_content)

    def get_fsize(self):
        fsize = 0
        try:
            fsize = os.path.getsize(self.database_path)
        except:
            pass
        return fsize
    def clear_database(self):
        if self.raw_read() != DigitsEnums.BAD_JSON_FILE:
            data = self.raw_read()
            data["barcodes"] = {}
            return self.raw_write(data)
    def size(self):
        barcode_size = len(self.read())
        return barcode_size if barcode_size != 0 else 0
    def delete_item(self,item):
        if self.exists(item):
            database = self.raw_read()
            database["barcodes"].pop(item)
            self.raw_write(database)
