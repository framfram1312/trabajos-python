



def calcularPuntajes (rondas: list):


    puntosTotales = {}

    puntosMaximos = {}

    rondasGanadas = {}

    numRonda = 1

    # recorro cada ronda
    for ronda in rondas:

        # Imprimo la ronda actual y la categoria
        categoriaActual = ronda['theme']
        print ('------------------------------------')
        print()
        print (f'ronda:',numRonda, categoriaActual)
        print()

        # tomo los puntajes de la ronda actual
        puntajes_ronda = ronda['scores']

        numRonda += 1

        resultadosRonda = []

        # participantes queda con los nombres de cada uno y jueces queda con los puntajes de los 3 jueces por ronda
        for participantes, jueces in puntajes_ronda.items():
            
            # sumo los 3 puntajes de los jueces
            puntos = sum(jueces.values())

            # guardo los resultados en mi lista de tuplas
            resultadosRonda.append((participantes, puntos))

            # sumo los puntajes en el diccionario de puntos por participante. Los inicializo si no existen
            puntosTotales[participantes] = puntosTotales.get(participantes, 0) + puntos

            # actualizo el maximo por participante
            if (puntos > puntosMaximos.get(participantes, 0)):
                puntosMaximos[participantes] = puntos

        # ordeno los participantes por su puntaje
        resultadosRonda.sort(key=lambda x: x[1], reverse=True)
        
        # imprimo la ronda ordenada por puntaje
        for i in range(len(resultadosRonda)):
            participanteAct, puntajeAct = resultadosRonda[i]
            if (i == 0):
                # imprimo el ganador y actualizo las rondas ganadas
                print(f'Ganador/a! nombre: {participanteAct}, puntaje: {puntajeAct}')
                rondasGanadas[participanteAct] = rondasGanadas.get(participanteAct, 0) + 1
            else :
                # imprimo a todos los demas
                print(f'nombre: {participanteAct}, puntaje: {puntajeAct}')

    print()
    print('---------------------------------------')
    print('tabla de posiciones final')
    print('---------------------------------------')
    print()

    # armo una lista para poder acomadar las posiciones 
    tabla = armadoDeTabla (puntosTotales, puntosMaximos, rondasGanadas, cantRondas = len(rondas))
    for i in range(len(tabla)):
        x = tabla[i]
        print (f'Lugar numero {i+1}: nombre: {x['nombre']} | puntaje total: {x['puntaje total']} | puntaje maximo: {x['puntaje maximo']} | promedio: {x['promedio']} | rondas ganadas: {x['rondas ganadas']} |')
        print ('---------------------------------------------------------------------------------------------------------------')

    return tabla

def armadoDeTabla (puntajes,maximos,rondas: dict, cantRondas: int): 
    tabla = []

    for nombre, total in puntajes.items():

        # guardo en la lista todos los participantes con sus datos
        participante = {
            'nombre': nombre,
            'puntaje total': total,
            'promedio': total / cantRondas,
            'puntaje maximo': maximos[nombre],
            'rondas ganadas': rondas.get(nombre, 0)
        }
        
        tabla.append(participante)

    # ordeno la tabla de mayor a menor
    tabla.sort(key=lambda x: x['puntaje total'], reverse=True)

    return tabla