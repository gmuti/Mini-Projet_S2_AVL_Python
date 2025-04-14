# Système de Surveillance des Connexions Réseau

Ce projet implémente un système de surveillance des connexions réseau utilisant une structure d'arbre AVL pour gérer efficacement les adresses IP et leurs horodatages.

## Fonctionnalités

- Ajout d'une adresse IP avec horodatage automatique
- Suppression d'une adresse IP spécifique
- Nettoyage automatique des connexions inactives (basé sur un seuil de temps)
- Recherche rapide d'une adresse IP
- Affichage de toutes les connexions triées par adresse IP
- Sauvegarde et chargement automatique des connexions

## Structure du Projet

- `avl.py` : Implémentation de l'arbre AVL et de la classe Connexion
- `main.py` : Interface utilisateur en ligne de commande

## Utilisation

1. Exécutez le programme avec Python 3 :
   ```
   python main.py
   ```

2. Utilisez le menu pour interagir avec le système :
   - Option 1 : Ajouter une nouvelle connexion IP
   - Option 2 : Supprimer une IP existante
   - Option 3 : Nettoyer les IP inactives depuis plus de X minutes
   - Option 4 : Rechercher une IP et afficher ses informations
   - Option 5 : Afficher toutes les connexions triées par IP
   - Option 6 : Quitter et sauvegarder les connexions

## Intérêt de l'Arbre AVL dans ce Contexte

L'utilisation d'un arbre AVL pour gérer les connexions réseau présente plusieurs avantages par rapport à d'autres structures de données :

### Comparaison avec une Liste Chaînée

- **Recherche** : O(log n) pour un AVL vs O(n) pour une liste chaînée
- **Insertion** : O(log n) pour un AVL vs O(1) ou O(n) pour une liste chaînée (selon l'implémentation)
- **Suppression** : O(log n) pour un AVL vs O(n) pour une liste chaînée
- **Affichage trié** : Naturellement trié pour un AVL vs nécessité de tri O(n log n) pour une liste chaînée

### Comparaison avec un BST (Binary Search Tree) Simple

- **Recherche** : O(log n) garanti pour un AVL vs O(n) dans le pire cas pour un BST déséquilibré
- **Insertion** : O(log n) garanti pour un AVL vs O(n) dans le pire cas pour un BST déséquilibré
- **Suppression** : O(log n) garanti pour un AVL vs O(n) dans le pire cas pour un BST déséquilibré

### Avantages Spécifiques pour la Surveillance Réseau

1. **Performance Constante** : Les opérations restent efficaces même avec un grand nombre de connexions
2. **Recherche Rapide** : Permet de vérifier rapidement si une IP est déjà connectée
3. **Affichage Ordonné** : Facilite l'analyse des connexions par ordre d'adresse IP
4. **Équilibrage Automatique** : Maintient les performances optimales même avec des modèles d'insertion/suppression déséquilibrés

Ces caractéristiques sont particulièrement importantes dans un contexte de cybersécurité où la rapidité de détection et d'analyse des connexions peut être critique.

## Implémentation Technique

L'arbre AVL est implémenté avec les caractéristiques suivantes :

- Facteur d'équilibre maintenu entre -1 et 1 pour chaque nœud
- Rotations automatiques (gauche, droite, gauche-droite, droite-gauche) pour maintenir l'équilibre
- Parcours inorder pour afficher les connexions triées
- Mécanisme de nettoyage basé sur l'horodatage des connexions

## Auteur

Ce projet a été réalisé dans le cadre du cours d'Algorithmique Avancée avec Python.