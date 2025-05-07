from src.api import get_vacancies_from_hh

def test_get_vacancies_from_hh(monkeypatch):
    class MockResponse:
        def json(self):
            return {
                "items": [
                    {
                        "name": "Python Developer",
                        "employer": {"name": "Test Company"},
                        "salary": {"from": 100000, "to": 150000, "currency": "RUR"},
                        "alternate_url": "http://example.com"
                    }
                ]
            }

        def raise_for_status(self):
            pass

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    vacancies = get_vacancies_from_hh("Python", 1)

    assert len(vacancies) == 1
    assert vacancies[0].title == "Python Developer"
    assert vacancies[0].company == "Test Company"
    assert vacancies[0].salary_from == 100000
    assert vacancies[0].salary_to == 150000
    assert vacancies[0].currency == "RUR"
    assert vacancies[0].url == "http://example.com"
