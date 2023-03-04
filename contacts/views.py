from django.shortcuts import render
from .models import Contacts

# Create your views here.
def index(request):
    contacts = Contacts.objects.all() # semelhante a consulta all em SQL
    return render(request, 'contacts/index.html', {
        'contacts': contacts
    })