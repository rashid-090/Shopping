from django.urls import path
from . import views

urlpatterns = [
    path('cartDetails',views.cart_details,name='cartDetails'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    path('cart_decrease/<int:product_id>/',views.min_cart,name='cart_decrement'),
    path('remove/<int:product_id>/',views.cart_delete,name='cartdelete'),
    path('orders/',views.Orders,name='orders'),
    
]