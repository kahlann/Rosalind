"""
Python script to convert an RNA sequence into a protein sequence. 
NOTE: This script will terminate if the start codon is not the first codon.
This script also requires a helper file, codons.txt. This contains the
amino acid coded for by each codon.

$ python3 Translation.py
MAMAPRTEINSTRING
"""

from collections import defaultdict
from pprint import pprint

# Function to get the codon library as a dictionary
def getCodonLib(textfile):
    # Read in the text file that has the codons
    f = open(textfile)
    
    # Dictionary that we'll write the codon: AA pair to 
    codon_library = defaultdict(str)

    # from each line, get the codon and the amino acid it codes for
    for line in f:
        codon_library[line[0:3].strip()] = line[4:].strip()

    # Return the codon library
    return codon_library

# Function to translate genetic code to protein sequence
def Translate(textfile):

    # Get the codon library
    codon_library = getCodonLib("codons.txt")

    # Read in the genetic sequence
    sequence = open(textfile).read()

    # Split up the sequence into 3-character chunks
    n = 3
    codons = [(sequence[i:i+n]) for i in range(0, len(sequence), n)]
    
    # check that the first codon is the start codon
    if codon_library[codons[0]] != "M":
        print("No start codon!")
        return 

    # Empty string to hold the protein sequnce
    prot = ""

    # Iterate over the codons, appending the respective amino acid to the string
    for n, codon in enumerate(codons):

        # If it's a "stop" codon, exit!
        if codon_library[codon] == "Stop":
            return prot
        # Otherwise, add the amino acid to the protein sequence
        else: 
            prot += codon_library[codon]
    
    # Return the protein sequence
    return prot

print(Translate("rosalind_prot.txt"))

    
