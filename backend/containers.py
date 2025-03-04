
from backend import InvalidDbObject
class BRCodeContainer:
    def __init__(self):
        self.container = {}
    def push_back(self,item_name: str,item_brcode_type,item_brcode):
        self.container[item_name] = {"barcode_type":item_brcode_type,"item_barcode":item_brcode}
    def get(self):
        return self.container
    def __iter__(self):
        for key,value in self.container.items():
            yield key,value["barcode_type"],value["item_barcode"]
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
        if db_object.get_db().get("barcodes") is None:
            raise InvalidDbObject("input parameter is invalid parameter must be DB object not %s" % db_object.__class__.__name__)
        self.container.update(db_object.get_db().get("barcodes"))