Cette mission suit un scénario de projet professionnel.

Fashion-Insta est une entreprise du monde de la mode qui commercialise des articles vestimentaires. Elle dispose d'un réseau de magasins physiques, mais également d'un site e-commerce qui lui permet de commercialiser ses produits selon ces deux canaux.

Vous êtes IA product manager et vous travaillez dans l'équipe d'Alicia, VP product, pour mener à bien des projets IA au sein de l'entreprise.

Alicia est chargée de construire et d'exécuter la vision produit de l'entreprise. Dans sa roadmap de projets prévus, le projet IA identifié comme ayant le plus de potentiel est le développement d'une application mobile de recommandation d'articles vestimentaires basée sur des photos.

![Data Scientist P10 Banner](https://user.oc-static.com/upload/2023/04/20/16820094601225_Data%20Scientist-P10-01-banner.png)

L'objectif de l'application mobile est de permettre aux utilisateurs de l'application de se prendre en photo avec leurs habits favoris et d'obtenir en retour des recommandations d'articles du même style vestimentaire.

L'application sera réalisée en s'appuyant sur les outils cloud fournis par Microsoft Azure, le partenaire cloud de "Fashion-Insta".

Dans 3 semaines se tient la réunion du comité exécutif (COMEX), qui va décider si ce projet sera lancé. Alicia tient beaucoup à ce projet et vous a confié la tâche d'en réaliser le cadrage et de le présenter durant le COMEX. Elle vous envoie le mail suivant pour cadrer votre démarche.

## le mail de Alicia

De : Alicia
Envoyé : Hier 11:22
À : Vous
Objet : Expression des besoins du projet application mobile IA

Bonjour,

Merci pour ton implication dans ce projet, je suis sûre que ton cadrage de ce projet nous permettra de bien le vendre au COMEX. Cette application va booster nos ventes et donc l'investissement sera rentable très rapidement !

N'oublie pas que dans le cadre de ce projet nous mettons en place une démarche agile basée sur SCRUM.
Nous avons réalisé la semaine dernière un atelier avec l'équipe produit, afin de recenser et formaliser les besoins en termes d'application mobile.
Tu trouveras la synthèse des besoins dans le document joint à ce mail.

Pourrais-tu, à partir de ces besoins, formaliser les user stories dans un backlog et les prioriser ? Cela va nous permettre de planifier leur implémentation lors de différents sprints successifs. Tu peux utiliser le template en pièce jointe. Je t'invite à utiliser la méthode MoSCoW pour prioriser les user stories.

Je serai ton product owner sur ce projet.
Je te propose de faire ensemble une revue du backlog la semaine prochaine, afin d'ajuster ensemble le contenu et les priorités.

À bientôt.

Alicia

Pièces jointes :

- [Expression de besoin](pieces_jointes/expression_de_besoin.md)
- [Template de backlog](pieces_jointes/Template_Backlog.xlsx)

# 1 semaine plus tard

Après votre réunion de revue des user stories avec Alicia, elle vous envoie un nouveau mail pour vous guider dans la suite du cadrage du projet.

## le mail de Alicia

De : Alicia
Envoyé : Aujourd'hui 15:27
À : Vous
Objet : Chiffrage et rentabilité du projet application mobile IA

Bonjour,

Super ton travail sur le backlog, nous avons bien formalisé le périmètre du projet, maintenant il va falloir chiffrer tout cela et surtout démontrer la rentabilité à court ou moyen terme du projet !

Pourrais-tu dans un premier temps estimer pour chaque user story du backlog, la charge en jours de réalisation et sa répartition en % par profil ?
Tu pourras ainsi calculer la charge en jours par profil et le coût par profil après application d'un coût journalier par profil.
Tu en déduiras le coût initial de développement de l'application.
Pense également à estimer les coûts initiaux d'infrastructure Azure pour la phase de conception et d'entraînement des modèles. Azure met à disposition un outil de calcul pour dimensionner l'infrastructure et estimer le coût d'utilisation du cloud.
Pour les coûts annuels de maintenance de l'application, je te propose de prendre par an 15% du coût de développement initial, comme nous faisons toujours sur ce type de projets.
Tu dois également estimer les coûts annuels d'infrastructure Azure de production, afin de gérer l'application et effectuer les prédictions des modèles.
Pour calculer la rentabilité, tu dois prendre les gains annuels générés par l'augmentation de nos ventes, estimés par le marketing. Ceci te permettra de calculer les gains et coûts cumulés année après année et ainsi montrer à quelle date une rentabilité apparaît. Un graphique serait très pertinent pour visualiser cette montée en rentabilité !
Pourrais-tu également planifier les différents sprints et leur contenu en termes de développement en fonction des priorités que nous avons définies ensemble, que tu formaliseras dans un tableau.
Enfin, tu dois décrire toute l'organisation du projet, les profils et leurs rôles, les différents types de points et revues tout au long du projet, de suivi, de pilotage et de (re)planification du projet, toujours dans le cadre de notre démarche agile SCRUM.

Merci, je sais que ça fait beaucoup, mais on va y arriver ensemble !

À bientôt.
Alicia

"Vous ne serez pas jugé sur la pertinence du chiffrage de chaque fonctionnalité, ni sur la pertinence des gains que vous estimerez vous-même, mais sur la démarche de réalisation de cette étape."

# 1 semaine plus tard

Vous avez réalisé et formalisé l'estimation des charges, des coûts et de la rentabilité, que vous avez envoyée à Alicia pour information. Elle vous répond dans la foulée.

De : Alicia
Envoyé : Aujourd'hui 18:34
À : Vous
Objet : Gestion des données personnelles et gestion des risques

Bonjour,

Top ton estimation, je vois que tu as été raisonnable sur les charges. C'est vraiment excellent, tu confirmes mon intuition que le projet est rentable.
Nous pouvons donc poursuivre le cadrage du projet !

J'ai vu le DPO, qui est très vigilant concernant la gestion des données personnelles, en particulier les fonctionnalités de type IA sur des images.

Il attend que tu formalises dans un "registre de traitements", selon le modèle de la [CNIL](pieces_jointes/registre-traitement-simplifie.ods), les traitements orientés IA de recommandation, afin d'être en conformité avec le RGPD et surtout de détecter les risques sur ces données personnelles.

Ce recensement des données personnelles sera pour toi une source pour alimenter ta réflexion sur les enjeux légaux et éthiques, en particulier ceux liés aux biais du modèle et à la collecte des données personnelles.

Tu dois faire une analyse complète des risques concernant la réalisation du projet, en plus de ceux concernant la gestion des données personnelles évoquée ci-dessus : détection des risques, conséquences, priorisation et plan d'action pour maîtriser ces risques.

Cela pourrait impliquer éventuellement des ajustements sur les fonctionnalités du projet, en particulier pour la maîtrise et la sécurité des données personnelles. À toi de voir.

Je t'ai fourni en pièce jointe une note recensant quelques éléments de contexte du projet (facteurs de risque) qui pourraient générer des risques, ainsi qu'un modèle d'analyse des risques.
On fait un point la semaine prochaine pour finaliser la présentation.

À bientôt.

Alicia

Pièce jointe :

- [Context du projet](pieces_jointes/context_projet.md)
- [Modéle Analyse de risques](pieces_jointes/Modèle_analyse_des_risques.xlsx)

# 1 semaine plus tard

Vous avez réalisé et formalisé l'analyse des données personnelles dans le cadre du RGPD et l'analyse des risques du projet.

Alicia semble vraiment satisfaite du travail réalisé. Elle vous envoie un mail précisant ses attentes au sujet de la présentation au COMEX.

## mail de Alicia

De : Alicia
Envoyé : Aujourd'hui 19:37
À : Vous
Objet : Présentation au COMEX – appli mobile

Bonjour,

Merci pour ton travail détaillé sur les données personnelles et les risques.

Effectivement, l'application va gérer des données sensibles et le risque de biais est important. Nous devrons être vraiment rassurants sur ces points lors du COMEX… le DPO sera là !

Comme tu le sais, j'aimerais vraiment que ce projet soit retenu par le COMEX ! Je suis sûre que tu sauras les convaincre.

Pour le support de présentation, voici les éléments qui, à mon avis, devraient être présents :
un résumé de la présentation du projet : la présentation devrait durer 20 min, mais c'est toujours bien d'avoir une slide de résumé des points clés de la présentation pour les absents (les membres du COMEX sont des gens pressés !) — tu ne présenteras donc pas oralement ce slide ;
les objectifs du projet et les gains attendus : pour convaincre un décideur, il faut commencer par ce qu'il peut y gagner — pense notamment à l'évaluation du succès de l'application mobile ;
l'identification des ressources humaines, techniques et financières requises pour la réalisation du projet ;
une présentation brève de la méthode agile : toujours important de rappeler la méthode avec laquelle on travaille et ses avantages — ne dépasse pas 2 à 3 slides pour cette partie ;
un zoom sur l'organisation et le contenu des points de suivi tout au long du projet (daily scrum, sprint review, rétrospective, suivi des charges avec le burndown chart) ;
le planning des sprints et leur contenu ;
les enjeux légaux et éthiques : les principes du RGPD, ainsi que les enjeux éthiques liés aux biais du modèle et à la collecte des données personnelles, qui sont des sujets chauds en ce moment ;
le plan d'action de mitigation des principaux risques identifiés pour le projet : cela permet de rassurer les décideurs vis-à-vis des risques ;
en annexe le backlog du projet : il contient les user stories priorisées à développer pour le projet — tu penseras à indiquer les user stories indispensables pour le MVP, qui évoluera bien entendu en cours de projet.

Je crois beaucoup à ce projet, donc j'espère qu'on fera bonne impression !
Bon courage, j'ai confiance.

Alicia.

Vous l'avez compris, Alicia a placé la barre assez haut… Bonne chance pour le COMEX !

# Etapes

1. Elaborer un backlog de User Story
   - Traduisez le besoin en user stories avec des estimations chiffrées en employant la méthode MoSCow.
   - Concentrez-vous sur des user stories IA, en partant du principe qu'un site web existe déjà.

2. Réaliser un dimensionement de l'équipe, des couts et des gains
   - L'équipe doit adopter la méthodologie SCRUM, quel que soit sa composition.
   - Mettez en évidence entre les coûts d'investissement "one-shot" et les coûts récurrents.
   - Démontrez à partir de quand la rentabilité est visible.

3. Démontrez votre maitrise des enjeux légaux et éthiques
   - Formalisez pour au moins une user story IA les traitements qui impliquent de la donnée personnelle et/ou sensible en utilisant le modèle CNIL.
   - Recensez des biais éventuels ou problématiques éthiques éventuels dans un des traitements IA du projet.

4. identifier les resiques et proposer des stratégies pour les cadrer
   - Utilisez la check-list "spectre 7D" du cours comme guide d'identification des risques génériques.
   - Evaluez la criticité des risques.
5. Vérifier votre travail
   - Vérifiez la complétion de votre backlog et votre tableur.
   - Assurez-vous d'avoir une présentation concise qui répond aux exigences d'Alicia, en limitant à l'essentiel pour une communication claire.
   - Préparez-vous pour une discussion approfondie sur vos choix de projet, en pratiquant votre présentation pour une livraison fluide.

---

pourquoi prendre

ethique de tes projets

DPO
