#Importing all of the modules that i'll need for the program
from sqlite3.dbapi2 import connect
import sys
import os
import sqlite3
from sqlite3 import Error
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic
import random

#Creating a global dictionary to store all of my widget names to later use when linking the GUI widgets to the program
global widgets
widgets = {'QLineEdit': ['CharacterName', 'ClassLevel', 'Background', 'PlayerName', 'Race', 'Alignment', 'ExperiencePoints',
           'ProficeiencyBonus', 'Inspiration', 'StrengthMod', 'Strength', 'DexterityMod', 'Dexterity', 'ConstitutionMod', 'Constitution', 'IntelligenceMod',
           'Intelligence', 'WisdomMod', 'Wisdom', 'CharismaMod', 'Charisma', 'PassivePerception', 'ArmourClass', 'Initiative', 'Speed',
           'TemporaryHP', 'HPMax', 'CurrentHP', 'TotalHitDice', 'HitDice', 'Weapon1', 'Weapon2', 'Weapon3', 'Damage1', 'Damage2', 'Damage3',
           'Attack1', 'Attack2', 'Attack3', 'Copper', 'Silver', 'Electrum', 'Gold', 'Platinum', 'Age', 'Height', 'Weight', 'Eyes',
           'Skin', 'Hair', 'SpellcastingClass', 'SpellcastingAbility', 'SpellSaveDC', 'SpellAttackBonus', 'SlotsTotal1', 'Expended1',
           'SlotsTotal2', 'Expended2', 'SlotsTotal3', 'Expended3', 'SlotsTotal4', 'Expended4', 'SlotsTotal5', 'Expended5', 'SlotsTotal6',
           'Expended6', 'SlotsTotal7', 'Expended7', 'SlotsTotal8', 'Expended8', 'SlotsTotal9', 'Expended9'],
           'QPlainTextEdit': ['Personality', 'Ideals', 'Bonds', 'Flaws', 'AttacksSpellcasting',
           'FeaturesTraits', 'Equipment', 'OtherProfs', 'Allies', 'Backstory', 'Treasure', 'CantripSpells', 'Lvl1Spells', 'Lvl2Spells',
           'Lvl3Spells', 'Lvl4Spells', 'Lvl5Spells', 'Lvl6Spells', 'Lvl7Spells', 'Lvl8Spells', 'Lvl9Spells'],
           'QRadioButton': ['StrengthSave', 'Athletics', 'DexteritySave', 'Acrobatics', 'Stealth', 'SleightOfHand',
           'ConstitutionSave', 'IntelligenceSave', 'Arcana', 'History', 'Investigation', 'Nature', 'Religion', 'WisdomSave',
           'AnimalHandling', 'Insight', 'Medicine', 'Perception', 'Survival', 'CharismaSave', 'Deception',
           'Intimidation', 'Performance', 'Persuassion', 'Success1', 'Success2', 'Success3',
           'Fail1', 'Fail2', 'Fail3',
           'Lvl1Prep1', 'Lvl1Prep2', 'Lvl1Prep3', 'Lvl1Prep4', 'Lvl1Prep5', 'Lvl1Prep6', 'Lvl1Prep7', 'Lvl1Prep8', 'Lvl1Prep9',
           'Lvl1Prep10', 'Lvl1Prep11', 'Lvl1Prep12', 'Lvl1Prep13',
           'Lvl2Prep1', 'Lvl2Prep2', 'Lvl2Prep3', 'Lvl2Prep4', 'Lvl2Prep5', 'Lvl2Prep6', 'Lvl2Prep7', 'Lvl2Prep8', 'Lvl2Prep9',
           'Lvl2Prep10', 'Lvl2Prep11', 'Lvl2Prep12', 'Lvl2Prep13',
           'Lvl3Prep1', 'Lvl3Prep2', 'Lvl3Prep3', 'Lvl3Prep4', 'Lvl3Prep5', 'Lvl3Prep6', 'Lvl3Prep7', 'Lvl3Prep8', 'Lvl3Prep9',
           'Lvl3Prep10', 'Lvl3Prep11', 'Lvl3Prep12', 'Lvl3Prep13',
           'Lvl4Prep1', 'Lvl4Prep2', 'Lvl4Prep3', 'Lvl4Prep4', 'Lvl4Prep5', 'Lvl4Prep6', 'Lvl4Prep7', 'Lvl4Prep8', 'Lvl4Prep9',
           'Lvl4Prep10', 'Lvl4Prep11', 'Lvl4Prep12', 'Lvl4Prep13',
           'Lvl5Prep1', 'Lvl5Prep2', 'Lvl5Prep3', 'Lvl5Prep4', 'Lvl5Prep5', 'Lvl5Prep6', 'Lvl5Prep7', 'Lvl5Prep8', 'Lvl5Prep9',
           'Lvl5Prep10', 'Lvl5Prep11', 'Lvl5Prep12', 'Lvl5Prep13',
           'Lvl6Prep1', 'Lvl6Prep2', 'Lvl6Prep3', 'Lvl6Prep4', 'Lvl6Prep5', 'Lvl6Prep6', 'Lvl6Prep7', 'Lvl6Prep8', 'Lvl6Prep9',
           'Lvl6Prep10', 'Lvl6Prep11', 'Lvl6Prep12', 'Lvl6Prep13',
           'Lvl7Prep1', 'Lvl7Prep2', 'Lvl7Prep3', 'Lvl7Prep4', 'Lvl7Prep5', 'Lvl7Prep6', 'Lvl7Prep7', 'Lvl7Prep8', 'Lvl7Prep9',
           'Lvl7Prep10', 'Lvl7Prep11', 'Lvl7Prep12', 'Lvl7Prep13',
           'Lvl8Prep1', 'Lvl8Prep2', 'Lvl8Prep3', 'Lvl8Prep4', 'Lvl8Prep5', 'Lvl8Prep6', 'Lvl8Prep7', 'Lvl8Prep8', 'Lvl8Prep9',
           'Lvl8Prep10', 'Lvl8Prep11', 'Lvl8Prep12', 'Lvl8Prep13',
           'Lvl9Prep1', 'Lvl9Prep2', 'Lvl9Prep3', 'Lvl9Prep4', 'Lvl9Prep5', 'Lvl9Prep6', 'Lvl9Prep7', 'Lvl9Prep8', 'Lvl9Prep9',
           'Lvl9Prep10', 'Lvl9Prep11', 'Lvl9Prep12', 'Lvl9Prep13'],
           'QPushButton': ['Back', 'Dice', 'Save']}

