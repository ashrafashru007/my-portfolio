from django.shortcuts import render, redirect
from .models import Profile, Project, Skill, Education
import cloudinary.uploader

# Home page view
def home_view(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    education = Education.objects.all()
    
    context = {
        "profile": profile,
        "projects": projects,
        "skills": skills,
        "education": education,
    }
    return render(request, "home/home.html", context)


# Upload or update profile
def upload_profile(request):
    """
    Handle profile upload/update with Cloudinary integration.
    """
    if request.method == "POST":
        # Get form data
        name = request.POST.get("name")
        role = request.POST.get("role", "Full Stack Developer")
        about = request.POST.get("about", "")
        location = request.POST.get("location", "")
        languages = request.POST.get("languages", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        linkedin = request.POST.get("linkedin", "")
        github = request.POST.get("github", "")

        # Get uploaded files
        image = request.FILES.get("profile_image")
        resume = request.FILES.get("resume")

        # Create or get existing profile
        profile, created = Profile.objects.get_or_create(
            name=name,
            defaults={"role": role, "about": about}
        )

        # Update profile fields
        profile.role = role
        profile.about = about
        profile.location = location
        profile.languages = languages
        profile.email = email
        profile.phone = phone
        profile.linkedin = linkedin
        profile.github = github

        # Upload profile image to Cloudinary
        if image:
            upload_result = cloudinary.uploader.upload(image, folder="portfolio/images")
            profile.profile_image_url = upload_result.get("secure_url")

        # Upload resume to Cloudinary
        if resume:
            upload_result = cloudinary.uploader.upload(
                resume, resource_type="raw", folder="portfolio/resumes"
            )
            profile.resume_url = upload_result.get("secure_url")

        profile.save()
        return redirect("home")  # Ensure "home" is defined in urls.py

    # GET request: display upload form
    return render(request, "home/upload.html")
