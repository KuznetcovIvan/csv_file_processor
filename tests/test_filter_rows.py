from pytest import mark, raises

from main import filter_rows
from settings.exception import ConfigurationError, DataValidationError

QUANTITY_MESSAGE = 'Неверное количество отфильтрованных строк'


@mark.parametrize(
    'condition, expected_count',
    [
        ('age>5', 2),
        ('age<10', 2),
        ('age=10', 1),
    ]
)
def test_filter_rows_valid(sample_rows, condition, expected_count):
    """Тестирование корректных условий фильтрации."""
    assert len(filter_rows(sample_rows, condition)) == expected_count, (
        QUANTITY_MESSAGE
    )


@mark.parametrize(
    'condition, expected_exception',
    [
        ('invalid_field=10', DataValidationError),
        ('age*10', ConfigurationError),
        ('name=10', DataValidationError),
        ('age>100', DataValidationError),
    ]
)
def test_filter_rows_invalid(sample_rows, condition, expected_exception):
    """Тестирование ошибочных условий фильтрации."""
    with raises(expected_exception):
        filter_rows(sample_rows, condition)
