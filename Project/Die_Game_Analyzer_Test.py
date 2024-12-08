#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 22:41:42 2024

@author: dreadedjosh
"""

import unittest
import numpy as np
import pandas as pd
from itertools import permutations
from collections import Counter

from Die_Game_Analyzer_Class import Die, Game, Analyzer

class TestDie(unittest.TestCase):
    def setUp(self):
        self.faces = np.array([1, 2, 3, 4, 5, 6])
        self.die = Die(self.faces)

    def test_initialization(self):
        self.assertIsInstance(self.die.show(), pd.DataFrame, "Die should store its state as a DataFrame.")

    def test_change_weight(self):
        self.die.change_weight(1, 2.5)
        self.assertEqual(self.die.show().loc[1, 'weights'], 2.5, "Weight for face 1 should be updated to 2.5.")

    def test_roll(self):
        rolls = self.die.roll(10)
        self.assertEqual(len(rolls), 10, "Roll method should return a list of length 10.")
        self.assertTrue(all(face in self.faces for face in rolls), "All rolled faces should be in the die's faces.")

    def test_show(self):
        df = self.die.show()
        self.assertIsInstance(df, pd.DataFrame, "Show method should return a DataFrame.")
        self.assertIn('weights', df.columns, "DataFrame should contain a 'weights' column.")

class TestGame(unittest.TestCase):
    def setUp(self):
        self.faces = np.array([1, 2, 3, 4, 5, 6])
        self.die1 = Die(self.faces)
        self.die2 = Die(self.faces)
        self.game = Game([self.die1, self.die2])

    def test_initialization(self):
        self.assertIsInstance(self.game._dice, list, "Game should be initialized with a list of dice.")

    def test_play(self):
        self.game.play(5)
        results = self.game.show()
        self.assertEqual(results.shape[0], 5, "Results should have 5 rows, one for each roll.")
        self.assertEqual(results.shape[1], 2, "Results should have 2 columns, one for each die.")

    def test_show_wide(self):
        self.game.play(3)
        results = self.game.show('wide')
        self.assertIsInstance(results, pd.DataFrame, "Show method in 'wide' form should return a DataFrame.")

    def test_show_narrow(self):
        self.game.play(3)
        results = self.game.show('narrow')
        self.assertIsInstance(results, pd.DataFrame, "Show method in 'narrow' form should return a DataFrame.")
        self.assertTrue('Die_Number' in results.index.names, "Narrow results should have 'Die_Number' in the index.")

class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        self.faces = np.array([1, 2, 3, 4, 5, 6])
        self.die1 = Die(self.faces)
        self.die2 = Die(self.faces)
        self.game = Game([self.die1, self.die2])
        self.game.play(10)
        self.analyzer = Analyzer(self.game)

    def test_initialization(self):
        self.assertIsInstance(self.analyzer._results, pd.DataFrame, "Analyzer should store game results in a DataFrame.")

    def test_jackpot(self):
        jackpots = self.analyzer.jackpot()
        self.assertTrue(isinstance(jackpots, (int, np.integer)), "Jackpot method should return an integer.")

    def test_face_counts_per_roll(self):
        face_counts = self.analyzer.face_counts_per_roll()
        self.assertIsInstance(face_counts, pd.DataFrame, "Face counts per roll should return a DataFrame.")
        self.assertTrue((face_counts >= 0).all().all(), "All counts should be non-negative.")

    def test_combo_count(self):
        combo_counts = self.analyzer.combo_count()
        self.assertIsInstance(combo_counts, pd.DataFrame, "Combo count should return a DataFrame.")
        self.assertIn('Count', combo_counts.columns, "Combo count DataFrame should have a 'Count' column.")

    def test_permutation_count(self):
        permutation_counts = self.analyzer.permutation_count()
        self.assertIsInstance(permutation_counts, pd.DataFrame, "Permutation count should return a DataFrame.")
        self.assertIn('Count', permutation_counts.columns, "Permutation count DataFrame should have a 'Count' column.")

# Run the tests
if __name__ == '__main__':
    unittest.main(verbosity=3)