#Global for the database connection
global conn
conn = sqlite3.connect(r"C:characterInformation.db")

#Global for the character name when a user choses a character they wish to load
global loadingCharacter
loadingCharacter = []

#Global for deleting a character
global delCharacter
delCharacter = []

#----Main Menu----#

class mainMenu(QtWidgets.QMainWindow):

    def __init__(self): #Initiator for the class
        super(mainMenu, self).__init__() #Giving the class control over itself
        uic.loadUi('home.ui', self) #Loading in the ui file for the screen

        menuWidgets = {'QPushButton': ['New', 'Load', 'Exit']} #Defining the widgets for this screen

        #Creating a loop that will automatically assign each widget the relevant data and commands.
        for widgettype in menuWidgets: #The widget type for the menu widgets
            for widget in range(0, len(menuWidgets[widgettype])): #Range loop
                #Connecting the widget to the program, so i can interact with it
                exec('self.' + menuWidgets[widgettype][widget] + ' = self.findChild(QtWidgets.' + widgettype + ', "' + menuWidgets[widgettype][widget] + '")')
                #Assing a button command to the buttons
                exec('self.' + menuWidgets[widgettype][widget] + '.clicked.connect(self.' + menuWidgets[widgettype][widget] + 'Function)')

        self.show()
        #Displaying the screen

    #----Button Funtions----#

    def NewFunction(self):
        #Button function for the 'New' button

        self.window = newCharacter() #Assigns the window variable as newCharacter()
        self.window.show() #Displaying that window
        mainMenu.close(self) #Closing the main menu

    def LoadFunction(self):
        #Button funtion for the 'Load' button

        self.window = loadCharacter() #Assigns the window variable as loadCharacter()
        self.window.show() #Displaying the window
        mainMenu.close(self) #Claoing the main menu

    def ExitFunction(self):
        #Button function for the 'Exit' button

        mainMenu.close(self) #Closing the main menu, terminating the program

