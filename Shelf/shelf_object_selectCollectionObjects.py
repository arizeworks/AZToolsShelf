import bpy

for obj in bpy.context.collection.all_objects:
    obj.select_set(True)