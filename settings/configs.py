from argparse import ArgumentParser

DESCRIPTION = 'Обработчик CSV файлов'
FILE_HELP = 'Путь к CSV файлу'
WHERE_HELP = 'Условие фильтрации'
AGGREGATE_HELP = 'Параметры агрегации'

FILE_ARG = '--file'
FILTER_ARG = '--where'
AGGREGATE_ARG = '--aggregate'


def configure_argument_parser() -> ArgumentParser:
    parser = ArgumentParser(description=DESCRIPTION)
    parser.add_argument(FILE_ARG, help=FILE_HELP)
    parser.add_argument(FILTER_ARG, help=WHERE_HELP)
    parser.add_argument(AGGREGATE_ARG, help=AGGREGATE_HELP)
    return parser
