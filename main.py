#Imports
import math
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import messagebox, Frame, Canvas, Scrollbar, LEFT, RIGHT, BOTH, Y, VERTICAL, NW
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# 1. DONNÉES GÉOGRAPHIQUES

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


ALBEDOS = [0.42, 0.37, 0.32, 0.27, 0.22, 0.17]
SEUIL_PHOTOTYPES = [150, 250, 300, 400, 600, 900]
PHOTOTYPES_TEXT = [
"I -  Phototype Celtique - Peau très claire",
"II - Phototype Nordique - Peau claire ",
"III -Phototype Mixte - Peau claire à brun clair",
"IV -  Phototype Méditerranéen - Peau brun clair",
"V - Phototype Foncé - Peau brun foncé",
"VI - Phototype Très Foncé - Peau brun foncé à noir"
]

#permet de construire la courbe de niveau de risque
def niveau_danger(r):
  if r < 0.25:
      return 0
  elif r < 0.5:
      return 1
  elif r < 1:
      return 2
  elif r < 2:
      return 3
  else:
      return 4

# 2. FONCTIONS DE CALCUL
def declinaison_solaire(nombre_jour):
  return 23.44 * math.sin(math.radians((360 / 365) * (nombre_jour - 81)))


def angle_horaire(heure, longitude, utc_offset):
  long_standard = utc_offset * 15
  heure_solaire = heure + (4 * (longitude - long_standard)) / 60
  return 15 * (heure_solaire - 12)


def angle_solaire(latitude, declinaison, angle_h):
  phi, delta, omega = map(math.radians, [latitude, declinaison, angle_h])
  sin_h = (math.sin(phi) * math.sin(delta) + math.cos(phi) * math.cos(delta) * math.cos(omega))
  return math.degrees(math.asin(max(-1, min(1, sin_h))))


def calcul_energie_cumulee(angles, indice_uv, phototype_index, SPF):
  e_sans, e_avec = [0], [0]
  somme_sans, somme_avec = 0.0, 0.0
  for ang in angles[1:]:
      uv_reel = max(0.1, indice_uv)
      irr = (uv_reel * 0.025) * math.sin(math.radians(ang)) * (1 - ALBEDOS[phototype_index])
      somme_sans += irr * 600
      somme_avec += (irr / SPF) * 600
      e_sans.append(somme_sans)
      e_avec.append(somme_avec)
  return e_sans, e_avec

# 3. LOGIQUE DE L'INTERFACE

def toggle_spf_display(*args):
  if var_creme.get() == "Oui":
      f_spf_input.pack(side=LEFT)
  else:
      f_spf_input.pack_forget()


def ajouter_graphique(fig):
  canvas = FigureCanvasTkAgg(fig, master=scrollable_frame)
  canvas_widget = canvas.get_tk_widget()
  canvas_widget.pack(pady=10, padx=10)
  canvas.draw()
  scrollable_frame.update_idletasks()
  canvas_container.configure(scrollregion=canvas_container.bbox("all"))


def effacer_tout():
  for widget in scrollable_frame.winfo_children():
      widget.destroy()
  canvas_container.yview_moveto(0.0)
  label_res_texte.config(text="En attente de calcul...")


