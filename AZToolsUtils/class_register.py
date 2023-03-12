import bpy

REGIST_CLASSES = []

def registerClass():
    def decorator(cls):
        global REGIST_CLASSES
        if cls not in REGIST_CLASSES:
            REGIST_CLASSES += [cls]
        return cls
    return decorator