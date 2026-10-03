from rest_framework import serializers
from .models import Course, Lesson




class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):

    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self,  course):
        return course.lesson_set.count()


    class Meta:
        model = Course
        fields = ['title', 'preview', 'description', 'lesson_count']