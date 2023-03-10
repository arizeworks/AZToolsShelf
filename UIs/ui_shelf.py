from ..Functions import func_name
from .. import data_path

import bpy
import os
import glob


SHELF_PATH = os.path.expandvars(bpy.utils.user_resource("SCRIPTS") + r"\addons\AZToolsShelf\Shelf")


def AZToolsShelf(self, context, mode=False):
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

    open_folder.path = SHELF_PATH
    self.execs = glob.glob(SHELF_PATH + r"\*.py")


    groups = ["None"]
    menus = []
    for exec in self.execs:
        exec_name = os.path.splitext(os.path.basename(exec))[0]
        exec_name_list = exec_name.split("_")

        if exec_name.startswith("shelf_") or exec_name.startswith("devshelf_"):

            # アンダーバー3つ以上の場合（グループモード）
            if len(exec_name_list) > 3:
                group_type = exec_name_list[1]
                menu_type = exec_name_list[2]
                button_name = exec_name_list[3]

            # アンダーバー2つの場合（レガシーモード）
            if len(exec_name_list) == 3:
                group_type = "None"
                menu_type = exec_name_list[1]
                button_name = exec_name_list[2]

            # メニュー描画
            if group_type not in groups:
                menus.append(group_type)

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

        exec_name_list = exec_name.split("_")
        # アンダーバー3つ以上の場合（グループモード）
        if len(exec_name_list) > 3:
            group_type = exec_name_list[1]
            exec_name = exec_name_list[2]
            button_name = exec_name_list[3]

        # アンダーバー2つの場合（レガシーモード）
        if len(exec_name_list) == 3:
            exec_name = exec_name_list[1]
            button_name = exec_name_list[2]

        if exec_name.startswith(menu_type):
            command = row.operator("object.aztools_shelf", text=func_name.camel_to_snake(button_name))

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
