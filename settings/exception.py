class CSVProcessingError(Exception):
    """
    Базовое исключение для всех ошибок обработки CSV файла.
    """


class DataValidationError(CSVProcessingError):
    """
    Исключение для ошибок валидации данных.
    """


class ConfigurationError(CSVProcessingError):
    """
    Исключение для ошибок конфигурации.
    """
