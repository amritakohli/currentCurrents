#!/usr/bin/python3

import subprocess
import json
from concurrent.futures import ProcessPoolExecutor, as_completed
import time
import os

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

def process_packages(package_names, output_file, max_workers=None):
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        future_to_name = {executor.submit(get_latest_version, name): name for name in package_names}
        for future in as_completed(future_to_name):
            try:
                result = future.result()
            except Exception as e:
                result = f"{future_to_name[future]}: error ({e})"
            output_file.write(result + '\n')
            output_file.flush()  # Ensure the output is written to the file immediately

def is_valid_package(registration):
    other = registration.get("component", {}).get("other", {})
    download_url = other.get("downloadUrl", "")
    return all([
        other.get("name"),
        "cblmarinerstorage.blob.core.windows.net" not in download_url,
        "files.pythonhosted.org" not in download_url,
        "github.com" not in download_url,
        "gitlab.com" not in download_url,
        "gitlab.freedesktop.org" not in download_url,
        "pypi.python.org" not in download_url,
        "pypi.io" not in download_url,
    ])

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
        if is_valid_package(registration)
    ]

    # Open the output file in append mode
    with open('last.txt', 'a') as output_file:
        # Determine the number of available CPU cores and set max_workers accordingly
        max_workers = 100
        #os.cpu_count()
        print(f"Max workers: {max_workers}")
        # Process all packages in one go
        process_packages(package_names, output_file, max_workers=max_workers)

    # Record the end time
    end_time = time.time()

    # Calculate and print the elapsed time
    elapsed_time = end_time - start_time
    print(f"Total execution time: {elapsed_time} seconds")