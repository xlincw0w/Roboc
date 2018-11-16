# @author Khazem Khaled
# Openclassrooms project

import labyrinthe

def read_from_file(dirr, map_name):    # Simple reading function
        with open(dirr + map_name +'txt') as fic:
            labyr = (map_name, fic.read())
            fic.close()
            return labyr

def run(laby):          # While loop that controls the game
    while True:
        try:
            user_decision = input('>')

            if (user_decision == ''):
                print('Erreur : Vous n''avez pas taper de direction')
            if (not user_decision[0].isalpha()):
                raise ValueError
                
            if (len(user_decision) > 1):
                for i in range(1, len(user_decision)):
                    if (not user_decision[i].isdigit()):
                        raise ValueError
                redundancy = int(user_decision[1:len(user_decision)])
            else:
                redundancy = 1

            action = user_decision[0].upper()
            
            if (action != labyrinthe.up and action != labyrinthe.down and action != labyrinthe.left and action != labyrinthe.right and action != labyrinthe.leave ):
                raise Exception
                

            if (action == labyrinthe.leave):
                break
            
            
        except Exception:
            print('Erreur: Veuillez saisir une valeur correct : \n')


        for _ in range(0, redundancy):
            if (not laby.check_No_Collision(action)):
                print('Direction impossible !')
            else:
                    laby.Update()
                    laby.Save()
                    laby.Show()

        if (laby.Check_Winning()):
            print('Félicitations ! Vous avez gagné !')
            break