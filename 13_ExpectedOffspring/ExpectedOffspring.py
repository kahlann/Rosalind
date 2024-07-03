"""
Given: Six nonnegative integers, each of which does not exceed 20,000. 
The integers correspond to the number of couples in a population possessing 
each genotype pairing for a given factor. In order, the six given integers 
represent the number of couples having the following genotypes:
AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa

Return: The expected number of offspring displaying the dominant phenotype 
in the next generation, under the assumption that every couple has exactly 
two offspring.
"""

def ExpectedOffspring(textfile):

    # Read in the number of each couple from the textfile
    nums = open(textfile).read().split(" ")
    dd = int(nums[0])   # Dominant offspring 100% of the time
    dh = int(nums[1])   # 100%
    dr = int(nums[2])   # 100%
    hh = int(nums[3])   # 75%
    hr = int(nums[4])   # 50%
    rr = int(nums[5])   # 0%

    # expected number of dominant offspring (if each couple has 2 children)
    return 2 * ( dd + dh + dr + 0.75*hh + 0.5*hr + 0*rr )

print(ExpectedOffspring("rosalind_iev.txt"))