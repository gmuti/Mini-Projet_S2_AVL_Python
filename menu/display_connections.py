def display_connections(avl, root):
    """
    Affiche toutes les connexions triées par IP.
    
    Args:
        avl: L'arbre AVL
        root: La racine de l'arbre
    """
    if root is None:
        print("Aucune connexion à afficher.")
        return
            
    connexions = avl.inorder(root)
    if connexions:
        print(f"\nListe des {len(connexions)} connexions (triées par IP):")
        for i, connexion in enumerate(connexions, 1):
            print(f"{i}. {connexion}")
    else:
        print("Aucune connexion à afficher.")