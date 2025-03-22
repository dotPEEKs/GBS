import os

from backend.msgbox import *
from backend.vars import Vars


def copy_exe_files():
    try:
        init()
        files = glob.glob(os.path.join(os.path.dirname(__file__),"*.exe"))
        for file in files:
            target_path = os.path.join(Vars.target_dir,os.path.basename(file))
            with open(file,"rb") as src:
                with open(target_path, "wb") as target:
                    target.write(src.read())
        exe_list_for_shortcuts = glob.glob(os.path.join(Vars.target_dir,"*.exe"))
        for exe_file in exe_list_for_shortcuts:
            CreateDesktopShortcuts(exe_file)
            print("Creating shortcut: %s" % (exe_file))
    except Exception as e:
       answser = MessageBox(
           title = "Hata ayıklama ",
           text = "Görünen o ki bir hata oluştu bunu kaydedip göndermemi ister misiniz ? (%s)" % (e),
           box = Dialogs.DIA_YES_NO | Icon.ICO_QUESTION
       )
       if answser == Response.RESP_YES:
           print("Hata bilgileri paketleniyor .....")

copy_exe_files()
print(os.listdir(os.getcwd()))
input()
