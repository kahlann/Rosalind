def ReadIn(textfile):
    # get n and k from the textfile
    nk = open(textfile).read().split(" ")
    n, k = int(nk[0]), int(nk[1])
