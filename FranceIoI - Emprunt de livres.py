nbr_livres, nbr_jours = map(int, input("Saisissez le nombre de livres et de jours : ").split())

L = [0]*nbr_livres

for jour in range(nbr_jours):
    nbr_clients = int(input("Saisissez le nombre de clients : "))
    for elmts in range(len(L)):
        if L[elmts]:
            L[elmts] -= 1
    for client in range(nbr_clients):
        indx = int(input("Saisissez l'indice du livre que vous souhaitez emprunter : "))
        duree = int(input("Saisissez la duree de l'emprunt : "))
        if L[indx] == 0:
            print(1)
            L[indx] = duree
        else:
            print(0)