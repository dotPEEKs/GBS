import os
from barcode import (ITF,EAN8,EAN13,EAN14,ISBN10)
class Vars:
    target_dir = os.path.join(os.getenv("LocalAppData"),"gbs")
    json_path = os.path.join(os.getenv("LocalAppData"),"gbs","database.json")
    default_user_desktop = os.path.expanduser("~")
    minimum_valid_barcode_len = 8
    barcodes_length = {
        "ITF":{
            "handler":ITF,
            "length":6
        },
        "EAN8":{
            "handler":EAN8,
            "length":8
        },
        "EAN13":{
            "handler":EAN13,
            "length":13
        },
        "EAN14":{
            "handler":EAN14,
            "length":14
        },
        "ISBN10":{
            "handler":ISBN10,
            "length":10
        }
    }

