# -*- coding: utf-8 -*-
"""Created on Mon Nov  9 20:26:05 2020
@author: Vic-gonz
"""
import random
modelo = [1,1,1,1,1,1] 
largo = 6 
cant = 8 
selec = 3 
probabilidad = 0.2 
  
def indi(min, max):
       return[random.randint(min, max) for i in range(largo)]
  
def poblacion():
       return [indi(1,6) for i in range(cant)]
  
def calcularFit(individual):
    
    fit = 0
    for i in range(len(individual)):
        if individual[i] == modelo[i]:
            fit += 1
    return fit
  
def seleccion(pobla):
   
    puntuados = [ (calcularFit(i), i) for i in pobla] 
    puntuados = [i[1] for i in sorted(puntuados)] 
    pobla = puntuados
    
    selected =  puntuados[(len(puntuados)-selec):]
  
      
    for i in range(len(pobla)-selec):
        punto = random.randint(1,largo-1) 
        padre = random.sample(selected, 2) 
          
        pobla[i][:punto] = padre[0][:punto] 
        pobla[i][punto:] = padre[1][punto:]
  
    return pobla
  
def mutacion(pobla):
    
    for i in range(len(pobla)-selec):
        if random.random() <= probabilidad: 
            punto = random.randint(0,largo-1) 
            nuevoValor = random.randint(1,9) 
  
           
            while nuevoValor == pobla[i][punto]:
                nuevoValor = random.randint(1,9)
  
            pobla[i][punto] = nuevoValor
  
    return pobla
      
print("Modelo: %s"%(modelo)) 
pobla = poblacion()
print("Poblacion Inicial: %s"%(pobla)) 
  
for i in range(100):
    pobla = seleccion(pobla)
    pobla = mutacion(pobla)
    
print("Poblacion Final: %s"%(pobla)) 



