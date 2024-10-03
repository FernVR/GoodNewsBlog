from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.

def about_me(request):
    """
    Renders the About page
    """
    # Fetch the most recent About entry
    about = About.objects.all().order_by('-updated_on').first()
    
    # Initialize the form
    collaborate_form = CollaborateForm()

    if request.method == "POST":
        # Populate the form with POST data
        collaborate_form = CollaborateForm(data=request.POST)
        
        # Check if the form is valid
        if collaborate_form.is_valid():
            # Save the valid form data
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS, 
                "Collaboration request received! I endeavour to respond within 2 working days."
            )
            return redirect(reverse('about'))  # Redirect after successful submission
        else:
            # Optionally, you can add an error message here
            messages.error(request, "Please correct the errors below.")  

    return render(
        request,
        "about/about.html",
        {"about": about, "collaborate_form": collaborate_form},
    )