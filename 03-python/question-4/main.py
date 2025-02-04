# Sort Text File Content 
def sort_file_contents(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    sorted_lines = [line.strip() for line in lines]
    sorted_lines.sort()
    
    with open(output_file, 'w') as file:
        for line in sorted_lines:
            file.write(line + '\n')

sort_file_contents(r'03-python/question-4/input.txt', r'03-python/question-4/output.txt')
