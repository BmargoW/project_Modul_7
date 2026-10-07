from django.contrib import admin
from .models import Course, Lesson


@admin.register(Course)
class DistributionAdmin(admin.ModelAdmin):
    list_display = ("title", "owner",)

@admin.register(Lesson)
class DistributionAdmin(admin.ModelAdmin):
    list_display = ("name", "course", "owner",)