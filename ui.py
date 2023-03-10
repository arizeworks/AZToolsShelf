import bpy
from .class_register import registerClass
from .UIs import ui_shelf


# Exec
@registerClass()
class AZTOOLS_MT_Shelf_00(bpy.types.Menu):
    bl_label = "AZTools Shelf"
    bl_options = {"REGISTER"}

    def draw(self, context):
        ui_shelf.AZToolsShelf(self, context, True)


@registerClass()
class AZTOOLS_PT_Shelf_00(bpy.types.Panel):
    bl_label = "AZTools Shelf"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "AZTools"

    def draw(self, context):
        ui_shelf.AZToolsShelf(self, context, False)


@registerClass()
class AZTOOLS_PT_Shelf_01(bpy.types.Panel):
    bl_label = "AZTools Shelf"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"

    def draw(self, context):
        ui_shelf.AZToolsShelf(self, context, False)


@registerClass()
class AZTOOLS_PT_Shelf_02(bpy.types.Panel):
    bl_label = "AZTools Shelf"
    bl_space_type = "IMAGE_EDITOR"
    bl_region_type = "UI"
    bl_category = "AZTools"

    def draw(self, context):
        ui_shelf.AZToolsShelf(self, context, False)

@registerClass()
class AZTOOLS_PT_Shelf_03(bpy.types.Panel):
    bl_label = "AZTools Shelf"
    bl_space_type = "IMAGE_EDITOR"
    bl_region_type = "TOOLS"

    def draw(self, context):
        ui_shelf.AZToolsShelf(self, context, False)

@registerClass()
class AZTOOLS_PT_Shelf_04(bpy.types.Panel):
    bl_label = "AZTools Shelf"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"

    def draw(self, context):
        ui_shelf.AZToolsShelf(self, context, False)

@registerClass()
class AZTOOLS_PT_Shelf_05(bpy.types.Panel):
    bl_label = "AZTools Shelf"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "TOOLS"

    def draw(self, context):
        ui_shelf.AZToolsShelf(self, context, False)