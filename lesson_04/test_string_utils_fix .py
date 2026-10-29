import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# ===== ТЕСТЫ ДЛЯ МЕТОДА CAPITALIZE ======


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
def test_capitalize_none():
    # Проверяем, что передача NONE вызывает ошибку (если метод не обрабатывает None внутри себя)
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)


@pytest.mark.positive
def test_capitalize_preserve_internal_caps():
    # Тест упадет, так как метод вернет "Skypro" вместо ожидаемого "SkyPro"
    assert string_utils.capitalize("SkyPro") == "SkyPro"


# ===== ТЕСТЫ ДЛЯ МЕТОДА DELETE_SYMBOL =====


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("skypro", "k", "sypro"),
    ("hello world", "l", "heo word"),  # удаляет все вхождения 'l'
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    # Случай, когда символа НЕТУ в строке (строка должна остаться прежней)
    ("skypro", "x", "skypro"),
    # Проверки с пустой строкой и пробелом ВОТ ТУТ
    ("", "a", ""),
    ("   ", " ", ""),
    ("skypro", "", "skypro"),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol", [
    (None, "a"),
    ("skypro", None),
])
def test_delete_symbol_none(input_str, symbol):
    # Проверяем падение на TypeError или AttributeError при передаче NONE
    with pytest.raises((TypeError, AttributeError)):
        string_utils.delete_symbol(input_str, symbol)


@pytest.mark.positive
def test_trim_multiple_spaces():
    # Передаем несколько пробелов ПОДРЯД перед текстом (или между словами)
    assert string_utils.trim("   skypro") == "skypro"

