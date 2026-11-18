from sqlalchemy import text


def get_student_by_email(session, email):
    """Получить запись студента по email."""
    result = session.execute(
        text("SELECT id, name, email FROM students WHERE email = :email"),
        {"email": email},
    ).fetchone()
    return result


def test_create_student(session):
    """Тест на добавление студента: создаём и проверяем наличие в БД."""
    new_email = "pytest.student@example.com"

    session.execute(
        text(
            """
            INSERT INTO students (name, email)
            VALUES (:name, :email)
            """
        ),
        {"name": "Pytest Student", "email": new_email},
    )
    session.commit()

    student = get_student_by_email(session, new_email)
    assert student is not None
    assert student.name == "Pytest Student"
    assert student.email == new_email


def test_update_student(session):
    """Тест на обновление студента: меняем имя и email, проверяем изменения."""
    email = "pytest.student@example.com"
    updated_email = "pytest.student.updated@example.com"

    session.execute(
        text(
            """
            INSERT INTO students (name, email)
            VALUES (:name, :email)
            """
        ),
        {"name": "Pytest Student", "email": email},
    )
    session.commit()

    session.execute(
        text(
            """
            UPDATE students
            SET name = :new_name, email = :new_email
            WHERE email = :old_email
            """
        ),
        {
            "new_name": "Pytest Student Updated",
            "new_email": updated_email,
            "old_email": email,
        },
    )
    session.commit()

    updated = get_student_by_email(session, updated_email)
    assert updated is not None
    assert updated.name == "Pytest Student Updated"

    # Убеждаемся, что по старому email записи больше нет
    assert get_student_by_email(session, email) is None


def test_delete_student(session):
    """Тест на удаление студента: создаём, удаляем, убеждаемся в отсутствии записи."""
    email = "pytest.student@example.com"

    session.execute(
        text(
            """
            INSERT INTO students (name, email)
            VALUES (:name, :email)
            """
        ),
        {"name": "Pytest Student", "email": email},
    )
    session.commit()

    student = get_student_by_email(session, email)
    assert student is not None

    session.execute(
        text("DELETE FROM students WHERE email = :email"),
        {"email": email},
    )
    session.commit()

    assert get_student_by_email(session, email) is None
