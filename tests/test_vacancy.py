from src.vacancy import Vacancy

def test_vacancy_str():
    vac = Vacancy("Инженер", "Компания", 100000, 150000, "RUR", "https://hh.ru")
    result = str(vac)
    assert "Инженер" in result
    assert "Компания" in result
    assert "100000" in result

def test_to_dict():
    vac = Vacancy("Тест", "Компания", 30000, 50000, "RUR", "http://example.com")
    d = vac.to_dict()
    assert d["title"] == "Тест"
    assert d["company"] == "Компания"
    assert d["salary_from"] == 30000
    assert d["salary_to"] == 50000
    assert d["currency"] == "RUR"
    assert d["url"] == "http://example.com"