import textwrap

def readPython(path):
    with open(path) as reader:
        text = reader.read()
    return text


def ExecFunc(path):
    command = '''
    import bpy
    import bmesh
    context = bpy.context

    '''
    command = textwrap.dedent(command)

    command += readPython(path)
    command = textwrap.dedent(command)
    # print(command)
    try:
        exec(command)
        print("SHELF SUCCESS : " + path)
    except Exception as e:
        print("SHELF FAILED : " + path)
        print(e)