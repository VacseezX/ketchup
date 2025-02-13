honap = []
napokSzama = 0

def beolvasas(lista:list):
    f = open("vasarlas.csv", "r")
    lista = (f.readline().strip("\n").split(";"))
    return lista

def napok(lista:list):
    napokSzama = 0
    for napok in lista:
        napokSzama += 1
    return napokSzama

honap = beolvasas(honap)
print(honap)
napokSzama = napok(honap)
print(napokSzama)