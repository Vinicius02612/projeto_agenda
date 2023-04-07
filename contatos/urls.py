from django.urls import path
from . import views

# rota da pagina de lista de contados
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_contato>', views.ver_contato, name='ver_contato'),
    path('busca/', views.busca, name='busca'),


]