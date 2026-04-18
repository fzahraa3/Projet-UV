import math
import matplotlib.pyplot as plt
import numpy as np
#Coordonnées terrestres des pays (prises directement d'Internet )
countries = {
    "afghanistan": (33.0, 65.0, 4.5),
    "afrique du sud": (-30.0, 25.0, 2.0),
    "albanie": (41.0, 20.0, 1.0),
    "algérie": (28.0, 3.0, 1.0),
    "allemagne": (51.0, 9.0, 1.0),
    "andorre": (42.5, 1.5, 1.0),
    "angola": (-12.5, 18.5, 1.0),
    "antigua-et-barbuda": (17.1, -61.8, -4.0),
    "arabie saoudite": (25.0, 45.0, 3.0),
    "argentine": (-34.0, -64.0, -3.0),
    "arménie": (40.0, 45.0, 4.0),
    "australie": (-25.0, 133.0, 9.5),
    "autriche": (47.3, 13.3, 1.0),
    "azerbaïdjan": (40.5, 47.5, 4.0),
    "bahamas": (24.3, -76.0, -5.0),
    "bahreïn": (26.0, 50.5, 3.0),
    "bangladesh": (24.0, 90.0, 6.0),
    "barbade": (13.2, -59.5, -4.0),
    "belgique": (50.8, 4.5, 1.0),
    "belize": (17.2, -88.7, -6.0),
    "bénin": (9.5, 2.2, 1.0),
    "bhoutan": (27.5, 90.5, 6.0),
    "biélorussie": (53.0, 28.0, 3.0),
    "birmanie": (22.0, 98.0, 6.5),
    "bolivie": (-17.0, -65.0, -4.0),
    "bosnie-herzégovine": (44.0, 18.0, 1.0),
    "botswana": (-22.0, 24.0, 2.0),
    "brésil": (-10.0, -55.0, -3.0),
    "brunei": (4.5, 114.7, 8.0),
    "bulgarie": (43.0, 25.0, 2.0),
    "burkina faso": (13.0, -2.0, 0.0),
    "burundi": (-3.5, 30.0, 2.0),
    "cambodge": (13.0, 105.0, 7.0),
    "cameroun": (6.0, 12.0, 1.0),
    "canada": (56.0, -106.0, -6.0),
    "cap-vert": (16.0, -24.0, -1.0),
    "chili": (-30.0, -71.0, -3.0),
    "chine": (35.0, 103.0, 8.0),
    "chypre": (35.0, 33.0, 2.0),
    "colombie": (4.0, -72.0, -5.0),
    "comores": (-12.2, 44.5, 3.0),
    "congo": (-1.0, 15.0, 1.0),
    "corée du nord": (40.0, 127.0, 9.0),
    "corée du sud": (36.0, 128.0, 9.0),
    "costa rica": (10.0, -84.0, -6.0),
    "côte d'ivoire": (8.0, -5.0, 0.0),
    "croatie": (45.1, 15.2, 1.0),
    "cuba": (21.5, -80.0, -5.0),
    "danemark": (56.0, 10.0, 1.0),
    "djibouti": (11.5, 43.0, 3.0),
    "dominique": (15.4, -61.3, -4.0),
    "égypte": (26.0, 30.0, 2.0),
    "émirats arabes unis": (24.0, 54.0, 4.0),
    "équateur": (-1.5, -78.0, -5.0),
    "érythrée": (15.0, 39.0, 3.0),
    "espagne": (40.0, -4.0, 1.0),
    "estonie": (59.0, 26.0, 2.0),
    "eswatini": (-26.5, 31.5, 2.0),
    "états-unis": (39.0, -98.0, -7.0),
    "éthiopie": (9.0, 40.0, 3.0),
    "fidji": (-17.8, 178.0, 12.0),
    "finlande": (64.0, 26.0, 2.0),
    "france": (46.0, 2.0, 1.0),
    "gabon": (-1.0, 11.8, 1.0),
    "gambie": (13.4, -15.3, 0.0),
    "géorgie": (42.0, 43.5, 4.0),
    "ghana": (8.0, -2.0, 0.0),
    "grèce": (39.0, 22.0, 2.0),
    "grenade": (12.1, -61.7, -4.0),
    "guatemala": (15.5, -90.3, -6.0),
    "guinée": (10.0, -10.0, 0.0),
    "guinée-bissau": (12.0, -15.0, 0.0),
    "guinée équatoriale": (1.6, 10.5, 1.0),
    "guyana": (5.0, -59.0, -4.0),
    "haïti": (19.0, -72.5, -5.0),
    "honduras": (15.0, -86.5, -6.0),
    "hongrie": (47.0, 20.0, 1.0),
    "îles marshall": (7.1, 171.0, 12.0),
    "îles salomon": (-9.6, 160.2, 11.0),
    "inde": (20.0, 77.0, 5.5),
    "indonésie": (-5.0, 120.0, 8.0),
    "irak": (33.0, 44.0, 3.0),
    "iran": (32.0, 53.0, 3.5),
    "irlande": (53.0, -8.0, 0.0),
    "islande": (65.0, -18.0, 0.0),
    "israël": (31.5, 34.8, 2.0),
    "italie": (42.5, 12.5, 1.0),
    "jamaïque": (18.1, -77.3, -5.0),
    "japon": (36.0, 138.0, 9.0),
    "jordanie": (31.0, 36.0, 3.0),
    "kazakhstan": (48.0, 68.0, 5.0),
    "kenya": (1.0, 38.0, 3.0),
    "kirghizistan": (41.0, 75.0, 6.0),
    "kiribati": (1.8, 173.0, 13.0),
    "koweït": (29.5, 47.5, 3.0),
    "laos": (18.0, 105.0, 7.0),
    "lesotho": (-29.5, 28.5, 2.0),
    "lettonie": (57.0, 25.0, 2.0),
    "liban": (33.8, 35.8, 2.0),
    "libéria": (6.5, -9.5, 0.0),
    "libye": (26.0, 17.0, 2.0),
    "liechtenstein": (47.2, 9.5, 1.0),
    "lituanie": (55.0, 24.0, 2.0),
    "luxembourg": (49.8, 6.1, 1.0),
    "macédoine du nord": (41.6, 21.7, 1.0),
    "madagascar": (-20.0, 47.0, 3.0),
    "malaisie": (2.5, 112.5, 8.0),
    "malawi": (-13.5, 34.0, 2.0),
    "maldives": (3.2, 73.0, 5.0),
    "mali": (17.0, -4.0, 0.0),
    "malte": (35.9, 14.5, 1.0),
    "maroc": (32.0, -6.0, 1.0),
    "maurice": (-20.3, 57.5, 4.0),
    "mauritanie": (20.0, -12.0, 0.0),
    "mexique": (23.0, -102.0, -6.0),
    "micronésie": (6.9, 158.2, 11.0),
    "moldavie": (47.0, 29.0, 2.0),
    "monaco": (43.7, 7.4, 1.0),
    "mongolie": (46.0, 105.0, 8.0),
    "monténégro": (42.5, 19.3, 1.0),
    "mozambique": (-18.5, 35.0, 2.0),
    "myanmar": (22.0, 98.0, 6.5),
    "namibie": (-22.0, 17.0, 2.0),
    "nauru": (-0.5, 166.9, 12.0),
    "népal": (28.0, 84.0, 5.75),
    "nicaragua": (13.0, -85.0, -6.0),
    "niger": (16.0, 8.0, 1.0),
    "nigeria": (9.0, 8.0, 1.0),
    "norvège": (62.0, 10.0, 1.0),
    "nouvelle-zélande": (-41.0, 174.0, 12.0),
    "oman": (21.0, 57.0, 4.0),
    "ouganda": (1.0, 32.0, 3.0),
    "ouzbékistan": (41.0, 64.0, 5.0),
    "pakistan": (30.0, 70.0, 5.0),
    "palaos": (7.5, 134.5, 9.0),
    "palestine": (31.9, 35.2, 2.0),
    "panama": (9.0, -80.0, -5.0),
    "papouasie-nouvelle-guinée": (-6.0, 147.0, 10.0),
    "paraguay": (-23.0, -58.0, -4.0),
    "pays-bas": (52.5, 5.7, 1.0),
    "pérou": (-10.0, -76.0, -5.0),
    "philippines": (13.0, 122.0, 8.0),
    "pologne": (52.0, 20.0, 1.0),
    "portugal": (39.5, -8.0, 0.0),
    "qatar": (25.3, 51.2, 3.0),
    "république centrafricaine": (7.0, 21.0, 1.0),
    "république démocratique du congo": (-2.5, 23.5, 1.5),
    "république dominicaine": (19.0, -70.7, -4.0),
    "roumanie": (46.0, 25.0, 2.0),
    "royaume-uni": (55.0, -3.0, 0.0),
    "russie": (60.0, 100.0, 7.0),
    "rwanda": (-2.0, 30.0, 2.0),
    "saint-christophe-et-niévès": (17.3, -62.7, -4.0),
    "saint-marin": (43.9, 12.5, 1.0),
    "saint-vincent-et-les-grenadines": (13.2, -61.2, -4.0),
    "sainte-lucie": (13.9, -60.9, -4.0),
    "samoa": (-13.8, -172.1, 13.0),
    "sao tomé-et-principe": (0.2, 6.7, 0.0),
    "sénégal": (14.0, -14.0, 0.0),
    "serbie": (44.0, 21.0, 1.0),
    "seychelles": (-4.6, 55.5, 4.0),
    "sierra leone": (8.5, -11.5, 0.0),
    "singapour": (1.3, 103.8, 8.0),
    "slovaquie": (48.7, 19.7, 1.0),
    "slovénie": (46.1, 14.8, 1.0),
    "somalie": (5.0, 46.0, 3.0),
    "soudan": (15.0, 30.0, 2.0),
    "soudan du sud": (7.0, 30.0, 2.0),
    "sri lanka": (7.0, 81.0, 5.5),
    "suède": (62.0, 15.0, 1.0),
    "suisse": (47.0, 8.0, 1.0),
    "suriname": (4.0, -56.0, -3.0),
    "syrie": (35.0, 38.0, 3.0),
    "tadjikistan": (39.0, 71.0, 5.0),
    "taïwan": (23.5, 121.0, 8.0),
    "tanzanie": (-6.0, 35.0, 3.0),
    "tchad": (15.0, 19.0, 1.0),
    "thaïlande": (15.0, 100.0, 7.0),
    "timor oriental": (-8.8, 125.7, 9.0),
    "togo": (8.0, 1.2, 0.0),
    "tonga": (-21.2, -175.2, 13.0),
    "trinité-et-tobago": (10.5, -61.2, -4.0),
    "tunisie": (34.0, 9.0, 1.0),
    "turkménistan": (39.0, 59.0, 5.0),
    "turquie": (39.0, 35.0, 3.0),
    "tuvalu": (-8.5, 179.2, 12.0),
    "ukraine": (49.0, 32.0, 2.0),
    "uruguay": (-33.0, -56.0, -3.0),
    "vanuatu": (-16.0, 167.0, 11.0),
    "vatican": (41.9, 12.4, 1.0),
    "venezuela": (7.0, -66.0, -4.0),
    "vietnam": (16.0, 108.0, 7.0),
    "yémen": (15.0, 48.0, 3.0),
    "zambie": (-15.0, 30.0, 2.0),
    "zimbabwe": (-20.0, 30.0, 2.0)
}
pays = input("Assistant : Bonjour ! Je vais vous aider à calculer l'élévation exacte du Soleil. Pour commencer, dans quel pays souhaitez-vous mesurer l'exposition ? : ").lower()


