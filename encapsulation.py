class Cricketer:

    Country = "INDIA"

    def __init__(self,name,runs,type):
        self.name=name
        self._type=type
        self.__runs=runs

    def runs(self):
        print(self.__runs)

Virat = Cricketer("Virat",10000,"Batsman")
print(Virat._type)
Virat.runs()
Cricketer.runs(Virat)