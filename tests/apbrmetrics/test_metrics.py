# -*- coding: utf-8 -*-

__author__ = 'Keita Tsukamoto'

import unittest
from apbrmetrics.metrics import Metrics

class TestMetrics(unittest.TestCase):
    """
    Metrics Class Tests
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_miniutes_played_per_game(self):
        # Lebron James(2003-2004)
        miniutes_played_per_game = Metrics.miniutes_played_per_game(3122, 79)
        self.assertEqual(miniutes_played_per_game, 39.5)

    def test_field_goals_per_game(self):
        # Lebron James(2003-2004)
        miniutes_played_per_game = Metrics.field_goals_per_game(622, 79)
        self.assertEqual(miniutes_played_per_game, 7.9)

    def test_field_goal_attempts_per_game(self):
        # Lebron James(2003-2004)
        miniutes_played_per_game = Metrics.field_goal_attempts_per_game(1492, 79)
        self.assertEqual(miniutes_played_per_game, 18.9)

    def test_two_point_percentage(self):
        # Lebron James(2003-2004)
        miniutes_played_per_game = Metrics.two_point_percentage(559, 1275)
        self.assertEqual(miniutes_played_per_game, 0.438)
