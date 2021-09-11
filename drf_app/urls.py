from django.urls import path
from .views import ThingsList, ThingsDetail

urlpatterns = [
    path('', ThingsList.as_view(), name='Things_list'),
    path('<int:pk>/', ThingsDetail.as_view(), name='Things_detail')
]