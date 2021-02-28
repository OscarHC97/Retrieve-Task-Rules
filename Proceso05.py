class Proceso05:
    def __init__(self):
        self.rulesIDA = []
   
    
    def entrada(self,IDrules,IDAudio ):
        
        for i in range(len(IDrules)) :
           
           if IDrules[i]==IDAudio[i]:
                self.rulesIDA = IDrules[i]
                print(self.rulesIDA)
            

    def salida(self):
        
        return self.rulesIDA

process = Proceso05()

process.entrada([(1,22),(2,22),(3,22)],[(1,22),(4,22),(6,22)])
process.salida()