from datetime import timedelta
from django.utils import timezone
from celery import shared_task

from users.models import CustomUser


@shared_task
def deactivate_users():

    one_month_ago = timezone.now() - timedelta(days=30)
    inactive_users = CustomUser.objects.filter(
        last_login__lt=one_month_ago,
        is_active=True,
    )

    count = inactive_users.count()
    if count == 0:
        return {"blocked": 0, "message": "Нет неактивных пользователей"}

    inactive_users.update(is_active=False)

    return {"blocked": count, "message": f"Заблокировано пользователей: {count}"}
