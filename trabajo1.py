import random

    # Diccionario con las categorias para elegir 

diccionario = {

    "lenguajes": [
        "python",
        "java",
        "pascal",
        "html",
         ],

    "electrodomesticos": [
        "microondas",
        "heladera",
        "lavarropas"
    ]
}
    # Elijo categoria y cuento la cantidad de palabras por categoria
categoria = ""

while not categoria:
    numCat = input("elegí categoria: 1(lenguajes), 2(electrodomesticos): ")
    if (numCat == "1"):
        categoria = "lenguajes"
    elif (numCat == "2"):
        categoria = "electrodomesticos"
    else:
        print("Categoria No Valida")

palabras = len(diccionario[categoria])

# Elijo 1 palabra sin repetir como str  
palabra_actual = random.sample(diccionario[categoria], palabras)


termine = "no"

# Mientras no termine y no me quede sin palabras sigo jugando

while (termine == "no") and (palabras > 0):
    
    
    # Elimino la palabra de la lista para que no se repita 
    word = palabra_actual.pop()
    palabras -= 1

    guessed = []
    attempts = 6
    puntos = int(0)

    print (word)

    print("¡Bienvenido al Ahorcado!")
    print()

    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
             progress += letter + " "
            else:
                progress += "_ "
        print(progress)
        # Verificar si el jugador ya adivinó la palabra completa
        # Modifico el puntaje 
        # Al finalizar pregunto si quiere seguir jugando
        if "_" not in progress:
            puntos += 6
            print("¡Ganaste!")
            print(f"Puntuacion: {puntos}/6")
            termine = input("Terminaste de jugar? (si o no) ")
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")
        # Cuando se ingresa mas de una letra imprime Entrada No Valida y vuelve a pedir otra letra
        if (len(letter) > 1):
            print("Entrada No Valida")
        elif letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            puntos -= 1
            print("Esa letra no está en la palabra.")

        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        puntos = 0
        print(f"Puntuacion: {puntos}/6")
        termine = input("Terminaste de jugar? (1 = no, 2 = si) ")

if palabras == 0:
    print ("No hay mas palabras para esta categoria")
