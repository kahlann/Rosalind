"""
Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
Return: The adjacency list corresponding to O3. You may return edges in any order.
"""

from collections import defaultdict

# Helper function to get the fasta sequences fro the txt file 
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



# Function to get the overlap graph
def OverlapGraph(textfile,k):
    # Get the sequences
    seqdata = GetFasta(textfile)

    # Empty list to hold edges
    edges = []

    # iterate over the keys
    for i in seqdata:
        # iterate over the other keys to compare this sequence to all the other ones
        for j in seqdata:
            # Do not compare a sequence to itself
            if j == i:
                pass
            else: 
                # If the end of the first string matches the start of the other string
                if seqdata[i][-k:] == seqdata[j][:k]:
                    # Add it to the list of edges
                    edges.append(f"{i} {j}")
                # If the end of the second string matches the start of the first string
                elif seqdata[j][-k:] == seqdata[i][:k]:
                    # Add it to the list of edges
                    edges.append(f"{j} {i}")
                # If there's no match, move on
                else: 
                    pass

    # Get the edge list as a set
    edges = list(set(edges))

    # Return the edge list
    return "\n".join(edges)


print(OverlapGraph("rosalind_grph.txt",3))
