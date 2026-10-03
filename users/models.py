from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from teaching.models import Course, Lesson


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    avatar = models.ImageField(upload_to="photos", blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


class Payments(models.Model):
    STATUS_CHOICES = [
        ("cash", "наличные"),
        ("remittance", "денежный перевод"),
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE,null=True, blank=True )
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True, blank=True)
    datetime_payments = models.DateTimeField(auto_now=False, verbose_name="дата платежа")
    payment_amount =  models.DecimalField(max_digits=10, decimal_places=2, verbose_name="сумма платежа")
    payment_method = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="cash",
        verbose_name="способ платежа",
    )

    def __str__(self):
        return f"{self.course if self.course else self.lesson} - {self.payment_amount}"


    class Meta:
        verbose_name = "Платежи"
        verbose_name_plural = "Платежи"
        ordering = ["-payment_amount"]



