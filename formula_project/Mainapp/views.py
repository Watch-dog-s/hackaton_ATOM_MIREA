from django.http import HttpResponse
from django.shortcuts import render





# Create your views here.




from django.shortcuts import render
from django.template.loader import render_to_string


def home(request):
    t=render_to_string('home.html')
    return HttpResponse(t)