"""
Лабораторная 7: асинхронный сбор и обработка данных.

Сценарий (осмысленный, не sleep ради sleep):
  Есть 5 независимых «источников данных» (условные API/БД).
  1) Параллельно запрашиваем все источники (fetch) — имитация сетевой задержки.
  2) Параллельно обрабатываем полученные строки (process) — имитация CPU/I/O.

Используется asyncio.gather для конкурентного выполния корутин.
Запуск: python LR7.py
"""

import asyncio
import random
from typing import List


async def fetch_from_source(source_id: int) -> str:
    """
    Шаг 1: асинхронное получение данных из источника source_id.

    В реальном приложении здесь был бы aiohttp / asyncpg и т.д.
    """
    print(f"[fetch] Запрос к источнику {source_id}...")
    await asyncio.sleep(random.uniform(1, 3))
    payload = f"Данные из источника {source_id}"
    print(f"[fetch] Источник {source_id}: {payload}")
    return payload


async def process_record(raw: str) -> str:
    """
    Шаг 2: асинхронная обработка одной записи (нормализация, валидация, запись).

    Имитируем работу, которая не блокирует event loop надолго (await sleep).
    """
    print(f"[process] Обработка: {raw}...")
    await asyncio.sleep(random.uniform(1, 2))
    result = f"Обработанные {raw}"
    print(f"[process] Готово: {result}")
    return result


async def run_pipeline(source_ids: List[int]) -> List[str]:
    """
    Полный пайплайн: gather(fetch) -> gather(process).

    Возвращает список обработанных строк.
    """
    print(f"Старт пайплайна для источников: {source_ids}\n")

    raw_rows = await asyncio.gather(
        *(fetch_from_source(sid) for sid in source_ids)
    )

    processed = await asyncio.gather(
        *(process_record(row) for row in raw_rows)
    )

    return processed


async def main() -> None:
    sources = [1, 2, 3, 4, 5]
    results = await run_pipeline(sources)

    print("\n=== Итог пайплайна ===")
    for line in results:
        print(line)


if __name__ == "__main__":
    asyncio.run(main())
