from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
# Create your views here.

def index(request):

    """
        Passando dados que vem da model Contato.

        Para passar os dados que vem de models contato é necessário
        criar um dincionário passando um chave nesse caso 'cont' e um valor 'contato'
        que contem todos os dados que vem de contato, dessa forma será possivel fazer com que os dados apareçam no front.
        Contato.objects.all() é semelhante ao SELECT *FROM contatos do SQL
    """

   

    contato = Contato.objects.order_by('-id').filter(mostrar =True) #order_by('-id')ordena os dados de pelo id de forma decrescente, filter(mostrar = True) retorna somente os dados com os campos marcados como mostrar
    paginas = Paginator(contato, 5)
    page = request.GET.get('p')
    contato = paginas.get_page(page)
    return render(request, 'contatos/index.html', {
        'cont': contato
    })

def ver_contato(request, id_contato):
    """
        Metodo que pega  um contato da tabela contato pelo id 
        
        Contato.objects.get(id = id_contato) pega apenas um dado, nesse caso o id da contato
    """
#    contato = Contato.objects.get(id = id_contato)
    contato = get_object_or_404(Contato, id = id_contato)

    if not contato.mostrar: # verifico se o campo mostrar esta setado com falso, caso sim ele o usuario não pode acessar a pagina
        raise Http404()

    # caso o contato esteja marcado para mostrar então ele redenriza as o contato  da pessoa
    return render(request, 'contatos/ver_contato.html',{
        'cont': contato
    })



def busca(request):

    termo = request.GET.get('termo')

    
    if termo is None or not termo: # se o campo de pesquisa estiver vazio ou não for encontrado nenhum dado retorna uma pagina 404
        messages.add_message(request, messages.ERROR, 'Campo busca não pode ser vazio.')
        return redirect('index')

    campo = Concat('nome', Value(' '), 'sobrenome')

    contato = Contato.objects.annotate(
        nome_completo = campo
    ).filter(
        Q(nome_completo__icontains = termo)| Q(telefone__icontains=termo)
    )

    
    """ 
    contato = Contato.objects.order_by('-id').filter(
        
        Q(nome__icontains = termo) | Q(sobrenome__icontains = termo),
        mostrar =True,
    ) """
     #order_by('-id')ordena os dados de pelo id de forma decrescente, filter(mostrar = True) retorna somente os dados com os campos marcados como mostrar
    paginas = Paginator(contato, 5)
    page = request.GET.get('p')
    contato = paginas.get_page(page)
    return render(request, 'contatos/busca.html', {
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