#----New Character----#

class newCharacter(QtWidgets.QMainWindow):

    def __init__(self): #Initiator for the class
        super(newCharacter, self).__init__() #Giving the class control of itself
        uic.loadUi('newWindow.ui', self) #Loading in the ui file for the screen

        #Creating a loop that will automatically assign each widget the relevant data and commands.
        for widgettype in widgets: #The widget type for the character sheet widgets
            for widget in range(0, len(widgets[widgettype])): #Range loop
                #Using the global 'widgets' to allows all widgets to be connected
                exec('self.' + widgets[widgettype][widget] + ' = self.findChild(QtWidgets.' + widgettype + ', "' + widgets[widgettype][widget] + '")')
                #If statement for the buttons of the screen, as they need extra commands
                if widgettype == 'QPushButton':
                    #Button command assignment
                    exec('self.' + widgets[widgettype][widget] + '.clicked.connect(self.' + widgets[widgettype][widget] + 'Function)')

        self.show() #Displaying the window

    #----Button Functions----#

    def BackFunction(self):
        #Button function for the 'Back' button

        self.window = mainMenu() #Assigns the window variable as mainMenu()
        self.window.show() #Displaing the window
        newCharacter.close(self) #Closing the new character window

    def DiceFunction(self):
        #Button function for 'Dice' button

        self.window = diceRoller() #Assigns the window variable as diceRoller()
        self.window.show() #Displaying the window

    def SaveFunction(self):
        #Button function for the 'Save' button

        def main(self):
            #Function for saving data to the databse

            #Working with the database to save the data
            with conn:

                for widgettype in widgets: #The widget type for the character sheet widgets
                    for widget in range(len(widgets[widgettype])): #Range loop
                        #Elif statement to correctly save the data based on the widget
                        if widgets[widgettype][widget] == 'CharacterName':
                            #SQL statement to insert the data
                            sqlName = ''' INSERT INTO characters(CharacterName)
                                          VALUES(?) '''
                            #Setting data as the character name
                            data = self.CharacterName.text()
                            #Creating a cursor for the databse
                            cur = conn.cursor()
                            #Executing the cursor to save data into the databse
                            cur.execute(sqlName, [data])
                            #Committing data
                            conn.commit()
                        elif widgettype == 'QLineEdit':
                            #Setting line equal to the current QLineEdit widget
                            exec('line = self.' + widgets[widgettype][widget] + '.text()')
                            #Creating the SQL statemtent with each widget
                            exec("sql = ''' UPDATE characters\
                                            SET " + widgets[widgettype][widget] + " = ?\
                                            WHERE CharacterName = '" + data + "' '''")
                            #Creating a cursor for the database
                            exec('cur = conn.cursor()')
                            #Executing the cursor to save data into the database
                            exec('cur.execute(sql, [line])')
                            #Committing that data
                            exec('conn.commit()')
                        elif widgettype == 'QPlainTextEdit':
                            #Setting line equal to the current QPlaintTextEdit widget
                            exec('line = self.' + widgets[widgettype][widget] + '.toPlainText()')
                            #Creating the SQL statemtent with each widget
                            exec("sql = ''' UPDATE characters\
                                            SET " + widgets[widgettype][widget] + " = ?\
                                            WHERE CharacterName = '" + data + "' '''")
                            #Creating a cursor for the database
                            exec('cur = conn.cursor()')
                            #Executing the cursor to save data into the database
                            exec('cur.execute(sql, [line])')
                            #Committing the data
                            exec('conn.commit()')
                        elif widgettype == 'QRadioButton':
                            #Setting line equal to the current QCheckBox widget
                            exec('line = self.' + widgets[widgettype][widget] + '.isChecked()')
                            #Creating the SQL satment with each widget
                            exec("sql = ''' UPDATE characters\
                                            SET " + widgets[widgettype][widget] + " = ?\
                                            WHERE CharacterName = '" + data + "' '''")
                            #Creating a cursor for the databse
                            exec('cur = conn.cursor()')
                            #Executing the cursor to save data into the databse
                            exec('cur.execute(sql, [line])')
                            #Committing the data
                            exec('conn.commit()')
                        elif widgettype == 'QPushButton':
                            #Passing the widget if its a QPushButton
                            pass

            self.window = saved() #Assigning the window variable as saved()
            self.window.show() #Displaying the window
            newCharacter.close(self) #Closing the new character window

        if __name__ == '__main__':
            
            #Running the main() function if name = main, which it is
            main(self)

