import uuid


# === [POST] /api-v2/projects ===

def test_create_project_positive(api):
    """Позитивный тест: создание проекта с обязательным полем title."""
    title = f"project_{uuid.uuid4().hex[:8]}"
    resp = api.create({"title": title})

    assert resp.status_code == 201
    body = resp.json()
    assert "id" in body
    assert isinstance(body["id"], str)

    # Удаляем проект за собой для сохранения чистоты окружения
    api.update(body["id"], {"deleted": True})


def test_create_project_negative_empty_title(api):
    """Негативный тест: создание проекта без обязательного поля title."""
    resp = api.create({})
    assert resp.status_code == 400


def test_create_project_negative_unauthorized(api):
    """Негативный тест: создание проекта без токена авторизации."""
    resp = api.create({"title": "Unauthorized Project"}, with_auth=False)
    assert resp.status_code == 401


# === [PUT] /api-v2/projects/{id} ===

def test_update_project_positive(api, project_id):
    """Позитивный тест: обновление названия существующего проекта."""
    new_title = f"updated_{uuid.uuid4().hex[:8]}"
    resp = api.update(project_id, {"title": new_title})

    assert resp.status_code == 200
    assert resp.json().get("id") == project_id

    # Проверяем через GET, что изменения сохранились
    get_resp = api.get_by_id(project_id)
    assert get_resp.status_code == 200
    assert get_resp.json().get("title") == new_title


def test_update_project_negative_nonexistent_id(api, nonexistent_id):
    """Негативный тест: попытка изменить несуществующий проект."""
    resp = api.update(nonexistent_id, {"title": "New Title"})
    assert resp.status_code == 404


def test_update_project_negative_empty_title(api, project_id):
    """Негативный тест: передача пустой строки в название проекта."""
    resp = api.update(project_id, {"title": ""})
    assert resp.status_code == 400


# === [GET] /api-v2/projects/{id} ===

def test_get_project_positive(api, project_id):
    """Позитивный тест: получение информации по ID существующего проекта."""
    resp = api.get_by_id(project_id)

    assert resp.status_code == 200
    body = resp.json()
    assert body.get("id") == project_id
    assert "title" in body


def test_get_project_negative_nonexistent_id(api, nonexistent_id):
    """Негативный тест: запрос несуществующего ID проекта."""
    resp = api.get_by_id(nonexistent_id)
    assert resp.status_code == 404
