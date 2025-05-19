class Vacancy:
    """
    Класс для работы с вакансиями.
    """
    __slots__ = ("__title", "__company", "__salary_from", "__salary_to", "__currency", "__url")

    def __init__(self, title: str, company: str, salary_from: int | None, salary_to: int | None, currency: str | None, url: str):
        """
        Инициализация вакансии.

        :param title: Название вакансии.
        :param company: Название компании.
        :param salary_from: Минимальная зарплата.
        :param salary_to: Максимальная зарплата.
        :param currency: Валюта.
        :param url: Ссылка на вакансию.
        """
        self.__title = title
        self.__company = company
        self.__salary_from = self.__validate_salary(salary_from)
        self.__salary_to = self.__validate_salary(salary_to)
        self.__currency = currency if currency else "Не указано"
        self.__url = url

    @staticmethod
    def __validate_salary(value):
        """
        Валидация зарплаты.

        :param value: Значение зарплаты.
        :return: Валидированное значение зарплаты.
        """
        if isinstance(value, int) and value > 0:
            return value
        return 0

    def __lt__(self, other):
        """
        Сравнение вакансий по минимальной зарплате.

        :param other: Другая вакансия.
        :return: Результат сравнения.
        """
        return self.__salary_from < other.__salary_from

    def __gt__(self, other):
        """
        Сравнение вакансий по минимальной зарплате.

        :param other: Другая вакансия.
        :return: Результат сравнения.
        """
        return self.__salary_from > other.__salary_from

    def to_dict(self) -> dict:
        """
        Преобразование вакансии в словарь.

        :return: Словарь с данными вакансии.
        """
        return {
            "title": self.__title,
            "company": self.__company,
            "salary_from": self.__salary_from,
            "salary_to": self.__salary_to,
            "currency": self.__currency,
            "url": self.__url
        }

    def __str__(self):
        """
        Преобразование вакансии в строку.

        :return: Строка с данными вакансии.
        """
        return f"Вакансия: {self.__title}\nКомпания: {self.__company}\nЗарплата: от {self.__salary_from} до {self.__salary_to} {self.__currency}\nСсылка: {self.__url}"

    # Методы доступа
    @property
    def title(self):
        """
        Получение названия вакансии.

        :return: Название вакансии.
        """
        return self.__title

    @property
    def company(self):
        """
        Получение названия компании.

        :return: Название компании.
        """
        return self.__company

    @property
    def salary_from(self):
        """
        Получение минимальной зарплаты.

        :return: Минимальная зарплата.
        """
        return self.__salary_from

    @property
    def salary_to(self):
        """
        Получение максимальной зарплаты.

        :return: Максимальная зарплата.
        """
        return self.__salary_to

    @property
    def currency(self):
        """
        Получение валюты.

        :return: Валюта.
        """
        return self.__currency

    @property
    def url(self):
        """
        Получение ссылки на вакансию.

        :return: Ссылка на вакансию.
        """
        return self.__url
