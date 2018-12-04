from django.urls import path
from . import views as views_core
urlpatterns = [
    path('', views_core.home, name='home'),
    path('about/', views_core.about, name='about'),

    path('store/', views_core.store, name='store'),
    path('contact/', views_core.contact, name='contact'),



]