import shutil
import sys

def copy_file(source_path, destination_path):
    try:
        shutil.copy(source_path, destination_path)
        print(f"File copied successfully from {source_path} to {destination_path}.")
    except FileNotFoundError:
        print("Source file not found.")
        sys.exit(1) # Exit with error status
    except PermissionError:
        print("Permission error. Make sure you have the necessary permissions.")
        sys.exit(1) # Exit with error status
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1) # Exit with error status

if __name__ == "__main__":
    source_file = "path/to/source/file.txt" # Replace with the actual source file path
    destination_file = "path/to/destination/file.txt" # Replace with the actual destination file path

    copy_file(source_file, destination_file)