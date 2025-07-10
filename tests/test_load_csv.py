from pytest import mark, raises

from main import load_csv
from settings.exception import ConfigurationError, DataValidationError


def test_load_valid_csv_file(complete_csv_file, sample_rows):
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


@mark.parametrize('csv_file,expected_exception', [
    ('empty_body_csv_file', DataValidationError),
    ('empty_field_names_csv_file', DataValidationError),
    ('not_exist.csv', ConfigurationError)
])
def test_load_csv_error_cases(csv_file, expected_exception, request):
    """Тестирование ошибочных случаев загрузки CSV-файла."""
    if csv_file != 'not_exist.csv':
        csv_file = request.getfixturevalue(csv_file)
    with raises(expected_exception):
        load_csv(csv_file)
