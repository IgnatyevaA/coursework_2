import json
from pathlib import Path
from src.vacancy import Vacancy
from src.savers import JSONSaver

def test_json_saver(tmp_path: Path):
    # Создаем временный файл
    test_file = tmp_path / "vacancies.json"
    saver = JSONSaver(str(test_file))

    # Создаем объект вакансии
    vacancy = Vacancy("Разработчик", "Компания", 50000, 70000, "RUR", "http://url.com")

    # Сохраняем вакансию
    saver.save_vacancies([vacancy])

    # Проверяем содержимое файла
    with open(test_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0] == {
        "title": "Разработчик",
        "company": "Компания",
        "salary_from": 50000,
        "salary_to": 70000,
        "currency": "RUR",
        "url": "http://url.com"
    }
