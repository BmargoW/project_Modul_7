from django.urls import path

from teaching.views import CourseViewSet, LessonCreate, LessonList, LessonRetrieve, LessonUpdate, LessonDestroy
from rest_framework.routers import DefaultRouter
# Описание маршрутизации для ViewSet

app_name = "teaching"


router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
urlpatterns = [ path("lesson/create/", LessonCreate.as_view(), name = "l-create"),
                path("lesson/list/", LessonList.as_view(), name = "l-list"),
                path("lesson/retrieve/<int:pk>/", LessonRetrieve.as_view(), name = "l-retrieve"),
                path("lesson/update/<int:pk>/", LessonUpdate.as_view(), name = "l-update"),
                path("lesson/delete/<int:pk>/", LessonDestroy.as_view(), name = "l-delete"),
    ] + router.urls