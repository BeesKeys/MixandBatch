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
        split = layout.split(factor=0.8)
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

        # Create a box for the warning message
        box = layout.box()
        box.label(text="BLENDER WILL FREEZE WHILE RENDERING, SAVE YOUR FILE FIRST, "
                       "THE ONLY WAY TO CANCEL THE RENDER IS TO FORCE CLOSE BLENDER")

        # Adding spacer to increase the height of the box
        box.prop(scene, "dummy_prop", text="", icon='NONE', emboss=False)  # Use an empty prop to create space

# Create a dummy property
def register():
    bpy.utils.register_class(RENDER_PT_BatchPanel)
    bpy.types.Scene.dummy_prop = bpy.props.StringProperty(name="Dummy Property")

def unregister():
    bpy.utils.unregister_class(RENDER_PT_BatchPanel)
    del bpy.types.Scene.dummy_prop

if __name__ == "__main__":
    register()
