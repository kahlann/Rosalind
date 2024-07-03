"""
Python script to find the consensus sequence of a list of sequences. 
NOTE: profile matrix is returned as a DataFrame. The profile matrix is not necessary to pass the task.

$ python3 Consensus.py
ACTGTGCAGAGTCACAGTGGAT
"""

import pandas as pd
from pprint import pprint
import numpy as np
from collections import defaultdict

# Helper function to read in the sequence data
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


def GetConsensus(textfile):
    # get list of sequences (list of lists)
    sequences = GetFasta(textfile)
    seqs = []
    for seq in sequences.values():
        seqs.append(list(seq))

    # Make a pandas dataframe where each row in a new sequence, each element in df is a base
    df  = pd.DataFrame(seqs)

    # Empty lists to hold the number of occurrences of each base in each column
    A, T, G, C = [], [], [], []
    
    # Count to frequency of each base at each position
    for i in df.columns:
        # Append the count for A, if present (if not, add a 0)
        try:
            A.append(df[i].value_counts()["A"])
        except:
            A.append(0)
        # T
        try:
            T.append(df[i].value_counts()["T"])
        except:
            T.append(0)
        # C
        try:
            C.append(df[i].value_counts()["C"])
        except:
            C.append(0)
        # G
        try:
            G.append(df[i].value_counts()["G"])
        except:
            G.append(0)
    
    # Add those lists as rows to the dataframe
    df_counts = pd.DataFrame([A,T,C,G], index=["A","T","C","G"])

    # Get the consensus for each position
    # Empty list to hold consensus
    consensus = []

    # For each column
    for i in df_counts.columns:

        # Get the A/T/C/G row of the maximum value for that position
        consensus.append(df_counts[i].idxmax())
        
    # Print the consensus sequence
    print("".join(consensus))
    
    # Convert the consensus list to dataframe
    consensus = pd.DataFrame([consensus], index=["Consensus"])

    # Stick all the dataframes together, return it
    df = pd.concat([df,df_counts,consensus], axis=0)
    return df

GetConsensus("rosalind_cons.txt")
