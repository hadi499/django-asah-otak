from django.urls import path
from .views import *

urlpatterns = [
    path('', main_easy_view, name="main-easy-view"),
    path('results/', result_easy, name="result-easy-view"),
    path('results/delete/', delete_results_easy, name="delete-results-easy"),
    path('<pk>/', easy_view, name='easy-view'),
    path('<pk>/data/', easy_data_view, name='easy-data-view'),
    path('<pk>/save/', save_easy_view, name='save-easy-view'),
]
