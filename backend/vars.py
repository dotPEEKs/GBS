import os
import sys
from barcode import (ITF,EAN8,EAN13,EAN14,ISBN10)

class Vars:
    real_path = os.path.join(os.path.dirname(__file__),"..","sources")
    target_dir = os.path.join(os.getenv("LocalAppData"),"gbs")
    json_path = os.path.join(os.getenv("LocalAppData"),"gbs","database.json")
    font_file_path = os.path.join(target_dir,"font.ttf")
    main_window_executable_path = os.path.join(target_dir,"main_window.exe")
    db_main_executable_path = os.path.join(target_dir,"db_main.exe")
    main_window_raw_source_path = os.path.join(real_path,"main_window.py")
    db_main_raw_source_path = os.path.join(real_path,"db_main.py")
    barcodes_length = {
        "ITF": {
            "handler": ITF,
            "length": 6
        },
        "EAN8": {
            "handler": EAN8,
            "length": 8
        },
        "EAN13": {
            "handler": EAN13,
            "length": 13
        },
        "EAN14": {
            "handler": EAN14,
            "length": 14
        },
        "ISBN10": {
            "handler": ISBN10,
            "length": 10
        }
    }

