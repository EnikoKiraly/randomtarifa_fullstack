from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    form_contact = ContactForm()
    
    return render(request, 'contact/contact.html', {'form_contact':form_contact})

