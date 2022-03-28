import datetime
import readFileTools as rfT

class FIFOLogic:
    def __init__(self, compName, timeFrom, timeTo):
        self.compName = compName
        self.timeFrom = timeFrom
        self.timeTo = timeTo
        self.operations = rfT.readFileOneComp(compName)
        self.finResult = 0
        self.inventory = []
        self.insidePeriod = 0

    def buy(self,operation):
        #podniesienie kosztu inw o prowizje 0,039%
        cost = operation[4] * 1.0039
        i = (operation[0],operation[3],cost)
        self.inventory.append(i)

    def sell(self,operation):
        result = 0
        volOp = operation[3]
        priceAfterProv = operation[4]*(1-0.0039)
        try:
            volInv = self.inventory[0][1]
        except IndexError:
            print('wystapil blad - brak sprzedawanej pozycji w inventory')
            print(operation)
            print('brak moze byc uzasadniony specyfiką (np pp), a moze nie być - ocen sam')
            print('jezeli nie potrafisz ocenic, zignoruj operacje albo przerwij dzialanie programu')
            print('jeżeli chcesz zaakceptować operację i dodac do inventory odpowiednik z cena zakupu 0 - wprowadz 1')
            print('jeżeli chcesz zignorowac tylko niniejsza operacje - wprowadz 2')
            print('aby przerwac dzialanie programu - wprowadz cokolwiek inneg')

            whatToDo = input('wprowadz 1, 2 albo cos innego :  ')
            if (whatToDo == '1'):
                print('kontynuujemy wyliczenia z uwzglednieniem ww operacji')
                i = (operation[0],operation[3],0.0)
                self.inventory.append(i)
                volInv = self.inventory[0][1]
            elif (whatToDo == '2'):
                print('kontynuujemy wyliczenia z pominięciem ww operacji')
                volOp = 0
            else:
                print('przerwano wykonywanie programu')
                quit()
        while volOp > 0:
            if volOp > volInv:
                result = result + (volInv*(priceAfterProv - self.inventory[0][2]))*self.insidePeriod
                volOp = volOp - volInv
                del self.inventory[0]
                volInv = self.inventory[0][1]
            elif volOp < volInv:
                result = result + (volOp*(priceAfterProv - self.inventory[0][2]))*self.insidePeriod
                #podmienic naruszona krotke inventory
                self.inventory[0] = (self.inventory[0][0],volInv - volOp,self.inventory[0][2])
                volOp = 0
            else: #volOp = volInv - usuwamy
                result = result + (volOp*(priceAfterProv - self.inventory[0][2]))*self.insidePeriod
                del self.inventory[0]
                volOp = 0

        self.finResult = self.finResult + result

    def countFinResult(self):
        for o1 in self.operations:
            if(o1[0] > self.timeFrom and o1[0] < self.timeTo):
                    self.insidePeriod = 1
            else:
                self.insidePeriod = 0
            if o1[2] == 'K':
                self.buy(o1)
            else:
                self.sell(o1)
        return self.finResult
