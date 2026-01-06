# ROADMAP – Projet Dungeon Manager

> Ce document décrit la vision globale du projet et le découpage en sprints (1 jour = 1 sprint).
> Il doit rester à jour tout au long de la semaine.

## 1. Vision du projet

- Objectif général :
_Ex : Concevoir un jeu de gestion de donjon jouable en TUI/Web, mettant en œuvre POO, patterns et
simulation._
- Public cible / utilisateur :
_Ex : Joueur qui veut concevoir, tester et optimiser un donjon contre des vagues de héros._
- Résultat attendu en fin de semaine :
_Ex : Application jouable + vidéo de démo scénarisée + tests unitaires de base.

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

> Liste des fonctionnalités et tâches importantes, avec une cible de sprint.
> À mettre à jour au fur et à mesure.

| ID | User story / tâche | Sprint cible | Priorité | Etat |
|----|------------------------------|-------|-----|---|
| US1 | En tant que joueur, je paux afficher une grille de donjon |  |  | DOING |
| US2 | En tant que joueur, je peux ajouter des objets (murs, ennemis) sur la grille |  |  | DOING |
| US3 | Ajouter un héro (qui se déplace aléatoirement) |  |  | DOING |
| US4 | Ajouter un menu pour pouvoir ajouter des objets / lancer une partie / avancer la partie |  |  | DOING |
| US5 | Pouvoir visualiser le jeu tel quel dans le terminal / sur HTML |  |  | DOING |
| US6 | Flask setup |  | | DOING |
| US7 | Implémenter la stratégie d'IA "plus court chemin" |  |  | TODO |
| US8 | Implémenter le score à la fin de la partie et l'argent récolté |  |  | TODO |
| US9 | Pouvoir jouer sur plusieurs vagues |  |  | TODO |
| US10 | Implémenter la stratégie d'IA "chemin le plus sûr" |  |  | TODO |
| US11 | Pouvoir visualiser le jeu en HTML et terminal |  |  | TODO |
| US12 | En tant que joueur, je dois pouvoir sauvegarder une partie à n'importe quel instant |  |  | TODO |
| US13 | Retravailler les visuels HTML (si nécessaire) |  |  | TODO |
| US14 | Préparer la vidéo de démonstration |  |  | TODO |
| US15 | Tourner la vidéo de démonstration |  |  | TODO |
| US16 | Monter la vidéo de démonstration |  |  | TODO |
| US17 | fin |  |  | TODO |


## 4. Vue par sprint (résumé)

> À maintenir en cohérence avec les fichiers de planning/retrospective.

### Sprint DAY_1 – [date]
- ...
### Sprint DAY_2 – [date]
- ...
### Sprint DAY_3 – [date]
- ...
### Sprint DAY_4 – [date]
- ...
### Sprint DAY_5 – [date]
- ...

## 5. Dette technique et améliorations futures

> Tâches non prioritaires pendant la semaine, mais à garder en mémoire.
- [ ] Ajouter une troisième stratégie IA.
- [ ] Améliorer l’ergonomie de l’IHM (raccourcis, couleurs, etc.).
- [ ] Ajouter plus de tests (cas extrêmes, erreurs utilisateur).