#----Load Character----#

class loadCharacter(QtWidgets.QMainWindow):

    def __init__(self): #Defining the initiator
        super(loadCharacter, self).__init__() #Giving the class control of itself
        uic.loadUi('load.ui', self) #Loading the ui file for the screen

        #Varaibles for each widget on this screen
        loadWidgets = {'QPushButton': ['Back', 'Delete', 'Select'],
                       'QListWidget': ['CharacterList']}

        for widgettype in loadWidgets: #The widget type for the load character widgets
            for widget in range(0, len(loadWidgets[widgettype])): #Range loop
                #Using the load widgets to connect the widgets to the program
                exec('self.' + loadWidgets[widgettype][widget] + ' = self.findChild(QtWidgets.' + widgettype + ', "' + loadWidgets[widgettype][widget] + '")')
                #If statements for the buttons on the screen, as they need extra commands
                if widgettype == 'QPushButton':
                    #Button command assignment
                    exec('self.' + loadWidgets[widgettype][widget] + '.clicked.connect(self.' + loadWidgets[widgettype][widget] + 'Function)')

        cur = conn.cursor() #Creating a cursor for the databse
        cur.execute('SELECT CharacterName FROM characters') #Exeecuting the cursor to select data frmo the databse
        rows = cur.fetchall() #Fetching all relevant data based on the query above

        #Loop for adding character names to a lsit
        for row in rows:

            #Addnig the character names to the list widget
            self.CharacterList.addItem(str(row[0]))

        self.show() #Displaying the window

    #----Button Functions----#

    def BackFunction(self):
        #Button function for the 'Back' button

        self.window = mainMenu() #Assigns the window variable as mainMenu()
        self.window.show() #Displaying the window
        loadCharacter.close(self) #Closing the load character window

    def DeleteFunction(self):
        #Button function for the 'Delete' button

        delCharacter.clear() #Clearing the variable now that it has been deleted

        cur = conn.cursor() #Creating a cursor for the database
        cur.execute('SELECT CharacterName FROM characters') #Executing the cursor to select data from the database
        rows = cur.fetchall() #Fetching all the relevant data absed on the query above

        #Loop for comparing selectino to the saved character names
        for row in rows:

            #If statement to delete selected name
            if self.CharacterList.currentItem().text() == row[0]:

                delCharacter.append(row[0]) #Sets delCharacter the the character the user wishes to delete
                self.window = confirmation() #Assigns the window variable as confirmation()
                self.window.show() #Displaying the window
                loadCharacter.close(self) #Closing the load character window

    def SelectFunction(self):
        #Button function for the 'Select' functino

        cur = conn.cursor() #Creating a cursor for the database
        cur.execute('SELECT CharacterName FROM characters') #Executing the cursor to select data from the databse
        rows = cur.fetchall() #Fetching all relevant data based on the query above

        #Loop for comparing selection to the saved character names
        for row in rows:

            #If statement to load appropriate data for character selected
            if self.CharacterList.currentItem().text() == row[0]:

                loadingCharacter.append(row[0]) #Appending the character name to the loadingCharacter global variable

                self.window = loadedCharacter() #Assigns the window varaible as loadedCharacter()
                self.window.show() #Displaying the window
                loadCharacter.close(self) #Closing the load character window

#----Loaded Character----#

