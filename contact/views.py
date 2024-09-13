from django.shortcuts import render
from .models import ContactForm
from django.contrib import messages

# Create your views here.

def contact_form(request):
    """
    Renders contact page
    """
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Collaboration request received! I endeavour to respond within 2 working days."
                )

    contact = ContactForm.objects.all().order_by('-updated_on').first()
    
    return render(
        request,
        "contact/contact.html",
        {"contact": contact},
    )