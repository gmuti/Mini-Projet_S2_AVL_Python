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
    if root:
        connexions = avl.inorder(root)
        avl.save_to_file(root, filename)
        print(f"Connexions sauvegardées dans {filename}")

        # Enregistrer l'opération dans les logs
        logger.log_connections_saved(filename, len(connexions))
    else:
        # Enregistrer qu'aucune connexion n'a été sauvegardée
        logger.log_connections_saved(filename, 0)

    print("Merci d'avoir utilisé le système de surveillance des connexions!")
    return True
