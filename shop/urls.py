from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='product_category'),
    path('<slug:c_slug>/<slug:product_slug>',views.ProductDetails,name='item_details'),
    path('search',views.Searching,name='search'),
    

]