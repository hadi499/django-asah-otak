from django.urls import path
from .views import *

urlpatterns = [
    path('', main_hard_view, name="main-hard-view"), 
     path('results/', result_hard, name="result-hard-view"),
    path('results/delete/', delete_results_hard, name="delete-results-hard"),
    path('<pk>/', hard_view, name='hard-view'),
    path('<pk>/data/', hard_data_view, name='hard-data-view'),
    path('<pk>/save/', save_hard_view, name='save-hard-view'),
]
