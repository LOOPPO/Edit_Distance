def create_indexes(word, n):
    word = word[:len(word)-1]
    x = len(word)
    gram = []
    if x < n:
        gram.append(word)
    else:
         for c in range(x):
             if (x - n) >= c:
                gram.append(word[c:c+n])
    return gram