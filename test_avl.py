import unittest
from avl import AVLTree, Connexion, AVLNode
from datetime import datetime, timedelta
import time
import os

class TestConnexion(unittest.TestCase):
    """Tests pour la classe Connexion."""
    
    def test_creation(self):
        """Teste la création d'une connexion."""
        ip = "192.168.1.1"
        connexion = Connexion(ip)
        self.assertEqual(connexion.ip, ip)
        self.assertIsInstance(connexion.timestamp, datetime)
    
    def test_comparaison(self):
        """Teste la comparaison entre connexions."""
        c1 = Connexion("192.168.1.1")
        c2 = Connexion("192.168.1.2")
        self.assertTrue(c1 < c2)
        self.assertFalse(c2 < c1)
    
    def test_representation(self):
        """Teste la représentation textuelle d'une connexion."""
        ip = "192.168.1.1"
        connexion = Connexion(ip)
        self.assertIn(ip, str(connexion))


class TestAVLTree(unittest.TestCase):
    """Tests pour la classe AVLTree."""
    
    def setUp(self):
        """Initialise un arbre AVL pour les tests."""
        self.avl = AVLTree()
        self.root = None
    
    def test_insertion(self):
        """Teste l'insertion dans l'arbre AVL."""
        # Insertion de plusieurs connexions
        ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4", "192.168.1.5"]
        for ip in ips:
            self.root = self.avl.insert(self.root, Connexion(ip))
        
        # Vérification que toutes les connexions sont présentes
        for ip in ips:
            self.assertIsNotNone(self.avl.search(self.root, ip))
        
        # Vérification que l'arbre est équilibré
        self.assertTrue(abs(self.avl.balance_factor(self.root)) <= 1)
    
    def test_suppression(self):
        """Teste la suppression dans l'arbre AVL."""
        # Insertion de connexions
        ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
        for ip in ips:
            self.root = self.avl.insert(self.root, Connexion(ip))
        
        # Suppression d'une connexion
        ip_to_delete = "192.168.1.2"
        self.root = self.avl.delete(self.root, ip_to_delete)
        
        # Vérification que la connexion a été supprimée
        self.assertIsNone(self.avl.search(self.root, ip_to_delete))
        
        # Vérification que les autres connexions sont toujours présentes
        for ip in ips:
            if ip != ip_to_delete:
                self.assertIsNotNone(self.avl.search(self.root, ip))
        
        # Vérification que l'arbre est équilibré
        if self.root:  # Si l'arbre n'est pas vide
            self.assertTrue(abs(self.avl.balance_factor(self.root)) <= 1)
    
    def test_recherche(self):
        """Teste la recherche dans l'arbre AVL."""
        # Insertion de connexions
        ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
        for ip in ips:
            self.root = self.avl.insert(self.root, Connexion(ip))
        
        # Recherche d'une connexion existante
        ip_to_search = "192.168.1.2"
        connexion = self.avl.search(self.root, ip_to_search)
        self.assertIsNotNone(connexion)
        self.assertEqual(connexion.ip, ip_to_search)
        
        # Recherche d'une connexion inexistante
        ip_inexistant = "192.168.1.99"
        connexion = self.avl.search(self.root, ip_inexistant)
        self.assertIsNone(connexion)
    
    def test_parcours_inorder(self):
        """Teste le parcours inorder de l'arbre AVL."""
        # Insertion de connexions dans un ordre aléatoire
        ips = ["192.168.1.3", "192.168.1.1", "192.168.1.5", "192.168.1.2", "192.168.1.4"]
        for ip in ips:
            self.root = self.avl.insert(self.root, Connexion(ip))
        
        # Récupération des connexions triées
        connexions = self.avl.inorder(self.root)
        
        # Vérification que les connexions sont triées par IP
        ips_tries = sorted(ips)
        for i, connexion in enumerate(connexions):
            self.assertEqual(connexion.ip, ips_tries[i])
    
    def test_nettoyage(self):
        """Teste le nettoyage des connexions inactives."""
        # Insertion de connexions avec des timestamps différents
        ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
        
        # Première connexion avec timestamp actuel
        self.root = self.avl.insert(self.root, Connexion(ips[0]))
        
        # Deuxième connexion avec timestamp ancien (10 minutes dans le passé)
        connexion_ancienne = Connexion(ips[1])
        connexion_ancienne.timestamp = datetime.now() - timedelta(minutes=10)
        self.root = self.avl.insert(self.root, connexion_ancienne)
        
        # Troisième connexion avec timestamp actuel
        self.root = self.avl.insert(self.root, Connexion(ips[2]))
        
        # Nettoyage des connexions inactives depuis plus de 5 minutes
        new_root, ips_supprimees = self.avl.nettoyage(self.root, 5)
        self.root = new_root
        
        # Vérification que la connexion ancienne a été supprimée
        self.assertEqual(len(ips_supprimees), 1)
        self.assertEqual(ips_supprimees[0], ips[1])
        self.assertIsNone(self.avl.search(self.root, ips[1]))
        
        # Vérification que les autres connexions sont toujours présentes
        self.assertIsNotNone(self.avl.search(self.root, ips[0]))
        self.assertIsNotNone(self.avl.search(self.root, ips[2]))
    
    def test_sauvegarde_chargement(self):
        """Teste la sauvegarde et le chargement des connexions."""
        # Nom du fichier de test
        filename = "test_connexions.txt"
        
        # Suppression du fichier s'il existe déjà
        if os.path.exists(filename):
            os.remove(filename)
        
        # Insertion de connexions
        ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
        for ip in ips:
            self.root = self.avl.insert(self.root, Connexion(ip))
        
        # Sauvegarde des connexions
        self.avl.save_to_file(self.root, filename)
        
        # Vérification que le fichier a été créé
        self.assertTrue(os.path.exists(filename))
        
        # Chargement des connexions dans un nouvel arbre
        new_avl = AVLTree()
        new_root = new_avl.load_from_file(filename)
        
        # Vérification que toutes les connexions ont été chargées
        for ip in ips:
            self.assertIsNotNone(new_avl.search(new_root, ip))
        
        # Nettoyage
        os.remove(filename)


if __name__ == "__main__":
    unittest.main()