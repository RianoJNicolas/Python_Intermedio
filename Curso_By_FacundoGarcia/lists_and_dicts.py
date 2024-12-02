def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Johan", "lastname": "Riano"}

    super_list = [
        {"firstname": "Johan", "lastname": "Riano"},
        {"firstname": "Nicolas", "lastname": "Torres"},
        {"firstname": "Stephanie", "lastname": "Bratt"},
        {"firstname": "Gladys", "lastname": "Torres"},
        {"firstname": "Rigoberto", "lastname": "Riano"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5,6,7,8,9],
        "integer_nums": [-3,-2,-1,0,1,2,3],
        "floating_nums": [1.2,2.5,3.5,8.5]
    }

    print("Elementos del Super diccionario: \n")
    for key, value in super_dict.items():
        print(key,"-",value)

    for item in super_list:
        for key, value in item.items():
            print(key,"-",value)


if __name__ == '__main__':
    run()