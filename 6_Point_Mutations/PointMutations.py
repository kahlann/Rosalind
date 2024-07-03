"""
Python script to calculate the Hamming distance (number of point mutations)
between two DNA sequences.

$ python3 PointMutations.py
7
"""

def PointMutations(textfile):

    # Read the sequences into a list
    with open(textfile) as file:
        seqs = [line.rstrip() for line in file]
    
    # Mutation counter
    mutations = 0

    # Compare the two strings
    for posn, base in enumerate(seqs[0]):
        # If the bases at this position do not match, add to counter
        if base != seqs[1][posn]:
            mutations += 1

    # Return the number of mutations
    return mutations

print(PointMutations("rosalind_hamm.txt"))
