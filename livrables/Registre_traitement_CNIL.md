# Registre des traitements de données personnelles — Fashion-Insta

> Version narrative de synthèse. **Le registre officiel, au format du gabarit CNIL transmis par le DPO, est rempli dans `Registre_traitement_CNIL.ods`** (onglet 2 : liste des 4 traitements ; onglet 3 : fiche détaillée du traitement T-001). Ce document reprend le même contenu sous une forme plus lisible pour la présentation au COMEX.
> Périmètre : traitements IA de l'application mobile de recommandation.

---

## 1. Coordonnées

| Rôle | Identité |
|---|---|
| Responsable de traitement | Fashion-Insta SAS — Direction Produit (représentée par Alicia, VP Product) |
| Délégué à la Protection des Données (DPO) | DPO Fashion-Insta — dpo@fashion-insta.com |
| Sous-traitants | Microsoft Azure (hébergement & inférence), Cabinet Data Science (sous-traitant modèles) |

---

## 2. Liste des traitements

| N° | Nom du traitement | Finalité principale | Données sensibles ? |
|---|---|---|---|
| T-001 | **Recommandation vestimentaire basée sur la garde-robe** | Proposer à l'utilisateur des articles correspondant à ses goûts à partir de ses photos | Oui (images de la personne) |
| T-002 | Recommandation basée sur les préférences déclarées | Proposer des articles à partir de styles/marques/sources sélectionnés | Non |
| T-003 | Gestion du compte utilisateur | Authentification et gestion des droits | Non |
| T-004 | Mesure d'audience / amélioration produit | Analyse statistique anonymisée | Non |

---

## 3. Fiche détaillée — Traitement T-001 (US04 + US05)

### 3.1 Identification

| Champ | Valeur |
|---|---|
| Nom du traitement | Recommandation vestimentaire basée sur la garde-robe |
| N° / Réf | T-001 |
| Date de création | 2026-05-15 |
| Dernière mise à jour | 2026-05-15 |

### 3.2 Finalités

- **Finalité principale** : proposer des articles du catalogue Fashion-Insta correspondant au style vestimentaire de l'utilisateur.
- **Sous-finalité 1** : détection / segmentation automatique des vêtements présents sur les photos.
- **Sous-finalité 2** : génération d'un vecteur d'embedding du style utilisateur.
- **Sous-finalité 3** : matching avec le catalogue produits et restitution dans l'application.
- **Sous-finalité 4** : ré-entraînement périodique du modèle à partir du feedback utilisateur.

### 3.3 Base légale

Consentement explicite de l'utilisateur (article 6.1.a et 9.2.a du RGPD), recueilli avant la première prise de photo, avec information claire sur l'usage IA.

### 3.4 Catégories de données traitées

| Catégorie | Description | Donnée sensible | Durée de conservation |
|---|---|---|---|
| État civil / identification | Adresse mail, identifiant utilisateur | Non | Durée du compte + 12 mois |
| **Images de la personne** | Photos prises par l'utilisateur en portant ses vêtements | **Oui (données biométriques au sens large + image)** | **12 mois sans activité, ou suppression immédiate sur demande** |
| Embeddings dérivés | Représentation vectorielle du style (issue du modèle) | Oui (pseudonyme fort dérivé de données sensibles) | Mêmes durées que les images |
| Préférences déclarées | Styles, marques, sources | Non | Durée du compte |
| Feedback recommandations | Like / dislike par produit | Non | 36 mois (pour ré-entraînement) |

### 3.5 Catégories de personnes concernées

- Clients / prospects de Fashion-Insta ayant créé un compte sur l'application mobile et activé le service de recommandation.

### 3.6 Destinataires

| Destinataire | Type | Précisions |
|---|---|---|
| Équipe Produit & Data Fashion-Insta | Service interne | Accès aux données pseudonymisées uniquement |
| Sous-traitant Data Science | Sous-traitant | Encadré par un contrat de sous-traitance RGPD (art. 28) |
| Microsoft Azure (France Centre / West Europe) | Hébergeur | Convention de sous-traitance, données chiffrées au repos et en transit |

