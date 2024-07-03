"""
Python script to find the longest common motif in a set of sequences. 
This script is too slow to use on the problem set and submit an answer within the 5 minutes. 
This script does work, though!

$ python3 LongestCommonMotif.py
ACTGATGACGGATGGACCC
"""

# THIS SOLUTION IS VERY SLOW! Too slow to solve the rosalind problem set in under 5 minutes
# It does work, though.
import numpy as np
import pandas as pd
from collections import defaultdict
from pprint import pprint
# https://readiab.org/pairwise-alignment.html

# HELPER FUNCTIONS 
# Read in fasta data to a dictionary 
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


# Compare two sequences
def GetLongestMotifs(seq_1, seq_2):
    # CREATE MATRIX TO HOLD ALIGNMENT
    # Create a blank matrix where the rows and 
    # columns represent the positions in the sequences
    data = np.zeros(shape=(len(seq_2), len(seq_1)), dtype=int)

    # Convert to dataframe to add column names and row indices
    data = pd.DataFrame(data, columns=[x for x in seq_1], index=[x for x in seq_2])

    # FIND MATCHING ELEMENTS 
    # If column and row labels are the same, replace 0 with 1 in the dataframe
    # Iterate over the row indices (from the original string, not the actual row indices)
    for row_number, row_character in enumerate(seq_2):
        # Iterate over the column labels (from the original string, not the actual column labels)
        for col_number, col_character in enumerate(seq_1):
            # If the column label and row index match
            if row_character == col_character:
                # Make that element of the dataframe a 1
                data.iloc[row_number, col_number] = 1

    # FIND LONGEST DIAGONAL(S) (LONGEST COMMON MOTIF) 
    # NOTE that there may be more than one longest common motif! 
    # Keep a dataframe of all diagonals - length of the diagonal, row, column of the (current) end of the diagonal
    # Then once we've been through the whole dataframe, remove all rows that are not of the same length as the longest diagonal
    track_diags = pd.DataFrame(columns=["length","row","column"])

    # Set counter for keeping track of the current longest motif
    max_len = 1

    # iterate over the cells in the data matrix, starting in the second row and second column
    # Iterate over rows
    for i in range(1, len(data.index)):
        # Iterate over columns
        for j in range(1, len(data.columns)):
            # if the value in the current cell is greater than zero
            # (i.e., the characters at the corresponding pair of
            # sequence positions are the same)...
            if data.iloc[i, j] > 0:
                # ... add the value from the cell that is diagonally up and to the left
                data.iloc[i, j] += data.iloc[i-1,j-1]

                # If this diagonal is longer than or the same length as the current longest diagonal
                if data.iloc[i, j] >= max_len:
                    track_diags = pd.concat([track_diags, pd.DataFrame([[data.iloc[i, j], i, j]], columns=["length","row","column"])], axis=0)
                    max_len = data.iloc[i, j]

    # Keep only the rows with the maximum length
    track_diags = track_diags.loc[track_diags['length'] == max_len]

    # Get the longest common motifs as a list
    lcms = []
    for i in range(len(track_diags['length'])):
        row = track_diags.iloc[i,:]
        lcms.append(seq_2[row[1]-row[0]+1:row[1]+1])

    # Return the list of longest common motifs
    return lcms, max_len


# MAIN FUNCTION 
# Function to get the longest common motif between sequences
# Takes the fasta file as input
def MultipleSeqMotif(fasta):

    # Read in the sequences, transform from dictionary to list (don't care about the sequence names in this case)
    seq_list = list(GetFasta(fasta).values())

    # Iterate over the list
    for n, seq in enumerate(seq_list):

        # If it's the first sequence
        if n == 0:
            print("Comparing sequences 1 and 2...")
            # Compare it to the second sequence
            lcms, max_len = GetLongestMotifs(seq, seq_list[1])
        
        # If it's the second sequence, skip (already compared)
        elif n == 1:
            pass

        # For all other sequences
        else:
            print(f"Comparing sequence {n+1}...")
            # Temporary dataframe to hold the longest common motifs in
            temp_df = pd.DataFrame(columns=['length','motif'])

            # For each item in the list of longest common motifs
            for lcm in lcms:
                # Compare that motif to the current sequence
                new_lcms, length  = GetLongestMotifs(lcm, seq)

                # Put the motif(s) in the temporary dataframe
                for motif in new_lcms:
                    temp_df = pd.concat([temp_df, pd.DataFrame([[length, motif]], columns=["length", "motif"])], axis=0)

            # Keep only the longest motif(s)
            temp_df = temp_df.loc[temp_df['length'] == max(temp_df['length'])]

            # Replace the longest common motif list with a fresh list of the new longest motifs
            lcms = []
            for i in range(len(temp_df['length'])):
                row = temp_df.iloc[i,:]
                lcms.append(row[1])

    # Return the list of longest common motifs
    return lcms

# Find the longest common motifs for a given list of sequences
pprint(MultipleSeqMotif("rosalind_lcsm.txt"))
