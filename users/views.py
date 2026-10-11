from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Payments, CustomUser
from .serializers import PaymentsSerializer, MyTokenObtainPairSerializer, CustomUserSerializer
from rest_framework import generics


from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class PaymentsCreate(generics.CreateAPIView):
    serializer_class = PaymentsSerializer


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
