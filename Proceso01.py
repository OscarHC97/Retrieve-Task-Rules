import random

class Proceso01:
	def __init__(self):
		self.regla = []
		self.cont = []
		for i in range (16):
			self.regla.append([0.0,0.0])
			self.cont.append(0)

	def Entrada(self,id_regla, recompensa):
		"""#average
		self.regla[id_regla][0] = (self.regla[id_regla][0] * self.cont[id_regla] + recompensa) 
		self.cont[id_regla] += 1
		self.regla[id_regla][0] = self.regla[id_regla][0]/self.cont[id_regla]
		self.regla[id_regla][1] = recompensa
		"""
		self.regla[id_regla][0] = max(self.regla[id_regla][0], recompensa)
		self.regla[id_regla][1] = recompensa

	def Salida(self):
		return(self.regla)