#!/usr/bin/python3
def extract_package_names(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            package_name = line.split(' ', 1)[0]  # Get the word before the first space
            outfile.write(package_name + '\n')

if __name__ == "__main__":
    input_file = 'existcurrent.txt'   # Replace with your input file name
    output_file = 'packagesToAddress.txt'  # Replace with your desired output file name
    extract_package_names(input_file, output_file)
