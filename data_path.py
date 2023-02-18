import bpy
import os
from collections import defaultdict


datapath = defaultdict(dict)
aztoolspath = defaultdict(dict)

# Blender
datapath["blender"]["exe"] = bpy.app.binary_path
datapath["blender"]["addon"] = bpy.utils.user_resource('SCRIPTS') + "\\addons"

# AZTools
aztoolspath["blender"]["dir"] = datapath["blender"]["addon"] + "\\AZToolsShelf"