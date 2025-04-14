from datetime import datetime, timedelta

class Connexion:
    """
    Classe représentant une connexion réseau avec une adresse IP et un horodatage.
    """
    def __init__(self, ip):
        """
        Initialise une nouvelle connexion avec l'adresse IP spécifiée.
        L'horodatage est automatiquement défini au moment de la création.
        
        Args:
            ip (str): L'adresse IP de la connexion
        """
        self.ip = ip
        self.timestamp = datetime.now()
    
    def __lt__(self, other):
        """
        Compare deux connexions par leur adresse IP.
        
        Args:
            other (Connexion): La connexion à comparer
            
        Returns:
            bool: True si l'IP de cette connexion est inférieure à l'autre, False sinon
        """
        return self.ip < other.ip
    
    def __str__(self):
        """
        Retourne une représentation textuelle de la connexion.
        
        Returns:
            str: Représentation de la connexion avec IP et horodatage
        """
        return f"IP: {self.ip}, Timestamp: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"


class AVLNode:
    """
    Nœud d'un arbre AVL contenant une connexion.
    """
    def __init__(self, data):
        """
        Initialise un nouveau nœud avec les données spécifiées.
        
        Args:
            data (Connexion): La connexion à stocker dans ce nœud
        """
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    """
    Implémentation d'un arbre AVL pour gérer les connexions réseau.
    """
    
    def height(self, node):
        """
        Retourne la hauteur d'un nœud.
        
        Args:
            node (AVLNode): Le nœud dont on veut connaître la hauteur
            
        Returns:
            int: La hauteur du nœud, 0 si le nœud est None
        """
        if node is None:
            return 0
        return node.height
    
    def balance_factor(self, node):
        """
        Calcule le facteur d'équilibre d'un nœud.
        
        Args:
            node (AVLNode): Le nœud dont on veut calculer le facteur d'équilibre
            
        Returns:
            int: Le facteur d'équilibre (différence de hauteur entre sous-arbres gauche et droit)
        """
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def update_height(self, node):
        """
        Met à jour la hauteur d'un nœud en fonction de ses enfants.
        
        Args:
            node (AVLNode): Le nœud dont on veut mettre à jour la hauteur
        """
        if node is not None:
            node.height = 1 + max(self.height(node.left), self.height(node.right))
    
    def right_rotate(self, y):
        """
        Effectue une rotation à droite autour du nœud y.
        
        Args:
            y (AVLNode): Le nœud autour duquel effectuer la rotation
            
        Returns:
            AVLNode: La nouvelle racine après rotation
        """
        x = y.left
        T2 = x.right
        
        # Rotation
        x.right = y
        y.left = T2
        
        # Mise à jour des hauteurs
        self.update_height(y)
        self.update_height(x)
        
        return x
    
    def left_rotate(self, x):
        """
        Effectue une rotation à gauche autour du nœud x.
        
        Args:
            x (AVLNode): Le nœud autour duquel effectuer la rotation
            
        Returns:
            AVLNode: La nouvelle racine après rotation
        """
        y = x.right
        T2 = y.left
        
        # Rotation
        y.left = x
        x.right = T2
        
        # Mise à jour des hauteurs
        self.update_height(x)
        self.update_height(y)
        
        return y
    
    def insert(self, root, data):
        """
        Insère une nouvelle connexion dans l'arbre AVL.
        
        Args:
            root (AVLNode): La racine de l'arbre (ou sous-arbre)
            data (Connexion): La connexion à insérer
            
        Returns:
            AVLNode: La nouvelle racine après insertion
        """
        # Insertion standard BST
        if root is None:
            return AVLNode(data)
        
        if data.ip < root.data.ip:
            root.left = self.insert(root.left, data)
        elif data.ip > root.data.ip:
            root.right = self.insert(root.right, data)
        else:
            # IP déjà présente, mise à jour du timestamp
            root.data.timestamp = data.timestamp
            return root
        
        # Mise à jour de la hauteur
        self.update_height(root)
        
        # Vérification de l'équilibre
        balance = self.balance_factor(root)
        
        # Cas de déséquilibre
        # Cas Gauche-Gauche
        if balance > 1 and data.ip < root.left.data.ip:
            return self.right_rotate(root)
        
        # Cas Droite-Droite
        if balance < -1 and data.ip > root.right.data.ip:
            return self.left_rotate(root)
        
        # Cas Gauche-Droite
        if balance > 1 and data.ip > root.left.data.ip:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # Cas Droite-Gauche
        if balance < -1 and data.ip < root.right.data.ip:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    
    def get_min_value_node(self, node):
        """
        Trouve le nœud avec la valeur minimale dans un sous-arbre.
        
        Args:
            node (AVLNode): La racine du sous-arbre
            
        Returns:
            AVLNode: Le nœud avec la valeur minimale
        """
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def delete(self, root, ip):
        """
        Supprime une connexion de l'arbre AVL par son IP.
        
        Args:
            root (AVLNode): La racine de l'arbre (ou sous-arbre)
            ip (str): L'IP de la connexion à supprimer
            
        Returns:
            AVLNode: La nouvelle racine après suppression
        """
        # Suppression standard BST
        if root is None:
            return root
        
        if ip < root.data.ip:
            root.left = self.delete(root.left, ip)
        elif ip > root.data.ip:
            root.right = self.delete(root.right, ip)
        else:
            # Nœud à supprimer trouvé
            
            # Cas avec un seul enfant ou sans enfant
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # Cas avec deux enfants
            # Trouver le successeur inorder (plus petit dans le sous-arbre droit)
            temp = self.get_min_value_node(root.right)
            
            # Copier les données du successeur
            root.data = temp.data
            
            # Supprimer le successeur
            root.right = self.delete(root.right, temp.data.ip)
        
        # Si l'arbre n'avait qu'un nœud
        if root is None:
            return root
        
        # Mise à jour de la hauteur
        self.update_height(root)
        
        # Vérification de l'équilibre
        balance = self.balance_factor(root)
        
        # Cas de déséquilibre
        # Cas Gauche-Gauche
        if balance > 1 and self.balance_factor(root.left) >= 0:
            return self.right_rotate(root)
        
        # Cas Gauche-Droite
        if balance > 1 and self.balance_factor(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # Cas Droite-Droite
        if balance < -1 and self.balance_factor(root.right) <= 0:
            return self.left_rotate(root)
        
        # Cas Droite-Gauche
        if balance < -1 and self.balance_factor(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    
    def search(self, root, ip):
        """
        Recherche une connexion par son IP.
        
        Args:
            root (AVLNode): La racine de l'arbre (ou sous-arbre)
            ip (str): L'IP à rechercher
            
        Returns:
            Connexion: La connexion trouvée ou None si non trouvée
        """
        if root is None or root.data.ip == ip:
            return root.data if root else None
        
        if ip < root.data.ip:
            return self.search(root.left, ip)
        return self.search(root.right, ip)
    
    def inorder(self, root):
        """
        Parcours inorder de l'arbre pour afficher les connexions triées par IP.
        
        Args:
            root (AVLNode): La racine de l'arbre (ou sous-arbre)
            
        Returns:
            list: Liste des connexions triées par IP
        """
        result = []
        if root:
            result.extend(self.inorder(root.left))
            result.append(root.data)
            result.extend(self.inorder(root.right))
        return result
    
    def nettoyage(self, root, seuil_minutes):
        """
        Supprime les connexions inactives depuis plus de X minutes.
        
        Args:
            root (AVLNode): La racine de l'arbre
            seuil_minutes (int): Nombre de minutes d'inactivité avant suppression
            
        Returns:
            AVLNode: La nouvelle racine après nettoyage
            list: Liste des IPs supprimées
        """
        if root is None:
            return None, []
        
        # Récupérer toutes les connexions
        connexions = self.inorder(root)
        
        # Identifier les connexions inactives
        now = datetime.now()
        ips_a_supprimer = []
        
        for connexion in connexions:
            if (now - connexion.timestamp).total_seconds() > seuil_minutes * 60:
                ips_a_supprimer.append(connexion.ip)
        
        # Supprimer les connexions inactives
        new_root = root
        for ip in ips_a_supprimer:
            new_root = self.delete(new_root, ip)
        
        return new_root, ips_a_supprimer
    
    def save_to_file(self, root, filename):
        """
        Sauvegarde les connexions dans un fichier texte.
        
        Args:
            root (AVLNode): La racine de l'arbre
            filename (str): Nom du fichier de sauvegarde
        """
        connexions = self.inorder(root)
        with open(filename, 'w') as f:
            for connexion in connexions:
                f.write(f"{connexion.ip},{connexion.timestamp.isoformat()}\n")
    
    def load_from_file(self, filename):
        """
        Charge les connexions depuis un fichier texte.
        
        Args:
            filename (str): Nom du fichier à charger
            
        Returns:
            AVLNode: La racine de l'arbre chargé
        """
        root = None
        try:
            with open(filename, 'r') as f:
                for line in f:
                    if line.strip():
                        ip, timestamp_str = line.strip().split(',')
                        connexion = Connexion(ip)
                        connexion.timestamp = datetime.fromisoformat(timestamp_str)
                        root = self.insert(root, connexion)
            return root
        except FileNotFoundError:
            return None