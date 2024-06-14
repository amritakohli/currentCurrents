#!/usr/bin/python3

import subprocess
import json
import time

def get_latest_version(package_name):
    try:
        version = "fail"
        result = subprocess.run(['lastversion', package_name], capture_output=True, text=True)
        if result.stdout:
            version = result.stdout.strip()
        return f"{package_name}: {version}"
    except subprocess.CalledProcessError as e:
        return f"{package_name}: error ({e})"
    except FileNotFoundError:
        return f"{package_name}: lastversion command not found"
    except Exception as e:
        return f"{package_name}: unknown error ({e})"

def process_packages(package_names, output_file):
    for name in package_names:
        result = get_latest_version(name)
        output_file.write(result + '\n')
        output_file.flush()  # Ensure the output is written to the file immediately

if __name__ == "__main__":
    # Record the start time
    start_time = time.time()

    filename = "./cgmanifest.json"

    # Load the JSON data from a file
    with open(filename, 'r') as file:
        data = json.load(file)

    # Extract package names
    package_names = [
        registration.get("component", {}).get("other", {}).get("name")
        for registration in data["Registrations"]
        if registration.get("component", {}).get("other", {}).get("name")
    ]

    # Open the output file in append mode
    with open('full.txt', 'a') as output_file:
        # Process all packages sequentially
        process_packages(package_names, output_file)

    # Record the end time
    end_time = time.time()

    # Calculate and print the elapsed time
    elapsed_time = end_time - start_time
    print(f"Total execution time: {elapsed_time} seconds")