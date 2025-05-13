from abc import ABC, abstractmethod
from typing import List, Dict
import requests


class AbstractAPI(ABC):
    """Абстрактный класс API для получения вакансий"""

    @abstractmethod
    def get_vacancies(self, keyword: str) -> List[Dict]:
        pass


class HeadHunterAPI(AbstractAPI):
    """Класс для работы с HeadHunter API"""

    BASE_URL = "https://api.hh.ru/vacancies"

    def get_vacancies(self, keyword: str) -> List[Dict]:
        params = {
            "text": keyword,
            "per_page": 50
        }
        response = requests.get(self.BASE_URL, params=params)
        if response.status_code == 200:
            return response.json().get("items", [])
        print(f"Ошибка {response.status_code}: не удалось получить вакансии.")
        return []
