from pytest import raises

from main import load_csv
from settings.exception import ConfigurationError, DataValidationError


def test_load_complete_csv_file(complete_csv_file, sample_rows):
    """Тестирование загрузки корректного CSV-файла."""
    rows = load_csv(complete_csv_file)
    assert len(rows) == len(sample_rows), (
        'Количество строк не совпадает с ожидаемым'
    )
    assert isinstance(rows, list), (
        'Возвращаемое значение не является списком'
    )
    assert all(isinstance(row, dict) for row in rows), (
        'В возвращаемом списке не все элементы являются словарями'
    )
    assert rows == sample_rows, (
        'Содержимое строк не совпадает'
    )


def test_load_csv_empty_body(empty_body_csv_file):
    """Тестирование загрузки CSV-файла без данных."""
    with raises(DataValidationError):
        load_csv(empty_body_csv_file)


def test_load_csv_no_fieldnames(empty_field_names_csv_file):
    """Тестирование загрузки CSV-файла без заголовков."""
    with raises(DataValidationError):
        load_csv(empty_field_names_csv_file)


def test_load_csv_file_not_found():
    """Тестирование загрузки несуществующего файла."""
    with raises(ConfigurationError):
        load_csv('not_exist.csv')
