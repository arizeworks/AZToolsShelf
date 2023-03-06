import bpy
import bmesh
import random
context = bpy.context


# 頂点ペイントモードへ
bpy.ops.object.mode_set(mode='VERTEX_PAINT')

bpy.context.object.data.use_paint_mask_vertex = True

bpy.ops.paint.vertex_color_smooth()

bpy.ops.object.mode_set(mode='EDIT')