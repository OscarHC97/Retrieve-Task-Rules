class Proceso05:
    def __init__(self):
        self.rulesIDA = []
   
    
    def entrada(self,IDrules,IDAudio ):
        for j in IDAudio:
            for i in range(len(IDrules)):
                if IDrules[i][0]==j:
                  self.rulesIDA.append(IDrules[i])
        
        
        #print("Reglas filtradas: ",self.rulesIDA)
                
            

    def salida(self):
        
        return self.rulesIDA

#process = Proceso05()
#process.entrada([(1,22),(2,22),(3,22)],[(1,22),(2,22),(3,22)])
#process.entrada([(1,22),(2,22),(3,22)],[2,3])
#id_RulesIDA = process.salida()