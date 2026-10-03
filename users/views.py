

from .models import Payments
from .serializers import PaymentsSerializer
from rest_framework import generics



class PaymentsCreate(generics.CreateAPIView):
    serializer_class = PaymentsSerializer


class PaymentsList(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()