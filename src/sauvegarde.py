import json 
import os

class GestionSauvegarde :

    DOSSIER_SAUVEGARDE = "saves"

    @staticmethod 
    def verifier_dossier() :
        if not os.path.exists(GestionSauvegarde.DOSSIER_SAUVEGARDE) :
            os.makedirs(GestionSauvegarde.DOSSIER_SAUVEGARDE)
    
    @staticmethod
    def sauvegarder_donjon(nom_fichier, donnees) : 
        GestionSauvegarde.verifier_dossier()
        chemin = os.path.join(GestionSauvegarde.DOSSIER_SAUVEGARDE, f"{nom_fichier}.json")
        try :
            with open(chemin, 'w') as f :
                json.dump(donnees, f, indent=4)
            print(f"Donjon sauvegardé à {chemin}")
            return True 
        except Exception as e :
            print(f"Erreur sauvegarde : {e}")
            return False 
    
    @staticmethod
    def charger_donjon(nom_fichier) :
        chemin = os.path.join(GestionSauvegarde.DOSSIER_SAUVEGARDE, f"{nom_fichier}.json")
        if not os.path.exists(chemin) :
            print("Fichier introuvable")
            return None
        try :
            with open(chemin, 'r') as f :
                return json.load(f)
        except Exception as e :
            print(f"Erreur chargement : {e}")
            return None
