import json
import os
from main import get_vacancies_from_hh, save_vacancies_to_json


def test_get_vacancies_from_hh():
    vacancies = get_vacancies_from_hh("Python", 5)
    assert len(vacancies) == 5
    assert vacancies[0].title
    assert vacancies[0].company


def test_save_vacancies_to_json(tmp_path):
    test_file = tmp_path / "test_vacancies.json"
    vacancies = get_vacancies_from_hh("Python", 2)
    save_vacancies_to_json(vacancies, test_file)

    assert test_file.exists()

    with open(test_file, encoding="utf-8") as f:
        data = json.load(f)
        assert isinstance(data, list)
        assert "title" in data[0]
