from django.urls import path

from . import views

app_name = 'shopping'
urlpatterns = [
    path('add/', views.add_product, name='add_product'),
    path('clear-add/', views.clear_add, name='clear_add'),
    path('minus/', views.minus_product, name='minus_product'),
    path('show/', views.show_cart, name='show_cart'),
]