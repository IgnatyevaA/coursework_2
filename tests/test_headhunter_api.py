from src.api import HeadHunterAPI

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

    api = HeadHunterAPI()
    vacancies = api.get_vacancies("Python", 1)

    assert len(vacancies) == 1
    v = vacancies[0]
    assert v.title == "Python Developer"
    assert v.company == "Test Company"
    assert v.salary_from == 100000
    assert v.salary_to == 150000
    assert v.currency == "RUR"
    assert v.url == "http://example.com"
