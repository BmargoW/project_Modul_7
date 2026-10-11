from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import PaymentsCreate, PaymentsList, MyTokenObtainPairView, UserList, UserRegistration, UserRetrieve, \
    UserDestroy

app_name = "users"

urlpatterns = [ path("payments/create/", PaymentsCreate.as_view(), name = "p-create"),
                path("payments/list/", PaymentsList.as_view(), name = "p-list"),
                path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
                path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                path("user/list/", UserList.as_view(), name = "u-list"),
                path("user/register/", UserRegistration.as_view(), name = "u-register"),
                path("user/retrieve/<int:pk>/", UserRetrieve.as_view(), name = "u-retrieve"),
                path("user/destroy/<int:pk>/", UserDestroy.as_view(), name = "u-destroy"),
                # path("lesson/update/<int:pk>/", LessonUpdate.as_view(), name = "l-update"),
                # path("lesson/delete/<int:pk>/", LessonDestroy.as_view(), name = "l-delete"),
    ]