import os
import glob
import json
import subprocess
from backend.msgbox import *
from backend.util import get_resource_dir,remove_dir


def get_source(fname: str):
    return os.path.join("sources", fname)


def compile_with_nuitka(debug,**kwargs):
    if not os.path.exists("bin"):
        os.makedirs("bin")
    for key, value in kwargs.items():
        print("Compiling: {}".format(key))
        command = """nuitka --onefile  --product-version=1.0 --file-version=1.0 --product-name=G.B.S --file-description="Coded-By-dotPEEK" --quiet"""
        command += " --windows-icon-from-ico=%s" % (value["icon"]) if value.get("icon") else ""
        command += " --windows-console-mode=disable" if not value.get("dbg") and not value.get("dbg") else ""
        command += " --enable-plugin=pyside6" if value.get("pyside6") is not None and  value.get("pyside6") else ""
        if value.get("extra_files"):
            for file in value["extra_files"]:
                command += " --include-data-files=%s=%s " % (file["src"], file["dst"])
        command += " --no-progress-bar"
        command += " %s" % (key)
        command += " --output-dir=bin"
    if debug:
        return command
    subprocess.call(command.split(), shell=True)


def build_setup():
    import_data = """import glob\nimport backend\nfrom backend.backend import Vars\nfrom backend.util import *\n"""
    if not os.path.exists("workarea"):
        os.makedirs("workarea")
    extra_files_options = []
    for file in glob.glob("bin\\*.exe"):
        if os.path.basename(file) == "setup.exe":
            continue
        extra_files_options.append({"src": file, "dst": ".\\" + os.path.basename(file)})
    with open(get_source("demo_setup1.py"), "r") as setup_file:
        content = setup_file.read()
        with open("workarea\\setup.py", "w") as setup_file:
            content = import_data + "files = " + json.dumps(extra_files_options, indent=4) + "\n" + content
            setup_file.write(content)

    setup_file_options = {
        r"workarea\\setup.py":{
            "icon":get_resource_dir("db.ico"),
            "dbg":True,
            "extra_files":extra_files_options
        }
    }
    compile_with_nuitka(False,**setup_file_options)
    for files in os.listdir("bin"):
        fullpath = os.path.join("bin", files)
        if os.path.isdir(fullpath):
            remove_dir(fullpath)
        elif os.path.isfile(fullpath) and os.path.basename(fullpath) != "setup.exe":
            os.remove(fullpath)
    print("All done! now you can run setup.exe :) ")
files = {
    r"sources\db_main.py":{
        "icon":get_resource_dir("db.ico"),
        "dbg":False, # disables windows console mode
        "pyside6":True,
    }
}
def main():
    print("Cleaning up :)")
    remove_dir("workarea")
    remove_dir("bin")
    compile_with_nuitka(False, **files)
    build_setup()
if __name__ == "__main__":
    main()