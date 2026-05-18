from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('post/<int:post_id>/', views.detalhe_post, name='detalhe_post'),
    path('perfil/<str:username>/', views.perfil_utilizador, name='perfil_utilizador'),
    path('like/<int:post_id>/', views.dar_like, name='dar_like'),
]