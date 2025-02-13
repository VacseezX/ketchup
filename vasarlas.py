honap = []
napokHonapban = 0
nemKoltes = 0
atlagKoltes = 0

def beolvasas(lista:list):
    intLista = []
    f = open("vasarlas.csv", "r")
    lista = (f.readline().strip("\n").split(";"))
    for i in lista:
        intLista.append(int(i))
    return intLista

def napok(lista:list):
    napokSzama = 0
    for nap in lista:
        napokSzama += 1
    return napokSzama

def nincsKoltes(lista:list):
    nemKoltottek = 0
    for nap in lista:
        if nap == 0:
            nemKoltottek += 1
    return nemKoltottek

def atlagKoltes(lista:list):
    koltes = 0
    for nap in lista:
        koltes += nap
    return round(koltes/len(lista), 2)

def legkisebb(lista:list):
    legkisebbKoltes = lista[0]
    for nap in lista:
        if nap < legkisebbKoltes and nap != 0:
            legkisebbKoltes = nap
    return legkisebbKoltes

def legnagyobb(lista:list):
    return max(lista)

def osszKoltes(lista:list):
    koltes = 0
    for nap in lista:
        koltes += nap
    return koltes

def sorozat(lista:list):
    koltesNelkNapokSzama = 0
    leghosszabbSorozat = 0
    for nap in lista:
        if nap == 0:
            koltesNelkNapokSzama += 1
            if koltesNelkNapokSzama > leghosszabbSorozat:
                leghosszabbSorozat = koltesNelkNapokSzama
        else:
            koltesNelkNapokSzama = 0
    return leghosszabbSorozat

honap = beolvasas(honap)
print(honap)
print("Ennyi nap volt az adott hónapban:",napok(honap))
print("Ennyi napon volt 0 a költés:",nincsKoltes(honap))
print("Ennyi volt a napi átlagköltés a hónapban:",atlagKoltes(honap),"Ft")
print("A legkisebb vásárlás a hónapban",legkisebb(honap),"Ft")
print("A legnagyobb vásárlás a hónapban",legnagyobb(honap),"Ft")
print("A havi össz költés:",osszKoltes(honap),"Ft")
print("Sorozatban a legtöbb nap költés nélkül:",sorozat(honap))