def scenario_egypte():
    lat, lon, utc = countries["égypte"]
    idx_uv, h_start, spf = 11, 12, 30
    inclinaison = declinaison_solaire(172)
    couleurs = ["green", "yellow", "orange", "red", "darkred"]
    x_h, angles = [], []

    # 1. Calcul des angles solaires
    for t in range(int(h_start * 3600), 24 * 3600, 600):
        ang = angle_solaire(lat, inclinaison, angle_horaire(t / 3600, lon, utc))
        if ang > 0: x_h.append(t / 3600); angles.append(ang)

    # 2. CALCUL DYNAMIQUE DU TEMPS AVANT BRÛLURE (TES CALCULS)
    resultats_bruts = []
    for p_idx in [0, 5]:
        # On utilise ta fonction de calcul d'énergie
        e_s, _ = calcul_energie_cumulee(angles, idx_uv, p_idx, spf)
        seuil = SEUIL_PHOTOTYPES[p_idx]

        # On cherche l'index exact où l'énergie accumulée dépasse le seuil
        t_m = next((x_h[i] for i, v in enumerate(e_s) if v >= seuil), None)

        if t_m:
            d = t_m - h_start  # Durée en heures décimales
            resultats_bruts.append(f"{int(d)}h {int((d - int(d)) * 60):02d}min")
        else:
            resultats_bruts.append("plus de 10h")

    # 3. Création du graphique
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 12))
    plt.subplots_adjust(hspace=0.4)

    for ax, p_idx, med, title in zip([ax1, ax2], [0, 5], [SEUIL_PHOTOTYPES[0], SEUIL_PHOTOTYPES[5]],
                                     ["Photo I", "Photo VI"]):
        e_s, e_a = calcul_energie_cumulee(angles, idx_uv, p_idx, spf)
        r_s, r_a = np.array(e_s) / med, np.array(e_a) / med
        for i in range(len(x_h) - 1):
            ax.plot(x_h[i:i + 2], r_s[i:i + 2], color=couleurs[niveau_danger(r_s[i])], linewidth=2)
            ax.plot(x_h[i:i + 2], r_a[i:i + 2], color=couleurs[niveau_danger(r_a[i])], linewidth=2, linestyle='--')
        ax.set_title(f"PIRE CAS - Égypte ({title}, UV 11, à partir de midi)")
        ax.set_xlabel("Moment de la journée (heures)")
        ax.set_ylabel("Niveau de brûlure")
        ax.set_yticks([0, 0.25, 0.5, 1, 2])
        ax.set_yticklabels(["Aucun", "Léger", "Modéré", "Sévère", "Très sévère"])
        ax.grid(True)
        ax.plot([], [], color="black", label="Sans crème")
        ax.plot([], [], color="green", linestyle="--", label="Avec SPF 30")
        ax.legend()

    # 4. MISE À JOUR DU TEXTE AVEC TES RÉSULTATS RÉELS
    texte = (f"PIRE CAS (Calculé selon tes MED et Albedos)\n"
             f"Une personne de phototype I à midi sans crème brûlera en environ {resultats_bruts[0]}.\n\n"
             f"COMPARAISON\n"
             f"Une personne de phototype VI (peau très foncée) mettra environ {resultats_bruts[1]} "
             f"pour atteindre son seuil de brûlure ({SEUIL_PHOTOTYPES[5]} J/m²) dans les mêmes conditions.")

    f_inter_islande.pack_forget()
    f_inter_egypte.pack(fill="x", pady=5)
    label_inter_egypte.delete("1.0", tk.END)
    label_inter_egypte.insert(tk.END, texte)
    ajouter_graphique(fig)



def scenario_islande():
  lat, lon, utc = countries["islande"]
  idx_uv, h_start, spf = 0.1, 11.5, 30
  inclinaison = declinaison_solaire(355)  # 21 décembre
  couleurs = ["green", "yellow", "orange", "red", "darkred"]
  x_h, angles = [], []
  for t in range(int(h_start * 3600), 24 * 3600, 600):
      ang = angle_solaire(lat, inclinaison, angle_horaire(t / 3600, lon, utc))
      if ang > 0: x_h.append(t / 3600); angles.append(ang)




  if not x_h:
      return messagebox.showinfo("Info", "Le soleil ne se lève pas ce jour-là en Islande.")


  fig, ax = plt.subplots(figsize=(8, 6))
  med = 150  # Phototype I
  e_s, e_a = calcul_energie_cumulee(angles, idx_uv, 0, spf)
  r_s, r_a = np.array(e_s) / med, np.array(e_a) / med




  for i in range(len(x_h) - 1):
      ax.plot(x_h[i:i + 2], r_s[i:i + 2], color=couleurs[niveau_danger(r_s[i])], linewidth=2)
      ax.plot(x_h[i:i + 2], r_a[i:i + 2], color=couleurs[niveau_danger(r_a[i])], linewidth=2, linestyle='--')




  ax.set_title("CAS LE MOINS ENSOLEILLÉ - Islande (Phototype I, UV 0, 11h30)")
  ax.set_xlabel("Moment de la journée (heures)")
  ax.set_ylabel("Niveau de brûlure")
  ax.set_yticks([0, 0.25, 0.5, 1, 2])
  ax.set_yticklabels(["Aucun", "Léger", "Modéré", "Sévère", "Très sévère"])
  ax.grid(True)
  ax.plot([], [], color="black", label="Sans crème")
  ax.plot([], [], color="green", linestyle="--", label="Avec SPF 30")
  ax.legend()


  texte = ("CAS LE MOINS ENSOLEILLÉ\nEn Islande le 21 décembre, l'indice UV est si faible (0) "
           "que même une peau très claire (phototype I) ne dépassera jamais le seuil de brûlure, "
           "peu importe le temps passé dehors.")


  # On cache la case Égypte, on affiche la case Islande
  f_inter_egypte.pack_forget()
  f_inter_islande.pack(fill="x", pady=5)
  label_inter_islande.delete("1.0", tk.END)
  label_inter_islande.insert(tk.END, texte)


  ajouter_graphique(fig)


