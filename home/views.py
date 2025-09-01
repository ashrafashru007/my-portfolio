from django.shortcuts import render
from .models import Project, Skill, Education, Profile

def home_view(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    education = Education.objects.all()

    # Split tech_stack into a list
    for project in projects:
        if project.tech_stack:
            project.tech_list = [tech.strip() for tech in project.tech_stack.split(',')]
        else:
            project.tech_list = []

    return render(request, "home/home.html", {
        "profile": profile,
        "projects": projects,
        "skills": skills,
        "education": education,
    })
