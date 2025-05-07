from src.vacancy import Vacancy

def test_vacancy_str():
    vac = Vacancy("Инженер", "Компания", 100000, 150000, "RUR", "https://hh.ru")
    assert "Инженер" in str(vac)
    assert "Компания" in str(vac)
    assert "100000" in str(vac)

def test_to_dict():
    vac = Vacancy("Тест", "Компания", 30000, 50000, "RUR", "http://example.com")
    d = vac.to_dict()
    assert d["title"] == "Тест"
    assert d["salary_to"] == 50000
