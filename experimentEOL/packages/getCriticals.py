def filter_critical_lines(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if "CRITICAL" in line:
                if "search query:" in line:
                    project_name = line.split("search query:")[1].strip()
                    outfile.write(project_name + '\n')
                else:
                    # Extract the project name, which is the part before the ':'
                    project_name = line.split("CRITICAL")[0].strip().rstrip(':')
                    outfile.write(project_name + '\n')

if __name__ == "__main__":
    input_file = 'last_version_packages_1.txt'
    output_file = 'criticals_1.txt'
    filter_critical_lines(input_file, output_file)
    print(f"Lines containing 'CRITICAL' have been written to {output_file}")
