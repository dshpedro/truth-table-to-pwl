import os
import subprocess

def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines]

def write_file(filename, data):
    with open(filename, 'w') as file:
        for line in data:
            file.write(line + '\n')

def split_into_files(lines):
    # iterate over each line and create a file for each sequence
    sequence_files = []
    for i, line in enumerate(lines):
        filename = f'seq_{chr(97 + i)}.txt'  # chr(97) == 'a'
        with open(filename, 'w') as file:
            file.write(line + '\n')
        sequence_files.append(filename)

    return sequence_files

def transpose_truth_table(truth_table):
    # split each line into individual characters, excluding the last column
    columns = [list(line[:-1]) for line in truth_table if line.strip()]
    # use zip to transpose rows and columns
    transposed = list(zip(*columns))
    # join each tuple back into a string
    return [''.join(row) for row in transposed]

def main():
    truth_table = read_file('truth_table.txt')
    transposed_table = transpose_truth_table(truth_table)
    
    sequence_files = split_into_files(transposed_table)
    for file in sequence_files:
        subprocess.run(['python', 'sequence_to_square_pwl.py', file])
        os.remove(file)

if __name__ == "__main__":
    main()

