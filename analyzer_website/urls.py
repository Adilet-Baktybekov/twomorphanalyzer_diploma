from django.urls import path
from analyzer_website import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('analyzer', views.analyzer, name='analyzer'),
    path('analyzer2', views.analyzer2, name='analyzer2'),
    path('validate', views.validate, name='validate'),
    path('validate2', views.validate2, name='validate2'),
    path('validate3', views.validate3, name='validate3')
]
