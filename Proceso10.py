import random

class Proceso10:
		
	def Entrada(self, regla_audio_movimiento, numero_ensayo):

		self.regla_usada = regla_audio_movimiento[0]
		self.audio_escuchado = regla_audio_movimiento[1]
		self.movimiento_hecho = regla_audio_movimiento[2]

		regla_del_ensayo = 0
		if(1<= numero_ensayo and numero_ensayo<=10):
			regla_del_ensayo = 12
		elif(11<=numero_ensayo and numero_ensayo<=20):
			regla_del_ensayo = 10
		elif(21<=numero_ensayo and numero_ensayo<=30):
			regla_del_ensayo = 5
		elif(31<=numero_ensayo and numero_ensayo<=40):
			regla_del_ensayo = 3
		elif(41<=numero_ensayo and numero_ensayo<=50):
			regla_del_ensayo = 12
		elif(51<=numero_ensayo and numero_ensayo<=60):
			regla_del_ensayo = 15
		else:
			print("ERROR EN EL NUMERO DE ENSAYO")

		movimiento_correcto = (regla_del_ensayo>>(4-self.audio_escuchado))%2
		self.recompensa = 0
		if(movimiento_correcto == self.movimiento_hecho):
			self.recompensa = 1
		
	def Salida(self):
		return ([self.regla_usada, self.recompensa])


