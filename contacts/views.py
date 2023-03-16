from django.shortcuts import render, get_object_or_404
from django.db.models.functions import Concat
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.contrib import messages
from django.http import Http404
from .models import Contacts

# Create your views here.
def index(request):

    messages.add_message(request, messages.ERROR, 'DEU RUIM MERMÃO')

    # contacts = Contacts.objects.all() => semelhante a consulta all em SQL
    contacts = Contacts.objects.order_by('category').filter(
        show = True
    ) # => Ordenação por ordem decrescente ID
    paginator = Paginator(contacts, 10)

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


def search(request):

    word = request.GET.get('word')

    if word is None or not word:
        raise Http404()

    field = Concat('name', Value(' '), 'surname')

    contacts = Contacts.objects.annotate(full_name = field).filter(Q(full_name__icontains = word) | Q(phone__icontains = word))

    # icotains => se tem parte do texto 
    # Busca
    # contacts = Contacts.objects.order_by('-id').filter(
    #     Q(name__icontains = word) | Q(surname__icontains = word),
    #     show = True
    #   )
    #  => o Q faz buscas mais especifícas e o | significa "ou"

    paginator = Paginator(contacts, 3)

    page = request.GET.get('p')
    contacts = paginator.get_page(page)

    return render(request, 'contacts/search.html', { 'contacts': contacts })

