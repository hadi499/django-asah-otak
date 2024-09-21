from django.urls import path
from .views import *

urlpatterns = [
    path('', buka_word, name='buka'),
]
