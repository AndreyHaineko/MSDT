# -*- coding: utf-8 -*-
"""
ФИНАЛЬНЫЙ КОД (после рефакторинга) — лабораторная 1.

Счёт в теннисе для двух игроков. Рефакторинг исходника из tennis_original.py.
Список применённых правил PEP8: см. REFACTORING.md.
"""


class TennisGame:
    """Подсчёт очков в одиночном матче (правила love / deuce / advantage)."""

    SCORE_NAMES = ("Love", "Fifteen", "Thirty", "Forty")
    TIED_BELOW_FOUR = {
        0: "Love-All",
        1: "Fifteen-All",
        2: "Thirty-All",
        3: "Forty-All",
    }

    def __init__(self, player1_name: str, player2_name: str) -> None:
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, player_name: str) -> None:
        """Начислить очко игроку по имени."""
        if player_name == self.player1_name:
            self.p1_points += 1
        else:
            self.p2_points += 1

    def score(self) -> str:
        """Текущая строка счёта для отображения."""
        if self.p1_points < 4 and self.p2_points < 4:
            if self.p1_points == self.p2_points:
                return self.TIED_BELOW_FOUR[self.p1_points]
            return (
                f"{self.SCORE_NAMES[self.p1_points]}-"
                f"{self.SCORE_NAMES[self.p2_points]}"
            )
        if self.p1_points == self.p2_points:
            return "Deuce"

        leader = (
            self.player1_name
            if self.p1_points > self.p2_points
            else self.player2_name
        )
        diff = abs(self.p1_points - self.p2_points)
        if diff == 1:
            return f"Advantage {leader}"
        return f"Win for {leader}"
