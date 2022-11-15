from django.shortcuts import render
from .models import Project


def portfolio(request):
    projects = Project.objects.all()
    # ahora pasamos los proyectos encontrados a la vista
    # mediante un diccionario de contexto
    return render(request, "portfolio/portfolio.html", {'projects': projects})
