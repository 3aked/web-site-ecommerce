from django.urls import path
from . import views 

urlpatterns = [
        #Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('loginpage/', views.loginpage, name="loginpage"),
	path('logout/', views.logoutUser, name="logout"),
	path('register/', views.register, name="register"),
	path('success/', views.success, name="success"),
	path('emailregister/', views.emailregister, name="emailregister"),

	path('update_customer/', views.update_customer, name="update_customer"),


]