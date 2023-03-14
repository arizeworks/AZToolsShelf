import sys

sys.dont_write_bytecode = True
from .AZToolsUtils.class_register import REGIST_CLASSES
import bpy
import importlib

bl_info = {
    "name": "AZTools Shelf",
    "version": (1, 0),
    "blender": (3, 4, 1),
    "author": "Arizeworks",
    "location": "3D View > N-Panel / T-Panel > AZTools Shelf",
    # "warning": "Warning: this addon is still developping",
    "description": "AZTools",
    "category": "AZTools",
    "url": "https://github.com/arizeworks/",
}

# Path
from .AZToolsUtils import data_path
from .Operators import operator_shelf
from .UIs import ui_shelf
from . import ui

import_libs = [
    data_path,
    operator_shelf,
    ui_shelf,
    ui,
]

for lib in import_libs:
    importlib.reload(lib)

def register():
    for cls in REGIST_CLASSES:
        bpy.utils.register_class(cls)


def unregister():
    for cls in REGIST_CLASSES:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
