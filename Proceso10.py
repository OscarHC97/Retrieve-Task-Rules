import random
import csv

class Proceso10:

	def Entrada(self, regla_audio_movimiento, numero_ensayo):

		self.regla_usada = regla_audio_movimiento[0]
		self.audio_escuchado = regla_audio_movimiento[1]
		self.movimiento_hecho = regla_audio_movimiento[2]

		regla_del_ensayo = 0
		regla_del_ensayo_pasado = 0	 	

		if(1<= numero_ensayo and numero_ensayo<=10):
			regla_del_ensayo = 12
			regla_del_ensayo_pasado = 0
		elif(11<=numero_ensayo and numero_ensayo<=20):
			regla_del_ensayo = 10
			regla_del_ensayo_pasado = 12
		elif(21<=numero_ensayo and numero_ensayo<=30):
			regla_del_ensayo = 5
			regla_del_ensayo_pasado = 10
		elif(31<=numero_ensayo and numero_ensayo<=40):
			regla_del_ensayo = 3
			regla_del_ensayo_pasado = 5
		elif(41<=numero_ensayo and numero_ensayo<=50):
			regla_del_ensayo = 12
			regla_del_ensayo_pasado = 3
		elif(51<=numero_ensayo and numero_ensayo<=60):
			regla_del_ensayo = 15
			regla_del_ensayo_pasado = 12
		else:
			print("ERROR EN EL NUMERO DE ENSAYO")

		movimiento_correcto = (regla_del_ensayo>>(4-self.audio_escuchado))%2
		movimiento_correcto_pasado = (regla_del_ensayo_pasado>>(4-self.audio_escuchado))%2

		#Se abre el archivo csv para escribir la nueva línea
		with open('architectureResults.csv', mode='a', newline='') as csv_file:
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
								 'Trial_was_not_Perseveration':1
								 })
			#Si el movimiento hecho no es correcto, se verifica si lo fue con la regla anterior
			elif(self.movimiento_hecho == movimiento_correcto_pasado):
				writer.writerow({'Reaction_Time': 0,
								 'Status': 2,
								 'Picked_Side': self.movimiento_hecho,
								 'Error': 1,
								 'Perseveration_Error': 1,
								 'Trial_was_not_Perseveration': 1
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


		self.recompensa = 0
		if(movimiento_correcto == self.movimiento_hecho):
			self.recompensa = 1
		
	def Salida(self):
		return ([self.regla_usada, self.recompensa])