"""
Юнит-тесты для msdt-5/main.py — сервис управления пользователями.

Что тестируем (не «кот в мешке»):
  - UserService + UserRepository + User из main.py
  - Сценарии: регистрация, чтение, смена имени/email, список всех пользователей

Два режима:
  1) «Интеграционные» тесты с настоящим UserRepository (без моков)
  2) Тесты с MagicMock репозитория — проверяем, что сервис вызывает add_user/update_user
"""

import os
import sys

import pytest
from unittest.mock import MagicMock

ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from main import User, UserRepository, UserService


@pytest.fixture
def real_repository():
    """Реальное хранилище в памяти — для проверки полного цикла операций."""
    return UserRepository()


@pytest.fixture
def real_service(real_repository):
    """UserService поверх реального репозитория."""
    return UserService(real_repository)


@pytest.fixture
def mock_repository():
    """Подмена репозитория: изолируем логику сервиса от хранилища."""
    return MagicMock(spec=UserRepository)


@pytest.fixture
def mock_service(mock_repository):
    return UserService(mock_repository)


# --- Реальный репозиторий: поведение end-to-end ---


def test_create_user_real(real_service):
    """Создание пользователя: UUID, имя и email сохраняются в репозитории."""
    user = real_service.create_user("John Doe", "john.doe@example.com")
    assert user.user_id is not None
    assert user.name == "John Doe"
    assert user.email == "john.doe@example.com"


def test_get_user_real(real_service):
    """После create_user get_user возвращает того же пользователя."""
    user = real_service.create_user("John Doe", "john.doe@example.com")
    fetched_user = real_service.get_user(user.user_id)
    assert fetched_user is not None
    assert fetched_user.name == "John Doe"
    assert fetched_user.email == "john.doe@example.com"


def test_update_user_name_real(real_service):
    """update_user_name меняет имя в объекте, доступном через get_user."""
    user = real_service.create_user("John Doe", "john.doe@example.com")
    real_service.update_user_name(user.user_id, "John Smith")
    updated_user = real_service.get_user(user.user_id)
    assert updated_user.name == "John Smith"


def test_update_user_email_real(real_service):
    """update_user_email меняет email в хранилище."""
    user = real_service.create_user("John Doe", "john.doe@example.com")
    real_service.update_user_email(user.user_id, "john.smith@example.com")
    updated_user = real_service.get_user(user.user_id)
    assert updated_user.email == "john.smith@example.com"


def test_get_all_users_real(real_service):
    """get_all_users возвращает всех созданных пользователей."""
    real_service.create_user("John Doe", "john.doe@example.com")
    real_service.create_user("Jane Doe", "jane.doe@example.com")
    all_users = real_service.get_all_users()
    assert len(all_users) == 2


# --- Моки: сервис должен вызывать методы репозитория ---


def test_create_user_mock(mock_service, mock_repository):
    """create_user делегирует сохранение в repository.add_user."""
    mock_service.create_user("John Doe", "john.doe@example.com")
    mock_repository.add_user.assert_called_once()


def test_update_user_name_mock(mock_service, mock_repository):
    """При обновлении имени сервис читает user, меняет поле и вызывает update_user."""
    mock_user = User("1", "John Doe", "john.doe@example.com")
    mock_repository.get_user.return_value = mock_user
    mock_service.update_user_name("1", "John Smith")
    assert mock_user.name == "John Smith"
    mock_repository.update_user.assert_called_once()


@pytest.mark.parametrize(
    "name, email, new_name, new_email",
    [
        ("John Doe", "john.doe@example.com", "John Smith", "john.smith@example.com"),
        ("Jane Doe", "jane.doe@example.com", "Jane Smith", "jane.smith@example.com"),
        ("Alice", "alice@example.com", "Alice Johnson", "alice.johnson@example.com"),
    ],
)
def test_update_user_with_parameters(real_service, name, email, new_name, new_email):
    """
    Параметризованный тест (лаб. 5): одна и та же цепочка
    create -> update name -> update email для разных наборов данных.
    """
    user = real_service.create_user(name, email)
    real_service.update_user_name(user.user_id, new_name)
    real_service.update_user_email(user.user_id, new_email)
    updated_user = real_service.get_user(user.user_id)
    assert updated_user.name == new_name
    assert updated_user.email == new_email
