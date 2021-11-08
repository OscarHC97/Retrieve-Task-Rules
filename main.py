from Proceso01 import Proceso01
from Proceso02 import Proceso02
from Proceso03 import Proceso03
from Proceso04 import Proceso04
from Proceso05 import Proceso05
from Proceso06 import Proceso06
from Proceso07 import Proceso07
from Proceso08 import Proceso08
from Proceso09 import Proceso09
from Proceso10 import Proceso10
import random
m=0

def main():
    p10 = Proceso10()
    etapa1 = Proceso01()
    Endsalida = []
    #Nivel_priority =[]
    for i in range(60):

     #PROCESO 1 in: (id_regla, recompensa)
     print("Proceso 1")
     
     #Nivel_priority = random.randint(0,1)
     #print(Nivel_priority)
     if i == 0:
         Nivel_priority = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
         
     else:
         #print("Salida de p10: ", p10.Salida()[0], p10.Salida()[1])
         etapa1.Entrada(Endsalida[0],Endsalida[1])
         Nivel_priority = etapa1.Salida()
         print(etapa1.Salida())
     #PROCESO 2
     print("Proceso 2")
     process = Proceso02()
     id_plan = process.salida()
     #print(process.salida())
    
    
     #PROCESO 3  in: ( Nivel_priority, id_plan )
     print("Proceso 3")
     etapa2 = Proceso03()
     etapa2.entrada(Nivel_priority,id_plan)
     id_rules = etapa2.salida()

     #PROCESO 4 
     print("Porceso 4", i)
     etapa4 = Proceso04()
     etapa4.entrada(i) #le paso la variable global para avanzar
     id_audio = etapa4.salida()
     


     #PROCESO 5 in: ( id_rules, id_audio )
     print("Proceso 5")
     process = Proceso05()
     #process.entrada([(1,22),(2,22),(3,22)],[(1,22),(2,22),(3,22)])
     process.entrada(id_rules,id_audio)
     id_RulesIDA = process.salida()


     #PROCESO 6 in: (id_Plan)
     print("Proceso 6")
     process = Proceso06()
     process.entrada(id_plan)
     Id_rulesMTL = process.salida()


     #PROCESO 7 in:( Id_rulesMTL, id_RulesIDA )
     print("Proceso 7")
     process7 = Proceso07()
     process7.entrada(Id_rulesMTL, id_RulesIDA)
     rulesI = process7.salida()
     #process.entrada([(1,22),(2,34),(3,2)],[(1,22),(2,22),(3,22)])


     #PROCESO 8 in:( rulesI )
     print("Proceso 8")
     process8 = Proceso08()
     process8.entrada(rulesI)
     #process8.entrada([(1, 22.0),(2, 44.0),(3, 22.0)])
     ruleset = process8.salida()


     #PROCESO 9 in: ( reglasConFamiliaridad_audio, audio )
     print("Proceso 9")
     p9 = Proceso09()
     #p9.Entrada([[15,1],[2,1],[3,1],[4,1]],[1,-1])
     p9.Entrada(ruleset)

     print(p9.Salida())
     print("--------------")


     #PROCEOS 10 in: ( proceso 9, num_Ensayo )
     print("Proceso 10", i)
 
     p10.Entrada(p9.Salida(),i)
     Endsalida = p10.Salida()
     print(p10.Salida())



if __name__ == "__main__":
    main()
     