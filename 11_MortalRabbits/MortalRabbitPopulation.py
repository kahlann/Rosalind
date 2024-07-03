"""
Python script to find the number of rabbit pairs after n months, when we start with a single
pair, and rabbits live for m months.

$ python3 MortalRabbitPopulation.py
4
"""

# Function to get the population of rabbits (as a number of PAIRS), with lifespan m months, after n months
# Takes the rosalind file and an initial population value (in pairs) as input
def MortalRabbitPopultion(textfile, initial_pop):

    # get n and m from the textfile
    # n is number of months
    # m is lifespan of the rabbits
    nm = open(textfile).read().split(" ")
    n, m = int(nm[0]), int(nm[1])

    # List to keep track of nuber of pairs - initiate with the initial population for months 1 and 2
    F = 2*[initial_pop]

    # Iterate over the months
    for month in range(n):
        # For the first 2 months, it's just the first pair
        if month < 2:
            pass
        # For all months before the first death, normal fibonacci        
        elif month < m:
            F.append(F[month-1] + F[month-2])
        # When we're in the month of the first death, take off the population from the first month
        elif month == m:
            F.append(F[month-1] + F[month-2] - F[0])
        # For all subsequent months, population is the previous 2 months minus all rabbits from m+1 months ago (who have died)
        else:
            F.append(F[month-1] + F[month-2] - F[month - (m + 1)]) 
    
    # Return the final month's population 
    return F[-1]

print(MortalRabbitPopultion("rosalind_fibd.txt",1))
