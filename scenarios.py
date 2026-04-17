
#Liste indiquant chacun des phototypes
phototypes = [
    "Phototype Celtique - Peau très claire, Cheveux roux à blond roux",
    "Phototype Nordique - Peau claire, Cheveux blonds à brun clair",
    "Phototype Mixte - Peau claire à brun clair, Cheveux blond foncé à brun",
    "Phototype Méditerranéen - Peau brun clair / olive, Cheveux brun foncé",
    "Phototype Foncé - Peau brun foncé, Cheveux brun foncé à noir",
    "Phototype Très Foncé - Peau brun foncé à noir, Cheveux noirs"
]

#Ce petit bout de code vient de ChatGPT (lignes 16 et 17)
#Demande à l'utilisateur de sélectionner son phototype
print("\nVeuillez maintenant choisir votre phototype parmi ceux-ci :\n")
for i, p in enumerate(phototypes, 1): #on soustrait 1 car les indices de la liste commencent à 0
    print(f"{i}. {p}")

phototype_index = int(input("\nEntrez le numéro correspondant à votre phototype : ")) -1
seuil_med = [200, 250, 300, 450, 600,1000]


energie_critique = seuil_med[phototype_index]
print("L'energie critique est:", energie_critique)


