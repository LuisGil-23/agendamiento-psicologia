from django.urls import path
from . import views

app_name = 'ui_frontend'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('psicologas/', views.psicologas_list_view, name='psicologas_list'),
    path('citas/', views.citas_list_view, name='citas_list'),
]
