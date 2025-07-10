from pytest import mark, raises

from main import aggregate_rows
from settings.exception import ConfigurationError, DataValidationError

RESULT_MESSAGE = 'Неверный результат агрегирования с оператором '


@mark.parametrize(
    'expression, expected_key, expected_value',
    [
        ('age=avg', 'avg', 7.3),
        ('age=min', 'min', 5),
        ('age=max', 'max', 10),
    ]
)
def test_aggregate_rows_valid(
    sample_rows, expression, expected_key, expected_value
):
    """Тестирование корректных агрегирующих операторов."""
    actual_value = aggregate_rows(sample_rows, expression)[0][expected_key]
    if isinstance(expected_value, float):
        actual_value = round(actual_value, 1)
    assert actual_value == expected_value, (
        RESULT_MESSAGE + expression.split('=')[1]
    )


@mark.parametrize(
    'expression, expected_exception',
    [
        ('age=invalid', ConfigurationError),
        ('invalid_field=avg', DataValidationError),
        ('name=avg', DataValidationError),
        ('age', ConfigurationError),
    ]
)
def test_aggregate_rows_invalid(sample_rows, expression, expected_exception):
    """Тестирование ошибочных случаев агрегирования."""
    with raises(expected_exception):
        aggregate_rows(sample_rows, expression)
