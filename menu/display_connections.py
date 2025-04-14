def display_connections(avl, root, logger):
    """
    Affiche toutes les connexions triées par IP.

    Args:
        avl: L'arbre AVL
        root: La racine de l'arbre
        logger: Le logger pour enregistrer l'opération
    """
    if root is None:
        print("Aucune connexion à afficher.")
        logger.log_connections_display(0)
        return

    connexions = avl.inorder(root)
    if connexions:
        print(f"\nListe des {len(connexions)} connexions (triées par IP):")
        for i, connexion in enumerate(connexions, 1):
            print(f"{i}. {connexion}")

        # Enregistrer l'opération dans les logs
        logger.log_connections_display(len(connexions))
    else:
        print("Aucune connexion à afficher.")
        logger.log_connections_display(0)
