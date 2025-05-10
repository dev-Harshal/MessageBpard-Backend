from django.urls import path
from users import views

urlpatterns = [
    path('create/', views.UserCreateView().as_view(), name="user-create"),
    path('profile/', views.UserProfileView().as_view(), name="user-profile"),
    path('@<str:username>/', views.UserDetailsView().as_view(), name="user-details"),
]
