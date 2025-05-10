from django.urls import path
from messenger import views

urlpatterns = [
    path('messages/', views.MessageView().as_view(), name="messages"),
    path('message/<int:pk>/', views.MessageDetailsView().as_view(), name="message-details"),
]
