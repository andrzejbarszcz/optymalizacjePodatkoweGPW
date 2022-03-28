import FIFOLogicClass as FLC
import datetime
import readFileTools as rfT

timeFrom = datetime.datetime(2020,1,1,0,0,0) #YYYY,MM,DD,HH,mm,ss
timeTo = datetime.datetime(2021,1,1,0,0,0)

def countTotalFinResult():
    totalResult = 0
    companies = rfT.readFileCompNames()
    for company in companies:
        currComp = FLC.FIFOLogic(company,timeFrom,timeTo)
        totalResult = totalResult + currComp.countFinResult()
    print(totalResult)

def countFinResultFor1Company(compName):
    currComp = FLC.FIFOLogic(compName,timeFrom,timeTo)
    print('wynik dla ' + compName + ' : ' + str(currComp.countFinResult()))

countTotalFinResult()
#countFinResultFor1Company('CELONPHARMA')
