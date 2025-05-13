from functools import total_ordering


@total_ordering
class Vacancy:
    """Класс представления вакансии"""

    def __init__(self, title: str, url: str, salary: int | None, description: str):
        self.title = title
        self.url = url
        self.salary = self.__validate_salary(salary)
        self.description = description

    def __repr__(self):
        return f"{self.title} ({self.salary} ₽)\n{self.url}"

    def __validate_salary(self, salary):
        if salary is None:
            return 0
        if isinstance(salary, int) and salary >= 0:
            return salary
        raise ValueError("Зарплата должна быть положительным числом или None")

    def __lt__(self, other):
        return self.salary < other.salary

    def __eq__(self, other):
        return self.salary == other.salary
