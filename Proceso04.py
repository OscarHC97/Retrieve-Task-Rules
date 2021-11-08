import csv
import numpy as np
import json
import random
class Proceso04:
    def __init__(self):
        self.result = []
        self.audioloc = []
        self.contenite = []
        self.id_audio = []
       
    def entrada(self,num):
        with open('pruebee.csv') as File: #read the AudioFile
            self.result = csv.reader(File, delimiter = ',',quotechar = ',', quoting = csv.QUOTE_MINIMAL)
           
            for i in self.result:
               #print(i)
               if(float(i[1]) <= 0): #convertir los decimales negativo  a 0
                   i[1] =(float(i[1]) +1 )/2
                   i[1] = random.choices([0,1],[1-float(i[1]),float(i[1])],k=1)[0]
               elif(float(i[1]) >= 0): #convertir los decimales positivos a 1
                   i[1] = (float(i[1]) +1)/2
                   i[1] = random.choices([0,1],[1-float(i[1]),float(i[1])],k=1)[0]
               i[0]=int(i[0])
               self.audioloc.append(i)

            
            #for i in self.audioloc:
                
               # print(i)
            #print("Audio, Localizacion: ",self.audioloc[num])
            ruta = "rulesData/Reglas-O.json"
            with open(ruta,"r") as contenido:
                self.contenite = json.load(contenido)
                for i in self.contenite:
                    if(i["if"][0]  == self.audioloc[num][0] and i["if"][1] == self.audioloc[num][1]):
                        self.id_audio.append(i["ID"])
                        #print(self.id_audio)
            #eliminar ID repetidos
            temp = set(self.id_audio)
            tuple(temp)
            self.id_audio =temp
            #print("ID de reglas: ",self.id_audio)
                        


    def salida(self):
        return self.id_audio

#print("Porceso 4")
#etapa4 = Proceso04()
#etapa4.entrada(2)
