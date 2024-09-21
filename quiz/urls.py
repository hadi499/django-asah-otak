from django.urls import path
from .views import *
from easy.views import *
from medium.views import *


urlpatterns = [
    path('', home_view, name='home'),
    path('easy/', main_easy_view, name="main-easy-view"),
    path('medium/', main_medium_view, name="main-medium-view"),
    path('results/', results_view, name='results-view'),  
    # path('easy/results/', result_easy, name='result-easy'),  
    path('easy/<pk>/', easy_view, name='easy-view'),
    path('medium/<pk>/', medium_view, name='medium-view'),
    path('easy/<pk>/data/', easy_data_view, name='data-easy-view'),
    path('medium/<pk>/data/', medium_data_view, name='medium-data-view'),
    path('easy/<pk>/save/', save_easy_view, name='save-easy-view'),
    path('medium/<pk>/save/', save_medium_view, name='save-medium-view'),
]
