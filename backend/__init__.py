import os
import sys

from reportlab.lib.pagesizes import elevenSeventeen

from .vars import Vars
from .util import get_resource_dir
class InvalidDbObject(Exception):
    pass

def extract_class_members(obj) -> str:
    string = ""
    class_members = [member for member in dir(obj) if not member.startswith("_")]
    for member in class_members:
        string+="\t%s = %s\n" % (member,getattr(obj,member))
    return string
class Repr:
    def __repr__(self,obj = None,get_class_name = False):
        extract_to_class = self if obj is None else obj
        class_name = extract_to_class.__class__.__name__ + " => "
        if get_class_name:
            return class_name
        repr_str = "<%s " % (class_name) + "\n" + extract_class_members(extract_to_class) + ">"
        return repr_str

def check_font_file(path):
    font_src_path = get_resource_dir("font.ttf")
    if getattr(sys,"frozen",False): # if program running in exe mode
        font_src_path = os.path.join(os.path.dirname(path),"font.ttf")
    with open(font_src_path,"rb") as src:
        with open(Vars.font_file_path,"wb") as dst:
            dst.write(src.read())