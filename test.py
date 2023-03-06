import os

scripts_path = r"C:\Users\d3-hayama\AppData\Roaming"

print(scripts_path.replace(os.path.abspath(os.path.expandvars(r"%APPDATA%")), r"%APPDATA%"))