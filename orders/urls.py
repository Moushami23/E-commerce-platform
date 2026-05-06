from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.payment_method, name='payment_method'),
    path('card/', views.card_payment, name='card_payment'),
    path('complete/', views.complete_order, name='complete_order'),
    path('success/<int:order_id>/', views.order_success, name='order_success'),

]
