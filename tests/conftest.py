import csv

from pytest import fixture


@fixture
def sample_rows():
    return [
        dict(name='Uncle', surname='Fyodor', age='10', experience='2'),
        dict(name='Matroskin', surname='Cat', age='5', experience='3'),
        dict(name='Sharik', surname='Dog', age='7', experience='4'),
    ]


@fixture
def complete_csv_file(tmp_path, sample_rows):
    path = tmp_path / 'complete.csv'
    with open(path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(
            file, fieldnames=['name', 'surname', 'age', 'experience'])
        writer.writeheader()
        writer.writerows(sample_rows)
    return path


@fixture
def empty_body_csv_file(tmp_path):
    path = tmp_path / 'empty_body.csv'
    with open(path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(
            file, fieldnames=['name', 'surname', 'age', 'experience'])
        writer.writeheader()
    return path


@fixture
def empty_field_names_csv_file(tmp_path, sample_rows):
    path = tmp_path / 'empty_field_names.csv'
    with open(path, 'w', encoding='utf-8', newline='') as file:
        file.write('\n')
        for row in sample_rows:
            file.write(','.join(row.values()) + '\n')
    return path
