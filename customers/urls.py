from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('customers/<str:pk>/', views.customers ,name="customer"),
    path('product/', views.products, name="product"),
    path('login/', views.loginPage, name="loginPage"),
    path('createOrder/', views.createOrder_form ,name="create-order"),
    path('updateOrder/<str:pk>', views.updateOrder ,name="update-order"),
    path('deleteOrder/<str:pk>', views.deleteOrder ,name="delete-order"),
    path('createCustomer/', views.createCustomer_form ,name="create-customer"),
    path('updateCustomer/<str:pk>', views.updateCustomer ,name="update-customer"),
    path('createProduct/', views.createProduct_form ,name="create-product"),
    path('register/', views.register, name="register"),
    path('logout/', views.logoutPage, name="logoutPage"),
    path('customer/', views.customer, name="customer"),
    path('deleteCustomer/<str:pk>', views.deleteCustomer, name="deleteCustomer"),
    path('updateProduct/<str:pk>', views.updateProducts, name="update-Product"),
    path('deleteProduct/<str:pk>', views.deleteProduct, name="delete-Product"),
    path('user/', views.userPage, name="user-page"),
    
   ]
