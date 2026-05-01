# 🎯 Prospection Next.js — Système de prospection intelligente

> Vault Obsidian partagé pour la prospection de clients (artisans & fast-food) pour création/refonte de sites en **Next.js**.
>
> **Argumentaire clé** : ⚡ Vitesse + 🔍 SEO naturel + 💰 Conversion

---

## 📁 Structure du repo

```
Prospection/
├── README.md                 ← Tu es ici
├── Méthodologie.md           → Guide pas à pas pour trouver des prospects
├── Dashboard.md              → 🎯 Actions du jour (auto-généré)
├── Suivi.md                  → 📋 Tableau global de tous les prospects
├── Index-Statuts.md          → 📑 Prospects groupés par statut
├── Index-Zones.md            → 🗺️ Prospects groupés par ville
├── Index-Metiers.md          → 🛠️ Prospects groupés par métier
├── update_index.py           → Script de régénération des index
│
├── Artisans/
│   ├── Index.md
│   ├── Plombier_Pro_Paris.md
│   ├── ÉlecService_Lyon.md
│   ├── Menuiserie_Dupont.md
│   ├── Serrurerie_Rapide.md
│   └── Peinture__Déco.md
│
├── Fast-Food/
│   ├── Index.md
│   ├── Ckebab.md
│   ├── Junk_Burgers.md
│   ├── Bio_Burger.md
│   ├── Bchef.md
│   ├── Alfred_Burger.md
│   └── Les_Burgers_de_Papa.md
│
└── Templates/
    ├── Fiche-Prospect.md     → Template pour créer une nouvelle fiche
    └── Email-Prospection.md  → Templates d'emails de prospection
```

---

## 🏷️ YAML Frontmatter — Le cœur du système

Chaque fiche de prospect commence par un **bloc YAML** (métadonnées) :

```yaml
---
nom: "Nom de l'entreprise"
type: "Fast-Food"           # ou "Artisan"
metier: "Kebab"             # Métier précis
zone: "Paris 15e"           # Ville / quartier
statut: "à_contacter"       # Voir les statuts ci-dessous
priorite: "haute"           # haute / moyenne / basse
site_actuel: "https://..."  # URL ou vide
techno: "WordPress"         # WordPress / Wix / N/A
date_contact: ""            # Rempli quand tu contactes
date_reponse: ""            # Rempli quand le client répond
canal: ""                   # email / telephone / physique
reponse: ""                 # Ce qu'a dit le client
telephone: "01 23 45 67 89"
email: "contact@exemple.fr"
tags:
  - "sans_site"             # ou "refonte", "site_existant"
  - "restauration"          # ou "artisanat"
---
```

### 🎨 Les 7 statuts possibles

| Statut | Emoji | Signification | Action |
|--------|-------|---------------|--------|
| `à_contacter` | 🔵 | Jamais contacté | **À prospecter** |
| `contacté` | 🟡 | Email/tel envoyé | Attendre réponse |
| `relancé` | 🟠 | Relance faite | Attendre réponse |
| `chaud` | 🔥 | Intéressé, négociation | **Prioritaire** |
| `froid` | ❄️ | Pas intéressé | Ne pas relancer |
| `gagné` | ✅ | Contrat signé | Client ! |
| `perdu` | ❌ | Refus définitif | Ne pas relancer |

### 🔴 Les 3 niveaux de priorité

| Priorité | Signification |
|----------|---------------|
| `haute` | 🔴 Sans site web = prospect CHAUD |
| `moyenne` | 🟡 Site existant mais à refaire |
| `basse` | 🟢 Site déjà correct, opportunité faible |

---

## 🔄 Workflow de prospection

### Étape 1 : Trouver un prospect

**Soit je le trouve** (recherche web) **soit tu me le forward** (Google Maps, rue, bouche-à-oreille).

### Étape 2 : Créer la fiche

Copier `Templates/Fiche-Prospect.md` et remplir le YAML :

```yaml
---
nom: "Serrurerie Martin"
type: "Artisan"
metier: "Serrurier"
zone: "Bordeaux"
statut: "à_contacter"
priorite: "haute"
site_actuel: ""
techno: "N/A"
telephone: "05 56 00 11 22"
email: ""
tags:
  - "sans_site"
  - "artisanat"
---
```

### Étape 3 : Régénérer les index

Après ajout/modification d'une fiche, exécuter :

```bash
python update_index.py
```

