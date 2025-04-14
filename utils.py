import os

def clear_screen():
    """Efface l'écran de la console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def afficher_menu():
    """Affiche le menu principal de l'application."""
    print("\n===== Système de Surveillance des Connexions =====")
    print("1. Ajouter une connexion IP")
    print("2. Supprimer une IP")
    print("3. Nettoyer les IP inactives (> X min)")
    print("4. Rechercher une IP")
    print("5. Afficher toutes les connexions")
    print("6. Quitter et sauvegarder")
    print("================================================")