'''
DNA Sequence Analyzer
Created by: Sarah Williams

Purpose: 
    1. Count nucleotides.
    2. Identify GC content (DNA stability).
    3. Identify proteins.
    4. Identify 5' and 3' ends.
    5. Data export.
'''

def analyze_dna_sequence(dna_sequence):
    # Initialize a dictionary to store nucleotide counts
    nucleotide_counts = {
        'A': 0,
        'T': 0,
        'C': 0,
        'G': 0
    }

    # Count each nucleotide in the sequence
    for nucleotide in dna_sequence:
        if nucleotide in nucleotide_counts:
            nucleotide_counts[nucleotide] += 1

    return nucleotide_counts

def main():
     # Example DNA sequence
    dna_sequence = input("DNA Sequence: ")

    # Analyze the DNA sequence
    counts = analyze_dna_sequence(dna_sequence)

    # Print the results
    print("Nucleotide counts:")
    for nucleotide, count in counts.items():
        print(f"{nucleotide}: {count}")

if __name__ == "__main__":
    main()