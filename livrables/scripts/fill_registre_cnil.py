"""Remplit le gabarit CNIL fourni (registre-traitement-simplifie.ods) avec les
données réelles du traitement IA de recommandation Fashion-Insta.

Onglets touchés :
- '2_-_Liste_des_traitements' : identité du responsable/DPO + liste des 4 traitements
  (l'exemple CNIL de la ligne 9 est conservé tel quel, nos données démarrent ligne 10)
- '3_-_Modèle_de_fiche_de_registre' : fiche complète pour T-001 (recommandation
  garde-robe), le traitement le plus sensible (images de personnes)

Onglets non modifiés : 'Tutoriel', '4_-_Exemple_de_fiche' (exemple CNIL de
référence), '5_-_Listes' (listes déroulantes).
"""
from pathlib import Path
from odf.opendocument import load
from odf.table import Table, TableRow
from odf.text import P, LineBreak

ROOT = Path(__file__).resolve().parents[2]
TEMPLATE = ROOT / "pieces_jointes" / "registre-traitement-simplifie.ods"
OUT = ROOT / "livrables" / "Registre_traitement_CNIL.ods"


def set_text(cell, text):
    """Remplace le contenu d'une cellule par du texte (multi-lignes géré)."""
    for child in list(cell.childNodes):
        cell.removeChild(child)
    if not text:
        return
    lines = str(text).split("\n")
    p = P()
    for i, line in enumerate(lines):
        if i > 0:
            p.addElement(LineBreak())
        p.addText(line)
    cell.addElement(p)


def cell(row, idx):
    return row.childNodes[idx]


def fill(row, values):
    """values: dict {index_colonne_enfant: texte}"""
    for idx, text in values.items():
        set_text(cell(row, idx), text)


def get_table(doc, name):
    for t in doc.spreadsheet.getElementsByType(Table):
        if t.getAttribute("name") == name:
            return t
    raise KeyError(name)


