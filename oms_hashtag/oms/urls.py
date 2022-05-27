from django.urls import path
from . import views


urlpatterns = [

    path('users/register/', views.register_user, name='register'),

    path('users/profile/', views.get_user_profile, name="user-profile"),
    path('users/', views.get_users, name="users"),
    path('users/<str:pk>/', views.get_user_by_id, name="user"),

    path('products/', views.get_products, name="products"),
    path('products/<str:pk>/', views.get_product, name="product"),

    path('orders/add/', views.add_order_items, name='orders-add'),
    path('orders/', views.get_orders, name='orders'),
    path('orders/<str:pk>/', views.get_order_by_id, name='order'),

]
