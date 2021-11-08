import json

class corejson:
    def eliminaO (self):
        self.IDrules= []
        self.PriRules = []
        self.rulesT = {}
        self.RecomAux = []
        ruta = "rulesData/Reglas-O.json"
        with open(ruta,'r') as contenido:
            self.rulesT = json.load(contenido)
            #se agrega el nivel de prioridad y se integra al ID de la regla
            for i in self.rulesT:
                 i['Priority']=0

           

           
             
        with open(ruta,"w") as contenido:
            json.dump(self.rulesT,contenido)
            print("Eliminado")

    def eliminaM (self):
        self.IDrules1= []
        self.rulesT1 = {}
        ruta1 = "rulesData/Reglas-MTL.json"
        with open(ruta1,'r') as contenido1:
            self.rulesT1 = json.load(contenido1)
            #se agrega el nivel de prioridad y se integra al ID de la regla

            self.rulesT1['rules'] = [ ]
           

        with open(ruta1,"w") as contenido1:
            json.dump(self.rulesT1,contenido1)
            print("Eliminado")



p1 = corejson()

p1.eliminaO()
p1.eliminaM()