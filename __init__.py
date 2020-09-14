import os,sys
import bpy

dir = os.path.dirname(bpy.data.filepath)
os.chdir(dir)
if not dir in sys.path:
    sys.path.append(dir)
if "bpy" in locals():
    import importlib
    if "import_fbx" in locals():
        importlib.reload(import_fbx)

