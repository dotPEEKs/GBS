import subprocess
import sys

packages_to_install = [
    "nuitka",
    "pypiwin32",
    "pyside6",
    "reportlab",
    "python-barcode",
    "pyserial",
    "pyusb",
    "pillow",
    
]

for package in packages_to_install:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
