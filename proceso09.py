import random
import math
class Proceso09:	
	def Entrada(self,reglasConFamiliaridad_audio):
		self.resultado = []
		#print(reglasConFamiliaridad_audio)
		self.audio = [row[1] for row in reglasConFamiliaridad_audio]  # pitch and location
		#print(self.audio)
		self.id =  [row[0] for row in reglasConFamiliaridad_audio]    #ID from the rule
		self.pow = [row[3] for row in reglasConFamiliaridad_audio]    #priority value 
	
		for i in range(len(self.pow)):
			if self.pow[i] == 0:
				self.pow[i]=0.01	
	
		if math.isclose(self.pow[0], self.pow[1], rel_tol=1e-3):
			self.respuesta = random.choices(self.id,[0.1,0.1],k=1)[0]
			#self.respuesta = random.choices(self.id,self.pow,k=1)[0]
		
		else:
			if self.pow[0] > self.pow[1]:
				self.respuesta = self.id[0]
			else:
				self.respuesta = self.id[1]

		
	
		#print(self.respuesta)

		for i in reglasConFamiliaridad_audio:
			if self.respuesta == i[0]:
				self.resultado = i
		print("regla seleccionada: ",self.resultado)

	
	def Salida(self):
		'''
		#self.audio[0][1] =  int(self.audio[0][1])
		aux1 = float(self.audio[0][0])*2  #convert in Int from STR 
		aux2 = (float(self.audio[0][1])/2)+1.5  #convert to INT from STR 
		caso = round(aux1+aux2)
		#seleccionar el movimiento adecuado respecto al formato 0-7
		importantBit = self.respuesta[0]>>(4-caso)
		return([self.respuesta[0], caso, importantBit%2])'''
		
		return(self.resultado)



#pruebas de unidad Proceso09 y Proceso10

#p9 = Proceso09()
#p9.Entrada([[15,1],[2,1],[3,1],[4,1]])
#p9.Entrada([(3, ['0', '-1'], '1', 0),(2, ['0', '-1'], '1',0)])
#print(p9.Salida())