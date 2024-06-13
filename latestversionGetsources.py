#!/usr/bin/python3
 
import subprocess
import json
import time
 
def get_latest_version(package_name):
    try:
        version = "fail"
        # Run the command "lastversion ansible"
        result = subprocess.run(['lastversion', package_name, "--source"], capture_output=True, text=True, check=False)
        # Print the output
        # print(result.stderr)
       
        if result.stdout != "":
            version = result.stdout.strip()
        if result.stderr != "":
            version = result.stderr.strip()
            return None
        # print(version)
        return f"{package_name}: {version}"
        # TODO: add to a file instead of print
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while fetching the latest version of {package_name}: {e}")
    except FileNotFoundError:
        print("The 'lastversion' command is not found. Make sure it is installed and available in your PATH.")
 
if __name__ == "__main__":
    # for everypackage in cgmanifest.json:
    # filename = "./cgmanifest.json"

    # Load the JSON data from a file
    # with open(filename, 'r') as file:
    #     data = json.load(file)
    start_time = time.time()

    input_file = "packagesToAddress.txt"
    output_file = "outputAddressedSources.txt"

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for name in infile:
            name = name.strip()
            result = get_latest_version(name)
            print(result)
            print('\n')
            print(time.time() - start_time)
            print('\n')
            if result is not None:
                outfile.write(result + '\n')
            outfile.flush() # write output to file immediately
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total exec time: {elapsed_time} seconds")

    # # Open the output file in append mode
    # with open('output.txt', 'a') as output_file:
    #     # Iterate through the registrations and write the package names to the output file
    #     for line in filename:
    #         component = registration.get("component", {})
    #         other = component.get("other", {})
    #         name = other.get("name")
    #         if name:
    #             # get_latest_version(name)
    #             # break
    #             output_file.write(get_latest_version(name) + '\n')
    #             # break
    

    #     # get_latest_version("ansible")