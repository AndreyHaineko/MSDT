# -*- coding: utf-8 -*-
"""
ИСХОДНЫЙ КОД (до рефакторинга) — лабораторная 1.

Источник: Tennis kata (Emily Bache), репозиторий cyber-dojo:
https://github.com/emilybache/TheTennisKata-Python

Файл намеренно оставлен в «грязном» виде: camelCase, длинные методы,
дублирование веток, без docstring — чтобы в PR было видно, ЧТО менялось.
Финальная версия: LR1.py + описание правок в REFACTORING.md.
"""


class TennisGame:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        if self.p1points == self.p2points:
            if self.p1points < 4:
                return {
                    0: "Love-All",
                    1: "Fifteen-All",
                    2: "Thirty-All",
                    3: "Forty-All",
                }[self.p1points]
            return "Deuce"

        if self.p1points >= 4 or self.p2points >= 4:
            return self.determine_winner()

        return self.get_score()

    def determine_winner(self):
        minus_result = self.p1points - self.p2points
        if minus_result == 1:
            return "Advantage " + self.player1Name
        elif minus_result == -1:
            return "Advantage " + self.player2Name
        elif minus_result >= 2:
            return "Win for " + self.player1Name
        else:
            return "Win for " + self.player2Name

    def get_score(self):
        score_map = ["Love", "Fifteen", "Thirty", "Forty"]
        return score_map[self.p1points] + "-" + score_map[self.p2points]
