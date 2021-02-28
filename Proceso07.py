import json
class Proceso07:
    def __init__(self):
        self.IDrulesMTL =[]
        self.rulesMTL =[]
    def entrada(self, IDrulesMTL, rulesIDA):
        self.rulesI =IDrulesMTL

        for i in range(len(IDrulesMTL)):
           
            if rulesIDA[i][0] ==IDrulesMTL[i][0]:
               #print(IDrulesMTL[i][1])
               self.rulesI[i]  = rulesIDA[i][0] ,(IDrulesMTL[i][1]+rulesIDA[i][1] )/2
               print(self.rulesI)          
            else:
                a =2
                self.rulesI[i] = rulesIDA[i][1]
            #print(temp[i],temp2[i])
        
       #Guardar los cambios en momeria MTL
        rutaO ='rulesData/Reglas-MTL.json'
        with open(rutaO,'r') as memoria:
                self.rulesMTL = json.load(memoria)
                for j in self.rulesMTL:
                    for i in self.rulesI:
                        if(j['ID']== i[0]):
                            print (j)
                            j['Priority-A'] =i[1]
                            
        with open(rutaO, 'w') as memoria:
            json.dump(self.rulesMTL,memoria)  
            print ("Guardado")  

    def salida(self):
        return  self.rulesI
process = Proceso07()
process.entrada([(1,22),(2,34),(3,2)],[(1,22),(2,22),(3,22)])
