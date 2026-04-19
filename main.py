
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


#FONCTIONS (l'entièreté des calculs suivants a été verifiée par un prof du département de physique)
#CALCUL DE LA DÉCLINAISON DU SOLEIL (position du soleil dans l'année)
def declinaison_solaire(nombre_jour):
    #transforme le jour de l'année en angle
    angle_deg = (360/365) * (nombre_jour - 81)
    angle_rad = math.radians(angle_deg)
    return 23.44 * math.sin(angle_rad)

#CALCUL DE L'ANGLE HORAIRE
# On récupère les 3 valeurs du dictionnaire
latitude = countries[pays][0]
longitude = countries[pays][1]
utc_offset = countries[pays][2]

def angle_horaire(heure, longitude, utc_offset):
    # Calcul de la longitude de référence du fuseau horaire
    long_standard = utc_offset * 15
    # Conversion heure civile en heure solaire
    heure_solaire = heure + (4 * (longitude - long_standard)) / 60
    return 15 * (heure_solaire - 12)

#CALCUL DE L'ANGLE D'ÉLÉVATION DU SOLEIL
def angle_solaire(latitude, declinaison_solaire, angle_horaire):
    #Calcul de l'angle d'élévation h du soleil et conversion en radians
    phi = math.radians(latitude)
    delta = math.radians(declinaison_solaire)
    omega = math.radians(angle_horaire)
    sin_h = (math.sin(phi)*math.sin(delta) + math.cos(phi)*math.cos(delta)*math.cos(omega))
    #Conversion en degrés
    return math.degrees(math.asin(sin_h))

#On appelle les fonctions
inclinaison = declinaison_solaire(nombre_jour)
horaire = angle_horaire(heure, longitude, utc_offset)
angle_solaire_deg = angle_solaire(latitude, inclinaison, horaire)

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

#Demande à l'utilisateur de sélectionner son phototype
print("\nVeuillez maintenant choisir votre phototype parmi ceux-ci :\n")
#Ce petit bout de code vient de ChatGPT (2 prochaines lignes)
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


#Liste des différents albédos selon le phototype
albedos = [0.42, 0.37, 0.32, 0.27, 0.22, 0.17]

#CALCUL DE L'IRRADIANCE ABSORBÉE (sans crème solaire)
def irradiance_absorbee (indice_uv, angle_solaire_deg, albedo):
    irradiance_totale = indice_uv * 0.025 # 1 unité d'indice UV correspond environ à 0.025 W/m²

    if angle_solaire_deg <= 0:
        return 0

    #Conversion angle solaire de degrés vers radians
    angle_solaire_rad = math.radians(angle_solaire_deg)
    return irradiance_totale * math.sin(angle_solaire_rad) * (1-albedo)

#On appelle la fonction
irradiance_abs_sans_creme = irradiance_absorbee(indice_uv, angle_solaire_deg, albedos[phototype_index])

def scenarios_creme_solaire (irradiance_abs_sans_creme):
    SPF_MIN = 30  # la valeur de SPF minimale recommandé est 30

    # Cas où le soleil est sous l'horizon
    if irradiance_abs_sans_creme == 0:
        print("Le soleil est sous l'horizon: aucune exposition UV!")
        return 0

    creme_solaire = input("Utilisez-vous de la crème solaire ? (oui/non) : ").lower()

    while creme_solaire not in ["oui", "non"]:
        creme_solaire = input("Réponse invalide. Veuillez répondre par 'oui' ou 'non' : ").lower()

    #Cas où la crème solaire est utilisée
    if creme_solaire == "oui":
        SPF = int(input("Entrez le facteur de protection solaire (SPF) :"))
        irradiance_abs_avec_creme = irradiance_abs_sans_creme / SPF
        difference = irradiance_abs_sans_creme - irradiance_abs_avec_creme
        print(f"\nSuper ! Avec votre crème solaire de SPF {SPF}, l'intensité des UV reçue est réduite de {round(difference, 3)} W/m².")
        print(f"\nLe soleil frappe donc votre peau avec une intensité d'environ {round(irradiance_abs_avec_creme, 3)} W/m².")
        return irradiance_abs_avec_creme

    #Cas où la crème solaire n'est pas utilisée
    else:
        irradiance_spf_min = irradiance_abs_sans_creme / SPF_MIN
        difference = irradiance_abs_sans_creme - irradiance_spf_min
        print(f"\nSi vous aviez appliqué une crème solaire de SPF {SPF_MIN}, l'intensité des UV aurait été réduite de {round(difference, 3)} W/m²! Pas mal, non ?")
        print(f"Sans crème, le soleil frappe actuellement votre peau avec une intensité de {round(irradiance_abs_sans_creme, 3)} W/m².")
        return irradiance_abs_sans_creme

irradiance_finale = scenarios_creme_solaire(irradiance_abs_sans_creme)


#Préparation des listes pour les graphiques
#a)- liste des heures de la journée (abcisses du graphique)

x_heures = []
angles_correspondants = []  #angle que fait le soleil avec l'horizon selon les heures de la journée (0-24h)

