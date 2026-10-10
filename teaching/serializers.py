import re

from rest_framework import serializers
from .models import Course, Lesson
from .validators import link_validator

YOUTUBE_REGEX = re.compile(
    r"^https?://(?:www\.)?(?:youtube\.com|youtu\.?be)/",
    re.IGNORECASE
)

class LessonSerializer(serializers.ModelSerializer):
    video_url = serializers.URLField(validators=[link_validator])

    class Meta:
        model = Lesson
        fields = "__all__"




class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(source="lessons", many= True)
    lesson_count = serializers.SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()

    def get_lesson_count(self,  course):
        return course.lessons.count()

    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            return False
        return obj.subscribers.filter(user=request.user).exists()

    class Meta:
        model = Course
        fields = ['title', 'preview', 'description', 'lesson_count', 'lesson', 'is_subscribed' ]