class loadedCharacter(QtWidgets.QMainWindow):

    def __init__(self): #Defining the initiator
        super(loadedCharacter, self).__init__() #Giving the class control of itself
        uic.loadUi('loadedCharacter.ui', self) #Loading the ui file for the screen

        for widgettype in widgets: #The widget type for the global 'widgets' widgets
            for widget in range(0, len(widgets[widgettype])): #For loop
                #Using the globa 'widgets' to connect the widgets to the program
                exec('self.' + widgets[widgettype][widget] + ' = self.findChild(QtWidgets.' + widgettype + ', "' + widgets[widgettype][widget] + '")')
                #If statements for the buttons on the screen, as they need extra commands
                if widgettype == 'QPushButton':
                    #Button command assignment
                    exec('self.' + widgets[widgettype][widget] + '.clicked.connect(self.' + widgets[widgettype][widget] + 'Function)')

        def main(self):
            #Function for loading data from the database into the program's GUI

            #Working with the databse to retrieve the data needed
            with conn:

                #Creating a cursor for the databse
                cur = conn.cursor()
                #SQL statement to retrieve the relevant data based on the character chosen on the previous screen
                sql = ''' SELECT * FROM characters
                          WHERE CharacterName = ? '''
                #Executing the cursor to retrieve the data
                cur.execute(sql, loadingCharacter)
                data = [] #Variable to store all selected data
                count = 0 #Count variable to conut through the data loaded

                #Loop for appending all the relevant data to the 'data' variable
                for row in cur.fetchall():

                    data.append(row) #Adding the data to the varaible

                for widgettype in widgets: #The widget type of the gloabl 'widgets'
                    for i in range(len(widgets[widgettype])): #For loop
                        #Elif statement for appening a piece of data to the GUI
                        if widgettype == 'QLineEdit':
                            #Setting the specified widget as the current loaded data in 'data'
                            exec('self.' + widgets[widgettype][i] + '.setText("' + str(data[0][count]) + '")')
                            count += 1 #Adding 1 to the counter
                        elif widgettype == 'QPlainTextEdit':
                            #Setting the specified widget as the current loaded data in 'data'
                            exec('self.' + widgets[widgettype][i] + ".setPlainText('''" + data[0][count] + "''')")
                            count += 1 #Adding 1 to the counter
                        elif widgettype == 'QRadioButton':
                            #If statement to determine whether the data is a 1 or 0
                            if data[0][count] == 1:
                                #Setting the check box as checked if the data is 1
                                exec('self.' + widgets[widgettype][i] + '.setChecked(True)')
                            count += 1 #Adding 1 to the counter
                        elif widgettype == 'QPushButton':
                            count += 1 #Adding 1 to the counter
                            #Passing the widget as it's a push button
                            pass

        if __name__ == '__main__':

            #Running the main() function is name = main, which it is
            main(self)        

        self.show() #Displaying thw window

    #----Button Function----#

    def BackFunction(self):
        #Button function for the 'Back' button

        loadingCharacter.clear() #Clears all data in the loadingCharacter variable
        self.window = loadCharacter() #Assigns the window variable as loadCharacter()
        self.window.show() #Displaying the window
        loadedCharacter.close(self) #Closing the loaded character window

    def DiceFunction(self):
        #Button function for the 'Dice' button

        self.window = diceRoller() #Assigns the window variable as diceRoller()
        self.window.show() #Displaying the window

    def SaveFunction(self):
        #Button function for the 'Save' button

        def main(self):
            #Function for saving data to the databse

            #Working with the database to save the data
            with conn:

                for widgettype in widgets: #The widget type for the character sheet widgets
                    for widget in range(len(widgets[widgettype])): #Range loop
                        #Elif statement to correctly save the data based on the widget
                        if widgets[widgettype][widget] == 'CharacterName':
                            #SQL statement to insert the data
                            sqlName = ''' INSERT INTO characters(CharacterName)
                                          VALUES(?) '''
                            #Setting data as the character name
                            data = self.CharacterName.text()
                            #Creating a cursor for the databse
                            cur = conn.cursor()
                            #Executing the cursor to save data into the databse
                            cur.execute(sqlName, [data])
                            #Committing data
                            conn.commit()
                        elif widgettype == 'QLineEdit':
                            #Setting line equal to the current QLineEdit widget
                            exec('line = self.' + widgets[widgettype][widget] + '.text()')
                            #Creating the SQL statemtent with each widget
                            exec("sql = ''' UPDATE characters\
                                            SET " + widgets[widgettype][widget] + " = ?\
                                            WHERE CharacterName = '" + data + "' '''")
                            #Creating a cursor for the database
                            exec('cur = conn.cursor()')
                            #Executing the cursor to save data into the database
                            exec('cur.execute(sql, [line])')
                            #Committing that data
                            exec('conn.commit()')
                        elif widgettype == 'QPlainTextEdit':
                            #Setting line equal to the current QPlaintTextEdit widget
                            exec('line = self.' + widgets[widgettype][widget] + '.toPlainText()')
                            #Creating the SQL statemtent with each widget
                            exec("sql = ''' UPDATE characters\
                                            SET " + widgets[widgettype][widget] + " = ?\
                                            WHERE CharacterName = '" + data + "' '''")
                            #Creating a cursor for the database
                            exec('cur = conn.cursor()')
                            #Executing the cursor to save data into the database
                            exec('cur.execute(sql, [line])')
                            #Committing the data
                            exec('conn.commit()')
                        elif widgettype == 'QRadioButton':
                            #Setting line equal to the current QCheckBox widget
                            exec('line = self.' + widgets[widgettype][widget] + '.isChecked()')
                            #Creating the SQL satment with each widget
                            exec("sql = ''' UPDATE characters\
                                            SET " + widgets[widgettype][widget] + " = ?\
                                            WHERE CharacterName = '" + data + "' '''")
                            #Creating a cursor for the databse
                            exec('cur = conn.cursor()')
                            #Executing the cursor to save data into the databse
                            exec('cur.execute(sql, [line])')
                            #Committing the data
                            exec('conn.commit()')
                        elif widgettype == 'QPushButton':
                            #Passing the widget if its a QPushButton
                            pass

            self.window = saved() #Assigning the window variable as saved()
            self.window.show() #Displaying the window
            loadedCharacter.close(self) #Closing the loaded character screen

        #Working with the databse to remove data
        with conn:

            #Creating a cursor for the database
            cur = conn.cursor()
            #SQL statement to delete the data under the selected character, so that it can be re-written
            sql = ''' DELETE FROM characters
                      WHERE CharacterName = ? '''
            #Executing the cursor to delete the data
            cur.execute(sql, loadingCharacter)
            #Committing the changes
            conn.commit()

        if __name__ == '__main__':

            #Running the main() function is name = main, which it is
            main(self)

