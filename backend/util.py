import os
import string
import random
import platform
import winreg
import subprocess
import win32print
from pathlib import Path
from backend.vars import Vars
from win32com.client import Dispatch

def get_reg(name,path):
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0,
                                       winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None

def get_resource_dir(fname: str) -> str:
    return os.path.join(Path(__file__).parent.parent,"resources",fname)

def get_source(fname: str):
    return os.path.join(Path(__file__).parent.parent, "sources", fname)

def get_user_desktop():
    reg_name = "Desktop"
    reg_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
    if "Windows-7" in platform.platform(): # God damnnnnn win7
        return os.path.join(os.path.expanduser("~"),"Desktop")
    return os.path.normpath(get_reg(reg_name,reg_path))

def get_source_path(filename: str):
    base_path = os.path.join(os.path.dirname(__file__),"resources",filename)
    return base_path

def init():
    if not os.path.exists(Vars.target_dir):
        os.makedirs(Vars.target_dir)
    if not os.path.exists(Vars.json_path):
        with open(Vars.json_path,"w") as f:
            pass

def get_barcode_type(barcode) -> dict:
    for barcode_name,barcodes in Vars.barcodes_length.items():
        if len(barcode) == barcodes["length"]:
            return barcode_name,barcodes["handler"]

def get_barcode_len(barcode):
    for _,barcodes in barcodes_length.items():
        if len(barcode) == barcodes["length"]:
            return barcodes["length"]
    return 0

"""def list_printers():
    print("Pyserial sonuçları")
    import serial.tools.list_ports
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(f"Port: {port.device}, Name: {port.name}, Description: {port.description}")

def list_printers_pyusb():
    print("Pyusb sonuçları")
    import usb.core
    import usb.util

    # Tüm USB cihazlarını ara
    devices = usb.core.find(find_all=True)

    for device in devices:
        print(f"ID: {hex(device.idVendor)}:{hex(device.idProduct)} - {device}")

"""

def list_physical_printers():
    return win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL,None,1)

def CreateRandChar():
    return "".join(random.sample(string.ascii_letters, 8))
def CreateDesktopShortcuts(exe_path):
    lnk_path = os.path.basename(os.path.splitext(exe_path)[0]) + ".lnk"
    lnk_path = os.path.join(get_user_desktop(), lnk_path)
    win32_client = Dispatch("WScript.Shell")
    shortcut = win32_client.CreateShortcut(lnk_path)
    shortcut.TargetPath = exe_path
    shortcut.Save()

def remove_dir(path):
    subprocess.call(["cmd.exe", "/c", "rmdir", "/s","/q", path])