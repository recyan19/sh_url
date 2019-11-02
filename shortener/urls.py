from django.urls import path

from shortener import views


app_name = 'shortener'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:url_id>/', views.get_original_url, name='get_origin'),
]