#----Dice Roller----#

class diceRoller(QtWidgets.QMainWindow):

    def __init__(self): #Defining the initiator
        super(diceRoller, self).__init__() #Giving the class control of itself
        uic.loadUi('diceSelection.ui', self) #Loading the ui file for the window

        #Variable for each widget on this screen
        diceWidgets = {'QPushButton': ['d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100']}

        for widgettype in diceWidgets: #The widget type of diceWidgets
            for widget in range(0, len(diceWidgets[widgettype])): #For loop
                #Using the diceWidgets to connect the widgets to the program
                exec('self.' + diceWidgets[widgettype][widget] + ' = self.findChild(QtWidgets.' + widgettype + ', "' + diceWidgets[widgettype][widget] + '")')
                #Button command assignment
                exec('self.' + diceWidgets[widgettype][widget] + '.clicked.connect(self.' + diceWidgets[widgettype][widget].upper() + ')')
                #Setting the image for the button
                exec('self.' + diceWidgets[widgettype][widget] + '.setStyleSheet("border-image: url(images/' + diceWidgets[widgettype][widget] + '.png);")')

        self.show() #Displaying the window

    #----Button Functions----#

    def D4(self):
        #Button function for the 'd4' button

        self.d4.setText(str(random.randint(1, 4)))
        #Sets the text as a random number between 1 and 4

    def D6(self):
        #Button function for the 'd6' button

        self.d6.setText(str(random.randint(1, 6)))
        #Sets the text as a random number between 1 and 6

    def D8(self):
        #Button function for the 'd8' button

        self.d8.setText(str(random.randint(1, 8)))
        #Sets the text as a random number between 1 and 8

    def D10(self):
        #Button function for the 'd10' button

        self.d10.setText(str(random.randint(1, 10)))
        #Sets the text as a random number between 1 and 10

    def D12(self):
        #Button function for the 'd12' button

        self.d12.setText(str(random.randint(1, 12)))
        #Sets the text as a random number between 1 and 12

    def D20(self):
        #Button function for the 'd20' button

        self.d20.setText(str(random.randint(1, 20)))
        #Sets the text as a random number between 1 and 20

    def D100(self):
        #Button function for the 'd100' button

        self.d100.setText(str(random.randint(1, 100)))
        #Sets the text as a random number between 1 and 100

