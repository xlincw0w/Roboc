# @author Khazem Khaled
# Openclassrooms project

import os
import labyrinthe
import func

# MAIN PROGRAM
load_option = False
saved_data_fold = 'Saves/'
maps_data_fold = 'Cartes/'
last_map_name = 'lastmap.'

print('1 - Nouvelle Partie  ')

dirr = os.listdir()
if (dirr.count('Saves')):
    dirr = os.listdir(maps_data_fold)
    if (len(dirr) != 0):
        print('2 - Charger Partie  ')
        load_option = True

type_partie = input('> ... :  ')

while True:
    try: 
        type_partie = int(type_partie)
        if (type_partie > 2 or type_partie < 1):
            raise ValueError
        if (not load_option and type_partie == 2):
            raise ValueError    
        break
    except:
        type_partie = input('Erreur: Veuillez saisir un nombre correct : ')

if (type_partie == 1):
    print('Labyrinthes Existants : ')
    map_names = os.listdir(maps_data_fold) 
    cartes = []  
    for i in range(0, len(map_names)):
        carte = map_names[i]
        cartes.append((i+1, carte[:-3]))
        print('{} - {}'.format(i+1, carte[:-3]))

    user_choise = input('> Entrez un numéro de labyrinthe pour commencer à jouer : ')  

    while True:
        try: 
            user_choise = int(user_choise)
            if (user_choise > len(map_names) or user_choise < 1):
                raise ValueError
            break
        except:
            user_choise = input('Erreur: Veuillez saisir un nombre correct : ')

    loaded_map = func.read_from_file(maps_data_fold ,cartes[user_choise-1][1])  
    laby = labyrinthe.Labyrinthe(loaded_map[0], cartes[user_choise-1][1], loaded_map[1])
    laby.Transform()
    laby.Show()
    laby.Seek(labyrinthe.robot_char)
    laby.Seek(labyrinthe.exit_char)



elif (type_partie == 2):
    loaded_map = func.read_from_file(saved_data_fold, last_map_name)  
    laby = labyrinthe.Labyrinthe(0, last_map_name, loaded_map[1])
    laby.Transform()
    laby.Show()
    laby.Seek(labyrinthe.robot_char)
    laby.Seek(labyrinthe.exit_char)

func.run(laby)