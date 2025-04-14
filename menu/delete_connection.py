def delete_connection(avl, root):
    """
    Supprime une connexion IP de l'arbre AVL.
    
    Args:
        avl: L'arbre AVL
        root: La racine de l'arbre
        
    Returns:
        La nouvelle racine de l'arbre après suppression
    """
    if root is None:
        print("Aucune connexion à supprimer.")
        return root
            
    ip = input("Entrez l'adresse IP à supprimer: ")
    if avl.search(root, ip):
        root = avl.delete(root, ip)
        print(f"Connexion {ip} supprimée avec succès!")
    else:
        print(f"Connexion {ip} non trouvée.")
    
    return root