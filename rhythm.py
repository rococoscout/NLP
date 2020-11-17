# Title: Rhythm tally
# Author: Jess Lonetti
# Purpose: identify meta data for rhythm
#
# Contact Information: rococoscout@gmail.com
# ********************************************************************************

from lyric_opener import lyricopener


def trackrhy(passages):
    last5words = list()
    rhymetally = list()
    for passage in passages:
        for line in passages[passage].split('\n'):
            listofwords = line.split()
            lastword = listofwords[len(listofwords)-1]
            for prevword  in last5words:
                # print(prevword)
                if prevword == lastword:
                    n=1

            array = [0,0,0,0,0]
            for i in range(len(last5words)):
                if lastword == last5words[i]:
                    array[i]= 1
                elif len(last5words[i])<4:
                    n=0
                    for char in last5words[i]:
                        if char in lastword:
                            n = n + 1
                    if n/len(last5words[i])>=.5:
                        array[i] = 1
                else:
                    n = 0
                    for char in last5words[i][len(last5words[i])-4:]:
                        if char in lastword:
                            n = n + 1
                    if n/4>=.75:
                        array[i] = 1


            rhymetally.append(array)

            if len(last5words) > 4:
                last5words.append(lastword)
                last5words.pop(0)
            else:
                last5words.append(lastword)



    return rhymetally

if __name__ == "__main__":
    lo = lyricopener(["adele","al-green"],"archive/")
    print(trackrhy(lo.gettext()))

    array = [0,0,0,0,1]
    oarray = [0,0,1,0,1]
    if oarray == array:
        print("true")
