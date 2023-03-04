from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Contacts

# Create your views here.
def index(request):
    contacts = Contacts.objects.all() # semelhante a consulta all em SQL
    return render(request, 'contacts/index.html', {
        'contacts': contacts
    })

def show_contact(request, contact_id):
   
    # contact = Contacts.objects.get(id = contact_id)
    contact = get_object_or_404(Contacts, id=contact_id)
    return render(request, 'contacts/show_contact.html', {
        'contact': contact
    })
