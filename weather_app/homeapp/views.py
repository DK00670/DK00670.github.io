from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'homeapp/index.html', context)