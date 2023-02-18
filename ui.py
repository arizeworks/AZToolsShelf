import bpy

from .UIs import ui_shelf


# Exec
class AZTOOLS_PT_Shelf_00(bpy.types.Panel):
    bl_label = "AZTools Shelf"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "AZTools"

    def draw(self, context):
        ui_shelf.AZToolsSHELF(self, context)

class AZTOOLS_PT_Shelf_01(bpy.types.Panel):
    bl_label = "AZTools Shelf"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"

    def draw(self, context):
        ui_shelf.AZToolsSHELF(self, context)

class AZTOOLS_PT_Shelf_02(bpy.types.Panel):
    bl_label = "AZTools Shelf"
    bl_space_type = "IMAGE_EDITOR"
    bl_region_type = "TOOLS"

    def draw(self, context):
        ui_shelf.AZToolsSHELF(self, context)


uiclasses = (
    AZTOOLS_PT_Shelf_00,
    # AZTOOLS_PT_Shelf_01,
    AZTOOLS_PT_Shelf_02,
)