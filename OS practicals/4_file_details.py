import os
import stat
import sys
import datetime

def get_file_details(file_path):
    try:
        # Get file stat information
        file_stat = os.stat(file_path)

        # Extract file details
        file_size = file_stat.st_size
        access_time = datetime.datetime.fromtimestamp(file_stat.st_atime)
        owner = file_stat.st_uid
        permissions = stat.filemode(file_stat.st_mode)

        # Print file details
        print(f"File Details for: {file_path}")
        print(f"Size: {file_size} bytes")
        print(f"Owner: {owner}")
        print(f"Access Permissions: {permissions}")
        print(f"Access Time: {access_time}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Check if a file name is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python file_details.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    get_file_details(file_name)

if __name__ == "__main__":
    main()
