from src.api import HeadHunterAPI
from src.vacancy import Vacancy
from src.savers import JSONSaver


def format_vacancies(raw_vacancies: list) -> list[Vacancy]:
    """Преобразует данные из HH в объекты Vacancy"""
    vacancies = []
    for item in raw_vacancies:
        title = item.get("name")
        url = item.get("alternate_url")
        description = item.get("snippet", {}).get("requirement", "")
        salary_data = item.get("salary")
        salary = salary_data.get("from") if salary_data else 0
        vacancies.append(Vacancy(title, url, salary, description))
    return vacancies


def main():
    keyword = input("Введите ключевое слово для поиска вакансий: ")
    hh = HeadHunterAPI()
    raw_data = hh.get_vacancies(keyword)
    vacancies = format_vacancies(raw_data)

    # Сортировка и вывод
    sorted_vacancies = sorted(vacancies, reverse=True)
    for vac in sorted_vacancies[:10]:
        print(vac)

    # Сохранение
    saver = JSONSaver()
    saver.save_vacancies(sorted_vacancies[:10])
    print("Топ-10 вакансий сохранены в файл.")


if __name__ == "__main__":
    main()
