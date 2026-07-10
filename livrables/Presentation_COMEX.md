# Application mobile IA — Recommandation vestimentaire

**Présentation au COMEX — Fashion-Insta**
*Auteur : IA Product Manager — Équipe Produit (VP : Alicia)*
*Durée : 25 minutes + Q&A*

---

## Slide 1 — Résumé exécutif *(slide non présentée à l'oral)*

- **Quoi** : application mobile IA permettant à l'utilisateur de recevoir des recommandations vestimentaires à partir de photos de sa garde-robe et de ses préférences, **et d'acheter sans quitter l'application**.
- **Pourquoi** : booster les ventes e-commerce, différencier Fashion-Insta face à un concurrent qui prépare la même offre, créer une nouvelle interaction client à forte valeur.
- **Combien** : **~141 k€ d'investissement initial**, **~82 k€ de coûts annuels récurrents en An 1** (jusqu'à ~146 k€ en An 5, indexés sur la croissance des utilisateurs), **rentabilité atteinte en année 4** sur la base des projections marketing (utilisateurs × taux de conversion × marge).
- **Quand** : MVP livrable en **6 sprints (~13 semaines, ~3 mois)** en méthode SCRUM, présentation au store dès le sprint 6.
- **Risques majeurs** : protection des données image (RGPD), biais du modèle IA, dépendance au sous-traitant data science, pression concurrentielle. Tous **maîtrisés par un plan d'action documenté**.
- **Demande au COMEX** : **GO** pour engager le projet.

---

## Slide 2 — Le contexte et l'opportunité

- Marché de la mode en ligne sous pression : différenciation par l'expérience et la personnalisation.
- Fashion-Insta = réseau physique + e-commerce existant → l'application étend le canal, sans le redéfinir.
- Un concurrent prépare une offre similaire → **first mover advantage** crucial.
- L'application IA = levier d'upsell et de fidélisation, **complémentaire** au site existant.

---

## Slide 3 — Objectifs & gains attendus

**Objectifs métier**
1. Augmenter le panier moyen sur le canal mobile.
2. Réduire le taux de retour produit (meilleur ciblage du goût).
3. Fidéliser via une expérience personnalisée unique.

**Gains attendus (estimations marketing)**

Le gain n'est pas "utilisateurs actifs × panier" — un utilisateur actif (qui ouvre l'appli) n'est pas un acheteur. Le calcul applique un **taux de conversion** (part des actifs qui achètent réellement via la recommandation) et une **marge brute** (pour raisonner en gain net, comparable aux coûts, et non en chiffre d'affaires brut) :

> Gain net = utilisateurs actifs × taux de conversion (8 %, aligné sur le KPI cible ≥5 %) × panier additionnel (25 €) × marge brute retail (45 %)

| Année | Utilisateurs actifs | Gain net annuel |
|---|---|---|
| An 1 | 50 000 | 45 k€ |
| An 2 | 150 000 | 135 k€ |
| An 3 | 280 000 | 252 k€ |
| An 4 | 380 000 | 342 k€ |
| An 5 | 450 000 | 405 k€ |

**KPI de succès (évaluation)**

| KPI | Cible An 1 |
|---|---|
| Utilisateurs actifs mensuels (MAU) | ≥ 50 k |
| Taux d'acceptation des recommandations | ≥ 25 % |
| Conversion reco → achat | ≥ 5 % |
| NPS (Net Promoter Score) | ≥ 30 |
| Score d'équité IA (parité par segment) | écart < 5 % |

> **Pourquoi le panier et le paiement sont dans le périmètre** : une recommandation qui n'aboutit pas à un achat *dans l'application* ne génère aucun des gains ci-dessus. Renvoyer l'utilisateur vers le site web pour payer casse le parcours et fait chuter la conversion — le KPI « conversion reco → achat ≥ 5 % » n'est d'ailleurs mesurable que si l'achat se termine dans l'app. Le backlog inclut donc désormais le tunnel panier/livraison/paiement (US16, US17), qui **réutilise le back-end e-commerce existant** (pas de nouvelle plateforme de paiement) : le site web n'est donc pas redéveloppé, seulement exposé dans l'app.