inclinaison = declinaison_solaire(nombre_jour) #composante necessaire au calcul de l'angle entre le soleil et l'horizon

heure_depart = heure * 3600
for t in range(heure_depart, 24 * 3600):
    heure_actuelle = t / 3600

    #calcul pour trouver tout les angles que fait le soleil avec l'horizon durant l'entiereté de la journée
    h_horaire = angle_horaire(heure_actuelle, longitude, utc_offset)
    a_solaire = angle_solaire(latitude, inclinaison, h_horaire)

    #On ne garde que la période de jour (entre lever et coucher, donc les angles plus grands que zéro)
    if a_solaire > 0:
        x_heures.append(heure_actuelle)
        angles_correspondants.append(a_solaire)

#b) Liste des ordonnées
#liste pour stocker toute les irradiances de 0 a 24 heures
energie_cumulee = []
somme_temporaire = 0.0
albedo_choisi = albedos[phototype_index]
energie_cumulee_avec_creme = []

for i in range(len(angles_correspondants)):      #calcul de l'irradince durant la journée grâce à la liste des angles ( repris par '' i '' )

    angle_actuel = angles_correspondants[i]
    irradiance_totale = indice_uv * 0.025        #calcul de l'irradiance qui arrive sur terre  partir de l'UV donné sur méteomedia
    sin_h = math.sin(math.radians(angle_actuel))
    #On prend en compte l'albédo (énergie absorbée par la peau)
    irr_abs = irradiance_totale * sin_h * (1 - albedo_choisi)
    somme_temporaire = somme_temporaire + irr_abs               #Cumul de l'énergie (Joules/m²). pour chaque seconde qui passe, la peau absorbe une irradiance de plus. donc on additionne, on ajoute la valeur a la liste et on recommence pour la seconde suivante
    # Irradiance avec protection
    irr_abs_creme = irr_abs / spf_comparaison
    somme_avec_creme += irr_abs_creme
    # 3. On stocke le résultat pour le graphique
    energie_cumulee.append(somme_temporaire)
    energie_cumulee_avec_creme.append(somme_avec_creme)
#AFFICHAGE DU GRAPHIQUE (sans creme solaire)

#On définit la taille de la figure pour qu'elle soit bien lisible
plt.figure(figsize=(10, 6))

# Création de la courbe : x_heures en abscisses, energie_cumulee en ordonnées
plt.plot(x_heures, energie_cumulee, color='orange', linewidth=2.5, label="Énergie cumulée")
plt.title("Évolution de l'énergie solaire absorbée au fil de la journée", fontsize=14)
plt.xlabel("Heure de la journée sur votre montre (heures)", fontsize=12)
plt.ylabel("Énergie totale accumulée (J/m²)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlim(min(x_heures), max(x_heures))

#AFFICHAGE DU GRAPHIQUE( Avec creme solaire)
plt.figure(figsize=(10, 6))
plt.plot(x_heures, energie_cumulee_AVEC, color='green', linewidth=2, label=f"AVEC protection (SPF {spf_comparaison})")
plt.legend(["Accumulation de l'energie sans crème solaire",  "Accumulation de l'énergie avec crème solaire"])
plt.show()


seuil_phototypes = [150, 250, 300, 400, 600, 900] #valeurs seuils de chaque phototype (avec source)
med = seuil_phototypes[phototype_index] #MED: Minimal Erythema Dose, correspond à la dose minimale d'UV causant une brulûre

x = np.array(x_heures)
ratio = np.array(energie_cumulee) / med

couleurs = ["green", "yellow", "orange", "red", "darkred"]

#Cette fonction transforme les ratios en catégorie
def niveau(r):
    if r < 0.25:
        return 0 #si l'utilisateur est à moins de 25% de la brulûre: aucun danger
    elif r < 0.5:
        return 1
    elif r < 1:
        return 2
    elif r < 2:
        return 3
    else:
        return 4

#Création du graphique
plt.figure(figsize=(10,6))

#Construction de la courbe colorée
for i in range(len(x) - 1): #on parcourt chaque segment de temps (chaque mini-ligne utilisée pour couper la courbe en morceaux pour permettre de délimiter les couleurs selon les niveaux)
    n = niveau(ratio[i])
    # Trace un petit segment de la courbe entre deux points consécutifs. La couleur dépend du niveau de brûlure à cet instant
    plt.plot(x[i:i+2], ratio[i:i+2], color=couleurs[n], linewidth=2) #x[i:i+2] = sous-liste de 2 points

plt.title("Risque de brûlure solaire")
plt.xlabel("Heure")
plt.xlim(min(x_heures), max(x_heures))
plt.xticks(np.arange(min(x_heures), max(x_heures)+0.5, 0.5))
plt.ylabel("Niveau de brûlure")
plt.yticks([0, 0.25, 0.5, 1, 2],["Aucun", "Léger", "Modéré", "Sévère", "Très sévère"])
plt.grid(True,linestyle='--', alpha=0.6)
plt.show()






