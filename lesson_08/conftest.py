import os
import uuid

import pytest
import requests
from dotenv import load_dotenv

from project_api import ProjectApi

load_dotenv()

BASE_URL = "https://ru.yougile.com/api-v2"


def _auth_payload() -> dict:
    return {
        "login": os.environ["YOUGILE_LOGIN"],
        "password": os.environ["YOUGILE_PASSWORD"],
        "companyId": os.environ["YOUGILE_COMPANY_ID"],
    }


def _get_token() -> str:
    # 0) Готовый токен из .env — самый быстрый путь
    token = os.getenv("YOUGILE_TOKEN")
    if token:
        return token

    # 1) Пытаемся найти действующий ключ через /auth/keys/get
    resp = requests.post(
        f"{BASE_URL}/auth/keys/get",
        json=_auth_payload(),
        timeout=15,
    )
    if resp.ok:
        for item in resp.json():
            if not item.get("deleted", True) and item.get("key"):
                return item["key"]

    # 2) Действующего ключа нет — создаём новый через /auth/keys
    resp = requests.post(
        f"{BASE_URL}/auth/keys",
        json=_auth_payload(),
        timeout=15,
    )
    assert resp.status_code == 201, f"Не удалось получить API-ключ: {resp.text}"
    return resp.json()["key"]


@pytest.fixture(scope="session")
def api() -> ProjectApi:
    return ProjectApi(BASE_URL, token=_get_token())


@pytest.fixture()
def project_id(api) -> str:
    """Создаёт новый проект для теста и удаляет его после теста."""
    title = f"autotest_{uuid.uuid4().hex[:8]}"
    resp = api.create({"title": title})
    assert resp.status_code == 201, f"Не удалось создать проект: {resp.text}"
    new_id = resp.json()["id"]

    yield new_id

    api.update(new_id, {"deleted": True})


@pytest.fixture()
def nonexistent_id() -> str:
    """Случайный id, которого заведомо не существует."""
    return uuid.uuid4().hex * 4
