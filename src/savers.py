from abc import ABC, abstractmethod
import json
from src.vacancy import Vacancy

class VacancySaver(ABC):
    @abstractmethod
    def save_vacancies(self, vacancies: list[Vacancy]):
        """
        Сохранение вакансий в файл.

        :param vacancies: Список вакансий.
        """
        pass

    @abstractmethod
    def load_vacancies(self) -> list[Vacancy]:
        """
        Загрузка вакансий из файла.

        :return: Список вакансий.
        """
        pass

    @abstractmethod
    def delete_all(self):
        """
        Удаление всех вакансий из файла.
        """
        pass

class JSONSaver(VacancySaver):
    def __init__(self, filename: str = "vacancies.json"):
        """
        Инициализация сохранителя вакансий.

        :param filename: Имя файла.
        """
        self.__filename = filename

    def save_vacancies(self, vacancies: list[Vacancy]):
        """
        Сохранение вакансий в файл.

        :param vacancies: Список вакансий.
        """
        existing_vacancies = self.load_vacancies()
        existing_vacancies.extend([v.to_dict() for v in vacancies])
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(existing_vacancies, f, ensure_ascii=False, indent=4)

    def load_vacancies(self) -> list[Vacancy]:
        """
        Загрузка вакансий из файла.

        :return: Список вакансий.
        """
        try:
            with open(self.__filename, "r", encoding="utf-8") as f:
                raw = json.load(f)
                return [
                    Vacancy(
                        title=v["title"],
                        company=v["company"],
                        salary_from=v["salary_from"],
                        salary_to=v["salary_to"],
                        currency=v["currency"],
                        url=v["url"]
                    )
                    for v in raw
                ]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def delete_all(self):
        """
        Удаление всех вакансий из файла.
        """
        try:
            open(self.__filename, "w", encoding="utf-8").close()
        except Exception as e:
            print(f"Ошибка при удалении данных: {e}")
