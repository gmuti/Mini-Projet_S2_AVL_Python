from avl import AVLTree, Connexion
import os
from utils import clear_screen, afficher_menu
from menu.add_connection import add_connection
from menu.delete_connection import delete_connection
from menu.clean_connections import clean_connections
from menu.search_connection import search_connection
from menu.display_connections import display_connections
from menu.save_and_exit import save_and_exit

def main():
    """Fonction principale du programme."""
    # Initialisation de l'arbre AVL
    avl = AVLTree()
    root = None

    # Chargement des connexions depuis le fichier s'il existe
    filename = "connexions.txt"
    if os.path.exists(filename):
        print(f"Chargement des connexions depuis {filename}...")
        root = avl.load_from_file(filename)
        if root:
            print("Connexions chargées avec succès!")
        else:
            print("Aucune connexion trouvée ou fichier vide.")

    while True:
        afficher_menu()
        choix = input("Entrez votre choix (1-6): ")

        if choix == "1":
            # Ajouter une connexion IP
            root = add_connection(avl, root)

        elif choix == "2":
            # Supprimer une IP
            root = delete_connection(avl, root)

        elif choix == "3":
            # Nettoyer les IP inactives
            root = clean_connections(avl, root)

        elif choix == "4":
            # Rechercher une IP
            search_connection(avl, root)

        elif choix == "5":
            # Afficher toutes les connexions
            display_connections(avl, root)

        elif choix == "6":
            # Quitter et sauvegarder
            if save_and_exit(avl, root, filename):
                break

        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 6.")

        input("\nAppuyez sur Entrée pour continuer...")
        clear_screen()

if __name__ == "__main__":
    main()
