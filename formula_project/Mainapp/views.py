from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.template.loader import render_to_string
from Mainapp.models import Formula


def home(request):
    if request.method == 'POST':
        clean_formula = request.POST.get('formula')
        short_description = request.POST.get('description', '')
        meta_inf = request.POST.get('meta', '')

        # Сохранение формулы в базе данных
        if clean_formula:
            new_formula = Formula(
                clean_formula=clean_formula,
                short_description=short_description,
                meta_inf=meta_inf
            )
            new_formula.save()
            return redirect('home')
        else:
            # Обработка случая, когда формула не была введена
            return render(request, 'home.html', {'error': 'Формула не может быть пустой.'})

    return render(request, 'home.html')