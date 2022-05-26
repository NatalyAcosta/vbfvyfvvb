#va al primer area sucia, asi optimizar el camino
def optmizarCamino( costo, posicion, menor ):
    for i in range( posicion,menor,-1 ):
            print('redirigiendo un puesto de zona ' + str(i) + ' a posicion ' + str(i-1))
            costo+=1
            
    posicion=menor
    
    return costo, posicion

#permite encontrar la zona a cortar
def containZona( numero, zonaAlimpiar, estado ):
    keys = list(estado.keys())
    for x in zonaAlimpiar:
        if( numero == x ):
            print('Frenando maquinaria ... \n')
            print('Podando ' + keys[x-1])
            return True
        
    return False

#guardará la información de las tierras
diccionario_tierras={}

#nos ayuda a saber el trabajo que cuesta cortar
costo=0
valor=1
area = 0
registros = int(input("Ingrese el valor de registros: "))
while(area <= registros-1):
    # verificacion para poder ingresar otra tierra
    estadoLimpieza = input("Ingrese el estado de esa zona: ")
    diccionario_tierras[str(area)] = [estadoLimpieza,valor]
    area +=1
    valor +=1

posicion_cortador = input("Digite la zona en que se encuentra la maquinaria: ")
tierrasSuciasEncontradas=[]
for k, v in diccionario_tierras.items():
    if( v[0]=='1' ):
        tierrasSuciasEncontradas.append(v[1])
        
if( posicion_cortador!=tierrasSuciasEncontradas[0] ):
        costo, posicion_cortador=optmizarCamino(int(costo), int(posicion_cortador)
                                                    , int(tierrasSuciasEncontradas[0]))
        
for i in range(posicion_cortador ,tierrasSuciasEncontradas[len(tierrasSuciasEncontradas)-1]+1,+1):
        if(containZona(i, tierrasSuciasEncontradas, diccionario_tierras)):
            costo+=2
            print('Frenando maquinaria ... \n')
            print('Acelerando a otra tierra...')
        else:
            costo+=1
            #print('Acelerando a otra tierra...')
    
print('Todo se ha limpiado!')

print('Trabajo realizado es de ' + str(costo) + ' m')
