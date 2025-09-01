from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default="Full Stack Developer")
    about = models.TextField()
    profile_image = models.ImageField(upload_to="profile/")
    resume = models.FileField(upload_to="resume/")
    location = models.CharField(max_length=200, blank=True, null=True)
    languages = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True, null=True)  # FontAwesome class (fab fa-python, etc.)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    tech_stack = models.CharField(max_length=200, blank=True, null=True)  # e.g. "Django, MySQL"

    def __str__(self):
        return self.title

class Education(models.Model):
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    details = models.TextField(blank=True)
    status = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title
