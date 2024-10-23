#!/usr/bin/env python3

def reverse_complement(sequence):
    """Return the reverse complement of a DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement.get(base, base) for base in reversed(sequence))

def main():
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <input_fasta_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as fasta_file:
            sequence_name = None
            sequence_lines = []
            
            for line in fasta_file:
                line = line.strip()
                if line.startswith('>'):
                    if sequence_name is not None:
                        # Process the previous sequence
                        sequence = ''.join(sequence_lines)
                        rev_comp = reverse_complement(sequence)
                        print(f">{sequence_name} reverse complement")
                        print(rev_comp)
                    
                    # Start a new sequence
                    sequence_name = line[1:]  # Remove '>'
                    sequence_lines = []
                else:
                    sequence_lines.append(line)
            
            # Process the last sequence
            if sequence_name is not None:
                sequence = ''.join(sequence_lines)
                rev_comp = reverse_complement(sequence)
                print(f">{sequence_name} reverse complement")
                print(rev_comp)
    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
