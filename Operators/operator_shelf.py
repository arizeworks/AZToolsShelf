import bpy
import subprocess
from ..AZToolsUtils.class_register import registerClass
from ..Functions import func_shelf
import os

from ..AZToolsUtils.data_path import button_group_type

shelf_path = os.path.expandvars(bpy.utils.user_resource('SCRIPTS') + r"\addons\AZToolsShelf\Shelf").replace("/", os.sep)
shelf_path = shelf_path.replace("\\", os.sep)


@registerClass()
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

@registerClass()
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

@registerClass()
class AZTOOLS_OT_Shelf_Group(bpy.types.Operator):
    bl_idname = "object.aztools_shelf_group"
    bl_label = "Group"
    bl_options = {'REGISTER', 'UNDO'}

    group_type: bpy.props.StringProperty(default="")

    def execute(self, context):
        for item in button_group_type.items():
            item = False
        button_group_type[self.group_type] = True


        return {'FINISHED'}
