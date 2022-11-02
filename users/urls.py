from django.urls import path
from . import views

urlpatterns = [
    path('user_profile/', views.UserAccountView.as_view(), name='account'),
    path('user_profile/create/', views.UserUpdateView.as_view(), name='account_create'),
    path("register/", views.UserCreateView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('interests/', views.InterestsListView.as_view(), name='interests'),
    path('remove/', views.RemoveNewsAccount.as_view(), name="remove"),
    path('filter/', views.FilterNewsInterestsTView.as_view(), name='filter'),
    path('newsletter/', views.NewsletterView.as_view(), name='newsletter'),

]
