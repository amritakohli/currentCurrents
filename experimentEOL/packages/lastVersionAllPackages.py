import subprocess
import json
import time

def get_latest_version(package_name):
    try:
        version = "fail"
        result = subprocess.run(['lastversion', package_name], capture_output=True, text=True, check=False)

        if result.stdout:
            version = result.stdout.strip()
        if result.stderr:
            version = result.stderr.strip()
            print(f"Error: {result.stderr.strip()}")
        return f"{package_name}: {version}"
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while fetching the latest version of {package_name}: {e}")
        return f"An error occurred while fetching the latest version of {package_name}: {e}"
    except FileNotFoundError:
        print("The 'lastversion' command is not found. Make sure it is installed and available in your PATH.")

if __name__ == "__main__":
    start_time = time.time()

    # Comment: I run it 5 times for 5 files (which is 300 packages) 
    # because it takes a while if you run it for all 1500
    input_file = "packages_split_file_5.txt"
    output_file = "last_version_packages_5.txt"

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for name in infile:
            name = name.strip()
            result = get_latest_version(name)
            outfile.write(result + '\n')
            outfile.flush() 
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total exec time: {elapsed_time} seconds")