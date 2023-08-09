import os

def merge_log_files0(log_directory0, output_file0):
    log_files = os.listdir(log_directory0)
    log_files = [os.path.join(log_directory0, file) for file in log_files if 'logfile' in file]
    log_files.sort()

    with open(output_file0, 'w') as merged_file:
        for i, file_path in enumerate(log_files):
            with open(file_path, 'r') as log_file:
                if i > 0:
                    # To skip the first 12 lines of each log file after the first one, because HemoCell writes excess data for the logfiles which isn't needed 
                    for _ in range(12):
                        next(log_file)
                merged_file.write(log_file.read())

    print(f"Log files merged into {output_file0}")

# defining the lo directories and output directory
log_directory0 = '/home/remi/irp/simulation_files/case_files/D31.5_0_4/output_0/log_test'
output_file0 = '/home/remi/irp/simulation_files/case_files/D31.5_0_4/output_0/log_test/D31.5_0_4.log'
merge_log_files0(log_directory0, output_file0)
