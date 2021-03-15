from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get' : 'list',
        'post' : 'create'
    })),
    path('products/<str: pk>', ProductViewSet.as_view({
        'get' : 'list',
        'put' : 'update',
        'delete' : 'destroy'
    })),
]
