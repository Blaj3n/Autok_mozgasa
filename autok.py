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
