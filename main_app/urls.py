from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.ItemCreate.as_view(), name='items_create'),
    path('<int:pk>/delete/', views.ItemDelete.as_view(), name='items_delete'),
]