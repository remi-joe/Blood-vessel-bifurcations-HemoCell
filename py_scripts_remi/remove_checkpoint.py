############### Created By: Remigius Joseph Selvaraj ####################
################### MSc. @ Cranfield University #########################
######################## DATE: 24/06/23 #################################
# This script is effectively a script to delete particular folders in the paths apecified 

import os

# List of folders to delete
folders = ['/work/e745/e745/remi23/HemoCell/examples/D31.5_0_0/checkpoint.xml', '/work/e745/e745/remi23/HemoCell/examples/D31.5_0_1/checkpoint.xml', '/work/e745/e745/remi23/HemoCell/examples/D31.5_0_2/checkpoint.xml', '/work/e745/e745/remi23/HemoCell/examples/D31.5_0_3/checkpoint.xml', '/work/e745/e745/remi23/HemoCell/examples/D31.5_0_4/checkpoint.xml', '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_0/checkpoint.xml', '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_1/checkpoint.xml', '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_2/checkpoint.xml', '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_3/checkpoint.xml', '/work/e745/e745/remi23/HemoCell/examples/D40.0_0_4/checkpoint.xml']

for folder in folders:
    # Check if the folder exists
    if os.path.exists(folder):
        # Delete the folder and its contents recursively
        os.system(f'rm -rf {folder}')
        print(f'Deleted folder: {folder}')
    else:
        print(f'Folder does not exist: {folder}')
