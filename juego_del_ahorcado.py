from ast import While
from random import randint, randrange
from operator import contains


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


def run():
    dir = "archivos/data.txt"
    word, length, word_dict, word_list = word_random(data_read(dir))
    game = True
    palabra_guiones = guiones_generator(length)

    while(game):
        print("\n")
        print("¡¡ ADIVINA LA PALABRA !!")
        print("\n")

        print(*palabra_guiones)

        letter_in = input("Ingresa una letra: ")

        list_pos = [i for i in word_dict if (letter_in == word_dict.get(i))]
        print(list_pos)
        
                  
        print("La palabra es: " + word)
        
                        
        game = False
    

if __name__ == '__main__':
    run()