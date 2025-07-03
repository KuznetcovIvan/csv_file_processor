from pytest import raises

from main import aggregate_rows
from settings.exception import ConfigurationError, DataValidationError

RESULT_MESSAGE = 'Неверный результат агрегирования с оператором '


def test_aggregate_rows_avg(sample_rows):
    """Тестирование агрегации с оператором 'avg'."""
    assert round(aggregate_rows(
        sample_rows, 'age=avg'
    )[0]['avg'], 1) == 7.3, RESULT_MESSAGE + 'avg'


def test_aggregate_rows_min(sample_rows):
    """Тестирование агрегации с оператором 'min'."""
    assert aggregate_rows(
        sample_rows, 'age=min'
    )[0]['min'] == 5, RESULT_MESSAGE + 'min'


def test_aggregate_rows_max(sample_rows):
    """Тестирование агрегации с оператором 'max'."""
    assert aggregate_rows(
        sample_rows, 'age=max'
    )[0]['max'] == 10, RESULT_MESSAGE + 'max'


def test_aggregate_rows_invalid_operator(sample_rows):
    """Тестирование агрегации с некорректным оператором."""
    with raises(ConfigurationError):
        aggregate_rows(sample_rows, 'age=invalid')


def test_aggregate_rows_invalid_field(sample_rows):
    """Тестирование агрегации с несуществующим полем."""
    with raises(DataValidationError):
        aggregate_rows(sample_rows, 'invalid_field=avg')


def test_aggregate_rows_text_field(sample_rows):
    """Тестирование агрегации по текстовому полю."""
    with raises(DataValidationError,):
        aggregate_rows(sample_rows, 'name=avg')


def test_aggregate_rows_invalid_condition_format(sample_rows):
    """Тестирование агрегации с некорректным форматом условия."""
    with raises(ConfigurationError):
        aggregate_rows(sample_rows, 'age')
