
import datetime

xFileName = 'C:/spolkiGPW/transakcjeGosi/transakcjeGosi21.txt'

def datetimeFromStrings(myDate, myTime):
    result = []
    for ch in myDate.split('.'):
        result.append(int(ch))
    for ch in myTime.split(':'):
        result.append(int(ch))
    return datetime.datetime(result[2],result[1],result[0],result[3],result[4],0)

def readFile(xFileName):
    operations = []
    operationsTemp = []
    xFile = open(xFileName)
    for xLine in xFile:
        t1 = xLine.split()
        operationsTemp.append(t1)
    #konwersja poszcz typow - do nowych krotek i nowej listy
    #poszcz elementy do wartosci czatkowych z nich krotka i do listy
    for t1 in operationsTemp:
        operationTime = datetimeFromStrings(t1[0],t1[1])
        compName = t1[2]
        KorS = t1[3]
        vol = float(t1[4])
        price = float(t1[5])
        t2 = (operationTime,compName,KorS,vol,price)
        operations.append(t2)
    return operations

def readFileOneComp(compName):
    operations = readFile(xFileName)
    opFiltered = list(filter(lambda x: (x[1] == compName),operations))
    opFiltered.sort(key=lambda x:x[0])
    return opFiltered

def readFileCompNames():
    #odczyt readFile(xFileName) - dostaje liste krotek
    operations = readFile(xFileName)
    #tworze zbior stringow do ktorego bede pakowac nazwy - bez dublowania
    names = set()
    for o1 in operations:
        names.add(o1[1])
    #zamienic zbior na liste
    return list(names)
