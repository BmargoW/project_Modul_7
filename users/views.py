from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import Payments
from .serializers import PaymentsSerializer
from rest_framework import generics


class PaymentsCreate(generics.CreateAPIView):
    serializer_class = PaymentsSerializer


class PaymentsList(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['course', 'lesson', 'payment_method']
    ordering_fields = ['payment_amount']
