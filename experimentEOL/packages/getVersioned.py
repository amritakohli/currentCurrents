def filter_non_critical_lines(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if "CRITICAL" not in line:
                # Extract the project name, which is the part before the ':'
                project_name = line.split(":")[0].strip()
                outfile.write(project_name + '\n')

if __name__ == "__main__":
    input_file = 'last_version_packages_5.txt'
    output_file = 'non_criticals_5.txt'
    filter_non_critical_lines(input_file, output_file)
    print(f"Lines not containing 'CRITICAL' have been written to {output_file}")
