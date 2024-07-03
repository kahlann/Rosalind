"""
Python script to find the longest common motif in a set of sequences. 
This script is adapted from an answer of Stack exchange, and is much more efficient
than the other script! https://stackoverflow.com/questions/2892931/longest-common-substring-from-more-than-two-strings

$ python3 LCM_Fast.py
ACTGATGACGGATGGACCC
"""

# Much more efficient answer. Stolen from StackExchange:
# https://stackoverflow.com/questions/2892931/longest-common-substring-from-more-than-two-strings
from collections import defaultdict

# Helper function to read in fasta data to a dictionary 
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


# Helper function to determine whether a substring is present in each string in a list of strings
# find is the substring to find in each string; data is the list of strings to test against
def is_substr(find, data):
    # If the list of strings is empty, and the length of the substring to find is 0, return False
    if len(data) < 1 and len(find) < 1:
        return False
    # Otherwise, test the substring against every string in the list
    for i in range(len(data)):
        # If the substring is not present in that substring, return False
        if find not in data[i]:
            return False
    # If the substring was found in every other string, return True
    return True


# Function to get the longest common substring across a list of strings
def long_substr(data):
    # Empty string to hold substring
    substr = ''
    # If there is more than one string in the list, and the first item in the list is not empty
    if len(data) > 1 and len(data[0]) > 0:
        # Iterate over the length of the first string
        for i in range(len(data[0])):
            # j sets the length of the substring being tested
            for j in range(len(data[0])-i+1):
                # While j is greater than the length of the current longest substring,
                # and the new substring in question is in all strings in the list
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    # Set the new longest substring
                    substr = data[0][i:i+j]

    # return the longest common substring
    return substr

# Get sequence list
seq_list = list(GetFasta("rosalind_lcsm.txt").values())
# Find longest common substring
print(long_substr(seq_list))
