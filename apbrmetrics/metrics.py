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
    def field_goal_percentage(cls, field_goals, field_goal_attempts):
        """
        Field Goal Percentage; the formula is FG / FGA.
        :param field_goals: Field Goals
        :param field_goal_attempts: Field Goal Attempts
        :return: (float) field_goal_percentage
        """
        return round(float(field_goals) / field_goal_attempts, 3)

    @classmethod
    def three_point_field_goals_per_game(cls, three_point_field_goals, games):
        """
        3-Point Field Goals Per Game
        :param three_point_field_goals: 3-Point Field Goals
        :param games: Games
        :return: (float) three_point_field_goals_per_game
        """
        return round(float(three_point_field_goals) / games, 1)

    @classmethod
    def three_point_field_goal_attempts_per_game(cls, three_point_field_goal_attempts, games):
        """
        3-Point Field Goal Attempts Per Game
        :param three_point_field_goal_attempts: 3-Point Field Goal Attempts
        :param games: Games
        :return: (float) three_point_field_goal_attempts_per_game
        """
        return round(float(three_point_field_goal_attempts) / games, 1)

    @classmethod
    def three_point_field_goal_percentage(cls, three_point_field_goals, three_point_field_goal_attempts):
        """
        3-Point Field Goal Percentage; the formula is 3P / 3PA.
        :param three_point_field_goals: 3-Point Field Goals
        :param three_point_field_goal_attempts: 3-Point Field Goal Attempts
        :return: (float) three_point_field_goal_percentage
        """
        return round(float(three_point_field_goals) / three_point_field_goal_attempts, 3)


    @classmethod
    def two_point_field_goals_per_game(cls, two_point_field_goals, games):
        """
        2-Point Field Goals Per Game
        :param two_point_field_goals: 3-Point Field Goals
        :param games: Games
        :return: (float) two_point_field_goals_per_game
        """
        return round(float(two_point_field_goals) / games, 1)

    @classmethod
    def two_point_field_goal_attempts_per_game(cls, two_point_field_goal_attempts, games):
        """
        2-Point Field Goal Attempts Per Game
        :param two_point_field_goal_attempts: 3-Point Field Goal Attempts
        :param games: Games
        :return: (float) two_point_field_goal_attempts_per_game
        """
        return round(float(two_point_field_goal_attempts) / games, 1)

    @classmethod
    def two_point_field_goal_percentage(cls, two_point_goals, two_point_attempts):
        """
        2-Point Field Goal Percentage; the formula is 2P / 2PA.
        :param two_point_goals: 2-Point Field Goals
        :param two_point_attempts: 2-Point Field Goal Attempts
        :return: (float) two_point_percentage
        """
        return round(float(two_point_goals) / two_point_attempts, 3)

    @classmethod
    def effective_field_goal_percentage(cls, field_goals, three_point_field_goals, field_goal_attempts):
        """
        Effective Field Goal Percentage; the formula is (FG + 0.5 * 3P) / FGA.
        :param field_goals: Field Goals
        :param three_point_field_goals: 3-Point Field Goals
        :param field_goal_attempts: Field Goal Attempts
        :return: (float) effective_field_goal_percentage
        """
        return round((float(field_goals) + 0.5 * three_point_field_goals) / field_goal_attempts, 3)

    @classmethod
    def free_throws_per_game(cls, free_throws, games):
        """
        Free Throws Per Game
        :param free_throws: Free Throws
        :param games: Games
        :return: (float) free_throws_per_game
        """
        return round(float(free_throws) / games, 1)

    @classmethod
    def free_throw_attempts_per_game(cls, free_throw_attempts, games):
        """
        Free Throw Attempts Per Game
        :param free_throw_attempts: Free Throw Attempts
        :param games: Games
        :return: (float) free_throw_attempts_per_game
        """
        return round(float(free_throw_attempts) / games, 1)

    @classmethod
    def free_throw_percentage(cls, free_throws, free_throw_attempts):
        """
        Free Throw Percentage; the formula is FT / FTA.
        :param free_throws: Free Throws
        :param free_throw_attempts: Free Throw Attempts
        :return: (float) free_throw_percentage
        """
        return round(float(free_throws) / free_throw_attempts, 3)

    @classmethod
    def offensive_rebounds_per_game(cls, offensive_rebounds, games):
        """
        Offensive Rebounds Per Game
        :param offensive_rebounds: Offensive Rebounds
        :param games: Games
        :return: (float) offensive_rebounds_per_game
        """
        return round(float(offensive_rebounds) / games, 1)

    @classmethod
    def deffensive_rebounds_per_game(cls, deffensive_rebounds, games):
        """
        Deffensive Rebounds Per Game
        :param deffensive_rebounds: Deffensive Rebounds
        :param games: Games
        :return: (float) deffensive_rebounds_per_game
        """
        return round(float(deffensive_rebounds) / games, 1)

    @classmethod
    def total_rebounds_per_game(cls, total_rebounds, games):
         """
         Total Rebounds Per Game
         :param total_rebounds: Total Rebounds
         :param games: Games
         :return: (float) total_rebounds_per_game
         """
         return round(float(total_rebounds) / games, 1)
