from django.contrib import admin

from .models import Categoria, Contato
# Register your models here.


class ContatoAdmin(admin.ModelAdmin):

    # mostra todos os campos da tabela contato
    list_display = ('id','nome', 'sobrenome','telefone', 'email', 'descricao','categoria','mostrar')

    # torna apenas os campo id e nome clicaveis(links)
    list_display_links = ('id', 'nome')

    #cria campo de busca
    search_fields = ('id', 'nome', 'sobrenome', 'email')

    #campos que podem ser editaveis
    list_editable = ('telefone', 'mostrar')

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
