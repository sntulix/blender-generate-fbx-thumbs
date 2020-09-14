import os
import sys
import glob
from mathutils import Vector

import bpy
from bpy.props import StringProperty, BoolProperty
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator

def clearMesh():
    for item in bpy.context.scene.objects:
        if item.type == 'MESH':
            bpy.context.scene.objects.unlink(item)
    for item in bpy.data.objects:
        if item.type == 'MESH':
            bpy.data.objects.remove(item)
    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)
    for item in bpy.data.materials:
        bpy.data.materials.remove(item)


def processFBX(fbxpath, sourcedir, outputdir_basename):
    print(fbxpath)
    fbx_basepath, fbx_filename = os.path.split(fbxpath)
    fbx_basename, fbx_ext = os.path.splitext(fbx_filename)

    clearMesh()

    if "bpy" in locals():
        import importlib
        if "import_fbx" in locals():
            importlib.reload(import_fbx)
    from . import import_fbx
    import_fbx.load(0,0, fbxpath)
    for item in bpy.context.scene.objects:
        if item.type == 'MESH':
            bpy.context.scene.objects.active = item
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            item.location = (0,0,0)

    scene = bpy.context.scene
    #cam = scene.camera
    #cam.location = (0.1, 0, 0)
    #cam.rotation_euler = (0, 0, 0)
    #empty = bpy.data.objects.new("Anchor", None)
    #mod = cam.constraints.new('TRACK_TO')
    #mod.target = empty
    #mod.up_axis = 'UP_Z'
    #mod.track_axis = 'TRACK_NEGATIVE_Y'
    scene.update()

    scene = bpy.context.scene
    scene.render.resolution_x = 512
    scene.render.resolution_y = 512
    scene.render.resolution_percentage = 100

    basedir, modulename = os.path.split(bpy.app.binary_path)
    ver = bpy.app.version_string[:4]
#    print(basedir)

    filepath = sourcedir + '/' + outputdir_basename + fbx_basename + '.png'
    print(filepath)
    bpy.ops.render.render()
    bpy.data.images['Render Result'].save_render(filepath)


class OT_FBXFolderOpenFilebrowser(Operator, ImportHelper):
    bl_idname = "fbxtool.open_filebrowser"
    bl_label = "Open the file browser (yay)"
    
    filter_glob: StringProperty(
        default='*.fbx',
        options={'HIDDEN'}
    )

    def execute(self, context):
        outputdir_basename = ""
        sourcedir = os.path.dirname(self.filepath)
        print('Selected Folder:', sourcedir)

#        if not os.path.exists(sourcedir + '/' + outputdir_basename):
#            sourcedir = argv[index:][0]
#            outputdir_basename = 'preview/'
#            os.mkdir(sourcedir + '/' + outputdir_basename)
        for fbxpath in glob.glob(sourcedir+'/*.fbx'):
            processFBX(fbxpath, sourcedir, outputdir_basename)

        clearMesh()

        return {'FINISHED'}
    
def register():
    bpy.utils.register_class(OT_FBXFolderOpenFilebrowser)
    
def unregister():
    bpy.utils.unregister_class(OT_FBXFolderOpenFilebrowser)
    

register()
bpy.ops.fbxtool.open_filebrowser('INVOKE_DEFAULT')
