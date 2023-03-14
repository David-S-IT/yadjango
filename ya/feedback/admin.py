from django.contrib import admin

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    fields = ('text', 'email', 'status')
    list_display = ('text', 'email', 'status', 'created_on')
