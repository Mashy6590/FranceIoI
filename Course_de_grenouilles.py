nbr_grenouilles = int(input("Saisissez le nombre de grenouilles participant à la course : "))
nbr_tours = int(input("Saisissez le nombre de tours de la course : "))

D = [0]*(nbr_grenouilles+1) #liste qui va contenir les distances des grenouilles
C = [0]*(nbr_grenouilles+1) #liste qui va compter le classement des grenouilles 

for tour in range(nbr_tours-1): #le dernier tour ne compte pas
    numero, distance = map(int, input("Saisissez le numéro de la grenouille qui saute et la distance qu'elle parcourt : ").split())
    D[numero] += distance 
    nbr_premiers = D.count(max(D))
    if nbr_premiers <= 1: #prendre en charge le cas des égalités
        indx_premier = D.index(max(D))
        C[indx_premier] += 1 
        premier = C.index(max(C))
        print(f"la grenouille numéro {premier} est strictement en tête")
    else: 
        print("il y a une égalité")
    

vainqueur = C.index(max(C))
if vainqueur == 0: #prendre en cas le charge où aucune grenouille ne se déplace 
    print(f"La grenouille numéro 1 a gagné la course")
else:
    print(f"La grenouille numéro {vainqueur} a gagné la course")
    