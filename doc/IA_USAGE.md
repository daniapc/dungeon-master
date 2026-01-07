# IA_USAGE

### Intéraction #1

**Contexte :**
Refonte esthétique de l'interface utilisateur (UI) du constructeur de donjon et amélioration de l'expérience utilisateur (UX) via CSS et HTML, tout en préservant la logique métier et l'intégration avec Flask.

**Prompt :**
Prompt en portugais (original): "como faço pra ficar esteticamente bonito? mantenha a essência das lógicas do código, só quero deixar bonito VISUALMENTE. ok? comentários em inglês."

Traduction: "comment puis-je rendre cela esthétiquement beau ? conserve l'essence de la logique du code, je veux seulement améliorer l'aspect VISUEL. ok ? commentaires en anglais."

Fichiers fournies: `jeu.html`, `jeu.css` et `sideBarButtons.js`

**Réponse IA :**
Fourniture d'une structure HTML améliorée, d'un fichier CSS complet avec thème sombre, effets de survol et variables, ainsi que l'ajout de stopPropagation dans le JavaScript pour corriger les conflits de sélection visuelle. Toutes les modifications suggérées par l'IA ont été intégrées dans le commit [ba0d733a](https://gibson.telecomnancy.univ-lorraine.fr/projets/2526/codingweek/grp09/-/commit/ba0d733a11f901f2f7b1f89e638b41f2694468f9) avec le message : "IA: UI visual improvement (Styling assisted by Gemini)"

### Intéraction #2

**Contexte :**
Tester le clacul de chemin avec BFS sans utiliser les classes grille ni case

**Prompt :**
(code de ia_strategy.py) Je. veux faire des tests indépendant de la classe grille

**Réponse :**
L'IA propose une série de test qui utilise unittest

**Décision :**

- Garder: l'utilisation de mock
- Modifier: simplifier les modules utilisés et adaptations en conséquence

**Remarques :**
Une correcttion du prompt est faite pour avoir une réponse qui utilise pytest-mock
