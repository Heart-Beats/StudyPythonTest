#!/user/bin/env python

import sys
import os


# print(sys.path)
# print(sys.argv)
# dir = os.popen('dir')
# print(dir.read())

# fpath = r'C:\Windows\system.ini'
# with open(fpath, 'r') as f:
#     s = f.read()
#     print(s)

def getDirAllFiles(fileDir):
    if os.path.isfile(fileDir):
        return os.path.split(os.path.abspath(fileDir))[1]
    elif os.path.isdir(fileDir):
        return list(map(getDirAllFiles, [os.path.join(fileDir, chdir) for chdir in os.listdir(fileDir)]))


def getContainStringfile(fileDir, *containStr):
    traveredFiles = []

    def traversingListFiles(files):
        if isinstance(files, list):
            for file in files:
                traversingListFiles(file)
            return traveredFiles
        else:
            traveredFiles.append(files)

    def filterFile(file):
        isFilter = False
        for fileStr in containStr:
            if isinstance(fileStr, str):
                isFilter = file.__contains__(fileStr)
                if isFilter:
                    return True
            else:
                raise ValueError('argument must be string!')
        return isFilter

    return list(filter(filterFile, traversingListFiles(getDirAllFiles(fileDir))))


print(getDirAllFiles('.'))
print(getContainStringfile('.', '购物车', 'xml', 'im'))
