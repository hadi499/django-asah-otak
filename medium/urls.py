from django.urls import path
from .views import *

urlpatterns = [
    path('', main_medium_view, name="main-medium-view"), 
     path('results/', result_medium, name="result-medium-view"),
    path('results/delete/', delete_results_medium, name="delete-results-medium"),
    path('<pk>/', medium_view, name='medium-view'),
    path('<pk>/data/', medium_data_view, name='medium-data-view'),
    path('<pk>/save/', save_medium_view, name='save-medium-view'),
]
