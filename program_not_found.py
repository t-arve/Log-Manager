"""
Last version on 17-05-23

@author: Thomas Aranda Verstraete
"""
import os


class ProgramNotFound(Exception):
    """
    Chaque instance de cette classe contiendra le nom du
    programme recherché et les noms des programmes disponibles.
    Nous allons également redéfinir la méthode « __str__ »
    pour pouvoir afficher l’erreur à l’utilisateur de façon lisible.
    """

    def __init__(self, searched_program, available_programs):
        """
        :param searched_program: String - le programme recherché
        :param available_programs: Liste de String - ensemble des
        programmes qui étaient disponibles
        """
        self.searched_program = searched_program
        self.available_programs = available_programs

    def __str__(self):
        """
        Renvoie une chaîne de caractères représentant l'erreur
        Exemple :
        Impossible de trouver le programme Prog dans la liste :
        Programme1
        Programme2
        Programme3
        :return: String
        """
        string = f"Impossible de trouver le programme {self.searched_program} dans la liste :"
        for program in self.available_programs:
            string += os.linesep + program
        return string
