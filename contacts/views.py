from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404
from .models import Contacts

# Create your views here.
def index(request):
    # contacts = Contacts.objects.all() => semelhante a consulta all em SQL
    contacts = Contacts.objects.order_by('-id').filter(
        show = True
    ) # => Ordenação por ordem decrescente ID
    paginator = Paginator(contacts, 2)

    page = request.GET.get('p')
    contacts = paginator.get_page(page)

    return render(request, 'contacts/index.html', { 'contacts': contacts })


def show_contact(request, contact_id):
   
    # contact = Contacts.objects.get(id = contact_id)
    contact = get_object_or_404(Contacts, id=contact_id)

    if not contact.show:
        raise Http404()

    return render(request, 'contacts/show_contact.html', {
        'contact': contact
    })
