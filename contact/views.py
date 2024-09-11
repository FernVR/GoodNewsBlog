from django.shortcuts import render
from .models import ContactForm

# Create your views here.

def contact_form(request):
    """
    Renders contact page
    """

    contact = ContactForm.objects.all().order_by('-updated_on').first()
    
    return render(
        request,
        "contact/contact.html",
        {"contact": contact},
    )