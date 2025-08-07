from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name = "review_list"),
    path('review/', views.add_review, name = "add_review"),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register')
]