#Choix du pays par l'utilisateur
while pays not in countries:
    print("Ce pays n'existe pas. Veuillez réessayer")
    pays = input("Entrez le pays : ")

print(f"Assistant : Très bien! j'utiliserai ses coordonnées moyennes de latitude et de longitude.")

latitude = countries[pays][0]
longitude = countries[pays][1]

#année
annee = input("S'agit-il d'une année bissextile ? (oui/non) : ")

#Entrée de la date par l'utilisateur (heure et mois)

if annee.lower()== "oui" :
    repertoire_mois = {
        "janvier": 0,
        "fevrier": 31,
        "mars": 60,
        "avril": 91,
        "mai": 121,
        "juin": 152,
        "juillet": 182,
        "aout": 213,
        "septembre": 244,
        "octobre": 274,
        "novembre": 305,
        "decembre": 335,
    }
elif annee.lower() == "non" :
    repertoire_mois = {
        "janvier": 0,
        "fevrier": 31,
        "mars": 59,
        "avril": 90,
        "mai": 120,
        "juin": 151,
        "juillet": 181,
        "aout": 212,
        "septembre": 243,
        "octobre": 273,
        "novembre": 304,
        "decembre": 334,
    }

mois = input("Entendu. À quel mois de l'année faisons-nous cette mesure ?")

