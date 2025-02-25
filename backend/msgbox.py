#!/usr/bin/env python3

# -*- encoding: utf-8 -*-

import ctypes

class Dialogs:
    DIA_OK = 0
    DIA_OK_CANCEL = 1
    DIA_ABORT_RETRY_IGNORE = 2
    DIA_YES_NO_CANCEL = 3
    DIA_YES_NO = 4
    DIA_RETRY_CANCEL = 5

class Icon:
    ICO_STOP = 16
    ICO_QUESTION = 32
    ICO_EXCLAMATION = 48
    ICO_INFO = 64

class Response:
    RESP_OK = 1
    RESP_CANCEL = 2
    RESP_ABORT = 3
    RESP_RETRY = 4
    RESP_IGNORE = 5
    RESP_YES = 6
    RESP_NO = 7



					    
class MessageBox:

    def __new__(
        cls,
        box = None,
        title = None,
        text = None,
        hwnd = None
    ) -> Response:
        cls.msgbox_dll_handler = ctypes.windll.user32.MessageBoxW
        cls.title = title
        cls.text = text
        cls.box = box
        return cls.msgbox_dll_handler(hwnd,cls.text,cls.title,cls.box)

