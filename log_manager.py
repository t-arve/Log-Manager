"""
Last version on 17-05-23

@author: Thomas Aranda Verstraete
"""
from program_not_found import *


class LogManager:
    """
    Notre classe Log permet de représenter une ligne de log contenue dans un fichier.
    Elle permettra de retrouver le chemin du fichier source ainsi que le contenu de la
    ligne (sous la forme d’attribut d’instance)
    """
    @staticmethod
    def sort_by_program(logs):
        """
        Renvoie un dictionnaire où chaque clé est un programme et la valeur
        associée à la clé est une liste contenant les logs du programme.
        :param logs: Une liste de Logs
        :return: Un dictionnaire
        """
        dico = {}
        for log in logs:
            program = log.get_program()
            if program not in dico:
                dico[program] = [log]
            else:
                dico[program].append(log)
        return dico

    def __init__(self, logs=None):
        """
        :param logs: Une liste de logs (string) - Optionnel
        """
        if logs is None:
            self.logs = {}
        else:
            self.logs = LogManager.sort_by_program(logs)

    def clear(self):
        """
        Remplace le contenu de self.logs par {}
        :return: None
        """
        self.logs = {}

    def add_logs(self, logs):
        """
        Rajoute les logs à self.logs
        :param logs: Une liste de logs (string)
        :return: None
        """
        dico = LogManager.sort_by_program(logs)

        for program, program_logs in dico.items():
            if program in self.logs:
                self.logs[program].extend(program_logs)
            else:
                self.logs[program] = program_logs

    @property
    def nbr_logs(self):
        """
        Renvoie la totalité des logs stockés dans le log_manager
        :return: Un entier représentant la totalité des logs dans le
        log_manager
        """
        counter = 0
        for value in self.logs.values():
            counter += len(value)
        return counter

    def search_logs(self, program_name):
        """
        Renvoie la liste de Logs associés au programme. Si le
        programme n'existe pas dans self.logs, la fonction renvoie une
        erreur ProgramNotFound !
        :param program_name - String
        :return: Liste de Logs
        """
        if program_name in self.logs.keys():
            return self.logs[program_name]
        else:
            raise ProgramNotFound(program_name,self.logs.keys())

    def __str__(self):
        """
        Renvoie une représentation en chaîne de caractères du
        log_manager et le nombre total de logs
        stockés dans le log_manager
        Exemple:
        Programme1:
        Log1
        Log2
        Programme2:
        Log3
        Log4
        Log5
        TOTAL LOGS: 5
        :return: String
        """
        messagelog = ""
        for program, logs in self.logs.items():
            messagelog += f"{program}:".format(os.linesep)
            messagelog += "=======".format(os.linesep)
            for log in logs:
                messagelog += str(log)
        messagelog += f"TOTAL LOGS: {self.nbr_logs}"
        return messagelog
