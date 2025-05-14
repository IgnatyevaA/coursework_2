from abc import ABC, abstractmethod
import json
from src.vacancy import Vacancy

class VacancySaver(ABC):
    @abstractmethod
    def save_vacancies(self, vacancies: list[Vacancy]):
        pass

    @abstractmethod
    def load_vacancies(self) -> list[Vacancy]:
        pass

    @abstractmethod
    def delete_all(self):
        pass

class JSONSaver(VacancySaver):
    def __init__(self, filename: str = "vacancies.json"):
        self.__filename = filename

    def save_vacancies(self, vacancies: list[Vacancy]):
        data = [v.to_dict() for v in vacancies]
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_vacancies(self) -> list[Vacancy]:
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
        except FileNotFoundError:
            return []

    def delete_all(self):
        try:
            open(self.__filename, "w", encoding="utf-8").close()
        except Exception as e:
            print(f"Ошибка при удалении данных: {e}")
