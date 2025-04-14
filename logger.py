import os
from datetime import datetime

class Logger:
    """
    Classe pour gérer les logs du système de surveillance des connexions.
    """
    def __init__(self, log_file="system_logs.txt"):
        """
        Initialise le logger avec le fichier de log spécifié.
        
        Args:
            log_file (str): Le nom du fichier de log
        """
        self.log_file = log_file
        
        # Créer le répertoire de logs s'il n'existe pas
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        # Enregistrer le démarrage du système
        self.log_system_start()
    
    def _write_log(self, message):
        """
        Écrit un message dans le fichier de log avec horodatage.
        
        Args:
            message (str): Le message à enregistrer
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        with open(self.log_file, "a") as f:
            f.write(log_entry)
    
    def log_connection_added(self, ip):
        """
        Enregistre l'ajout d'une connexion.
        
        Args:
            ip (str): L'adresse IP ajoutée
        """
        self._write_log(f"CONNEXION AJOUTÉE: {ip}")
    
    def log_connection_deleted(self, ip):
        """
        Enregistre la suppression d'une connexion.
        
        Args:
            ip (str): L'adresse IP supprimée
        """
        self._write_log(f"CONNEXION SUPPRIMÉE: {ip}")
    
    def log_connections_cleaned(self, ips, seuil_minutes):
        """
        Enregistre le nettoyage des connexions inactives.
        
        Args:
            ips (list): Liste des adresses IP supprimées
            seuil_minutes (int): Seuil d'inactivité en minutes
        """
        if ips:
            self._write_log(f"NETTOYAGE: {len(ips)} connexions inactives depuis plus de {seuil_minutes} minutes supprimées")
            for ip in ips:
                self._write_log(f"  - {ip}")
        else:
            self._write_log(f"NETTOYAGE: Aucune connexion inactive depuis plus de {seuil_minutes} minutes")
    
    def log_connection_search(self, ip, found):
        """
        Enregistre une recherche de connexion.
        
        Args:
            ip (str): L'adresse IP recherchée
            found (bool): Indique si la connexion a été trouvée
        """
        result = "trouvée" if found else "non trouvée"
        self._write_log(f"RECHERCHE: Connexion {ip} {result}")
    
    def log_connections_display(self, count):
        """
        Enregistre l'affichage des connexions.
        
        Args:
            count (int): Nombre de connexions affichées
        """
        self._write_log(f"AFFICHAGE: {count} connexions listées")
    
    def log_connections_saved(self, filename, count):
        """
        Enregistre la sauvegarde des connexions.
        
        Args:
            filename (str): Nom du fichier de sauvegarde
            count (int): Nombre de connexions sauvegardées
        """
        self._write_log(f"SAUVEGARDE: {count} connexions sauvegardées dans {filename}")
    
    def log_connections_loaded(self, filename, count):
        """
        Enregistre le chargement des connexions.
        
        Args:
            filename (str): Nom du fichier chargé
            count (int): Nombre de connexions chargées
        """
        self._write_log(f"CHARGEMENT: {count} connexions chargées depuis {filename}")
    
    def log_system_start(self):
        """
        Enregistre le démarrage du système.
        """
        self._write_log("SYSTÈME DÉMARRÉ")
    
    def log_system_exit(self):
        """
        Enregistre l'arrêt du système.
        """
        self._write_log("SYSTÈME ARRÊTÉ")