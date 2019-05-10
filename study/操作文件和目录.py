#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

#获取指定目录下的所有文件和子文件
def getDirAllFiles(fileDir):
    if os.path.isfile(fileDir):
        return os.path.split(os.path.abspath(fileDir))[1]
    elif os.path.isdir(fileDir):
        return list(map(getDirAllFiles, [os.path.join(fileDir, chdir) for chdir in os.listdir(fileDir)]))

#获取包含指定字符串的文件
def getContainStringfile(fileDir, *containStr):
    traveredFiles = []

    #遍历文件层次列表转为一维列表
    def traversingListFiles(files):
        if isinstance(files, list):
            for file in files:
                traversingListFiles(file)
            return traveredFiles
        else:
            traveredFiles.append(files)

    #过滤文件
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
print(getContainStringfile('.', 'aewfja'))
