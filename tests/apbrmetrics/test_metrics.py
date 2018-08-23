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
        field_goals_per_game = Metrics.field_goals_per_game(622, 79)
        self.assertEqual(field_goals_per_game, 7.9)

    def test_field_goal_attempts_per_game(self):
        # Lebron James(2003-2004)
        field_goal_attempts_per_game = Metrics.field_goal_attempts_per_game(1492, 79)
        self.assertEqual(field_goal_attempts_per_game, 18.9)

    def test_field_goal_percentage(self):
        # Lebron James(2003-2004)
        field_goal_percentage = Metrics.field_goal_percentage(622, 1492)
        self.assertEqual(field_goal_percentage, 0.417)

    def test_three_point_field_goals_per_game(self):
        # Lebron James(2003-2004)
        three_point_field_goals_per_game = Metrics.three_point_field_goals_per_game(63, 79)
        self.assertEqual(three_point_field_goals_per_game, 0.8)

    def test_three_point_field_goal_attempts_per_game(self):
        # Lebron James(2003-2004)
        three_point_field_goal_attempts_per_game = Metrics.three_point_field_goal_attempts_per_game(217, 79)
        self.assertEqual(three_point_field_goal_attempts_per_game, 2.7)

    def test_three_point_field_goal_percentage(self):
        # Lebron James(2003-2004)
        miniutes_played_per_game = Metrics.three_point_field_goal_percentage(63, 217)
        self.assertEqual(miniutes_played_per_game, 0.290)

    def test_two_point_field_goals_per_game(self):
        # Lebron James(2003-2004)
        two_point_field_goals_per_game = Metrics.two_point_field_goals_per_game(559, 79)
        self.assertEqual(two_point_field_goals_per_game, 7.1)

    def test_two_point_field_goal_attempts_per_game(self):
        # Lebron James(2003-2004)
        two_point_field_goal_attempts_per_game = Metrics.two_point_field_goal_attempts_per_game(1275, 79)
        self.assertEqual(two_point_field_goal_attempts_per_game, 16.1)

    def test_two_point_field_goal_percentage(self):
        # Lebron James(2003-2004)
        two_point_field_goal_percentage = Metrics.two_point_field_goal_percentage(559, 1275)
        self.assertEqual(two_point_field_goal_percentage, 0.438)

    def test_effective_field_goal_percentage(self):
        # Lebron James(2003-2004)
        effective_field_goal_percentage = Metrics.effective_field_goal_percentage(622, 63, 1492)
        self.assertEqual(effective_field_goal_percentage, 0.438)

    def test_free_throws_per_game(self):
        # Lebron James(2003-2004)
        free_throws_per_game = Metrics.free_throws_per_game(347, 79)
        self.assertEqual(free_throws_per_game, 4.4)

    def test_free_throw_attempts_per_game(self):
        # Lebron James(2003-2004)
        free_throw_attempts_per_game = Metrics.free_throw_attempts_per_game(460, 79)
        self.assertEqual(free_throw_attempts_per_game, 5.8)

    def test_free_throw_percentage(self):
        # Lebron James(2003-2004)
        free_throw_percentage = Metrics.free_throw_percentage(347, 460)
        self.assertEqual(free_throw_percentage, 0.754)

    def test_offensive_rebounds_per_game(self):
        # Lebron James(2003-2004)
        offensive_rebounds_per_game = Metrics.offensive_rebounds_per_game(99, 79)
        self.assertEqual(offensive_rebounds_per_game, 1.3)

    def test_deffensive_rebounds_per_game(self):
        # Lebron James(2003-2004)
        deffensive_rebounds_per_game = Metrics.deffensive_rebounds_per_game(333, 79)
        self.assertEqual(deffensive_rebounds_per_game, 4.2)