#Nombre de jour à partir du premier janvier
#b) limites pour le mois

while mois.lower() not in repertoire_mois:
    mois = input("Ce mois n'existe pas, veuillez recommencer. Entrez le mois :")


mois_31 = ["janvier", "mars", "mai", "juillet", "aout", "octobre", "decembre"]
mois_30 = ["avril", "juin", "septembre", "novembre"]

if mois.lower() in mois_31:
    max_jour = 31

elif mois.lower() in mois_30:
    max_jour = 30

else:  # concernant février seulement
    if annee.lower() == "oui":
        max_jour = 29
    else:
        max_jour = 28

#b) limites pour le jour
jour = int(input("Et quel jour de ce mois? : "))

while jour < 1 or jour > max_jour:
    jour = int(input("Jour invalide pour ce mois, recommencez : "))

nombre_jour = repertoire_mois[mois.lower()] + jour

#c) limites pour l'heure

heure = int(input("Veuillez entrer une heure de la journée entre 0h et 23h : "))
while heure < 0 or heure >= 24 :
    heure = int(input("Cette heure n'existe pas, veuillez recommencer. Entrez une heure de la journée entre 0h et 23h : "))


#CALCUL DE L'ANGLE SOLAIRE (l'entièreté des calculs suivants ont été verifiés par un prof du département de physique)
#a) inclinaison solaire

