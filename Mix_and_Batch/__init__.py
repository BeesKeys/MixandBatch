bl_info = {
    "name": "Mix & Batch Addon",
    "blender": (2, 80, 0),
    "category": "Render",
    "description": "Batch render objects with different materials and cameras",
    "author": "Bees.Keys LTD",
    "version": (1, 1),
    "location": "View3D > N-panel > Mix & Batch",
}

import bpy
from .operators import (
    RENDER_OT_BatchRender, 
    RENDER_OT_AddObject, 
    RENDER_OT_RemoveObject, 
    RENDER_OT_AddMaterial, 
    RENDER_OT_RemoveMaterial, 
    RENDER_OT_AddCamera, 
    RENDER_OT_RemoveCamera, 
    RENDER_OT_AddCollection, 
    RENDER_OT_RemoveCollection
)
from .properties import (
    ObjectProperties, 
    MaterialProperties, 
    CameraProperties, 
    CollectionProperties, 
    RenderProperties
)
from .ui import (
    RENDER_PT_BatchPanel, 
    RENDER_UL_ObjectList, 
    RENDER_UL_MaterialList, 
    RENDER_UL_CameraList, 
    RENDER_UL_CollectionList
)

classes = (
    ObjectProperties,
    MaterialProperties,
    CameraProperties,
    CollectionProperties,
    RenderProperties,
    RENDER_OT_BatchRender,
    RENDER_PT_BatchPanel,
    RENDER_UL_ObjectList,
    RENDER_UL_MaterialList,
    RENDER_UL_CameraList,
    RENDER_UL_CollectionList,
    RENDER_OT_AddObject,
    RENDER_OT_RemoveObject,
    RENDER_OT_AddMaterial,
    RENDER_OT_RemoveMaterial,
    RENDER_OT_AddCamera,
    RENDER_OT_RemoveCamera,
    RENDER_OT_AddCollection,
    RENDER_OT_RemoveCollection,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.render_properties = bpy.props.PointerProperty(type=RenderProperties)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.render_properties

if __name__ == "__main__":
    register()
