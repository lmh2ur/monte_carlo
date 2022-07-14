"""
    The monte carlo simulator module lets you model chance mechanisms such as dice or coins. It does this by using random number generators to model the behaviorof random variables. 

    Classes:
        Die
        Game
        Analyzer
    
    Functions:
        change_weights(int, int or float)
        roll_die() -> list 
        show_die() -> dataframe
        play(int) 
        show_play() -> dataframe
        jackpot() -> int
        combo() -> dataframe
        face_counts_per_roll -> dataframe
"""
import pandas as pd
import numpy as np

class Die():
    """
    A class to represent a die. 

    Attributes
    ----------
        faces : list 
            strs, int or floats for faces of die
    
    Methods
    -------
        __init__(list) : initalize with list of faces
        change_weights(int, int or float) : change weight of face
        roll_die(int) : roll die specified amount of time, returns list of faces rolled
        show_die() : returns dataframe of the die object
    """

    def __init__(self, faces):
        """
        Constructor for die object.

        Parameters
        ----------
            faces : list
                strs, ints, or floats of die object faces
        """
        self.faces = faces
        self._weights = []
        for face in faces:
            self._weights.append(1.0)       
        self._df = pd.DataFrame({'die_face':faces, 'die_weight':self._weights})

    def change_weights(self, face, weight):
        """
        Changes the weight of a face of the die.

        Parameters
        ----------
            face : str, int or float 
                specfic die face wanting to be changes
            weight: int or float
                new weight of face

        Returns
        _______
            None

        Raises
        ______
            Exception : when face entered is not in die object 
            Exception : when weight is not an int or float
        """
        if face in self._df['die_face'].values:
            try:
                if isinstance(weight, float) == True or isinstance(float(weight),float) == True:
                    self._df.loc[self._df['die_face'] == face, 'die_weight'] = weight
            except:
                print("Weight is not a number.")
        else:
            print("Choose a face of the die.")

    def roll_die(self, rolls=1): 
        """
        Rolls die and returns list of face values randomly rolled based on weights.

        Parameters
        __________
            rolls : int
                number of rolls, default: rolls = 1
        
        Returns
        _______
            list of faces rolled
        """
        return [self._df['die_face'].sample(weights = self._df['die_weight']).values[0] for i in range(rolls)]
    
    def show_die(self):
        """
        Shows dataframe of die object.

        Parameters
        __________
            None

        Returns
        _______
            dataframe of die, columns = die_face, die_weight

        """
        return self._df


class Game():
    """
    Class for game of multiple dice.

    Attributes
    __________
        dice : list
            list of die objects to be played

    Methods 
    _______
        __init___(list) : initalize with list of die
        play(int) : specify number of rolls to be played
        show_play() : returns dataframe of playing game
    """
    def __init__(self, dice):
        """ 
        Constructor for game object. 

        Parameters
        __________
            dice : list
                list of die objects to be played 
        """
        self.dice = dice

    def play(self, rolls):
        """
        Plays die object a specified amount of times.

        Parameters
        __________
            rolls : int
                number of times to roll dice
        
        Returns
        _______
            None
        """
        self._play = pd.DataFrame({'roll_number':[], 'die_number':[], "face_rolled":[]})
        
        for i in range(rolls):
            for idx, die in enumerate(self.dice):
                _die_roll = Die.roll_die(die)
                _new_roll = pd.DataFrame({'roll_number':[i+1],'die_number':[idx+1], 'face_rolled': [_die_roll]})
                self._play = pd.concat([self._play, _new_roll], ignore_index=True)

        self._play = self._play.astype({'roll_number':'int32', 'die_number':'int32'})
        self._play = self._play.reset_index(drop=True).set_index(['roll_number','die_number'])

    def show_play(self, wide = True):
        """
        Shows dataframe of playing dice.

        Parameters
        __________
            wide : boolean
                returns wide or narrow dataframe, default: wide = True
        
        Returns
        _______
            Dataframe of results from play method with information about roll number, die number and face rolled

        Raises
        ______
            Exception : when wide is not set to a boolean
        """
        if wide == True:
            _wide_df = self._play.face_rolled.unstack()
            return _wide_df
        elif wide == False:
            _narrow_df = self._play
            return _narrow_df
        else:
            print("Set wide equal to True or False.")

class Analyzer():
    """
    Class for analyzing game.

    Attributes
    __________
        game : object
            played game object
        jackpot_count : int
            number of times same faces are rolled
        jackpot_results : dataframe
            all rolls that produced same faces 
        combo_results : dataframe
            counts of all combinations of faces rolled
        face_counts_results : dataframe
            counts of all the faces rolled per roll 
    
    Methods
    _______
        __init__(object) : initalize with game object
        jackpot() : returns count of number of jackpots
        combo() : returns dataframe of combinations and counts
        face_counts_per_roll() : returns dataframe of counts of faces rolled
    """
    def __init__(self, game):
        """
        Constructor for analyzer class. 

        Parameters
        __________
            game : object of played game class
        """
        self.game = Game.show_play(game).astype(str)
    
    def jackpot(self):
        """
        Calculates number of jackpots which is when roll produces all die having the same face.

        Parameters
        __________
            None
        
        Returns
        _______
            jackpot_count : int
                number of jackpots per game
        
        Raise
        _____
            Exception : when there are no jackpots for the game
        """
        _same_faces = self.game.eq(self.game.iloc[:,0],axis=0).all(axis=1)
        self.jackpot_results = self.game[_same_faces]

        self.jackpot_count = 0

        for i in range(len(self.game)):
            if _same_faces[i+1] == True:
                self.jackpot_count += 1

        if self.jackpot_count == 0:
            print("No rolls resulted in all the dice having the same face")
        else:
            return self.jackpot_count
            
    def combo(self):
        """
        Calculates the number of unique combinations in a game.

        Parameters
        __________
            None
        
        Returns
        _______
            combo_results : dataframe
                The different combinations produced and count of each
        """
        self.combo_results = self.game.value_counts().reset_index().rename(columns={0:'count'})

        return self.combo_results
    
    def face_counts_per_roll(self):
        """
        Calculates count of each face rolled per roll.

        Parameters
        __________
            None
        
        Returns
            face_counts_results : dataframe
                count of face rolled per roll
        """

        _face_values_per_roll = self.game.unstack().droplevel(0)

        self.face_counts_results = _face_values_per_roll.groupby(['roll_number']).value_counts().to_frame().reset_index().rename(columns={'level_1': 'face_rolled', 0:'count'}).set_index(['roll_number', 'face_rolled']).unstack(fill_value = 0)

        return self.face_counts_results