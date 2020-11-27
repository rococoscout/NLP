# Title: Rhythm tally
# Author: Jess Lonetti
# Purpose: identify meta data for rhythm
#
# Contact Information: rococoscout@gmail.com
# ********************************************************************************

from lyric_opener import lyricopener


def rhymescore(passage):
    initialDict = {}
    listoflist = []
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

    return initialDict

if __name__ == "__main__":
    lo = lyricopener(["adele","al-green"])
    print(rhymescore(lo.gettext()["adele"]))
