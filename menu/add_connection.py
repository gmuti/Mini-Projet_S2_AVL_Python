from avl import Connexion

def add_connection(avl, root, logger):
    """
    Ajoute une nouvelle connexion IP à l'arbre AVL.

    Args:
        avl: L'arbre AVL
        root: La racine de l'arbre
        logger: Le logger pour enregistrer l'opération

    Returns:
        La nouvelle racine de l'arbre après insertion
    """
    ip = input("Entrez l'adresse IP à ajouter: ")
    connexion = Connexion(ip)
    root = avl.insert(root, connexion)
    print(f"Connexion {ip} ajoutée avec succès!")

    # Enregistrer l'opération dans les logs
    logger.log_connection_added(ip)

    return root
