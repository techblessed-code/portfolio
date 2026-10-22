from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import Message


def about(request):
    return render(request, "core/about.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            Message.objects.create(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                subject=form.cleaned_data.get("subject", ""),
                body=form.cleaned_data["body"],
            )
            messages.success(request, "Thanks! Your message has been sent.")
            return redirect("contact")
        # invalid -> fall through, re-render the BOUND form with its errors
    else:
        form = ContactForm()
    return render(request, "core/contact.html", {"form": form})
