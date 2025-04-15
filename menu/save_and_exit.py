def save_and_exit(avl, root, filename, logger):
    """
    Sauvegarde les connexions dans un fichier et quitte le programme.

    Args:
        avl: L'arbre AVL
        root: La racine de l'arbre
        filename: Le nom du fichier de sauvegarde
        logger: Le logger pour enregistrer l'opération

    Returns:
        bool: True pour indiquer qu'il faut quitter le programme
    """
    from menu.save_connections import save_connections

    # Utiliser la fonction save_connections pour sauvegarder les connexions
    save_connections(avl, root, filename, logger)

    if root:
        print(f"Connexions sauvegardées dans {filename}")

    print("Merci d'avoir utilisé le système de surveillance des connexions!")
    return True
