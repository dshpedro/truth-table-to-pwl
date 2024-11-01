import sys
import os

def read_file(filename):
    with open(filename, 'r') as file:
        return file.readline().strip()

def write_file(filename, pwl_data):
    with open(filename, 'w') as file:
        for line in pwl_data:
            file.write(line + '\n')

def generate_pwl(sequence, transition_time, interval):
    pwl_data = []
    time = 0  # Start at 0ns

    for digit in sequence:
        # Point 1 (transition point)
        time += transition_time
        pwl_data.append(f"{time:.3f}ns {digit}") # *.001ns
        # Point 2
        time += (interval - transition_time)
        pwl_data.append(f"{time:.3f}ns {digit}") # *.000ns

    return pwl_data

def main():
    if len(sys.argv) < 2:
        print("Usage: py sequence_to_square_pwl.py <sequence_file>")
        return

    sequence_file = sys.argv[1]
    sequence = read_file(sequence_file)
    
    output_filename = os.path.splitext(sequence_file)[0] + '.pwl'
    pwl_data = generate_pwl(sequence, .001, 1)
    write_file(output_filename, pwl_data)

if __name__ == "__main__":
    main()

