import unittest
from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer

class DieTestSuite(unittest.TestCase):

    def test_1_die(self):
        #check if die faces in dataframe
        test_die1 = Die([1,2,3,4,5,6])
        actual_faces = test_die1.show_die()['die_face'].values.tolist()
        expected_faces = [1,2,3,4,5,6]
        self.assertListEqual(actual_faces, expected_faces)

    def test_2_change_weights(self):
        #change weight of face that is not a number
        test_die1 = Die([1,2,3,4,5,6])
        self.assertRaises(Exception, test_die1.change_weights(1, 'h'))

    def test_2_change_weights(self):
        #change weight of face that is not in face list
        test_die1 = Die([1,2,3,4,5,6])
        self.assertRaises(Exception, test_die1.change_weights(7, 3))

    def test_4_change_weights(self):
        #change weights and check if new weights in dataframe
        test_die1 = Die([1,2,3,4,5,6])
        test_die1.change_weights(1, 1000)
        test_die1.change_weights(3, 57)
        actual_weights = test_die1.show_die()['die_weight'].values.tolist()
        expected_weights = [1000.0, 1.0, 57.0, 1.0, 1.0, 1.0]
        self.assertListEqual(actual_weights, expected_weights)

    def test_5_roll_die(self):
        #roll die 5 times and see if it rolls 5 times based on die face weights
        test_die1 = Die([1,2,3,4,5,6])
        test_die1.change_weights(1, 1000)
        actual = test_die1.roll_die(rolls = 2)
        expected = [1, 1]
        self.assertEqual(actual, expected)

    def test_6_show_die(self):
        #initalize die and check dataframe shape, n = die faces, m = 2
        test_die1 = Die([1,2,3,4])
        actual_shape = test_die1.show_die().shape
        expected_shape = (4,2)
        self.assertEqual(actual_shape, expected_shape)
    
class GameTestSuite(unittest.TestCase):

    def test_1_play(self):
        #play dice and see if length of dataframe equals number of rolls
        test_die1 = Die([1,2,3,4,5,6])
        test_die1.change_weights(3, 10)
        test_die2 = Die([1,2,3,4,5,6])
        test_die2.change_weights(1, 20)
        test_game = Game([test_die1, test_die2])
        test_game.play(rolls=3)
        self.assertEqual(len(test_game.show_play()), 3)

        
    def test_2_show_play(self):
        #play dice and test wide parameter only takes true/false
        test_die1 = Die([1,2,3,4,5,6])
        test_die1.change_weights(3, 20)
        test_die2 = Die([1,2,3,4,5,6])
        test_die2.change_weights(1, 20)
        test_game = Game([test_die1, test_die2])
        test_game.play(rolls=3)
        self.assertRaises(Exception, test_game.show_play(wide='narrow'))
    
    def test_3_show_play(self):
        #play die and check dataframe shape, n = num rolls, m = num die
        test_die1 = Die([1,2,3,4,5,6])
        test_die2 = Die([1,2,3,4,5,6])
        test_game = Game([test_die1, test_die2])
        test_game.play(rolls=8)
        actual_shape = test_game.show_play(wide=True).shape
        expected_shape = (8, 2)
        self.assertEqual(actual_shape, expected_shape)

    def test_4_show_play(self):
        #play die and check dataframe shape, n = num rolls * num die, m = 1 (narrow form)
        test_die1 = Die([1,2,3,4,5,6])
        test_die2 = Die([1,2,3,4,5,6])
        test_game = Game([test_die1, test_die2])
        test_game.play(rolls=8)
        actual_shape = test_game.show_play(wide=False).shape
        expected_shape = (16, 1)
        self.assertEqual(actual_shape, expected_shape)

class AnalyzerTestSuite(unittest.TestCase):

    def test_1_jackpot(self):
        #set die so that none will have the same results
        test_die1 = Die([1,2,3,4,5,6])
        test_die2 = Die([1,2,3,4,5,6])
        test_die1.change_weights(1, 1000)
        test_die2.change_weights(5, 1000)
        test_game = Game([test_die1, test_die2])
        test_game.play(rolls=3)
        test_analyzer = Analyzer(test_game)
        self.assertRaises(Exception, test_analyzer.jackpot())
    
    def test_2_jackpot(self):
        #set die so that all rolls will have same result to test jackpot count
        test_die1 = Die([1,2,3,4,5,6])
        test_die2 = Die([1,2,3,4,5,6])
        test_die1.change_weights(1, 1000)
        test_die2.change_weights(1, 1000)
        test_game = Game([test_die1, test_die2])
        test_game.play(rolls=3)
        test_analyzer = Analyzer(test_game)
        self.assertEqual(test_analyzer.jackpot(), 3)

    def test_3_combo(self):
        #set die so that all rolls have same combo and test that dataframe only has one value
        test_die1 = Die([1,2,3,4,5,6])
        test_die2 = Die([1,2,3,4,5,6])
        test_die1.change_weights(1, 1000)
        test_die2.change_weights(1, 1000)
        test_game = Game([test_die1, test_die2])
        test_game.play(rolls=5)
        test_analyzer = Analyzer(test_game)
        self.assertEqual(len(test_analyzer.combo()), 1)
    
    def test_4_face_counts_per_roll(self):
        #see if combo results dataframe length is the same as num rolls
        test_die1 = Die([1,2,3,4,5,6])
        test_die2 = Die([1,2,3,4,5,6])
        test_die1.change_weights(1, 1000)
        test_die2.change_weights(5, 1000)
        test_game = Game([test_die1, test_die2])
        test_game.play(rolls=3)
        test_analyzer = Analyzer(test_game)
        self.assertEqual(len(test_analyzer.face_counts_per_roll()), 3)

if __name__ == '__main__':
    unittest.main(verbosity=3)