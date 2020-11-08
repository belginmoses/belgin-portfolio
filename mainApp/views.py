from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import About, Project, Skill,Job

# Create your views here.

def home(request):
    return render(request,'home.html',{'jobs': Job.objects.all()})
    #return HttpResponse('Hello World!')

def reachme(request):
    return render(request,'ReachMe.html')

def resume(request):
    return render(request,'resume.html')

def about(request):
    about = About.objects
    return render(request, 'About.html', {'about': about.all()[0], 'projects': Project.objects.all().order_by('id'), 'skills': Skill.objects.all()})

def projectdetails(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    project_points = project.description.split(". ")

    return render(request, 'ProjectDetail.html', {'project': project, 'project_points': project_points})