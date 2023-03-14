import bpy
import os
from collections import defaultdict

import configparser

SHOW_CONSOLE = False

datapath = defaultdict(dict)
aztoolspath = defaultdict(dict)
myassets = defaultdict(dict)

button_group_type = defaultdict(dict)

# SYSTEM ##############################################################################################

datapath["system"]["os"] = os.__file__
datapath["system"]["home"] = os.path.expanduser("~")
datapath["system"]["pictures"] = datapath["system"]["home"] + "/Pictures"
datapath["system"]["temp"] = datapath["system"]["home"] + "/3D Objects/Temp/"


# Python ##############################################################################################

datapath["python"]["blender"] = '"' + os.path.abspath(datapath["system"]["os"] + "/../.." + "/bin/python.exe") + '"'
datapath["python"]["os"] = os.path.expandvars("%LOCALAPPDATA%/Programs/Python/Python310/pythonw.exe")

pathList = os.get_exec_path()
for path in pathList:
    if "Python" in path and "Scripts" not in path:
        datapath["python"]["os"] = path + "pythonw.exe"


# SOFTWARE ############################################################################################
# VSCode
datapath["editor"]["exe"] = os.path.expandvars("%LOCALAPPDATA%/Programs/Microsoft VS Code/Code.exe")

# Blender
datapath["blender"]["exe"] = bpy.app.binary_path
datapath["blender"]["addon"] = bpy.utils.user_resource("SCRIPTS") + "/addons"
datapath["blender"]["keyconfig"] = bpy.utils.user_resource('SCRIPTS') + "/presets/keyconfig"

# Assets
datapath["blender"]["myassets"] = datapath["system"]["home"] + "/GoogleDrive/MyAssets/AZAssets.blend"
datapath["blender"]["mymaterials"] = datapath["system"]["home"] + "/GoogleDrive/MyAssets/AZMat.blend"
datapath["blender"]["mycomp"] = datapath["system"]["home"] + "/GoogleDrive/MyAssets/AZComp.blend"
datapath["blender"]["exassets"] = datapath["system"]["home"] + "/GoogleDrive/ExternalAssets/"

# Maya
datapath["maya"]["bridge"] = datapath["system"]["home"] + "/3D Objects/MayaBridge/"
datapath["maya"]["dsw"] = datapath["system"]["home"] + "/3D Objects/MayaBridge/dsw/"

# Substance
datapath["sp"]["bridge"] = datapath["system"]["home"] + "/3D Objects/SubstanceBridge/"

# MoI
datapath["moi"]["bridge"] = os.path.expandvars("%APPDATA%/Moi/bridge/")

# ZBrush
datapath["zbrush"]["bridge"] = datapath["system"]["home"] + "/3D Objects/ZbrushBridge/"

# Houdini
datapath["houdini"]["bridge"] = datapath["system"]["home"] + "/3D Objects/Houdini/"
datapath["houdini"]["building"] = datapath["system"]["home"] + "/3D Objects/HoudiniBridge/Building/"

# Other
datapath["md"]["bridge"] = datapath["system"]["home"] + "/3D Objects/MDBridge/"
datapath["gaea"]["bridge"] = datapath["system"]["home"] + "/3D Objects/GaeaBridge/"
datapath["daz"]["bridge"] = datapath["system"]["home"] + "/3D Objects/DazBridge/"
datapath["3dcoat"]["bridge"] = datapath["system"]["home"] + "/3D Objects/3DCoatBridge/"

# Unity
datapath["unity"]["bridge"] = datapath["system"]["home"] + "/3D Objects/UnityBridge/"


# AZTOOLS ############################################################################################

aztoolspath["aztoolbox"]["dir"] = os.path.expandvars("%USERPROFILE%/GoogleDrive/MyPreferences/AZToolBox")
aztoolspath["blender"]["dir"] = datapath["blender"]["addon"] + "/AZTools"
aztoolspath["blenderdev"]["dir"] = datapath["blender"]["addon"] + "/AZToolsDev"
aztoolspath["blendergui"]["dir"] = datapath["blender"]["addon"] + "/AZToolsBlender"
aztoolspath["blendermirror"]["dir"] = datapath["blender"]["addon"] + "/AZToolsMirror"

