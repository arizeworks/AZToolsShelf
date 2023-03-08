import bpy

if "DataTransfer" not in bpy.context.object.modifiers:
    bpy.ops.object.modifier_add(type='DATA_TRANSFER')

bpy.context.object.modifiers["DataTransfer"].use_loop_data = True
bpy.context.object.modifiers["DataTransfer"].data_types_loops = {'CUSTOM_NORMAL'}
