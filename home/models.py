from django.db import models

# ===============================
# Profile model for personal info
# ===============================
class Profile(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default="Full Stack Developer")
    about = models.TextField(blank=True)
    
    # Local file storage (optional)
    profile_image = models.ImageField(upload_to="profile/", blank=True, null=True)
    resume = models.FileField(upload_to="resume/", blank=True, null=True)
    
    # Cloudinary URLs (optional)
    profile_image_url = models.URLField(blank=True, null=True)
    resume_url = models.URLField(blank=True, null=True)
    
    # Additional info
    location = models.CharField(max_length=200, blank=True, null=True)
    languages = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

# ===============================
# Skill model for frontend/backend
# ===============================
class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True, null=True)  # FontAwesome class

    def __str__(self):
        return self.name

# ===============================
# Project model for portfolio projects
# ===============================
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    tech_stack = models.CharField(max_length=200, blank=True, null=True)  # e.g., "Django, MySQL"

    def __str__(self):
        return self.title

# ===============================
# Education model
# ===============================
class Education(models.Model):
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    details = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)  # e.g., "Completed", "Ongoing"

    def __str__(self):
        return f"{self.title} - {self.institution}"
