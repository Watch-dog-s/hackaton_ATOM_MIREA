import re

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from Mainapp.models import Formula
from sympy import simplify, latex, symbols


# Представление для главной страницы
def home(request):
    if request.method == 'POST':
        if 'formula' in request.POST:  # Обработка добавления формулы
            clean_formula = request.POST.get('formula')
            if clean_formula:
                new_formula = Formula(clean_formula=clean_formula)
                new_formula.save()
                return redirect('home')
            else:
                return render(request, 'home.html', {'error': 'Формула не может быть пустой.'})

        elif 'compare_formula' in request.POST:  # Обработка сравнения формул
            compare_formula = request.POST.get('compare_formula')
            if compare_formula:
                # Получаем все формулы из базы данных
                all_formulas = Formula.objects.all()
                results = []

                # Сравниваем введённую формулу с формулами в БД
                for formula in all_formulas:
                    result = compare_formulas(compare_formula, formula.clean_formula)
                    results.append(f'Сравнение с формулой ID {formula.id}: {result * 100}% схожести')

                # Вывод результатов
                comparison_result = '<br>'.join(results)
                return render(request, 'home.html', {'comparison_result': comparison_result})

            else:
                return render(request, 'home.html', {'error': 'Формула для сравнения не может быть пустой.'})

    return render(request, 'home.html')


# Функция для сравнения двух формул
def compare_formulas(formula1, formula2):
    sr = sravnitel()  # Создаём экземпляр класса sravnitel
    return sr.findCopy(formula1, formula2)  # Используем метод для расчёта процента сходства


# Класс для обработки и сравнения формул
class sravnitel:
    # Определение символов для sympy
    q, w, e, r, t, y, u, i, o, p, a, s, d, f, g, h, j, k, l, z, x, c, v, b, n, m = symbols(
        'q w e r t y u i o p a s d f g h j k l z x c v b n m'
    )

    # Упрощение формул до базового вида
    def toBasic1(self, text):
        text = re.sub(r"(\d+)\/(\d+)", r"1", text)
        text = re.sub(r"([a-z])", r"a", text)
        text = re.sub(r"(\d+)", r"1", text)
        return text


    def findCopy(self, text1, text2):
        text1 = simplify(text1)
        text2 = simplify(text2)
        text1 = str(text1)
        text2 = str(text2)
        count = 0

        for char in text1:
            if char in text2:
                count += 1

        # Расчёт процента схожести
        if len(text1) >= len(text2):
            return round(count / len(text1), 2)
        else:
            return round(count / len(text2), 2)