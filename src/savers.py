from abc import ABC, abstractmethod
import json
from typing import List
from src.vacancy import Vacancy


class AbstractSaver(ABC):
    """Абстрактный класс для сохранения вакансий"""

    @abstractmethod
    def save_vacancies(self, vacancies: List[Vacancy]) -> None:
        pass


class JSONSaver(AbstractSaver):
    """Сохраняет вакансии в JSON-файл"""

    def __init__(self, filename: str = "vacancies.json"):
        self.filename = filename

    def save_vacancies(self, vacancies: List[Vacancy]) -> None:
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([vac.__dict__ for vac in vacancies], f, ensure_ascii=False, indent=2)
