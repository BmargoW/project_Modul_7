from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import Group




class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    objects = CustomUserManager()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    avatar = models.ImageField(upload_to="photos", blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    username= models.CharField(max_length=20, blank=True, null=True, unique=True)
    groups = models.ManyToManyField(Group)

    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def has_module_perms(self, app_label):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]



    def __str__(self):
        return self.email

from teaching.models import Course, Lesson
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



