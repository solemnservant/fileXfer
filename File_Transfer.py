from pathlib import Path
import shutil

# Define the file you want to copy
file_to_copy = Path("/mnt/mastiff/SUMMIT/Production/DO2/DGED5_DSM/50TN/Templates/Step_7_Hydro/heights/Step_10_RiverHeightUpdate_vs_928.xml")

# Define the base directory and the pattern for directories to search
base_directory = Path("/mnt/mastiff/SUMMIT/Production/DO2/DGED5_DSM")
directory_pattern = "*/heights"

# Use rglob to find matching directories
matching_directories = base_directory.rglob(directory_pattern)

# Loop through each matching directory and copy the file
for directory in matching_directories:
    if directory.is_dir():
        destination = directory / file_to_copy.name
        shutil.copy(file_to_copy, destination)
        print(f"Copied {file_to_copy} to {destination}")
    else:
        print(f"Skipping non-directory path: {directory}")
