from django.shortcuts import render
from .models import Project
from django.views import generic

# Create your views here.
def index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'index.html', context=context)

def UserProjects(request):
    projects = Project.objects.all().filter(user=request.user)
    context = {
        'projects': projects,
    }
    return render(request, 'user_projects.html', context=context)


class ProjectDetaillView(generic.DetailView):
    model = Project
    template_name = 'project_detail.html'

