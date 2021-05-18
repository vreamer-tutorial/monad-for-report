import enum
from time import sleep

from src.monad import Failure


class FoodTypesEnum(enum.Enum):
    carbs = 'Carbohydrates'
    protein = 'Protein'
    fruit_n_veggie = 'Fruit and Vegetables'

    def __str__(self):
        return self.value


class ReportService:
    def __init__(self, repo):
        self.repo = repo

    def get_report(self):
        report = self.get_diet_calories() | ReportService.calculate_total | ReportService.print_report
        return report.get() if not report.is_failed() else ReportService.print_error_report(report.get_errors())

    def get_diet_calories(self) -> Failure:
        calories = [v.get('calories') for v in self.repo.get_diet()]
        missing_types = [v.get('food_type') for v in self.repo.get_diet() if v.get('calories') is None]
        return Failure(calories, errors=missing_types)

    @staticmethod
    def calculate_total(calories):
        sleep(3)
        return sum(calories)

    @staticmethod
    def print_report(total):
        return f"Total Calories Consumed is {total}kcal"

    @staticmethod
    def print_error_report(errors):
        return f"Missing Food Types: {', '.join(errors)}"
