import bpy

REGIST_CLASSES = []


def registerClass():
    def decorator(cls):
        global REGIST_CLASSES
        if cls not in REGIST_CLASSES:
            REGIST_CLASSES += [cls]
        return cls

    return decorator


def register_idname():
    def decorator(cls):
        if "AZTOOLS_OT_" in cls.__name__:
            cls.bl_idname = cls.__name__.replace("AZTOOLS_OT_", "aztools.").lower()
        return cls

    return decorator


def title_except_uppercase(s):
    words = s.split(' ')
    for i, word in enumerate(words):
        if word in ["to", "of", "at", "in", "from", "not"]:
            pass
        elif len(word) == 2:
            words[i] = word.upper()
        elif not word.isupper():
            words[i] = word.capitalize()
    return ' '.join(words)


def register_label():
    def decorator(cls):
        if "AZTOOLS_OT_" in cls.__name__:
            bl_label = cls.__name__.replace("AZTOOLS_OT_", "").replace("_", " ")
            bl_label = title_except_uppercase(str(bl_label))
            cls.bl_label = bl_label

        if cls.__doc__ != None:
            cls.bl_description = "AZTools : " + cls.__doc__
        else:
            cls.bl_description = "AZTools : " + bl_label
        return cls

    return decorator


def register_undo():
    def decorator(cls):
        cls.bl_options = {"REGISTER", "UNDO"}
        return cls

    return decorator
