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
from . import data_path
importlib.reload(data_path)


# Operators
from . import operator
importlib.reload(operator)

from .Operators import operator_shelf
importlib.reload(operator_shelf)

# UIs
from . import ui
importlib.reload(ui)

from .UIs import ui_shelf
importlib.reload(ui_shelf)


regist_classes = operator.operatorclasses + ui.uiclasses

def register():
    for regist_cls in regist_classes:
        bpy.utils.register_class(regist_cls)

def unregister():
    for regist_cls in regist_classes:
        bpy.utils.unregister_class(regist_cls)


if __name__ == "__main__":
    register()