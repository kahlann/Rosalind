"""
Python script to find the number of rabbit pairs (immortal) after n months, 
assuming that we begin with a single pair and in each generation every pair 
of reproduction-age rabbits produces a litter of k rabbit pairs.

$ python3 RabbitPopulation.py
19
"""

def RabbitPopultion(textfile):

    # get n and k from the textfile
    nk = open(textfile).read().split(" ")
    n, k = int(nk[0]), int(nk[1])

    # List to keep track of nuber of pairs - initiate with 1,1 for months 1 and 2
    F = [1,1]

    # Iterate over the months
    for month in range(n):
        # For the first 2 months, it's just the first pair
        if month < 2:
            pass
        # For all other months, the population is the previous month's population, plus however many pairs were produced by mature rabbits (2 months or older!)
        else:
            F.append(F[month-1] + k*F[month-2])
    
    # Return the final month's population
    return F[-1]

print(RabbitPopultion("rosalind_fib.txt"))