### 3.7 Transferts hors UE

Aucun. L'ensemble du traitement est hébergé sur des régions Azure UE (France Central + West Europe en redondance). Si un transfert devenait nécessaire, des clauses contractuelles types (CCT) seraient mises en place.

### 3.8 Mesures de sécurité

| Type | Précisions |
|---|---|
| Contrôle d'accès | Authentification forte (MFA) pour les administrateurs ; ACL par rôle pour l'accès aux données |
| Chiffrement | AES-256 au repos (Blob Storage), TLS 1.3 en transit |
| Pseudonymisation | Séparation logique entre identifiants utilisateurs et embeddings |
| Journalisation | Logs d'accès aux images, conservés 12 mois, supervisés (Defender for Cloud) |
| Sauvegarde | Snapshots quotidiens, redondance ZRS |
| Purge automatique | Job planifié supprimant les images au-delà de 12 mois d'inactivité (US15) |
| Sensibilisation | Charte de sécurité, formation RGPD annuelle des équipes |
| Sous-traitants | Contrats art. 28, audits annuels |

### 3.9 Droits des personnes

- **Information** : politique de confidentialité accessible dans l'application, écran d'onboarding dédié à l'IA.
- **Consentement** : opt-in explicite, retirable à tout moment via le menu Paramètres.
- **Accès / rectification / suppression** (US13) : disponibles depuis l'application en self-service.
- **Portabilité** : export JSON sur demande au DPO.
- **Opposition / désinscription** (US14) : déclenche la suppression des images et embeddings sous 30 jours.

### 3.10 Analyse d'Impact (AIPD / DPIA)

Compte tenu :
- du traitement à grande échelle d'images de personnes,
- de l'usage d'un algorithme d'apprentissage automatique,
- du risque de biais discriminatoire,

une **AIPD complète est obligatoire** avant la mise en production (art. 35 RGPD). Elle sera conduite par le DPO avec l'équipe Data Science et présentée pour avis avant le go/no-go production.

---

## 4. Enjeux éthiques & biais identifiés (T-001)

| Problématique | Description | Mitigation |
|---|---|---|
| **Biais de représentativité** | Les jeux d'entraînement publics (DeepFashion, etc.) sont dominés par des modèles caucasiens, minces, valides — la recommandation pourrait moins bien fonctionner pour certaines morphologies, couleurs de peau, genres | Audit du dataset (statistiques de représentation), enrichissement avec données diverses, tests d'équité (parité de qualité par sous-groupes) avant chaque release |
| **Biais commercial** | Le modèle pourrait sur-pousser les articles à forte marge | Séparer scoring de pertinence et logique commerciale, surveillance des écarts |
| **Stéréotype de genre** | Recommandations genrées par défaut sur la base d'apparence | Permettre à l'utilisateur de désactiver l'inférence de genre, ne pas inférer le genre automatiquement |
| **Effet bulle de filtre** | Renforcement excessif des goûts existants | Diversifier les recommandations (taux d'exploration ≥ 10%) |
| **Consentement éclairé** | L'utilisateur peut sous-estimer ce qu'il accepte en téléversant une photo | Onboarding pédagogique, exemples concrets, langage non juridique |
| **Réutilisation hors finalité** | Tentation d'utiliser les photos pour d'autres usages (ciblage publicitaire, etc.) | Finalité limitée par design, audit par le DPO, séparation des environnements |
| **Sécurité des images** | Fuite de photos = atteinte grave (intimité) | Chiffrement, contrôle d'accès strict, plan de réponse incident |

---

## 5. Synthèse — points de vigilance pour le COMEX

1. Les images utilisateurs sont des **données à caractère personnel hautement sensibles**, qui imposent une AIPD avant production.
2. Le **consentement explicite et révocable** doit être la pierre angulaire du parcours utilisateur.
3. Les **biais du modèle** doivent être mesurés en continu (KPI d'équité) et publiés en interne.
4. La **localisation UE** des données et le **chiffrement bout-en-bout** sont des prérequis non négociables.
5. La **purge automatique** (US15) garantit la minimisation de la conservation, attendue par le DPO.
