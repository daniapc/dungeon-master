# ROADMAP – Projet Dungeon Manager

> Ce document décrit la vision globale du projet et le découpage en sprints (1 jour = 1 sprint).

## 1. Vision du projet

- Objectif général :
Concevoir un jeu de gestion de donjon jouable en TUI/Web.
- Public cible / utilisateur :
Joueur qui veut concevoir, tester et optimiser un donjon contre des vagues de héros.

## 2. Conventions

- **Statuts des tâches** :
- `TODO` : à faire
- `DOING` : en cours
- `DONE` : terminé
- **Sprints** :
- `DAY_1` à `DAY_5` (1 sprint par jour)
- Les détails de chaque sprint sont dans :
`SPRINT_PLANNING_DAY_X.md` et `SPRINT_RETROSPECTIVE_DAY_X.md`.

## 3. Backlog global

> Liste des fonctionnalités et tâches importantes

| ID | Tâche | Priorité | Etat |
|----|------------------------------|-----|---|
| 1 | Faire une structure de grille et de cases | Haute | DONE |
| 2 | Pouvoir afficher une grille Terminal / Web | Haute | DONE |
| 3 | Faire une structure de Héros et Objets (Murs, Pièges) | Haute | DONE |
| 4 | Implémenter une Factory pour chaque élément | Moyenne | DONE |
| 5 | Faire un diagramme UML et le tenir à jour | Moyenne | DOING |
| 6 | Pouvoir placer des objets sur le grille de donjon | Haute | DONE |
| 7 | Lancer une vague | Haute | DONE |
| 8 | Faire une boucle de jeu (placement & vagues) | Haute | DONE |
| 9 | Calcul de budjet selon placements faits | Haute | DONE |
| 10 | Calcul de score | Haute | DONE |
| 11 | Faire un système de sauvegarde/chargement de partie | Haute | DONE |
| 12 | Développer les interfaces | Moyenne | DOING |
| 13 | Implémenter une stratégie "plus court chemin " pour le déplacement des héros | Haute | DONE |
| 14 | Implémenter une stratégie "chemin le plus sûr" | Haute | DONE |
| 15 | Pouvoir choisir la stratégie à appliquer | Moyenne | DONE |
| 16 | Configuration de serveur | Faible | DONE |
| 17 | Configuration de l'application Flask | Haute | DONE |
| 18 | Intégration de menus de contrôle sur interfaces | Moyenne | DONE |
| 19 | Faire un menu de lancement | Moyenne | DONE |
| 20 | Avoir un récapitulatif en fin de partie | Moyenne | DONE |
| 21 | Faire des tests unitaires sur le code | Moyenne | DOING |
| 22 | Avoir un README complet| Haute | DOING |
| 23 | Implémenter des monstres | Faible | DOING |
| 24 | Amélioration de l'UX | Faible | TODO |
| 25 | Préparer la vidéo de démonstration | Haute | TODO |
| 26 | Tourner la vidéo de démonstration | Haute  | TODO |
| 27 | Monter la vidéo de démonstration |  Moyenne | TODO |

## 4. Vue par sprint (résumé)

### Sprint DAY_1 – [05/01/2026]
Objectif : Mise en place de l'architecture et de l'environnement.

    - Implémentation de la structure de données de base (Grille, Case).

    - Configuration de l'environnement serveur (Flask) et choix d'architecture (Web vs Terminal).

    - Début de la logique de déplacement des héros.

    - Définition des classes principales du projet.
### Sprint DAY_2 – [06/01/2026]
Objectif : Patterns de conception et cœur du gameplay.

    - Implémentation des Design Patterns : Factory (pour la création d'objets) et Observer (pour le suivi des Héros/Budget).

    - Création de la boucle de jeu principale et calcul du score.

    - Affichage dynamique de la grille sur l'interface Web et Terminal.

    - Communication fonctionnelle entre le Backend (Flask) et le Frontend.
### Sprint DAY_3 – [07/01/2026]
Objectif : Intelligence Artificielle et Intégration.

    - Finalisation et intégration de l'algorithme BFS (Plus court chemin).

    - Implémentation de l'algorithme Dijkstra (Chemin le moins dangereux/coûteux).

    - Fusion des phases de jeu : Construction du donjon ↔ Simulation des vagues.

    - Ajout de contrôles interface (Sidebar, boutons) et Tests Unitaires (Constructeur).

    - Réalisation du Diagramme UML et documentation technique.
### Sprint DAY_4 – [08/01/2026]
Objectif : Finalisation des fonctionnalités, Expérience Utilisateur (UX) et Nettoyage.

    - Nettoyage du dépôt Git et mise à jour de la documentation.

    - Implémentation et intégration des algorithmes Dijkstra et A* pour le déplacement des héros.

    - Finalisation du système de Sauvegarde/Chargement (Donjon et Partie).

    - Création des menus d'interface : Menu de lancement, Sélection de stratégie et Récapitulatif de fin de partie.

    - Adaptation et intégration complète des fonctionnalités sur l'interface Web.

    - (Bonus) Implémentation initiale des Monstres.
### Sprint DAY_5 – [09/01/2026]
- ...

## 5. Dette technique et améliorations futures
- [ ] Améliorer l’ergonomie de l’IHM (raccourcis, couleurs, etc.).
- [ ] Ajouter plus de tests (cas extrêmes, erreurs utilisateur).