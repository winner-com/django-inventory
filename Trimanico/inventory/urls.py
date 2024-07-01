from django.urls import path
from .import views

urlpatterns=[
    path('',views.home, name="hone"),
    path('inventory/',views.inventory, name="inventory" ),
]