from django.db import models

from users.models import CustomUser


class Course(models.Model):
    title= models.CharField(max_length=150, verbose_name="Название курса")
    preview = models.ImageField(
        upload_to="pictures/", verbose_name="Картинка", blank=True
    )
    description = models.CharField(max_length=150, verbose_name="Описание")
    owner = models.ForeignKey(
        CustomUser,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="owners",
        verbose_name="Пользователь",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["title"]


class Lesson(models.Model):

    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.CharField(max_length=150, verbose_name="Описание")
    picture = models.ImageField(
        upload_to="pictures/", verbose_name="Изображение", blank=True
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
    )
    video_url = models.URLField(max_length=2000, blank=True, null=True)
    owner = models.ForeignKey(
        CustomUser,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ["name"]


