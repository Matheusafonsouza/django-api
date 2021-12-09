from django.contrib import admin

from client.models import Client


class Clients(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'cpf', 'rg', 'phone', 'active')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('active',)
    list_editable = ('active',)
    list_per_page = 20


admin.site.register(Client, Clients)