angle_deg = (360/365)*(nombre_jour - 81)
angle_rad = math.radians(angle_deg)
declinaison_s = 23.44*math.sin(angle_rad)

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


#Conditions pour l'utilisation de la crème solaire

SPF_MIN = 30 #la valeur de SPF minimale recommandé est 30

# Question crème solaire
creme_solaire = input("Utilisez-vous de la crème solaire ? (oui/non) : ").lower()

while creme_solaire not in ["oui", "non"]:
    creme_solaire = input("Réponse invalide. Veuillez répondre par 'oui' ou 'non' : ").lower()

if creme_solaire == "oui":
        SPF = int(input("Entrez le facteur de protection solaire (SPF) :"))
        irradiance_abs_avec_creme = irradiance_abs_sans_creme / SPF
        difference = irradiance_abs_sans_creme - irradiance_abs_avec_creme
        print(f"\nSuper ! Avec votre crème solaire de SPF {SPF}, l'intensité des UV reçue est réduite de {round(difference, 3)} W/m².")
        print(f"\nLe soleil frappe donc votre peau avec une intensité d'environ {round(irradiance_abs_avec_creme,3)} W/m².")


elif creme_solaire == "non":
    irradiance_spf_min = irradiance_abs_sans_creme / SPF_MIN
    difference = irradiance_abs_sans_creme - irradiance_spf_min
    print(f"\nSi vous aviez appliqué une crème solaire de SPF {SPF_MIN}, l'intensité des UV aurait été réduite de {round(difference, 3)} W/m²! Pas mal, non ?")
    print(f"Sans crème, le soleil frappe actuellement votre peau avec une intensité de {round(irradiance_abs_sans_creme, 3)} W/m².")




