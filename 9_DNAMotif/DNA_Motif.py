"""
Python script to find the position(s) of a given motif (subsequence) within a DNA sequence.

$ python3 DNA_Motif.py
2 4 10 
"""

def FindMotifs(textfile):

    # Read the text file, splitting into the sequence and the search motif
    f = open(textfile).read().split("\n")
    seq, motif = f[0], f[1]

    # empty list for positions
    posns = []

    # iterate over the sequence, up to the point where the motif would overhang the end of the sequence
    for i in range(len(seq)-len(motif)):
        # Compare the subsection of the string to the motif
        # If they match, append the position of the start of the motif to the list
        if seq[i:i+len(motif)] == motif:
            posns.append(str(i+1))
    
    # Return the positions string
    return " ".join(posns)

print(FindMotifs("rosalind_subs.txt"))
