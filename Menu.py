class People:
    def __init__(self,name):
        self.listPeople = []
        self.__functionPrivate(name)
        
    def functionPublic(self):
        return 'Public function'

    def __functionPrivate(self,name):
        self.listPeople.append(name)
        return 'Private function'
    #__functionPrivate = functionPrivate

    def getListPeople(self):
        return self.listPeople

class Staff(People):
    def update(self, name, jobPosition):
        s=[name,jobPosition]
        self.listPeople.append(s)

x = People('Messias')
print(x.functionPublic())
People.functionPrivate
print(x.getListPeople())
print(x.functionPrivate('meme'))
print(x.getListPeople())
