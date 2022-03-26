def run():
    dicc = {}
    for key in range(1,101):
        if key%3!=0:
            dicc[key] = key**3
        else:
            continue   
    print(dicc)


if __name__ == '__main__':
    run()
