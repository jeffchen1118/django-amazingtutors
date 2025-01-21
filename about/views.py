from django.contrib import messages
from django.shortcuts import render

from .forms import CollaborateForm
from .models import About

# Create your views here.


def about_me(request):
    """
    Display the about page.

    **Context**

    ``about``
        An instance of :model:`about.About`.

    **Template:**

    :template:`about/about.html`
    """
    about = About.objects.all().order_by("-updated_on").first()

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
    collaborate_form = CollaborateForm()
    messages.add_message(
        request,
        messages.SUCCESS,
        "Collaboration request received! I endeavor to resond within 2 working days.",
    )

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form,
        },
    )
