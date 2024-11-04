import os

# List of folders to create the "output" folder in
folders = ['/work/e745/e745/remi23/HemoCell/examples/D31.5_0_0', '/work/e745/e745/remi23/HemoCell/examples/D31.5_0_1', '/work/e745/e745/remi23/HemoCell/examples/D31.5_0_2', '/work/e745/e745/remi23/HemoCell/examples/D31.5_0_3', '/work/e745/e745/remi23/HemoCell/examples/D31.5_0_4', '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_0', '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_1', '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_2', '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_3', '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_4']

for folder in folders:
    # Create the "output" folder inside the current folder
    output_folder = os.path.join(folder, 'output')
    
    # Check if the "output" folder already exists
    if os.path.exists(output_folder):
        print(f'Output folder already exists in {folder}')
    else:
        try:
            # Create the "output" folder
            os.makedirs(output_folder)
            print(f'Created output folder in {folder}')
        except OSError as e:
            print(f'Failed to create output folder in {folder}: {e}')

