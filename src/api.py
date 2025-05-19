from abc import ABC, abstractmethod
import requests
from src.vacancy import Vacancy

class JobAPI(ABC):
    """
    Абстрактный класс для работы с API сервиса с вакансиями.
    """
    @abstractmethod
    def connect(self):
        """
        Подключение к API.
        """
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, per_page: int = 20) -> list[Vacancy]:
        """
        Получение вакансий.

        :param keyword: Ключевое слово для поиска.
        :param per_page: Количество вакансий на странице.
        :return: Список вакансий.
        """
        pass

class HeadHunterAPI(JobAPI):
    """
    Класс для работы с API hh.ru.
    """
    __base_url = "https://api.hh.ru/vacancies"

    def connect(self):
        """
        Подключение к API hh.ru.
        """
        try:
            response = requests.get(self.__base_url)
            response.raise_for_status()
            return True
        except requests.RequestException as e:
            print(f"Ошибка при подключении к API HH: {e}")
            return False

    def get_vacancies(self, keyword: str, per_page: int = 20) -> list[Vacancy]:
        """
        Получение вакансий с hh.ru.

        :param keyword: Ключевое слово для поиска.
        :param per_page: Количество вакансий на странице.
        :return: Список вакансий.
        """
        if not self.connect():
            return []

        params = {
            "text": keyword,
            "per_page": per_page,
            "page": 0
        }
        try:
            response = requests.get(self.__base_url, params=params)
            response.raise_for_status()
            vacancies_json = response.json().get("items", [])
            return [self.__parse_vacancy(v) for v in vacancies_json]
        except requests.RequestException as e:
            print(f"Ошибка при подключении к API HH: {e}")
            return []

    @staticmethod
    def __parse_vacancy(data: dict) -> Vacancy:
        """
        Преобразование данных вакансии в объект Vacancy.

        :param data: Данные вакансии.
        :return: Объект Vacancy.
        """
        salary_data = data.get("salary")
        if salary_data is None:
            salary_data = {}
        return Vacancy(
            title=data.get("name", "Не указано"),
            company=data.get("employer", {}).get("name", "Не указано"),
            salary_from=salary_data.get("from"),
            salary_to=salary_data.get("to"),
            currency=salary_data.get("currency"),
            url=data.get("alternate_url")
        )
