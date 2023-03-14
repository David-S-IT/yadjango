from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import FeedbackForm
from .models import Feedback


def feedback(request):
    template = 'feedback/feedback.html'
    form = FeedbackForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        text = form.cleaned_data[Feedback.text.field.name]
        email = form.cleaned_data[Feedback.email.field.name]

        send_mail(
            'Yadjango company',
            text,
            settings.ADMIN_EMAIL,
            [email],
            fail_silently=False,
        )

        Feedback.objects.create(**form.cleaned_data)

        messages.success(request, 'Отзыв отправлен')

        return redirect('feedback:feedback')

    context = {'form': form}
    return render(request, template, context)
