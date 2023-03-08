from ..Functions import func_name
from ..data_path import aztoolspath

import bpy
import os
import glob

import os
import bpy


def AZToolsSHELF(self, context, mode=False):

    # Menuモード
    if mode:
        layout = self.layout
        row = layout.row()
        row.label(text="Shelf Folder")
        row = layout.row(align=True)
        row.scale_y = 1.5
        layout.separator()

    # Panelモード
    else:
        layout = self.layout
        box = layout.box()
        box.label(text="Shelf Folder")
        row = box.row(align=True)
        row.scale_y = 1.5

    open_folder = row.operator("object.aztools_shelf_folder")

    shelf_path = os.path.expandvars(bpy.utils.user_resource('SCRIPTS') + r"\addons\AZToolsShelf\Shelf")
    open_folder.path = shelf_path
    self.execs = glob.glob(shelf_path + r"\*.py")

    menus = []

    for exec in self.execs:
        exec_name = os.path.splitext(os.path.basename(exec))[0]
        exec_name_list = exec_name.split('_')

        if exec_name.startswith("shelf_") or exec_name.startswith("devshelf_"):

            # アンダーバー2つの場合
            if len(exec_name_list) == 3:
                menu_type = exec_name_list[1]
                if menu_type not in menus:

                    # Menuモード
                    if mode:
                        shelfMenu(self, menu_type, mode)
                        menus.append(menu_type)

                    # Panelモード
                    else:
                        if self.bl_space_type == "IMAGE_EDITOR":
                            if menu_type in ["uv", "image"]:
                                shelfMenu(self, menu_type, mode)
                                menus.append(menu_type)
                            else:
                                pass
                        else:
                            if menu_type == ["uv", "image"]:
                                pass
                            else:
                                shelfMenu(self, menu_type, mode)
                                menus.append(menu_type)

            # # アンダーバー3つ以上の場合
            # elif len(exec_name_list) > 3:
            #     group_type = exec_name_list[1]
            #     menu_type = exec_name_list[2]

            else:
                print('Please review the naming convention. exp)"shelf_object_" :' + exec_name)
        else:
            print('Please Add Prefix. exp)"shelf_object_" :' + exec_name)



def shelfMenu(self, menu_type, mode=False):

    # Menuモード
    if mode:
        layout = self.layout
        layout.label(text=func_name.camel_to_snake(menu_type))
        row = layout.row(align=True)
        row.scale_y = 1.5

    # Panel モード
    else:
        layout = self.layout
        box = layout.box()
        box.label(text=func_name.camel_to_snake(menu_type))
        row = box.row(align=True)
        row.scale_y = 1.5



    exec_list = []
    i = 0
    for exec in self.execs:
        exec_name = os.path.splitext(os.path.basename(exec))[0]

        if exec_name.startswith("devshelf_"):
            row.alert = True
        else:
            row.alert = False

        exec_name = exec_name.removeprefix("shelf_")
        exec_name = exec_name.removeprefix("devshelf_")

        if exec_name.startswith(menu_type + "_"):
            exec_name = exec_name.removeprefix(menu_type + "_")

            command = row.operator("object.aztools_shelf", text=func_name.camel_to_snake(exec_name))

            exec_list.append(command)
            exec_list[i].path = os.path.basename(exec)
            i += 1

            if mode:
                if not i % 4:
                    layout.separator()
                    row = layout.row(align=True)
            else:
                if not i % 2:
                    row = box.row(align=True)
            row.scale_y = 1.5

    if mode:
        layout.separator()