# -*- coding: utf-8 -*-

__author__ = 'Keita Tsukamoto'

class Metrics(object):

    def __init__(self):
        pass

    @classmethod
    def miniutes_played_per_game(cls, minutes_played, games):
        """
        Minutes Played Per Game
        :param minutes_played: Minutes Played
        :param games: Games
        :return: (float) miniutes_played_per_game
        """
        return round(float(minutes_played) / games, 1)

    @classmethod
    def field_goals_per_game(cls, field_goals, games):
        """
        Field Goals Per Game
        :param field_goals: Field Goals
        :param games: Games
        :return: (float) field_goals_per_game
        """
        return round(float(field_goals) / games, 1)

    @classmethod
    def field_goal_attempts_per_game(cls, field_goal_attempts, games):
        """
        Field Goal Attempts Per Game
        :param field_goal_attempts: Field Goal Attempts
        :param games: Games
        :return: (float) field_goal_attempts_per_game
        """
        return round(float(field_goal_attempts) / games, 1)

    @classmethod
    def two_point_percentage(cls, two_point_goals, two_point_attempts):
        """
        2P%: 2-Point Field Goal Percentage; the formula is 2P / 2PA.
        :param two_point_goals: 2-Point Field Goals
        :param two_point_attempts: 2-Point Field Goal Attempts
        :return: (float) two_point_percentage
        """
        return round(float(two_point_goals) / two_point_attempts, 3)