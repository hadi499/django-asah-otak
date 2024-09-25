from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', include('quiz.urls')),
    path('admin/', admin.site.urls),
    path('easy/', include('easy.urls')),
    path('medium/', include('medium.urls')),  
    path('hard/', include('hard.urls')),  
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]


urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