def build():
    doc = load(str(TEMPLATE))

    # ---------- Onglet 2 : Liste des traitements ----------
    t2 = get_table(doc, "2_-_Liste_des_traitements")
    rows2 = t2.getElementsByType(TableRow)

    RESPONSABLE_NOM = "Fashion-Insta SAS"
    RESPONSABLE_ADR = "12 rue de la Mode"
    RESPONSABLE_CP = "75002"
    RESPONSABLE_VILLE = "Paris"
    RESPONSABLE_TEL = "01 XX XX XX XX"
    RESPONSABLE_MAIL = "rgpd@fashion-insta.com"

    # Row 0-1 : Responsable de traitement
    fill(rows2[0], {2: RESPONSABLE_NOM, 4: "(personne morale)", 6: RESPONSABLE_ADR, 8: RESPONSABLE_MAIL})
    fill(rows2[1], {2: RESPONSABLE_CP, 4: RESPONSABLE_VILLE, 6: RESPONSABLE_TEL})

    # Row 2-3 : Représentant (non applicable, responsable établi en UE)
    fill(rows2[2], {2: "Non applicable — responsable de traitement établi dans l'UE (France)"})

    # Row 4-5 : DPO
    fill(rows2[4], {2: "DPO Fashion-Insta", 4: "", 6: "N/A (DPO interne)", 8: RESPONSABLE_ADR})
    fill(rows2[5], {2: RESPONSABLE_CP, 4: RESPONSABLE_VILLE, 6: RESPONSABLE_TEL, 8: "dpo@fashion-insta.com"})

    # Rows 9-12 : nos 4 traitements (la ligne 8 = exemple CNIL, conservée telle quelle)
    traitements = [
        ("Recommandation vestimentaire basée sur la garde-robe", "T-001", "15/05/2026", "10/07/2026",
         "Proposer des articles du catalogue Fashion-Insta correspondant au style vestimentaire de "
         "l'utilisateur à partir de ses photos de garde-robe (détection, embeddings, matching, "
         "ré-entraînement périodique)", "Oui"),
        ("Recommandation basée sur les préférences et tendances déclarées", "T-002", "15/05/2026", "10/07/2026",
         "Proposer des articles à partir des styles, marques et sources d'inspiration sélectionnés "
         "par l'utilisateur", "Non"),
        ("Gestion du compte utilisateur", "T-003", "15/05/2026", "10/07/2026",
         "Authentification et gestion des droits de l'utilisateur sur l'application", "Non"),
        ("Mesure d'audience / amélioration produit", "T-004", "15/05/2026", "10/07/2026",
         "Analyse statistique anonymisée de l'usage de l'application pour l'amélioration produit", "Non"),
    ]
    for offset, (nom, ref, creation, maj, finalite, sensible) in enumerate(traitements, start=9):
        fill(rows2[offset], {0: nom, 1: ref, 2: creation, 3: maj, 4: finalite, 6: sensible})

    # ---------- Onglet 3 : Fiche T-001 ----------
    t3 = get_table(doc, "3_-_Modèle_de_fiche_de_registre")
    rows3 = t3.getElementsByType(TableRow)

    fill(rows3[0], {4: "T-001"})
    fill(rows3[3], {1: "Recommandation vestimentaire basée sur la garde-robe"})
    fill(rows3[4], {1: "T-001"})
    fill(rows3[5], {1: "15/05/2026"})
    fill(rows3[6], {1: "10/07/2026"})

    # Acteurs (Nom | ... | Téléphone | Adresse mél)
    fill(rows3[9], {  # Responsable du traitement
        1: f"{RESPONSABLE_NOM} — Direction Produit (Alicia, VP Product), {RESPONSABLE_ADR}, "
           f"{RESPONSABLE_CP} {RESPONSABLE_VILLE}, France",
        3: RESPONSABLE_TEL,
        4: RESPONSABLE_MAIL,
    })
    fill(rows3[10], {  # DPO
        1: f"DPO Fashion-Insta, {RESPONSABLE_ADR}, {RESPONSABLE_CP} {RESPONSABLE_VILLE}, France",
        3: RESPONSABLE_TEL,
        4: "dpo@fashion-insta.com",
    })
    fill(rows3[11], {1: "N/A (DPO interne à Fashion-Insta)"})
    fill(rows3[12], {1: "Non applicable (responsable établi dans l'UE)"})
    fill(rows3[13], {1: "Non applicable"})

    # Finalités
    fill(rows3[16], {1: "Proposer des articles du catalogue Fashion-Insta correspondant au style "
                         "vestimentaire de l'utilisateur, à partir de ses photos de garde-robe"})
    fill(rows3[17], {1: "Détection / segmentation automatique des vêtements présents sur les photos"})
    fill(rows3[18], {1: "Génération d'un vecteur d'embedding du style utilisateur"})
    fill(rows3[19], {1: "Matching avec le catalogue produits et restitution dans l'application"})
    fill(rows3[20], {1: "Ré-entraînement périodique du modèle à partir du feedback utilisateur"})

    # Catégories de données personnelles (non sensibles)
    fill(rows3[24], {  # État civil, identité, images...
        1: "Adresse mail, identifiant utilisateur ; photos de l'utilisateur portant ses vêtements "
           "(image de la personne) ; embeddings de style dérivés des photos (représentation "
           "vectorielle, pseudonyme fort)",
        3: "Compte : durée du compte + 12 mois. Photos et embeddings : 12 mois sans activité, "
           "ou suppression immédiate sur demande",
    })
    fill(rows3[25], {  # Vie personnelle
        1: "Préférences de style, marques et sources d'inspiration déclarées ; retours "
           "j'aime/je n'aime pas sur les recommandations",
        3: "Durée du compte (préférences) ; 36 mois (feedback, pour ré-entraînement)",
    })
    fill(rows3[26], {1: "Non concerné (aucune donnée économique/financière dans ce traitement)", 3: "—"})
    fill(rows3[27], {1: "Logs d'accès aux images (journalisation de sécurité)", 3: "12 mois"})
    fill(rows3[28], {1: "Non concerné", 3: "—"})
    fill(rows3[29], {1: "Non concerné", 3: "—"})

    # Données sensibles
    fill(rows3[32], {1: "Non collectée explicitement ; risque de biais indirect via les photos "
                         "(cf. analyse des biais du modèle)", 3: "—"})
    fill(rows3[33], {1: "Non concerné", 3: "—"})
    fill(rows3[34], {1: "Non concerné", 3: "—"})
    fill(rows3[35], {1: "Non concerné", 3: "—"})
    fill(rows3[36], {1: "Non concerné", 3: "—"})
    fill(rows3[37], {  # Données biométriques
        1: "Photos de la personne portant ses vêtements et embeddings de style dérivés, traités "
           "par précaution comme données sensibles (image de la personne), bien que non utilisés "
           "à des fins d'identification biométrique stricte",
        3: "12 mois sans activité, ou suppression immédiate sur demande",
    })
    fill(rows3[38], {1: "Non concerné", 3: "—"})
    fill(rows3[39], {1: "Non concerné", 3: "—"})
    fill(rows3[40], {1: "Non concerné", 3: "—"})

    # Catégories de personnes concernées
    fill(rows3[43], {1: "Clients", 3: "Clients/prospects de Fashion-Insta ayant créé un compte sur "
                                       "l'application mobile et activé le service de recommandation"})

    # Destinataires
    fill(rows3[47], {1: "Service interne qui traite les données",
                      3: "Équipe Produit & Data Fashion-Insta — accès aux données pseudonymisées uniquement"})
    fill(rows3[48], {1: "Sous-traitants",
                      3: "Cabinet Data Science (sous-traitant modèles), encadré par un contrat de "
                         "sous-traitance RGPD (art. 28)"})
    fill(rows3[49], {1: "Sous-traitants",
                      3: "Microsoft Azure (hébergement & inférence), régions France Central / West "
                         "Europe, convention de sous-traitance"})

    # Mesures de sécurité
    fill(rows3[53], {1: "Chiffrement des données",
                      3: "AES-256 au repos (Blob Storage), TLS 1.3 en transit"})
    fill(rows3[54], {1: "Contrôle d'accès des utilisateurs",
                      3: "Authentification forte (MFA) pour les administrateurs, ACL par rôle, "
                         "séparation identifiants/embeddings (pseudonymisation)"})
    fill(rows3[55], {1: "Sauvegarde des données",
                      3: "Snapshots quotidiens, redondance ZRS, purge automatique après 12 mois "
                         "d'inactivité (US15)"})

    # Transferts hors UE : aucun
    fill(rows3[58], {
        1: "Sans objet — aucun transfert hors UE à ce jour",
        2: "",
        3: "",
        5: "Hébergement exclusif sur les régions Azure UE (France Central + West Europe). Si un "
           "transfert devenait nécessaire, des clauses contractuelles types (CCT) seraient mises en place.",
    })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(OUT))
    print(f"Saved {OUT}")


if __name__ == "__main__":
    build()
