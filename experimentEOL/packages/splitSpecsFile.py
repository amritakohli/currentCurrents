def split_file(input_file, lines_per_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        
    total_lines = len(lines)
    num_files = total_lines // lines_per_file + (1 if total_lines % lines_per_file else 0)
    
    for i in range(num_files):
        start = i * lines_per_file
        end = start + lines_per_file
        output_file = f"packages_split_file_{i+1}.txt"
        with open(output_file, 'w') as output:
            output.writelines(lines[start:end])

if __name__ == "__main__":
    input_file = 'specs.txt'
    lines_per_file = 300
    split_file(input_file, lines_per_file)
