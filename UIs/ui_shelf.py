from ..Functions import func_name
from ..data_path import aztoolspath

import os
import glob


def AZToolsSHELF(self, context):

    layout = self.layout
    box = layout.box()
    box.label(text="Shelf Folder")
    row = box.row(align=True)
    row.scale_y = 1.5
    open_folder = row.operator("object.aztools_shelf_folder")
    open_folder.path = aztoolspath["blender"]["dir"] + "\\Shelf"

    self.execs = glob.glob(aztoolspath["blender"]["dir"] + "\\Shelf\\*")

    menus = []

    for exec in self.execs:
        exec_name = os.path.splitext(os.path.basename(exec))[0]

        if exec_name.startswith("shelf_"):
            exec_name_list = exec_name.split('_')
            if len(exec_name_list) >= 3:
                menu_type = exec_name_list[1]
                if menu_type not in menus:
                    if self.bl_space_type == "IMAGE_EDITOR":
                        if menu_type == "uv":
                            shelfMenu(self, menu_type)
                            menus.append(menu_type)
                        else:
                            pass
                    else:
                        if menu_type == "uv":
                            pass
                        else:
                            shelfMenu(self, menu_type)
                            menus.append(menu_type)

            else:
                print('Please review the naming convention. exp)"shelf_object_" :' + exec_name)
        else:
            print('Please Add Prefix. exp)"shelf_object_" :' + exec_name)



def shelfMenu(self, menu_type):
    layout = self.layout
    box = layout.box()
    box.label(text=func_name.camel_to_snake(menu_type))
    row = box.row(align=True)
    row.scale_y = 1.5

    exec_list = []
    i = 0
    for exec in self.execs:
        exec_name = os.path.splitext(os.path.basename(exec))[0]
        exec_name = exec_name.removeprefix("shelf_")

        if exec_name.startswith(menu_type + "_"):
            exec_name = exec_name.removeprefix(menu_type + "_")

            command = row.operator("object.aztools_shelf", text=func_name.camel_to_snake(exec_name))
            exec_list.append(command)
            exec_list[i].path = exec
            i += 1

            if not i % 2:
                row = box.row(align=True)
                row.scale_y = 1.5
