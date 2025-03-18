import os
from backend.util import remove_dir
from backend.vars import Vars
from backend.util import get_user_desktop
desktop_shortcuts = [
    os.path.join(get_user_desktop(),path) + ".lnk" for path in ["main_window","db_main"]
]

remove_dir(Vars.target_dir)
print(desktop_shortcuts)
for shorcuts in desktop_shortcuts:
    os.remove(shorcuts)