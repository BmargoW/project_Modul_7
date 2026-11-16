
from teaching.models import Course, Lesson
from teaching.serializers import CourseSerializer, LessonSerializer
from rest_framework import viewsets, generics


class CourseViewSet(viewsets.ModelViewSet):
    """
    Простой ViewSet-класс для вывода списка пользователей и информации по одному объекту
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonCreate(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonList(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieve(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonUpdate(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonDestroy(generics.DestroyAPIView):
    queryset = Lesson.objects.all()