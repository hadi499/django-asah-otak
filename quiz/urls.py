from django.urls import path
from .views import *



urlpatterns = [
    path('', home_view, name='home'), 
    path('results/', result_all, name='result-all'),
    path('results/easy', result_all_easy, name='result-all-easy'), 
    path('results/medium', result_all_medium, name='result-all-medium'), 
    path('results/hard', result_all_hard, name='result-all-hard'), 
    path('results/easy/delete', delete_results_easy, name='delete-all-easy'), 
    path('results/medium/delete', delete_results_medium, name='delete-all-medium'), 
    path('results/hard/delete', delete_results_hard, name='delete-all-hard'), 
   
   
    
    
]
