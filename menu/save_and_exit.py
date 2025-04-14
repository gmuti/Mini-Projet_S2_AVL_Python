def save_and_exit(avl, root, filename):
    """
    Sauvegarde les connexions dans un fichier et quitte le programme.
    
    Args:
        avl: L'arbre AVL
        root: La racine de l'arbre
        filename: Le nom du fichier de sauvegarde
        
    Returns:
        bool: True pour indiquer qu'il faut quitter le programme
    """
    if root:
        avl.save_to_file(root, filename)
        print(f"Connexions sauvegardées dans {filename}")
    print("Merci d'avoir utilisé le système de surveillance des connexions!")
    return True