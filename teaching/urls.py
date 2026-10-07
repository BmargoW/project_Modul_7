from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from teaching.views import CourseViewSet, LessonCreate, LessonList, LessonRetrieve, LessonUpdate, LessonDestroy
from rest_framework.routers import DefaultRouter

from users.views import MyTokenObtainPairView

# Описание маршрутизации для ViewSet

app_name = "teaching"


router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
urlpatterns = [ path("lesson/create/", LessonCreate.as_view(), name = "l-create"),
                path("lesson/list/", LessonList.as_view(), name = "l-list"),
                path("lesson/retrieve/<int:pk>/", LessonRetrieve.as_view(), name = "l-retrieve"),
                path("lesson/update/<int:pk>/", LessonUpdate.as_view(), name = "l-update"),
                path("lesson/delete/<int:pk>/", LessonDestroy.as_view(), name = "l-delete"),
                path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
                path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ] + router.urls