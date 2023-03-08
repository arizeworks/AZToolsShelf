import bpy

from .UIs import ui_shelf


# Exec
class AZTOOLS_MT_Shelf_00(bpy.types.Menu):
    bl_label = "AZTools Shelf"
    bl_options = {'REGISTER'}

    def draw(self, context):
        ui_shelf.AZToolsSHELF(self, context, True)


class AZTOOLS_PT_Shelf_00(bpy.types.Panel):
    bl_label = "AZTools Shelf"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "AZTools"

    def draw(self, context):
        ui_shelf.AZToolsSHELF(self, context, False)

class AZTOOLS_PT_Shelf_01(bpy.types.Panel):
    bl_label = "AZTools Shelf"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"

    def draw(self, context):
        ui_shelf.AZToolsSHELF(self, context, False)

class AZTOOLS_PT_Shelf_02(bpy.types.Panel):
    bl_label = "AZTools Shelf"
    bl_space_type = "IMAGE_EDITOR"
    bl_region_type = "UI"
    bl_category = "AZTools"

    def draw(self, context):
        ui_shelf.AZToolsSHELF(self, context, False)

class AZTOOLS_PT_Shelf_03(bpy.types.Panel):
    bl_label = "AZTools Shelf"
    bl_space_type = "IMAGE_EDITOR"
    bl_region_type = "TOOLS"

    def draw(self, context):
        ui_shelf.AZToolsSHELF(self, context, False)

class AZTOOLS_PT_Shelf_04(bpy.types.Panel):
    bl_label = "AZTools Shelf"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"

    def draw(self, context):
        ui_shelf.AZToolsSHELF(self, context, False)

class AZTOOLS_PT_Shelf_05(bpy.types.Panel):
    bl_label = "AZTools Shelf"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "TOOLS"

    def draw(self, context):
        ui_shelf.AZToolsSHELF(self, context, False)


uiclasses = (
    AZTOOLS_MT_Shelf_00,
    AZTOOLS_PT_Shelf_00,
    AZTOOLS_PT_Shelf_01,
    AZTOOLS_PT_Shelf_02,
    AZTOOLS_PT_Shelf_03,
    AZTOOLS_PT_Shelf_04,
    AZTOOLS_PT_Shelf_05,
)