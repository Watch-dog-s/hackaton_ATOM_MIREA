from django.test import TestCase

# Create your tests here.



from django.test import TestCase
from .models import formula


class FormulaDatabaseTest(TestCase):

    def setUp(self):
        # Создание тестового объекта
        self.test_formula = formula.objects.create(
            clean_formula="x^2 + y^2 = z^2",
            short_description="Пифагор",
            meta_inf="Теорема"
        )

    def test_formula_creation(self):
        # Проверяем, что объект создан в БД
        formula1 = formula.objects.get(id_formula=self.test_formula.id_formula)
        self.assertEqual(formula.clean_formula, "x^2 + y^2 = z^2")
        self.assertEqual(formula.short_description, "Пифагор")
        self.assertEqual(formula.meta_inf, "Теорема")

    def test_database_count(self):
        # Проверяем количество записей в таблице
        self.assertEqual(formula.objects.count(), 1)

    def test_update_formula(self):
        # Обновление записи
        self.test_formula.clean_formula = "x^2 - y^2 = z"
        self.test_formula.save()
        updated_formula = formula.objects.get(id_formula=self.test_formula.id_formula)
        self.assertEqual(updated_formula.clean_formula, "x^2 - y^2 = z")

    def test_delete_formula(self):
        # Удаление записи
        self.test_formula.delete()
        self.assertEqual(formula.objects.count(), 0)
