#!/usr/bin/env python3
from datetime import datetime
from pathlib import Path


def buildfindList(kind):
    pelroot = Path.cwd()
    findlist = []
    if kind == 'tag':
        findpath = Path(pelroot,'./output/tag/')
    if kind == 'cat':
        findpath = Path(pelroot,'./output/category/')
    for find in findpath.iterdir():
        findlist.append(find.name.replace(".html",""))
    findlistsorted = sorted(findlist)
    return findlistsorted

def showTheList(findlist,srchstring):
    allgroup = []
    rowIter = 1                                     ## rowIter keeps count of items in a row
    for t in findlist:
        if srchstring in t:
            allgroup.append(t)
    sglen = len(allgroup)
    prtstr = ""
    for i in range(sglen):
        prtstr = prtstr + allgroup[i] + '\t'
        if rowIter <= 4:
            rowIter += 1
        else:
            prtstr = prtstr + '\n'
            rowIter = 1
    # print(prtstr.expandtabs(20) + '\n')
    return prtstr

def buildkeepers(kind):
    findlist = buildfindList(kind)
    srchstring = ""
    keepers = ""
    print("Add tags one at a time.\nAppend or type a semicolon ';' to quit.\n")

    while kind == 'cat':
        prtstr = showTheList(findlist,srchstring)
        print(prtstr.expandtabs(20) + '\n')
        srchstring = input("Use this category: =>> ")  ## Prompt for search string.
        keepers = srchstring.strip(',').replace(';','')
        print("Category : " + keepers)
        return(keepers)
        quit()

    while kind == 'tag' and ';' not in srchstring:
        prtstr = showTheList(findlist,srchstring)
        if prtstr == '':
            print("That was a new one.")
        else:
            print(prtstr.expandtabs(20) + '\n')
        
        srchstring = input("Add this tag: =>> ")  ## Prompt for search string.
        keepers = keepers + srchstring.replace(';','') + ","
        print("Tags : " + keepers.replace(';','').strip(','))

        if kind == 'tag' and ';' in srchstring:
            keepers = keepers.replace(';','').strip(',')
            # print("Tags2 : " + keepers)
            return(keepers)
            quit()
    print("Keepers: " + keepers)






