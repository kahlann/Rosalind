from collections import defaultdict

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
