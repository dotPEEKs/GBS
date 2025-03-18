import os
class Vars:
    target_dir = os.path.join(os.getenv("LocalAppData"),"gbs")
    json_path = os.path.join(os.getenv("LocalAppData"),"gbs","database.json")
    font_file_path = os.path.join(target_dir,"font.ttf")


