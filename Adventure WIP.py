"""

ADVENTURE

Adventure is a open-world text-based game by Spider. Trying to mimic the old text games from the good ol' days, this game is only text, nothing else.

In Adventure, you can do anything from fight evil forces to discover magical fortresses to exploring the hidden caves.

Whatever you choose to do, it's your adventure.

TERMS

This is downloadable, but you must know that this game was made by Spider. It's illegal to pretend you made it. So don't steal it.

TESTING

If you want to test the game, you will have to message me in some way, and have access to Python 3. Do this, and I will give you access to the game.

After the full release, you will be thanked greatly and be put in the credits for an eternity.

"""

# Import modules
import sys
import time
import json
import random

# Define classes
class Adventure:
    """A class for making adventures."""

    def __init__(self, name, ID, characterList, location, dictionary):
        """Initiate function."""
        self.name = name
        self.ID = ID
        self.characterList = characterList
        self.location = location
        self.dictionary = dictionary

# Define functions
def titleSelect():
    """Everything the user(s) must do to start an adventure on the title page."""
    titleSelection = input('Type P for play, E to exit, or C for the credits. \t')

    # Check the user's selection
    if titleSelection.upper() == 'P':
        adventureSelect()

    elif titleSelection.upper() == 'E':
        print('Bye! Have a great day!')
        sys.exit()

    elif titleSelection.upper() == 'C':
        print()
        print('CREDITS')
        print()
        print('Coded and created by Spider.')
        print()
        titleSelect()

    else:
        notAnOption()
        titleSelect()

def adventureSelect():
    adventureSelection = input('Would you like to continue a saved adventure, or start a new one? Type C to continue a saved one, or N to make start a new adventure. \t')
    if adventureSelection.upper() == 'C':
        adventureID = input('Please type in the adventure ID. \t')

        # Check if the adventure ID exists
        retrievedID = open(adventureFilename,'r')
        print(retreivedID)
        currentAdventure = Adventure(retrievedName, retrievedID, retrievedCharacterList, retrievedLocation, {'Name': retrievedName, 'ID': adventureID, 'Characters': retrievedCharacterList, 'Location': retrievedLocation})

    elif adventureSelection.upper() == 'N':
        adventureName = input('What would you like to name your new adventure? \t')
        adventureID = random.randint(1, 10)

        # Name your adventure and give you the ID and basic adventure info
        currentAdventure = Adventure(adventureName, adventureID, [], '', {'Name': adventureName, 'ID': adventureID, 'Characters': [], 'Location': ''})
        print('New adventure named', currentAdventure.name, '. New adventure ID is', currentAdventure.ID, '. This adventure will be saved on this computer until you delete it or you make a new one. If you ever want info about your current adventure in-game, type \'info\'. Do not delete the files. You can manually save the adventure by typing in \'save\'. The adventure will save after every action.')

        # Save the new adventure
        save(currentAdventure.dictionary, adventureFilename)

        # Ask for the characters in the adventure
        

    else:
        notAnOption()
        adventureSelect()

def save(dictionary, filename):
    """Using a dictionary, save important info to a json file."""
    print('Saving...')
    with open(filename, 'w') as fileSaver:
        json.dump(dictionary, fileSaver)

    print('Saved!')

def notAnOption():
    """Tells the user that what they did is not an option."""
    print()
    print('Your input does not compute. Please try again.')
    print()
    
# Get global variables ready
global titleSelection
global adventureSelection
global adventureID
global adventureName
global characters
global filename
global adventureFilename
global characterFilename
global fileSaver
global retrievedName
global retrievedID
global retrievedCharacterList
global retrievedLocation
global currentAdventure

# Get save files ready
adventureFilename = 'adventureinfo.json'
characterFilename = 'characterinfo.json'
fileSaver = open(adventureFilename, 'w+')
fileSaver.close()
characterSaver = open(characterFilename, 'w+')
characterSaver.close()


# Title page
print('Welcome to...')
print()
time.sleep(3)
print('ADVENTURE')
print()
time.sleep(0.5)
print('An open-world text-based game by Spider. What do you want to do?')
titleSelect()
