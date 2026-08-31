#from traceback import print_tb



print("-------------titulo: FAROL 7 — RESGATE EM ÓRBITA----------")
print("\n Narrativa:ARA precisa conduzir uma equipe de resgate, recuperar tripulantes e religar três módulos críticos antes que o oxigênio e a integridade estrutural acabem.  ")


print("\nVitoria: Até o final do turno 20, manter oxigênio e integridade acima de zero, religar os 3 módulos (Energia, Comunicações eSuporte de Vida), resgatar os 4 tripulantes e chegar à Doca.       ")
print("\nDerrota: A missão termina em derrota se oxigênio chegar a 0, integridade chegar a 0 ou o turno 20 terminar sem que todos os objetivos de vitória tenham sido cumpridos.")
print("\n 1 Ver status")
print("\n 2 Explorar corredor")
print("\n 3 Reparar")
print("\n 4 Descansa")
print("\n 5 Ver objetivos")
print("\n 0 Sair")
turno=1
oxigenio=100
integridade= 100
energia =30
tripulantes_resgatados =0
modulos_religados = 0
local_atual = ("Doca")
nome=input("\nDigite seu nome: ")
if nome == "":
    print("Opção inválida")
op=int(input("celecione uma opção: "))


   

   
if op==1:
 print(f"oxigenio :{oxigenio}")
 print(f"integridade: {integridade}")
 print(f"energia:{energia}")
 print(f"tripulantes resgatados: {tripulantes_resgatados}")
 print(f"\n modulos religados:{modulos_religados}")
 print(f"local atual:{local_atual}")
 print(f"turnos{turno}")
      
       
       

elif op==2:
        print("\niniciar exploração")
        oxigenio =oxigenio -  5
        integridade =integridade-2
        turno=turno +1
    
    
       

    
        

       
   
elif op==3:
            
        
         
         
         if energia >=5:
            print("\niniciar reparo")
            energia = energia-5
            integridade =integridade+10
            turno=turno+1

         else:
          print("n pode ser realizado sua energia esta baixa")
    


        
        
elif op==4:
        print("\niniciar descanço")
        energia=energia+5
        turno=turno+1
        

        

elif op==5:

        print("resgatar tripulantes")
        print("reeligar modulos ")
       
elif op==0:
  print("\nsaindo")
elif turno >=30:
        turno ==30
        print ("vc atingiu o limite de turnos")
     

        
elif integridade >=100:
         integridade==100
            
elif energia >=30:
          energia==30  
else:
    print("n temos essa opção ")    
    
   
        

