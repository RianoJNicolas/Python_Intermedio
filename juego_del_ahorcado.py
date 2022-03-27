from ast import While
from random import randint, randrange
from operator import contains


def data_read(dir):
    with open(dir,"r",encoding="utf-8") as f:
        lista = [linea for linea in f]
    return lista


def word_random(lista):
    longitud = len(lista)
    pos = randrange(0,longitud)
    word = lista[pos].replace("\n","")
    word_dict = dict(enumerate(word))
    word_list = [letra for letra in word]
    return word, len(word), word_dict, word_list


def run():
    dir = "archivos/data.txt"
    word, longitud, diccionario, lista = word_random(data_read(dir))
    game = True
    
    while(game):
        letra = input("Ingresa una letra: ")

        print(word) 
        print(diccionario)
        game = False
    

if __name__ == '__main__':
    run()