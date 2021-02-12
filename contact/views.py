from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "sending mail via django"
            body = {
                'username': form.cleaned_data['username'],
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data['phone'],
                'address': form.cleaned_data['address'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, body.get('email'),
                          ['abc@gmail.com'])
                return HttpResponse("Thank u")
            except BadHeaderError:
                return HttpResponse("Invalid email found!!")
    return render(request, 'contact.html')
