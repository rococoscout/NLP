# Title: Lyric Opener
# Author: Jess Lonetti
# Purpose: identify meta data for rhythm
#
# Contact Information: rococoscout@gmail.com
# ********************************************************************************

from lyric_opener import lyricopener 

if __name__ == "__main__":
    lo = lyricopener(["adele","al-green"],"archive/")
    print(lo.gettext())
