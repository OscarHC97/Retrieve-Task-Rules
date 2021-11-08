import random
import csv
from Proceso01 import Proceso01
class Proceso10:

	def Entrada(self, regla_audio_movimiento, numero_ensayo):
		self.recompensa = 0
		self.reglalista =[]
		self.regla_usada = regla_audio_movimiento[0]
		self.audio_escuchado = regla_audio_movimiento[1]
		self.movimiento_hecho = regla_audio_movimiento[2]

		regla_del_ensayo = 0
		regla_del_ensayo_pasado = 0	 	

		if(0<= numero_ensayo and numero_ensayo<=9):
			regla_del_ensayo = 12 #indice de la regla correcta en formato 0-15
			regla_del_ensayo_pasado = 0 #indice de la anterior regla correcta 0-15
		elif(10<=numero_ensayo and numero_ensayo<=19):
			regla_del_ensayo = 10
			regla_del_ensayo_pasado = 12
		elif(20<=numero_ensayo and numero_ensayo<=29):
			regla_del_ensayo = 5
			regla_del_ensayo_pasado = 10
		elif(30<=numero_ensayo and numero_ensayo<=39):
			regla_del_ensayo = 3
			regla_del_ensayo_pasado = 5
		elif(40<=numero_ensayo and numero_ensayo<=49):
			regla_del_ensayo = 12
			regla_del_ensayo_pasado = 3
		elif(50<=numero_ensayo and numero_ensayo<=59):
			regla_del_ensayo = 15
			regla_del_ensayo_pasado = 12
		else:
			print("ERROR EN EL NUMERO DE ENSAYO")
		if self.audio_escuchado[0] == 0 and self.audio_escuchado[1] == 0:
			self.caso = 3
		elif self.audio_escuchado[0] == 0 and self.audio_escuchado[1] == 1:
			self.caso = 2
		elif self.audio_escuchado[0] == 1 and self.audio_escuchado[1] == 0:
			self.caso = 1
		elif self.audio_escuchado[0] == 1 and self.audio_escuchado[1] == 1:
			self.caso = 0
		
		movimiento_correcto = (regla_del_ensayo>>(self.caso))%2
		movimiento_correcto_pasado = (regla_del_ensayo_pasado>>(self.caso))%2

		#Se abre el archivo csv para escribir la nueva línea
		with open('KCC5.csv', mode='a', newline='') as csv_file:
			fieldnames = ['Reaction_Time', 'Status', 'Picked_Side', 'Error', 'Perseveration_Error', 'Trial_was_not_Perseveration']
			writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
			#writer.writeheader()

			#Si el movimiento hecho y el correcto son iguales, no hubo error
			if (self.movimiento_hecho == movimiento_correcto):
				writer.writerow({'Reaction_Time':0,
								 'Status':1,
								 'Picked_Side':self.movimiento_hecho,
								 'Error':0,
								 'Perseveration_Error':0,
								 'Trial_was_not_Perseveration':0
								 })
			#Si el movimiento hecho no es correcto, se verifica si lo fue con la regla anterior
			elif(self.movimiento_hecho == movimiento_correcto_pasado):
				writer.writerow({'Reaction_Time': 0,
								 'Status': 2,
								 'Picked_Side': self.movimiento_hecho,
								 'Error': 1,
								 'Perseveration_Error': 1,
								 'Trial_was_not_Perseveration': 0
								 })
			#Si ninguna condición se cumple, entonces tenemos error sin perseveración
			else:
				writer.writerow({'Reaction_Time':0,
								 'Status':2,
								 'Picked_Side':self.movimiento_hecho,
								 'Error':1,
								 'Perseveration_Error':0,
								 'Trial_was_not_Perseveration':1
								 })
		
		if(movimiento_correcto == self.movimiento_hecho):
			self.recompensa = 1
		else:
			self.recompensa = 0 #recompenza negativa o no recompenza negativa
		
	def Salida(self):
		self.reglalista=[]
		#p1 =Proceso01()
		#self.reglalista = p1.Similar(self.audio_escuchado[0],self.audio_escuchado[1],self.movimiento_hecho)
		#print(self.reglalista)
		self.reglalista.append(self.regla_usada)

		return ([self.reglalista, self.recompensa])#recompenza usada formato de 0-7