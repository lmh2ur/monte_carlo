# Monte Carlo Simulator 

## Metadata
Leah Hogenmiller (lmh2ur)
Final Project for DS5100

## Synopsis

### Installing
1. Clone repo <br />
`git clone https://github.com/lmh2ur/monte_carlo.git`
2. Install <br />
`git install .`

### Importing
1. Importing Die class <br />
  `from montecarlo import Die` <br />
2. Importing Game class <br />
  `from montecarlo import Game` <br />
3. Importing Analzyer class <br />
  `from montecarlo import Analyzer` <br />
 
 ### Creating a die
 1. Intializing die object <br />
 `die = Die([faces])`
 2. Change weight of die face <br /> 
 `die.change_weights(face, weight)` <br />
 3. Roll die <br />
 `die.roll_die(rolls)`
 4. Show die  <br />
 `die.show()` <br />
 Returns dataframe of die faces and weights
 
 ### Playing a game
 1. Intializing game object <br />
 `game = Game([dice])`
 2. Play game (must be done before showing play or analzying game) <br />
 `game.play(rolls)`
 3. Show play <br />
 `game.show_play()`<br />
 Returns dataframe of face rolled for each die for each roll
 
 ### Analzying a game
 1. Intializing analyzer object <br />
 `analyze = Analzyer(game)`
 2. Number of jackpots (same faces rolled for a roll) <br />
 `analzye.jackpot()` <br />
 Returns jackpot_count
 3. Dataframe of jackpots <br />
 `analyze.jackpot_results` <br />
 Returns dataframe of jackpots for a game
 4. Count of different combinations <br />
 `analyze.combo()` <br />
 Returns dataframe of counts for each different combinations
 5. Face counts per roll <br />
 `analyze.face_counts_per_roll()` <br />
 Returns dataframe of count for each face rolled for every roll
 
 ## API Description
 ### Die Class
 ```
    Attributes
    ----------
        faces : list 
            strs, int or floats for faces of die
    
    Methods
    -------
        __init__(list) : initalize with list of faces
        change_weights(int, int or float) : change weight of face
        roll_die(int) : roll die specified amount of time, returns list of faces rolled, default: roll = 1
        show_die() : returns dataframe of die faces and weights in wide form, default: wide = True
 ```
 ### Game Class
 ```
    Attributes
    __________
        dice : list
            list of die objects to be played

    Methods 
    _______
        __init___(list) : initalize with list of die
        play(int) : specify number of rolls to be played
        show_play() : returns dataframe of faces rolled per die number per roll 
 ```
 ### Analzyer Class
 ```
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
        combo() : returns dataframe counts of each different combination
        face_counts_per_roll() : returns dataframe of counts of faces rolled per roll 
```
## Manifest 
- monte_carlo_package <br />
  - montecarlo.py
  - \_\_init_\_\.py
- LICENSE
- README.md
- Scenarios.ipynb
- final_project_submission.ipynb
- montecarlo_rsults.txt
- montecarlo_test.py
- setup.py
