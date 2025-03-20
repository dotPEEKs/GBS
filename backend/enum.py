from enum import Enum
from enum import auto as Auto

class DigitsEnums:
    ENUM_BAD_PROGRESS = Auto()
    BAD_BARCODE_LEN = Auto()
    BAD_BARCODE_TYPE = Auto()
    BAD_PRINT_DEVICE = Auto()

class Index:
    INDEX_ITEM_NAME = 0
    INDEX_ITEM_BARCODE = 1
    INDEX_QLINE_EDIT = 2
    INDEX_BARCODE_TYPE = 3
    INDEX_ITEM_CHECKBOX_STATUS = 4

class Defaults:
    DEFAULT_QLINE_EDIT_VALUE = 1


