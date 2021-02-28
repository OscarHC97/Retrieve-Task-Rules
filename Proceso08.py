import json
class Proceso08:
    def __init__(self):
        self.selectRules = []
       
    def entrada (self, rulesI):
       
        k=0
        ruta = 'rulesData/Reglas-O.json'
        with open(ruta, 'r') as contenido:
            #en las reglas de MTL buscas las reglas que te interezan y sacas un promedio con las reglas del Proceso 6
            #agregas a un vector ID + REGLA + PRIORIDAD.
            self.selectRules = json.load(contenido)
            self.ruleset =rulesI
            for i in self.selectRules: 
                for j in rulesI:
                     if i["ID"] == j[0]:
                        i["Priority"] =j[1]
                        self.ruleset[k] = i.get("ID"), i.get("if"), i.get("then"), i.get("Priority")
                        k=k+1
                        print (self.ruleset)
                         
        #para hacer cambio el cambio en la VLPFC
        with open(ruta,"w") as contenido:
            json.dump(self.selectRules,contenido)
            print("Guardado")       
        for i in self.ruleset:
            print(i)
                   # self.ruleset = i['ID'],i['if'], i['then'], rulesI['Priority']
            
    def salida (self):
        return self.ruleset

process = Proceso08()
process.entrada([(1, 22.0),(2, 44.0),(3, 22.0)])