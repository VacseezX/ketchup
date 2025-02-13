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

def nincskoltes(lista:list):
    nemKoltottek = 0
    for nap in lista:
        if nap == 0:
            nemKoltottek += 1
    return nemKoltottek

def atlagK(lista:list):
    kereset = 0
    for nap in lista:
        kereset += nap
    return round(kereset/len(lista), 2)

def legkisebb(lista:list):
    # for koltes in lista:
    #     if koltes != 0:
    #         return min(lista)
    return min(lista)

def legnagyobb(lista:list):
    return max(lista)

def osszKoltes(lista:list):
    kereset = 0
    for nap in lista:
        kereset += nap
    return kereset

honap = beolvasas(honap)
print(honap)
print("Ennyi nap volt az adott hónapban:",napok(honap))
print("Ennyi napon volt 0 a költés:",nincskoltes(honap))
print("Ennyi volt a napi átlagköltés a hónapban:",atlagK(honap))
print("A legkisebb vásárlás a hónapban",legkisebb(honap))
print("A legnagyobb vásárlás a hónapban",legnagyobb(honap))
print("A havi össz költés:",osszKoltes(honap),"Ft")