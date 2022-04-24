from ast import While
from random import randint, randrange
from operator import contains
import os
import string

def data_read(dir):
    with open(dir,"r",encoding="utf-8") as f:
        lista = [line for line in f]
    return lista


def word_random(lista):
    length = len(lista)
    pos = randrange(0,length)
    word = lista[pos].replace("\n","")
    word_dict = dict(enumerate(word))
    word_list = [letra for letra in word]
    return word, len(word), word_dict, word_list


def guiones_generator(quantity):
    lista = []
    for i in range (0,quantity):
        lista.append("_")
    return lista


def get_points(points,level,tries,letterGuess,wordGuess):
    try:
        if (level == 1):
            if ((wordGuess) and (tries == 1)):
                p = points + 100

            elif ((wordGuess) and (tries == 2)):
                p = points + 80

            elif ((wordGuess) and (tries == 3)):
                p = points + 50
            
            elif ((wordGuess) and (tries == 4)):
                p = points + 20
            
            elif ((letterGuess)):
                p = points + 10
            
            else:
                p = points

    except Exception as e:
        print(e)

    return p

def run():
    dir = "archivos/data.txt"
    word, length, word_dict, word_list = word_random(data_read(dir))
    game = True
    level = 0
    points = 0
    tries_player = 0
    palabra_guiones = guiones_generator(length)

    while(game):
        level = level + 1
        wordGuess = False
        
        while (wordGuess==False):
            print("\n")
            print("¡¡ ADIVINA LA PALABRA !!")
            print("\n")
            print("Nivel -> {}".format(str(level)))
            print("Puntos -> {}".format(str(points)))
            print(*palabra_guiones)

            tries_player = tries_player + 1
            letter_in = input("Ingresa una letra: ")

            list_pos = [i for i in word_dict if (letter_in == word_dict.get(i))]
                    
            for i in list_pos:
                palabra_guiones[i] = letter_in

            if (len(list_pos) > 0):
                letterGuess = True
            else:
                letterGuess = False   
            
            palabra_guiones_str = "".join(palabra_guiones)
            os.system("clear")

            if word == palabra_guiones_str:
                wordGuess = True
                os.system("clear") 

            points = get_points(points,level,tries_player,letterGuess,wordGuess)

        print("HAS GANADO, LA PALABRA ERA: " + word)               
        game = False


if __name__ == '__main__':
    run()