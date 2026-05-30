import sys
import os
from platformdirs import user_data_dir

def get_user_save_dir():
    # name of the exe file, example: "Gambling_addiction"
    exe_name = os.path.splitext(os.path.basename(sys.executable))[0]
    VERSION = "3.3"   # change this before making new .exe
    path = user_data_dir(exe_name, "YourName", version=VERSION)
    os.makedirs(path, exist_ok=True)
    return path

def resource_path(relative_path):
    try:
        # If its .exe, sys._MEIPASS will exist
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)