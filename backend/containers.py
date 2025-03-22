import win32print

from backend import *
from backend.database import Database


class BRCodeContainer(Repr):
    def __init__(self,**kwargs):
        self.container = {**kwargs}
    def push_back(self,item_name,item_brcode_type,item_brcode,brcode_count):
        self.container[item_name] = {"barcode_type":item_brcode_type,"item_barcode":item_brcode,"item_count":brcode_count}
    def get(self):
        return self.container
    def __iter__(self):
        for key,value in self.container.items():
            yield key,value
    def __getitem__(self,index):
        try:
            key = list(self.container.keys())[index]
            value = self.container[key]
            return key,value
        except:
            return (None,None)
    def __repr__(self):
        repr_string = "<BRCodeContainer("
        for k, v in self.container.items():
            repr_string += f"\t{k}={v},\n"
        repr_string += ")>"
        return repr_string
    def __call__(self,db_object):
        self.dump_from_db(db_object)
    def dump_from_db(self,db_object):
        if not isinstance(db_object,Database):
            raise InvalidDbObject("input parameter is invalid parameter must be DB object not %s" % db_object.__class__.__name__)
        self.container.update(db_object.read())
    def size(self):
        return len(self.container)
class PDFGenContainer(Repr):
    def __init__(self,filename: str,item_name,item_barcode_type,item_barcode):
        self.fname = filename
        self.item_name = item_name
        self.item_barcode_type = item_barcode_type
        self.item_barcode = item_barcode

class PDFGenPageSizesContainer(Repr):
    def __init__(self,xpos = 50,ypos = 700,barcode_width = 150,barcode_height = 50,spacing_xpos = 30,spacing_ypos = 20):
        self.xpos = xpos
        self.ypos = ypos
        self.barcode_width = barcode_width
        self.barcode_height = barcode_height
        self.spacing_xpos = spacing_xpos
        self.spacing_ypos = spacing_ypos

class PrinterContainer(Repr):
    def __init__(self,hwid: int,printer_name: str):
        self.hwid = hwid
        self.printer_name = printer_name

