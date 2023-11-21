import bpy
from math import isclose

def delete_duplicate_objects():
    scene = bpy.context.scene
    objects = bpy.data.objects
    duplicate_meshes = {}
    
    # Iterate over all objects in the scene
    for obj in objects:
        if obj.type == 'MESH':
            mesh = obj.data
            mesh_key = get_mesh_key(mesh)
            
            # Check if a mesh with the same properties has been found before
            if duplicate_meshes.get(mesh_key):
                duplicate_meshes[mesh_key].append(obj)
            else:
                duplicate_meshes[mesh_key] = [obj]

    # Delete all duplicate objects except for the first instance
    for mesh_objs in duplicate_meshes.values():
        if len(mesh_objs) > 1:
            # Select all duplicate objects for deletion except the first one
            for obj in mesh_objs[1:]:
                obj.select_set(True)
            
    bpy.ops.object.delete()

def get_mesh_key(mesh):
    vertices = [tuple(v.co) for v in mesh.vertices]
    return tuple(vertices)

# Run the script
delete_duplicate_objects()
