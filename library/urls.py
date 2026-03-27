from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    
    path('register/', views.register, name='register'),  
    path('home/', views.home, name='home'),
    
    path('mybooks/', views.my_books, name='mybooks'),    
    
    path('search/', views.search, name='search'),
    path('issue/<int:item_id>/', views.issue_item, name='issue'),
    path('return/<int:trans_id>/', views.return_item, name='return'),
    path('pay/<int:trans_id>/', views.pay_fine, name='pay'),
]