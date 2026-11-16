from django.urls import path

from users.views import PaymentsCreate, PaymentsList



app_name = "users"

urlpatterns = [ path("payments/create/", PaymentsCreate.as_view(), name = "p-create"),
                path("payments/list/", PaymentsList.as_view(), name = "p-list"),
                # path("lesson/retrieve/<int:pk>/", LessonRetrieve.as_view(), name = "l-retrieve"),
                # path("lesson/update/<int:pk>/", LessonUpdate.as_view(), name = "l-update"),
                # path("lesson/delete/<int:pk>/", LessonDestroy.as_view(), name = "l-delete"),
    ]