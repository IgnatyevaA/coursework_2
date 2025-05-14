import json
from pathlib import Path
from src.api import HeadHunterAPI
from src.savers import JSONSaver

def test_get_vacancies_from_hh():
    api = HeadHunterAPI()
    vacancies = api.get_vacancies("Python", 5)
    assert len(vacancies) == 5
    assert hasattr(vacancies[0], "title")
    assert hasattr(vacancies[0], "company")

def test_save_vacancies_to_json(tmp_path: Path):
    test_file = tmp_path / "test_vacancies.json"
    api = HeadHunterAPI()
    vacancies = api.get_vacancies("Python", 2)
    saver = JSONSaver(str(test_file))
    saver.save_vacancies(vacancies)

    assert test_file.exists()

    with open(test_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert isinstance(data, list)
    assert len(data) == 2
    assert "title" in data[0]
    assert "company" in data[0]
