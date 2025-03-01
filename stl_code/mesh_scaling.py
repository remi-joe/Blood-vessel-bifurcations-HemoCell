import trimesh

input_dir = "/home/remi/irp/stl_files/"
mesh = trimesh.load_mesh(input_dir + "mesh_0.93_0.58.stl")

# Define the movement offsets in millimeters
mov_x_mm = 11.20453446758326
mov_y_mm = 2.1275

# Convert millimeters to meters
mov_x = mov_x_mm # Convert to meters
mov_y = 2*mov_y_mm  # Convert to meters

# Apply the translation (movement) to the mesh vertices
translated_mesh = mesh.copy()
translated_mesh.apply_translation([mov_x, mov_y, 0])

# Define the scaling factor in micrometers
scaling_factor_um = 32e-6  # 31.5 micrometers in meters

# Scale the translated mesh vertices
scaled_mesh = translated_mesh.copy()
scaled_mesh.apply_scale(scaling_factor_um)

# Save the scaled and translated mesh to a new STL file

scaled_mesh.export(input_dir + "scaled_case0.stl")