def executer_tout():
  try:
      #  VALIDATIONS
      # 1. Pays
      p_nom = entry_pays.get().lower().strip()
      if p_nom not in countries:
          return messagebox.showwarning("Attention", f"Le pays '{p_nom}' n'est pas reconnu.")
      lat, lon, utc = countries[p_nom]


      # 2. Heure (entre 0 et 23)
      try:
          h_saisie = float(entry_heure.get())
          if not (0 <= h_saisie <= 23.9): raise ValueError
      except ValueError:
          return messagebox.showwarning("Erreur", "L'heure doit être comprise entre 0 et 23.")

       #Indice UV (entre 0 et 11)
      try:
          idx_uv = float(entry_uv.get())
          if not (0 <= idx_uv <= 11): raise ValueError
      except ValueError:
          return messagebox.showwarning("Erreur", "L'indice UV doit être compris entre 0 et 11.")


      # 4. Phototype
      selection = listbox_photo.curselection()
      if not selection:
          return messagebox.showwarning("Attention", "Sélectionnez un phototype dans la liste.")
      photo_idx = selection[0]


      a_creme = var_creme.get()

      spf_val = int(entry_spf.get()) if (a_creme == "Oui" and entry_spf.get()) else 30


      mois_dict = {"Janvier": 0, "Février": 31, "Mars": 59, "Avril": 90, "Mai": 120, "Juin": 151, "Juillet": 181,
                   "Août": 212, "Septembre": 243, "Octobre": 273, "Novembre": 304, "Décembre": 334}
      n_jour = mois_dict[var_mois.get()] + int(entry_jour.get())


      # LOGIQUE BISSEXTILE
      if var_bissextile.get() == "Année bissextile":
          est_bissextile = True
          # Si on est après février (jour 59), on ajoute le 29 février au compteur
          if n_jour > 59:
              n_jour += 1
      else:
          est_bissextile = False


      inclinaison = declinaison_solaire(n_jour)
      x_h, angles = [], []
      for t in range(int(h_saisie * 3600), 24 * 3600, 600):
          ang = angle_solaire(lat, inclinaison, angle_horaire(t / 3600, lon, utc))
          if ang > 0: x_h.append(t / 3600); angles.append(ang)


      if not x_h: return messagebox.showinfo("Info", "Le soleil est couché.")


      e_s, e_a = calcul_energie_cumulee(angles, idx_uv, photo_idx, spf_val)
      med = SEUIL_PHOTOTYPES[photo_idx]

      fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))
      plt.subplots_adjust(hspace=0.4)

      # GRAPHIQUE 1 : ÉNERGIE
      ax1.plot(x_h, e_s, color='red', label="Sans crème")
      ax1.plot(x_h, e_a, color='green', linestyle='--', label=f"Avec SPF {spf_val}")
      # Ajout de la ligne correspondant au MED
      ax1.axhline(y=med, color='black', linestyle=':', label="Seuil de brûlure (MED)")

      ax1.set_title(f"Énergie solaire absorbée - {p_nom.capitalize()}")
      ax1.set_xlabel("Moment de la journée (heures)")
      ax1.set_ylabel("Énergie accumulée (J/m²)")
      ax1.grid(True);
      ax1.legend()

      # GRAPHIQUE 2 : RISQUE
      r_s, r_a = np.array(e_s) / med, np.array(e_a) / med
      couleurs = ["green", "yellow", "orange", "red", "darkred"]
      for i in range(len(x_h) - 1):
          ax2.plot(x_h[i:i + 2], r_s[i:i + 2], color=couleurs[niveau_danger(r_s[i])], linewidth=2)
          ax2.plot(x_h[i:i + 2], r_a[i:i + 2], color=couleurs[niveau_danger(r_a[i])], linewidth=2, linestyle='--')
      ax2.set_title("Risque de brûlure solaire")
      ax2.set_xlabel("Moment de la journée (heures)")
      ax2.set_ylabel("Niveau de brûlure")
      ax2.set_yticks([0, 0.25, 0.5, 1, 2])
      ax2.set_yticklabels(["Aucun", "Léger", "Modéré", "Sévère", "Très sévère"])
      ax2.grid(True)
      ax2.plot([], [], color='black', label="Sans crème")
      ax2.plot([], [], color='green', linestyle='--', label=f"SPF {spf_val}")
      ax2.legend()
      ajouter_graphique(fig)



      e_ref = e_a if a_creme == "Oui" else e_s
      t_m = next((x_h[i] for i, v in enumerate(e_ref) if v >= med), None)
      if t_m:
          d = t_m - h_saisie
          label_res_texte.config(text=f"📍 {p_nom.upper()}\nTemps max dehors : {int(d)}h {int((d - int(d)) * 60)}min")
      else:
          label_res_texte.config(text=f"📍 {p_nom.upper()}\nAucun risque de brûlure !")
  except Exception as e:
      messagebox.showerror("Erreur", str(e))





