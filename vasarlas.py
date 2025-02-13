honap = []
napokHonapban = 0
nemKoltes = 0
atlagKoltes = 0

def beolvasas(lista:list):
    f = open("vasarlas.csv", "r")
    lista = (f.readline().strip("\n").split(";"))
    return lista

def napok(lista:list):
    napokSzama = 0
    for nap in lista:
        napokSzama += 1
    return napokSzama

def nincskoltes(lista:list):
    nemKoltottek = 0
    for nap in lista:
        if nap == "0":
            nemKoltottek += 1
    return nemKoltottek

def atlagK(lista:list):
    napokSzama = 0
    kereset = 0
    for nap in lista:
        napokSzama += 1
        kereset += int(nap)
    return round(kereset/napokSzama, 2)

honap = beolvasas(honap)
print(honap)
napokHonapban = napok(honap)
print(napokHonapban)
nemKoltes = nincskoltes(honap)
print(nemKoltes)
atlagKoltes = atlagK(honap)
print(atlagKoltes)