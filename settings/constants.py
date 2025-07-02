ENCODING_TYPE = 'utf-8'
TABLE_FORMAT = 'psql'

FILTER_OPERATORS_MAP = {
    '<': lambda x, y: x < y,
    '>': lambda x, y: x > y,
    '=': lambda x, y: x == y
}
FILTER_OPERATORS = FILTER_OPERATORS_MAP.keys()

AGGREGATE_OPERATORS_MAP = {
    'avg': lambda values: sum(values) / len(values),
    'min': lambda values: min(values),
    'max': lambda values: max(values)
}
AGGREGATE_OPERATORS = AGGREGATE_OPERATORS_MAP.keys()
CONDITION_SPLITTER = '='
