"""
Python script to convert a DNA sequence to an RNA sequence (replace T with U).

$ python3 ToRNA.py
 AUCCCGUAUGAUGCUAUGACU
"""

def DNA2RNA(textfile):

    # open the text file
    nuc_str = open(textfile).read()

    # Return string with T replaced with U
    return "{}".format(nuc_str.replace("T","U"))

print(DNA2RNA('rosalind_rna.txt'))
