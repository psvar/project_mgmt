from django.shortcuts import render
from .models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all()
    # project_invoice = Project.invoice.all()
    context = {
        'projects': projects,
    }
    return render(request, 'index.html', context=context)