# 4. INITIALISATION UI

#COULEURS
COULEUR_DROITE = "#FFF9E3"  # Beige très pâle (Crème)
COULEUR_GAUCHE = "#F5E1A4"


root = tk.Tk()
root.title("Calculateur d'exposition solaire")
root.geometry("1100x850")


f_in = Frame(root, width=380, padx=20, bg=COULEUR_GAUCHE)
f_in.pack(side=LEFT, fill=Y)
tk.Label(f_in, text="\nCONFIGURATION", font=("Arial", 12, "bold"),  bg="#FFF9E3", fg="#8B4513").pack()#rendre les cadres colorés
# Modifie cette ligne dans la section # 4. INITIALISATION UI
entry_pays = tk.Entry(f_in, bg="white") # Ajout du fond blanc
entry_pays.insert(0, "france")
entry_pays.pack(pady=2)




f_d = Frame(f_in, bg="#FFF9E3");                 #on colorie
f_d.pack()
entry_jour = tk.Entry(f_d, width=5);
entry_jour.insert(0, "21");
entry_jour.pack(side=LEFT)
var_mois = tk.StringVar(value="Juin") # On met 'J' en majuscule ici
tk.OptionMenu(f_d, var_mois,
            *["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre",
              "Novembre", "Décembre"]).pack(side=LEFT)
var_bissextile = tk.StringVar(value="Année non bissextile")                                           #creation du bouton non
tk.OptionMenu(f_d, var_bissextile, "Année non bissextile", "Année bissextile").pack(side=LEFT)




f_h_uv = Frame(f_in, bg="#FFF9E3") ;
f_h_uv.pack(pady=5)
tk.Label(f_h_uv, text="Heure:").pack(side=LEFT);
entry_heure = tk.Entry(f_h_uv, width=5);
entry_heure.insert(0, "10");
entry_heure.pack(side=LEFT)
tk.Label(f_h_uv, text=" UV:").pack(side=LEFT);
entry_uv = tk.Entry(f_h_uv, width=5);
entry_uv.insert(0, "6");
entry_uv.pack(side=LEFT)




listbox_photo = tk.Listbox(f_in, height=6, width=45)
for p in PHOTOTYPES_TEXT: listbox_photo.insert(tk.END, p)
listbox_photo.select_set(0);
listbox_photo.pack(pady=5)




f_spf_container = Frame(f_in, bg="#FFF9E3") ;
f_spf_container.pack(pady=5)
tk.Label(f_spf_container, text="Crème ?").pack(side=LEFT)
var_creme = tk.StringVar(value="Non")
tk.OptionMenu(f_spf_container, var_creme, "Non", "Oui").pack(side=LEFT)
f_spf_input = Frame(f_spf_container, bg="#FFF9E3")
tk.Label(f_spf_input, text=" SPF:").pack(side=LEFT)
entry_spf = tk.Entry(f_spf_input, width=5);
entry_spf.insert(0, "30");
entry_spf.pack(side=LEFT)
var_creme.trace("w", toggle_spf_display)




# BOUTONS
tk.Button(f_in, text="LANCER LE CALCUL", command=executer_tout, bg="#4CAF50", fg="white", font=("Arial", 11, "bold"),
        highlightbackground="#4CAF50", relief="raised").pack(fill="x", pady=5)


