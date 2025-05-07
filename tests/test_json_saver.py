import json
from src.vacancy import Vacancy
from src.savers import JSONSaver


def test_json_saver(tmp_path):
    # Подготовка данных
    vacancy = Vacancy("Разработчик", "Компания", 50000, 70000, "RUR", "http://url.com")
    test_file = tmp_path / "vacancies.json"
    saver = JSONSaver(str(test_file))

    # Сохраняем вакансию в файл
    saver.save([vacancy])

    # Проверяем, что файл существует и содержит корректные данные
    with open(test_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["title"] == "Разработчик"
    assert data[0]["company"] == "Компания"
    assert data[0]["salary_from"] == 50000
    assert data[0]["salary_to"] == 70000
    assert data[0]["currency"] == "RUR"
    assert data[0]["url"] == "http://url.com"
