import os
class Database:
    lstRegisters = []
    def __init__(self):
        self.__checkFileExist()
        #print(self.lstRegisters)
    def __checkFileExist(self):
        if not(os.path.isfile('./database.txt')):
            file=open('./database.txt','w')
            file.close()
        return True

    def showAll(self):
        file=open('./database.txt','r')
        for i in file:
            print ('Item ',i)
        file.close()
    
    def include(self,lstRegister):
        try:
            if len(self.lstRegisters)>0:
                self.lstRegisters.append(lstRegister)
                print('aqui')
                return True
            return False
        except ValueError:
            return False

    def getLstRegisters(self):
        return self.lstRegisters
    def getSizeLstRegisters(self):
        return len(self.lstRegisters)
    def save(self,lstRegister):
        try:
            if len(lstRegister)>0:
                file=open('./database.txt','a')
                for i in lstRegister:
                    file.write(str(i)+'\n')
                file.close()
                return True
            else:
                print('Not possible register')
                return False
        except ValueError:
            print('Error: ', ValueError)
            return False

#d = Database()


#print(d.show())

