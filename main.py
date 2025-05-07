from src.api import get_vacancies_from_hh
from src.vacancy import Vacancy
from src.savers import JSONSaver


def filter_vacancies_by_salary(vacancies, min_salary):
    return [
        vacancy for vacancy in vacancies
        if vacancy.salary_from is not None and vacancy.salary_from >= min_salary
    ]


def sort_vacancies_by_salary(vacancies):
    return sorted(vacancies, key=lambda v: v.salary_from or 0, reverse=True)


def get_top_vacancies(vacancies, top_n):
    return vacancies[:top_n]


def save_vacancies_to_json(vacancies, path="vacancies.json"):
    saver = JSONSaver(path)
    saver.save(vacancies)


def main():
    keyword = input("🔎 Введите ключевое слово для поиска вакансий: ")
    num_vacancies = int(input("📄 Сколько вакансий загрузить? (например, 10): "))
    min_salary = int(input("💰 Минимальная зарплата для фильтрации: "))
    top_n = int(input("🏆 Сколько топ-вакансий показать?: "))

    print("📡 Загрузка вакансий...")
    vacancies = get_vacancies_from_hh(keyword, num_vacancies)

    print("📂 Сохранение вакансий в JSON...")
    save_vacancies_to_json(vacancies)

    filtered = filter_vacancies_by_salary(vacancies, min_salary)
    sorted_vacancies = sort_vacancies_by_salary(filtered)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    print(f"\n🎯 Топ-{top_n} вакансий:\n")
    for vacancy in top_vacancies:
        print(vacancy)
        print("-" * 40)


if __name__ == "__main__":
    main()
