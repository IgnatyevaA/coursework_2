class Vacancy:
    def __init__(self, title: str, company: str, salary_from: int = None,
                 salary_to: int = None, currency: str = None, url: str = None):
        self.title = title
        self.company = company
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.url = url

    def __str__(self):
        return (f"{self.title} в компании {self.company}, "
                f"{self.salary_from or 'N/A'} - {self.salary_to or 'N/A'} {self.currency or ''}\n{self.url}")

    def to_dict(self):
        return {
            "title": self.title,
            "company": self.company,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "currency": self.currency,
            "url": self.url
        }

    @classmethod
    def from_hh(cls, data: dict):
        return cls(
            title=data.get("name"),
            company=data.get("employer", {}).get("name"),
            salary_from=(data.get("salary") or {}).get("from"),
            salary_to=(data.get("salary") or {}).get("to"),
            currency=(data.get("salary") or {}).get("currency"),
            url=data.get("alternate_url")
        )
