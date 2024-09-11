from django.contrib import admin
from .models import ContactForm
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(ContactForm)
class ContactAdmin(SummernoteModelAdmin):

    summernote_fields = ('feedback_message',)

