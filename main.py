import csv

from tabulate import tabulate

from settings.configs import (AGGREGATE_ARG, FILE_ARG, FILTER_ARG,
                              configure_argument_parser)
from settings.constants import (AGGREGATE_OPERATORS, AGGREGATE_OPERATORS_MAP,
                                CONDITION_SPLITTER, ENCODING_TYPE,
                                FILTER_OPERATORS, FILTER_OPERATORS_MAP,
                                TABLE_FORMAT)
from settings.exception import (ConfigurationError, CSVProcessingError,
                                DataValidationError)

LOAD_ERROR = 'Файл {path} не найден'
FIELDNAMES_ERROR = 'Отсутствуют заголовки в файле {path}'
CONDITION_ERROR = 'Некоректные условия: {condition}'
FIELD_ERROR = 'В таблице отсутствует поле {field}'
EMPTY_ERROR = 'В файле отсутствуют запрашиваемые данные'
TYPE_ERROR = 'Не соответствие типов данных поля {name}'
OPERATOR_ERROR = 'Недопустимый оператор агрегации: {operator}'
TEXT_FIELD_ERROR = 'Невозможно агрегировать текстовое поле {field}'


def load_csv(path: str) -> list[dict[str, str]]:
    try:
        with open(path, encoding=ENCODING_TYPE) as file:
            reader = csv.DictReader(file)
            if not reader.fieldnames:
                raise DataValidationError(FIELDNAMES_ERROR.format(path=path))
            rows = list(reader)
            if not rows:
                raise DataValidationError(EMPTY_ERROR)
            return rows
    except FileNotFoundError:
        raise ConfigurationError(LOAD_ERROR.format(path=path))


def filter_rows(
    rows: list[dict[str, str]], condition: str
) -> list[dict[str, str]]:
    for operator in FILTER_OPERATORS:
        if operator in condition:
            filtered_name, filtered_value = condition.split(operator)
            try:
                filtered_value = float(filtered_value)
            except ValueError:
                pass
            break
    else:
        raise ConfigurationError(CONDITION_ERROR.format(
            condition=f'{FILTER_ARG} {condition}'
        ))
    filtered = []
    for row in rows:
        row_value = row.get(filtered_name)
        if row_value is None:
            raise DataValidationError(FIELD_ERROR.format(field=filtered_name))
        if type(filtered_value) is float:
            try:
                row_value = float(row_value)
            except ValueError:
                raise DataValidationError(
                    TYPE_ERROR.format(name=filtered_name)
                )
        if FILTER_OPERATORS_MAP[operator](row_value, filtered_value):
            filtered.append(row)
    if not filtered:
        raise DataValidationError(EMPTY_ERROR)
    return filtered


def aggregate_rows(
    rows: list[dict[str, str]], condition: str
) -> list[dict[str, float]]:
    condition = condition.split(CONDITION_SPLITTER)
    try:
        aggregate_name, operator = condition
    except ValueError:
        raise ConfigurationError(CONDITION_ERROR.format(
            condition=f'{AGGREGATE_ARG} {"".join(condition)}'
        ))
    if operator not in AGGREGATE_OPERATORS:
        raise ConfigurationError(OPERATOR_ERROR.format(operator=operator))
    if aggregate_name not in rows[0].keys():
        raise DataValidationError(FIELD_ERROR.format(field=aggregate_name))
    try:
        values = [float(row[aggregate_name]) for row in rows]
    except ValueError:
        raise DataValidationError(
            TEXT_FIELD_ERROR.format(field=aggregate_name)
        )
    return [{operator: AGGREGATE_OPERATORS_MAP[operator](values)}]


def main() -> None:
    try:
        args = configure_argument_parser().parse_args()
        if args.file is None:
            raise DataValidationError(
                CONDITION_ERROR.format(condition=FILE_ARG)
            )
        where = args.where
        aggregate = args.aggregate
        rows = load_csv(args.file)
        if where is not None:
            rows = filter_rows(rows, where)
        if aggregate is not None:
            rows = aggregate_rows(rows, aggregate)
        print(tabulate(rows, headers='keys', tablefmt=TABLE_FORMAT))
    except CSVProcessingError as error:
        print(error)


if __name__ == '__main__':
    main()
