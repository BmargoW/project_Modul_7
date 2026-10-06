from rest_framework import serializers
from .models import Course, Lesson




class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(source="lessons", many= True)
    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self,  course):
        return course.lessons.count()

    class Meta:
        model = Course
        fields = ['title', 'preview', 'description', 'lesson_count', 'lesson']
