from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.showChat, name="Show chat"),
    path('messages/send', views.sendMessage, name="Send Message"),
    path('messages/', views.getAllMessageByReceiverId, name='get_receiver_messages'),
    path('messages/list', views.getChatList, name="Get Chat List")
]
