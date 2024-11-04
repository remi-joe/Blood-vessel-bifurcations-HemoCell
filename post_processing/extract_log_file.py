import re
import csv
import os

# Define the list of log file paths for each case
log_file_paths = [
    '/home/remi/irp/simulation_files/case_files/D31.5_0_0/output_0/log_test/D31.5_0_0.log',
    '/home/remi/irp/simulation_files/case_files/D31.5_0_1/output_0/log_test/D31.5_0_1.log',
    '/home/remi/irp/simulation_files/case_files/D31.5_0_2/output_0/log_test/D31.5_0_2.log',
    '/home/remi/irp/simulation_files/case_files/D31.5_0_3/output_0/log_test/D31.5_0_3.log',
    '/home/remi/irp/simulation_files/case_files/D31.5_0_4/output_0/log_test/D31.5_0_4.log',
]

# Define the output directory for CSV files
output_dir = "/home/remi/Desktop/post_processing_images/csv/"

# Define a regular expression pattern to match lines with statistics
stats_pattern = re.compile(r"Stats\. @ (\d+) \(([\d\.]+) s\):\n"
                           r"(?:\s*# of cells: (\d+) \| # of RBC: (\d+)\s+Velocity  -  max\.: ([\d\.]+) m/s, mean: ([\d\.]+) m/s, rel. app. viscosity: ([\d\.]+)\s+Force  -  min\.: ([\d\.]+) pN, max\.: ([\d\.]+) pN)+")

# Process data for each log file
for log_path in log_file_paths:
    # Extract the casename from the log file path
    casename = os.path.splitext(os.path.basename(log_path))[0]
    
    # Initialize a list to hold the extracted stats
    stats_list = []

    # Open the log file and read its content
    with open(log_path, "r") as log_file:
        log_content = log_file.read()

    # Find all matches of the stats pattern in the log content
    matches = stats_pattern.findall(log_content)

    # Iterate through the matches and append the data to the stats list
    for match in matches:
        timestep, time_seconds, num_cells, num_rbc, max_velocity, mean_velocity, rel_viscosity, min_force, max_force = match
        stats_list.append([timestep, time_seconds, num_cells, num_rbc, max_velocity, mean_velocity, rel_viscosity, min_force, max_force])

    # Write the stats to a CSV file
    csv_filename = os.path.join(output_dir, f"{casename}.csv")
    with open(csv_filename, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write header row
        csv_writer.writerow(["Timestep", "Time (s)", "Num Cells", "Num RBC", "Max Velocity (m/s)", "Mean Velocity (m/s)", "Relative Viscosity", "Min Force (pN)", "Max Force (pN)"])
        # Write stats data
        csv_writer.writerows(stats_list)

    print(f"Stats for '{casename}' have been extracted and saved to {csv_filename}")
