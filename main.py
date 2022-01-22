'''
3.1 Feladat
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja, hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! 
A program tartalmazza a függvény hívását is!
'''
def harommal_oszthatok(n, *args):
    num = 0
    for i in args:
        if i % 3 == 0:
            num += 1
    return num

print(harommal_oszthatok(1,2,3,4,5,6,7,8,9))
