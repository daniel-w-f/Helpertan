import os
import re

directory = "dir"  # Replace with the actual directory path

# Regular expression pattern to match the original file names
pattern = r"(rob) \((\d+)\)(\..*)"

# Function to rename the files
def rename_files():
    counter = 1
    for filename in os.listdir(directory):
        match = re.search(pattern, filename)
        if match:
            file_name_prefix = match.group(1)
            file_extension = match.group(3)
            # new pattern
            new_filename = file_name_prefix + "_" + str(counter) + file_extension
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            counter += 1

# Execute the rename_files function
rename_files()
