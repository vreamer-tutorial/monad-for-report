import unittest
from unittest.mock import Mock

from src.report_service import ReportService, FoodTypesEnum


class TestReport(unittest.TestCase):
    def test_get_report_when_data_are_all_present(self):
        mock_repo = Mock()
        mock_repo.get_diet.return_value = [
            {'food_type': FoodTypesEnum.carbs.value, 'calories': 300},
            {'food_type': FoodTypesEnum.protein.value, 'calories': 300},
            {'food_type': FoodTypesEnum.fruit_n_veggie.value, 'calories': 600},
        ]

        report = ReportService(mock_repo).get_report()

        self.assertEqual("Total Calories Consumed is 1200kcal", report)

    @unittest.skip
    def test_get_report_when_some_data_is_missing(self):
        mock_repo = Mock()
        mock_repo.get_diet.return_value = [
            {'food_type': FoodTypesEnum.carbs.value, 'calories': 300},
            {'food_type': FoodTypesEnum.protein.value, 'calories': None},
            {'food_type': FoodTypesEnum.fruit_n_veggie.value, 'calories': None},
        ]

        report = ReportService(mock_repo).get_report()

        self.assertEqual('Missing Food Types: Protein, Fruit and Vegetables', report)
