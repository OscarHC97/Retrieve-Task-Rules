import numpy as np
import json


class Proceso03:
    
    def __init__(self):
        self.IDrules= []
        self.PriRules = []
        self.rulesT = {}
    def entrada (self, Nivel_Priorida, IDplan):
        ruta = "rulesData/Reglas-O.json"
        with open(ruta,'r') as contenido:
            self.rulesT = json.load(contenido)
            #se agrega el nivel de prioridad y se integra al ID de la regla
            for i in self.rulesT:
                 i['Priority'] = Nivel_Priorida
                 print("ID:",i.get('ID'),"Priority: ",i.get('Priority'))
             
        with open(ruta,"w") as contenido:
            json.dump(self.rulesT,contenido)
            print("Guardado")
    def salida(self):
        ruta = "rulesData/Reglas-O.json"
        with open(ruta,'r') as contenido:
            self.rulesT = json.load(contenido)
            for i in self.rulesT:
                self.IDrules = i['ID'],i['Priority']
               
                print(self.IDrules)
        return(self.IDrules)
          
       

proceso = Proceso03()
proceso.entrada(22,34)
proceso.salida()
