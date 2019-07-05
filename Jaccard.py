def jaccard(x,y):
    intersection = set(x).intersection(y)
    #print("Intersetion = ", intersection) #uncomment
    union = set(x).union(set(y))
    #print("Union = ", union)  #uncomment
    if union != 0:
        jaccard = len(intersection)/len(union)
        return jaccard
