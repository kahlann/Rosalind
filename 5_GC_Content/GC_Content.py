"""
Python script that takes a list of sequences in the FASTA format, and returns 
the ID of the sequence with the greatest GC content, as well as the % GC 
content of that sequence

$ python3 GC_Content.py
Rosalind_0808
60.919540
"""


from collections import defaultdict
from pprint import pprint

def GetFasta(fasta):
    # Read the fasta file, split by > characters, remove any empty strings
    fasta_seqs = open(fasta).read().split(">")
    fasta_seqs.remove("")

    # Empty dictionary to hold the data
    data = defaultdict(str)

    # For each sequence
    for seq in fasta_seqs:
        # Split new lines - creates a list. 
        # First element will be the sequence name, the rest is the sequence itself
        seq = seq.splitlines()
        
        # Join together the sequence elements, put in the dictionary
        data[seq[0]] = "".join(seq[1:])

    # Return the dictionary
    return data

def GC_Content(fasta):

    # Read the fasta file, split by > characters, remove any empty strings
    fasta_seqs = open(fasta).read().split(">")
    fasta_seqs.remove("")

    # Empty dictionary to hold the data
    GC_data = defaultdict(float)

    # For each sequence
    for seq in fasta_seqs:
        # Split new lines - creates a list. 
        # First element will be the sequence name, the rest is the sequence itself
        seq = seq.splitlines()
        sequence = "".join(seq[1:])

        # Dictionary entry is the GC percentage
        GC_data[seq[0]] = 100 * (sequence.count("G") + sequence.count("C")) / len(sequence)

    # Print the dictionary
    #pprint(GC_data)

    # Get the maximum GC %
    max_gc = max(GC_data.items(), key=lambda x: x[1])
    return "{}\n{:.6f}".format(max_gc[0], max_gc[1])

print(GC_Content("rosalind_gc.txt"))
