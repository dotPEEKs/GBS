import os
import shutil
from backend.investigator import screenshot
from backend.msgbox import *
from backend.vars import Vars

def copy_exe_files():
    try:
        init()
        files = glob.glob(os.path.join(os.path.dirname(__file__),"*.exe"))
        for source_path in files:
            if not file != "setup.exe"
                target_path = os.path.join(Vars.target_dir,os.path.basename(file))
                shutil.copy(source_path,target_path)
        exe_list_for_shortcuts = glob.glob(os.path.join(Vars.target_dir,"*.exe"))
        for exe_file in exe_list_for_shortcuts:
            CreateDesktopShortcuts(exe_file)
            print("Creating shortcut: %s" % (exe_file))
    except Exception as e:
       screenshot()
       answser = MessageBox(
           title = "Hata ayıklama ",
           text = "Görünen o ki bir hata oluştu bunu kaydedip göndermemi ister misiniz ? (%s)" % (e),
           box = Dialogs.DIA_YES_NO | Icon.ICO_QUESTION
       )

copy_exe_files()

input()
