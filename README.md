# Dungeon Manager

## Installation

1.  **Cloner le projet**
    ```bash
    git clone https://gibson.telecomnancy.univ-lorraine.fr/projets/2526/codingweek/grp09.git
    cd grp09
    ```

2.  **Créer un environnement virtuel (Recommandé)**
    ```bash
    # Création
    python3 -m venv venv
    
    # Activation
    source venv/bin/activate
    ```

3.  **Installer les dépendances**
    ```bash
    pip install -r requirements.txt
    ```
## Utilisation
Pour lancer le jeu:

    python3 -m src.jeu
## Tests
Lancement des tests:

    python3 -m pytest

## Guide de jeu
Objectif: gérer un donjon et empêcher les héros d'atteindre votre trésor

Le jeu se déroule en deux phases:
### 1. Phase de construction
Vous disposez d'un **budget** limité, chaque objet a un coût.
* Placez des **murs**  pour bloquer les chemins directs
* Installez des **pièges** (Faible, Moyen, Fort) pour infliger des dégâts aux héros\
        - Faible: peu de dégâts, se désactive après premier déclenchement\
        - Moyen: même dégâts que piège faible mais se déclanche deux fois (imaginons qu'un héros tombe sur un piège moyen, il subit des dégâts. S'il repasse dessus, il subit les dégâts une deuxième fois)\
        - Fort: même fonctionnement que les pièges faibles mais avec plus de dégâts
  
* Placez des **Monstres** pour défendre le trésor\
        Les monstres ont des PV et peuvent mourir quand ils s'affrontent à un héros.\
        Ils se déplacent en chercheant le plus court chemin vers un héros pris comme target.\

**Attention :** Si l'entrée au donjon ou l'accès au trésort sont bloqués par des mur, la vague ne pourra être lancée.

### 2. Phase de simulation (vagues) 
Une fois le donjon prêt, lancez la vague :
* Vous pouvez choisir la stratégie de déplacement des héros :
    * **BFS :** Ils prennent le chemin le plus court
    * **Dijkstra :** Ils tentent d'éviter les pièges (chemin le plus sûr)
    * **A star :** Un mix optimisé des deux

* Les héros apparaissent à l'entrée et cherchent le trésor. Ils ont tous les mêmes PV.

### Option de sauvgarde/chargement
- Vous pouvez sauvegarder un dojon ainsi qu'une partie (vague en cours).\
- Vous pouvez choisir de charger un donjon que vous avez crée au préalable.\
- Vous pouvez reprendre une partie, ceci gardera la disposition de votre donjon (murs et pièges) et l'emplacement des héros et monstres.

## Interfaces
### Terminal
Voici quelques commandes:
* M x,y : Placer Mur à la position (x,y)
* P1 x,y : Placer Piège faible à la position (x,y)
* O x,y : Placer Monstre à la position (x,y)
* R x,y : Retirer l'objet en (x,y)
### Web
Une fois lancée (http://127.0.0.1:5000/), utilisez la souris pour sélectionner un objet puis sur la grille pour lle placer.\
Le jeu est aussi accessible sur le serveur: http://35.188.222.36:5000/

Graphismes:\
    - Entrée : ruche\
    - Trésor : fleur\
    - Héros : abeille  

## Vidéo de démonstration
Lien dans doc/DEMONSTRATION.md
 
## Auteur : Les DALTons
 - Teresa FERNANDEZ DEL BUSTO JIMENEZ
 - Arthur HUTIN
 - Loan LECLERE-MOINAUX
 - Daniel Augusto PIRES DE CASTRO

