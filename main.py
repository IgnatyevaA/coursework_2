from src.api import HeadHunterAPI
from src.savers import JSONSaver
from src.utils import filter_vacancies_by_keyword, filter_vacancies_by_salary, sort_vacancies_by_salary

def main():
    api = HeadHunterAPI()
    saver = JSONSaver()

    query = input("🔎 Введите ключевое слово для поиска вакансий: ")
    per_page = int(input("📄 Сколько вакансий загрузить? (например, 10): "))
    min_salary = int(input("💰 Минимальная зарплата для фильтрации: "))
    top_n = int(input("🏆 Сколько топ-вакансий показать?: "))

    vacancies = api.get_vacancies(query, per_page)
    saver.save_vacancies(vacancies)

    filtered = filter_vacancies_by_salary(vacancies, min_salary)
    sorted_vacancies = sort_vacancies_by_salary(filtered)

    for vacancy in sorted_vacancies[:top_n]:
        print(vacancy)

if __name__ == "__main__":
    main()
