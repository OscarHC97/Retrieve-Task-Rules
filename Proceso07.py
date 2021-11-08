import json
class Proceso07:
    def __init__(self):
        self.IDrulesMTL =[]
        self.rulesMTL =[]
        self.rulesI =[]
        self.datos ={}
        self.vector =[] #auxiliares para almacenar reglas MTL
        self.vector2 = [] #auxiliar para almacenar reglas IDA
        self.diferente = []
    def entrada(self, IDrulesMTL, rulesIDA):
        
        for j in IDrulesMTL:# reglas proceso 6
            self.vector.append(j[0])
        for i in rulesIDA: #reglas proceso 5
            self.vector2.append(i[0])
        #print(self.vector2, self.vector)
        dif = set(self.vector2) - set(self.vector)
        #print(dif)
        for i in rulesIDA: #obtain the diferent rule
            for j in dif:
                if i[0] == j:
                    self.diferente.append(i)
        #print("Diferente: ",self.diferente)

        #self.rulesI = self.diferente
        for j in rulesIDA:
         for i in IDrulesMTL:
            #print(i[1],j[1])
            if j[0] == i[0]:
               self.rulesI.append((i[0],(i[1]+j[1])/2))
        #print(self.rulesI, "reglas iguales")   
            
        
       #Guardar los cambios en momeria MTL
        rutaO ='rulesData/Reglas-MTL.json'
        with open(rutaO,'r') as memoria:
                self.rulesMTL = json.load(memoria)
                for j in self.rulesMTL['rules']:
                    for i in self.rulesI:
                        if(j['ID'] == i[0]):
                            #print (j)
                            j['Priority-A'] = i[1]
                #print(self.diferente)
                for k in self.diferente: #Guarda la regla que aun no se a echo
                    #print(k[0], k[1])
                    self.rulesMTL['rules'].append({'ID':k[0],'Priority-A':k[1]})
                  
                    self.rulesI.append(k)
               
        with open(rutaO, 'w') as memoria:
            json.dump(self.rulesMTL,memoria)  
            #json.dump(self.datos, memoria)
            #print ("Guardado")
            #print(self.rulesI)  
       
        
            #print("Datos: ",self.datos)   

    def salida(self):
        return  self.rulesI

#process = Proceso07()
#process.entrada([(1,55),(2,44),(3,11)],[(1,22),(2,22),(3,22),(4,22)])