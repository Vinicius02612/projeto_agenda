from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Contato
from django.core.paginator import Paginator
# Create your views here.

def index(request):

    """
        Passando dados que vem da model Contato.

        Para passar os dados que vem de models contato é necessário
        criar um dincionário passando um chave nesse caso 'cont' e um valor 'contato'
        que contem todos os dados que vem de contato, dessa forma será possivel fazer com que os dados apareçam no front.
        Contato.objects.all() é semelhante ao SELECT *FROM contatos do SQL
    """
    contato = Contato.objects.all()
    paginas = Paginator(contato, 5)
    page = request.GET.get('p')
    contato = paginas.get_page(page)
    return render(request, 'contatos/index.html', {
        'cont': contato
    })

def ver_contato(request, id_contato):
    """
        Metodo que pega um um contato da tabela contato pelo id 
        
        Contato.objects.get(id = id_contato) pega apenas um dado, nesse caso o id da contato
    """
#    contato = Contato.objects.get(id = id_contato)
    contato = get_object_or_404(Contato, id = id_contato)

    return render(request, 'contatos/ver_contato.html',{
        'cont': contato
    })





# uma das maneiras diferentes de tratar erros 

'''
def ver_contato(request, id_contato):
    """
        Metodo que pega um um contato da tabela contato pelo id 
        
        Contato.objects.get(id = id_contato) pega apenas um dado, nesse caso o id da contato
    """
    # tenta entrar na requisição da pagina de contatos, caso não encontra, mostra o erro 404
    try:
        contato = Contato.objects.get(id = id_contato)

        return render(request, 'contatos/ver_contato.html',{
            'cont': contato
        })
    except Contato.DoesNotExist as e:
        raise Http404()


'''

