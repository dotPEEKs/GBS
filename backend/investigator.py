import os
import ctypes
import functools
import ctypes.wintypes
from backend.util import get_user_desktop
from backend.util import CreateRandChar
from backend.msgbox import *
class BITMAP(ctypes.Structure):
    _fields_ = [
        ("bmType", ctypes.wintypes.LONG),
        ("bmWidth", ctypes.wintypes.LONG),
        ("bmHeight", ctypes.wintypes.LONG),
        ("bmWidthBytes", ctypes.wintypes.LONG),
        ("bmPlanes", ctypes.wintypes.WORD),
        ("bmBitsPixel", ctypes.wintypes.WORD),
        ("bmBits", ctypes.wintypes.LPVOID),
    ]

# Code created by chat-gpt


def screenshot():
    user32 = ctypes.windll.user32
    gdi32 = ctypes.windll.gdi32

    # Ekran boyutlarını al
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)

    # Ekran DC'sini al
    hdc_screen = user32.GetDC(0)
    hdc_mem = gdi32.CreateCompatibleDC(hdc_screen)
    hbitmap = gdi32.CreateCompatibleBitmap(hdc_screen, screen_width, screen_height)
    gdi32.SelectObject(hdc_mem, hbitmap)

    # Ekran görüntüsünü al
    gdi32.BitBlt(hdc_mem, 0, 0, screen_width, screen_height, hdc_screen, 0, 0, 0x00CC0020)

    # Bitmap verisini kaydet
    bmp_info = BITMAP()
    gdi32.GetObjectW(hbitmap, ctypes.sizeof(bmp_info), ctypes.byref(bmp_info))

    bmp_header = b"BM" + (14 + 40 + bmp_info.bmWidth * bmp_info.bmHeight * 4).to_bytes(4, "little")
    bmp_header += (0).to_bytes(4, "little")  # Reserved
    bmp_header += (14 + 40).to_bytes(4, "little")

    bmp_info_header = (40).to_bytes(4, "little")
    bmp_info_header += bmp_info.bmWidth.to_bytes(4, "little")
    bmp_info_header += (-bmp_info.bmHeight).to_bytes(4, "little", signed=True)
    bmp_info_header += (1).to_bytes(2, "little")  # Planes
    bmp_info_header += (32).to_bytes(2, "little")  # Bit count
    bmp_info_header += (0).to_bytes(4, "little")  # Compression
    bmp_info_header += (bmp_info.bmWidth * bmp_info.bmHeight * 4).to_bytes(4, "little")
    bmp_info_header += (2835).to_bytes(4, "little") * 2  # PPM X, Y
    bmp_info_header += (0).to_bytes(4, "little") * 2  # Color tables

    buffer_size = bmp_info.bmWidth * bmp_info.bmHeight * 4
    bmp_data = ctypes.create_string_buffer(buffer_size)
    gdi32.GetBitmapBits(hbitmap, buffer_size, bmp_data)

    with open(os.path.join(get_user_desktop(),f"screenshot_{CreateRandChar()}.bmp"), "wb") as f:
        f.write(bmp_header + bmp_info_header + bmp_data.raw)

    # Kaynakları temizle
    user32.ReleaseDC(0, hdc_screen)
    gdi32.DeleteDC(hdc_mem)
    gdi32.DeleteObject(hbitmap)

def Investigator(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            screenshot()
            MessageBox(title = "Hata ayıklandı",text=str(e),box = Dialogs.DIA_YES_NO | Icon.ICO_EXCLAMATION)
    return wrapper
