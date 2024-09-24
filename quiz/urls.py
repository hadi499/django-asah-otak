from django.urls import path
from .views import *



urlpatterns = [
    path('', home_view, name='home'), 
    path('results/', result_all, name='result-all'), 
    path('quiz/results/delete/', delete_results_all, name='delete-results-all'),  
    
    
]
