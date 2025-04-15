def save_connections(avl, root, filename, logger):

    if root:
        connexions = avl.inorder(root)
        avl.save_to_file(root, filename)
        
        # Enregistrer l'opération dans les logs
        logger.log_connections_saved(filename, len(connexions))
    else:
        # Enregistrer qu'aucune connexion n'a été sauvegardée
        logger.log_connections_saved(filename, 0)