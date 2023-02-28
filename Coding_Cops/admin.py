from django.contrib import admin
from .models import *

class ProfilesAdmin(admin.ModelAdmin):
    list_filter = ("user", "agency")
    list_display = ("user", "agency", "private")


class CoursesAdmin(admin.ModelAdmin):
    list_filter = ("level", "cost", "title")
    list_display = ("title", "level", "cost", "link") 
    prepopulated_fields = {"slug": ("title",)}


class TechnologiesAdmin(admin.ModelAdmin):
    list_filter = ("title",)
    list_display = ("title", "link")
    prepopulated_fields = {"slug": ("title",)}


class ProjectsAdmin(admin.ModelAdmin):
     list_filter = ("title", "project_profile")
     list_display = ("title", "project_profile", "link") 
     prepopulated_fields = {"slug": ("title",)}


admin.site.register(Profiles, ProfilesAdmin)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(Technologies, TechnologiesAdmin)
admin.site.register(Tags)
#admin.site.register(Messages)
#admin.site.register(Projects, ProjectsAdmin)