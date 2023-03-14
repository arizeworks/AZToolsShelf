"""
Blender Script - Copy "Viewer Node" image to clipboard


- Windows only
- needs: Python module: Pillow (PIL)


ref:
    python - Copy PIL/PILLOW Image to Windows Clipboard - Stack Overflow
    http://stackoverflow.com/questions/21319486/copy-pil-pillow-image-to-windows-clipboard
"""


import bpy
import numpy as np
from PIL import Image

import array


def clipboard_copy_image(pimg):
    import io

    import ctypes

    msvcrt = ctypes.cdll.msvcrt
    kernel32 = ctypes.windll.kernel32
    user32 = ctypes.windll.user32

    output = io.BytesIO()
    pimg.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    CF_DIB = 8
    GMEM_MOVEABLE = 0x0002

    global_mem = kernel32.GlobalAlloc(GMEM_MOVEABLE, len(data))
    global_data = kernel32.GlobalLock(global_mem)
    msvcrt.memcpy(ctypes.c_char_p(global_data), data, len(data))
    kernel32.GlobalUnlock(global_mem)
    user32.OpenClipboard(None)
    user32.EmptyClipboard()
    user32.SetClipboardData(CF_DIB, global_mem)
    user32.CloseClipboard()


img0 = bpy.data.images["Render Result"]
W, H = img0.size

# px0 = img0.pixels[:]
px0 = [min(max(v, 0), 1) for v in img0.pixels]
pixels = np.array([int(v * 255) for v in px0])
pixels.resize(W, H * 4)
pixels = np.flipud(pixels).flatten()


ping = Image.frombytes("RGBA", (W, H), str(array.array("B", pixels)))
clipboard_copy_image(ping)

print("copied the image to clipboard")
