
from teaching.models import Subscription, Course
from django.core.mail import send_mail
from celery import shared_task

@shared_task
def notify_subscriber(course_id):
    course = Course.objects.get(pk=course_id)
    subscriptions = Subscription.objects.filter(course=course)
    emails = [sub.user.email for sub in subscriptions if sub.user.email]
    send_mail(
        subject="Новость по подписке: курс обновлён",
        message=f"Курс «{course.title}» был обновлён.\nПроверьте новые материалы.",
        from_email=None,
        recipient_list=emails,
    )


