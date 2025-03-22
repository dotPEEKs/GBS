import os
from backend.util import remove_dir
from backend.vars import Vars
from backend.util import get_user_desktop
desktop_shortcuts = [
    os.path.join(get_user_desktop(),path) + ".lnk" for path in ["main_window","db_main"]
]

if os.path.exists(Vars.target_dir):
    print("Cleaning dir")
    remove_dir(Vars.target_dir)

print("Cleaning shortcuts")

for shorcuts in desktop_shortcuts:
    if os.path.exists(shorcuts):
        os.remove(shorcuts)
        print("Cleaning shortcut: ",shorcuts)