from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/resultados/', views.resultados, name='resultados'),
    path('<int:post_id>/likes/', views.likes, name='likes'),
]