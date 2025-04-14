def clean_connections(avl, root, logger):
    """
    Nettoie les connexions inactives depuis plus de X minutes.

    Args:
        avl: L'arbre AVL
        root: La racine de l'arbre
        logger: Le logger pour enregistrer l'opération

    Returns:
        La nouvelle racine de l'arbre après nettoyage
    """
    if root is None:
        print("Aucune connexion à nettoyer.")
        return root

    try:
        seuil = int(input("Entrez le seuil d'inactivité en minutes: "))
        if seuil <= 0:
            print("Le seuil doit être un nombre positif.")
            return root

        new_root, ips_supprimees = avl.nettoyage(root, seuil)

        # Enregistrer l'opération dans les logs
        logger.log_connections_cleaned(ips_supprimees, seuil)

        if ips_supprimees:
            print(f"{len(ips_supprimees)} connexions inactives supprimées:")
            for ip in ips_supprimees:
                print(f" - {ip}")
        else:
            print("Aucune connexion inactive trouvée.")

        return new_root
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        return root