datapath["Assets"]["Dir"] = os.path.abspath(os.path.expandvars(r"%HOMEDRIVE%%HOMEPATH%")) + r"\Documents\GoogleDrive\MyAssets"
datapath["Assets"]["Mat"] = datapath["Assets"]["Dir"] + r"\AZMat.blend"
datapath["Assets"]["Comp"] = datapath["Assets"]["Dir"] + r"\AZComp.blend"
datapath["Assets"]["Geo"] = datapath["Assets"]["Dir"] + r"\AZGeo.blend"


# LOAD ini ##########################################################################################
# def loadPath():
#     ini = configparser.ConfigParser()
#     try:
#         ini.read(os.path.expandvars("%APPDATA%/AZTools/data_path_global.ini"), "UTF-8")
#     except:
#         ini.read(os.path.expandvars("data_path_local.ini"), "UTF-8")

#     def lineEditLoadPath(iniKey, key1, key2):
#         # iniに値がある場合セット
#         try:
#             if len(ini["General"][iniKey]) > 0:
#                 datapath[key1][key2] = ini["General"][iniKey].replace("\\\\", "\\")
#         except:
#             pass

#         print("LOADED datapath['" + key1 + "']['" + key2 + "'] == " + datapath[key1][key2])

#     lineEditLoadPath("lineEdit_path_python_os", "python", "os")
#     lineEditLoadPath("lineEdit_path_python_venv", "python", "venv")
#     lineEditLoadPath("lineEdit_path_pyside2", "pyside2", "qtdesigner")
#     lineEditLoadPath("lineEdit_path_pyside6", "pyside6", "qtdesigner")

#     lineEditLoadPath("lineEdit_path_ahk", "ahk", "exe")
#     lineEditLoadPath("lineEdit_path_azt_bridge", "aztools", "bridge")
#     lineEditLoadPath("lineEdit_path_azt_icon", "icon", "dir")

#     lineEditLoadPath("lineEdit_path_editor", "editor", "exe")
#     lineEditLoadPath("lineEdit_path_photoshop", "photoshop", "exe")
#     lineEditLoadPath("lineEdit_path_illustrator", "illustrator", "exe")
#     lineEditLoadPath("lineEdit_path_csp", "csp", "exe")

#     lineEditLoadPath("lineEdit_path_blender", "blender", "exe")
#     lineEditLoadPath("lineEdit_path_maya", "maya", "exe")
#     lineEditLoadPath("lineEdit_path_sp", "sp", "exe")
#     lineEditLoadPath("lineEdit_path_moi", "moi", "exe")


# loadPath()


# SLASH CONVERTER ###################################################################################
def slashConverter(dict: dict):
    for i in dict:
        for j in dict[i]:
            dict[i][j] = dict[i][j].replace("/", os.sep)
            # dict[i][j] = dict[i][j].replace('\\', '/')
            if __name__ == "__main__":
                print(dict[i][j])


slashConverter(datapath)
slashConverter(aztoolspath)

# 最近開いたファイルパスを取得
# 初回起動時エラー発生

fp = bpy.utils.user_resource("CONFIG") + "/recent-files.txt"

recent_files = [""] * 10

try:
    with open(fp) as file:
        temp_files = file.read().splitlines()
except:
    temp_files = [""] * 10

for i in range(len(temp_files)):
    recent_files[i] = temp_files[i]


# import configparser
# ini設定
# config = configparser.ConfigParser()
# config.read(aztoolspath["blender"]["dir"] + "/data_env.ini")
# test_path = config["Path"]["maya_path"]
# print(test_path)

# try:
#     json_open = open(aztoolspath["blender"]["dir"] + "/data_env.json", "r")
#     json_load = json.load(json_open)
# except:
#     pass
