from django.db import models

# Create your models here.

class ContactForm(models.Model):
    full_name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=200)
    feedback_message = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
