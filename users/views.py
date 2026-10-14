from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Payments, CustomUser
from .serializers import PaymentsSerializer, MyTokenObtainPairSerializer, CustomUserSerializer
from rest_framework import generics, serializers

from rest_framework_simplejwt.views import TokenObtainPairView

from .services import create_stripe_price, create_stripe_session, create_stripe_product


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class PaymentsCreate(generics.CreateAPIView):
    serializer_class = PaymentsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Сначала получаем данные из валидированного сериализатора
        payment_data = serializer.validated_data
        course = payment_data.get("course")
        lesson = payment_data.get("lesson")
        amount = payment_data["payment_amount"]

        if not course and not lesson:
            raise serializers.ValidationError("Нужно указать course или lesson.")

        # Формируем понятное название продукта для Stripe
        if course:
            product_name = f"Курс: {course.title}"
        else:
            product_name = f"Урок: {lesson.title}"

        # 1. Создаём продукт в Stripe
        product = create_stripe_product(product_name)

        # 2. Создаём цену
        price = create_stripe_price(product.id, amount)

        # 3. Создаём сессию
        success_url = "http://127.0.0.1:8000/payment-success"
        cancel_url = "http://127.0.0.1:8000/payment-cancel"
        session_id, payment_link = create_stripe_session(price.id, success_url, cancel_url)

        # 4. Теперь сохраняем платёж, сразу с данными сессии
        payment = serializer.save(
            user=self.request.user,
            sessions_id=session_id,
            link=payment_link,
        )




class PaymentsList(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['course', 'lesson', 'payment_method']
    ordering_fields = ['payment_amount']
    permission_classes = [IsAuthenticated]


class UserRegistration(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

class UserList(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated, )

class UserRetrieve(generics.RetrieveAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

class UserUpdate(generics.UpdateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

class UserDestroy(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]
