
import math
#Coordonnées terrestres des pays (prises directement d'Internet )
countries = {

    "Afghanistan": (33.0, 65.0, 4.5),
    "Afrique du Sud": (-30.0, 25.0, 2.0),
    "Albanie": (41.0, 20.0, 1.0),
    "Algérie": (28.0, 3.0, 1.0),
    "Allemagne": (51.0, 9.0, 1.0),
    "Andorre": (42.5, 1.5, 1.0),
    "Angola": (-12.5, 18.5, 1.0),
    "Antigua-et-Barbuda": (17.1, -61.8, -4.0),
    "Arabie saoudite": (25.0, 45.0, 3.0),
    "Argentine": (-34.0, -64.0, -3.0),
    "Arménie": (40.0, 45.0, 4.0),
    "Australie": (-25.0, 133.0, 9.5),
    "Autriche": (47.3, 13.3, 1.0),
    "Azerbaïdjan": (40.5, 47.5, 4.0),
    "Bahamas": (24.3, -76.0, -5.0),
    "Bahreïn": (26.0, 50.5, 3.0),
    "Bangladesh": (24.0, 90.0, 6.0),
    "Barbade": (13.2, -59.5, -4.0),
    "Belgique": (50.8, 4.5, 1.0),
    "Belize": (17.2, -88.7, -6.0),
    "Bénin": (9.5, 2.2, 1.0),
    "Bhoutan": (27.5, 90.5, 6.0),
    "Biélorussie": (53.0, 28.0, 3.0),
    "Birmanie": (22.0, 98.0, 6.5),
    "Bolivie": (-17.0, -65.0, -4.0),
    "Bosnie-Herzégovine": (44.0, 18.0, 1.0),
    "Botswana": (-22.0, 24.0, 2.0),
    "Brésil": (-10.0, -55.0, -3.0),
    "Brunei": (4.5, 114.7, 8.0),
    "Bulgarie": (43.0, 25.0, 2.0),
    "Burkina Faso": (13.0, -2.0, 0.0),
    "Burundi": (-3.5, 30.0, 2.0),
    "Cambodge": (13.0, 105.0, 7.0),
    "Cameroun": (6.0, 12.0, 1.0),
    "Canada": (56.0, -106.0, -6.0),
    "Cap-Vert": (16.0, -24.0, -1.0),
    "Chili": (-30.0, -71.0, -3.0),
    "Chine": (35.0, 103.0, 8.0),
    "Chypre": (35.0, 33.0, 2.0),
    "Colombie": (4.0, -72.0, -5.0),
    "Comores": (-12.2, 44.5, 3.0),
    "Congo": (-1.0, 15.0, 1.0),
    "Corée du Nord": (40.0, 127.0, 9.0),
    "Corée du Sud": (36.0, 128.0, 9.0),
    "Costa Rica": (10.0, -84.0, -6.0),
    "Côte d’Ivoire": (8.0, -5.0, 0.0),
    "Croatie": (45.1, 15.2, 1.0),
    "Cuba": (21.5, -80.0, -5.0),
    "Danemark": (56.0, 10.0, 1.0),
    "Djibouti": (11.5, 43.0, 3.0),
    "Dominique": (15.4, -61.3, -4.0),
    "Égypte": (26.0, 30.0, 2.0),
    "Émirats arabes unis": (24.0, 54.0, 4.0),
    "Équateur": (-1.5, -78.0, -5.0),
    "Érythrée": (15.0, 39.0, 3.0),
    "Espagne": (40.0, -4.0, 1.0),
    "Estonie": (59.0, 26.0, 2.0),
    "Eswatini": (-26.5, 31.5, 2.0),
    "États-Unis": (39.0, -98.0, -7.0),
    "Éthiopie": (9.0, 40.0, 3.0),
    "Fidji": (-17.8, 178.0, 12.0),
    "Finlande": (64.0, 26.0, 2.0),
    "France": (46.0, 2.0, 1.0),
    "Gabon": (-1.0, 11.8, 1.0),
    "Gambie": (13.4, -15.3, 0.0),
    "Géorgie": (42.0, 43.5, 4.0),
    "Ghana": (8.0, -2.0, 0.0),
    "Grèce": (39.0, 22.0, 2.0),
    "Grenade": (12.1, -61.7, -4.0),
    "Guatemala": (15.5, -90.3, -6.0),
    "Guinée": (10.0, -10.0, 0.0),
    "Guinée-Bissau": (12.0, -15.0, 0.0),
    "Guinée équatoriale": (1.6, 10.5, 1.0),
    "Guyana": (5.0, -59.0, -4.0),
    "Haïti": (19.0, -72.5, -5.0),
    "Honduras": (15.0, -86.5, -6.0),
    "Hongrie": (47.0, 20.0, 1.0),
    "Îles Marshall": (7.1, 171.0, 12.0),
    "Îles Salomon": (-9.6, 160.2, 11.0),
    "Inde": (20.0, 77.0, 5.5),
    "Indonésie": (-5.0, 120.0, 8.0),
    "Irak": (33.0, 44.0, 3.0),
    "Iran": (32.0, 53.0, 3.5),
    "Irlande": (53.0, -8.0, 0.0),
    "Islande": (65.0, -18.0, 0.0),
    "Israël": (31.5, 34.8, 2.0),
    "Italie": (42.5, 12.5, 1.0),
    "Jamaïque": (18.1, -77.3, -5.0),
    "Japon": (36.0, 138.0, 9.0),
    "Jordanie": (31.0, 36.0, 3.0),
    "Kazakhstan": (48.0, 68.0, 5.0),
    "Kenya": (1.0, 38.0, 3.0),
    "Kirghizistan": (41.0, 75.0, 6.0),
    "Kiribati": (1.8, 173.0, 13.0),
    "Koweït": (29.5, 47.5, 3.0),
    "Laos": (18.0, 105.0, 7.0),
    "Lesotho": (-29.5, 28.5, 2.0),
    "Lettonie": (57.0, 25.0, 2.0),
    "Liban": (33.8, 35.8, 2.0),
    "Libéria": (6.5, -9.5, 0.0),
    "Libye": (26.0, 17.0, 2.0),
    "Liechtenstein": (47.2, 9.5, 1.0),
    "Lituanie": (55.0, 24.0, 2.0),
    "Luxembourg": (49.8, 6.1, 1.0),
    "Macédoine du Nord": (41.6, 21.7, 1.0),
    "Madagascar": (-20.0, 47.0, 3.0),
    "Malaisie": (2.5, 112.5, 8.0),
    "Malawi": (-13.5, 34.0, 2.0),
    "Maldives": (3.2, 73.0, 5.0),
    "Mali": (17.0, -4.0, 0.0),
    "Malte": (35.9, 14.5, 1.0),
    "Maroc": (32.0, -6.0, 1.0),
    "Maurice": (-20.3, 57.5, 4.0),
    "Mauritanie": (20.0, -12.0, 0.0),
    "Mexique": (23.0, -102.0, -6.0),
    "Micronésie": (6.9, 158.2, 11.0),
    "Moldavie": (47.0, 29.0, 2.0),
    "Monaco": (43.7, 7.4, 1.0),
    "Mongolie": (46.0, 105.0, 8.0),
    "Monténégro": (42.5, 19.3, 1.0),
    "Mozambique": (-18.5, 35.0, 2.0),
    "Myanmar": (22.0, 98.0, 6.5),
    "Namibie": (-22.0, 17.0, 2.0),
    "Nauru": (-0.5, 166.9, 12.0),
    "Népal": (28.0, 84.0, 5.75),
    "Nicaragua": (13.0, -85.0, -6.0),
    "Niger": (16.0, 8.0, 1.0),
    "Nigeria": (9.0, 8.0, 1.0),
    "Norvège": (62.0, 10.0, 1.0),
    "Nouvelle-Zélande": (-41.0, 174.0, 12.0),
    "Oman": (21.0, 57.0, 4.0),
    "Ouganda": (1.0, 32.0, 3.0),
    "Ouzbékistan": (41.0, 64.0, 5.0),
    "Pakistan": (30.0, 70.0, 5.0),
    "Palaos": (7.5, 134.5, 9.0),
    "Palestine": (31.9, 35.2, 2.0),
    "Panama": (9.0, -80.0, -5.0),
    "Papouasie-Nouvelle-Guinée": (-6.0, 147.0, 10.0),
    "Paraguay": (-23.0, -58.0, -4.0),
    "Pays-Bas": (52.5, 5.7, 1.0),
    "Pérou": (-10.0, -76.0, -5.0),
    "Philippines": (13.0, 122.0, 8.0),
    "Pologne": (52.0, 20.0, 1.0),
    "Portugal": (39.5, -8.0, 0.0),
    "Qatar": (25.3, 51.2, 3.0),
    "République centrafricaine": (7.0, 21.0, 1.0),
    "République démocratique du Congo": (-2.5, 23.5, 1.5),
    "République dominicaine": (19.0, -70.7, -4.0),
    "Roumanie": (46.0, 25.0, 2.0),
    "Royaume-Uni": (55.0, -3.0, 0.0),
    "Russie": (60.0, 100.0, 7.0),
    "Rwanda": (-2.0, 30.0, 2.0),
    "Saint-Christophe-et-Niévès": (17.3, -62.7, -4.0),
    "Saint-Marin": (43.9, 12.5, 1.0),
    "Saint-Vincent-et-les-Grenadines": (13.2, -61.2, -4.0),
    "Sainte-Lucie": (13.9, -60.9, -4.0),
    "Samoa": (-13.8, -172.1, 13.0),
    "Sao Tomé-et-Principe": (0.2, 6.7, 0.0),
    "Sénégal": (14.0, -14.0, 0.0),
    "Serbie": (44.0, 21.0, 1.0),
    "Seychelles": (-4.6, 55.5, 4.0),
    "Sierra Leone": (8.5, -11.5, 0.0),
    "Singapour": (1.3, 103.8, 8.0),
    "Slovaquie": (48.7, 19.7, 1.0),
    "Slovénie": (46.1, 14.8, 1.0),
    "Somalie": (5.0, 46.0, 3.0),
    "Soudan": (15.0, 30.0, 2.0),
    "Soudan du Sud": (7.0, 30.0, 2.0),
    "Sri Lanka": (7.0, 81.0, 5.5),
    "Suède": (62.0, 15.0, 1.0),
    "Suisse": (47.0, 8.0, 1.0),
    "Suriname": (4.0, -56.0, -3.0),
    "Syrie": (35.0, 38.0, 3.0),
    "Tadjikistan": (39.0, 71.0, 5.0),
    "Taïwan": (23.5, 121.0, 8.0),
    "Tanzanie": (-6.0, 35.0, 3.0),
    "Tchad": (15.0, 19.0, 1.0),
    "Thaïlande": (15.0, 100.0, 7.0),
    "Timor oriental": (-8.8, 125.7, 9.0),
    "Togo": (8.0, 1.2, 0.0),
    "Tonga": (-21.2, -175.2, 13.0),
    "Trinité-et-Tobago": (10.5, -61.2, -4.0),
    "Tunisie": (34.0, 9.0, 1.0),
    "Turkménistan": (39.0, 59.0, 5.0),
    "Turquie": (39.0, 35.0, 3.0),
    "Tuvalu": (-8.5, 179.2, 12.0),
    "Ukraine": (49.0, 32.0, 2.0),
    "Uruguay": (-33.0, -56.0, -3.0),
    "Vanuatu": (-16.0, 167.0, 11.0),
    "Vatican": (41.9, 12.4, 1.0),
    "Venezuela": (7.0, -66.0, -4.0),
    "Vietnam": (16.0, 108.0, 7.0),
    "Yémen": (15.0, 48.0, 3.0),
    "Zambie": (-15.0, 30.0, 2.0),
    "Zimbabwe": (-20.0, 30.0, 2.0)
}
pays = input("Assistant : Bonjour ! Je vais vous aider à calculer l'élévation exacte du Soleil. Pour commencer, dans quel pays souhaitez-vous mesurer l'exposition ? : ").lower()


#Choix du pays par l'utilisateur
while pays not in countries:
    print("Ce pays n'existe pas. Veuillez réessayer")
    pays = input("Entrez le pays : ")

print(f"Assistant : Très bien! j'utiliserai ses coordonnées moyennes.")

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
    heure = int(input("Cette heure n'existe pas, veuillez recommencer. Entrer une heure de la journée entre 0h et 23h : "))


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



