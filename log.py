"""
Last version on 17-05-23

@author: Thomas Aranda Verstraete
"""


class Log:
    """Notre classe Log permet de représenter une ligne de log contenue dans un fichier.
    Elle permettra de retrouver le chemin du fichier source ainsi que le contenu de la ligne
     (sous laforme d’attribut d’instance)"""

    def __init__(self, text, source=None):
        """
        Constructeur de la classe Log
        :param text: String - Contenu de la ligne de log
        :param source: String - Chemin vers le fichier qui contenait
        cette ligne de log
        """
        self.text = text
        self.source = source

    def get_program(self):
        """
        :return: Le nom du programme contenu dans la ligne de log.
        Si la ligne ne contient
        pas de nom, "Unknown" sera renvoyé
        """
        log = self.text
        split = log.split()
        name = split[4]
        if "" == name:
            return "unknown"
        elif "[" in name:
            split = name.split("[")
            name = split[0]
        elif ":" in name:
            split = name.split(":")
            name = split[0]
        return name

    def __str__(self):
        """
        :return: String - renvoie le contenu du log
        """
        return self.text
