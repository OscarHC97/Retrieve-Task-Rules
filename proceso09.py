import random

class Proceso09:	
	def Entrada(self,reglasConFamiliaridad, audio):
		self.audio = audio
		self.id =  [row[0] for row in reglasConFamiliaridad]
		self.pow = [row[1] for row in reglasConFamiliaridad]
		self.respuesta = random.choices(self.id,self.pow,k=1)
	
	def Salida(self):
		aux1 = self.audio[0]*2
		aux2 = (self.audio[1]/2)+1.5
		caso = round(aux1+aux2)
		importantBit = self.respuesta[0]>>(4-caso)
		return([self.respuesta[0], caso, importantBit%2])