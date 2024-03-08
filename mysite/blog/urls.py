from django.urls import path, include
from .views import PostView

urlpatterns = [
    path('', PostView.as_view(), name='home'),  # Rota vazia para redirecionar para hello/
    path('hello/', PostView.as_view(), name='hello_world'),
]