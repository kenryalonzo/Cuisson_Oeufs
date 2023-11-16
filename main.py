import time
import beepy

def point_By_Sec():
    for i in range(10):
        time.sleep(1)
        print(".", end="", flush=True)

def timer(x):
    d = x * 60
    min = d // 60
    sec = d - min * 60

    print("Cuisson en cours", end="", flush=True)
    point_By_Sec()
    print("")

    while d > 0:
        d -= 10
        min = d // 60
        sec = d - min * 60

        if min == 0 and sec == 0:
            print(f"Durée restante : {min:02}:{sec:02}", end="", flush=True)
            print("")
            break
        else:
            print(f"Durée restante : {min:02}:{sec:02}", end="", flush=True)
            point_By_Sec()
            print("")

    print("Cuisson terminée!")
    beepy.beep(sound="ping")


print("Cuisson des œufs")
print("-----------------")
print("a) Œufs à la coque (3 min)")
print("b) Œufs mollets (6 min)")
print("c) Œufs durs (9 min)")

choix = input("Entrez votre choix ici : ")

if choix == 'a':
    timer(3)
elif choix == 'b':
    timer(6)
elif choix == 'c':
    timer(9)
else:
    print("Veuillez entrer un choix valide compris entre 'a' et 'c'")