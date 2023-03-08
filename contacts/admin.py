from django.contrib import admin
from .models import Contacts, Category

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'phone', 'mail', 'creation_date', 'show')

    list_display_links = ('id', 'name', 'surname')

    # list_filter = ('name', 'surname')

    list_per_page = 10

    search_fields = ('name', 'id', 'creation_date')

    list_editable = ('phone', 'show')

    

admin.site.register(Category)
admin.site.register(Contacts, ContactAdmin)