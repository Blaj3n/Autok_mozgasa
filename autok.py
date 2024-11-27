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
print(f"Az első jármű: {elso_jarmu}")
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


with open("ido.txt", "w", encoding="utf-8") as fajl:
