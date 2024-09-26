import bpy

class RENDER_PT_BatchPanel(bpy.types.Panel):
    bl_label = "Mix & Batch"
    bl_idname = "RENDER_PT_batch_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Mix & Batch'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        render_props = scene.render_properties

        layout.prop(render_props, "output_dir")

        # Objects Section
        layout.label(text="Objects")
        split = layout.split(factor=0.8)  # Adjust the factor to control the width of the list vs the button column
        col_left = split.column()
        col_right = split.column()

        col_left.template_list("RENDER_UL_ObjectList", "", render_props, "object_list", render_props, "object_list_index")
        col_right.operator("render.add_object", icon='ADD', text="")
        col_right.operator("render.remove_object", icon='REMOVE', text="")

        # Collections Section
        layout.label(text="Collections")
        split = layout.split(factor=0.8)
        col_left = split.column()
        col_right = split.column()

        col_left.template_list("RENDER_UL_CollectionList", "", render_props, "collection_list", render_props, "collection_list_index")
        col_right.operator("render.add_collection", icon='ADD', text="")
        col_right.operator("render.remove_collection", icon='REMOVE', text="")

        # Materials Section
        layout.label(text="Materials")
        split = layout.split(factor=0.8)
        col_left = split.column()
        col_right = split.column()

        col_left.template_list("RENDER_UL_MaterialList", "", render_props, "material_list", render_props, "material_list_index")
        col_right.operator("render.add_material", icon='ADD', text="")
        col_right.operator("render.remove_material", icon='REMOVE', text="")

        # Cameras Section
        layout.label(text="Cameras")
        split = layout.split(factor=0.8)
        col_left = split.column()
        col_right = split.column()

        col_left.template_list("RENDER_UL_CameraList", "", render_props, "camera_list", render_props, "camera_list_index")
        col_right.operator("render.add_camera", icon='ADD', text="")
        col_right.operator("render.remove_camera", icon='REMOVE', text="")

        # Render Button
        layout.operator("render.batch_render")


class RENDER_UL_ObjectList(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.prop(item, "object", text="")


class RENDER_UL_MaterialList(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.prop(item, "material", text="")


class RENDER_UL_CameraList(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.prop(item, "camera", text="")


class RENDER_UL_CollectionList(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.prop(item, "collection", text="")
