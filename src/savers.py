import json
from src.vacancy import Vacancy


class JSONSaver:
    def __init__(self, path: str):
        self.path = path

    def save(self, vacancies: list[Vacancy]):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump([vac.to_dict() for vac in vacancies], f, ensure_ascii=False, indent=4)
