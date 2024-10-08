import bpy
import os
import itertools
import threading

def save_image_in_thread(image_buffer, output_file):
    """ Save image in a separate thread to avoid blocking Blender """
    print(f"Saving image to {output_file}")
    image_buffer.filepath_raw = output_file
    image_buffer.file_format = 'PNG'
    image_buffer.save()
    bpy.data.images.remove(image_buffer)  # Remove buffer after saving
    print(f"Finished saving image to {output_file}")

class RENDER_OT_BatchRender(bpy.types.Operator):
    bl_idname = "render.batch_render"
    bl_label = "Batch Render"

    def execute(self, context):
        print("Batch render started.")
        scene = context.scene
        render_props = scene.render_properties
        output_dir = render_props.output_dir

        if not os.path.exists(output_dir):
            print(f"Creating output directory: {output_dir}")
            os.makedirs(output_dir)

        objects = [item.object for item in render_props.object_list]
        collections = [item.collection for item in render_props.collection_list]
        materials = [item.material for item in render_props.material_list]
        cameras = [item.camera for item in render_props.camera_list]
        all_objects = objects + [coll for coll in collections if coll is not None]

        if not all_objects:
            self.report({'WARNING'}, "No objects or collections selected!")
            return {'CANCELLED'}

        material_combinations = list(itertools.product(materials, repeat=len(all_objects)))
        print(f"Material combinations: {len(material_combinations)}")
        render_counter = 1
        threads = []  # Track threads

        for cam in cameras:
            if cam is None:
                self.report({'WARNING'}, "Camera not found!")
                continue

            print(f"Using camera: {cam.name}")
            bpy.context.scene.camera = cam
            camera_name = cam.name

            for combination in material_combinations:
                print(f"Rendering combination {render_counter}...")
                item_material_pairs = []

                for item, material in zip(all_objects, combination):
                    if item is None or material is None:
                        print("Warning: Item or material is None.")
                        continue

                    if isinstance(item, bpy.types.Collection):
                        for obj in item.objects:
                            if obj.type == 'MESH':
                                if obj.data.materials:
                                    obj.data.materials[0] = material
                                else:
                                    obj.data.materials.append(material)
                        item_material_pairs.append(f"{item.name}-{material.name}")
                    else:
                        if item.data.materials:
                            item.data.materials[0] = material
                        else:
                            item.data.materials.append(material)
                        item_material_pairs.append(f"{item.name}-{material.name}")

                materials_str = "_".join(item_material_pairs)
                image_name = f"Render_{camera_name}_{materials_str}_{render_counter}"

                # Set render output to a buffer
                bpy.context.scene.render.filepath = "//" + image_name  # Dummy path
                print(f"Rendering image: {image_name}")
                bpy.ops.render.render(write_still=False)
                print("Render complete.")

                # Get rendered image buffer
                image_buffer = bpy.data.images['Render Result'].copy()
                print("Image buffer copied.")

                # Define actual file path for saving
                output_file = os.path.join(output_dir, f"{camera_name}_{materials_str}.png")

                # Save image in a separate thread
                thread = threading.Thread(target=save_image_in_thread, args=(image_buffer, output_file))
                threads.append(thread)
                thread.start()
                print(f"Started thread for saving image: {output_file}")

                render_counter += 1

        # Ensure all threads complete
        for thread in threads:
            thread.join()
            print("Thread finished.")

        print("Batch rendering complete.")
        self.report({'INFO'}, "Rendering complete!")
        return {'FINISHED'}



class RENDER_OT_AddObject(bpy.types.Operator):
    bl_idname = "render.add_object"
    bl_label = "Add Object"

    def execute(self, context):
        context.scene.render_properties.object_list.add()
        return {'FINISHED'}


class RENDER_OT_RemoveObject(bpy.types.Operator):
    bl_idname = "render.remove_object"
    bl_label = "Remove Object"

    def execute(self, context):
        render_props = context.scene.render_properties
        render_props.object_list.remove(render_props.object_list_index)
        render_props.object_list_index = max(0, render_props.object_list_index - 1)
        return {'FINISHED'}


class RENDER_OT_AddMaterial(bpy.types.Operator):
    bl_idname = "render.add_material"
    bl_label = "Add Material"

    def execute(self, context):
        context.scene.render_properties.material_list.add()
        return {'FINISHED'}


class RENDER_OT_RemoveMaterial(bpy.types.Operator):
    bl_idname = "render.remove_material"
    bl_label = "Remove Material"

    def execute(self, context):
        render_props = context.scene.render_properties
        render_props.material_list.remove(render_props.material_list_index)
        render_props.material_list_index = max(0, render_props.material_list_index - 1)
        return {'FINISHED'}


class RENDER_OT_AddCamera(bpy.types.Operator):
    bl_idname = "render.add_camera"
    bl_label = "Add Camera"

    def execute(self, context):
        context.scene.render_properties.camera_list.add()
        return {'FINISHED'}


class RENDER_OT_RemoveCamera(bpy.types.Operator):
    bl_idname = "render.remove_camera"
    bl_label = "Remove Camera"

    def execute(self, context):
        render_props = context.scene.render_properties
        render_props.camera_list.remove(render_props.camera_list_index)
        render_props.camera_list_index = max(0, render_props.camera_list_index - 1)
        return {'FINISHED'}


class RENDER_OT_AddCollection(bpy.types.Operator):
    bl_idname = "render.add_collection"
    bl_label = "Add Collection"

    def execute(self, context):
        context.scene.render_properties.collection_list.add()
        return {'FINISHED'}


class RENDER_OT_RemoveCollection(bpy.types.Operator):
    bl_idname = "render.remove_collection"
    bl_label = "Remove Collection"

    def execute(self, context):
        render_props = context.scene.render_properties
        render_props.collection_list.remove(render_props.collection_list_index)
        render_props.collection_list_index = max(0, render_props.collection_list_index - 1)
        return {'FINISHED'}
