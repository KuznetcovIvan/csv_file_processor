# Обработчик csv файлов
Это скрипт для обработки CSV-файлов и вывода результата в консоль, поддерживающий операции: 
- фильтрацию по колонкам с текстовыми и числовыми значениями с операторами больше (>), меньше (<) и равно (=)
- агрегацию по числовым колонкам с расчетом среднего (avg), минимального (min) и максимального (max) значения

---
## Установка и запуск:
- Клонируйте [репозиторий](https://github.com/KuznetcovIvan/csv_file_processor): `git clone https://github.com/KuznetcovIvan/csv_file_processor.git`
- Перейдите в директорию со скриптом `cd csv_file_processor`
- Создайте виртуальное окружение `python -m venv venv`, и активируйте его
   `venv\Scripts\activate` (для Linux/macOS: `source venv/bin/activate`)
- Установите зависимости:
   `pip install -r requirements.txt`

- Скрипт запускается через командную строку с аргументами:

    - `--file` <путь к csv файлу>
    - `--where` <параметры фильтрации>
    - `--aggregate` <параметры агрегации>

---

## Примеры запуска скрипта (на основе файла [products.csv](/products.csv)):
### `python main.py --file products.csv`

Отображает все строки CSV-файла в виде таблицы.

![](images/--file%20products.csv.PNG)

### `python main.py --file products.csv --where "rating>4.7"`

Выводит строки, где значение в столбце rating больше 4.7

![](images/--file%20products.csv%20--where%20rating_4.7.PNG)

### `python main.py --file products.csv --where "brand=apple"`

Выводит строки, где значение в столбце brand равно apple

![](images/--file%20products.csv%20--where%20brand_apple.PNG)

### `python main.py --file products.csv --aggregate "rating=avg"`

Вычисляет среднее значение столбца rating

![](images/--file%20products.csv%20--aggregate%20rating_avg.PNG)

### `python main.py --file products.csv --aggregate "rating=min"`

Вычисляет минимальное значение столбца rating

![](images/--file%20products.csv%20--aggregate%20rating_min.PNG)

---

## Скрипт покрыт тестами:
### `pytest --cov=main`
![](images/pytest%20--cov_main.PNG)

---

### Используемые библиотеки
- csv
- argparse
- tabulate
- pytest
- pytest-cov

---

#### Автор: [Иван Кузнецов](https://github.com/KuznetcovIvan)