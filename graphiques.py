#GRAPHIQUES
#a) Les abcisses (variable de temps). Nous voulons isoler les valeurs entre le lever et le coucher du soleil car elles sont les plus pertinentes


import math



# 1 - CONSTANTES DEJA CALCULEES

phi = math.radians(latitude)
delta = math.radians(declinaison_s)


long_standard = utc_offset * 15



# 2 - COURBE SUR 24h



heures = []
angles = []


for t in range(heure*3600, 24 * 3600):  # 24h en secondes


   heure = t / 3600


   # heure solaire
   heure_solaire = heure + (4 * (longitude - long_standard)) / 60


   # angle horaire
   angle_horaire = 15 * (heure_solaire - 12)


   omega = math.radians(angle_horaire)


   # élévation solaire
   sin_h = (math.sin(phi) * math.sin(delta) +
            math.cos(phi) * math.cos(delta) * math.cos(omega))


   sin_h = max(-1, min(1, sin_h))  # sécurité numérique


   angle = math.degrees(math.asin(sin_h))


   heures.append(heure)
   angles.append(angle)


# 3 - CALCUL COUCHER

cos_omega = -math.tan(phi) * math.tan(delta)
cos_omega = max(-1, min(1, cos_omega))


omega = math.degrees(math.acos(cos_omega))
heure_coucher = 12 + omega / 15



x_heures = []
x_angles = []


for h, a in zip(heures, angles):


   if  h <= heure_coucher:
       x_heures.append(h)
       x_angles.append(a)


print(x_heures)

#4-ORDONNEES
#b) Angle horaire H
# On récupère les 3 valeurs du dictionnaire
latitude = countries[pays][0]
longitude = countries[pays][1]
utc_offset = countries[pays][2]

# Calcul de la longitude de référence du fuseau
long_standard = utc_offset * 15

# Conversion heure civile en heure solaire
heure_solaire = heure + (4 * (longitude - long_standard)) / 60

# 2 - angle horaire
angle_horaire = 15*(heure_solaire - 12)

#c ) l'angle d'élévation h du soleil
#conversions des mesures en radians
phi = math.radians(latitude)
delta = math.radians(declinaison_s)
omega = math.radians(angle_horaire)

sin_h = (math.sin(phi)*math.sin(delta) + math.cos(phi)*math.cos(delta)*math.cos(omega))

angle_solaire_deg = math.degrees(math.asin(sin_h))

print(f"Voici vos résultats ! Le {jour} {mois}, au pays sélectionné, à {heure}h, le Soleil se trouve à {round(angle_solaire_deg,2)} degrès")


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


while phototype_index < 0 or phototype_index > 5:
    phototype_index = int(input("Numéro invalide. Veuillez entrer un numéro entre 1 et 6 : ")) - 1

print("Parfait! Le phototype sélectionné est:",phototypes[phototype_index])

#Entrée de l'indice UV par l'utilisateur
indice_uv = float(input("Veuillez entrer l'indice UV mesuré à votre position géographique (valeur comprise entre 0 et 11, disponible dans votre application météo):"))

while indice_uv < 0 or indice_uv > 11:
     indice_uv = float(input("Indice UV invalide. Veuillez entrer une valeur comprise entre 0 et 11 : "))


#Calcul de l'irradiance totale
irradiance_totale = indice_uv * 0.025 # 1 unité d'indice UV correspond environ à 0.025 W/m²

#Liste des différents albédos selon le phototype
albedos = [0.42, 0.37, 0.32, 0.27, 0.22, 0.17]

#Conversion angle solaire de degrés vers radians
angle_solaire_rad = math.radians(angle_solaire_deg)

#Calcul de l'irradiance absorbée (sans crème solaire)
irradiance_abs_sans_creme = irradiance_totale * math.cos(angle_solaire_rad) * (1 - albedos[phototype_index])


irradiance_temps = []
for k in x_heures:
    irradiance_temps
E =


#Ici, nous avons procédé en deux étapes. Premièrement, nous avons défini un intervalle de temps allant de 0 à 24 heures,
# discrétisé en secondes. Ensuite, nous avons calculé l’angle solaire associé à chaque instant de la journée et avons stocké ces valeurs dans deux listes intermédiaires.
#Dans un second temps, nous avons appliqué un filtre en ne conservant que les valeurs de l’angle solaire supérieures ou égales à zéro.
# Cela correspond aux périodes où le Soleil est au-dessus de l’horizon, c’est-à-dire entre le lever et le coucher du Soleil.
if __name__ == "main":
    print("test")



#GRAPHIQUES
#a) Les abcisses (variable de temps). Nous voulons isoler les valeurs entre le lever et le coucher du soleil car elles sont les plus pertinentes


import math


# =========================
# 1 - CONSTANTES LOCALES
# =========================


phi = math.radians(latitude)
delta = math.radians(declinaison_s)


long_standard = utc_offset * 15


# =========================
# 2 - COURBE SUR 24h
# =========================


heures = []
angles = []


for t in range(heure*3600, 24 * 3600):  # 24h en secondes


   heure = t / 3600


   # heure solaire
   heure_solaire = heure + (4 * (longitude - long_standard)) / 60


   # angle horaire
   angle_horaire = 15 * (heure_solaire - 12)


   omega = math.radians(angle_horaire)


   # élévation solaire
   sin_h = (math.sin(phi) * math.sin(delta) +
            math.cos(phi) * math.cos(delta) * math.cos(omega))


   sin_h = max(-1, min(1, sin_h))  # sécurité numérique


   angle = math.degrees(math.asin(sin_h))


   heures.append(heure)
   angles.append(angle)


# =========================
# 3 - CALCUL LEVER / COUCHER
# =========================


cos_omega = -math.tan(phi) * math.tan(delta)
cos_omega = max(-1, min(1, cos_omega))


omega = math.degrees(math.acos(cos_omega))




heure_coucher = 12 + omega / 15


# =========================
# 4 - FILTRAGE (zone jour)
# =========================


x_heures = []
x_angles = []


for h, a in zip(heures, angles):


   if  h <= heure_coucher:
       x_heures.append(h)
       x_angles.append(a)


print(x_heures)


#Ici, nous avons procédé en deux étapes. Premièrement, nous avons défini un intervalle de temps allant de 0 à 24 heures,
# discrétisé en secondes. Ensuite, nous avons calculé l’angle solaire associé à chaque instant de la journée et avons stocké ces valeurs dans deux listes intermédiaires.
#Dans un second temps, nous avons appliqué un filtre en ne conservant que les valeurs de l’angle solaire supérieures ou égales à zéro.
# Cela correspond aux périodes où le Soleil est au-dessus de l’horizon, c’est-à-dire entre le lever et le coucher du Soleil.


