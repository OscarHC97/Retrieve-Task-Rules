import json
class Proceso08:
    def __init__(self):
        self.selectRules = []
        self.ruleset = []
       
    def entrada (self, rulesI):
       
        ruta = 'rulesData/Reglas-O.json'
        with open(ruta, 'r') as contenido:
            #en las reglas de MTL buscas las reglas que te interezan y sacas un promedio con las reglas del Proceso 6
            #agregas a un vector ID + REGLA + PRIORIDAD.
            self.selectRules = json.load(contenido)
            #self.ruleset =rulesI
            for i in self.selectRules: 
                for j in rulesI:
                     if i["ID"] == j[0]:
                        #i["Priority"] =j[1]
                        #print(i)
                        self.ruleset.append(( i["ID"], i["if"], i["then"], i["Priority"]))
                   
            #print (self.ruleset)
                               
       
                   # self.ruleset = i['ID'],i['if'], i['then'], rulesI['Priority']
            
    def salida (self):
        return self.ruleset

#process8 = Proceso08()
#process8.entrada(rulesI)
#process8.entrada([(1, 22.0),(2, 44.0),(3, 22.0)])
#ruleset = process8.salida()