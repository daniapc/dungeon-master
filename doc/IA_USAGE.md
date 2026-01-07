# IA_USAGE

### Intéraction #1
**Contexte :** 
Création de série de tests pour les créateurs de Héros et Objet

**Prompt :**
Propose des test sur Fabrique_Objet

**Réponse IA :**
exemple de code pour tester l'instanciation et le polymorphisme


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
