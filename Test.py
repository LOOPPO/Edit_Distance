from EditDistance import edit_distance
import numpy as np
from NGram import create_indexes
from Jaccard import jaccard
from timeit import default_timer as timer

def main():
    list_of_word = []
    list_complete = open('a.txt', 'r')
    list_reader = list_complete.readlines()
    for line in (list_reader):
        list_of_word.append(line.rstrip('\n'))
    word = 'cane\n'
    number_of_tests=14
    number_of_columns=2
    matrix_of_time = np.zeros((number_of_tests, number_of_columns))
    for t in range(number_of_tests):
        startEdidtDistance = timer()
        editArray = []
        for k in range(len(list_of_word)):
            x = edit_distance(word, list_of_word[k])
            # print("Edit distance tra: ", word, " e ", list_of_word[k], "e': \n", x)
            if x <= 1:
                editArray.append(list_of_word[k])
        print("Array Edit distance di: ", word, " e' ",editArray)
        timerEditDistance = []
        endEditDistance = timer()
        elapsedEditDistance = endEditDistance - startEdidtDistance
        timerEditDistance.append(elapsedEditDistance)
        matrix_of_time[t][0] = elapsedEditDistance
        print("tempo per edit distance: ", timerEditDistance)
        matrix_of_time[t][0] = elapsedEditDistance

        ngram = create_indexes(word, 3)
        timerNGramJaccard = []
        startNGramJaccard = timer()
        jaccardArray = ['cena']
        for m in range(len(list_of_word)):
            y = create_indexes(list_of_word[m], 3)
            jc = jaccard(ngram, y)
            if jc >= 0.8:
                jaccardArray.append(list_of_word[m])
        editdistance_jaccard_array = []
        for i in range(len(jaccardArray)):
            eJaccard = edit_distance(word, jaccardArray[i])
            if eJaccard <= 2:
                editdistance_jaccard_array.append(jaccardArray[i])
        print("Array Edit con jaccard: ", editdistance_jaccard_array)
        endNGramJaccard = timer()
        elapsedNGramJaccard = endNGramJaccard - startNGramJaccard
        timerNGramJaccard.append(elapsedNGramJaccard)
        matrix_of_time[t][1] = elapsedNGramJaccard
        print("tempo per ngram e jaccard: ", timerNGramJaccard)
    print("Matrice con tempi finale: \n", matrix_of_time)

if __name__== '__main__':
    main()