from django.contrib import admin
from django.utils.html import format_html
from .models import Profile, Skill, Project, Education

# Profile Admin
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email', 'phone')
    search_fields = ('name', 'role')
    readonly_fields = ('profile_image_preview',)
    fields = (
        'name', 'role', 'about', 'location', 'languages',
        'email', 'phone', 'linkedin', 'github',
        'profile_image_url', 'resume_url', 'profile_image_preview'
    )

    def profile_image_preview(self, obj):
        if obj.profile_image_url:
            return format_html('<img src="{}" width="100" />', obj.profile_image_url)
        return "-"
    profile_image_preview.short_description = "Profile Image Preview"

# Skill Admin
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    search_fields = ('name',)

# Project Admin
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_stack', 'github_link', 'live_link')
    search_fields = ('title', 'tech_stack')

# Education Admin
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'institution', 'status')
    search_fields = ('title', 'institution')