# SEPARATION ET TITRE SCENARIOS
tk.Label(f_in, text="").pack() # Un petit espace vide pour respirer
tk.Label(f_in, text="SCÉNARIOS SPÉCIAUX", font=("Arial", 10, "bold"), fg="black").pack(pady=5)





tk.Button(f_in, text="Pire Cas (Égypte)", command=scenario_egypte, bg="orange", fg="black", font=("Arial", 11, "bold"),
        highlightbackground="orange", relief="raised").pack(fill="x", pady=2)
tk.Button(f_in, text="Moins ensoleillé (Islande)", command=scenario_islande, bg="lightblue", fg="black",
        font=("Arial", 11, "bold"), highlightbackground="lightblue", relief="raised").pack(fill="x", pady=2)




f_res = tk.LabelFrame(f_in, text=" RÉSULTAT ", fg="blue", padx=10, pady=10)
f_res.pack(fill="x", pady=20)
label_res_texte = tk.Label(f_res, text="En attente...", font=("Arial", 10, "bold"))
label_res_texte.pack()




# CASE INTERPRÉTATION ÉGYPTE
f_inter_egypte = tk.LabelFrame(f_in, text=" INTERPRÉTATION (ÉGYPTE) ", fg="darkred", padx=10, pady=10)
# Remplacement par tk.Text pour permettre le scroll
label_inter_egypte = tk.Text(f_inter_egypte, height=5, width=40, font=("Arial", 9), wrap="word", bg="#F5E1A4", relief="flat")
label_inter_egypte.pack(side=LEFT, fill="both", expand=True)


# Barre de défilement pour Égypte
scroll_eg = tk.Scrollbar(f_inter_egypte, command=label_inter_egypte.yview)
scroll_eg.pack(side=RIGHT, fill=Y)
label_inter_egypte.config(yscrollcommand=scroll_eg.set)




# CASE INTERPRÉTATION ISLANDE
f_inter_islande = tk.LabelFrame(f_in, text=" INTERPRÉTATION (ISLANDE) ", fg="darkblue", padx=10, pady=10)
# Remplacement par tk.Text pour permettre le scroll
label_inter_islande = tk.Text(f_inter_islande, height=5, width=40, font=("Arial", 9), wrap="word", bg="#F5E1A4", relief="flat")
label_inter_islande.pack(side=LEFT, fill="both", expand=True)


# Barre de défilement pour Islande
scroll_is = tk.Scrollbar(f_inter_islande, command=label_inter_islande.yview)
scroll_is.pack(side=RIGHT, fill=Y)
label_inter_islande.config(yscrollcommand=scroll_is.set)


tk.Button(f_in, text="🔄 EFFACER GRAPHIQUES", command=effacer_tout, bg="#f44336", fg="white", font=("Arial", 10, "bold"),
        highlightbackground="#f44336", relief="raised").pack(side="bottom", fill="x", pady=20)




f_graph = Frame(root, bg=COULEUR_DROITE)
f_graph.pack(side=RIGHT, fill=BOTH, expand=True)
canvas_container = Canvas(f_graph, bg=COULEUR_DROITE, highlightthickness=0)
scrollable_frame = Frame(canvas_container, bg=COULEUR_DROITE)
scrollbar = Scrollbar(f_graph, command=canvas_container.yview)
canvas_container.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y);
canvas_container.pack(fill=BOTH, expand=True)
scrollable_frame = Frame(canvas_container, bg="white")
canvas_container.create_window((0, 0), window=scrollable_frame, anchor=NW)
scrollable_frame.bind("<Configure>", lambda e: canvas_container.configure(scrollregion=canvas_container.bbox("all")))


# Force tous les widgets du panneau de gauche à devenir beige foncé
# On colorie tout ce qui est à GAUCHE en beige PÂLE
for widget in f_in.winfo_children():
   try:
       # On ne change pas la couleur des boutons
       if not isinstance(widget, tk.Button):
           widget.configure(bg=COULEUR_GAUCHE)


       # Optionnel : Si on a des cadres imbriqués (f_d, f_h_uv, etc.)
       if isinstance(widget, tk.Frame):
           widget.configure(bg=COULEUR_GAUCHE)
           for sub_widget in widget.winfo_children():
               if not isinstance(sub_widget, tk.Button):
                   sub_widget.configure(bg=COULEUR_GAUCHE)
   except:
       pass


root.mainloop()



