import sys
import os
import const
import shutil
import const 
from platformdirs import user_data_dir
import ast

def get_user_save_dir():
    # name of the exe file, example: "Gambling_addiction"
    exe_name = os.path.splitext(os.path.basename(sys.executable))[0]
    VERSION = "0.74"   # change this before making new .exe
    path = user_data_dir(exe_name, "YourName", version=VERSION)
    os.makedirs(path, exist_ok=True)
    return path

def extract_default_save():
    user_dir = get_user_save_dir()
    target = os.path.join(user_dir, "information.txt")
    if not os.path.exists(target):
        if hasattr(sys, "_MEIPASS"):
            base = sys._MEIPASS
        else:
            base = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        src = os.path.join(base, "save_files", "information.txt")
        if not os.path.isfile(src):
            os.makedirs(os.path.dirname(src), exist_ok=True)
            with open(src, "w", encoding="utf-8") as f:
                f.write("")  
        shutil.copy(src, target)
    return target

def load_save_game_info(path, value):
    full_path = extract_default_save()
    money_value = 0
    with open(full_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith(f"{value}:"):
                money_value = float(line.split(":", 1)[1].strip())
                break
    return round(money_value, 2)

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

def load_list_from_file(path, key):
    full_path = extract_default_save()
    with open(full_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith(f"{key}:"):
                value_str = line.split(":", 1)[1].strip()
                return ast.literal_eval(value_str)
    raise ValueError(f"Key '{key}' not found in file.")

def update_list_in_file(path, key, new_list):
    lines = []
    full_path = extract_default_save()
    key_found = False
    with open(full_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith(f"{key}:"):
                lines.append(f"{key}: {repr(new_list)}\n")
                key_found = True
            else:
                lines.append(line)
    if not key_found:
        lines.append(f"{key}: {repr(new_list)}\n")
    with open(full_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def resource_path(relative_path):
    try:
        # If its .exe, sys._MEIPASS will exist
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)