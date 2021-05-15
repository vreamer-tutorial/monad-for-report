import enum
from time import sleep


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
        diet_calories = self.get_diet_calories()
        total_calories = ReportService.calculate_total(diet_calories)
        return ReportService.print_report(total_calories)

    def get_diet_calories(self):
        return [v.get('calories') for v in self.repo.get_diet()]

    @staticmethod
    def calculate_total(calories):
        sleep(3)
        return sum(calories)

    @staticmethod
    def print_report(total):
        return f"Total Calories Consumed is {total}kcal"
