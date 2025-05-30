import sys
import os
import const
import shutil
import const 
from platformdirs import user_data_dir

def get_user_save_dir():
    # name of the exe file, example: "Gambling_addiction"
    exe_name = os.path.splitext(os.path.basename(sys.executable))[0]
    VERSION = "0.11111"   # change this before making new .exe
    path = user_data_dir(exe_name, "YourName", version=VERSION)
    os.makedirs(path, exist_ok=True)
    return path

def extract_default_save():
    user_dir = get_user_save_dir()
    target = os.path.join(user_dir, "information.txt")
    if not os.path.exists(target):
        base = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))
        src = os.path.join(base, "save_files", "information.txt")
        shutil.copy(src, target)
    return target

def load_save_game_info(path, value):
    full_path = extract_default_save()
    money_value = 0
    with open(full_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith(f"{value}:"):
                money_value = int(line.split(":", 1)[1].strip())
                break
    return money_value

def update_value_in_file(path, key):
    full_path = extract_default_save()
    with open(full_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_value = getattr(const, key)
    for i, line in enumerate(lines):
        if line.startswith(f"{key}:"):
            lines[i] = f"{key}: {new_value}\n"
            break

    with open(full_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

def resource_path(relative_path):
    try:
        # If its .exe, sys._MEIPASS will exist
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)