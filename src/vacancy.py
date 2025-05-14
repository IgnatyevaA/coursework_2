class Vacancy:
    __slots__ = ("__title", "__company", "__salary_from", "__salary_to", "__currency", "__url")

    def __init__(self, title: str, company: str, salary_from: int | None, salary_to: int | None, currency: str | None, url: str):
        self.__title = title
        self.__company = company
        self.__salary_from = self.__validate_salary(salary_from)
        self.__salary_to = self.__validate_salary(salary_to)
        self.__currency = currency if currency else "Не указано"
        self.__url = url

    @staticmethod
    def __validate_salary(value):
        if isinstance(value, int) and value > 0:
            return value
        return 0

    def __lt__(self, other):
        return self.__salary_from < other.__salary_from

    def __gt__(self, other):
        return self.__salary_from > other.__salary_from

    def to_dict(self) -> dict:
        return {
            "title": self.__title,
            "company": self.__company,
            "salary_from": self.__salary_from,
            "salary_to": self.__salary_to,
            "currency": self.__currency,
            "url": self.__url
        }

    def __str__(self):
        return f"{self.__title} в компании {self.__company} — от {self.__salary_from} до {self.__salary_to} {self.__currency} \nСсылка: {self.__url}"

    # Методы доступа
    @property
    def title(self):
        return self.__title

    @property
    def company(self):
        return self.__company

    @property
    def salary_from(self):
        return self.__salary_from

    @property
    def salary_to(self):
        return self.__salary_to

    @property
    def currency(self):
        return self.__currency

    @property
    def url(self):
        return self.__url
