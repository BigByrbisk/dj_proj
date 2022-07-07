from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    a = 4 * 5
    return render(request, 'about.html', {'gr': a})


def home(request):
    return HttpResponse('This is my home')
