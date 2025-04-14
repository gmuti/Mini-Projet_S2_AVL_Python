from datetime import datetime

def search_connection(avl, root):
    """
    Recherche une connexion IP dans l'arbre AVL.
    
    Args:
        avl: L'arbre AVL
        root: La racine de l'arbre
    """
    if root is None:
        print("Aucune connexion à rechercher.")
        return
            
    ip = input("Entrez l'adresse IP à rechercher: ")
    connexion = avl.search(root, ip)
    
    if connexion:
        print(f"Connexion trouvée: {connexion}")
        temps_ecoule = (datetime.now() - connexion.timestamp).total_seconds() / 60
        print(f"Temps écoulé depuis la dernière activité: {temps_ecoule:.2f} minutes")
    else:
        print(f"Connexion {ip} non trouvée.")