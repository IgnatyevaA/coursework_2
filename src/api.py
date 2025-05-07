import requests
from src.vacancy import Vacancy


def get_vacancies_from_hh(keyword: str, max_count: int = 10) -> list[Vacancy]:
    url = "https://api.hh.ru/vacancies"
    params = {"text": keyword, "per_page": max_count, "page": 0}
    response = requests.get(url, params=params)
    response.raise_for_status()

    vacancies_data = response.json().get("items", [])

    vacancies = []
    for item in vacancies_data:
        name = item.get("name")
        employer = item.get("employer", {}).get("name")
        salary = item.get("salary")
        salary_from = salary.get("from") if salary else None
        salary_to = salary.get("to") if salary else None
        currency = salary.get("currency") if salary else None
        url = item.get("alternate_url")

        vacancy = Vacancy(name, employer, salary_from, salary_to, currency, url)
        vacancies.append(vacancy)

    return vacancies