Ou demander à l'agent de le faire.

Les fichiers suivants se mettent à jour automatiquement :
- `Dashboard.md` → Actions prioritaires
- `Suivi.md` → Tableau global
- `Index-Statuts.md` → Par statut
- `Index-Zones.md` → Par ville
- `Index-Metiers.md` → Par métier

### Étape 4 : Contacter le prospect

Ouvrir `Dashboard.md` → section **🔵 À contacter**.

Utiliser `Templates/Email-Prospection.md` pour rédiger l'email.

### Étape 5 : Mettre à jour le statut

Dans la fiche du prospect, modifier le YAML :

```yaml
statut: "contacté"
date_contact: "2026-05-01"
canal: "email"
```

Puis régénérer les index. Le prospect disparaît de "À contacter" et apparaît dans "Contacté".

### Étape 6 : Suivre la réponse

Quand le client répond :

```yaml
statut: "chaud"          # ou "froid", "gagné", "perdu"
date_reponse: "2026-05-03"
reponse: "Intéressé par un devis, envoyer proposition"
```

---

## 🚫 Anti-doublon / Anti-spam

| Règle | Comment ça marche |
|-------|-------------------|
| **Pas de recherche en double** | Avant d'ajouter un prospect, je vérifie dans `Suivi.md` ou `Index-Zones.md` s'il existe déjà |
| **Pas de contact en double** | Un prospect avec `statut: contacté` ou `relancé` n'apparaît plus dans "À contacter" |
| **Pas de relance sur froid** | Les prospects `froid` ou `perdu` sont exclus des tableaux d'action |
| **Relances programmées** | `contacté` → relance J+3 → `relancé` → dernière relance J+7 → `froid` |

---

## 📊 Les 5 tableaux auto-générés

### 1. Dashboard.md 🎯
**Le plus important** — ce que tu dois faire AUJOURD'HUI :
- 🔵 Qui contacter aujourd'hui (trié par priorité)
- 🟠 Qui relancer cette semaine
- 🔥 Qui est chaud en négociation
- 📈 Stats globales (total, gagnés, etc.)

### 2. Suivi.md 📋
**Vue d'ensemble** de TOUS les prospects sous forme de tableau.

### 3. Index-Statuts.md 📑
Prospects **groupés par statut** :
- Tous les "à contacter"
- Tous les "contacté"
- Tous les "chaud"
- etc.

### 4. Index-Zones.md 🗺️
Prospects **groupés par ville** :
- Paris (5 prospects)
- Lyon (3 prospects)
- etc.

### 5. Index-Metiers.md 🛠️
Prospects **groupés par métier** :
- Plombier (2)
- Kebab (3)
- Burger (4)
- etc.

---

## 🛠️ Pour les développeurs (agent)

### Ajouter un prospect via script

```python
from hermes_tools import write_file

content = """---
nom: "Nouveau Prospect"
type: "Artisan"
metier: "Plombier"
zone: "Lyon"
statut: "à_contacter"
priorite: "haute"
site_actuel: ""
techno: "N/A"
telephone: "04 78 00 00 00"
email: ""
tags:
  - "sans_site"
  - "artisanat"
---

# Nouveau Prospect

## 📋 Infos générales
...
"""

write_file("~/Documents/Obsidian Vault/Prospection/Artisans/Nouveau_Prospect.md", content)
```

### Régénérer les index

```bash
cd ~/Documents/Obsidian\ Vault/Prospection
python update_index.py
git add -A
git commit -m "feat: ajout prospect X + maj index"
git push origin main
```

---

## 💡 Astuces

1. **Utilise les wikilinks** `[[Nom du fichier]]` dans Obsidian pour naviguer rapidement
2. **Les tags** dans le YAML permettent de filtrer : `sans_site`, `refonte`, `restauration`, `artisanat`
3. **La priorité** `haute` = toujours contacter en premier
4. **Le Dashboard** est ton point d'entrée chaque matin
5. **Après chaque modification** → régénérer les index pour voir les changements

---

## 🔗 Liens utiles

- **Repo GitHub** : https://github.com/floclawww/prospection-nextjs
- **Méthodologie de prospection** : [[Méthodologie]]
- **Template fiche** : [[Templates/Fiche-Prospect]]
- **Template email** : [[Templates/Email-Prospection]]

---

*Dernière mise à jour : auto-générée depuis les fiches YAML*
