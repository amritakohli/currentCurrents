#!/usr/bin/python3
 
import subprocess
 
def get_latest_version(package_name):
    try:
        # Run the command "lastversion ansible"
        result = subprocess.run(['lastversion', package_name], capture_output=True, text=True, check=True)
        # Print the output
        print(f"{package_name}: {result.stdout.strip()}")
        # TODO: add to a file instead of print
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while fetching the latest version of {package_name}: {e}")
    except FileNotFoundError:
        print("The 'lastversion' command is not found. Make sure it is installed and available in your PATH.")
 
if __name__ == "__main__":
    # for everypackage in cgmanifest.json:
    get_latest_version("ansible")