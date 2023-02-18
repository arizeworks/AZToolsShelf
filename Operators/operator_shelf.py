import bpy
import subprocess
from ..Functions import func_shelf


class AZTOOLS_OT_Shelf(bpy.types.Operator):
    bl_idname = "object.aztools_shelf"
    bl_label = "shelf"
    bl_options = {'REGISTER', 'UNDO'}

    path: bpy.props.StringProperty(default="")

    def execute(self, context):

        func_shelf.ExecFunc(self.path)

        return {'FINISHED'}


class AZTOOLS_OT_Open_Shelf_Folder(bpy.types.Operator):
    bl_idname = "object.aztools_shelf_folder"
    bl_label = "Open"
    bl_options = {'REGISTER', 'UNDO'}

    path: bpy.props.StringProperty(default="")

    def execute(self, context):

        subprocess.Popen(["explorer", self.path])

        return {'FINISHED'}


shelfclasses = (
    AZTOOLS_OT_Shelf,
    AZTOOLS_OT_Open_Shelf_Folder,
)
