import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


@pytest.fixture(scope="session")
def session():
    """Фикстура сессии на весь запуск тестов."""
    session_obj = Session()
    yield session_obj
    session_obj.close()


@pytest.fixture(autouse=True)
def cleanup_students(session):
    """Автоматическая очистка тестовых данных до и после каждого теста.

    Удаляет записи студентов с тестовыми email-адресами, чтобы тесты были
    стабильными и не зависели от предыдущего состояния БД.
    """
    test_emails = (
        "pytest.student@example.com",
        "pytest.student.updated@example.com",
    )

    for email in test_emails:
        session.execute(
            text("DELETE FROM students WHERE email = :email"),
            {"email": email},
        )
    session.commit()

    yield

    for email in test_emails:
        session.execute(
            text("DELETE FROM students WHERE email = :email"),
            {"email": email},
        )
    session.commit()
