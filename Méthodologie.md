# 📖 Méthodologie de Prospection

## 🔍 Étape 1: Trouver les prospects

### Outils recommandés
1. **Google Maps** (gratuit)
   - Rechercher "plombier [ville]" ou "kebab [ville]"
   - Vérifier s'ils ont un site web dans la fiche
   - Noter: nom, adresse, téléphone, site actuel

2. **Pages Jaunes** (pagesjaunes.fr)
   - Filtrer par métier et zone géographique
   - Exporter les contacts (fonction payante disponible)
   - Identifier ceux sans site web

3. **La Fourchette / TripAdvisor**
   - Restaurants sans site = prospects chauds
   - Vérifier la qualité du site s'il existe

4. **OpenStreetMap / Overpass Turbo** (gratuit, technique)
   - Requêtes pour extraire des POIs par zone
   - Utile pour les campagnes massives

### Recherches Google efficaces
```
plombier "site en construction" [ville]
restaurant "pas de site web" [ville]
électricien "WordPress" [ville]
kebab "Wix" [ville]
```

## ⚡ Étape 2: Audit rapide (2 minutes)

### Vérifier la techno du site
```bash
# Détecter WordPress
curl -s https://site.com | grep -i "wp-content"

# Détecter Wix
curl -s https://site.com | grep -i "wix"

# Vérifier HTTPS
curl -I https://site.com 2>/dev/null | head -1
```

### PageSpeed Insights (Google)
- Aller sur https://pagespeed.web.dev/
- Tester l'URL du prospect
- Noter le score mobile (si < 50 = prospect chaud)

### Vérifier le SEO basique
- Le site apparaît-il en 1ère page pour "[métier] [ville]" ?
- A-t-il des pages Google Business / avis ?
- Le site est-il responsive sur mobile ?

## 📝 Étape 3: Remplir la fiche Obsidian

Utiliser le template: [[Templates/Fiche-Prospect]]

Champs obligatoires:
- ✅ Nom de l'entreprise
- ✅ Zone géographique
- ✅ Téléphone
- ✅ Site actuel (et défauts)
- ✅ 2-3 leviers de vente concrets

## 📧 Étape 4: Contacter

### Email (préféré)
- Utiliser le template: [[Templates/Email-Prospection]]
- Personnaliser avec 1 détail réel du prospect
- Mentionner un chiffre concret (score PageSpeed, temps de chargement)
- Proposer un audit gratuit de 15 min

### Téléphone
- Script: "Bonjour, je suis Flo, développeur web. J'ai remarqué que votre site [détail]. Je propose des audits gratuits, ça vous dit qu'on en discute 5 minutes ?"

### Passage sur place (très efficace pour fast-food)
- Commander un produit
- Discuter avec le patron après le service
- Montrer le site sur mobile en direct

## 🔄 Étape 5: Suivi

- J+3: Relance email courte si pas de réponse
- J+7: Deuxième relance
- J+15: Dernière relance, puis passer à froid

Noter tout dans: [[Suivi]]

## 🎯 Zones prioritaires à cibler

1. **Artisans**: Plombiers, électriciens, serruriers, menuisiers (urgence = besoin immédiat de visibilité)
2. **Fast-Food**: Kebabs, burgers, tacos (concurrence forte = besoin de différenciation digitale)
3. **Restaurants**: Indépendants sans chaîne (réservation en ligne = argument fort)

## 💡 Astuce pro

Créer un **audit visuel** en 2 clics:
1. Screenshot du site actuel du prospect
2. Screenshot d'un site Next.js rapide
3. Côte à côte = choc visuel immédiat
