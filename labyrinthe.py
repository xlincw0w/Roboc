# @author Khazem Khaled
# Openclassrooms project

import os
import shutil

# Structure character representation

wall_char = 'O'
exit_char = 'U'
door_char = '.'
robot_char = 'X'
clearway_char = ' '

# binds

up  = 'N'
down = 'S'
left = 'O'
right = 'E'
leave = 'Q'

class Labyrinthe:


    def __init__(self, id, name, lines):    # Constructor
        self.id = id
        self.name = name
        self.lines = lines
        self.robot = (0, 0)
        self.robot_is_in_door = False
        self.robot_is_moving_to_door = False
        self.exit = (0, 0)
        self.next_position = (0, 0)
        self.won = False


    # Getters and Setters

    def _getLines(self):
        return self.lines
    def _getRobot(self):
        return self.robot
    def _getExit(self):
        return self.exit
    def _getNextPosition(self):
        return self.next_position
    def _getWon(self):
        return self.won
    def _setLines(self, lines):
        self.lines = lines
    def _setRobot(self, robot):
        self.robot = robot
    def _setExit(self, exit):
        self.exit = exit
    def _setNextPosition(self, next):
        self.next_position = next
    def _setWon(self, bool):
        self.won = bool

    def Show(self):                   # Simple matrix show function
        print()
        __line = str()
        for line in self.lines:
            for char in line:
                __line += char
            print(__line)
            __line = str()

    def Transform(self):           # Transforming the map into a matrix
        labyr = []
        line = str()
        for i in range(0, len(self.lines)):
            if (self.lines[i] == '\n'):
                labyr.append(line) 
                line = str()
            else:
                line += self.lines[i]
        self.lines = labyr
    
    
    def Seek(self, thing):      # Finding position (x, y) of a Robot / Exit 
        if (thing == None or (thing != exit_char and thing != robot_char)):
            print('Erreur : Charactére non valide')
        for i in range(0, len(self.lines)):
            for j in range(0, len(self.lines[i])):
                if (self.lines[i][j] == thing):
                   continue
                else:
                    if (self.lines[i][j] == robot_char):
                        self._setRobot((i, j))
                    if (self.lines[i][j] == exit_char):
                        self._setExit((i, j)) 

    
    def getStructure(self, pos):    # Funtion that return a caractere
        if (pos[0] > len(self.lines) or pos[1] > len(self.lines[pos[0]])):
            print('Erreur : Position a vérifié dépasse le nombre de lignes / colonnes')
        if (pos == self.robot):
            print('Erreur : Positionnement')
        return self.lines[pos[0]][pos[1]]

    
    def Transpose(self, string, char, index):    # Function that helps grid manipulation
        temp = list(string)
        temp[index] = char 
        temp = "".join(temp)
        return temp


    def check_No_Collision(self, way):     # Caractere moving possibilities
        if (way == None):
            print('Erreur : Probleme de direction')

        if (way == up):

            if (self._getRobot()[0] == 0):
                return False
            else:
                if (self.getStructure( (self._getRobot()[0] - 1, self._getRobot()[1]) ) != wall_char):
                    self._setNextPosition( ((self._getRobot()[0] - 1, self._getRobot()[1])) )
                    return True
                else: 
                    return False  

        if (way == down):
            if (self._getRobot()[0] == len(self._getLines()) - 1 ):
                return False
            else:
                if (self.getStructure( (self._getRobot()[0] + 1, self._getRobot()[1]) ) != wall_char):
                    self._setNextPosition( ((self._getRobot()[0] + 1, self._getRobot()[1])) )
                    return True
                else: 
                    return False    

        if (way == right):
            if (self._getRobot()[1] == len(self._getLines()[self._getRobot()[0]]) - 1 ):
                return False
            else:
                if (self.getStructure( (self._getRobot()[0], self._getRobot()[1] + 1) ) != wall_char):
                    self._setNextPosition( ((self._getRobot()[0], self._getRobot()[1] + 1)) )
                    return True
                else: 
                    return False     

        if (way == left):
            if (self._getRobot()[1] == 0):
                return False
            else:
                if (self.getStructure( (self._getRobot()[0], self._getRobot()[1] - 1) ) != wall_char):
                    self._setNextPosition( ((self._getRobot()[0], self._getRobot()[1] - 1)) )
                    return True
                else: 
                    return False  


    def Update(self):      # Animation changing and Grid manipulation
        lines = self._getLines()
        rob_pos = self._getRobot() 
        next_pos = self._getNextPosition()
    
        if (self._getRobot() == None or self._getNextPosition() == None):
            print('Erreur : Position inéxistant')

        if (lines[next_pos[0]][next_pos[1]] == door_char):
            self.robot_is_moving_to_door = True

        if (lines[next_pos[0]][next_pos[1]] == exit_char):
            self._setWon(True)

        if (not self.robot_is_moving_to_door):
            if (not self.robot_is_in_door):
                lines[rob_pos[0]] = self.Transpose(lines[rob_pos[0]], clearway_char, rob_pos[1])
                lines[next_pos[0]] = self.Transpose(lines[next_pos[0]], robot_char, next_pos[1])
                self.robot_is_in_door = False
            else:
                lines[rob_pos[0]] = self.Transpose(lines[rob_pos[0]], door_char, rob_pos[1])
                lines[next_pos[0]] = self.Transpose(lines[next_pos[0]], robot_char, next_pos[1])
                self.robot_is_in_door = False
                self.robot_is_moving_to_door = False
        else:
            if (not self.robot_is_in_door):
                lines[rob_pos[0]] = self.Transpose(lines[rob_pos[0]], clearway_char, rob_pos[1])
                lines[next_pos[0]] = self.Transpose(lines[next_pos[0]], robot_char, next_pos[1])
                self.robot_is_in_door = True
                self.robot_is_moving_to_door = False
            else:
                lines[rob_pos[0]] = self.Transpose(lines[rob_pos[0]], door_char, rob_pos[1])
                lines[next_pos[0]] = self.Transpose(lines[next_pos[0]], robot_char, next_pos[1])
                self.robot_is_in_door = True
                self.robot_is_moving_to_door = False
        

        self._setRobot( (next_pos[0], next_pos[1]) )
        

    def Check_Winning(self):
        if (self._getWon()):
            shutil.rmtree('Saves')
            return True
        else:
            return False

    def Save(self):         # In real time file saving
        dirr = os.listdir()
        st = str()

        if (dirr.count('Saves') == 1):
            os.chdir('Saves/')
        elif (dirr.count('Saves') == 0):
            os.mkdir('Saves')
            os.chdir('Saves/')

        lines = self._getLines()

        for i in range(0, len(lines)):
            for j in range (0, len(lines[0])):
                st += lines[i][j]
            st += '\n'
            
        with open('lastmap.txt', 'w') as f:
            f.write(st)
            f.close()
        os.chdir('../')