"""
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: 
k individuals are homozygous dominant for a factor, 
m are heterozygous, 
and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele 
(and thus displaying the dominant phenotype). Assume that any two organisms can mate.
Possible combinations:
# dom dom --> Will yield dominant 100% of the time
# dom het --> 100%
# dom rec --> 100%
# het het --> 75%
# het rec --> 50%
# rec rec --> Will never yield dominant phenotype 
"""

def DominantChance(textfile):

    # Get k, m, n from the textfile
    nums = open(textfile).read().split(" ")
    k, m, n = int(nums[0]), int(nums[1]), int(nums[2])
    population = k + m + n

    # Chance of each pair occurring
    # Dominant-dominant pair
    dd = k/population * (k-1)/(population-1)
    # Dominant-hetero pair
    dh = 2 * ( k/population * m/(population-1) )
    # Dominant-recessive pair
    dr = 2 * ( k/population * n/(population-1) ) 
    # Hetero-hetero pair
    hh = m/population * (m-1)/(population-1)
    # Hetero-recessive pair
    hr = 2* ( m/population * (n)/(population-1) )
    # Recessive-recessive pair
    rr = n/population * (n-1)/(population-1)

    # Get the chance of a dominant allele showing up 
    return "{:.5f}".format(dd + dh + dr + 0.75*hh + 0.5*hr + 0*rr)

print(DominantChance("rosalind_iprb.txt"))
    
    
