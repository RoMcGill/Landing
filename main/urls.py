from django.urls import path
from .views import home
from .views import about
from .views import getStarted

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('get-started/', getStarted, name='get-started'),
]
