import os
import platform

class env:
    if platform.system() == "Linux":
        home = os.environ["HOME"]
        root = "\\"
    
    elif platform.system() == "Windows":
        home = os.environ["USERPROFILE"]
        root = "C:\\"

class ext:
    if platform.system() == "Linux":
        executable = ["bin", "out", "run", ""]
        script = ["sh"]
    
    elif platform.system() == "Windows":
        executable = ["exe", "bin", "scr", "com"]
        script = ["bat", "cmd", "ps1"]