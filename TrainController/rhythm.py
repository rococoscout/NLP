# Title: Rhythm tally
# Author: Jess Lonetti
# Purpose: identify meta data for rhythm
#
# Contact Information: rococoscout@gmail.com
# ********************************************************************************

from lyric_opener import lyricopener

def rhyme(word1,word2):
    if word1 == word2:
        return True
    n = 0
    if len(word1)>3 and len(word2)>3:
        for i in range(1,5):
            if word2[len(word2)-i]==word1[len(word1)-i]:
                n = n+1
        if n/4 >= .75:
            print(n/4 )
            return True
    if len(word1)< len(word2):
        temp = word1
        word1=word2
        word2 = temp

    for i in range(1,len(word2)):
        if word2[len(word2)-i]==word1[len(word1)-i]:
            print(word2[len(word2)-i])
            n = n+1

        if n/len(word2) >= .60:
            print( n/len(word2))
            print(len(word2))
            return True

    return False


def rhymescore(passage):
    initialDict = {}
    finalDict = {}
    lineon = 0
    for line in passage.split('\n'):
        listofwords = line.split()
        lastword = listofwords[len(listofwords)-1]


        if len(lastword)<4:
            if lastword in initialDict:
                initialDict[lastword].append(lineon)
            else:
                initialDict[lastword] = []
                initialDict[lastword].append(lineon)
        else:
            if lastword[len(lastword)-4:] in initialDict:
                initialDict[lastword[len(lastword)-4:]].append(lineon)
            else:
                initialDict[lastword[len(lastword)-4:]] = []
                initialDict[lastword[len(lastword)-4:]].append(lineon)


        lineon += 1
    # flag = True
    # total = 0
    # for end in initialDict:
    #     total += len(initialDict[end])
    #     for compared in finalDict:
    #         flag = False
    #         if compared == end:
    #             finalDict[compared].append(initialDict[end])
    #         elif len(end) == len(compared):
    #             n = 0
    #             for i in range(len(end)):
    #                 if end[i] == compared[i]:
    #                     n = 1 + n
    #             if n/len(end) >= .5:
    #                 finalDict[compared].append(initialDict[end])
    #         else:
    #             flag = True
    #
    #         if flag:
    #             finalDict[end] = initialDict[end]
    #
    #     if flag:
    #         finalDict[end] = initialDict[end]
    #
    # rhymed = 0
    # for i in finalDict:
    #     if len(i)>1:
    #         rhymed += len(i)



    return

if __name__ == "__main__":
    lo = lyricopener(["adele","al-green"])
    print(rhymescore(lo.gettext()["al-green"]))
    print(rhyme("harder","faster"))
