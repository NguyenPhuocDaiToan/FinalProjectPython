from django.urls import path

from .admin.views import index
from .users.views import authenticate
from .users.views import home
from .users.views import about

urlpatterns = [
    path('', home.index, name='index'),
    path('about/', about.get, name='about'),
    path('login/', authenticate.login, name='login'),
    path('register/', authenticate.register, name='register'),
    path('admin/', index.index, name='admin'),
]