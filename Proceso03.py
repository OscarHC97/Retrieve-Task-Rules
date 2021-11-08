import numpy as np
import json
import random
from Proceso01 import Proceso01

class Proceso03:
    
    def __init__(self):
        self.IDrules= []
        self.PriRules = []
        self.rulesT = {}
        self.RecomAux = []
    def entrada (self, Nivel_Priorida, IDplan):
        k = 0
        p1 = Proceso01()
        for u in Nivel_Priorida:
            self.RecomAux.append(((u[0]+(u[1]))/2)) #sin prioridad en la ultima recompenza
            #self.RecomAux.append(((u[0]+(u[1]*1.5))/2.5)) #con prioridad a la ultima recompenza
        print(self.RecomAux)

        ruta = "rulesData/Reglas-O.json"
        with open(ruta,'r') as contenido:
            self.rulesT = json.load(contenido)
            #se agrega el nivel de prioridad y se integra al ID de la regla
            for i in self.rulesT:
                #print(i['if'][0],i['if'][1],i['then'])
                #indices  = p1.Similar(i['if'][0],i['if'][1],i['then'])
                #promedio = 0
                for j in range(8):
                    if i['ID'] == j:
                        i['Priority'] = (i['Priority'] + self.RecomAux[j])/2

                   # if j in indices:
                    #    promedio = promedio + self.RecomAux[j]
                #promedio = promedio /8
                #i['Priority']=promedio

                '''
                if self.RecomAux[k] == 0:
                    i['Priority'] = i['Priority'] 
                else:
                    i['Priority'] = (i['Priority'] + self.RecomAux[k])/2 #Promedia las reglas las reglas en el Json
                k +=1'''

                #print("ID:",i.get('ID'),"Priority: ",i.get('Priority'))
             
        with open(ruta,"w") as contenido:
            json.dump(self.rulesT,contenido)
            print("Guardado")
    def salida(self):
        ruta = "rulesData/Reglas-O.json"
        with open(ruta,'r') as contenido:
            self.rulesT = json.load(contenido)
            for i in self.rulesT:
                self.IDrules.append((i['ID'],i['Priority'])) 
               
            #print(self.IDrules)
        return(self.IDrules)
          
'''      
p1 = Proceso01()
#Process 10 simulation--------
ran1 = random.randrange(1,16)
ran2 = random.randint(0,1)

#process 1 simularion--------
print("rule: ", ran1, " Recom: ",ran2)
p1.Entrada(ran1,ran2) '''     
'''
matrizz =  [[0,0], [1,1], [0,0], [1,1], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]

proceso = Proceso03()
proceso.entrada(matrizz,20087)
proceso.salida()'''