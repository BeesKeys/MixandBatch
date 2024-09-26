import bpy

class ObjectProperties(bpy.types.PropertyGroup):
    object: bpy.props.PointerProperty(type=bpy.types.Object)


class MaterialProperties(bpy.types.PropertyGroup):
    material: bpy.props.PointerProperty(type=bpy.types.Material)


class CameraProperties(bpy.types.PropertyGroup):
    camera: bpy.props.PointerProperty(type=bpy.types.Object, poll=lambda self, obj: obj.type == 'CAMERA')


class CollectionProperties(bpy.types.PropertyGroup):
    collection: bpy.props.PointerProperty(type=bpy.types.Collection)


class RenderProperties(bpy.types.PropertyGroup):
    output_dir: bpy.props.StringProperty(
        name="Output Directory",
        subtype='DIR_PATH',
        default=""
    )
    object_list: bpy.props.CollectionProperty(type=ObjectProperties)
    object_list_index: bpy.props.IntProperty()

    collection_list: bpy.props.CollectionProperty(type=CollectionProperties)
    collection_list_index: bpy.props.IntProperty()

    material_list: bpy.props.CollectionProperty(type=MaterialProperties)
    material_list_index: bpy.props.IntProperty()

    camera_list: bpy.props.CollectionProperty(type=CameraProperties)
    camera_list_index: bpy.props.IntProperty()