---

## Slide 4 — Ressources humaines et techniques

**Équipe projet (SCRUM)**

| Profil | Effort | Rôle |
|---|---|---|
| Product Owner (Alicia) | partiel | Vision, priorisation, validation US |
| Scrum Master | partiel | Animation cérémonies, levée d'obstacles |
| Tech Lead | partiel | Architecture, qualité technique |
| Data Scientist junior | plein | Implémentation modèles, MLOps |
| Data Scientist senior (sous-traitant) | partiel | Expertise CV, modèles avancés |
| ML / Computer Vision Engineer | plein | Pipeline d'inférence, optim |
| Développeur mobile | plein | iOS + Android |
| DevOps / Cloud Azure | partiel | Infra, sécurité, MLOps |
| UX / UI Designer | partiel | Parcours, design |
| QA / Testeur | partiel | Recette, tests d'équité |

**Stack technique**
- Cloud : **Microsoft Azure** (Azure ML, App Service, Blob Storage, Cosmos DB, Azure DevOps)
- Mobile : React Native (iOS + Android)
- IA : PyTorch + Azure ML, vision (segmentation + embeddings)

**Budget global**

| Poste | Montant |
|---|---|
| Coût RH initial (équipe sur la phase projet, dont tunnel d'achat) | ~127 k€ |
| Coût Azure initial (entraînement + dev) | ~14 k€ |
| **Total investissement one-shot** | **~141 k€** |
| Coûts annuels récurrents (maintenance 15 %, Azure prod, ré-entraînement, DPO) | **~82 k€/an en An 1 → ~146 k€/an en An 5** |

> Les coûts Azure de production (hébergement, inférence, stockage) sont indexés sur la croissance des utilisateurs actifs (facteur √(utilisateurs/50k)) — ils ne restent pas plats alors que la base d'utilisateurs croît x9 entre l'An 1 et l'An 5. Le poste sécurité/monitoring n'inclut plus de SIEM Sentinel (coût disproportionné pour ce périmètre : quelques dizaines de Go/mois ingérés suffiraient à dépasser le budget dédié) ; seul Microsoft Defender for Cloud est conservé.

> Détail complet dans le fichier `Chiffrage_Couts_Rentabilite.xlsx`.

---

## Slide 5 — Zoom : d'où viennent les coûts récurrents (82 k€ → 146 k€) ?

**Composition détaillée (base An 1, à 50 000 utilisateurs actifs)**

| Poste | Montant An 1 | Type | D'où ça vient |
|---|---|---|---|
| Maintenance applicative | 19 k€ | Fixe | 15 % du coût RH initial (127 k€) — bugs, correctifs, évolutions mineures |
| Hébergement (Azure App Service) | 12 k€ | Variable | API de recommandation, auto-scaling |
| Inférence ML (Azure ML Endpoint) | 14 k€ | Variable | Calcul des recommandations, ~1M requêtes/mois (CPU) |
| Stockage Blob (photos utilisateurs) | 6 k€ | Variable | Photos garde-robe, chiffrées, redondance ZRS |
| Base de données managée | 5 k€ | Fixe | Comptes utilisateurs + préférences |
| Sécurité & monitoring | 2 k€ | Fixe | Microsoft Defender for Cloud |
| Ré-entraînement des modèles IA | 18 k€ | Fixe | Compute + 20 j Data Scientist junior, pour intégrer nouvelles données/tendances |
| DPO / RGPD | 6 k€ | Fixe | Veille réglementaire + audits annuels |
| **TOTAL An 1** | **82 k€** | | |

**Pourquoi ça monte à 146 k€ en An 5 ?**

Seuls 3 postes sont "Variable" (hébergement + inférence + stockage = 32 k€ sur les 82 k€) : ils augmentent logiquement avec le succès de l'app — plus d'utilisateurs, plus de recommandations calculées, plus de photos stockées. Les 5 autres postes (50 k€) sont fixes, indépendants du nombre d'utilisateurs.

| | An 1 | An 2 | An 3 | An 4 | An 5 |
|---|---|---|---|---|---|
| Utilisateurs actifs | 50 k | 150 k | 280 k | 380 k | 450 k |
| Coûts fixes | 50 k€ | 50 k€ | 50 k€ | 50 k€ | 50 k€ |
| Coûts Azure variables | 32 k€ | 56 k€ | 76 k€ | 88 k€ | 96 k€ |
| **Total récurrent** | **82 k€** | **106 k€** | **126 k€** | **138 k€** | **146 k€** |

> La part variable ne suit pas une croissance linéaire (x9 utilisateurs entre An 1 et An 5) mais une progression en racine carrée — hypothèse d'économies d'échelle standard sur le cloud (mutualisation des ressources, cache, tarifs dégressifs par palier). Sans cette hypothèse, une croissance strictement proportionnelle porterait ce seul poste à ~288 k€ en An 5, ce qui serait surestimé.

> Cette hausse doit se lire **en miroir des gains**, qui croissent eux aussi avec les utilisateurs (45 k€ → 405 k€, cf. slide suivante) : l'augmentation des coûts récurrents accompagne la croissance du service, elle ne la subit pas — c'est le signe que le produit fonctionne.

> Détail chiffré : `Chiffrage_Couts_Rentabilite.xlsx`, onglets *Coûts récurrents* et *Rentabilité*.

---

## Slide 6 — Rentabilité

**Coûts vs gains cumulés sur 5 ans**

| € | An 0 | An 1 | An 2 | An 3 | An 4 | An 5 |
|---|---|---|---|---|---|---|
| Coûts cumulés | 141 k | 223 k | 329 k | 455 k | 593 k | 739 k |
| Gains cumulés | 0 | 45 k | 180 k | 432 k | 774 k | 1 179 k |
| **Solde cumulé** | **-141 k** | **-178 k** | **-149 k** | **-23 k** | **+181 k** | **+440 k** |

→ **Rentabilité atteinte en année 4** (cf. graphique dans `Chiffrage_Couts_Rentabilite.xlsx`, onglet *Rentabilité*).

> Note : ces gains restent des hypothèses marketing (nombre d'utilisateurs actifs, taux de conversion 8 %, panier additionnel 25 €, marge 45 %). Le calcul applique désormais un taux de conversion et une marge — il ne suppose plus que 100 % des utilisateurs actifs achètent, ce qui rend le point de rentabilité (An 4) plus tardif mais plus crédible que l'estimation précédente.

---

## Slide 7 — Méthode agile SCRUM (1/2)

- **Pourquoi SCRUM** : projet IA = incertitude technique + cible mouvante → besoin de boucles de feedback courtes.
- **Sprints** : 2 semaines (**3 semaines pour le Sprint 3**), livrable potentiellement déployable à chaque fin de sprint.
- **MVP livré au sprint 3** : recommandation IA (garde-robe + préférences) **jusqu'à l'achat** (panier, livraison, paiement) → on mesure directement la conversion, pas seulement l'intérêt. Ce sprint porte 60 j de charge (2 moteurs IA + tunnel d'achat complet) : sur 10 j ouvrés (2 semaines), cela demanderait 6 personnes à temps plein en simultané — il est donc étendu à 3 semaines (15 j ouvrés) pour rester réaliste.

---

## Slide 8 — Méthode agile SCRUM (2/2) — cérémonies et suivi

| Cérémonie | Fréquence | Objet |
|---|---|---|
| **Sprint planning** | Début de sprint | Engagement de l'équipe sur les US |
| **Daily scrum** | Tous les jours, 15 min | Synchronisation, levée d'obstacles |
| **Sprint review** | Fin de sprint | Démonstration au PO, ajustement du backlog |
| **Rétrospective** | Fin de sprint | Amélioration continue de l'équipe |
| **Backlog refinement** | 1 fois / sprint | Préparation des US suivantes |
| **Comité de pilotage** | Bi-mensuel | PO + DPO + Sponsor : arbitrages, KPI, risques |

**Suivi de charge** : *burndown chart* mis à jour quotidiennement par le Scrum Master, partagé en daily.

---

## Slide 9 — Planning des sprints et contenu

| Sprint | Thème | US clés | Charge (j) | Durée | Livrable |
|---|---|---|---|---|---|
| Sprint 1 | Socle utilisateur & ingestion | US01, US02 | 20 | 2 sem. | Compte + capture photo |
| Sprint 2 | Garde-robe & 1er modèle IA | US03, US04, US08 | 43 | 2 sem. | Détection vêtements (PoC) |
| Sprint 3 | **MVP IA + tunnel d'achat** | US05, US09, US11, US16, US17 | 60 | **3 sem.** | **MVP recommandation → panier → paiement** |
| Sprint 4 | RGPD & feedback | US06, US12, US13, US14 | 43 | 2 sem. | Conformité RGPD |
| Sprint 5 | Personnalisation & purge | US07, US15 | 16 | 2 sem. | Personnalisation + purge auto |
| Sprint 6 | Sources externes & polissage | US10 | 10 | 2 sem. | Sources d'inspiration |
| **Total** | | | **192 j** | **13 sem.** | |

> Sprint 3 étendu à 3 semaines (15 j ouvrés) : à 2 semaines, ses 60 j de charge auraient demandé 6 personnes à temps plein en simultané sur le sprint le plus critique (2 moteurs IA + tunnel d'achat), sans marge pour les imprévus.
> Détails dans `Backlog_Fashion_Insta.xlsx`, onglet *Planning sprints*.

---

## Slide 10 — Enjeux légaux : RGPD

**Données traitées = données personnelles sensibles (images)**

- Base légale : **consentement explicite et révocable** de l'utilisateur.
- Finalité limitée à la recommandation vestimentaire — pas de réutilisation.
- Durée de conservation : **12 mois max** sans activité, purge automatique.
- Localisation : **régions Azure UE uniquement** (France Central + West Europe).
- Chiffrement systématique au repos et en transit.
- Droits utilisateur (accès, rectification, suppression, portabilité) intégrés dès l'application.
- **AIPD obligatoire** (article 35 RGPD) avant la mise en production, conduite avec le DPO.

> Le registre de traitement complet, au format du gabarit CNIL fourni par le DPO, est livré (`Registre_traitement_CNIL.ods`) ; une synthèse narrative est disponible dans `Registre_traitement_CNIL.md`.

---

## Slide 11 — Enjeux éthiques : biais et collecte

| Biais / enjeu | Mitigation |
|---|---|
| **Représentativité** des datasets (morphologie, origine, genre) | Audit du dataset, enrichissement, métriques d'équité par sous-groupe à chaque release |
| **Stéréotypes de genre** | Pas d'inférence automatique du genre, opt-in utilisateur |
| **Effet bulle de filtre** | Diversité forcée ≥ 10 % dans les recommandations |
| **Biais commercial** (sur-pousser les fortes marges) | Séparation pertinence / logique commerciale, audit |
| **Consentement éclairé** | Onboarding pédagogique, exemples concrets |
| **Transparence** | Charte éthique IA publiée, KPI d'équité dans les revues |

**Comité éthique interne** mis en place dès le lancement du projet.

---

## Slide 12 — Plan d'action de mitigation des risques

> Risques priorisés via le **spectre 7D** (Données, Délais, Dépendances, Dimensionnement, Décisions, Déontologie, Déploiement). Détail dans `Analyse_des_risques.xlsx`.

**Top 5 des risques (criticité = impact × probabilité)**

| # | Axe | Risque | Crit. | Action clé |
|---|---|---|---|---|
| 1 | Données | Modèle biaisé (datasets peu diversifiés) | **9** | Métriques d'équité par sous-groupe + enrichissement du dataset |
| 2 | Données | Fuite des photos utilisateurs | **6** | Chiffrement, MFA, AIPD, pen-test |
| 3 | Délais | Concurrent plus rapide | **6** | MoSCoW strict, MVP au sprint 3 |
| 4 | Dépendances | Indispo. équipe mobile (autre projet) | **6** | Engagement formel + freelance back-up |
| 5 | Déontologie | Polémique éthique IA | **6** | Charte éthique, opt-in clair, comité éthique |

---

## Slide 13 — Demande au COMEX

- **Go demandé** pour engager les 141 k€ d'investissement initial.
- **Engagement** : MVP testable en 7 semaines (fin du Sprint 3), déploiement complet à 13 semaines (~3 mois).
- **Garanties** : conformité RGPD validée par le DPO, KPI de succès suivis en COPIL bi-mensuel, plan de risque actif.
- **Premier livrable de confiance** : à la fin du sprint 3, démonstration du MVP au COMEX.

> *« Soyons les premiers à offrir cette expérience à nos clients. »*

---

## Annexe — Backlog priorisé (extrait)

| ID | Titre | Sprint | MoSCoW | MVP |
|---|---|---|---|---|
| US01 | Création de compte / connexion sécurisée | 1 | MUST | ✅ |
| US02 | Prise de photo et alimentation de la garde-robe | 1 | MUST | ✅ |
| US03 | Gestion de la collection de photos | 2 | MUST | ✅ |
| **US04** | **[IA] Détection / segmentation du vêtement** | **2** | **MUST** | **✅** |
| **US05** | **[IA] Recommandation à partir de la garde-robe** | **3** | **MUST** | **✅** |
| US06 | Affichage du vêtement recommandé sur la photo | 4 | SHOULD | ❌ |
| US07 | Personnalisation couleur/style | 5 | COULD | ❌ |
| US08 | Définition des styles préférés | 2 | MUST | ✅ |
| US09 | Référencement marques préférées | 3 | SHOULD | ❌ |
| US10 | Référencement sources d'inspiration | 6 | COULD | ❌ |
| **US11** | **[IA] Recommandation préférences/tendances** | **3** | **MUST** | **✅** |
| US12 | Avis / feedback sur les recommandations | 4 | SHOULD | ❌ |
| US13 | [RGPD] Consultation/modif/suppression données | 4 | MUST | ✅ |
| US14 | [RGPD] Désinscription + purge à la demande | 4 | MUST | ✅ |
| US15 | [RGPD] Purge automatique après inactivité | 5 | MUST | ✅ |
| **US16** | **[Commande] Panier et validation de commande** | **3** | **MUST** | **✅** |
| **US17** | **[Commande] Livraison et paiement** | **3** | **MUST** | **✅** |

> Les US **MUST + MVP** définissent le périmètre minimal pour une mise en marché crédible et sont les seules à être garanties pour le sprint 3.
> US16/US17 complètent le périmètre initial : sans tunnel d'achat natif, l'application ne génère aucun des gains projetés (une recommandation seule ne vend rien) et le KPI de conversion ne serait pas mesurable. Ces deux US **réutilisent le back-end e-commerce existant** (panier, livraison, paiement) — seule l'intégration mobile est à développer, d'où une charge limitée (13 jours au total).

---

## Annexe — Liste des livrables remis avec ce dossier

1. `Backlog_Fashion_Insta.xlsx` — backlog priorisé MoSCoW + chiffrage par profil + planning sprints
2. `Chiffrage_Couts_Rentabilite.xlsx` — coûts initiaux, récurrents, rentabilité 5 ans + graphique
3. `Registre_traitement_CNIL.ods` — registre officiel (gabarit CNIL du DPO, rempli) pour les 4 traitements, fiche détaillée T-001 ; synthèse narrative dans `Registre_traitement_CNIL.md`
4. `Analyse_des_risques.xlsx` — analyse 7D, criticité, plan d'action
5. `Presentation_COMEX.md` — ce document