#----Saved----#

class saved(QtWidgets.QMainWindow):

    def __init__(self): #Defining the initiator
        super(saved, self).__init__() #Giving the class control of itself
        uic.loadUi('saved.ui', self) #Loading the ui file for the screen

        #Variable for each widget on the screen
        savedWidgets = {'QPushButton': ['Okay']}

        for widgettype in savedWidgets: #The widget type of savedWidgets
            for widget in range(len(savedWidgets[widgettype])): #For loop
                #Using savedWidgets to connect the widgets to the program
                exec('self.' + savedWidgets[widgettype][widget] + ' = self.findChild(QtWidgets.' + widgettype + ', "' + savedWidgets[widgettype][widget] + '")')
                #Button command assignment
                exec('self.' + savedWidgets[widgettype][widget] + '.clicked.connect(self.' + savedWidgets[widgettype][widget] + 'Function)')

        self.show() #Displaying the screen

    def OkayFunction(self):
        #Button funtion for the 'Okay' button

        loadingCharacter.clear() #Clears the variable of all data
        self.window = mainMenu() #Assigning the window variable as mainMenu()
        self.window.show() #Displaying the window
        saved.close(self) #Closing the saved window

#----Confirmation----#

class confirmation(QtWidgets.QMainWindow):

    def __init__(self): #Defning the initiator
        super(confirmation, self).__init__() #Giving the class control of itself
        uic.loadUi('confirmation.ui', self) #Loading the ui file for the screen

        #Variable for each widget on the screen
        confirmWidgets = {'QPushButton': ['Yes', 'No']}

        for widgettype in confirmWidgets: #The widget type of confirmWidgets
            for widget in range(len(confirmWidgets[widgettype])): #For loop
                #Using confirmWidgets to connect the widgets to the program
                exec('self.' + confirmWidgets[widgettype][widget] + ' = self.findChild(QtWidgets.' + widgettype + ', "' + confirmWidgets[widgettype][widget] + '")')
                #Button command assignment
                exec('self.' + confirmWidgets[widgettype][widget] + '.clicked.connect(self.' + confirmWidgets[widgettype][widget] + 'Function)')

        self.show() #Displaying the screen

    def YesFunction(self):
        #Button function for the 'Yes' button
        
        cur = conn.cursor() #Creating a cursor for the database
        cur.execute('SELECT CharacterName FROM characters') #Executing the cursor to select data from the database
        rows = cur.fetchall() #Fetching all the relevant data absed on the query above

        #Loop for comparing selectino to the saved character names
        for row in rows:

            #If statement to delete selected name
            if delCharacter[0] == row[0]:

                #SQL statement for deleting a unwanted character
                sql = ''' DELETE FROM characters
                          WHERE CharacterName = ? '''
                #Executing the cursor to delete the data signified by 'delCharacter'
                cur.execute(sql, delCharacter)
                #Committing the changes
                conn.commit()

                self.window = loadCharacter() #Assigning the window variable as loadCharacter()
                self.window.show() #Displaying the window
                confirmation.close(self) #Closing the confirmation screen

    def NoFunction(self):
        #Button function for the 'No' button

        self.window = loadCharacter() #Assigning the window variable as loadCharacter()
        self.window.show() #Diplsaying the window
        confirmation.close(self) #Closing the confirmation screen

app = QtWidgets.QApplication(sys.argv) #Sets the app as a GUI based program
window = mainMenu() #Assigns the window varaible as mainMenu()
app.exec_() #Executes the program