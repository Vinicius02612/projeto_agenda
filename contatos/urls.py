from django.urls import path
from . import views

# rota da pagina de lista de contados
urlpatterns = [
    path('', views.index, name='index'),
]