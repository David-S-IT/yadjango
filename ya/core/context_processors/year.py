from django.utils import timezone


def year(request):
    """Добавляет переменную с текущим годом."""

    year_today = timezone.now().year

    return {'year': year_today}
