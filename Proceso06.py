import json

class Proceso06:

    def __init__(self):
        self.rulesMTL = []
        self.IDrulesMTL = []

    def entrada(self,IDplan):
        #reglas Operativas
        rutaO ='rulesData/Reglas-MTL.json'
        #reglas de Dominio
        #rutaD = 'rulesData/Reglas-MTL.json'

        #separa las reglas por dominio reglas operativas
        if(IDplan == 20087):
            with open(rutaO,'r') as memoria:
                self.rulesMTL = json.load(memoria)
                for i in self.rulesMTL['rules']:
                    self.IDrulesMTL.append((i['ID'], i['Priority-A']))
                #print(self.IDrulesMTL)

        


    def salida(self):
        return self.IDrulesMTL
#process = Proceso06()
#process.entrada(20087)
#print(process.salida())