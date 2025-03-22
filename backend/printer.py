import win32print
import win32ui
from .containers import PrinterContainer
from backend import Repr
from .enum import DigitsEnums


class Printer(Repr):
    def __init__(self,print_to_file = None):
        self.fname = print_to_file
        self.raw_printer_list = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1)
        self.printer_list = []
        self.retranser_to_list()
        self._default_printer = ""
        self.exception = ""
    def __getitem__(self, item):
        return next(
            (value for value in self.printer_list if value.hwid == item or value.printer_name),None
        )
    def retranser_to_list(self):
        for printer_data in self.raw_printer_list:
            hwid = printer_data[0]
            printer_name = printer_data[2]
            if "," in printer_name:
                printer_name = printer_name.split(",")[0]
            self.printer_list.append(
                PrinterContainer(
                    hwid = hwid,
                    printer_name = printer_name
                )
            )
    def __repr__(self):
        string = ""
        for printer_obj in self.printer_list:
            string+=super().__repr__(obj = printer_obj) + "\n"
        return string
    def print_doc(self):
        if self._default_printer == "":
            return DigitsEnums.BAD_PRINT_DEVICE
        try:
            handle_of_printer = win32print.OpenPrinter(self._default_printer)
            default_printer_info = win32print.GetPrinter(handle_of_printer,2)
            default_printer_info["pDevMode"].DriverData = b"RAW"

            with open(self.fname,"rb") as src:
                printer_dc = win32ui.CreateDC()
                printer_dc = printer_dc.CreatePrinterDC(self._default_printer)
                printer_dc.StartDoc(self.fname)
                printer_dc.StartPage()
                printer_dc.Write(src.read())
                printer_dc.EndPage()
                printer_dc.EndDoc()
                win32print.ClosePrinter(handle_of_printer)
        except Exception as e:
            self.exception = str(e)
            print(e)
            return DigitsEnums.ENUM_BAD_PROGRESS
        return "SUCCES"
    @property
    def set_default_printer(self):
        return self._default_printer
    @set_default_printer.setter
    def set_default_printer(self,value):
        if not isinstance(value,str):
            raise TypeError("Input must be str")
        self._default_printer = value
    @classmethod
    def list_printer(cls):
        instance = cls()
        instance.retranser_to_list()
        return instance.printer_list