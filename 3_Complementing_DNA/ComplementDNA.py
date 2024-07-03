"""
Python script to generate the sequence for a complementary DNA strand. 
Complements are in the reverse order: one strand is 5' --> 3', its complement is 3' --> 5'. 

$ python3 ComplementDNA.py
ACCTGACTGACGGTGATCTGA 
"""

def ReverseComplement(textfile):

    # Read in the sequence as a string, reverse it
    rev_seq = open(textfile).read()[::-1]

    # New string to hold the complement of the reverse
    comp = ""

    # Iterate over the string, replacing each base with its complement
    for nt in rev_seq:
        match nt:
            case "A":
                comp += "T"
            case "T":
                comp += "A"
            case "C":
                comp += "G"
            case "G":
                comp += "C"
    
    # Return the reverse complement string
    return comp

print(ReverseComplement("rosalind_revc.txt"))
