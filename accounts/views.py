from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import FormContato
# Create your views here.
def cadastro(request):

    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')
    

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email =  request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha =  request.POST.get('senha')
    retrysenha =  request.POST.get('retrysenha')

    if not nome or not sobrenome or not email or  not usuario or not senha or not retrysenha:
        messages.error(request, 'Os campos não podem ser vazios!')
        return render(request, 'accounts/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email invalido!')
        return render(request, 'accounts/cadastro.html')
    
    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais!')
        return render(request, 'accounts/cadastro.html')

    if senha != retrysenha:
        messages.error(request, 'senha não são iguais!')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(username = usuario).exists():
        messages.error(request, 'Usuário ja cadastrado!')
        return render(request, 'accounts/cadastro.html')


    if User.objects.filter(email = email).exists():
        messages.error(request, 'Email ja cadastrado!')
        return render(request, 'accounts/cadastro.html')

    user =  User.objects.create_user(
        username=usuario,
        email=email,
        password=senha,
        first_name= nome,
        last_name = sobrenome
    )

    if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                password='123456'
            )
        

    user.save()
    messages.success(request, 'Dados cadastrados com sucesso!')
    return redirect('login')


def login(request):  
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')


    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuario ou senha invalidos.')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login realizado com sucesso.')
        return redirect('dashboard')



def logout(request):
    auth.logout(request)
    return redirect('index')


    
@login_required(redirect_field_name='login')
def dashboard(request):

    if request.method != 'POST':
        form =  FormContato()
        return render(request, 'accounts/dashboard.html', {'form': form })
    
    form = FormContato(request.POST)

    if not form.is_valid():
        messages.error(request, 'erro ao enviar formulario, verifique se so dados foram preenchidos corretamente.')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form })

    form.save()
    messages.success(request, f'Contato {request.POST.get("nome")} salvo com sucesso')
    return redirect('dashboard')
        