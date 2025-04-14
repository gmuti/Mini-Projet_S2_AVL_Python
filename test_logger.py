import unittest
import os
from logger import Logger
from datetime import datetime

class TestLogger(unittest.TestCase):
    """Tests pour la classe Logger."""
    
    def setUp(self):
        """Initialise un logger de test."""
        self.test_log_file = "test_logs.txt"
        # Supprimer le fichier de test s'il existe déjà
        if os.path.exists(self.test_log_file):
            os.remove(self.test_log_file)
        self.logger = Logger(self.test_log_file)
    
    def tearDown(self):
        """Nettoie après les tests."""
        if os.path.exists(self.test_log_file):
            os.remove(self.test_log_file)
    
    def test_log_file_creation(self):
        """Teste la création du fichier de log."""
        self.assertTrue(os.path.exists(self.test_log_file))
    
    def test_log_system_start(self):
        """Teste l'enregistrement du démarrage du système."""
        # Le démarrage est déjà enregistré dans setUp
        with open(self.test_log_file, 'r') as f:
            content = f.read()
        self.assertIn("SYSTÈME DÉMARRÉ", content)
    
    def test_log_connection_added(self):
        """Teste l'enregistrement de l'ajout d'une connexion."""
        ip = "192.168.1.1"
        self.logger.log_connection_added(ip)
        with open(self.test_log_file, 'r') as f:
            content = f.read()
        self.assertIn(f"CONNEXION AJOUTÉE: {ip}", content)
    
    def test_log_connection_deleted(self):
        """Teste l'enregistrement de la suppression d'une connexion."""
        ip = "192.168.1.1"
        self.logger.log_connection_deleted(ip)
        with open(self.test_log_file, 'r') as f:
            content = f.read()
        self.assertIn(f"CONNEXION SUPPRIMÉE: {ip}", content)
    
    def test_log_connections_cleaned(self):
        """Teste l'enregistrement du nettoyage des connexions."""
        ips = ["192.168.1.1", "192.168.1.2"]
        seuil = 10
        self.logger.log_connections_cleaned(ips, seuil)
        with open(self.test_log_file, 'r') as f:
            content = f.read()
        self.assertIn(f"NETTOYAGE: {len(ips)} connexions inactives depuis plus de {seuil} minutes", content)
    
    def test_log_connection_search(self):
        """Teste l'enregistrement de la recherche d'une connexion."""
        ip = "192.168.1.1"
        self.logger.log_connection_search(ip, True)
        with open(self.test_log_file, 'r') as f:
            content = f.read()
        self.assertIn(f"RECHERCHE: Connexion {ip} trouvée", content)
        
        self.logger.log_connection_search(ip, False)
        with open(self.test_log_file, 'r') as f:
            content = f.read()
        self.assertIn(f"RECHERCHE: Connexion {ip} non trouvée", content)
    
    def test_log_connections_display(self):
        """Teste l'enregistrement de l'affichage des connexions."""
        count = 5
        self.logger.log_connections_display(count)
        with open(self.test_log_file, 'r') as f:
            content = f.read()
        self.assertIn(f"AFFICHAGE: {count} connexions listées", content)
    
    def test_log_connections_saved(self):
        """Teste l'enregistrement de la sauvegarde des connexions."""
        filename = "connexions.txt"
        count = 3
        self.logger.log_connections_saved(filename, count)
        with open(self.test_log_file, 'r') as f:
            content = f.read()
        self.assertIn(f"SAUVEGARDE: {count} connexions sauvegardées dans {filename}", content)
    
    def test_log_connections_loaded(self):
        """Teste l'enregistrement du chargement des connexions."""
        filename = "connexions.txt"
        count = 3
        self.logger.log_connections_loaded(filename, count)
        with open(self.test_log_file, 'r') as f:
            content = f.read()
        self.assertIn(f"CHARGEMENT: {count} connexions chargées depuis {filename}", content)
    
    def test_log_system_exit(self):
        """Teste l'enregistrement de l'arrêt du système."""
        self.logger.log_system_exit()
        with open(self.test_log_file, 'r') as f:
            content = f.read()
        self.assertIn("SYSTÈME ARRÊTÉ", content)

if __name__ == "__main__":
    unittest.main()