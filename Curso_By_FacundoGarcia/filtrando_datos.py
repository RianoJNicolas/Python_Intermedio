DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():

    # Utilizando List Comprehensions
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == 'python']
    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == 'Platzi']
    
    # Utilizando Funciones de Orden Superior

    ## Filter
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    ## Map
    adults = list(map(lambda worker: worker["name"], adults))

    ## Para versiones de Python menores a 3.9 y mayores a 3.5 se concatenan dos diccionarios asi:
    old_people = list(map(lambda worker: {**worker, **{"old": worker["age"] > 70}}, DATA))

    ## Para versiones de python mayores a 3.9 dos diccionarios se pueden concatenar asi:
    # old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    # for worker in all_python_devs:
    #     print(worker)

    # for worker in all_Platzi_workers:
    #     print(worker)

    # for worker in adults:
    #     print(worker)

    for worker in old_people:
        print(worker)


if __name__ == '__main__':
    run()