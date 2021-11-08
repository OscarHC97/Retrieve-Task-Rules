import random
from decimal import *
class Proceso01:
	def __init__(self):
		self.regla = []
		self.cont = []
		for i in range (8):
			self.regla.append([0.0,0.0])
			self.cont.append(0)

	def Entrada(self,id_regla, recompensa): #ID_regla debe ser un arreglo
		#average
		for i in id_regla:
			#self.regla[i][0] = max(self.regla[i][0], recompensa) #khaneman
			#self.regla[i][1] = recompensa
			
			#self.regla[i][0] = (self.regla[i][0] * self.cont[i] + recompensa) #sin olvido
			self.cont[i] += 1
			self.regla[i][0] = (self.regla[i][0]+ recompensa)/2 #con olvido
			#self.regla[i][0] = self.regla[i][0]/self.cont[i] #sin olvido
			self.regla[i][1] = recompensa

		

	def Salida(self):
		return(self.regla)

	def Similar(self,a,b,c):
		getcontext().rounding = ROUND_HALF_UP
		aux = []
		a1 = (a*(-1))+1
		b1 = (b/2.0)+0.5
		b1 = b1*(-1)+1
		cont = int(Decimal(a1*2+b1).quantize(Decimal('1')))
		#cont = round(2.51)
		
		for i in range(16):
			if((i>>cont)%2 == c):
				aux.append(i)

		return aux

#p1 = Proceso01()
#p1.Entrada(2,33)
#print(p1.Salida())