import matplotlib.pyplot as plt

#graphique energie selon temps

temps = np.arange(1,25)

#energie
energie = irradiance_abs_sans_creme * temps



#GRAPHIQUES
#a) Les abcisses (variable de temps). Nous voulons isoler les valeurs entre le lever et le coucher du soleil car elles sont les plus
# pertinentes
# 1 - CONSTANTES LOCALES

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


# =========================
# 3 - CALCUL LEVER / COUCHER


cos_omega = -math.tan(phi) * math.tan(delta)
cos_omega = max(-1, min(1, cos_omega))

omega = math.degrees(math.acos(cos_omega))

heure_coucher = 12 + omega / 15


# 4 - FILTRAGE (zone jour)
# =========================


x_heures = []
x_angles = []


for h, a in zip(heures, angles):


   if  h <= heure_coucher:
       x_heures.append(h)
       x_angles.append(a)

#Ici, nous avons procédé en deux étapes. Premièrement, nous avons défini un intervalle de temps allant de 0 à 24 heures,
# discrétisé en secondes. Ensuite, nous avons calculé l’angle solaire associé à chaque instant de la journée et avons stocké ces valeurs dans deux listes intermédiaires.
#Dans un second temps, nous avons appliqué un filtre en ne conservant que les valeurs de l’angle solaire supérieures ou égales à zéro.
# Cela correspond aux périodes où le Soleil est au-dessus de l’horizon, c’est-à-dire entre le lever et le coucher du Soleil.

#CALCUL IRRADIANCE  (en fonction du temps)


# 1. On crée une liste vide pour stocker nos résultats
irradiances_par_seconde = []
irradiance_max = indice_uv * 0.025  # Puissance max au zénith

# 2. On parcourt la liste des angles que tu as déjà calculée
for i in range(len(x_angles)):                     #Ici nous avions deja creer une liste avec tt les ngle de la journée. on l'utilise pr retrouver l'irradiance
    angle_actuel = x_angles[i]

    # Si le soleil est au-dessus de l'horizon
    if angle_actuel > 0:
        # On calcule le sinus de l'angle (en radians)
        sin_h = math.sin(math.radians(angle_actuel))

        # On calcule l'irradiance pour cette seconde précise
        irr_inst = irradiance_max * sin_h
        irradiances_par_seconde.append(irr_inst)
    else:
        # Si le soleil est couché, l'irradiance est de 0
        irradiances_par_seconde.append(0.0)


#LISTE POUR L'ÉNERGIE


# LISTE POUR L'ÉNERGIE (Ordonnées pour le graphique)
energie_cumulee = []
somme_temporaire = 0.0

# On utilise range(len(...)) pour parcourir l'indice k
for k in range(len(irradiances_par_seconde)):
    # On ajoute l'irradiance de la seconde actuelle à notre total
    # Énergie = Irradiance * 1 seconde, donc on ajoute juste la valeur
    somme_temporaire = somme_temporaire + irradiances_par_seconde[k]

    # On ajoute ce cumul dans notre liste d'ordonnées
    energie_cumulee.append(somme_temporaire)

# Maintenant tu as tes deux listes pour ton graphique :
# Abscisses (X) : x_heures
# Ordonnées (Y) : energie_cumulee

print("Ta liste d'énergie est prête pour le graphique !")

import matplotlib.pyplot as plt

plt.plot(x_heures, energie_cumulee)
plt.title("Énergie solaire accumulée sur la peau")
plt.xlabel("Heure de la journée (heures)")
plt.ylabel("Énergie totale (J/m²)")
plt.show()


