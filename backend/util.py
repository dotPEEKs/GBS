import os
import unicodedata
import string
import random
import winreg
import subprocess
from pathlib import Path
from backend.vars import Vars
from win32com.client import Dispatch
from backend.enum import DigitsEnums


def get_reg(name,path):
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0,
                                       winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return DigitsEnums.ENUM_BAD_PROGRESS

def get_resource_dir(fname: str) -> str:
    return os.path.join(Path(__file__).parent.parent,"resources",fname)

def get_source(fname: str):
    return os.path.join(Path(__file__).parent.parent, "sources", fname)

def get_user_desktop():
    reg_name = "Desktop"
    reg_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
    desktop_path = os.path.normpath(get_reg(reg_name,reg_path))
    if desktop_path.startswith("%"):
        env = desktop_path[0:desktop_path.index("%",1)].replace("%","")
        desktop_path = os.path.join(os.getenv(env),"Desktop")
    return desktop_path
def get_source_path(filename: str):
    base_path = os.path.join(os.path.dirname(__file__),"resources",filename)
    return base_path

def init():
    if not os.path.exists(Vars.target_dir):
        os.makedirs(Vars.target_dir)
    if not os.path.exists(Vars.json_path):
        with open(Vars.json_path,"w") as f:
            pass

def convert_turkish_char_to_eng(input):
    normalized = unicodedata.normalize("NFD",input)
    return "".join(char for char in normalized if not unicodedata.combining(char)).replace("ı","i")

def get_barcode_type(barcode) -> dict:
    for barcode_name,barcodes in Vars.barcodes_length.items():
        if len(barcode) == barcodes["length"]:
            return barcode_name
    return DigitsEnums.BAD_BARCODE_TYPE


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

def is_program_running_exe():
    return globals().get("__compiled__",False) # if program running exe nuitka uses __compiled__ not sys.frozen