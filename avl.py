# -*- coding: utf-8 -*-

"""
AVL Module
"""

class AVL:
    """AVL main class."""
    def __init__(self, key, left, right, bal):
        self.key = key
        self.left = left
        self.right = right
        self.bal = bal


def to_str(B, s=""):
    """
    Simple AVL to String conversion for "print"
    Warning : B is not empty! (not optimized...)
    """
    r = s + '- ' + str(B.key) + ' (' + str(B.bal) + ')\n'
    if B.left != None or B.right != None: # internal node
        if B.left!= None:
            r += to_str(B.left, s + "  |")
        else:
            r += s + "  |" + '- '+ '\n'
        if B.right != None:
            r +=    to_str(B.right, s + "  |")
        else:
            r += s + "  |" + '- '+ '\n'
    return r


# rotations: works only in "usefull" cases

def lr(A):  # rotation gauche
    # Check if A.right is None before accessing its attributes
    if A.right is None:
        return A

    aux = A.right
    A.right = aux.left
    aux.left = A
    aux.bal += 1
    A.bal = -aux.bal
    return aux


def rr(A):  # rotation droite
    # Check if A.left is None before accessing its attributes
    if A.left is None:
        return A

    aux = A.left
    A.left = aux.right
    aux.right = A
    aux.bal -= 1
    A.bal = -aux.bal
    return aux


def lrr(A):  # rotation gauche-droite
    # Check if A.left is None before accessing its attributes
    if A.left is None:
        return A

    # Check if A.left.right is None before proceeding
    if A.left.right is None:
        return A

    # left rotation on left child
    aux = A.left.right
    A.left.right = aux.left
    aux.left = A.left
    # right rotation
    A.left = aux.right
    aux.right = A
    A = aux

    if A.bal == -1:
        (A.left.bal, A.right.bal) = (1, 0)
    elif A.bal == 1:
        (A.left.bal, A.right.bal) = (0, -1)
    else:
        (A.left.bal, A.right.bal) = (0, 0)
    A.bal = 0

    return A


def rlr(A):  # rotation droite-gauche
    # Check if A.right is None before accessing its attributes
    if A.right is None:
        return A

    aux = A.right.left
    # Check if aux (A.right.left) is None before proceeding
    if aux is None:
        return A

    A.right.left = aux.right
    aux.right = A.right

    A.right = aux.left
    aux.left = A

    (aux.left.bal, aux.right.bal) = (0, 0)
    if aux.bal == -1:
        aux.left.bal = 1
    elif aux.bal == 1:
        aux.right.bal = -1
    aux.bal = 0

    return aux

# For backward compatibility with existing code
from datetime import datetime, timedelta

class Connexion:
    def __init__(self, ip):
        self.ip = ip
        self.timestamp = datetime.now()

    def __lt__(self, other):
        return self.ip < other.ip

    def __str__(self):
        return f"IP: {self.ip}, Timestamp: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        if node is not None:
            node.height = 1 + max(self.height(node.left), self.height(node.right))

    def right_rotate(self, y):
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
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, ip):
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
        if root is None or root.data.ip == ip:
            return root.data if root else None

        if ip < root.data.ip:
            return self.search(root.left, ip)
        return self.search(root.right, ip)

    def inorder(self, root):
        result = []
        if root:
            result.extend(self.inorder(root.left))
            result.append(root.data)
            result.extend(self.inorder(root.right))
        return result

    def nettoyage(self, root, seuil_minutes):
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
        connexions = self.inorder(root)
        with open(filename, 'w') as f:
            for connexion in connexions:
                f.write(f"{connexion.ip},{connexion.timestamp.isoformat()}\n")

    def load_from_file(self, filename):
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