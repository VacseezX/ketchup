haviKoltes = []

def beolvasas(lista:list):
    f = open("vasarlas.csv", "r")
    lista.append(f.readline().strip("\n").split(";"))
    return lista

haviKoltes = beolvasas(haviKoltes)
print(haviKoltes)
