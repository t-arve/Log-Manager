"""
Last version on 19-05-23

@author: Thomas Aranda Verstraete
"""
import os
from log import *
from log_manager import *


def load_log_from_file(relative_path):
    """
    La fonction permet de récupérer les logs se trouvant dans un
    fichier grâce au chemin relatif passé en argument de la fonction.
    La fonction NE peut PAS lancer d’erreur. Si le chemin n'existe
    pas, la fonction affiche "Le chemin n'existe pas" et donne le chemin
    ABSOLU du fichier demandé.
    S'il y a eu une exception, renvoyez explicitement un "None"
    :param relative_path: String représentant un chemin relatif
    (vers un fichier) par rapport au dossier courant.
    :return: Renvoie un tableau de strings qui sont les logs
    contenant les logs.
    """
    try:
        with open(relative_path, "r") as file:
            logs = file.readlines()
            return logs

    except:
        return None


def load_logs_from_folder(folder_path):
    """
    La fonction permet de charger les logs de tous les fichiers
    présents dans un dossier. Le chemin
    relatif en argument de la fonction est le chemin relatif
    vers un dossier.
    La fonction NE peut PAS lancer d’erreur. Si le chemin
    n'existe pas, la fonction affiche "Le chemin n'existe pas" et
    retourne le chemin ABSOLU du dossier demandé.
    S'il y a eu une exception, renvoyez explicitement un "None".
    :param folder_path: String représentant un chemin relatif
    (vers un dossier) par rapport au
    dossier courant
    :return: Renvoie un tableau de strings qui sont les logs
    contenant les logs ou None en cas d’erreur
    """
    absolute_path = os.path.join(os.getcwd(),folder_path)
    try:
        if not os.path.exists(absolute_path):
            print(f" le chemin: {absolute_path}, n'existe pas")
            return absolute_path
        else:
            syslogs_list = []
            for file in os.scandir(folder_path):
                new_path = os.path.join(folder_path,file.name)
                syslogs_list.append(load_log_from_file(new_path))

            return syslogs_list
    except:
        return None


def get_folders_and_subfolders(folder_path):
    """
    La fonction renvoie une liste de chemins relatifs avec le chemin
    folder_path et ses sous-dossiers.
    La fonction NE peut PAS lancer d’erreur. Si le chemin n'existe pas, la
    fonction affiche "Le chemin n'existe pas" et donne le chemin ABSOLU du
    dossier demandé.
    S'il y a eu une exception, renvoyez explicitement un "None".
    :param folder_path: String représentant le chemin relatif vers le
    dossier cible
    :return: une liste de chemins relatifs avec le chemin folder_path et
    ses sous-dossiers
    """
    absolute_path = os.path.join(os.getcwd(), folder_path)
    try:
        if not os.path.exists(folder_path):
            print(f" le chemin: {absolute_path}, n'existe pas")
            return None
        else:
            subfolders_list = [folder_path]
            with os.scandir(folder_path) as scan_directory:

                for elem in scan_directory:
                    if elem.is_dir():
                        subfolders_list.append(folder_path+ "/"+ elem.name)
            return subfolders_list

    except:
        print("Le chemin du fichier n'existe pas:")
        return None


def load(path_folder):
    """
    La fonction renvoie un tableau de logs à partir des fichiers
    dans le dossier (obtenu via le chemin relatif) et les sous-
    dossiers de ce dossier.
    :param path_folder: String représentant le chemin relatif
    vers un dossier
    :return: Renvoie un tableau de string contenant les logs
    """
    logs_table = []
    all_folders = get_folders_and_subfolders(path_folder)
    try:
        for elem in all_folders:
            if elem:
                logs_table.append(load_logs_from_folder(path_folder))
        return logs_table

    except FileNotFoundError:
        print(f"Le fichier '{path_folder}' n'a pas été trouvé.")
        return None

    except IsADirectoryError:
        print(f"'{path_folder}' est un dossier,  .")
        return None


def menu(available_choices):
    """
    Affiche un menu et demande à l'utilisateur de taper un
    nombre correspondant à l'un des choix.
    La fonction repose la question tant que l'utilisateur
    n'entre pas un nombre parmi les choix possibles.
    :param available_choices: Un dictionnaire où les clés sont
    des nombres et les valeurs sont du texte.
    :return: Renvoie un entier correspond au choix de
    l'utilisateur.
    """
    verif = 0
    for nombre, action in available_choices.items():
        print(f"{nombre} : {action}")
    while verif == 0 :
        choix = input("que voulez vous faire : ")
        if choix.isnumeric() is not True :
            print("veillez entre un nombre !")
        elif int(choix) not in available_choices.keys():
            print()
        else :
            verif = 1
    return int(choix)


def main():
    """
    Fonction principale du programme qui permet d'afficher le
    menu avec les différents choix possibles ainsi que la gestion de
    ses choix.
    :return: None
    """
    chemin = input("choisir un chemin : ")
    available_choices = {1: "affiche les logs d´un programme",
                         2: "charger un autre dossier contenant des fichiers de logs",
                         9: "termine le programme"}
    verif = 0
    while verif == 0 :
        match menu(available_choices):
            case 1 :
                logs = []
                for elem in load_log_from_file(chemin) :
                    log = Log(elem, chemin)
                    logs.append(log)
                program = input("entrez le nom du programe : ")
                log_manager = LogManager(logs)
                for log in log_manager.logs[program]:
                    print(log)
            case 2 :
                chemin = input ("choisir un autre chemin : ")
            case 9 :
                verif = 1


if __name__ == "__main__":
    main()
