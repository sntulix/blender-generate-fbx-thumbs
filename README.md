# blender fbx thumbs generator
generate thumb images from fbx files in a folder.

## for 2.8x

Download Zip, Extract.
Open blender28_gen_thumb_fbx.blend, Press Alt + p.
In FileBrowser, Open a Folder of FBX Files, then Press "this folder" button.

![bl28_fbx_gen_thumb](https://user-images.githubusercontent.com/616940/93096805-c9ae3a80-f6df-11ea-97a0-8f1bff5a03b9.gif)

### In 2.8x, this script's UI Previews function is unimplemented.

## for 2.7x (command line)
Download Zip, Extract. from terminal or command prompt,
```
./blender gen_thumb_fbx.blend -- <fbx dir>
```

```
/Applications/blender/blender-2.76b-OSX_10.6-x86_64/blender.app/Contents/MacOS/blender ~/Dropbox/blender/blender-generate-fbx-thumbs/gen_thumb_fbx.blend -- /Users/xyz/Downloads/3dcg/cartoon_city_builder_pack/models
```

## note
based on FBX Importer (official), [UI Previews - Proposal](https://wiki.blender.org/index.php/User:Brita/Proposals/UIPreviews) (wiki.blender.org)

## sample image
![image](https://raw.github.com/wiki/sntulix/blender-generate-fbx-thumbs/images/blender-ui-preview-images.png)

# thanks
- https://sinestesia.co/blog/tutorials/using-blenders-filebrowser-with-python/
- https://blender.stackexchange.com/questions/124347/blender-2-8-python-code-to-switch-shading-mode-between-wireframe-and-solid-mo
- http://rikoubou.hatenablog.com/entry/2018/11/26/183709
- https://qiita.com/hibit/items/d6b92d49d4d3a5730aa4
