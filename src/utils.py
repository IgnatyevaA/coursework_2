from src.vacancy import Vacancy

def filter_vacancies_by_keyword(vacancies: list[Vacancy], keyword: str) -> list[Vacancy]:
    """
    Фильтрует вакансии по ключевому слову.

    :param vacancies: Список вакансий.
    :param keyword: Ключевое слово для фильтрации.
    :return: Отфильтрованный список вакансий.
    """
    return [v for v in vacancies if keyword.lower() in str(v).lower()]

def filter_vacancies_by_salary(vacancies: list[Vacancy], min_salary: int) -> list[Vacancy]:
    """
    Фильтрует вакансии по минимальной зарплате.

    :param vacancies: Список вакансий.
    :param min_salary: Минимальная зарплата для фильтрации.
    :return: Отфильтрованный список вакансий.
    """
    return [v for v in vacancies if v.to_dict()["salary_from"] >= min_salary]

def sort_vacancies_by_salary(vacancies: list[Vacancy]) -> list[Vacancy]:
    """
    Сортирует вакансии по зарплате.

    :param vacancies: Список вакансий.
    :return: Отсортированный список вакансий.
    """
    return sorted(vacancies, reverse=True)
