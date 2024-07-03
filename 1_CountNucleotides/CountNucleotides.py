"""
Python script to count the number of A, C, G, and T nucleotides in a given DNA sequence.

$ python3 CountNucleotides.py 
10 15 23 17
"""

def CountNucleotides(textfile):

    # open the text file
    nuc_str = open(textfile).read()

    # Return string with nucleotide counts
    return "{} {} {} {}".format(nuc_str.count("A"), nuc_str.count("C"), nuc_str.count("G"), nuc_str.count("T"))

print(CountNucleotides('rosalind_dna.txt'))
