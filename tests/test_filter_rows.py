from pytest import raises

from main import filter_rows
from settings.exception import ConfigurationError, DataValidationError

QUANTITY_MESSAGE = 'Неверное количество отфильтрованных строк'


def test_filter_rows_greater_than(sample_rows):
    """Тестирование фильтрации с оператором '>'."""
    assert len(filter_rows(sample_rows, 'age>5')) == 2, QUANTITY_MESSAGE


def test_filter_rows_less_than(sample_rows):
    """Тестирование фильтрации с оператором '<'."""
    assert len(filter_rows(sample_rows, 'age<10')) == 2, QUANTITY_MESSAGE


def test_filter_rows_equal(sample_rows):
    """Тестирование фильтрации с оператором '='."""
    assert len(filter_rows(sample_rows, 'age=10')) == 1, QUANTITY_MESSAGE


def test_filter_rows_not_exist_field(sample_rows):
    """Тестирование фильтрации с несуществующим полем."""
    with raises(DataValidationError):
        filter_rows(sample_rows, 'invalid_field=10')


def test_filter_rows_invalid_condition(sample_rows):
    """Тестирование фильтрации с некорректным условием."""
    with raises(ConfigurationError):
        filter_rows(sample_rows, 'age*10')


def test_filter_rows_type_mismatch(sample_rows):
    """Тестирование фильтрации с несовпадением типов данных."""
    with raises(DataValidationError):
        filter_rows(sample_rows, 'name=10')


def test_filter_rows_empty_result(sample_rows):
    """Тестирование фильтрации с пустым результатом."""
    with raises(DataValidationError):
        filter_rows(sample_rows, 'age>100')
