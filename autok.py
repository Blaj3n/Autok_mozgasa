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
