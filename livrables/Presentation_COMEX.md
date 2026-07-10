# Application mobile IA — Recommandation vestimentaire

**Présentation au COMEX — Fashion-Insta**
*Auteur : IA Product Manager — Équipe Produit (VP : Alicia)*
*Durée : 20 minutes + Q&A*

---

## Slide 1 — Résumé exécutif *(slide non présentée à l'oral)*

- **Quoi** : application mobile IA permettant à l'utilisateur de recevoir des recommandations vestimentaires à partir de photos de sa garde-robe et de ses préférences, **et d'acheter sans quitter l'application**.
- **Pourquoi** : booster les ventes e-commerce, différencier Fashion-Insta face à un concurrent qui prépare la même offre, créer une nouvelle interaction client à forte valeur.
- **Combien** : **~141 k€ d'investissement initial**, **~83 k€ de coûts annuels récurrents**, **rentabilité dès l'année 1** sur la base des projections marketing.
- **Quand** : MVP livrable en **6 sprints (~3 mois)** en méthode SCRUM, présentation au store dès le sprint 6.
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

| Année | Utilisateurs actifs | Panier additionnel / user / an | Gains annuels |
|---|---|---|---|
| An 1 | 50 000 | 25 € | 1,25 M€ |
| An 2 | 150 000 | 25 € | 3,75 M€ |
| An 3 | 280 000 | 25 € | 7,00 M€ |
| An 4 | 380 000 | 25 € | 9,50 M€ |
| An 5 | 450 000 | 25 € | 11,25 M€ |

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
| Coûts annuels récurrents (maintenance 15 %, Azure prod, ré-entraînement, DPO) | **~83 k€/an** |

> Détail complet dans le fichier `Chiffrage_Couts_Rentabilite.xlsx`.

---

## Slide 5 — Rentabilité

**Coûts vs gains cumulés sur 5 ans**

| € | An 0 | An 1 | An 2 | An 3 | An 4 | An 5 |
|---|---|---|---|---|---|---|
| Coûts cumulés | 141 k | 224 k | 307 k | 391 k | 474 k | 557 k |
| Gains cumulés | 0 | 1 250 k | 5 000 k | 12 000 k | 21 500 k | 32 750 k |
| **Solde cumulé** | **-141 k** | **+1 026 k** | **+4 693 k** | **+11 609 k** | **+21 026 k** | **+32 193 k** |

→ **Rentabilité atteinte dès l'année 1** (cf. graphique dans `Chiffrage_Couts_Rentabilite.xlsx`, onglet *Rentabilité*).

> Note : ces gains sont des hypothèses fournies par le marketing. La rentabilité reste positive même avec une division par 3 de l'hypothèse.

---

## Slide 6 — Méthode agile SCRUM (1/2)

- **Pourquoi SCRUM** : projet IA = incertitude technique + cible mouvante → besoin de boucles de feedback courtes.
- **Sprints** : 2 semaines, livrable potentiellement déployable à chaque fin de sprint.
- **MVP livré au sprint 3** : recommandation IA (garde-robe + préférences) **jusqu'à l'achat** (panier, livraison, paiement) → on mesure directement la conversion, pas seulement l'intérêt.

---

## Slide 7 — Méthode agile SCRUM (2/2) — cérémonies et suivi

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

## Slide 8 — Planning des sprints et contenu

| Sprint | Thème | US clés | Charge (j) | Livrable |
|---|---|---|---|---|
| Sprint 1 | Socle utilisateur & ingestion | US01, US02 | 20 | Compte + capture photo |
| Sprint 2 | Garde-robe & 1er modèle IA | US03, US04, US08 | 43 | Détection vêtements (PoC) |
| Sprint 3 | **MVP IA + tunnel d'achat** | US05, US09, US11, US16, US17 | 60 | **MVP recommandation → panier → paiement** |
| Sprint 4 | RGPD & feedback | US06, US12, US13, US14 | 43 | Conformité RGPD |
| Sprint 5 | Personnalisation & purge | US07, US15 | 16 | Personnalisation + purge auto |
| Sprint 6 | Sources externes & polissage | US10 | 10 | Sources d'inspiration |
| **Total** | | | **192 j** | |

> Détails dans `Backlog_Fashion_Insta.xlsx`, onglet *Planning sprints*.

---

## Slide 9 — Enjeux légaux : RGPD

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

## Slide 10 — Enjeux éthiques : biais et collecte

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

## Slide 11 — Plan d'action de mitigation des risques

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

## Slide 12 — Demande au COMEX

- **Go demandé** pour engager les 141 k€ d'investissement initial.
- **Engagement** : MVP testable en 6 semaines, déploiement complet à 3 mois.
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
