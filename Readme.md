# Projeto Agenda


Este projeto tem como finalidade colocar em prática os conhecimentos adquiridos no curso de Python do Framework Web Django.

O projeto consistem um cadastro de agenda de contatos, onde é possivel adicionar contatos de pessoas que pertencem a uma determinada contegoria, como Famili, Amigos e Trabalho.

## Funcionalidades

<ol>
    <li>Cadastrar um contato</li>
    <li>Cadastrar Usuarios ADMIN</li>
    <li>Lista os contatos salvos</li>
    <li>remover - (não adicionada)</li>
    <li>Painel Administrativo, onde somente usários cadastrados podem adicionar novos contatos</li>
</ol>

## Como executar o projeto ?

<span>Obs:  O projeto esta hospedado no enderoço :<a>http://13.58.154.141/</a>, caso faça alguma alteração, crie uma nova branch e faça as alterações.</span> <br>
1 -  Faça o clone do projeto:

         git clone https://github.com/Vinicius02612/projeto_agenda.git 

2 - Para o rodar o projeto é necessário criar ter instalado na sua máquina o <a href="https://www.python.org/">Python</a>
e o framwork <a href="https://www.djangoproject.com/">Django</a>;

3 - Para rodar a aplicação na sua máquina primeiro digite os seguintes comando:

    python3 manage.py makemigrations 

    em seguida:

    python3 manage.py migrate

4 - Por fim rode o camando:

    python3 manage.py runserver
