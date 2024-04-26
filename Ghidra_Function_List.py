"""
Function Listing Script for Linux:
Iterates through all the functions in the loaded binary
and prints out their names and entry points.
All data is saved in Function_List.txt
"""

# Import necessary Ghidra classes
from java.io import FileWriter
from ghidra.program.model.listing import FunctionManager
from ghidra.util.task import ConsoleTaskMonitor
import os

# Access function manager of current program loaded
function_manager = currentProgram.getFunctionManager()
functions = function_manager.getFunctions(True)  # True condition to iterate forward

# Get the current user's home directory
home_dir = os.path.expanduser("~")

# Specifying the output file path
file_path = os.path.join(home_dir, "Function_List.txt")
file_writer = FileWriter(file_path)

try:
    # Retrieve the binary name and file path
    binary_name = currentProgram.getDomainFile().getName()
    binary_path = currentProgram.getExecutablePath()

    # Write the binary name and file path to the file
    file_writer.write("Binary Name: {}\n".format(binary_name))
    file_writer.write("Binary Path: {}\n".format(binary_path))
    file_writer.write("\n")  # Add an empty line for visuals

    # Write the header to the file
    file_writer.write("{:<40} {:<20}\n".format("Function Name", "Entry Point"))
    file_writer.write("-" * 60 + "\n")  # Divider for visuals

    # Iterate over all functions and write their names and entry points to the file
    for function in functions:
        name = function.getName()
        entry_point = function.getEntryPoint()
        # Formatting each line for column alignment
        file_writer.write("{:<40} {:<20}\n".format(name, str(entry_point)))
finally:
    # Close the file writer
    file_writer.close()

# Print the location of the output file to the Ghidra console
print("Function list written to {}".format(file_path))
