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
    lessons = LessonSerializer(many=True)
    lesson_count = serializers.SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'preview', 'description', 'lessons', 'lesson_count', 'is_subscribed']

    def create(self, validated_data):
        lessons_data = validated_data.pop("lessons", [])
        course = Course.objects.create(**validated_data)

        for lesson_data in lessons_data:
            lesson_data.pop("course", None)
            Lesson.objects.create(course=course, **lesson_data)

        return course

    def get_lesson_count(self,  course):
        return course.lessons.count()

    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            return False
        return obj.subscribers.filter(user=request.user).exists()


