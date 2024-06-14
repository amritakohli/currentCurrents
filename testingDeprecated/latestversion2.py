#!/usr/bin/python3

import subprocess
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_latest_version(package_name):
    try:
        version = "fail"
        # Run the command "lastversion ansible"
        result = subprocess.run(['lastversion', package_name], capture_output=True, text=True, check=False)
        # Print the output
        # print(result.stderr)
       
        if result.stdout:
            version = result.stdout.strip()

        return f"{package_name}: {version}"
    except subprocess.CalledProcessError as e:
        return f"{package_name}: error ({e})"
    except FileNotFoundError:
        return f"{package_name}: lastversion command not found"

def process_packages(package_names, output_file):
    with ThreadPoolExecutor(max_workers=50) as executor:
        future_to_name = {executor.submit(get_latest_version, name): name for name in package_names}
        for future in as_completed(future_to_name):
            result = future.result()
            output_file.write(result + '\n')

if __name__ == "__main__":
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
    with open('second.txt', 'a') as output_file:
        # Process packages in chunks of 50
        for i in range(0, len(package_names), 50):
            chunk = package_names[i:i + 50]
            process_packages(chunk, output_file)
