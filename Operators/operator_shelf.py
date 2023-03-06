import bpy
import subprocess
from ..Functions import func_shelf
import os

shelf_path = os.path.expandvars(bpy.utils.user_resource('SCRIPTS') + r"\addons\AZToolsShelf\Shelf").replace("/", os.sep)
shelf_path = shelf_path.replace("\\", os.sep)

class AZTOOLS_OT_Shelf(bpy.types.Operator):
    bl_idname = "object.aztools_shelf"
    bl_label = "shelf"
    bl_options = {'REGISTER', 'UNDO'}

    path: bpy.props.StringProperty(default="")

    def execute(self, context):

        if "\\" in self.path or "/" in self.path:
            pass
        else:
            self.path = shelf_path + os.sep + self.path

        path = os.path.expandvars(self.path)
        path = path.replace("/", os.sep)
        path = path.replace("\\", os.sep)

        func_shelf.ExecFunc(path)

        return {'FINISHED'}


class AZTOOLS_OT_Open_Shelf_Folder(bpy.types.Operator):
    bl_idname = "object.aztools_shelf_folder"
    bl_label = "Open"
    bl_options = {'REGISTER', 'UNDO'}

    path: bpy.props.StringProperty(default="")

    def execute(self, context):

        if "\\" in self.path or "/" in self.path:
            pass
        else:
            self.path = shelf_path + os.sep + self.path

        path = os.path.expandvars(self.path)

        path = path.replace("/", os.sep)
        path = path.replace("\\", os.sep)

        subprocess.Popen(["explorer", path])

        return {'FINISHED'}


shelfclasses = (
    AZTOOLS_OT_Shelf,
    AZTOOLS_OT_Open_Shelf_Folder,
)
