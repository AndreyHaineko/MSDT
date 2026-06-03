# Лабораторная 1: что изменено

## Исходник

- **До:** `tennis_original.py`
- **После:** `LR1.py`
- **Источник кода:** [The Tennis Kata (Python)](https://github.com/emilybache/TheTennisKata-Python) — классическая задача Emily Bache для рефакторинга.

В PR видны **два файла**: исходная версия и результат правок. Сравнение: `git diff msdt-1/tennis_original.py msdt-1/LR1.py`.

## Применённые правила (≥ 5)

| № | Правило PEP8 / качества | Было (`tennis_original.py`) | Стало (`LR1.py`) |
|---|-------------------------|----------------------------|------------------|
| 1 | Именование переменных `snake_case` | `player1Name`, `p1points` | `player1_name`, `p1_points` |
| 2 | Именование методов и аргументов | `won_point(self, playerName)` | `won_point(self, player_name)` |
| 3 | Docstring модуля, класса и публичных методов | нет | есть у класса и `won_point`, `score` |
| 4 | Декомпозиция и устранение дублирования | отдельные `determine_winner`, `get_score`, словарь в `score()` | одна ветвистая `score()`, константы `SCORE_NAMES`, `TIED_BELOW_FOUR` |
| 5 | Строковые литералы | конкатенация `"Advantage " + name` | f-строки `f"Advantage {leader}"` |
| 6 | Типизация публичного API | без аннотаций | `-> str`, `-> None`, типы аргументов |
| 7 | Магические значения | `["Love", ...]` внутри метода | кортеж `SCORE_NAMES` на уровне класса |

## Рекомендуемые коммиты в PR

1. `refactor: snake_case для имён игроков и очков`
2. `refactor: docstring и константы счёта`
3. `refactor: упрощение метода score() и f-строки`
4. `docs: REFACTORING.md и пояснение исходника`

## Проверка

```bash
python -c "from LR1 import TennisGame; g=TennisGame('A','B'); g.won_point('A'); print(g.score())"
# Fifteen-Love
```
