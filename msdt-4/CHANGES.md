# Лабораторная 4: что добавлено

## Исходник и результат

| Файл | Назначение |
|------|------------|
| `dungeon_before.py` | Игра **без** `logging` (~115 строк) |
| `LR4.py` | Та же логика + **модуль logging** (~125 строк) |

В PR сравните: `git diff msdt-4/dungeon_before.py msdt-4/LR4.py`

Исходник — собственная упрощённая RPG на базе учебных примеров по ООП; доработан под условие лабы (≥100 строк, ≥5 точек логирования).

## Настройка логирования (`LR4.py`)

```python
logging.basicConfig(
    filename='game_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

Записи пишутся в файл `game_log.txt`, уровень INFO и выше.

## Точки логирования (8 событий)

| № | Событие | Где в `LR4.py` |
|---|---------|----------------|
| 1 | Старт игры | `main()` — `Game started.` |
| 2 | Создание персонажа | `Character.__init__` |
| 3 | Урон / HP | `Character.take_damage` |
| 4 | Лечение | `Character.heal` |
| 5 | Предмет в инвентарь | `Player.add_item` |
| 6 | Просмотр инвентаря | `Player.show_inventory` |
| 7 | Создание монстра | `create_monster` |
| 8 | Бой: атака, побег, урон монстра | `battle` |
| 9 | Исследование / пустая комната | `explore` |
| 10 | Game Over | `main()` в конце |

## Запуск

```bash
cd msdt-4
python LR4.py          # игра + лог в game_log.txt
python dungeon_before.py   # та же игра без лога
```
