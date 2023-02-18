
import bpy
context = bpy.context

def getSelectedObjects(context):
    return [o for o in context.selected_objects if o.type != 'MESH']


if len(getSelectedObjects(context)) > 0:
    for obj in getSelectedObjects(context):
        obj.select_set(False)

if len(getSelectedObjects(context)) == 0:
    bpy.ops.object.select_by_type(type='MESH')
