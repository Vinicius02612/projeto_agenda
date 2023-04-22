from django.urls import path
from . import views

# rota da pagina de lista de contados
urlpatterns = [
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('dashboard/', views.dashboard, name='dashboard'),
]