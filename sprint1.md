# Sprint 1

## Besoins utilisateurs et critères de réussite

### 1. Date et heure
En tant qu’utilisateur, je veux entrer la date et l’heure afin d’évaluer l’exposition solaire à un moment précis.

Critères de réussite :
- L’utilisateur peut entrer le mois, le jour et l’heure.
Le programme vérifie que le jour correspond au mois, en tenant compte des années bissextiles pour février.
- L’utilisateur peut indiquer si l’année est bissextile ou non.
- L’heure doit être comprise entre 0 et 23.
- Si une valeur est invalide, le programme redemande une entrée.

---
### 2. Position géographique
En tant qu’utilisateur, je veux indiquer le pays ou le lieu afin de tenir compte de la position géographique.

Critères de réussite :
- L’utilisateur peut entrer le nom d’un pays.
- Le programme vérifie si ce pays existe dans la base de données.
- Si le pays n’existe pas, le programme demande de réessayer.
- Les coordonnées géographiques du pays sont récupérées.

---

### 3. Type de peau
En tant qu’utilisateur, je veux choisir mon type de peau afin d’adapter l’estimation à ma sensibilité.

Critères de réussite :
- Le programme affiche la liste des phototypes disponibles.
- L’utilisateur peut choisir un phototype avec un numéro.
- Le programme vérifie que le numéro est compris entre 1 et 6.
- Si la réponse est invalide, le programme redemande une entrée.
- Le phototype sélectionné est enregistré pour les calculs.

---

### 4. Intensité des UV
En tant qu’utilisateur, je veux connaître l’intensité des UV pour mon lieu et mon moment d’exposition afin de mieux comprendre le niveau de risque.

Critères de réussite :
- L’utilisateur peut entrer l’indice UV.
- Le programme vérifie que la valeur est entre 0 et 11.
- L’irradiance solaire est calculée à partir de l’indice UV.
- L’intensité des UV reçue par la peau est affichée.

---

### 5. Crème solaire
En tant qu’utilisateur, je veux indiquer si j’utilise une crème solaire afin d’observer son effet sur l’exposition.

Critères de réussite :
- L’utilisateur peut répondre par "oui" ou "non".
- Si la réponse est invalide, le programme redemande une entrée.
- Si l’utilisateur utilise une crème solaire, il peut entrer un SPF.
- Le programme calcule l’effet de la crème solaire sur l’intensité des UV et affiche la différence entre l'intensité avec crème solaire et l'intesité sans.

