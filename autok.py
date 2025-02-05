def feladatok(szam):
    print(f"{szam}. feladat ")

# feladatok(1)

autok = []

with open("jeladas.txt", "r", encoding="utf-8") as file:
    for egysor in file:
        egysor = egysor.strip().split()
        autok.append([str(egysor[0]), int(egysor[1]),
                      int(egysor[2]), int(egysor[3])])
print(autok)

feladatok(2)

print(f"Az utolsó jeladás időpontja {autok[-1][1]}:{autok[-1][2]}, a jármű rendszáma {autok[-1][0]}")

feladatok(3)

elso_jarmu = autok[0][0]
print("Az első jármű: %s" %elso_jarmu)
print("Jeladásainak időpontjai: ", end="")

for auto in autok:
    if elso_jarmu == auto[0]:
        print(f"{auto[1]}:{auto[2]}", end=" ")
print()

feladatok(4)

idopont_ora = 6     #int(input("Kérem, adja meg az órát: "))
idopont_perc = 54   #int(input("Kérem, adja meg az percet: "))
szamlalo = 0
for auto in autok:
    if idopont_ora == auto[1] and idopont_perc == auto[2]:
        szamlalo += 1
print(f"A jeladások száma: {szamlalo}")

feladatok(5)
sebesseg = [auto[-1] for auto in autok]
gyors_jarmuvek = []
for auto in autok:
    if auto[-1] == max(sebesseg):
        gyors_jarmuvek.append(auto[0])
print(f"A legnagyobb sebesség km/h: {max(sebesseg)}")
print(f"A járművek: ", end="")
for i in range(len(gyors_jarmuvek)):
    print(gyors_jarmuvek[i], end=" ")
print("")

feladatok(6)


def perc_alakitas(ora:int, perc:int):
    return ora * 60 + perc


jarmu_rendszam = "ZVJ-638" #input("Kérem, adja meg a rendszámot: ")
if jarmu_rendszam not in [egyelem[0] for egyelem in autok]:
    print("Nem szerepel ilyen rendszám! ")
else:
    ora_perc_sebesseg = [[auto[1], auto[2], auto[-1]] for auto in autok if auto[0] == jarmu_rendszam]
    print(f"{ora_perc_sebesseg[0][0]}:{ora_perc_sebesseg[0][1]} 0.0 km ")
    kilometer = 0
    for i in range(1, len(ora_perc_sebesseg)):
        kilometer += (perc_alakitas(ora_perc_sebesseg[i][0], ora_perc_sebesseg[i][1]) -
                      perc_alakitas(ora_perc_sebesseg[i-1][0], ora_perc_sebesseg[i-1][1])) * ora_perc_sebesseg[i][-1] / 60
        print(f"{ora_perc_sebesseg[i][0]}:{ora_perc_sebesseg[i][1]} {round(kilometer, 1)} km")

feladatok(7)

rendszamok = []

for auto in autok:
    if auto[0] not in rendszamok:
        rendszamok.append(auto[0])


# # auto[0], auto[1], auto[2], auto[1], auto[2]
with open("ido.txt", "w", encoding="utf-8") as fajl:
    for rendszam in rendszamok:     # 1. eset: TLJ-509
        idopontok = []
        for auto in autok:
            if rendszam == auto[0]:
                idopontok.append(   [auto[1], auto[2]]  ) # [óra, perc] <- belső lista, második index
        # print(f"{rendszam} {idopontok[0][0]} {idopontok[0][1]} {idopontok[-1][0]} {idopontok[-1][1]}")
        fajl.write(f"{rendszam} {idopontok[0][0]} {idopontok[0][1]} {idopontok[-1][0]} {idopontok[-1][1]}\n")


# nyitunk egy fajl nevű txt-t, írni fogunk bele, TEHÁT belül kell dolgoznunk, amint kívül dolgozunk, egyből close-olja. rendszamok listát végigjárjuk, és egyesével az idopontok listánkba külön beletesszük az órákat, és a perceket. És azért szükséges a listában lista, mert az append metódus csak egy bemenetet enged, ez szükségessé teszi, hogy egy listába helyezzük a listát. Ezáltal az indexelésnél az első index az 'idopontok' listára vonatkozik, a második index az idopontokon belüli belső lista [óra, perc] - jére utal.
