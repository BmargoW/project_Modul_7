from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from teaching.models import Course, Lesson, Subscription
from teaching.pagination import MyPagination
from teaching.permissions import ModeratorPerm, OwnerPerm
from teaching.serializers import CourseSerializer, LessonSerializer
from rest_framework import viewsets, generics




class CourseViewSet(viewsets.ModelViewSet):
    """
    Простой ViewSet-класс для вывода списка пользователей и информации по одному объекту
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = MyPagination
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


    def get_permissions(self):
        if self.action == 'update':
            self.permission_classes = [OwnerPerm | ModeratorPerm]
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            self.permission_classes = [OwnerPerm | ModeratorPerm]
        elif self.action == 'destroy':
            self.permission_classes = [OwnerPerm]
        return [permission() for permission in self.permission_classes]

    # def create(self, request):
    #     serializer = CourseSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)
    #
    #
    # def list(self, request):
    #     # Метод для вывода списка пользователей с определением выборки из базы и указанием сериализатора
    #     queryset = Course.objects.all()
    #     serializer = CourseSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    #
    #
    # def retrieve(self, request, pk=None):
    #     # Метод для вывода информации по пользователю с определением выборки из базы и указанием сериализатора
    #     queryset = Course.objects.all()
    #     course = get_object_or_404(queryset, pk=pk)
    #     serializer = CourseSerializer(course)
    #     return Response(serializer.data)
    #
    # def update(self, request, pk=None):
    #     course = get_object_or_404(Course, pk=pk)
    #     serializer = CourseSerializer(course, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=400)
    #
    # def destroy(self, request, pk=None):
    #     course = get_object_or_404(Course, pk=pk)
    #     course.delete()
    #     return Response(status=204)


class LessonCreate(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonList(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes =  [IsAuthenticated]
    pagination_class = MyPagination


class LessonRetrieve(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [OwnerPerm|ModeratorPerm]

class LessonUpdate(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [OwnerPerm]

class LessonDestroy(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [OwnerPerm]


class CourseSubscriptionView(APIView):

    def post(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        user = request.user

        # Если уже подписан — можно вернуть 200 с сообщением или 409 Conflict
        if Subscription.objects.filter(user=user, course=course).exists():
            return Response(
                {'detail': 'Вы уже подписаны на этот курс'})

        Subscription.objects.create(user=user, course=course)
        return Response({'detail': 'Подписка оформлена'} )

    def delete(self, request, course_id):
        course = get_object_or_404(Course, pk=course_id)
        user = request.user
        subscription = Subscription.objects.filter(user=user, course=course).first()

        if not subscription:
            return Response({'detail': 'Вы не подписаны на этот курс'})

        subscription.delete()
        return Response({'detail': 'Отписка выполнена'})

# def contacts(request):
#     if request.method == "POST":
#         amount = request.POST.get("amount")
#         url =  # адрес. по которому мы берем сессию перевода
#         response = # ответ из сервиса
#         data = response.json()
#         a = # дале генерирует ссылку, возможно из data
#         b = # поулчаем ссылку id сессиий
#         element = MyModel(amount = amount, a =a, b =b)
#     return HttpResponse (f"Спасибо за внимание!")
