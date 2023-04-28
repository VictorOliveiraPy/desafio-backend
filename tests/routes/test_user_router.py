from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

from src.domain.entities.person import PersonCreate
from src.main import app

client = TestClient(app)


@pytest.fixture
def mock_db(mocker):
    return mocker.MagicMock()


def test_create_user(mock_db, mocker):
    # Define o retorno do método create_user do mock do banco de dados
    created_user = PersonCreate(username="johndoe", password="password")
    mock_db.create_person.return_value = created_user

    # Passa o mock do banco de dados como argumento para a rota
    response = client.post("/users", json={"username": "johndoe", "password": "password"},)
    assert response.status_code == 201

    # Verifica se a função create_user do mock do banco de dados foi chamada com o objeto UserCreate correto
    mock_db.create_person.assert_called_once_with(created_user)
