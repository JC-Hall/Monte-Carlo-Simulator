#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:45:44 2024

@author: dreadedjosh
"""

import numpy as np
import pandas as pd
from itertools import permutations
from collections import Counter

class Die: 
    def __init__(self, faces):        
        if not isinstance(faces, np.ndarray):
            raise TypeError("Faces must be a NumPy array.")
        
        if len(faces) != len(set(faces)):
            raise ValueError("Faces must have distinct values.")
        
        self._die_df = pd.DataFrame({
            'faces': faces,
            'weights': np.ones(len(faces))  
        }).set_index('faces')
    
    def change_weight(self, face, new_weight):
        if face not in self._die_df.index:
            raise IndexError("The specified face does not exist.")
        try:
            new_weight = float(new_weight)
        except ValueError:
            raise TypeError("The new weight must be numeric.")
        self._die_df.loc[face, 'weights'] = new_weight
    
    def roll(self, num_rolls=1):    
        if not isinstance(num_rolls, int) or num_rolls < 1:
            raise ValueError("Number of rolls must be a positive integer.")
        outcomes = self._die_df.sample(
            n=num_rolls,
            weights='weights',
            replace=True
        ).index.tolist()
        return outcomes

    def show(self):        
        return self._die_df.copy()
    
class Game:
    def __init__(self, dice):
        if not isinstance(dice, list) or not all(isinstance(d, Die) for d in dice):
            raise TypeError("Dice must be a list of Die objects.")
        self._dice = dice
        self._results = None
        
    def play(self, num_rolls):
        if not isinstance(num_rolls, int) or num_rolls < 1:
            raise ValueError("Number of rolls must be a positive integer.")
        results = {}
        for i, die in enumerate(self._dice):
            results[f"Die_{i}"] = die.roll(num_rolls)
        self._results = pd.DataFrame(results)
        self._results.index.name = 'Roll_Number'

    def show(self, form='wide'):
        if self._results is None:
            raise ValueError("No results available. Please play the game first.")
        if form == 'wide':
            return self._results.copy()
        elif form == 'narrow':
            return self._results.reset_index().melt(
                id_vars='Roll_Number',
                var_name='Die_Number',
                value_name='Outcome'
            ).set_index(['Roll_Number', 'Die_Number'])
        else:
            raise ValueError("Invalid form specified. Use 'wide' or 'narrow'.")    
    
class Analyzer:
    def __init__(self, game):
        if not isinstance(game, Game):
            raise ValueError("The input must be a Game object.")
        self._game = game
        self._results = game.show('wide')

    def jackpot(self):
        return (self._results.nunique(axis=1) ==1).sum()

    def face_counts_per_roll(self):
        return self._results.apply(pd.Series.value_counts, axis=1).fillna(0).astype(int)

    def combo_count(self):
        combinations = self._results.apply(lambda row: tuple(sorted(row)), axis=1)
        return combinations.value_counts().rename_axis('Combination').reset_index(name='Count')

    def permutation_count(self):
        perm_counts = Counter(
            perm for roll in self._results.itertuples(index=False) for perm in permutations(roll)
        )
        return pd.DataFrame.from_dict(perm_counts, orient='index', columns=['Count']).rename_axis('Permutation') 
   

   
    
   
    
   
    
   
    
   
